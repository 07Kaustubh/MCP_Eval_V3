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
    ("StarPM meta refs",    re.compile(r"\bStarPM[_ ]?Base[_ ]?Universe\b", re.IGNORECASE)),
    # v22: the grading loop itself. These leaked into platform-facing justification
    # fields on Task 44 and cleared every pattern above. Origin: operator review
    # 2026-07-26, "filed as a dispute" / "diverges from the current export" /
    # "this cell is the reason the criterion was rewritten".
    ("grading-process meta", re.compile(
        r"\b(?:the\s+(?:current\s+|new\s+|prior\s+|previous\s+)?export|re-?export(?:ed)?|re-?grad(?:e|ed|ing)"
        r"|verifier\s+export|grading\s+of\s+record"
        r"|filed?\s+as\s+a\s+dispute|per-?cell\s+(?:appeal|dispute)|contested\s+cell"
        r"|diverges?\s+from|divergence\s+from"
        r"|corrected\s+wording|as\s+(?:re)?written\s+now|criterion\s+was\s+(?:rewritten|revised|edited|corrected)"
        r"|rubric\s+was\s+(?:rewritten|revised|edited|corrected)"
        r"|bucket\s*[123]\b"
        r"|pass\s*[234]\b|pre-?fix|post-?fix)\b", re.IGNORECASE)),
    # NOTE: "all-failing" / "all-fail" is deliberately NOT forbidden. The platform's
    # own step is titled "Justify All-Fail Rubrics", so it is the reviewer's own
    # vocabulary rather than internal pipeline language.
    # v22: a bare cross-criterion pointer ("Follows from 38") leaves the platform
    # reviewer hunting. The rubric-number pattern above misses the bare-integer form.
    ("cross-criterion ref",  re.compile(
        r"\b(?:follows?\s+from|per|see|same\s+as|as\s+(?:in|with))\s+#?\d{1,2}\b(?!\s*(?:%|units?|water|hose|of|and|or|new|rows?|calls?|runs?|cells?|criteria))",
        re.IGNORECASE)),
    # v22: the no-em-dash rule was only ever enforced on the prompt. Justification
    # text typed straight into a platform form never passed a sweep.
    # v23: applied OUTSIDE quoted spans only. The em-dash ban is a pipeline style rule
    # with no basis in the source specs (which themselves contain 610 em-dashes), and on
    # Task 44 it caused a verbatim agent artifact to be altered inside the very document
    # written to prove what that artifact said. Evidence fidelity outranks house style.
    ("em-dash outside a quote", re.compile(r"—")),
]


QUOTED = re.compile(r"`[^`\n]*`|```.*?```|\u201c[^\u201d]*\u201d|\"[^\"\n]{0,400}\"|\*\"[^\"]*\"\*", re.DOTALL)


def _blank_quotes(text):
    """Replace quoted spans with spaces so style rules skip them but offsets survive."""
    return QUOTED.sub(lambda m: " " * len(m.group(0)), text)


def scan(path):
    text = path.read_text(encoding="utf-8")
    unquoted = _blank_quotes(text)
    hits = []
    for label, pat in FORBIDDEN:
        target = unquoted if label == "em-dash outside a quote" else text
        for m in pat.finditer(target):
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
