#!/usr/bin/env python3
"""
Usage:
    python Validators/phase_ready.py --phase <name> --task <path_to_task_dir>

Refuses to start a phase if upstream artifacts are missing. Catches the
case where an agent silently skipped a previous phase (an architectural
enforcement layer that the runbook STOP gates cannot provide alone).

Phases and the artifacts they require:

  s0        no preconditions (entry point)
  hardness  S0 outputs: _aux/Universe_Split/, _aux/Universe_Index/,
            _aux/Fact_Ledger.json
  s1        HARDNESS output: _aux/Hardness_Plan.md
  s1.5      S1 output: 5_Prompt.txt
  s2        S1 output: 5_Prompt.txt
  s3        S2 output: 6_Oracle_Events.txt + S1 output: 5_Prompt.txt
  final     S3 output: 7_Rubrics.json (+ 5/6 + Hardness_Plan + Fact_Ledger)
  s4        deliverables 5/6/7 + 8_Verifier_Fails.txt (+ trajectory-runs/
            or Agent_Responses/ for parse_trajectories.py)
  review    user-pasted prefilled 5/6/7 + the same S0 outputs as above
  redo      candidate originals to archive (5/6/7) + _aux setup outputs
  compare   7_Rubrics.json + 10_Rubrics_Platform.json

Exits 0 if all required artifacts exist + are non-empty.
Exits 1 with a clear stop-reason listing what is missing.
"""

import argparse
import sys
from pathlib import Path

PHASES = {
    "s0":          [],
    "hardness":    ["_aux/Universe_Split", "_aux/Universe_Index", "_aux/Fact_Ledger.json"],
    "s1":          ["_aux/Hardness_Plan.md"],
    "s1.5":        ["5_Prompt.txt"],
    "s2":          ["5_Prompt.txt"],
    "s3":          ["5_Prompt.txt", "6_Oracle_Events.txt"],
    "final":       ["5_Prompt.txt", "6_Oracle_Events.txt", "7_Rubrics.json",
                    "_aux/Hardness_Plan.md", "_aux/Fact_Ledger.json"],
    "s4":          ["5_Prompt.txt", "6_Oracle_Events.txt", "7_Rubrics.json",
                    "8_Verifier_Fails.txt"],
    "review":      ["5_Prompt.txt", "6_Oracle_Events.txt", "7_Rubrics.json",
                    "3_UniverseDataForThisTask.json"],
    "materialize": ["changes.md", "5_Prompt.txt", "6_Oracle_Events.txt", "7_Rubrics.json",
                    "_aux/Universe_Split", "_aux/Fact_Ledger.json",
                    "_aux/Council_Reports/REVIEW_triage.md"],
    "redo":        ["5_Prompt.txt", "6_Oracle_Events.txt", "7_Rubrics.json"],
    "compare":     ["7_Rubrics.json", "10_Rubrics_Platform.json"],
}

TODO_PHASES = {"s0", "hardness", "s1", "s1.5", "s2", "s3", "final", "s4", "review", "materialize", "redo"}

VERIFICATION_DEPS = {
    "hardness": ["s0"],
    "s1": ["hardness"],
    "s2": ["s1"],
    "s3": ["s2"],
    "final": ["s3"],
    "s4": ["final"],
}


