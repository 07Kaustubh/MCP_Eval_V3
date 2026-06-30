#!/usr/bin/env python3
"""
check_eval_hashes.py — Eval-file drift detector (v21).

Mirrors check_tool_catalog.py shape, but pins SHA256 of Evals/*.md (and
Evals_keystone/, Evals_moveops/) instead of tool catalogs. WARN-only — phase
proceeds on drift; this surfaces upstream Brookfield/KeyStone/MoveOps Eval
spec updates so the pipeline operator notices and runs an intentional sync.

Usage:
    python3 Validators/check_eval_hashes.py                # verify all Evals
    python3 Validators/check_eval_hashes.py --update       # repin baseline
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HASH_FILE = Path(__file__).resolve().parent / "eval_file_hashes.json"


def compute_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--update", action="store_true")
    args = ap.parse_args()

    if not HASH_FILE.is_file():
        print(f"ERROR: {HASH_FILE} not found", file=sys.stderr)
        sys.exit(2)

    pinned = json.loads(HASH_FILE.read_text(encoding="utf-8"))
    any_drift = False
    any_placeholder = False
    placeholders_updated = 0

    for rel_path, expected in pinned.items():
        p = ROOT / rel_path
        if not p.is_file():
            print(f"[FAIL] {rel_path}: file missing on disk")
            any_drift = True
            continue

        actual = compute_hash(p)

        if expected == "PLACEHOLDER_RUN_UPDATE":
            any_placeholder = True
            if args.update:
                pinned[rel_path] = actual
                placeholders_updated += 1
                print(f"[POPULATE] {rel_path}: {actual[:16]}...")
            else:
                print(f"[REMIND] {rel_path}: PLACEHOLDER_RUN_UPDATE — run with --update to populate")
            continue

        if actual == expected:
            print(f"[OK] {rel_path}: hash matches ({actual[:16]}...)")
        else:
            print(f"[DRIFT] {rel_path}: content changed")
            print(f"  expected: {expected}")
            print(f"  actual:   {actual}")
            print(f"  Upstream Eval text may have changed; consult AGENTS.md 'Pipeline Deviations' table.")
            print(f"  Run with --update once the change is intentional and re-tested.")
            if args.update:
                pinned[rel_path] = actual
                print(f"  -> updated pinned hash for {rel_path}")
            any_drift = True

    if args.update:
        HASH_FILE.write_text(json.dumps(pinned, indent=2) + "\n", encoding="utf-8")
        if placeholders_updated:
            print(f"\nPopulated {placeholders_updated} placeholder(s); pinned {HASH_FILE} updated.")
        else:
            print(f"\nUpdated {HASH_FILE}")
        sys.exit(0)

    if any_drift:
        sys.exit(1)
    if any_placeholder:
        sys.exit(0)
    sys.exit(0)


if __name__ == "__main__":
    main()
