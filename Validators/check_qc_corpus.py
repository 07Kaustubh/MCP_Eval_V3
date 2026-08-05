#!/usr/bin/env python3
"""
check_qc_corpus.py - QC ground-truth corpus drift detector (v22).

Mirrors check_eval_hashes.py / check_tool_catalog.py, but pins the LABELED QC
CORPORA under QC_Tasks/. Those corpora are the ground truth that
`qc_verdict.py selftest` grades itself against (138/138 bucket-correct across
V3_Buckets, V3.1_Buckets, V2.1_Buckets, V4_Tasks, V5_HG_Buckets).

WHY THIS EXISTS
---------------
On 2026-08-06 the HarmonyGames drop changed 35 of 112 corpus files - including
7_Rubrics.json, 8_Verifier_Fails.txt, 6_Oracle_Events.txt and 12 trajectories -
and NOTHING caught it:

  * check_source_sync.py did not list QC_Tasks in its SURFACES table at all, and
    even now that it does, it requires `--source <extracted drop>`. An operator
    without the drop on disk cannot run it, and it can never see a REPO-SIDE edit.
  * qc_verdict.py selftest kept reporting 10/10 bucket-correct, because the labels
    still matched the (stale) artifacts. A green selftest is not evidence the
    corpus is current.

Industry practice for exactly this failure is to treat a golden/ground-truth set
as a VERSIONED artifact pinned by content hash, never as a frozen fixture, and to
treat modifying a labeled case as production risk rather than housekeeping. This
checker is the mechanical half of that: it cannot tell you a label is wrong, but
it refuses to let the corpus move without someone saying so out loud.

GRANULARITY
-----------
Per TASK, not per file. 1,476 files would make the manifest unreadable and would
rot on every whitespace change; a per-task rollup still names the exact task that
moved, which is the actionable unit. Each task hash is sha256 over the sorted
`relpath\\0filehash` lines beneath that task directory, so a rename, a deletion and
a content edit are all caught.

Usage:
    python3 Validators/check_qc_corpus.py            # verify (non-zero on drift)
    python3 Validators/check_qc_corpus.py --update   # re-pin after an INTENTIONAL sync
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HASH_FILE = Path(__file__).resolve().parent / "qc_corpus_hashes.json"

# Corpus dir -> the framework whose verdict logic it pins. Kept explicit rather than
# globbed so a stray directory under QC_Tasks/ cannot silently join the ground truth.
CORPORA = {
    "V3_Buckets": "v3 (Brookfield)",
    "V3.1_Buckets": "v3.1 (KeyStone)",
    "V2.1_Buckets": "v2.1 (MoveOps)",
    "V4_Tasks": "v4 (StarPM)",
    "V5_HG_Buckets": "hg (HarmonyGames)",
}


def _file_sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def task_hash(task_dir: Path) -> str:
    """sha256 over every file beneath a task, path-sorted, path included.

    Path is folded in so a rename is drift. Files are streamed so a large
    trajectory JSON cannot blow memory (AGENTS.md rule 33).
    """
    parts = []
    for f in sorted(p for p in task_dir.rglob("*") if p.is_file()):
        parts.append(f"{f.relative_to(task_dir).as_posix()}\0{_file_sha(f)}")
    return hashlib.sha256("\n".join(parts).encode("utf-8")).hexdigest()


def scan() -> dict:
    out = {}
    for corpus in CORPORA:
        root = ROOT / "QC_Tasks" / corpus
        if not root.is_dir():
            continue
        entry = {}
        for bucket in sorted(p for p in root.iterdir() if p.is_dir()):
            for task in sorted(p for p in bucket.iterdir() if p.is_dir()):
                entry[f"{bucket.name}/{task.name}"] = task_hash(task)
        entry["_tasks"] = len(entry)
        entry["_files"] = sum(1 for p in root.rglob("*") if p.is_file())
        out[corpus] = entry
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--update", action="store_true",
                    help="re-pin after an INTENTIONAL corpus sync; re-run qc_verdict selftest first")
    args = ap.parse_args()

    current = scan()

    if args.update:
        HASH_FILE.write_text(json.dumps(current, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        total = sum(v["_tasks"] for v in current.values())
        print(f"[UPDATED] {HASH_FILE.name}: {len(current)} corpora, {total} tasks pinned")
        print("   Re-run `qc_verdict.py selftest <corpus>` for every corpus before trusting this.")
        return 0

    if not HASH_FILE.is_file():
        print(f"ERROR: {HASH_FILE} not found. Run --update to create the baseline.", file=sys.stderr)
        return 2

    pinned = json.loads(HASH_FILE.read_text(encoding="utf-8"))
    findings = []

    for corpus, label in CORPORA.items():
        if corpus not in current:
            if corpus in pinned:
                findings.append(f"[FAIL] {corpus}: pinned but MISSING from disk")
            continue
        if corpus not in pinned:
            findings.append(f"[FAIL] {corpus}: present on disk but NOT pinned ({current[corpus]['_tasks']} tasks)")
            continue
        cur, pin = current[corpus], pinned[corpus]
        cur_tasks = {k: v for k, v in cur.items() if not k.startswith("_")}
        pin_tasks = {k: v for k, v in pin.items() if not k.startswith("_")}
        added = sorted(set(cur_tasks) - set(pin_tasks))
        removed = sorted(set(pin_tasks) - set(cur_tasks))
        moved = sorted(k for k in set(cur_tasks) & set(pin_tasks) if cur_tasks[k] != pin_tasks[k])
        for t in added:
            findings.append(f"[FAIL] {corpus}/{t}: NEW task not in the pinned ground truth")
        for t in removed:
            findings.append(f"[FAIL] {corpus}/{t}: pinned task REMOVED from disk")
        for t in moved:
            findings.append(f"[FAIL] {corpus}/{t}: CONTENT CHANGED since it was pinned")
        if not (added or removed or moved):
            print(f"[OK] {corpus}: {cur['_tasks']} tasks / {cur['_files']} files match the pin ({label})")

    if findings:
        print()
        for f in findings:
            print(f"  {f}")
        print()
        print(f"QC CORPUS: {len(findings)} drift finding(s). The labeled corpus is the ground truth")
        print("  `qc_verdict.py selftest` grades against - a green selftest does NOT prove it is current.")
        print("  If the change was an intentional upstream sync: re-run selftest for EVERY corpus, then")
        print("  `check_qc_corpus.py --update`. If it was not, revert it.")
        return 1

    total = sum(v["_tasks"] for v in current.values())
    print(f"\nQC CORPUS: 0 drift across {len(current)} corpora / {total} labeled tasks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
