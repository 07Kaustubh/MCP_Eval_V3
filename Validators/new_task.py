#!/usr/bin/env python3
"""
Usage:
    python Validators/new_task.py <task_id_or_full_name> [--review]

Examples:
    python Validators/new_task.py 6a35abc123def...              # CB mode, auto-index
    python Validators/new_task.py 25_6a35abc123def...           # CB mode, given index
    python Validators/new_task.py 6a35abc123def... --review     # REVIEW mode, auto-index

CB mode scaffolds the 3 user-paste files (1/2/3 + folders for trajectories).
REVIEW mode adds the candidate-prefilled 5/6/7 + 8 placeholders so the
reviewer can paste the candidate's deliverables.

Refuses to overwrite an existing folder. Prints exact paste paths + next-
trigger nudge.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TASKS_DIR = ROOT / "Tasks"

CB_PASTE_FILES = [
    ("1_Business_Function.txt", "Paste the assigned business function."),
    ("2_Persona.txt",            "Paste the assigned persona."),
    ("3_UniverseDataForThisTask.json", "Paste the per-task universe data (pgweb export)."),
]

REVIEW_PASTE_FILES = CB_PASTE_FILES + [
    ("5_Prompt.txt",          "Paste the candidate's prefilled prompt."),
    ("6_Oracle_Events.txt",    "Paste the candidate's prefilled Oracle Events."),
    ("7_Rubrics.json",         "Paste the candidate's prefilled rubrics (JSON array)."),
    ("8_Verifier_Fails.txt",   "Paste the candidate's verifier-fails text IF the candidate already submitted and ran trajectories. Otherwise leave empty."),
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
    ap.add_argument("--review", action="store_true",
                    help="REVIEW mode: scaffold candidate-prefilled 5/6/7/8 files too")
    args = ap.parse_args()

    name = resolve_task_dir_name(args.task_id_or_full_name)
    task_dir = TASKS_DIR / name

    if task_dir.exists():
        print(f"ERROR: {task_dir} already exists. Refusing to overwrite.", file=sys.stderr)
        sys.exit(1)

    paste_files = REVIEW_PASTE_FILES if args.review else CB_PASTE_FILES
    mode = "REVIEW" if args.review else "CB"

    TASKS_DIR.mkdir(parents=True, exist_ok=True)
    task_dir.mkdir()
    for fname, _ in paste_files:
        (task_dir / fname).touch()
    (task_dir / "Agent_Responses").mkdir()
    (task_dir / "trajectory-runs").mkdir()

    print(f"Created: {task_dir}")
    print(f"Mode:    {mode}")
    print()
    print(f"Paste these {len(paste_files)} files NOW (each in its own file):")
    for fname, hint in paste_files:
        print(f"  {task_dir / fname}")
        print(f"      <- {hint}")
    print()
    if args.review:
        print(f"Also (OPTIONAL): if the candidate already ran trajectories on the platform,")
        print(f"drop the JSON files into:")
        print(f"  {task_dir / 'trajectory-runs'}/")
        print(f"and parse_trajectories.py will pick them up during REVIEW step 3.")
        print()
        print("Then run, in a fresh chat:")
        print(f"  PIPELINE REVIEW - Tasks/{name}")
        print()
        print("(REVIEW will produce PersonaBrief, Universe_Split, Universe_Index, Fact_Ledger,")
        print(" graph_report; then validate + run councils + FINAL + triage SALVAGEABLE/REBUILD.)")
    else:
        print("Then run, in a fresh chat:")
        print(f"  PIPELINE S0 - Tasks/{name}")
        print()
        print("(S0 will produce PersonaBrief, Universe_Split, Universe_Index, Fact_Ledger, graph_report.)")


if __name__ == "__main__":
    main()
