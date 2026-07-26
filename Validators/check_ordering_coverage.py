#!/usr/bin/env python3
"""
Usage:
    python Validators/check_ordering_coverage.py <task_dir>

Catches the one requirement class Outcome rubrics structurally cannot verify:
ORDERING between actions.

Why this exists
---------------
`Docs*/11_Taxonomy.md` and `Docs*/2_Rubrics_V3_Guidelines.md` name ordering as the
*primary* case for a Process rubric, and say so unambiguously:

  "The primary case is ordering between actions (A must happen before B, but both
   1.1s pass regardless of sequence)."
  "Ordering constraints can be explicit in the prompt ... and still require a Process
   rubric - because no Outcome rubric can verify ordering."

The pipeline's own rule 8 says "Default to zero [Process]. All 4 V3 reference tasks have
zero process rubrics." That default is an observation about four tasks promoted into a
policy, and it silently suppresses the only rubric class that can cover ordering.

Task 44 is the demonstration. Its prompt contains "put a slot on my calendar to go back
out and re-inspect whatever ends up in that follow-up" (the calendar slot depends on the
maintenance-ticket set being determined first) and "Then post where this stands in the
channel" (the post follows the tracking work). It shipped 60 Outcome rubrics and ZERO
Process rubrics. The calendar and channel-post criteria pass regardless of sequence, so
the ordering requirement in the prompt was never graded at all - an uncovered requirement
in the deliverable the pipeline exists to protect.

What it does
------------
Scans the prompt for ordering language, then checks whether any Process rubric covers
ordering. Reports the specific prompt clause so the author can either write the Process
rubric or record why the ordering is not load-bearing.

Exit 0 when covered or when no ordering language is present; 1 when the prompt orders
actions and nothing grades it.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Ordering language in a natural work request. Deliberately narrow: these are phrasings
# that make one action depend on another having happened, not mere narrative sequence.
ORDERING = [
    (r"\bthen\b\s+(?:post|send|draft|create|update|schedule|book|tell|let|loop|notify|raise|log)",
     "an explicit 'then <write action>' sequencing the deliverables"),
    (r"\bbefore\b\s+(?:you\s+)?(?:post|send|draft|creat\w+|updat\w+|schedul\w+|book\w*|notif\w+|clos\w+|sign)",
     "an explicit 'before <action>' precondition"),
    (r"\bafter\b\s+(?:you\s+)?(?:post|send|draft|creat\w+|updat\w+|schedul\w+|book\w*|notif\w+|confirm\w*)",
     "an explicit 'after <action>' precondition"),
    (r"\bonce\b\s+(?:you|that|the|it|they)\b[^.]{0,60}\b(?:post|send|draft|create|update|schedule|book|notify)",
     "an 'once X ... then Y' dependency"),
    (r"whatever ends up in|whatever comes out of|whatever lands in|based on what you find",
     "a deliverable whose content depends on an earlier step's result"),
    (r"\bfirst\b[^.]{0,50}\bthen\b", "an explicit first/then sequence"),
]

# A Process rubric that actually grades ordering.
ORDER_RUBRIC = re.compile(
    r"\b(?:before|after|prior to|then|once)\b", re.IGNORECASE)


def load_rubrics(task: Path):
    data = json.loads((task / "7_Rubrics.json").read_text(encoding="utf-8"))
    crits = data if isinstance(data, list) else (data.get("rubrics") or data.get("criteria"))
    return crits


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    task = Path(sys.argv[1])
    if not task.is_absolute():
        task = ROOT / task
    prompt_p, rub_p = task / "5_Prompt.txt", task / "7_Rubrics.json"
    if not prompt_p.is_file() or not rub_p.is_file():
        print(f"[SKIP] {task.name}: needs 5_Prompt.txt and 7_Rubrics.json")
        return 0

    prompt = prompt_p.read_text(encoding="utf-8")
    crits = load_rubrics(task)
    process = [c for c in crits if (c.get("category") or "").lower() == "process"]

    found = []
    for pat, desc in ORDERING:
        for m in re.finditer(pat, prompt, re.IGNORECASE):
            lo = max(0, m.start() - 70)
            found.append((desc, prompt[lo:m.end() + 70].replace("\n", " ").strip()))

    ordering_rubrics = [c for c in process if ORDER_RUBRIC.search(c.get("title") or "")]

    print(f"=== Ordering coverage: {task.name} ===")
    print(f"prompt: {len(prompt.split())} words · rubrics: {len(crits)} "
          f"({len(process)} process, {len(ordering_rubrics)} grading order)\n")

    if not found:
        print(f"[OK] {task.name}: no ordering language detected in the prompt.")
        return 0

    seen, uniq = set(), []
    for desc, ctx in found:
        if desc not in seen:
            seen.add(desc)
            uniq.append((desc, ctx))

    print(f"{len(uniq)} ordering construction(s) in the prompt:")
    for desc, ctx in uniq:
        print(f"  - {desc}")
        print(f"      ...{ctx}...")
    print()

    if ordering_rubrics:
        print(f"[OK] {len(ordering_rubrics)} Process rubric(s) grade ordering:")
        for c in ordering_rubrics:
            print(f"  - {c.get('title')}")
        return 0

    print(f"[FAIL] The prompt orders actions and NO Process rubric grades that ordering.")
    print()
    print("Outcome rubrics cannot verify sequence: each write action's 1.1 passes whether it")
    print("happened first or last. The guidelines name ordering as the PRIMARY case for a")
    print("Process rubric for exactly this reason.")
    print()
    print("Write one Process rubric per ordering constraint, phrased broadly enough that any")
    print("valid path passes (\"Agent raises the tracking items before posting the channel")
    print("update\", not \"Agent calls save_issue before slack_send_message\"). One constraint")
    print("per rubric; atomicity applies to Process rubrics too.")
    print()
    print("If the ordering genuinely is not load-bearing, record that decision rather than")
    print("leaving the requirement ungraded. AGENTS.md rule 8's \"default to zero\" is a")
    print("budgeting heuristic and does not override a requirement no Outcome can cover.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
