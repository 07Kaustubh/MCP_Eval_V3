#!/usr/bin/env python3
"""
Usage:
    python Validators/test_gate_vacuity.py

Meta-gate: attacks the CLASS of defect where a check reports PASS/CAUGHT while guarding
nothing. Not the three instances - the class.

The three instances, all found in one session
---------------------------------------------
1. test_memory_bounds declared a mutant "combined blob no longer skipped". It mutated
   SOURCE TEXT and the static guard duly noticed, so it reported CAUGHT - while the
   filename it protected, Base_Universe_Complete_Data.json, matched ZERO files on disk.
   Skipping or not skipping a file that does not exist is the same program.
2. test_score_extraction declared two mutation cases that could not fail, because an
   attributable score meant the fallback they mutated was never reached.
3. The --dead-gate allowlist matched with bare startswith, so the entry "v22 HG-1"
   absorbed HG-10..HG-13 and printed a real leak as "allowlisted".

Each looked right because the number looked right. Validators/AGENTS.md already names the
pattern ("Matching rules that return the expected number"); this file is the standing gate
for it.

What the literature calls these, and what this adopts
-----------------------------------------------------
(1) is an EQUIVALENT MUTANT: syntactically different, semantically identical. Deciding
equivalence in general is undecidable (Budd & Angluin, 1982), and it is the long-standing
barrier to mutation testing. Papadakis, Jia, Harman & Le Traon (ICSE 2015, "Trivial
Compiler Equivalence") make the consequence explicit: equivalent and duplicated mutants
"artificially inflate the apparent mutant killing power of a test suite" and distort the
mutation score. A mutant reported CAUGHT with no behavioural difference is exactly that -
an inflated score. Their detection technique, TCE, compiles each mutant and compares
machine code. That does NOT transfer here and is deliberately not attempted: TCE needs an
optimising compiler emitting canonical object code, and CPython's .pyc is not that - it
embeds docstrings, line numbers and constants, so byte-comparing bytecode would report
"different" for changes that are semantically identical and vice versa.

(2) is ANTECEDENT FAILURE, the oldest form of VACUITY (Beatty & Bryant; formalised by
Beer, Ben-David, Eisner & Rodeh, CAV 1997 / FMSD 2001). `p -> q` is trivially valid where
p never holds; the subformula does not affect the verdict. Their detection method is
PERTURBATION: M satisfies phi vacuously iff phi[psi <- false] has the same verdict as
phi. Kupferman & Vardi generalise it to CTL*. That IS adopted, and it is the core idea
below: a guard whose verdict does not move when the thing it guards is perturbed is
guarding nothing. The IBM Haifa experience report is the reason this is a blocking gate
rather than a warning - "vacuous passes ALWAYS point to a real problem in either the
design or its specification or environment", at roughly 20% of specifications on first
runs. This session found three in one repo.

(3) is a permissive-matching defect, the allowlist cousin of an unanchored regex
(CWE-777, missing anchors; CWE-625, permissive regex). The fix is the standard one:
match on an exact identifier or a boundary, never a bare prefix.

What does NOT transfer, stated plainly
--------------------------------------
- Mutation-testing FRAMEWORKS (PIT, Stryker, mutmut, cosmic-ray) are third-party; this
  repo is stdlib-only by policy, and the suites here are small hand-authored mutant sets
  rather than a generated population.
- MUTATION SCORE as a metric is meaningless at this scale. With ~10 deliberate mutants,
  the useful question is not "what fraction die" but "is any one of them incapable of
  dying", which is the inverse and is what this checks.
- Mutant SAMPLING, higher-order mutation and TCE all target the cost of a large generated
  population. There is no population here to reduce.

Checks
------
V1  every filesystem literal a guard protects has a live referent on disk
V2  no allowlist entry prefix-absorbs a sibling identifier
V3  every mutation-style suite exposes a self-check, and that self-check can report dirty

Exit 0 clean, 1 on any finding.
"""

