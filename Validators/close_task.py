#!/usr/bin/env python3
"""
Usage:
    python Validators/close_task.py <path_to_task_dir>

Wraps up a finished task. Verifies all required deliverables are present
(per the CB or Review flow), prints what would be missing if anything is,
and reports the trajectory verdict if trajectories exist. Read-only:
does NOT modify or move files.

Use this as the final sanity check before declaring a task done. Refuses
to greenlight if the FINAL council report doesn't show PASS, or if
parse_trajectories says REBUILD_CANDIDATE.
"""

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED_FOR_SHIP = [
    "1_Business_Function.txt",
    "2_Persona.txt",
    "3_UniverseDataForThisTask.json",
    "5_Prompt.txt",
    "6_Oracle_Events.txt",
    "7_Rubrics.json",
]

REVIEW_ARTIFACTS = [
    "changes.md",
    "13_Feedback.txt",
]


def nonempty(p):
    return p.exists() and (p.is_dir() or p.stat().st_size > 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("task_dir")
    args = ap.parse_args()
    task_dir = Path(args.task_dir).resolve()
    if not task_dir.is_dir():
        print(f"ERROR: {task_dir} not a directory", file=sys.stderr)
        sys.exit(2)

    missing = [f for f in REQUIRED_FOR_SHIP if not nonempty(task_dir / f)]
    has_review = nonempty(task_dir / "changes.md") or nonempty(task_dir / "13_Feedback.txt")
    flow = "REVIEW" if has_review else "CB"

    print(f"=== Closing task: {task_dir.name} ===")
    print(f"Flow detected: {flow}")
    print()

    if missing:
        print(f"NOT READY TO CLOSE — missing required artifacts:")
        for f in missing:
            print(f"  - {f}")
        print()

    final_report = task_dir / "_aux" / "Council_Reports" / "FINAL_council.md"
    final_pass = False
    if final_report.is_file():
        text = final_report.read_text(encoding="utf-8")
        final_pass = bool(re.search(r"VERDICT\s*:\s*PASS", text, re.IGNORECASE))
        print(f"FINAL council:    {'PASS' if final_pass else 'NOT PASS (or no PASS verdict found)'}")
    else:
        print(f"FINAL council:    not run (no {final_report.relative_to(task_dir)})")

    traj_stats = task_dir / "_aux" / "Trajectory_Stats.json"
    traj_verdict = None
    if traj_stats.is_file():
        try:
            data = json.loads(traj_stats.read_text(encoding="utf-8"))
            traj_verdict = data.get("verdict")
            print(f"Trajectory stats: verdict={traj_verdict}  avg_tool_calls={data.get('avg_tool_calls_total')}  pass@1={data.get('verifier_fails', {}).get('pass_at_1') if data.get('verifier_fails') else 'n/a'}")
        except json.JSONDecodeError:
            print(f"Trajectory stats: file exists but invalid JSON")
    else:
        print(f"Trajectory stats: not run (no {traj_stats.relative_to(task_dir)})")

    review_missing = []
    if flow == "REVIEW":
        print()
        print("Review artifacts:")
        for f in REVIEW_ARTIFACTS:
            ok = nonempty(task_dir / f)
            mark = "OK" if ok else "MISSING"
            print(f"  [{mark}] {f}")
            if not ok:
                review_missing.append(f)
        for f in ("14_Updated_Oracle_Events.txt", "15_Updated_Rubrics.json"):
            mark = "present" if nonempty(task_dir / f) else "n/a (no Applied rows)"
            print(f"  [{mark}] {f}")

    print()
    ready = (not missing) and (not review_missing) and (final_pass or not final_report.exists()) and (traj_verdict in (None, "OK"))
    if ready:
        print("READY TO CLOSE.")
        print()
        print("Recommended next actions before declaring done:")
        print("  1. If your task surfaced a novel Opus 4.8 failure pattern: append a finding to Submitted-Tasks/_meta/Learnings.md.")
        print("  2. If REDO was used at any point: confirm Submitted-Tasks/_meta/Hardness_Patterns_Log.md was updated.")
        print("  3. If a linter justification was sent: confirm Submitted-Tasks/_meta/Linter_Justifications.md was updated.")
        print("  4. If a similarity pivot was used: confirm Submitted-Tasks/_meta/Similarity_Log.md was updated.")
        print("  5. If trajectory data is here, confirm the stump hypothesis vs actual fails in Submitted-Tasks/_meta/Stump_Hypotheses.md.")
        sys.exit(0)

    print("NOT READY — fix the items above first.")
    sys.exit(1)


if __name__ == "__main__":
    main()
