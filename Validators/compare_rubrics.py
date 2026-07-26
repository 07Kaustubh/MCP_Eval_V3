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
import builtins
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

    # Knowledge_Flow.md declares COMPARE's output as `_aux/Compare_Report.md`. Until v23 the
    # script only printed to stdout, so that contract was false and nothing downstream could
    # read the diff. Tee every line to the report alongside stdout.
    _lines = []
    _stdout_print = builtins.print

    def print(*a, **k):  # noqa: A001 - deliberate shadow, scoped to main()
        _stdout_print(*a, **k)
        _lines.append(" ".join(str(x) for x in a))

    def _write_report(verdict):
        out = Path(args.local).resolve().parent / "_aux" / "Compare_Report.md"
        try:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(
                "# COMPARE: local rubrics vs platform paste-back\n\n"
                f"- local: `{args.local}`\n- platform: `{args.platform}`\n"
                f"- verdict: **{verdict}**\n\n```\n" + "\n".join(_lines) + "\n```\n",
                encoding="utf-8")
            _stdout_print(f"\nWrote {out}")
        except OSError as e:
            _stdout_print(f"\n[warn] could not write Compare_Report.md: {e}")

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
        _write_report("MATCH")
        sys.exit(0)
    print(f"\n{diffs} difference(s) found.")
    _write_report(f"{diffs} DIFFERENCE(S)")
    sys.exit(1)


if __name__ == "__main__":
    main()
