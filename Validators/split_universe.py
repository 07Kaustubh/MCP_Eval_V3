#!/usr/bin/env python3
"""
split_universe.py — patched wrapper around data.py.

Writes per-task split into <TASK_DIR>/_aux/Universe_Split/
instead of the shared Brookfield_Base_Universe/Data/ directory.
This prevents cross-task collisions when multiple tasks are in flight.

Usage:
    python Validators/split_universe.py <path_to_task_dir>

Example:
    python Validators/split_universe.py <TASK_DIR>
"""

import json
import sys
import hashlib
from collections import defaultdict
from pathlib import Path

COMPLETE_DATA_FILE = "Universe_complete_data.json"


def split_and_write(task_dir: Path) -> int:
    task_dir = task_dir.resolve()
    src = task_dir / "3_UniverseDataForThisTask.json"
    if not src.is_file():
        print(f"ERROR: not found: {src}", file=sys.stderr)
        return 1

    out_dir = task_dir / "_aux" / "Universe_Split"
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Reading: {src}")
    with open(src, "r", encoding="utf-8") as f:
        records = json.load(f)

    if not isinstance(records, list):
        print("ERROR: top-level JSON must be an array.", file=sys.stderr)
        return 1

    groups: dict[str, list] = defaultdict(list)
    missing_source = 0
    for rec in records:
        source = rec.get("source")
        if source is None:
            missing_source += 1
            continue
        groups[source].append(rec)

    for source in sorted(groups):
        out = out_dir / f"{source}.json"
        with open(out, "w", encoding="utf-8") as f:
            json.dump(groups[source], f, indent=2, ensure_ascii=False)
            f.write("\n")

    with open(out_dir / COMPLETE_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
        f.write("\n")

    with open(src, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()
    with open(task_dir / "_aux" / "data_hash.txt", "w", encoding="utf-8") as f:
        f.write(h + "\n")

    print(f"Total: {len(records)} records across {len(groups)} services")
    for src_name in sorted(groups):
        print(f"  {src_name + '.json':<45} {len(groups[src_name]):>6}")
    if missing_source:
        print(f"  WARNING: {missing_source} records had no 'source' field")
    print(f"sha256: {h}")
    print(f"Output: {out_dir}")
    return 0


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python Validators/split_universe.py <path_to_task_dir>", file=sys.stderr)
        sys.exit(1)
    code = split_and_write(Path(sys.argv[1]))
    sys.exit(code)


if __name__ == "__main__":
    main()
