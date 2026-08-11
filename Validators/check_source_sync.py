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
  python3 Validators/check_source_sync.py --source <extracted_pkg_root> --universe {brookfield|keystone|moveops|starpm|harmonygames}

Exit 0 = fully in sync. Exit 1 = BLOCKING divergences found (listed; adopt upstream
verbatim or record a deviation in AGENTS.md - never leave it silent).

EXTRA_IN_REPO (a path present only on the repo side) is REPORTED but never blocking: a
repo-only path is usually legitimate. It is surfaced because the alternative is the blind
spot that let HarmonyGames_Base_Universe/Tool_Access/ carry catalogs for two banned servers
with no gate able to observe them either way (AGENTS.md HG-U20).
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
    "harmonygames": [
        ("Evals", "Evals_harmonygames"), ("Docs", "Docs_harmonygames"),
        ("Guide", "Guide_harmonygames"),
        ("HarmonyGames_Base_Universe", "HarmonyGames_Base_Universe"),
        ("Tasks_Template", "Tasks_Template_harmonygames"),
        # The labeled QC corpus is SSOT for qc_verdict.py selftest. It was absent from this
        # table until 2026-08-06, so a drop that changed 35 of 112 corpus files - including
        # 7_Rubrics, 8_Verifier_Fails, 6_Oracle_Events and 12 trajectories - passed sync
        # while selftest reported 10/10 against stale ground truth. Only the other universes'
        # corpora stay unmapped, because their upstream drops are not on hand to verify the
        # source-side directory name.
        ("QC_Tasks", "QC_Tasks/V5_HG_Buckets"),
    ],
    "starpm": [
        ("Evals", "Evals_starpm"), ("Docs", "Docs_starpm"), ("Guide", "Guide_starpm"),
        ("StarPM_Base_Universe", "StarPM_Base_Universe"),
        ("Tasks_Template", "Tasks_Template_starpm"),
    ],
}
IGNORE = {".DS_Store", "__MACOSX", "_aux", "AGENTS.md"}

# Kinds that make this gate exit 1. EXTRA_IN_REPO is deliberately absent - see the module
# docstring. Keep this as the single source of truth for "does this kind block?"; a second
# hardcoded list in main() is how a reporting-only kind silently becomes blocking.
BLOCKING_KINDS = frozenset({"DIFFERS", "MISSING_IN_REPO", "REPO_DIR_MISSING"})


def compare(src: Path, dst: Path, rel=""):
    """Yield (kind, path) for every divergence between the upstream drop and the repo.

    DIFFERS / MISSING_IN_REPO are blocking. EXTRA_IN_REPO (repo-only) is reporting-only:
    the previous contract was that repo-only files "are allowed", which was implemented as
    not looking at them at all - so a repo-extra path was invisible rather than accepted.
    """
    cmp = filecmp.dircmp(str(src), str(dst), ignore=list(IGNORE))
    for f in cmp.diff_files:
        yield ("DIFFERS", f"{rel}{f}")
    for f in cmp.left_only:
        yield ("MISSING_IN_REPO", f"{rel}{f}")
    for f in cmp.right_only:
        yield ("EXTRA_IN_REPO", f"{rel}{f}")
    for sub in cmp.common_dirs:
        yield from compare(src / sub, dst / sub, f"{rel}{sub}/")


def _documented_by(path: str, expected: dict):
    """Return the manifest key documenting `path`, or None.

    source_sync_deviations.json carries two entry shapes and this function used to read only
    one. A path-KEYED entry (`"HarmonyGames_Base_Universe/Data": "..."`) matched; an ID-keyed
    entry (`"HG-U18": {"path": "..."}`) did not, so every HG-U* row suppressed nothing and the
    file's own note conceded they were "documentation only". Two deviations were suppressed
    only because somebody hand-wrote a path-keyed twin beside the ID-keyed row.

    Matching stays deliberately narrow - exact match, or a `dir/**` prefix. A trailing bare
    `/` is NOT treated as a wildcard even though several entries carry one: `QC_Tasks/
    V5_HG_Buckets/` as a prefix would suppress drift across the entire labeled corpus, which
    is the opposite of what a pin is for. `*` inside a path (HG-U3) is likewise not expanded.
    An entry that needs directory scope must say so with `/**`.

    Returns the key rather than a bool so callers can print WHY a finding was suppressed;
    a suppression nobody can attribute is indistinguishable from an accident.
    """
    for key, entry in expected.items():
        if key.startswith("_"):
            continue  # metadata (_comment, _state_field, _last_update, ...), never a path
        candidates = [key]
        if isinstance(entry, dict) and isinstance(entry.get("path"), str):
            candidates.append(entry["path"])
        for cand in candidates:
            if cand == path:
                return key
            if cand.endswith("/**") and path.startswith(cand[:-2]):
                return key
    return None