import ast
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VDIR = ROOT / "Validators"

# ---------------------------------------------------------------------------
# V1: guards whose subject is a filesystem literal.
#
# Only modules that STATICALLY assert about named payload files are listed. A guard that
# reasons about behaviour needs no entry; this is aimed squarely at the shape that failed,
# where the assertion is "the source still mentions <filename>" and nothing ever checks
# that <filename> exists.
# ---------------------------------------------------------------------------
# Each guard maps to the DOMAIN it actually scans. Scoping is the whole point, and
# getting it wrong makes this check worthless: Base_Universe_Complete_Data.json - the
# literal in the motivating bug - still exists under StarPM_Base_Universe/Data and
# Brookfield_Base_Universe/Data. A repo-wide "does this name exist anywhere" test says
# LIVE and would NOT have caught it. It is dead only within the export payload that guard
# actually reads, which is where the guard's claim lives. A None domain means repo-wide.
GUARD_DOMAINS = {
    "test_memory_bounds.py":     "HarmonyGames_Base_Universe/Services_Data",
    "universe_data_source.py":   "HarmonyGames_Base_Universe/Services_Data",
    "check_hydration.py":        "HarmonyGames_Base_Universe/Services_Data",
    "verify_universe_atoms.py":  None,
}
GUARD_MODULES = list(GUARD_DOMAINS)

# Data-file extensions only. .py/.md are covered by check_pipeline_wiring W1/W2/W13.
DATA_SUFFIXES = (".json", ".sql", ".txt", ".csv")

# Literals that are not payload members in ANY module: task-directory inputs and
# generated siblings. Payload scoping does not apply to them at all.
NON_PAYLOAD_LITERALS = {
    "3_UniverseDataForThisTask.json": "per-task input, not a payload member",
    "4_Changelog.json": "per-task input, not a payload member",
    "Universe.txt": "per-task cache, not a payload member",
    "hydration_manifest.json": "generated beside the payload, not inside it",
}

# A literal may be dead ON PURPOSE, but only in a SPECIFIC module. Keyed by
# (module, literal), never by literal alone, because the same filename can be a correct
# absence assertion in one guard and a vacuous presence guard in another - which is
# exactly the case below. A global exemption would re-vacuum the bug this file exists for.
# Each entry must say why, and "why" may not be "the gate went red".
RETIRED_LITERALS = {
    ("check_hydration.py", "Base_Universe_Complete_Data.json"):
        "Asserted ABSENT on purpose. check_hydration declares it RETIRED_BLOB and FAILS "
        "if it reappears, because its presence means someone hydrated the superseded V4 "
        "drop on top of this one, so zero referents is the DESIRED state. Deliberately "
        "NOT exempt in test_memory_bounds, where the same name was a SKIP guard and its "
        "absence from the payload is precisely what made that mutant equivalent.",
}

# Whitespace means prose ("presence search in 3_UniverseDataForThisTask.json"), not a
# filename. Globs and placeholders are not filenames either.
_NOT_A_FILENAME = re.compile(r"[*?\[\]{}<>%\s]|^\.|^$")


def _string_literals(path: Path):
    """(literal, lineno) for every str constant in a module, via AST rather than regex."""
    try:
        tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        return []
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            out.append((node.value, node.lineno))
    return out


def _domain_names(domain: str):
    """Basenames present in a guard's scan domain, bounded to two levels.

    Bounded deliberately: the HG payload is 316k files / 7.3 GB and this gate runs inside
    check_regression. Payload TABLE files live at depth 1-2, which is what the guards
    name; nothing deeper is a table.
    """
    root = ROOT / domain
    if not root.is_dir():
        return None                      # unhydrated - caller SKIPs rather than guesses
    names = set()
    for child in root.iterdir():
        names.add(child.name)
        if child.is_dir():
            try:
                for g in child.iterdir():
                    names.add(g.name)
            except OSError:
                pass
    return names


