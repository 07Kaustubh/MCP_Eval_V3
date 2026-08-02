#!/usr/bin/env python3
"""
Usage:
    python Validators/check_pipeline_wiring.py [--task <task_dir>]

Audits the pipeline's own internal wiring: do the paths, scripts, flags and phases that the
docs and runbooks cite actually exist, and does every validator import and run.

Why this exists
---------------
The pipeline is ~34 validators, 16 runbooks and a dozen reference docs that cite each other
by name. Nothing verified those citations. A runbook can tell an operator to run a script
with a flag the script never had, or to read a file that was renamed, and the only way to
find out was to hit it mid-phase. This is the same class of defect as every other one found
in this repo: a claim in prose that nothing checks.

Checks
------
W1  file paths cited in AGENTS.md / Reference/**.md resolve on disk
W2  scripts cited in runbooks exist under Validators/
W3  CLI flags cited for each script exist in that script's argument parser
W4  --phase values cited for validate.py exist in its phase list
W5  every validator imports cleanly (syntax + import-time errors)
W6  cross-validator symbol references resolve (from X import Y)
W7  every validator declares a usage/CLI entry point
W8  validators referenced in AGENTS.md's registry exist, and vice versa
W9  no validator is both un-imported and undocumented (orphan)
W10 rubric-category canonicalisation has exactly one implementation
W11 the tool head-segment vocabulary is non-empty (phantom detection fails closed)
W12 docs asserting a universe COUNT agree with the registry (CHANGELOG exempt)
W13 no tracked pipeline file embeds a machine-local home path

Exit 0 clean, 1 when any check fails.
"""

import argparse
import ast
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VDIR = ROOT / "Validators"

# QUICK_START.md was absent here, which is why it sat at "four universes / v20" through
# the whole HarmonyGames integration with no gate noticing. It is a LIVE operator doc and
# must stay accurate. CHANGELOG.md is deliberately NOT scanned: it is append-only history,
# so it legitimately names modules that were later deleted - v21.3 records removing a
# stale detection-module reference, and scanning history for live paths flagged it 8 times.
DOC_GLOBS = ["AGENTS.md", "QUICK_START.md",
             "Reference/*.md", "Reference/Sessions/*.md"]

# path-shaped tokens inside backticks
PATH_RE = re.compile(r"`([A-Za-z0-9_][A-Za-z0-9_./*-]*\.(?:py|md|json|txt|sql|sh))`")
SCRIPT_RE = re.compile(r"(?:python3?\s+)?Validators/([A-Za-z0-9_]+\.py)((?:\s+--?[a-z-]+)*)")
FLAG_RE = re.compile(r"--([a-z][a-z0-9-]*)")
PHASE_RE = re.compile(r"--phase\s+\{?([a-z_|\s]+)\}?")


def docs():
    out = []
    for g in DOC_GLOBS:
        out.extend(sorted(ROOT.glob(g)))
    return out


def check_unread_locals() -> list:
    """W14: a local assigned from the capability registry and never read.

    Added because three separate flags were "wired" by assigning them to a local that
    nothing subsequently read - `_oe_grammar`, `_target`, and a `severity_for` helper that
    had no call site. Each looked consumed to a grep and enforced nothing. The existing
    dead-code check only looked for uncalled `def`s, so it reported clean all three times
    and only manual review caught them.

    Scope is deliberately narrow: assignments whose right-hand side mentions
    get_framework_profile or get_universe_constants. Those are the ones that claim to make
    a registry flag load-bearing, so a false positive elsewhere cannot make this noisy.
    """
    import ast
    issues = []
    root = Path(__file__).resolve().parent.parent
    for f in sorted((root / "Validators").glob("*.py")):
        if f.name == Path(__file__).name:
            continue
        try:
            tree = ast.parse(f.read_text(encoding="utf-8", errors="ignore"))
        except SyntaxError:
            continue
        for fn in [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]:
            assigned = {}
            for node in ast.walk(fn):
                if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                        and isinstance(node.targets[0], ast.Name):
                    rhs = ast.dump(node.value)
                    if "get_framework_profile" in rhs or "get_universe_constants" in rhs:
                        assigned[node.targets[0].id] = node.lineno
            if not assigned:
                continue
            read = {n.id for n in ast.walk(fn) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}
            for name, line in sorted(assigned.items()):
                if name not in read:
                    issues.append(
                        f"  [W14] {f.name}:{line} `{name}` is assigned from the registry in "
                        f"`{fn.name}` and never read - the flag it reads enforces nothing"
                    )
    return issues


