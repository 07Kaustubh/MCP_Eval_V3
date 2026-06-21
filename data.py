#!/usr/bin/env python3
"""
data.py — smart forwarder.

The pipeline-correct way to split a per-task universe is to write into
<TASK_DIR>/_aux/Universe_Split/ via:

    python Validators/split_universe.py <TASK_DIR>

This script preserves the old `python data.py <path_to_pgweb.json>` muscle-
memory: if the input path is a <TASK_DIR>/3_UniverseDataForThisTask.json,
it forwards to split_universe.py (per-task, no shared-dir collisions). If the
input is anything else, it refuses and points to the legacy script.

Usage:
    python data.py <TASK_DIR>/3_UniverseDataForThisTask.json
"""

import os
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python data.py <path_to_per_task_universe_json>", file=sys.stderr)
        print("Example: python data.py <TASK_DIR>/3_UniverseDataForThisTask.json", file=sys.stderr)
        sys.exit(1)

    input_path = Path(sys.argv[1]).resolve()
    if not input_path.is_file():
        print(f"ERROR: file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    # If the input looks like a per-task universe file, forward to the wrapper.
    # Match on filename only; active task dirs sit at the repo root (no Tasks/ parent).
    if input_path.name == "3_UniverseDataForThisTask.json":
        task_dir = input_path.parent
        print(f"[data.py] Detected per-task universe file. Forwarding to Validators/split_universe.py...")
        print(f"[data.py] Output will go to: {task_dir}/_aux/Universe_Split/")
        wrapper = SCRIPT_DIR / "Validators" / "split_universe.py"
        result = subprocess.run([sys.executable, str(wrapper), str(task_dir)], check=False)
        sys.exit(result.returncode)

    # Otherwise refuse — the legacy script overwrites a shared directory and
    # corrupts parallel work across tasks.
    print("ERROR: This input does not look like a per-task universe file.", file=sys.stderr)
    print("Expected path shape: <TASK_DIR>/3_UniverseDataForThisTask.json", file=sys.stderr)
    print("", file=sys.stderr)
    print("If you really need the legacy behavior (writes to shared", file=sys.stderr)
    print("Brookfield_Base_Universe/Data/ and overwrites parallel work), run", file=sys.stderr)
    print("data.legacy.py directly. Be aware this can corrupt other tasks.", file=sys.stderr)
    sys.exit(2)


if __name__ == "__main__":
    main()
