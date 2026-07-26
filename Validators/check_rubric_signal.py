#!/usr/bin/env python3
"""
Usage:
    python Validators/check_rubric_signal.py <task_dir>

Measures how much DISCRIMINATION each criterion actually contributes, and flags the ones
carrying none.

Why this exists
---------------
A rubric set is a test suite for agent behaviour, and test-suite adequacy has a mature
methodology the pipeline was not borrowing. Mutation-testing practice treats an assertion
that holds on every mutant as a WEAK assertion: it executes but verifies nothing. The
canonical example is asserting non-null instead of asserting the value.

The rubric equivalent is a criterion that passes on every run of every model. It consumed a
slot in a capped set, it cost author and grader effort, and it separated no good run from
any bad one. Existence-only criteria ("the Agent creates a ticket") are the usual culprits,
because any artifact of the right shape satisfies them regardless of content.

This matters at the margin, not in the abstract. Task 44 shipped at the 60-criterion ceiling
and could not fit a Process rubric for an ordering requirement that nothing else could grade
(`check_ordering_coverage.py`). Meanwhile ten of its sixty criteria passed 12/12. The budget
to cover the ordering requirement already existed; it was spent on assertions that verified
nothing.

Categories
----------
ZERO-SIGNAL   passes every cell on every model. Weak assertion. Candidate to cut, ESPECIALLY
              if existence-only with a content sibling that already covers it.
ALL-FAIL      fails every cell. Handled by the all-failing rule (AGENTS.md rule 21: default
              is removal unless vehemently defensible). Reported here for completeness.
DISCRIMINATES separates runs. This is what a criterion is for.

An existence-only criterion is not automatically wrong: the guidelines require a 1.1
write-action result for every write action. It is wrong when it passes universally AND a
sibling criterion already grades the same artifact's content, because then the 1.1 adds no
check the 1.2 does not already make.

Advisory: exits 0. This is budget analysis, not a correctness gate.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# "The Agent <creates|raises|posts|drafts|schedules> ..." with no content constraint after.
EXISTENCE = re.compile(
    r"^The Agent\s+(?:creates|raises|opens|files|posts|drafts|schedules|sends|adds|logs)\b",
    re.IGNORECASE)
# A content criterion names what the artifact must say.
CONTENT = re.compile(
    r"\b(?:states|mentions|includes|covers|records|describes|identifies|names|reports|carries)\b",
    re.IGNORECASE)

# Which DELIVERABLE a criterion grades. Sibling analysis has to be per-artifact: a plumbing
# ticket criterion and a North-HVAC ticket criterion are not each other's content sibling.
# A first cut used bare token overlap and pointed the calendar, plumbing and draft criteria
# all at one unrelated criterion, so it is grouped explicitly instead.
ARTIFACTS = [
    ("maintenance ticket", r"maintenance ticket|ticket log|Maintenance Tickets"),
    ("tracking item",      r"tracking (?:item|work)|Operations board"),
    ("spot-check note",    r"note on OPS-\d+|spot-check record"),
    ("calendar slot",      r"calendar|re-inspection slot|schedules a"),
    ("channel update",     r"channel status update|posts a status|#maintenance"),
    ("draft to Brooke",    r"draft to Brooke|drafts an email"),
    ("final response",     r"final response"),
]


def artifact_of(title):
    for name, pat in ARTIFACTS:
        if re.search(pat, title, re.IGNORECASE):
            return name
    return "other"


def norm_title(s):
    s = re.sub(r"\[([^\]]+)\]\(mailto:[^)]+\)", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = s.replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip().rstrip(".").lower()


def parse_export(path: Path):
    runs, cur = {}, None
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"^Run\s*#?(\d+)\s*$", raw.strip())
        if m:
            cur = int(m.group(1)); runs[cur] = {}; continue
        if "\t" not in raw or cur is None:
            continue
        p = raw.split("\t")
        if len(p) < 2 or p[1].strip() not in ("Pass", "Fail"):
            continue
        runs[cur][norm_title(p[0])] = p[1].strip()
    return runs


def main():
    if len(sys.argv) != 2:
        print(__doc__); return 2
    task = Path(sys.argv[1])
    if not task.is_absolute():
        task = ROOT / task
    rub = task / "7_Rubrics.json"
    if not rub.is_file():
        print(f"[SKIP] {task.name}: no 7_Rubrics.json"); return 0
    crits = json.loads(rub.read_text(encoding="utf-8"))
    crits = crits if isinstance(crits, list) else (crits.get("rubrics") or crits.get("criteria"))

    exports = [(("opus" if "Opus" in n else "gemini" if "Gemini" in n else "model"), task / n)
               for n in ("8a_Verifier_Fails_Opus.txt", "8b_Verifier_Fails_Gemini.txt",
                         "8_Verifier_Fails.txt")
               if (task / n).is_file() and (task / n).stat().st_size > 0]
    if not exports:
        print(f"[SKIP] {task.name}: no verifier export"); return 0

    grids = {lab: parse_export(p) for lab, p in exports}

    rows = []
    for i, c in enumerate(crits, 1):
        t = c.get("title") or ""
        nt = norm_title(t)
        cells = []
        for lab, g in grids.items():
            for r in sorted(g):
                v = g[r].get(nt)
                if v:
                    cells.append(v)
        if not cells:
            rows.append((i, t, "NOT-GRADED", 0, 0)); continue
        p = cells.count("Pass"); f = cells.count("Fail")
        kind = "ZERO-SIGNAL" if f == 0 else ("ALL-FAIL" if p == 0 else "DISCRIMINATES")
        rows.append((i, t, kind, p, f))

    zero = [r for r in rows if r[2] == "ZERO-SIGNAL"]
    allf = [r for r in rows if r[2] == "ALL-FAIL"]
    disc = [r for r in rows if r[2] == "DISCRIMINATES"]
    ng = [r for r in rows if r[2] == "NOT-GRADED"]

    titles = {i: t for i, t, *_ in rows}

    print(f"=== Rubric signal: {task.name} ===")
    print(f"{len(crits)} criteria graded across {sum(len(g) for g in grids.values())} run(s) "
          f"on {len(grids)} model(s)\n")
    print(f"  DISCRIMINATES : {len(disc):>3}  ({len(disc)/len(crits):.0%})")
    print(f"  ZERO-SIGNAL   : {len(zero):>3}  ({len(zero)/len(crits):.0%})  passes every cell")
    print(f"  ALL-FAIL      : {len(allf):>3}  ({len(allf)/len(crits):.0%})")
    if ng:
        print(f"  NOT-GRADED    : {len(ng):>3}  title absent from the export (stale export or edited title)")
    print()

    if zero:
        print("ZERO-SIGNAL criteria (weak assertions: hold on every variant):")
        for i, t, _, p, f in zero:
            existence = bool(EXISTENCE.match(t)) and not CONTENT.search(t)
            art = artifact_of(t)
            # siblings = other criteria grading the SAME artifact with a content constraint
            sibs = [j for j, t2, *_ in rows
                    if j != i and artifact_of(t2) == art and CONTENT.search(t2)]
            kind = "existence-only" if existence else "content"
            cut = existence and sibs
            print(f"  [{i:>2}] ({art}, {kind}) {t[:88]}")
            if cut:
                print(f"       -> CUT CANDIDATE: content of this artifact is already graded by "
                      f"criterion(s) {sibs[:6]}")
            elif not existence:
                print(f"       -> real content check the models always satisfied. Easy, not weak. "
                      f"Keep unless the slot is needed.")
            elif not sibs:
                print(f"       -> existence-only with NO content sibling. Do not cut: it is the "
                      f"only check on this artifact.")
        print()
        cuts = [i for i, t, k, p, f in zero
                if EXISTENCE.match(t) and not CONTENT.search(t)
                and [j for j, t2, *_ in rows if j != i and artifact_of(t2) == artifact_of(t)
                     and CONTENT.search(t2)]]
        print(f"{len(zero)} of {len(crits)} slots produced no discrimination, of which "
              f"{len(cuts)} are cut candidates: {cuts}")
        print("Each is existence-only on an artifact whose content another criterion already")
        print("grades, so cutting it removes no coverage. In a set at the 60-criterion ceiling")
        print("that is the budget for coverage the cap forced out. Never cut a lever carrier")
        print("(AGENTS.md rule 14).")
    else:
        print("[OK] every criterion separates at least one run from another.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