def check_universe_parity() -> list:
    """W15: a runbook that names SOME universes must name ALL of them.

    Added because the "5th arm" was applied to ~20 prose files by hand and measurement
    afterwards found 6 of 16 runbooks still naming only a subset. Hand-editing N
    near-identical documents does not converge, and nothing detected the gap: a runbook
    that routes on universe but omits one silently sends that universe down another's path.

    Scope is deliberately narrow. A file that names NO universe is universe-generic and is
    left alone; only a file that already routes by universe is required to be complete.
    That keeps the check from demanding boilerplate in files that legitimately do not care.
    """
    issues = []
    root = Path(__file__).resolve().parent.parent
    try:
        sys.path.insert(0, str(root / "Validators"))
        from universes import UNIVERSES
        names = sorted(UNIVERSES)
    except Exception:
        return []
    for f in sorted((root / "Reference").rglob("*.md")):
        text = f.read_text(encoding="utf-8", errors="ignore").lower()
        present = [n for n in names if n in text]
        # A file naming exactly ONE universe is calling out an exception ("HarmonyGames
        # differs because..."), which is legitimate and complete on its own. A file naming
        # TWO OR MORE is maintaining a routing table, and an incomplete routing table
        # silently sends the omitted universe down another's path. Only the latter is a
        # defect; flagging the former would demand four paragraphs of boilerplate in files
        # that correctly do not care.
        if len(present) < 2 or len(present) == len(names):
            continue
        missing = [n for n in names if n not in present]
        rel = f.relative_to(root)
        issues.append(
            f"  [W15] {rel} routes by universe but never names: {', '.join(missing)}"
        )
    return issues


