#!/usr/bin/env python3
"""
Usage:
    python Validators/compare_rubrics.py <local_rubrics.json> <platform_paste_back.json>

Diffs two rubric JSON files index-by-index. Exits non-zero on any
count mismatch or per-field text difference (whitespace-trimmed).

Use when re-pasting rubrics from the platform — catches silent platform-side
mutations (reformatting, field stripping, reordering).
"""

import argparse
import json
import sys
from pathlib import Path

FIELDS = ["title", "category", "rubric_category", "criterion", "justification", "evidence"]


def load(p: str):
    path = Path(p)
    if not path.exists():
        raise SystemExit(f"file not found: {p}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise SystemExit(f"{p}: invalid JSON ({e})")
    if not isinstance(data, list):
        raise SystemExit(f"{p}: expected a JSON array")
    return data


def field(item, name):
    if not isinstance(item, dict):
        return ""
    if name in item:
        return str(item[name])
    ann = item.get("annotations")
    if isinstance(ann, dict) and name in ann:
        return str(ann[name])
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("local", help="local rubrics (e.g. Tasks/<id>/7_Rubrics.json)")
    ap.add_argument("platform", help="platform paste-back (e.g. Tasks/<id>/10_Rubrics_Platform.json)")
    args = ap.parse_args()

    a = load(args.local)
    b = load(args.platform)

    diffs = 0
    if len(a) != len(b):
        print(f"COUNT MISMATCH: local={len(a)} platform={len(b)}")
        diffs += 1

    for i in range(max(len(a), len(b))):
        x = a[i] if i < len(a) else None
        y = b[i] if i < len(b) else None
        if x is None:
            print(f"[{i + 1}] only in platform")
            diffs += 1
            continue
        if y is None:
            print(f"[{i + 1}] only in local")
            diffs += 1
            continue
        for f in FIELDS:
            xv, yv = field(x, f).strip(), field(y, f).strip()
            if xv != yv:
                diffs += 1
                print(f"[{i + 1}] {f} differs")
                print(f"  local   : {xv[:200]}")
                print(f"  platform: {yv[:200]}")

    if diffs == 0:
        print("Rubrics match.")
        sys.exit(0)
    print(f"\n{diffs} difference(s) found.")
    sys.exit(1)


if __name__ == "__main__":
    main()
