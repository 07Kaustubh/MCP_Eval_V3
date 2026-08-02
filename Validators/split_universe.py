#!/usr/bin/env python3
"""
split_universe.py — patched wrapper around data.py.

Writes per-task split into Tasks/<TASK_DIR>/_aux/Universe_Split/
instead of the shared Brookfield_Base_Universe/Data/ directory.
This prevents cross-task collisions when multiple tasks are in flight.

Usage:
    python Validators/split_universe.py <path_to_task_dir>

Example:
    python Validators/split_universe.py Tasks/Task01_abc123
"""

import json
import re
import sys
import hashlib
from collections import defaultdict
from pathlib import Path

COMPLETE_DATA_FILE = "Universe_complete_data.json"


_UNSAFE_SOURCE_CHARS = re.compile(r"[^A-Za-z0-9._-]")


def _safe_source_name(source: str) -> str:
    """Turn a record's `source` into a filename that cannot escape the split directory.

    `out_dir / f"{source}.json"` is unsafe: pathlib DISCARDS out_dir when the right-hand
    side is absolute, so a single upstream row whose source began with "/" wrote outside the
    task entirely. In the HarmonyGames base export exactly one source is absolute (it carries
    the fixture author's own Downloads path) and 92 more contain "..". The v3-family sources
    are plain dotted tokens and are unaffected: sanitising them is a no-op, verified by the
    byte-identical regression reports.
    """
    return _UNSAFE_SOURCE_CHARS.sub("_", str(source).strip("/")) or "unnamed_source"


def split_and_write(task_dir: Path) -> int:
    task_dir = task_dir.resolve()
    src = task_dir / "3_UniverseDataForThisTask.json"
    if not src.is_file():
        print(f"ERROR: not found: {src}", file=sys.stderr)
        return 1

    out_dir = task_dir / "_aux" / "Universe_Split"
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Reading: {src}")
    # Route through the contract-aware accessor. For the four per_task_json universes this
    # is byte-identical to reading the file directly; for HarmonyGames it resolves the
    # pointer to the base export plus changelog. It also turns "pointer fed to the
    # per_task_json reader" from a silent empty split into a hard, actionable error.
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from universe_data_source import load_universe_records, UniverseDataError
        records, _meta = load_universe_records(task_dir)
        if _meta["contract"] != "per_task_json":
            print(f"contract: {_meta['contract']} (base={_meta['base_dir']}, "
                  f"changelog rows={_meta['changelog_rows']})")
    except UniverseDataError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

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
        out = out_dir / f"{_safe_source_name(source)}.json"
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
