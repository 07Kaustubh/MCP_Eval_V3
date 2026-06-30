#!/usr/bin/env python3
"""
data.py — smart forwarder.

The pipeline-correct way to split a per-task universe is to write into
Tasks/<TASK_DIR>/_aux/Universe_Split/ via:

    python Validators/split_universe.py Tasks/<TASK_DIR>

This script preserves the old `python data.py <path_to_pgweb.json>` muscle-
memory: if the input path is a Tasks/<TASK_DIR>/3_UniverseDataForThisTask.json,
it forwards to split_universe.py (per-task, no shared-dir collisions). If the
input is anything else, it refuses and points to the legacy script.

Usage:
    python data.py Tasks/<TASK_DIR>/3_UniverseDataForThisTask.json
"""

import os
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python data.py <path_to_per_task_universe_json>", file=sys.stderr)
        print("Example: python data.py Tasks/Task01_abc123/3_UniverseDataForThisTask.json", file=sys.stderr)
        sys.exit(1)

    input_path = Path(sys.argv[1]).resolve()
    if not input_path.is_file():
        print(f"ERROR: file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    # If the input looks like a per-task universe file, forward to the wrapper.
    if input_path.name == "3_UniverseDataForThisTask.json" and input_path.parent.parent.name == "Tasks":
        task_dir = input_path.parent
        print(f"[data.py] Detected per-task universe file. Forwarding to Validators/split_universe.py...")
        print(f"[data.py] Output will go to: {task_dir}/_aux/Universe_Split/")
        wrapper = SCRIPT_DIR / "Validators" / "split_universe.py"
        result = subprocess.run([sys.executable, str(wrapper), str(task_dir)], check=False)
        sys.exit(result.returncode)

    # Otherwise refuse — only per-task inputs are supported. The legacy script
    # that wrote to the shared Brookfield_Base_Universe/Data/ directory has
    # been archived (v21); per-task is the only sanctioned flow.
    print("ERROR: This input does not look like a per-task universe file.", file=sys.stderr)
    print("Expected path shape: Tasks/<TASK_DIR>/3_UniverseDataForThisTask.json", file=sys.stderr)
    sys.exit(2)


if __name__ == "__main__":
    main()
