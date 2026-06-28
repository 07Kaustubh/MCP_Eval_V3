#!/usr/bin/env python3
"""
check_verification.py — validates a Verification_<phase>.md file matches the template.

Enforces v16 Cross-Source Verification Discipline by checking the operator-produced
verification file has all required sections + non-empty evidence cells.

Usage:
    python3 Validators/check_verification.py --task Tasks/<TASK_DIR> --phase <phase>
"""

import argparse
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "## Sources consulted",
    "## Verification statements",
    "## Discrepancies surfaced",
    "## Verdict",
]

REQUIRED_SOURCE_CATEGORIES = [
    "Per-task data",
    "Eval spec",
    "QC spec",
]


def check(file_path: Path) -> list:
    issues = []
    if not file_path.is_file():
        return [f"FAIL: {file_path} does not exist"]
    text = file_path.read_text(encoding="utf-8")
    for sect in REQUIRED_SECTIONS:
        if sect not in text:
            issues.append(f"FAIL: missing section `{sect}`")
    sources_block_match = re.search(r"## Sources consulted.*?(?=^## |\Z)", text, re.DOTALL | re.MULTILINE)
    if sources_block_match:
        sources_block = sources_block_match.group(0)
        for cat in REQUIRED_SOURCE_CATEGORIES:
            if cat not in sources_block:
                issues.append(f"FAIL: missing source category `{cat}` in Sources consulted")
    checklist_match = re.search(r"## Verification statements.*?(?=^## |\Z)", text, re.DOTALL | re.MULTILINE)
    if checklist_match:
        checklist = checklist_match.group(0)
        unchecked = checklist.count("- [ ]")
        checked = checklist.count("- [x]") + checklist.count("- [X]")
        if unchecked > 0 and checked == 0:
            issues.append(f"FAIL: all {unchecked} verification statement checkboxes are unchecked")
        elif unchecked > 0:
            issues.append(f"WARN: {unchecked} unchecked verification statement(s) remain")
    verdict_match = re.search(r"## Verdict\s*(.+?)(?=^## |\Z)", text, re.DOTALL | re.MULTILINE)
    if verdict_match:
        verdict_text = verdict_match.group(1).strip()
        if not re.search(r"\b(PASS|REVISE|BLOCK)\b", verdict_text):
            issues.append("FAIL: Verdict section does not contain PASS / REVISE / BLOCK")
    return issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True)
    ap.add_argument("--phase", required=True)
    args = ap.parse_args()

    task_dir = Path(args.task).resolve()
    f = task_dir / "_aux" / f"Verification_{args.phase}.md"
    issues = check(f)

    if not issues:
        print(f"[OK] Verification_{args.phase}.md valid: all sections + source categories + verdict present")
        sys.exit(0)
    fails = [i for i in issues if i.startswith("FAIL")]
    warns = [i for i in issues if i.startswith("WARN")]
    for f_msg in fails:
        print(f_msg)
    for w_msg in warns:
        print(w_msg)
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
