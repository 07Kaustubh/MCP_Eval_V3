#!/usr/bin/env python3
"""
Usage:
    python Validators/check_justification.py <path_to_justification_file> [...]

Enforces no-rubric-numbers + no-internal-terminology + no-guide-references
in linter justifications, AF justifications, and reviewer feedback. These
are seen by the platform reviewer; they must read as a human's plain-voice
reasoning, not a process-aware artifact.

Exits 0 if clean. Non-zero with per-hit report otherwise.
"""

import argparse
import re
import sys
from pathlib import Path

FORBIDDEN = [
    ("rubric number",       re.compile(r"\b(?:rubric\s*\[?\d+\]?|R\d+|criteria\s+#?\d+)\b", re.IGNORECASE)),
    ("council reference",   re.compile(r"\bcouncil\s+[ABab]\b|\bcouncil\s+protocol\b|\bcouncil\s+report\b", re.IGNORECASE)),
    ("pipeline phase name", re.compile(r"\b(?:PIPELINE\s+(?:S0|S1|S1\.5|S2|S3|S4|HARDNESS|FINAL|REVIEW|REDO|COMPARE|CLOSE|NEW|AUDIT))\b|\bphase\s+(?:S0|S1|S1\.5|S2|S3|S4|HARDNESS|FINAL|REVIEW|REDO|COMPARE|CLOSE|NEW|AUDIT)\b", re.IGNORECASE)),
    ("internal artifact",   re.compile(r"\b(?:Fact[_ ]?Ledger|Hardness[_ ]?Plan|Stump[_ ]?Hypothesis|Strict[_ ]?Convention[_ ]?Inventory|OE[_ ]?Convention[_ ]?Inventory|Universe[_ ]?Index|Universe[_ ]?Split|Trajectory[_ ]?Stats|REDO[_ ]?reason|Candidate[_ ]?Originals)\b", re.IGNORECASE)),
    ("script name",         re.compile(r"\b(?:validate|build_fact_ledger|build_graph_report|build_universe_index|split_universe|parse_trajectories|phase_ready|calc_similarity|check_justification|compare_rubrics|new_task|close_task)\.py\b", re.IGNORECASE)),
    ("guide / spec ref",    re.compile(r"\b(?:eval\s+guide|QC\s+spec(?:\s+doc)?|spec\s+doc|the\s+framework|the\s+playbook|the\s+runbook|guidelines\s+doc)\b", re.IGNORECASE)),
    ("V3 framework refs",   re.compile(r"\b(?:V3\s+framework|V3\s+rubric|Outcome\s+1\.\d|Process\s+rubric\s+three-condition)\b", re.IGNORECASE)),
    ("Brookfield meta refs",re.compile(r"\b(?:Brookfield[_ ]?Base[_ ]?Universe|per[- ]task\s+universe|stale\s+universe)\b", re.IGNORECASE)),
]


def scan(path):
    text = path.read_text(encoding="utf-8")
    hits = []
    for label, pat in FORBIDDEN:
        for m in pat.finditer(text):
            line_no = text.count("\n", 0, m.start()) + 1
            snippet = text[max(0, m.start() - 30):min(len(text), m.end() + 30)].replace("\n", " ")
            hits.append({
                "label": label,
                "match": m.group(0),
                "line": line_no,
                "context": snippet,
            })
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+", help="one or more justification files to check")
    args = ap.parse_args()

    total = 0
    for p_str in args.paths:
        p = Path(p_str).resolve()
        if not p.is_file():
            print(f"[SKIP] {p}: not a file")
            continue
        hits = scan(p)
        if not hits:
            print(f"[OK]   {p}: 0 hits")
            continue
        total += len(hits)
        print(f"[FAIL] {p}: {len(hits)} hit(s)")
        for h in hits:
            print(f"  line {h['line']}: [{h['label']}] `{h['match']}`")
            print(f"      ...{h['context']}...")

    if total:
        print(f"\n{total} forbidden-term hit(s) across all files.")
        print("Revise the justification to use plain operator voice — no rubric numbers, no internal artifact names, no pipeline phase names, no guide / spec references.")
        sys.exit(1)
    print("\nAll files clean.")
    sys.exit(0)


if __name__ == "__main__":
    main()
