#!/usr/bin/env python3
"""
check_tool_catalog.py — version-pin tool catalog hashes per universe.

Computes SHA256 of <universe>/<NN>_Server_Tools_Details.json + compares against
Validators/tool_catalog_hashes.json. WARN on drift (catalog content changed),
useful to surface upstream Brookfield/KeyStone universe updates that would
make the validator's parameter-strictness checks silently stale.

Usage:
    python3 Validators/check_tool_catalog.py                # verify all universes
    python3 Validators/check_tool_catalog.py --universe brookfield
    python3 Validators/check_tool_catalog.py --update      # update the pinned hashes
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HASH_FILE = Path(__file__).resolve().parent / "tool_catalog_hashes.json"


def compute_hash(path: Path) -> str:
    """Hash a catalog with line endings normalised to LF.

    The pinned hashes were captured on macOS. A Windows checkout with
    core.autocrlf=true materialises the same catalog with CRLF, so a raw byte hash
    reported DRIFT on all five universes at once for content that had not changed.
    That made the printed "Run with --update" advice actively dangerous: on Windows it
    rewrote every pinned hash with a CRLF value and broke the baseline for everyone else.
    Normalising here means only a real content change can drift, which is what makes
    --update safe to follow.

    Line endings ONLY. Unlike the validator reports, a catalog is JSON, where a
    backslash is an escape character rather than a path separator - rewriting it would
    change what the hash means. Verified: all five catalogs contain zero backslash bytes,
    so there is nothing separator-shaped to normalise anyway.
    """
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--universe")
    ap.add_argument("--update", action="store_true")
    args = ap.parse_args()

    pinned = json.loads(HASH_FILE.read_text(encoding="utf-8"))

    universes = [args.universe] if args.universe else list(pinned.keys())
    any_drift = False
    for u in universes:
        if u not in pinned:
            print(f"[WARN] universe `{u}` not in pinned hashes")
            continue
        path = ROOT / pinned[u]["path"]
        if not path.is_file():
            print(f"[FAIL] {u}: tool catalog missing at {path}")
            any_drift = True
            continue
        actual = compute_hash(path)
        expected = pinned[u]["sha256"]
        if actual == expected:
            print(f"[OK] {u}: catalog hash matches ({actual[:16]}...)")
        else:
            print(f"[DRIFT] {u}: catalog changed")
            print(f"  expected: {expected}")
            print(f"  actual:   {actual}")
            print(f"  Run with --update if change is intentional and re-test validators.")
            if args.update:
                pinned[u]["sha256"] = actual
                print(f"  -> updated pinned hash for {u}")
            any_drift = True

    if args.update:
        HASH_FILE.write_text(json.dumps(pinned, indent=2) + "\n", encoding="utf-8")
        print(f"\nUpdated {HASH_FILE}")
        sys.exit(0)

    sys.exit(1 if any_drift else 0)


if __name__ == "__main__":
    main()
