#!/usr/bin/env python3
"""Compare repo spec surfaces against an extracted upstream source drop.

The eval-hash pins (eval_file_hashes.json) guard REPO-side drift: they fire when
someone edits our copy. They cannot detect UPSTREAM releases - a newer zip with
changed evals matches nothing locally and stays invisible (exactly how the
Brookfield lane went one generation stale before v21.2). This tool closes that
gap: point it at an extracted upstream package and it reports, per spec surface,
whether the repo copy is identical or divergent, so adopt/deviate decisions are
explicit instead of accidental.

Usage:
  python3 Validators/check_source_sync.py --source <extracted_pkg_root> --universe {brookfield|keystone|moveops|starpm}

Exit 0 = fully in sync. Exit 1 = divergences found (listed; adopt upstream
verbatim or record a deviation in AGENTS.md - never leave it silent).
"""
import argparse
import filecmp
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# repo-relative spec surfaces per universe: (source-subdir, repo-dir)
SURFACES = {
    "brookfield": [
        ("Evals", "Evals"), ("Docs", "Docs"), ("Guide", "Guide"),
        ("Brookfield_Base_Universe", "Brookfield_Base_Universe"),
        ("Tasks_Template", "Tasks_Template"),
    ],
    "keystone": [
        ("Evals", "Evals_keystone"), ("Docs", "Docs_keystone"),
        ("Mortgage_Base_Universe", "Mortgage_Base_Universe"),
        ("Tasks_Template", "Tasks_Template_keystone"),
    ],
    "moveops": [
        ("Evals", "Evals_moveops"), ("Docs", "Docs_moveops"),
        ("MoveOps_Base_Universe", "MoveOps_Base_Universe"),
        ("Tasks_Template", "Tasks_Template_moveops"),
    ],
    "starpm": [
        ("Evals", "Evals_starpm"), ("Docs", "Docs_starpm"), ("Guide", "Guide_starpm"),
        ("StarPM_Base_Universe", "StarPM_Base_Universe"),
        ("Tasks_Template", "Tasks_Template_starpm"),
    ],
}
IGNORE = {".DS_Store", "__MACOSX", "_aux", "AGENTS.md"}


def compare(src: Path, dst: Path, rel=""):
    """Yield (kind, path) for files differing or missing from the repo side.
    Files that exist only in the repo are allowed (pipeline additions)."""
    cmp = filecmp.dircmp(str(src), str(dst), ignore=list(IGNORE))
    for f in cmp.diff_files:
        yield ("DIFFERS", f"{rel}{f}")
    for f in cmp.left_only:
        yield ("MISSING_IN_REPO", f"{rel}{f}")
    for sub in cmp.common_dirs:
        yield from compare(src / sub, dst / sub, f"{rel}{sub}/")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, help="extracted upstream package root (the dir holding Evals/, Docs/, ...)")
    ap.add_argument("--universe", required=True, choices=sorted(SURFACES))
    ap.add_argument("--expect-deviations", action="store_true",
                    help="PASS when the only deltas are the documented ones in source_sync_deviations.json")
    args = ap.parse_args()
    import json
    dev_path = Path(__file__).resolve().parent / "source_sync_deviations.json"
    expected = {}
    if args.expect_deviations and dev_path.is_file():
        expected = json.loads(dev_path.read_text()).get(args.universe, {})
    src_root = Path(args.source).resolve()
    if not src_root.is_dir():
        print(f"ERROR: {src_root} is not a directory", file=sys.stderr)
        return 2

    findings = []
    for src_sub, repo_sub in SURFACES[args.universe]:
        s, d = src_root / src_sub, ROOT / repo_sub
        if not s.is_dir():
            print(f"[SKIP] source has no {src_sub}/")
            continue
        if not d.is_dir():
            findings.append(("REPO_DIR_MISSING", repo_sub))
            continue
        deltas = list(compare(s, d))
        status = "IN SYNC" if not deltas else f"{len(deltas)} delta(s)"
        print(f"[{args.universe}] {src_sub} -> {repo_sub}: {status}")
        for kind, path in deltas:
            print(f"    {kind}: {repo_sub}/{path}")
            findings.append((kind, f"{repo_sub}/{path}"))

    if findings:
        unexpected = [(k, f) for k, f in findings if f not in expected]
        if args.expect_deviations and not unexpected:
            print(f"\nSOURCE SYNC: PASS with {len(findings)} documented deviation(s) (source_sync_deviations.json)")
            return 0
        print(f"\nSOURCE SYNC: {len(unexpected) if args.expect_deviations else len(findings)} undocumented divergence(s)."
              f" Adopt upstream verbatim or record a deviation in AGENTS.md + Validators/source_sync_deviations.json."
              f" Silent divergence is forbidden.")
        return 1
    print("\nSOURCE SYNC: PASS - repo spec surfaces identical to upstream drop")
    return 0


if __name__ == "__main__":
    sys.exit(main())
