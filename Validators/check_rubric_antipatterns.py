#!/usr/bin/env python3
"""
Usage:
    python Validators/check_rubric_antipatterns.py <task_dir>

Mechanically enforces the criterion-construction anti-patterns that councils and AUDIT
have found by hand, so a closed finding cannot be silently reintroduced.

Why this exists
---------------
The pipeline already computes a severity census, but it is a council SELF-REPORT in
prose, not a measurement. On Task 44 four separate reports asserted "0 Major / 0
Moderate / 0 Minor across 64" and "0/60 with any issue", while a third-party review of
the same artifact found two Moderate Overly Specific defects and one Overly Broad. An
assertion authored by the same agent that wrote the rubrics cannot catch that agent's
blind spot.

Worse, closed findings were reintroducible. `AUDIT_rubrics.md` finding F1 classified
`FAIL only if` as MODERATE ("made omission a PASS, nullifying the criterion"), fixed it
to the additive `FAIL if X, and FAIL if Y`, and verified the fix with a regex run ONCE
by hand and recorded in prose. Hours later a subsequent edit to that same criterion put
`FAIL only if` straight back, and nothing objected: `validate.py --phase rubrics`
returned 0 fails, 0 warns.

This checker turns those hand-run greps into a standing gate. It is deliberately
standalone rather than folded into `validate.py`, because `check_regression.py` pins the
hashes of 21 `validate.py` reports and changing that output would break the zero-
regression gate.

Checks
------
A1  `FAIL only if`               MODERATE. An exhaustive fail list turns every
                                unenumerated shape into a PASS, including plain
                                omission. Additive `FAIL if ... and FAIL if ...`
                                expresses the same intent with no nullification risk.
A2  bare `after <date>`          MINOR. Excludes a valid same-day action. Use
                                "on or after".
A3  hedged title, no FAIL clause MINOR. A criterion whose title hedges with
                                "recorded/reported as" but whose evidence sets no FAIL
                                condition leaves the grader to invent one, which is the
                                shape that produced attribution-demand misgrading.
NOT mechanised: nested accept-sets (AUDIT_rubrics.md F2, `pass(51) => pass(23)`).
A token-overlap proxy was built and discarded: it produced 14 false positives and zero
true positives on Task 44, because mentioning a location does not mean a criterion is
restricted to it, and shared topic words do not establish that two criteria grade the
same fact. Establishing subject identity needs semantic judgement, so nesting stays a
council/AUDIT check. A gate that noisy would be ignored, which is worse than absent.

Exit 0 clean, 1 when any MODERATE fires, 0 with a printed advisory when only MINORs do.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIELDS = ("title", "evidence", "justification")

FAIL_ONLY_IF = re.compile(r"FAIL\s+only\s+if", re.IGNORECASE)
BARE_AFTER = re.compile(r"(?<!on or )\bdated\s+after\s+\w+\s+\d{1,2},?\s+20\d{2}", re.IGNORECASE)
HEDGE = re.compile(r"\b(?:recorded|reported)\s+as\b", re.IGNORECASE)
HAS_FAIL = re.compile(r"\bFAIL\b", re.IGNORECASE)


def load(task: Path):
    data = json.loads((task / "7_Rubrics.json").read_text(encoding="utf-8"))
    crits = data if isinstance(data, list) else (data.get("rubrics") or data.get("criteria"))
    return [{"idx": i + 1, **{f: (c.get(f) or "") for f in FIELDS}} for i, c in enumerate(crits)]


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    task = Path(sys.argv[1])
    if not task.is_absolute():
        task = ROOT / task
    if not (task / "7_Rubrics.json").is_file():
        print(f"[SKIP] {task}: no 7_Rubrics.json")
        return 0

    crits = load(task)
    mod, minor = [], []

    for c in crits:
        for f in FIELDS:
            for m in FAIL_ONLY_IF.finditer(c[f]):
                mod.append(("A1", c["idx"], f,
                            "`FAIL only if` makes every unenumerated shape a PASS, "
                            "including plain omission. Rewrite additively: "
                            "`FAIL if X, and FAIL if Y`.",
                            c[f][max(0, m.start() - 60):m.start() + 90]))
            for m in BARE_AFTER.finditer(c[f]):
                minor.append(("A2", c["idx"], f,
                              "bare `after <date>` excludes a valid same-day action; "
                              "use `on or after`.", m.group(0)))
        if HEDGE.search(c["title"]) and not HAS_FAIL.search(c["evidence"]):
            minor.append(("A3", c["idx"], "evidence",
                          "title hedges with 'recorded/reported as' but the evidence sets "
                          "no FAIL condition, leaving the grader to invent one. This is the "
                          "shape that produces attribution-demand misgrading.",
                          c["title"][:90]))

    print(f"=== Rubric anti-pattern scan: {task.name} ===")
    print(f"{len(crits)} criteria x {len(FIELDS)} fields\n")

    seen, uniq_mod = set(), []
    for h in mod:
        k = (h[0], h[1], h[2])
        if k not in seen:
            seen.add(k)
            uniq_mod.append(h)

    for label, bucket in (("MODERATE", uniq_mod), ("MINOR", minor)):
        if not bucket:
            continue
        print(f"[{label}] {len(bucket)} finding(s):")
        for code, idx, field, why, snip in bucket:
            print(f"  {code}  criterion {idx} [{field}]")
            print(f"      {why}")
            print(f"      ...{snip.strip()}...")
        print()

    if not uniq_mod and not minor:
        print(f"[OK] {task.name}: no construction anti-patterns found.")
        return 0
    if uniq_mod:
        print("MODERATE findings block. Each one has cost this project a council round "
              "before; they are mechanically detectable and must not ship.")
        return 1
    print("MINOR findings only, advisory. Fix if cheap.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