def _documented(path: str, expected: dict) -> bool:
    """Boolean face of _documented_by. Lifted out of main() so it is testable at all."""
    return _documented_by(path, expected) is not None


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
    # Loaded unconditionally so repo-only paths and suppressed findings can be ATTRIBUTED to
    # the entry that documents them, even on a plain run. Pass/fail still consults it only
    # under --expect-deviations, so this does not change any exit code.
    if dev_path.is_file():
        expected = json.loads(dev_path.read_text()).get(args.universe, {})
    src_root = Path(args.source).resolve()
    if not src_root.is_dir():
        print(f"ERROR: {src_root} is not a directory", file=sys.stderr)
        return 2

    findings = []   # blocking
    extras = []     # reporting-only (EXTRA_IN_REPO)
    for src_sub, repo_sub in SURFACES[args.universe]:
        s, d = src_root / src_sub, ROOT / repo_sub
        if not s.is_dir():
            print(f"[SKIP] source has no {src_sub}/")
            continue
        if not d.is_dir():
            findings.append(("REPO_DIR_MISSING", repo_sub))
            continue
        deltas = list(compare(s, d))
        blocking = [(k, p) for k, p in deltas if k in BLOCKING_KINDS]
        extra = [(k, p) for k, p in deltas if k not in BLOCKING_KINDS]
        if not deltas:
            status = "IN SYNC"
        elif not blocking:
            status = f"IN SYNC ({len(extra)} repo-only)"
        else:
            status = f"{len(blocking)} delta(s)" + (f" + {len(extra)} repo-only" if extra else "")
        print(f"[{args.universe}] {src_sub} -> {repo_sub}: {status}")
        for kind, path in blocking:
            print(f"    {kind}: {repo_sub}/{path}")
            findings.append((kind, f"{repo_sub}/{path}"))
        for kind, path in extra:
            extras.append((kind, f"{repo_sub}/{path}"))

    if extras:
        undoc = [f for _, f in extras if not _documented(f, expected)]
        print(f"\n--- repo-only paths ({len(extras)}; REPORTING ONLY, never blocking) ---")
        for kind, f in extras:
            key = _documented_by(f, expected)
            print(f"    {kind}: {f}" + (f"   [documented: {key}]" if key else ""))
        print(f"    {len(extras) - len(undoc)} documented, {len(undoc)} undeclared."
              f" Undeclared is not a failure; it is a prompt to decide whether the path is a"
              f" deliberate pipeline addition or something upstream deleted underneath us.")

    if findings:
        unexpected = [(k, f) for k, f in findings if not _documented(f, expected)]
        if args.expect_deviations and not unexpected:
            print(f"\nSOURCE SYNC: PASS with {len(findings)} documented deviation(s) (source_sync_deviations.json)")
            # Print the attribution. A count of suppressed findings cannot distinguish
            # "every one matched the entry written for it" from "one entry happens to absorb
            # them all", and that difference is the whole value of the manifest.
            for k, f in findings:
                print(f"    suppressed {k}: {f}   <- {_documented_by(f, expected)}")
            return 0
        print(f"\nSOURCE SYNC: {len(unexpected) if args.expect_deviations else len(findings)} undocumented divergence(s)."
              f" Adopt upstream verbatim or record a deviation in AGENTS.md + Validators/source_sync_deviations.json."
              f" Silent divergence is forbidden.")
        return 1
    print("\nSOURCE SYNC: PASS - repo spec surfaces identical to upstream drop")
    return 0


if __name__ == "__main__":
    sys.exit(main())
