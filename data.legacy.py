#!/usr/bin/env python3
"""
Usage:  python update_data.py <path_to_pgweb.json>

Reads a pgweb export JSON, splits records by `source` into Data/<source>.json,
and writes a combined Data/Universe_complete_data.json.
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "Data"
COMPLETE_DATA_FILE = "Universe_complete_data.json"


def split_and_write(pgweb_path: Path) -> None:
    print(f"Reading: {pgweb_path}")
    with open(pgweb_path, "r", encoding="utf-8") as f:
        records = json.load(f)

    if not isinstance(records, list):
        print("ERROR: Expected a JSON array at the top level.", file=sys.stderr)
        sys.exit(1)

    # Group by source
    groups: dict[str, list] = defaultdict(list)
    for rec in records:
        source = rec.get("source")
        if source is None:
            print(f"WARNING: record missing 'source' – skipped: {str(rec)[:120]}")
            continue
        groups[source].append(rec)

    # Existing source files (preserve empty ones not in new data)
    existing: set[str] = set()
    for p in DATA_DIR.glob("*.json"):
        if p.stem != Path(COMPLETE_DATA_FILE).stem:
            existing.add(p.stem)

    # Write per-source files
    all_sources = set(groups.keys()) | existing
    for source in sorted(all_sources):
        out = DATA_DIR / f"{source}.json"
        with open(out, "w", encoding="utf-8") as f:
            json.dump(groups.get(source, []), f, indent=2, ensure_ascii=False)
            f.write("\n")

    # Write complete file
    with open(DATA_DIR / COMPLETE_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
        f.write("\n")

    # Summary
    print(f"Total: {len(records)} records across {len(groups)} sources")
    for src in sorted(groups):
        print(f"  {src + '.json':<45} {len(groups[src]):>5}")
    empty = sorted(existing - set(groups.keys()))
    if empty:
        print(f"  (empty): {', '.join(s + '.json' for s in empty)}")
    print("Done.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python update_data.py <pgweb_json_file>", file=sys.stderr)
        sys.exit(1)

    pgweb_path = Path(sys.argv[1]).resolve()
    if not pgweb_path.is_file():
        print(f"ERROR: File not found: {pgweb_path}", file=sys.stderr)
        sys.exit(1)

    split_and_write(pgweb_path)


if __name__ == "__main__":
    main()
