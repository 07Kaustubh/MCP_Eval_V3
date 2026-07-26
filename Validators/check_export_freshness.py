#!/usr/bin/env python3
"""
Usage:
    python Validators/check_export_freshness.py <task_dir>          # verify
    python Validators/check_export_freshness.py <task_dir> --pin    # (re)pin current inputs

Pins the S4 input surface by content hash so a silent re-paste cannot invalidate
the reports without a gate noticing.

Why this exists
---------------
S4 reads three things that the operator can replace at any time from the platform:
the two verifier exports and the rubric file. Nothing in the pipeline recorded WHICH
bytes a given S4 pass was reasoning about, so a re-paste left every per-run count,
every bucket call and every all-failing set in the reports silently stale, while
`phase_ready.py` still said the phase was ready and `close_task.py` still said READY.

On Task 44 this happened twice inside one session. Pass 3 was written against a
13:24 export, superseded by 16:18 without anything flagging it. Pass 4 was written
against the 16:18 export and superseded by an 18:20 re-paste the same way, which
moved Opus from 28/33/43/31/32/37 to 32/32/44/32/36/46 and shrank the both-model
all-failing set from six criteria to five. Both times the drift was found by hand.

Contract
--------
`--pin` writes `_aux/S4_input_pin.json` recording the sha256 of each input plus the
derived per-run pass counts. Run it at the START of an S4 pass, immediately after
reading the inputs. Bare invocation re-hashes and FAILS on any drift, naming which
input moved and how the per-run counts changed.

Exit 0 clean, 1 on drift, 2 on usage error.
"""

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INPUTS = ("8a_Verifier_Fails_Opus.txt", "8b_Verifier_Fails_Gemini.txt",
          "8_Verifier_Fails.txt", "7_Rubrics.json")
PIN = "_aux/S4_input_pin.json"


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def per_run_counts(p: Path):
    """Pull the '<n>/<total> criteria passed' header from each Run block."""
    if p.suffix != ".txt":
        return None
    out = []
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"^(\d+)\s*/\s*(\d+)\s+criteria passed\s*$", line.strip())
        if m:
            out.append(int(m.group(1)))
    return out or None


def snapshot(task: Path):
    snap = {}
    for name in INPUTS:
        p = task / name
        if p.is_file() and p.stat().st_size > 0:
            snap[name] = {"sha256": sha256(p), "bytes": p.stat().st_size}
            counts = per_run_counts(p)
            if counts:
                snap[name]["per_run_passed"] = counts
    return snap


def main():
    args = [a for a in sys.argv[1:]]
    if not args:
        print(__doc__)
        return 2
    do_pin = "--pin" in args
    args = [a for a in args if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2

    task = Path(args[0])
    if not task.is_absolute():
        task = ROOT / task
    if not task.is_dir():
        print(f"[FAIL] {task}: not a directory")
        return 1

    cur = snapshot(task)
    if not cur:
        print(f"[SKIP] {task.name}: no verifier export or rubric file present yet")
        return 0

    pin_path = task / PIN
    if do_pin:
        pin_path.parent.mkdir(parents=True, exist_ok=True)
        pin_path.write_text(json.dumps({"task": task.name, "inputs": cur}, indent=1) + "\n",
                            encoding="utf-8")
        print(f"[PINNED] {task.name}: {len(cur)} input(s) recorded to {PIN}")
        for name, meta in cur.items():
            extra = f"  per-run {meta['per_run_passed']}" if "per_run_passed" in meta else ""
            print(f"  {name}  {meta['sha256'][:16]}...  {meta['bytes']}B{extra}")
        return 0

    if not pin_path.is_file():
        print(f"[FAIL] {task.name}: no {PIN}. The S4 inputs were never pinned, so no "
              f"report in this task can be shown to describe the export on disk.")
        print(f"       Run: python Validators/check_export_freshness.py {task} --pin")
        return 1

    pinned = json.loads(pin_path.read_text(encoding="utf-8")).get("inputs", {})
    drift = []
    for name, meta in cur.items():
        old = pinned.get(name)
        if old is None:
            drift.append((name, "NEW input not present at pin time", None, None))
        elif old["sha256"] != meta["sha256"]:
            drift.append((name, "CONTENT CHANGED since pin",
                          old.get("per_run_passed"), meta.get("per_run_passed")))
    for name in pinned:
        if name not in cur:
            drift.append((name, "input REMOVED since pin", None, None))

    if not drift:
        print(f"[OK] {task.name}: all {len(cur)} S4 input(s) match the pin. "
              f"Reports describe the export on disk.")
        return 0

    print(f"[FAIL] {task.name}: {len(drift)} S4 input(s) drifted from the pin.\n")
    for name, why, oldc, newc in drift:
        print(f"  {name}: {why}")
        if oldc and newc and oldc != newc:
            print(f"    per-run passed  pinned: {oldc}")
            print(f"    per-run passed  now   : {newc}")
    print("\nEvery per-run count, bucket call and all-failing set in this task's S4")
    print("reports was derived from the pinned bytes and must be re-derived. Re-run the")
    print("S4 classification loop against the current export, then re-pin.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