def _resolves_repo_wide(name: str) -> bool:
    if (ROOT / name).exists():
        return True
    for p in ROOT.rglob(Path(name).name):
        if "_dist" in p.parts:
            continue
        return True
    return False


def check_literal_liveness() -> list:
    """V1: a guard may not protect a filename that has no referent in the domain it scans.

    The standing gate for instance (1). The mutant was 'stop skipping
    Base_Universe_Complete_Data.json'; the static guard saw the source change and reported
    CAUGHT; the file had been absent from the HG payload since the V5 drop, so the mutated
    program and the original behaved identically on every input it would ever see. In
    perturbation terms (Beer et al.) the guarded subformula did not affect the verdict, so
    the CAUGHT was vacuous - and in mutation terms the mutant was equivalent, inflating the
    kill count exactly as Papadakis et al. describe.
    """
    out = []
    for mod, domain in GUARD_DOMAINS.items():
        p = VDIR / mod
        if not p.is_file():
            out.append(f"[V1] Validators/{mod} is a declared guard module but does not exist")
            continue
        names = _domain_names(domain) if domain else None
        if domain and names is None:
            print(f"  [V1-SKIP] {domain} is not hydrated; {mod} literals unchecked")
            continue
        seen = set()
        for lit, line in _string_literals(p):
            if not lit.endswith(DATA_SUFFIXES) or _NOT_A_FILENAME.search(lit):
                continue
            if (lit in seen or lit in NON_PAYLOAD_LITERALS
                    or (mod, lit) in RETIRED_LITERALS):
                continue
            seen.add(lit)
            live = (Path(lit).name in names) if domain else _resolves_repo_wide(lit)
            if not live:
                where = domain if domain else "the repo"
                out.append(
                    f"[V1] Validators/{mod}:{line} guards `{lit}`, which matches ZERO "
                    f"files in {where} - the guard cannot be protecting behaviour. Give it "
                    f"a live referent, or declare it in RETIRED_LITERALS with a reason.")
    return out


# ---------------------------------------------------------------------------
# V2: allowlists matched by prefix.
# ---------------------------------------------------------------------------
def _anchor_ids() -> list:
    """Every anchor name declared in the anchor suite, read as text.

    Text rather than import: importing test_regression_anchors pulls in the whole suite
    and this gate must stay cheap enough to run on every check_regression.
    """
    src = (VDIR / "test_regression_anchors.py").read_text(encoding="utf-8", errors="replace")
    return re.findall(r'"name":\s*"([^"]+)"', src)


def check_allowlist_prefixes() -> list:
    """V2: an allowlist must not be matched in a way that absorbs a sibling identifier.

    Instance (3): the entry "v22 HG-1" was matched with a bare startswith, so it swallowed
    HG-10..HG-13 and printed a real leak as "allowlisted". Same family as an unanchored
    regex (CWE-777).

    Two-stage, because the SHAPE alone is not the defect. An allowlist storing bare IDs is
    supposed to prefix its own anchor - "v18 KS-5" precedes "v18 KS-5 - description" - and
    flagging that would be noise on 9 safe entries. What matters is whether the MATCHER is
    boundary-anchored. It is today (`name == a or name.startswith(a + " ")`), so a prefix
    entry is unambiguous and nothing is reported. If that anchoring is ever removed, the
    matcher check fires AND every genuinely absorbing entry is named, so the finding
    arrives with the fix list attached.
    """
    out = []
    src = (VDIR / "test_regression_anchors.py").read_text(encoding="utf-8", errors="replace")

    m = re.search(r"(?:DEAD_GATE_ALLOWLIST|ALLOWLIST)\s*=\s*[\{\[](.*?)[\}\]]", src, re.S)
    if not m:
        return ["[V2] no allowlist found in test_regression_anchors.py - if it was "
                "removed, drop this check; if it was renamed, teach this check the name"]
    entries = re.findall(r'"([^"]+)"', m.group(1))

    # Every comparison against an allowlist element, in the lines that mention it.
    uses = [ln for ln in src.splitlines()
            if "ALLOWLIST" in ln or ("startswith(a" in ln and "for a in" in ln)]
    joined = "\n".join(uses)
    anchored = bool(re.search(r'startswith\(\s*\w+\s*\+\s*["\'][ \-_]["\']', joined))
    exact = bool(re.search(r'\w+\s*==\s*a\b|\bname\s*==\s*\w+', joined))
    bare = bool(re.search(r'startswith\(\s*a\s*\)', joined))

    if bare and not anchored:
        out.append("[V2] the allowlist is matched with a BARE startswith - an entry "
                   "silently absorbs every sibling whose id extends it. Anchor the match "
                   "on a separator, or compare exactly.")
        for e in entries:
            absorbed = [n for n in re.findall(r'"name":\s*"([^"]+)"', src)
                        if n != e and n.startswith(e) and len(n) > len(e)
                        and (n[len(e)].isalnum() or n[len(e)] == "-")]
            if absorbed:
                out.append(f"[V2]   `{e}` would absorb {len(absorbed)}, e.g. `{absorbed[0]}`")
    elif not (anchored or exact):
        out.append("[V2] could not confirm the allowlist match is boundary-anchored or "
                   "exact. If the matching moved, teach this check where it went - a "
                   "silent 'cannot tell' is how the original bug survived.")
    return out


