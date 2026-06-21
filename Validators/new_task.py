#!/usr/bin/env python3
"""
Usage:
    python Validators/new_task.py <task_id_or_full_name>

Examples:
    python Validators/new_task.py 6a35abc123def...     # auto-picks next index
    python Validators/new_task.py 25_6a35abc123def...  # uses given index

Creates a fresh per-task folder under Tasks/ with empty template files for
the 3 user-pasted inputs. Refuses to overwrite an existing folder. Prints
the exact paste instructions + next-trigger nudge.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TASKS_DIR = ROOT / "Tasks"

USER_PASTE_FILES = [
    ("1_Business_Function.txt", "Paste the assigned business function."),
    ("2_Persona.txt",            "Paste the assigned persona."),
    ("3_UniverseDataForThisTask.json", "Paste the per-task universe data (pgweb export)."),
]


def next_index(tasks_dir):
    max_n = 0
    if not tasks_dir.is_dir():
        return 1
    for p in tasks_dir.iterdir():
        if not p.is_dir():
            continue
        m = re.match(r"^(\d+)_[a-f0-9]+$", p.name)
        if m:
            n = int(m.group(1))
            if n > max_n:
                max_n = n
    return max_n + 1


def resolve_task_dir_name(arg):
    arg = arg.strip()
    m = re.match(r"^(\d+)_([a-f0-9]+)$", arg)
    if m:
        return arg
    if re.match(r"^[a-f0-9]{8,}$", arg):
        idx = next_index(TASKS_DIR)
        return f"{idx}_{arg}"
    raise SystemExit(f"ERROR: '{arg}' is not a recognized task id (expected hex string or <index>_<hex>)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("task_id_or_full_name")
    args = ap.parse_args()

    name = resolve_task_dir_name(args.task_id_or_full_name)
    task_dir = TASKS_DIR / name

    if task_dir.exists():
        print(f"ERROR: {task_dir} already exists. Refusing to overwrite.", file=sys.stderr)
        sys.exit(1)

    TASKS_DIR.mkdir(parents=True, exist_ok=True)
    task_dir.mkdir()
    for fname, _ in USER_PASTE_FILES:
        (task_dir / fname).touch()
    (task_dir / "Agent_Responses").mkdir()
    (task_dir / "trajectory-runs").mkdir()

    print(f"Created: {task_dir}")
    print()
    print("Paste these 3 files NOW (each in its own file):")
    for fname, hint in USER_PASTE_FILES:
        print(f"  {task_dir / fname}")
        print(f"      <- {hint}")
    print()
    print("Then run, in a fresh chat:")
    print(f"  PIPELINE S0 - Tasks/{name}")
    print()
    print("(S0 will produce PersonaBrief, Universe_Split, Universe_Index, Fact_Ledger, graph_report.)")


if __name__ == "__main__":
    main()
