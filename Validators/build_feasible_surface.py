#!/usr/bin/env python3
"""
build_feasible_surface.py — per-task feasible-surface map (v18).

Scans `_aux/Universe_Split/<table>.json` per task. For each table, extracts
distinct values of enum-like columns (status / state / category / type /
classification / kind / lifecycle / phase). Writes `_aux/Feasible_Surface.json`.

Validator cross-references rubric values against this map; a rubric testing
`status = "finalized"` for a Brookfield JE (where valid statuses are
{draft, submitted, approved, posted, reversed}) gets flagged as
universe-contradicting.

Universe-aware: different tables per universe.

Usage:
    python3 Validators/build_feasible_surface.py Tasks/<TASK_DIR>
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict

ROOT = Path(__file__).resolve().parent.parent

try:
    from Validators.universes import detect_universe, get_universe_constants
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from universes import detect_universe, get_universe_constants


ENUM_COLUMN_HINTS = (
    "status", "state", "category", "type", "classification", "kind",
    "lifecycle", "phase", "stage", "milestone", "milestone_status",
    "approval_status", "review_status", "resolution_status", "exception_type",
    "retention_policy_code", "exception_state", "channel_type",
)


def build(task_dir: Path) -> Dict[str, Dict]:
    universe = detect_universe(task_dir)
    universe_split_dir = task_dir / "_aux" / "Universe_Split"
    if not universe_split_dir.is_dir():
        return {"meta": {"universe": universe, "tables_scanned": 0, "note": "no Universe_Split/ — run S0 first"}}

    feasible: Dict[str, Dict] = {"meta": {"universe": universe, "tables_scanned": 0}, "tables": {}}
    for table_file in sorted(universe_split_dir.glob("*.json")):
        if table_file.name == "Universe_complete_data.json":
            continue
        try:
            data = json.loads(table_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if not isinstance(data, list):
            continue
        feasible["meta"]["tables_scanned"] += 1
        table_name = table_file.stem
        table_enums: Dict[str, list] = {}
        for row in data[:5000]:
            if not isinstance(row, dict):
                continue
            rd = row.get("row_data", row)
            if isinstance(rd, str):
                try:
                    rd = json.loads(rd)
                except json.JSONDecodeError:
                    continue
            if not isinstance(rd, dict):
                continue
            for col, val in rd.items():
                if not isinstance(col, str):
                    continue
                if any(hint in col.lower() for hint in ENUM_COLUMN_HINTS):
                    if val is None:
                        continue
                    sval = str(val)
                    if len(sval) > 60:
                        continue
                    table_enums.setdefault(col, [])
                    if sval not in table_enums[col]:
                        if len(table_enums[col]) < 50:
                            table_enums[col].append(sval)
        if table_enums:
            feasible["tables"][table_name] = {k: sorted(v) for k, v in table_enums.items()}
    return feasible


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("task_dir")
    args = ap.parse_args()

    task_dir = Path(args.task_dir).resolve()
    if not task_dir.is_dir():
        print(f"ERROR: {task_dir} not a directory", file=sys.stderr)
        sys.exit(2)

    feasible = build(task_dir)
    out_dir = task_dir / "_aux"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "Feasible_Surface.json"
    out_file.write_text(json.dumps(feasible, indent=2, default=str), encoding="utf-8")

    tables = len(feasible.get("tables", {}))
    enum_cols = sum(len(t) for t in feasible.get("tables", {}).values())
    print(f"[OK] Feasible_Surface: {tables} tables with enums, {enum_cols} enum columns total -> {out_file}")


if __name__ == "__main__":
    main()