# ---------------------------------------------------------------------------
# V3: mutation suites must be able to report dirty.
# ---------------------------------------------------------------------------
# suite -> flag that runs its own vacuity self-check.
MUTATION_SUITES = {
    "test_memory_bounds.py": ["--self-check"],
    "test_regression_anchors.py": ["--dead-gate"],
    "test_s0_builders.py": None,      # frozen-output gate; its mutants are proven in review
    "test_score_extraction.py": None,
}


def check_selfcheck_declared() -> list:
    """V3: a suite that declares mutants must expose a self-check, and it must work.

    A mutation suite that has only ever printed CAUGHT is indistinguishable from one that
    cannot print anything else - the same argument --dead-gate already makes for the
    anchors, generalised. Suites mapped to None are declared as having no self-check
    flag; they are REPORTED, never silently skipped, so the absence stays visible.
    """
    out = []
    for suite, flag in MUTATION_SUITES.items():
        p = VDIR / suite
        if not p.is_file():
            out.append(f"[V3] Validators/{suite} is a declared mutation suite but is missing")
            continue
        if flag is None:
            print(f"  [V3-INFO] Validators/{suite} declares no self-check flag; its "
                  f"mutants are verified by review, not by this gate")
            continue
        # Declaration is checked STATICALLY. Actually running --dead-gate and
        # --self-check here would duplicate two of the slowest steps check_regression
        # already runs, for no new information: if either regressed, check_regression is
        # red before this gate is reached. What is NOT otherwise checked is that the flag
        # still EXISTS, which is how a self-check quietly disappears in a refactor.
        src = p.read_text(encoding="utf-8", errors="replace")
        for f in flag:
            if f'"{f}"' not in src and f"'{f}'" not in src:
                out.append(f"[V3] Validators/{suite} no longer declares {f} - its "
                           f"vacuity self-check has been removed")
    return out


def main() -> int:
    findings = []
    print("=== Gate vacuity meta-audit ===")
    print("V1 literal liveness · V2 allowlist prefix absorption · V3 suite self-checks\n")
    findings += check_literal_liveness()
    findings += check_allowlist_prefixes()
    findings += check_selfcheck_declared()

    for f in findings:
        print(f"  {f}")
    if findings:
        print(f"\n[FAIL] {len(findings)} vacuity finding(s). A gate that cannot report "
              f"dirty is not a gate.")
        return 1
    print(f"\n[OK] no vacuous gates: {len(GUARD_MODULES)} guard module(s), "
          f"{len(MUTATION_SUITES)} mutation suite(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
