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
import shutil
import sys
from pathlib import Path

try:
    from Validators.universes import get_framework_profile, list_universes
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from universes import get_framework_profile, list_universes

ROOT = Path(__file__).resolve().parent.parent
TASKS_DIR = ROOT / "Tasks"   # default; per-universe override via FRAMEWORKS working_dir_name

TASKS_TEMPLATE_STARPM = ROOT / "Tasks_Template_starpm"
# v21.2: upstream ships per-universe templates (3_UniverseDataForThisTask stub +
# 9_Universe_inject.sql header are universe-flavored). Fall back to the shared
# Brookfield-flavored Tasks_Template when a universe-specific dir is absent.
TEMPLATE_BY_UNIVERSE = {
    "keystone": ROOT / "Tasks_Template_keystone",
    "moveops": ROOT / "Tasks_Template_moveops",
}


def template_root_for(universe):
    cand = TEMPLATE_BY_UNIVERSE.get(universe)
    return cand if cand is not None and cand.is_dir() else ROOT / "Tasks_Template"
V4_QC_PLACEHOLDER_FILES = [
    "9_QC_Feedback.txt",
    "10_PT_Dispute_To_QC_Feedback.txt",
    "11_Final_QC_Validation_On_PT_Dispute.txt",
]

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


def resolve_task_dir_name(arg, work_root=None):
    arg = arg.strip()
    m = re.match(r"^(\d+)_([a-f0-9]+)$", arg)
    if m:
        return arg
    if re.match(r"^[a-f0-9]{8,}$", arg):
        idx = next_index(work_root if work_root is not None else TASKS_DIR)
        return f"{idx}_{arg}"
    raise SystemExit(f"ERROR: '{arg}' is not a recognized task id (expected hex string or <index>_<hex>)")


def copy_template_tree(src, dst):
    """Recursively copy a template dir into dst as writable files/dirs (data only)."""
    for item in sorted(src.rglob("*")):
        rel = item.relative_to(src)
        target = dst / rel
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(item, target)


def scaffold_v4(task_dir, name, universe, review):
    """Scaffold the V4 (dual-model / per_model) task shape from Tasks_Template_starpm."""
    if not TASKS_TEMPLATE_STARPM.is_dir():
        print(f"ERROR: V4 template missing: {TASKS_TEMPLATE_STARPM}", file=sys.stderr)
        sys.exit(1)
    task_dir.parent.mkdir(parents=True, exist_ok=True)
    task_dir.mkdir()
    copy_template_tree(TASKS_TEMPLATE_STARPM, task_dir)
    for fname in V4_QC_PLACEHOLDER_FILES:
        (task_dir / fname).touch()

    print(f"Created: {task_dir}")
    print(f"Mode:    V4 ({universe})")
    print()
    print("Scaffolded the V4 (dual-model) task shape from Tasks_Template_starpm:")
    print("  1/2/3 + 4_Changelog.json + 5/6/7 + 8a/8b + 9_Universe_inject.sql")
    print("  Agent_Responses/Opus|Gemini/Run1..6_Trajectory.json + README.md")
    print(f"  QC/dispute placeholders: {', '.join(V4_QC_PLACEHOLDER_FILES)}")
    print()
    print("Paste these input files NOW (each in its own file):")
    for fname, hint in CB_PASTE_FILES:
        print(f"  {task_dir / fname}")
        print(f"      <- {hint}")
    print()
    print("Drop trajectories per model into:")
    print(f"  {task_dir / 'Agent_Responses' / 'Opus'}/RunN_Trajectory.json")
    print(f"  {task_dir / 'Agent_Responses' / 'Gemini'}/RunN_Trajectory.json")
    print()
    print("Then run, in a fresh chat:")
    if review:
        print(f"  PIPELINE REVIEW - {task_dir.parent.name}/{name}")
    else:
        print(f"  PIPELINE S0 - {task_dir.parent.name}/{name}")


def working_dir_for(universe: str):
    """Per-universe task root. HarmonyGames authors into Generated_Tasks/, not Tasks/."""
    name = get_framework_profile(universe).get("working_dir_name", "Tasks")
    return ROOT / name


def write_universe_marker(task_dir, universe: str) -> None:
    """Persist the universe the operator ASKED for.

    Without this, a freshly scaffolded task carries no universe marker anywhere, so the
    first detect_universe() call scores zero on every signal set and resolves to the
    tie-break default. That answer is then cached to _aux/Universe.txt and read
    unconditionally by every later call, so the mis-detection is sticky and silent.
    The operator already told us the universe on the command line; record it.
    """
    aux = task_dir / "_aux"
    aux.mkdir(parents=True, exist_ok=True)
    (aux / "Universe.txt").write_text(universe + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("task_id_or_full_name")
    ap.add_argument("--review", action="store_true",
                    help="REVIEW mode: scaffold candidate-prefilled 5/6/7/8 files too")
    ap.add_argument("--universe", default="brookfield", choices=list_universes(),
                    help="Target universe. starpm (v4) scaffolds the dual-model V4 shape; others keep the v3 shape.")
    args = ap.parse_args()

    work_root = working_dir_for(args.universe)
    name = resolve_task_dir_name(args.task_id_or_full_name, work_root)
    task_dir = work_root / name

    if task_dir.exists():
        print(f"ERROR: {task_dir} already exists. Refusing to overwrite.", file=sys.stderr)
        sys.exit(1)

    if get_framework_profile(args.universe).get("trajectory_layout") == "per_model":
        scaffold_v4(task_dir, name, args.universe, args.review)
        write_universe_marker(task_dir, args.universe)
        return

    paste_files = REVIEW_PASTE_FILES if args.review else CB_PASTE_FILES
    mode = "REVIEW" if args.review else "CB"

    work_root.mkdir(parents=True, exist_ok=True)
    task_dir.mkdir()
    write_universe_marker(task_dir, args.universe)
    for fname, _ in paste_files:
        (task_dir / fname).touch()
    # v21.2: every universe's upstream Tasks_Template ships injection artifacts.
    # Seed them from the universe-correct template so the CB gets the right
    # universe-flavored authoring header (validated by validate.py --phase injection).
    tmpl = template_root_for(args.universe)
    for fname in ("4_Changelog.json", "9_Universe_inject.sql"):
        src = tmpl / fname
        if src.is_file() and not (task_dir / fname).exists():
            (task_dir / fname).write_bytes(src.read_bytes())
    (task_dir / "Agent_Responses").mkdir()
    (task_dir / "trajectory-runs").mkdir()

    print(f"Created: {task_dir}")
    print(f"Universe: {args.universe}  (recorded in _aux/Universe.txt)")
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
        print(f"  PIPELINE REVIEW - {task_dir.parent.name}/{name}")
        print()
        print("(REVIEW will produce PersonaBrief, Universe_Split, Universe_Index, Fact_Ledger,")
        print(" graph_report; then validate + run councils + FINAL + triage SALVAGEABLE/REBUILD.)")
    else:
        print("Then run, in a fresh chat:")
        print(f"  PIPELINE S0 - {task_dir.parent.name}/{name}")
        print()
        print("(S0 will produce PersonaBrief, Universe_Split, Universe_Index, Fact_Ledger, graph_report.)")


if __name__ == "__main__":
    main()
