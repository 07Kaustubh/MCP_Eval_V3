#!/usr/bin/env python3
"""
Usage:
    python Validators/check_persona_acl.py <task_dir>

Persona ACL gate. Runs only for universes whose framework profile sets `acl_gate: true`
(today: HarmonyGames). SKIPs cleanly everywhere else.

Why this exists
---------------
HarmonyGames is the only universe with persona-scoped read visibility as a first-class
rule. Seven of its thirteen services filter reads by acting identity; six are unscoped.
A read performed under the wrong identity is neither a pass nor a fail, it is an
`Excluded` execution, which is a third trajectory disposition the other four universes do
not have.

Two properties are mechanically checkable from the authored artifacts alone, without
trajectories, and both are cheap to get wrong:

ACL-1  The persona named in `2_Persona.txt` must resolve to exactly one roster entry.
       HarmonyGames persona emails are irregular BY DESIGN - `arthur_blake` is `blake@`,
       `julia_lawson` is `jlawson@`, `martin_walsh` is `martin.walsh@`. Docs 15 states
       plainly: never construct, normalize or infer an email from a person's name. A task
       that invents `arthur.blake@harmonygames.co` names a persona that does not exist,
       and every downstream rubric bound to that identity is ungradeable.

ACL-2  A deliverable may not require a WRITE to a service the universe cannot write.
       Gmail here is read-only across all 27 tools: no send, no reply, no compose, not
       even a draft. "Email the vendor" is not an available action, so a rubric requiring
       one can never pass, which is an all-failing criterion by construction rather than
       by difficulty.

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
READ_ONLY_WRITE_PHRASES = {
    "gmail": [r"\bsend(?:s|ing)?\s+(?:an?\s+)?email\b", r"\bemail(?:s|ing)?\s+(?:the|a|an)\b",
              r"\breply(?:s|ing)?\s+to\s+(?:the\s+)?(?:email|thread)\b",
              r"\bcompose(?:s|ing)?\s+(?:an?\s+)?email\b", r"\bdrafts?\s+an?\s+email\b"],
    "snowflake": [r"\binsert(?:s|ing)?\s+into\b", r"\bupdate(?:s|ing)?\s+the\s+table\b"],
}


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
    if not get_framework_profile(universe).get("acl_gate", False):
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

    brief_names = load_brief_names(consts)
    issues = check_persona_resolves(task_dir, roster, brief_names) + check_no_impossible_writes(task_dir)
    for i in issues:
        print(i)
    print()
    print(f"PERSONA ACL: {len(issues)} finding(s)")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