def check(task_dir, path_str):
    p = task_dir / path_str
    if not p.exists():
        return False, "missing"
    if p.is_file() and p.stat().st_size == 0:
        return False, "empty"
    if p.is_dir() and not any(p.iterdir()):
        return False, "empty directory"
    return True, "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", required=True, choices=sorted(PHASES))
    ap.add_argument("--task", required=True)
    args = ap.parse_args()

    task_dir = Path(args.task).resolve()
    if not task_dir.is_dir():
        print(f"ERROR: {task_dir} not a directory", file=sys.stderr)
        sys.exit(2)

    required = PHASES[args.phase]
    if not required:
        print(f"[OK] {args.phase}: no preconditions (entry-point phase)")
        sys.exit(0)

    missing = []
    for path in required:
        ok, reason = check(task_dir, path)
        if not ok:
            missing.append((path, reason))

    if missing:
        print(f"STOP: phase {args.phase.upper()} is not ready — missing upstream artifacts:")
        for path, reason in missing:
            print(f"  - {path}  ({reason})")
        print()
        print("Run the upstream phase first. Phase dependency chain:")
        print("  S0 -> HARDNESS -> S1 -> S1.5 (if linter) -> S2 -> S3 -> FINAL -> upload -> S4")
        print("  REVIEW takes the candidate-prefilled 5/6/7 instead of S1/S2/S3.")
        print("  REDO takes candidate originals + runs HARDNESS -> S1 -> S2 -> S3 -> FINAL.")
        sys.exit(1)

    print(f"[OK] {args.phase}: all {len(required)} upstream artifacts present")
    for path in required:
        print(f"  - {path}")

    if args.phase == "materialize":
        import subprocess
        verifier = Path(__file__).resolve().parent / "verify_universe_atoms.py"
        result = subprocess.run(
            ["python3", str(verifier), "--task", str(task_dir)],
            capture_output=True, text=True,
        )
        first_line = (result.stdout.splitlines() or [""])[0]
        if result.returncode != 0:
            print(f"STOP: verify_universe_atoms.py failed — MATERIALIZE cannot start with universe-atom failures.")
            print(f"  {first_line}")
            print("  Review _aux/Council_Reports/verify_universe_atoms.md, fix the failing atoms in OE / rubrics, then re-run.")
            print("  Override: only with documented justification (the same pattern as Class B linter invalidation).")
            sys.exit(1)
        else:
            print(f"[OK] verify_universe_atoms: clean — {first_line}")

    if args.phase in VERIFICATION_DEPS:
        verifier = Path(__file__).resolve().parent / "check_verification.py"
        for upstream_phase in VERIFICATION_DEPS[args.phase]:
            verif_path = task_dir / "_aux" / f"Verification_{upstream_phase}.md"
            if verif_path.exists() and verif_path.stat().st_size > 0:
                if verifier.is_file():
                    import subprocess
                    result = subprocess.run(
                        ["python3", str(verifier), "--task", str(task_dir), "--phase", upstream_phase],
                        capture_output=True, text=True,
                    )
                    if result.returncode == 0:
                        print(f"[OK] upstream _aux/Verification_{upstream_phase}.md valid — content checked")
                    else:
                        print(f"[FAIL] upstream Verification_{upstream_phase}.md malformed:")
                        for line in result.stdout.splitlines():
                            print(f"    {line}")
                        sys.exit(1)
                else:
                    print(f"[OK] upstream _aux/Verification_{upstream_phase}.md present")
            else:
                print(f"[REMIND] Upstream phase {upstream_phase.upper()} should have produced _aux/Verification_{upstream_phase}.md before this phase runs.")
                print(f"         The v16 cross-source verification discipline requires each phase to declare what it verified against data + eval spec + QC spec.")
                print(f"         If missing, the upstream phase did not record its cross-source check; consider re-running it.")

    if args.phase in TODO_PHASES:
        todo_path = task_dir / "_aux" / f"Todos_{args.phase}.md"
        if todo_path.exists() and todo_path.stat().st_size > 0:
            print(f"[OK] _aux/Todos_{args.phase}.md present ({todo_path.stat().st_size} bytes) — agent TODO discipline confirmed")
        else:
            print(f"[REMIND] Create _aux/Todos_{args.phase}.md as your FIRST action of this phase.")
            print(f"         List atomic todos for every step the runbook prescribes; mark in_progress / completed as you go.")
            print(f"         This is the v11 E1 operator-discipline gate. AUDIT will check this file exists before exit.")

        reads_path = task_dir / "_aux" / f"Reads_{args.phase}.md"
        if reads_path.exists() and reads_path.stat().st_size > 0:
            print(f"[OK] _aux/Reads_{args.phase}.md present ({reads_path.stat().st_size} bytes) — reference-doc reading log confirmed")
        else:
            print(f"[REMIND] Create _aux/Reads_{args.phase}.md as your SECOND action of this phase.")
            print(f"         Log every QC spec doc / Reference card / Eval spec you read with one line each:")
            print(f"         `Docs/7_QC_Spec_Doc1.json :: <one-line summary of what you confirmed>`")
            print(f"         This is the v11 E2 compliance gate — agents that skip the spec docs are caught here.")
    sys.exit(0)


if __name__ == "__main__":
    main()