def check_code_comment_citations() -> list:
    """W13: a path cited inside a Validators/*.py comment must resolve.

    Added because a comment in `detect_universe` cited
    `Validators/test_signal_exclusivity.py` as the authority for its correctness while that
    file did not exist, and this auditor reported 0 errors because it only read prose docs.
    A dangling citation inside the function whose correctness it is supposed to establish is
    exactly the failure hard rule 30 exists to prevent.
    """
    import re
    issues = []
    root = Path(__file__).resolve().parent.parent
    cite = re.compile(r"(Validators/[A-Za-z0-9_./-]+\.py)")
    for f in sorted((root / "Validators").glob("*.py")):
        for i, line in enumerate(f.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            st = line.strip()
            if not (st.startswith("#") or '"""' in line or st.startswith("*")):
                continue
            for m in cite.finditer(line):
                if not (root / m.group(1)).exists():
                    issues.append(f"  [W13] {f.name}:{i} cites {m.group(1)}, which does not exist")
    return issues


def check_orphan_validators() -> list:
    """W9: a validator nothing imports AND no doc mentions is dead weight or a lost wiring.

    Doc-referenced-but-never-imported is normal and NOT reported: most validators are CLI
    entry points invoked by a runbook, not libraries. Only the intersection is suspicious.
    """
    out = []
    mods = sorted(p.stem for p in VDIR.glob("*.py") if p.stem != "__init__")
    pys = [q for q in ROOT.rglob("*.py") if "__pycache__" not in str(q)]
    mds = list(ROOT.rglob("*.md"))
    for m in mods:
        imported = any(re.search(rf"\b(?:import\s+{re.escape(m)}\b|from\s+{re.escape(m)}\s+import)",
                                 q.read_text(encoding="utf-8", errors="ignore"))
                       for q in pys if q.stem != m)
        if imported:
            continue
        mentioned = any(re.search(rf"\b{re.escape(m)}\.py\b", q.read_text(encoding="utf-8", errors="ignore"))
                        for q in mds)
        if not mentioned:
            out.append(f"[W9] Validators/{m}.py is imported by nothing and mentioned in no doc - orphan")
    return out


def check_duplicated_logic() -> list:
    """W10: the rubric-category census must have exactly ONE implementation.

    validate.py and v4_gates.py each grew their own copy; they gate the SAME balance rules
    (Outcome-majority, or a Process<=40% cap), so drift between them is a scoring defect that
    no other gate would catch. The shared implementation lives in universes.py because
    validate.py imports v4_gates, which makes the reverse direction circular.
    """
    out = []
    needle = 'startswith(' + '"outcome")'      # split so this file is not its own match
    impls = [q.name for q in VDIR.glob("*.py")
             if q.name != Path(__file__).name
             and needle in q.read_text(encoding="utf-8", errors="ignore")]
    if len(impls) > 1:
        out.append("[W10] rubric-category canonicalisation is implemented in "
                   f"{len(impls)} modules ({', '.join(sorted(impls))}) - collapse to "
                   "universes.canonical_rubric_category")
    return out


def check_tool_vocab() -> list:
    """W11: the tool head-segment vocabulary must be non-empty.

    `_looks_like_tool_name` now fails closed, so an empty vocabulary would silently disable
    phantom-tool detection rather than loosen it. Either failure mode is a scoring defect, so
    the invariant is gated here instead of being assumed.
    """
    try:
        sys.path.insert(0, str(VDIR))
        from v4_gates import _tool_head_vocab
        n = len(_tool_head_vocab())
    except Exception as e:
        return [f"[W11] could not build the tool head-segment vocabulary: {e}"]
    return [] if n >= 20 else [f"[W11] tool head-segment vocabulary is {n} entries - expected 20+; "
                               "tool catalogues are probably unreadable, which silently disables "
                               "phantom-tool detection"]


def check_universe_count_claims() -> list:
    """W12: a doc asserting "N universes" must agree with the registry.

    CHANGELOG.md is exempt: it is append-only history, so an old entry saying "four
    universes" was true when written and must not be rewritten.
    """
    sys.path.insert(0, str(VDIR))
    from universes import UNIVERSES
    n = len(UNIVERSES)
    words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven"}
    expected = {str(n), words.get(n, "")}
    out = []
    for d in docs():
        if d.name == "CHANGELOG.md":
            continue
        txt = d.read_text(encoding="utf-8", errors="ignore")
        # "the other N universes" is RELATIVE phrasing and is correct when N == total - 1
        # (e.g. the HarmonyGames section saying "the other four universes" with 5 registered).
        # Accepting it blindly would hide a real defect: the StarPM section said "the other
        # three universes", which was right at 4 registered and wrong at 5.
        # The possessive form ("three universes' output") names a SUBSET, not a total, so
        # it is excluded by the lookahead above rather than being counted as a claim.
        rel = {str(n - 1), words.get(n - 1, "")}
        for m in re.finditer(r"(other\s+)?\b(one|two|three|four|five|six|seven|\d+)\s+universes\b(?!['\u2019])",
                             txt, re.I):
            is_rel = bool(m.group(1))
            val = m.group(2).lower()
            if (val in rel) if is_rel else (val in expected):
                continue
            if True:
                kind = "relative count should be " + str(n - 1) if is_rel else "should be " + str(n)
                out.append(f"[W12] {d.relative_to(ROOT)} claims '{m.group(0).strip()}' - {kind} "
                           f"({n} registered: {', '.join(sorted(UNIVERSES))})")
    return out


def check_absolute_paths() -> list:
    """W13: no tracked pipeline file may embed a machine-local home path.

    Two frozen baseline reports carried the author's absolute path. Report comparison is
    sha256 over the whole file, so `check_regression` reported 21/21 on the machine that
    froze it and "report drift" for every other user - a gate that only its author could
    pass. The hydration pointer had the same defect: it told a teammate to rsync from a
    directory that exists on one laptop.

    Agent session directories are excluded: they are machine-local by nature and the repo
    tracks them by convention.
    """
    import subprocess
    try:
        tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True,
                                 text=True, timeout=60).stdout.split()
    except Exception as e:
        return [f"[W13] could not list tracked files: {e}"]
    # Scope: PIPELINE-OWNED files only. QC_Tasks/** and Tasks/** are vendored platform data
    # and per-task outputs - their trajectory JSONs legitimately contain the agent sandbox's
    # own sandbox home paths (~300 of them), which are captured content, not ours.
    # The defect this guards is a pipeline artifact carrying its AUTHOR's home directory:
    # two frozen baseline reports did exactly that and made check_regression unpassable for
    # anyone else.
    pat = re.compile(r"/(?:Users|home)/[A-Za-z0-9._-]+/")
    owned = ("Validators/", "Reference/")
    out = []
    for rel in tracked:
        is_owned = rel.startswith(owned) or ("/" not in rel) or rel.endswith("README_HYDRATE.md")
        if not is_owned or not rel.endswith((".py", ".md", ".json", ".txt", ".out", ".sql")):
            continue
        f = ROOT / rel
        try:
            txt = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        m = pat.search(txt)
        if m:
            n = len(pat.findall(txt))
            out.append(f"[W13] {rel} embeds a machine-local path ({n}x, e.g. '{m.group(0)}') - "
                       "use a repo-relative path or a documented placeholder")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", default=None)
    args = ap.parse_args()

    fails, warns = [], []

    # ---------- W1 / W2 : cited paths + scripts resolve
    cited_scripts = set()
    for d in docs():
        txt = d.read_text(encoding="utf-8", errors="replace")
        rel = d.relative_to(ROOT)
        for m in PATH_RE.finditer(txt):
            tok = m.group(1)
            if "*" in tok or tok.startswith(("Docs", "Evals", "Tasks_Template")):
                continue  # glob or per-universe pattern
            # "TaskN..TaskM" is range shorthand and the real dirs carry a hex suffix
            # (QC_Tasks/V3_Tasks/Task11_6a2202b8.../Rubrics.json). Resolve the leaf name
            # under the parent glob instead of treating the literal string as a path.
            if ".." in tok:
                parts = tok.split("/")
                leaf = parts[-1]
                stem = "/".join(parts[:-2]) if len(parts) > 2 else ""
                base = ROOT / stem if stem else ROOT
                if base.is_dir() and any((d / leaf).is_file() for d in base.iterdir() if d.is_dir()):
                    continue
            # try a few plausible roots
            cands = [ROOT / tok, ROOT / "Validators" / tok, ROOT / "Reference" / tok]
            if tok.startswith("Tasks/") or "<TASK_DIR>" in tok:
                continue
            if not any(c.exists() for c in cands) and not list(ROOT.glob(f"**/{tok}"))[:1]:
                fails.append(f"[W1] {rel}: cites `{tok}` which does not exist")
        for m in SCRIPT_RE.finditer(txt):
            script, flagblob = m.group(1), m.group(2) or ""
            cited_scripts.add(script)
            if not (VDIR / script).is_file():
                fails.append(f"[W2] {rel}: cites Validators/{script} which does not exist")
                continue
            # ---------- W3 : cited flags exist in the script
            src = (VDIR / script).read_text(encoding="utf-8", errors="replace")
            for f in FLAG_RE.findall(flagblob):
                if f in ("help",):
                    continue
                if f"--{f}" not in src:
                    fails.append(f"[W3] {rel}: `Validators/{script} --{f}` but the script "
                                 f"declares no --{f}")
        # ---------- W4 : validate.py --phase values
        vsrc = (VDIR / "validate.py").read_text(encoding="utf-8", errors="replace")
        known = set(re.findall(r'"(prompt|oe|rubrics|all|injection|submission_gate)"', vsrc))
        for m in re.finditer(r"validate\.py[^\n]*--phase\s+([a-z_]+)", txt):
            ph = m.group(1)
            if ph not in known:
                fails.append(f"[W4] {rel}: cites validate.py --phase {ph}, not a known phase "
                             f"{sorted(known)}")

    # ---------- W5 : every validator imports cleanly
    for p in sorted(VDIR.glob("*.py")):
        try:
            ast.parse(p.read_text(encoding="utf-8", errors="replace"))
        except SyntaxError as e:
            fails.append(f"[W5] {p.name}: SyntaxError line {e.lineno}: {e.msg}")
            continue
        if p.name in ("test_regression_anchors.py",):
            continue
        spec = importlib.util.spec_from_file_location(f"_w5_{p.stem}", p)
        try:
            mod = importlib.util.module_from_spec(spec)
            sys.modules[spec.name] = mod
            spec.loader.exec_module(mod)
        except SystemExit:
            pass
        except Exception as e:
            fails.append(f"[W5] {p.name}: import-time {type(e).__name__}: {e}")

    # ---------- W6 : cross-validator symbol references resolve
    for p in sorted(VDIR.glob("*.py")):
        try:
            tree = ast.parse(p.read_text(encoding="utf-8", errors="replace"))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module:
                target = VDIR / f"{node.module.split('.')[-1]}.py"
                if not target.is_file():
                    continue
                tsrc = target.read_text(encoding="utf-8", errors="replace")
                try:
                    ttree = ast.parse(tsrc)
                except SyntaxError:
                    continue
                defined = {n.name for n in ast.walk(ttree)
                           if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}
                defined |= {t.id for n in ast.walk(ttree) if isinstance(n, ast.Assign)
                            for t in n.targets if isinstance(t, ast.Name)}
                for a in node.names:
                    if a.name != "*" and a.name not in defined:
                        fails.append(f"[W6] {p.name}: imports `{a.name}` from {target.name} "
                                     f"which does not define it")

    # ---------- W7 : CLI entry point
    for p in sorted(VDIR.glob("*.py")):
        src = p.read_text(encoding="utf-8", errors="replace")
        if p.name in ("universes.py", "v4_gates.py"):
            continue  # library modules by design
        if "__main__" not in src:
            warns.append(f"[W7] {p.name}: no __main__ entry point (library, or missing CLI?)")

    # ---------- W8 : AGENTS registry vs disk
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8", errors="replace")
    # registry tree uses ├── for members and └── for the last item in a group
    registered = set(re.findall(r"│\s+[├└]──\s+([a-z0-9_]+\.py)", agents))
    on_disk = {p.name for p in VDIR.glob("*.py")}
    for s in sorted(registered - on_disk):
        fails.append(f"[W8] AGENTS.md registers Validators/{s} which does not exist")
    for s in sorted(on_disk - registered):
        warns.append(f"[W8] Validators/{s} exists but is not in the AGENTS.md registry")

    # ---------- extra checks. These MUST run BEFORE the report: they were appended to
    # `fails`/`warns` AFTER the print loop, so their findings counted toward the exit
    # code and printed nowhere - the gate said '5 wiring error(s)' and listed none.
    # These three ran ONLY when `warns` was already non-empty, so on a clean run they were
    # silently skipped - the exact silent-no-op this auditor exists to catch.
    warns = (list(warns) + check_code_comment_citations() + check_unread_locals()
             + check_universe_parity() + check_orphan_validators())
    # W10 is a FAIL, not a warning: two live copies of the rubric-category census can drift
    # apart and silently mis-score the balance rules - exactly the defect class AGENTS.md
    # rule 18 says must become a standing gate instead of prose.
    fails = (list(fails) + check_duplicated_logic() + check_tool_vocab()
             + check_universe_count_claims() + check_absolute_paths())

    # ---------- report
    print("=== Pipeline wiring audit ===")
    print(f"{len(list(VDIR.glob('*.py')))} validators · {len(docs())} docs · "
          f"{len(cited_scripts)} scripts cited by docs\n")
    for f in fails:
        print(f"  {f}")
    if warns:
        print()
        for w in warns:
            print(f"  {w}")
    print()
    if fails:
        print(f"[FAIL] {len(fails)} wiring error(s), {len(warns)} warning(s)")
        return 1
    print(f"[OK] no wiring errors. {len(warns)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
