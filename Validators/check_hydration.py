#!/usr/bin/env python3
"""
Usage:
    python Validators/check_hydration.py [universe]

Verifies that a gitignored, hydrate-on-demand universe payload is actually present and
matches its recorded manifest. Exits 0 when hydrated or not applicable, non-zero otherwise.

Why this exists
---------------
HarmonyGames' universe data is 5.6 GB and is deliberately kept out of git behind a
README with a sha256 (the gitignore-plus-manifest pattern, which is the recommended
approach for a read-only, rarely-changing multi-GB reference corpus: git-lfs would exceed
a 1 GB free tier, double local disk, and cannot really be undone; a submodule would turn
the payload's four nested git packs into broken gitlinks).

The failure mode that pattern is known for is silent: when hydration has not happened, or
happened against a stale source, downstream tools do not see "missing data" - they see an
empty directory or a pointer and emit cryptic parse errors far from the cause. A README
cannot fail a build. This can.

Checked: the directory exists, carries the expected service subdirectories, and the
recorded sha256 of the combined export still matches. A hash mismatch means the upstream
drop moved under you, which is a re-adjudication event, not a warning.
"""
import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from universes import UNIVERSES, get_framework_profile, get_universe_constants  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def parse_pointer(readme: Path) -> dict:
    """Pull the recorded size / count / sha256 out of the hydration pointer."""
    if not readme.is_file():
        return {}
    text = readme.read_text(encoding="utf-8", errors="ignore")
    out = {}
    m = re.search(r"sha256:\s*([0-9a-f]{64})", text, re.IGNORECASE)
    if m:
        out["sha256"] = m.group(1).lower()
    m = re.search(r"bytes:\s*([0-9]+)", text, re.IGNORECASE)
    if m:
        out["bytes"] = int(m.group(1))
    m = re.search(r"service dirs:\s*([0-9]+)", text, re.IGNORECASE)
    if m:
        out["service_dirs"] = int(m.group(1))
    return out


def check_universe(name: str) -> list:
    consts = get_universe_constants(name)
    data_dir = ROOT / consts["base_path"] / "Services_Data"
    readme = data_dir / "README_HYDRATE.md"
    if not readme.is_file():
        return []          # universe does not use the hydrate pattern

    issues = []
    pointer = parse_pointer(readme)
    subdirs = [p for p in data_dir.iterdir() if p.is_dir()] if data_dir.is_dir() else []
    if not subdirs:
        issues.append(
            f"FAIL: `{name}` payload is NOT HYDRATED. {data_dir} contains no service "
            f"directories. Downstream builders will report success against no data. "
            f"Hydrate per {readme.relative_to(ROOT)} before running the S0 chain."
        )
        return issues

    expected = pointer.get("service_dirs")
    if expected is not None and len(subdirs) != expected:
        issues.append(
            f"FAIL: `{name}` has {len(subdirs)} service dir(s), manifest records {expected}. "
            f"The hydrate is partial or the upstream drop changed shape."
        )

    blob = data_dir / "Base_Universe_Complete_Data.json"
    want = pointer.get("sha256")
    want_bytes = pointer.get("bytes")

    # An ABSENT blob previously skipped the hash entirely, so 13 empty directories
    # created by a `mkdir` loop reported "payload hydrated and matches its manifest".
    # A partial rsync is the single most likely real failure on a 5.6 GB out-of-band
    # payload, and it passed.
    if want and not blob.is_file():
        issues.append(
            f"FAIL: `{name}` Base_Universe_Complete_Data.json is MISSING while the manifest "
            f"records a sha256 for it. The service directories exist but the payload does "
            f"not - this is the partial-hydrate case, not a completed one."
        )
        return issues

    if want_bytes is not None and blob.is_file():
        got_bytes = blob.stat().st_size
        if got_bytes != want_bytes:
            issues.append(
                f"FAIL: `{name}` Base_Universe_Complete_Data.json is {got_bytes} bytes, "
                f"manifest records {want_bytes}. Recorded size was parsed and never compared."
            )
            return issues

    if want and blob.is_file():
        h = hashlib.sha256()
        with open(blob, "rb") as fh:
            for chunk in iter(lambda: fh.read(1 << 22), b""):
                h.update(chunk)
        got = h.hexdigest()
        if got != want:
            issues.append(
                f"FAIL: `{name}` Base_Universe_Complete_Data.json sha256 {got[:16]}... does "
                f"not match the manifest {want[:16]}.... The upstream payload moved; "
                f"re-adjudicate rather than silently accepting the new bytes."
            )
    return issues


def main() -> int:
    targets = [sys.argv[1]] if len(sys.argv) > 1 else sorted(UNIVERSES)
    issues, checked = [], 0
    for name in targets:
        consts = get_universe_constants(name)
        readme = ROOT / consts["base_path"] / "Services_Data" / "README_HYDRATE.md"
        if not readme.is_file():
            continue
        checked += 1
        found = check_universe(name)
        if not found:
            print(f"[OK] {name}: payload hydrated and matches its manifest")
        issues += found
    if checked == 0:
        print("[SKIP] no universe uses the hydrate-on-demand pattern")
        return 0
    for i in issues:
        print(i)
    print()
    print(f"HYDRATION: {len(issues)} issue(s) across {checked} universe(s)")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
