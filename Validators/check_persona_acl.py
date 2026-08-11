#!/usr/bin/env python3
"""
Usage:
    python Validators/check_persona_acl.py <task_dir>

Persona ACL gate. Runs only for universes whose framework profile sets `acl_gate: true`
(today: HarmonyGames). SKIPs cleanly everywhere else.

Why this exists
---------------
HarmonyGames is the only universe with persona-scoped read visibility as a first-class
rule. Seven of its eleven services filter reads by acting identity; four are unscoped.
A read performed under the wrong identity is neither a pass nor a fail, it is an
`Excluded` execution, which is a third trajectory disposition the other four universes do
not have.

Two properties are mechanically checkable from the authored artifacts alone, without
trajectories, and both are cheap to get wrong:

ACL-1  The persona named in `2_Persona.txt` must resolve to exactly one roster entry.
       V5 REGULARISED HarmonyGames persona emails to `firstname.lastname@`, so the pre-V5
       spellings this note used to teach (`blake@`, `jlawson@`, `leonard@`) now match ZERO
       rows in the payload. An older copy of this paragraph asserted the exact inverse - that
       `arthur.blake@harmonygames.co` "names a persona that does not exist" - and it is the
       real address. Docs 14 still says never construct, normalize or infer an email from a
       name, and that still bites: `douglas` and `robert` are single-token keys mapping to
       `douglas@` / `robert@`, so even a mechanical `firstname.lastname@` rule breaks on 2
       of the 17. Resolve from the roster, always.

ACL-2  A deliverable may not require a WRITE to a service the universe cannot write.
       Gmail here is read-only across all 27 tools: no send, no reply, no compose, not
       even a draft. "Email the vendor" is not an available action, so a rubric requiring
       one can never pass, which is an all-failing criterion by construction rather than
       by difficulty.

ACL-3  The registry's ACL sets must equal the ones the spec doc's Access matrix declares.
       Evals_harmonygames/1_Prompt_Eval.md instructs at :14, :42, :99 and :432 that the
       scoped set be derived live, and :99 forbids reintroducing a memorised list. So the
       matrix is PARSED here on every run, and the parse is then compared against the
       registry. Parsing alone would only move the hardcoding one file over; the comparison
       is what turns the next upstream ACL edit from silent staleness into a red gate
       (AGENTS.md rule 18). The TABLE is authoritative, not the summary sentence beneath it.

ACL-4  The registry's `personas` map must equal the roster on disk. Same argument as ACL-3,
       found the hard way: at the V5 re-baseline 14 of the 17 entries still carried retired
       pre-V5 addresses. `v4_gates.py:416` and `:759` read that map, so the staleness never
       failed loudly - it quietly checked prompts against addresses the universe no longer
       contained. Nothing compared the two until a hand-run diff found it, and rule 18 says a
       finding closed by a hand-run check gets a real check in the same pass. Anchor
       `v22 ACL-8` restores the `blake@` spelling in memory to prove this can still fail.

Exit 0 clean or SKIP, non-zero on any finding.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from universes import detect_universe, get_framework_profile, get_universe_constants  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# Services with no write path in this universe's catalog. Phrases that imply a write to
# one of them are ungradeable regardless of how the rubric is worded.
#
# A RETIRED server must never be keyed here. Until V5 this carried a `snowflake` entry, and
# once the 2026-08 drop removed every snowflake_* tool the entry stopped describing anything
# real: a hit would have reported "requires a write to `snowflake`, which is read-only in
# this universe" about a service the universe does not ship at all. That is a misattribution
# rather than a dead branch, which is worse - it is a finding a reader would act on. The
# whole dependency, read or write, is now owned by the V5 A1 HARD GATE in
# check_retired_servers.py, which is wired into validate.py --phase prompt and --phase oe.
# check_write_rules_are_live() below keeps that decision enforced instead of merely made.
READ_ONLY_WRITE_PHRASES = {
    "gmail": [r"\bsend(?:s|ing)?\s+(?:an?\s+)?email\b", r"\bemail(?:s|ing)?\s+(?:the|a|an)\b",
              r"\breply(?:s|ing)?\s+to\s+(?:the\s+)?(?:email|thread)\b",
              r"\bcompose(?:s|ing)?\s+(?:an?\s+)?email\b", r"\bdrafts?\s+an?\s+email\b"],
}


# ---------------------------------------------------------------------------
# ACL-3. The Access matrix, parsed live.
# ---------------------------------------------------------------------------
# Globbed rather than named, because upstream renumbers this file: the 2026-08 drop moved it
# from 15_Persona_ACL.md to 14_Persona_ACL.md. A hardcoded number would have turned a
# renumbering into a silent SKIP, which is the failure shape this check exists to remove.
_ACL_DOC_GLOB = "*_Persona_ACL.md"

_MATRIX_HEADING = re.compile(r"^#{2,}\s*Access matrix\s*$", re.IGNORECASE)
_ANY_HEADING = re.compile(r"^#{1,6}\s")
# Two leading cells only: `| <Service> | <Yes|No> | ...`. The third column is free prose and
# is deliberately not captured.
_MATRIX_ROW = re.compile(r"^\|([^|]+)\|([^|]+)\|")


def acl_doc_path(consts):
    """The persona ACL spec doc for this universe, or None."""
    docs = consts.get("docs_path")
    if not docs:
        return None
    hits = sorted((ROOT / docs).glob(_ACL_DOC_GLOB))
    return hits[0] if hits else None


def parse_access_matrix(path: Path):
    """(scoped, unscoped) service keys read from the doc's Access matrix TABLE.

    Scoped to the `## Access matrix` section and stopped at the next heading, so a table
    elsewhere in the doc cannot contribute rows.

    The TABLE is parsed, never the prose. The doc carries a one-sentence human summary of
    the unscoped group directly beneath the table, and a mechanic note that GDocs, GSheets
    and GSlides inherit GDrive's file ACL. Neither is a table row, and requiring the second
    cell to be exactly Yes or No drops both the header and the `|---|:---:|---|` separator
    without needing to count lines. The summary sentence is precisely what went stale in the
    superseded 15_Persona_ACL.md, whose prose claimed eight scoped services while its own
    matrix marked Contacts "No" - so the matrix, not the sentence, is the authority.

    Display names map onto registry keys by lowercasing, and that is checked rather than
    assumed: any row whose service the registry does not know is reported by the caller.
    """
    scoped, unscoped = set(), set()
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    start = next((i for i, ln in enumerate(lines) if _MATRIX_HEADING.match(ln.strip())), None)
    if start is None:
        return scoped, unscoped
    for ln in lines[start + 1:]:
        if _ANY_HEADING.match(ln):
            break
        m = _MATRIX_ROW.match(ln.strip())
        if not m:
            continue
        svc, flag = m.group(1).strip().lower(), m.group(2).strip().lower()
        if flag == "yes":
            scoped.add(svc)
        elif flag == "no":
            unscoped.add(svc)
    return scoped, unscoped


def check_acl_matrix_matches_registry(consts) -> list:
    """Assert the registry's ACL sets equal the ones the spec doc declares.

    Loud on mismatch, naming the service AND the direction, because the two directions call
    for opposite fixes: a service the matrix scopes and the registry does not means reads are
    being validated god-mode, while the reverse means a feasible read is being rejected.

    Takes the constants dict directly so a caller can hand in a mutated registry - which is
    exactly what anchor v22 ACL-6 does to prove this comparison can fail at all.
    """
    doc = acl_doc_path(consts)
    if doc is None or not doc.is_file():
        return [f"FAIL ACL-3: no persona ACL doc matched {consts.get('docs_path')}/"
                f"{_ACL_DOC_GLOB}, so the Access matrix cannot be derived and the registry's "
                f"ACL sets are unverifiable."]
    scoped_doc, unscoped_doc = parse_access_matrix(doc)
    if not scoped_doc and not unscoped_doc:
        return [f"FAIL ACL-3: parsed zero Access matrix rows from {doc.name}. Either the "
                f"`## Access matrix` section or its table shape changed upstream; the "
                f"registry's ACL sets are unverified until the parse is repaired."]

    scoped_reg = {s.lower() for s in (consts.get("acl_scoped_services") or [])}
    unscoped_reg = {s.lower() for s in (consts.get("acl_unscoped_services") or [])}
    where = f"{doc.name} Access matrix"
    issues = []

    for svc in sorted(scoped_reg - scoped_doc):
        if svc in unscoped_doc:
            issues.append(f"FAIL ACL-3: `{svc}` - registry lists it as scoped but the Access "
                          f"matrix marks it unscoped ({where}). The matrix is authoritative.")
        else:
            issues.append(f"FAIL ACL-3: `{svc}` - registry lists it as scoped but the Access "
                          f"matrix has no row for it ({where}).")
    for svc in sorted(unscoped_reg - unscoped_doc):
        if svc in scoped_doc:
            issues.append(f"FAIL ACL-3: `{svc}` - registry lists it as unscoped but the Access "
                          f"matrix marks it persona-scoped ({where}). Every required read of "
                          f"it must be validated from the acting persona's view.")
        else:
            issues.append(f"FAIL ACL-3: `{svc}` - registry lists it as unscoped but the Access "
                          f"matrix has no row for it ({where}). If the service was retired, "
                          f"drop it from the registry rather than leaving it declared.")
    # Only report a doc-side service the registry places in NEITHER set. One the registry
    # merely files under the wrong heading is already reported above, and saying it twice
    # would inflate a one-service disagreement into two findings.
    for svc in sorted(scoped_doc - scoped_reg):
        if svc not in unscoped_reg:
            issues.append(f"FAIL ACL-3: `{svc}` - the Access matrix marks it persona-scoped "
                          f"but the registry declares it in neither ACL set ({where}).")
    for svc in sorted(unscoped_doc - unscoped_reg):
        if svc not in scoped_reg:
            issues.append(f"FAIL ACL-3: `{svc}` - the Access matrix marks it unscoped but the "
                          f"registry declares it in neither ACL set ({where}).")
    return issues


def check_personas_match_roster(consts, roster) -> list:
    """Assert the registry's `personas` map equals the persona roster on disk.

    The standing gate for a defect found BY HAND at the V5 re-baseline: 14 of the 17
    HarmonyGames entries still carried pre-V5 addresses (`blake@`, `jlawson@`, `leonard@`)
    after V5 regularised every multi-word persona to `firstname.lastname@`. The old
    spellings matched ZERO rows anywhere in the payload, and `v4_gates.py:416` / `:759`
    read this map for their persona/address checks - so the staleness never failed loudly,
    it quietly weakened those checks against addresses that no longer existed. Nothing
    compared the two, which is why it survived the whole re-baseline until a hand-run diff.

    Direction is named on every finding because the fixes are opposite: roster-only means
    the registry is missing a real identity, registry-only means it is asserting a dead one.

    Takes `consts` directly so a caller can hand in a mutated registry and prove this
    comparison can fail at all - the same anti-vacuity route anchor v22 ACL-6 uses.

    Skips cleanly when a universe declares no roster. Only HarmonyGames ships one; starpm
    has a `personas` map with no roster on disk, so there is nothing to compare it against.
    """
    if not consts.get("persona_acl_roster") or not roster:
        return []
    reg = {e.lower() for e in (consts.get("personas") or {})}
    if not reg:
        return []
    disk = {p["email"].lower() for p in roster if p.get("email")}
    issues = []
    for e in sorted(disk - reg):
        issues.append(f"FAIL ACL-4: `{e}` is in the roster but NOT in the registry "
                      f"`personas` map. Transcribe it; never derive an address from a name.")
    for e in sorted(reg - disk):
        issues.append(f"FAIL ACL-4: `{e}` is in the registry `personas` map but NOT in the "
                      f"roster. The roster is authoritative, so this is a stale spelling and "
                      f"every check reading this map is weakened by it.")
    return issues


def check_write_rules_are_live(consts, profile) -> list:
    """Every READ_ONLY_WRITE_PHRASES key must name a service this universe still ships.

    The standing gate for the removal recorded above. Deleting the retired `snowflake` entry
    was a one-time edit that any later change could undo; this makes the undo fail loudly.
    AGENTS.md rule 18: a finding closed by hand becomes a check, or it comes back.
    """
    live = {s.lower() for s in (consts.get("services") or [])}
    retired = {s.lower() for s in (profile.get("retired_services") or ())}
    issues = []
    for svc in sorted(READ_ONLY_WRITE_PHRASES):
        if svc in retired:
            issues.append(f"FAIL ACL-2r: a read-only write rule is keyed to `{svc}`, a RETIRED "
                          f"server. It ships no tools at all, so reporting a WRITE denial "
                          f"misattributes the defect. The dependency belongs to the A1 hard "
                          f"gate in check_retired_servers.py.")
        elif live and svc not in live:
            issues.append(f"FAIL ACL-2r: a read-only write rule is keyed to `{svc}`, which is "
                          f"not in this universe's `services`. The rule can only ever "
                          f"misattribute a finding.")
    return issues


def load_brief_names(consts) -> set:
    """Persona names documented in the universe's persona briefs.

    The ACL roster is NOT the full persona set. `4_Persona_ACL_Roster.json` carries 17
    entries, but `2_Persona_Briefs.md` documents others - Tim Steudler (Business
    Development Manager, Licensing) appears in the briefs, the universe summary and the
    reference sheet, and is the assigned persona of a task that PASSED upstream QC.
    Treating the roster as the sole authority made this gate reject ground truth, which is
    a worse failure than not having the gate: a documented persona missing from the roster
    is an upstream roster gap, not a task defect.
    """
    rel = consts.get("persona_briefs")
    if not rel:
        return set()
    p = ROOT / rel
    if not p.is_file():
        return set()
    import re as _re
    text = p.read_text(encoding="utf-8", errors="ignore")
    return {m.lower() for m in _re.findall(r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b", text)}


def load_roster(consts) -> list:
    rel = consts.get("persona_acl_roster")
    if not rel:
        return []
    p = ROOT / rel
    if not p.is_file():
        return []
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    return d if isinstance(d, list) else d.get("personas", [])


def check_persona_resolves(task_dir: Path, roster: list, brief_names: set) -> list:
    issues = []
    f = task_dir / "2_Persona.txt"
    if not f.is_file():
        return ["FAIL ACL-1: 2_Persona.txt missing; the acting identity cannot be resolved"]
    text = f.read_text(encoding="utf-8", errors="ignore").strip()
    if not text:
        return ["FAIL ACL-1: 2_Persona.txt is empty"]

    emails = {e.lower() for e in re.findall(r"[\w.+-]+@[\w.-]+", text)}
    keys = {str(r.get("persona_key", "")).lower() for r in roster}
    roster_emails = {str(r.get("email", "")).lower() for r in roster}
    names = {str(r.get("name", "")).lower() for r in roster}

    if emails:
        unknown = emails - roster_emails
        if unknown:
            issues.append(
                f"FAIL ACL-1: email(s) {sorted(unknown)} are not in the persona roster. "
                f"HarmonyGames persona addresses are irregular by design and must be read "
                f"from 4_Persona_ACL_Roster.json, never constructed from a name."
            )
        return issues

    low = text.lower()
    if any(k and k in low for k in keys) or any(n and n in low for n in names):
        return issues
    # Documented in the persona briefs but absent from the ACL roster: an upstream roster
    # gap, not a task defect. WARN so the gap is visible without blocking valid work.
    if any(b and b in low for b in brief_names):
        who = next(b for b in brief_names if b and b in low)
        print(f"[WARN] ACL-1: persona {who.title()!r} is documented in "
              f"{ROOT.name}/2_Persona_Briefs.md but is absent from 4_Persona_ACL_Roster.json "
              f"({len(roster)} entries). Upstream roster gap; not blocking.")
        return issues
    issues.append(
        "FAIL ACL-1: 2_Persona.txt names no persona found in either "
        "4_Persona_ACL_Roster.json or the persona briefs."
    )
    return issues


def check_no_impossible_writes(task_dir: Path) -> list:
    issues = []
    for fname in ("5_Prompt.txt", "6_Oracle_Events.txt", "7_Rubrics.json"):
        f = task_dir / fname
        if not f.is_file():
            continue
        text = f.read_text(encoding="utf-8", errors="ignore")
        for svc, patterns in READ_ONLY_WRITE_PHRASES.items():
            for pat in patterns:
                m = re.search(pat, text, re.IGNORECASE)
                if m:
                    issues.append(
                        f"FAIL ACL-2: {fname} requires a write to `{svc}`, which is "
                        f"read-only in this universe (matched {m.group(0)!r}). No tool "
                        f"performs that action, so the requirement can never be satisfied."
                    )
                    break
    return issues


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python Validators/check_persona_acl.py <task_dir>", file=sys.stderr)
        return 1
    task_dir = Path(sys.argv[1]).resolve()
    if not task_dir.is_dir():
        print(f"ERROR: not a directory: {task_dir}", file=sys.stderr)
        return 1

    universe = detect_universe(task_dir)
    profile = get_framework_profile(universe)
    if not profile.get("acl_gate", False):
        print(f"[SKIP] universe `{universe}` has no persona ACL gate (acl_gate=false)")
        return 0

    consts = get_universe_constants(universe)
    roster = load_roster(consts)
    if not roster:
        print(f"[WARN] persona roster not found or empty: {consts.get('persona_acl_roster')}")
        print("PERSONA ACL: cannot verify ACL-1 without the roster")
        return 1

    scoped = consts.get("acl_scoped_services", [])
    unscoped = consts.get("acl_unscoped_services", [])
    print(f"universe: {universe} · roster: {len(roster)} personas")
    print(f"scoped services ({len(scoped)}): {', '.join(scoped)}")
    print(f"unscoped ({len(unscoped)}): {', '.join(unscoped)}")

    acl3 = check_acl_matrix_matches_registry(consts)
    if not acl3:
        _doc = acl_doc_path(consts)
        _s, _u = parse_access_matrix(_doc)
        print(f"[OK] ACL-3: {_doc.name} Access matrix agrees with the registry "
              f"({len(_s)} scoped / {len(_u)} unscoped)")

    acl4 = check_personas_match_roster(consts, roster)
    if not acl4 and consts.get("persona_acl_roster"):
        print(f"[OK] ACL-4: registry `personas` agrees with the roster on disk "
              f"({len(consts.get('personas') or {})} addresses, transcribed not derived)")

    brief_names = load_brief_names(consts)
    issues = (check_persona_resolves(task_dir, roster, brief_names)
              + check_no_impossible_writes(task_dir)
              + check_write_rules_are_live(consts, profile)
              + acl3 + acl4)
    for i in issues:
        print(i)
    print()
    print(f"PERSONA ACL: {len(issues)} finding(s)")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
