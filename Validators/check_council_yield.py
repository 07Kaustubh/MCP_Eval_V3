#!/usr/bin/env python3
"""
Usage:
    python Validators/check_council_yield.py <task_dir> [--budget-kb N]

Measures what each council / AUDIT report actually FOUND, per KB of prose it produced.

Why this exists
---------------
Report length was being read as evidence of rigour. It is not, and the pipeline had no
way to see the difference. Task 44 produced 485 KB of council and AUDIT prose for one
60-criterion task; 169 KB of that (35%) came from reports that recorded ZERO severity
findings, including a single 92 KB / 804-line prompt audit that found nothing. Meanwhile
an independent review of the shipped artifact found two Moderate defects and one Overly
Broad that those same reports had examined and cleared.

This is the measurement behind AGENTS.md rule 20. It does not judge whether a finding was
correct; it reports yield so a phase that reliably produces prose and no findings can be
cut or replaced with a deterministic check (rule 18), and so a phase that declines most of
what it finds is visible (rule 19).

Metrics
-------
findings   severity-tagged findings raised (MAJOR / MODERATE / MINOR / BLOCKER)
declined   findings the report closed WITHOUT an artifact change
applied    findings recorded as applied or closed by a fix
kb         report size
yield      findings per 10 KB of prose

Flags
-----
ZERO-YIELD    report exceeds the size budget and raised no findings at all
DECLINE-HEAVY report declined at least half of what it raised (rule 19 exposure)

Known limitation, stated rather than hidden
------------------------------------------
The finding count is only reliable for reports that tag findings with IDs
("MODERATE-3"). Where a report does not, the fallback counts bare severity words and
inflates badly: a report that merely PRINTS the severity taxonomy or a scoring table
scores as though it raised dozens of findings. On Task 44 that fallback rated
`S1_A_grounding.md` at 38 findings when its own summary records zero. So treat the
KB column and the DECLINE-HEAVY flag as sound, and the yield column as indicative only.
The durable fix is upstream: require councils to tag findings with IDs, at which point
ZERO-YIELD becomes trustworthy too.

Advisory: exits 0 always. This informs pipeline design, it does not gate a task.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FINDING = re.compile(r"\b(MAJOR|MODERATE|MINOR|BLOCKER)\b[-\s]*\d*", re.IGNORECASE)
DECLINED = re.compile(r"\bDECLIN(?:E|ED|ING)\b", re.IGNORECASE)
APPLIED = re.compile(r"\b(?:APPLIED|CLOSED|FIXED IN PLACE)\b", re.IGNORECASE)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("task_dir")
    ap.add_argument("--budget-kb", type=float, default=20.0,
                    help="a report larger than this with zero findings is flagged (default 20)")
    args = ap.parse_args()

    task = Path(args.task_dir)
    if not task.is_absolute():
        task = ROOT / task
    reports = task / "_aux" / "Council_Reports"
    if not reports.is_dir():
        print(f"[SKIP] {task.name}: no _aux/Council_Reports/")
        return 0

    files = sorted(p for p in reports.glob("*.md") if p.is_file())
    if not files:
        print(f"[SKIP] {task.name}: no reports")
        return 0

    rows, tot_kb, tot_find, tot_dec = [], 0.0, 0, 0
    for p in files:
        txt = p.read_text(encoding="utf-8", errors="replace")
        kb = len(txt.encode()) / 1024
        # count distinct severity-tagged finding IDs where present, else raw mentions
        ids = set(re.findall(r"\b(?:MAJOR|MODERATE|MINOR|BLOCKER)-\d+", txt, re.IGNORECASE))
        n_find = len(ids) if ids else len(FINDING.findall(txt))
        n_dec = len(DECLINED.findall(txt))
        n_app = len(APPLIED.findall(txt))
        rows.append((p.name, kb, n_find, n_dec, n_app))
        tot_kb += kb
        tot_find += n_find
        tot_dec += n_dec

    print(f"=== Council yield: {task.name} ===")
    print(f"{len(rows)} report(s), {tot_kb:.0f} KB total prose\n")
    print(f"{'REPORT':<30}{'KB':>7}{'FIND':>6}{'DECL':>6}{'APPL':>6}{'/10KB':>7}  FLAGS")
    zero_kb = 0.0
    for name, kb, f, d, a in sorted(rows, key=lambda r: -r[1]):
        flags = []
        if f == 0 and kb > args.budget_kb:
            flags.append("ZERO-YIELD")
            zero_kb += kb
        if f and d >= max(1, f / 2):
            flags.append("DECLINE-HEAVY")
        y = (f / kb * 10) if kb else 0
        print(f"{name:<30}{kb:>7.1f}{f:>6}{d:>6}{a:>6}{y:>7.2f}  {' '.join(flags)}")

    print()
    print(f"total findings raised : {tot_find}")
    print(f"total declines        : {tot_dec}"
          + (f"  ({tot_dec/tot_find:.0%} of findings raised)" if tot_find else ""))
    print(f"overall yield         : {tot_find/tot_kb*10:.2f} findings per 10 KB"
          if tot_kb else "")
    if zero_kb:
        print(f"zero-yield prose      : {zero_kb:.0f} KB ({zero_kb/tot_kb:.0%} of total) "
              f"produced no findings at all")
        print()
        print("Per AGENTS.md rule 20, a phase that reliably produces prose and no findings")
        print("should be cut or replaced with a deterministic check (rule 18). Per rule 19,")
        print("a DECLINE-HEAVY report is where self-validated findings get argued away.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
