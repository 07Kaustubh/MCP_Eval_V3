#!/usr/bin/env python3
"""
Usage:
    python Validators/check_hydration.py [universe]
    python Validators/check_hydration.py --print-manifest <universe>

Verifies that a gitignored, hydrate-on-demand universe payload is actually present and
matches its recorded manifest. Exits 0 when hydrated or not applicable, non-zero otherwise.

Why this exists
---------------
HarmonyGames' universe data is 7.6 GB and is deliberately kept out of git behind a
README with a manifest (the gitignore-plus-manifest pattern, which is the recommended
approach for a read-only, rarely-changing multi-GB reference corpus: git-lfs would exceed
a 1 GB free tier, double local disk, and cannot really be undone; a submodule would turn
the payload's nested git packs into broken gitlinks).

The failure mode that pattern is known for is silent: when hydration has not happened, or
happened against a stale source, downstream tools do not see "missing data" - they see an
empty directory or a pointer and emit cryptic parse errors far from the cause. A README
cannot fail a build. This can.

What the V5 re-hydrate changed
------------------------------
The V4 payload carried a 359 MB `Base_Universe_Complete_Data.json` combined export, and
this gate's version pin was that one file's sha256. The V5 drop does not ship it at all,
and the accessor's export walk never read it anyway (it walks the per-service JSON; an HG
task resolves to the same record count with and without it). That walk was called
`universe_data_source._stream_base_export` when this note was written; it is now
`_iter_base_export`, rewritten to stream rather than accumulate (AGENTS.md HG-U22).

So the pin moved rather than being deleted. It is now a TREE DIGEST: sha256 over the
sorted `relpath\0size` listing of every payload file. That is strictly stronger than the
old blob hash - the blob hash pinned 359 MB of ONE file and said nothing about the other
296,499, while the digest pins the path and size of every one of them, so a rename, a
move, a truncation, a partial rsync or a whole wrong-version drop all move it. It is also
O(files) via os.scandir/stat and reads ZERO payload bytes, which keeps it inside the
constant-memory rule (AGENTS.md rule 33) that forbids materialising this tree.

What each retained check now proves
-----------------------------------
H1 manifest parses        -> the gate cannot silently disable itself by matching nothing.
H2 service dirs exist     -> distinguishes "not hydrated" from "hydrated".
H3 service dir NAME SET   -> catches a wrong-version drop whose dir COUNT coincides.
H4 registry cross-check   -> catches registry/payload divergence (the registry could
                             declare 11 services against a 13-dir tree and nothing noticed).
H5 file count             -> catches a partial rsync that still produced the right dirs.
H6 total payload bytes    -> catches truncated files, which a file COUNT cannot see.
H7 tree digest            -> catches any rename/move/resize anywhere in the tree.
H8 combined blob absent   -> catches re-hydrating the OLD V4 payload over the new one.
"""
import argparse
import hashlib
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from universes import UNIVERSES, get_universe_constants  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# The V4 combined export. It must NOT come back: nothing reads it, it is 359 MB, and its
# presence means someone hydrated the superseded drop on top of this one.
RETIRED_BLOB = "Base_Universe_Complete_Data.json"
POINTER_NAME = "README_HYDRATE.md"


def parse_pointer(readme: Path) -> dict:
    """Pull the recorded counts / sizes / digest out of the hydration pointer.

    The pointer is a MARKDOWN TABLE, not colon-delimited lines. An earlier version of this
    parser looked for `sha256:` / `bytes:` / `service dirs:` and therefore matched NOTHING
    once the table landed, so parse_pointer returned {} and every downstream check was
    guarded out - check_universe reported `[OK] payload hydrated and matches its manifest`
    while verifying nothing at all. That is the exact "matching rule returns the expected
    result while matching the wrong thing" failure Validators/AGENTS.md documents.

    An unparseable pointer is therefore a FINDING, never a silent skip.
    """
    if not readme.is_file():
        return {}
    text = readme.read_text(encoding="utf-8", errors="ignore")
    out = {}

    # payload row: | payload | 316,500 files across 11 service directories |
    m = re.search(r"\|\s*payload\s*\|\s*([0-9,]+)\s*files\s+across\s+([0-9]+)\s+service",
                  text, re.IGNORECASE)
    if m:
        out["files"] = int(m.group(1).replace(",", ""))
        out["service_dirs"] = int(m.group(2))

    # service dirs row: | service dirs | `contacts, gcal, ...` |
    m = re.search(r"\|\s*service dirs\s*\|\s*`([^`]+)`", text, re.IGNORECASE)
    if m:
        out["services"] = sorted({s.strip() for s in m.group(1).split(",") if s.strip()})

    # payload bytes row: | payload bytes | 7,302,587,458 |
    m = re.search(r"\|\s*payload bytes\s*\|\s*([0-9,]+)", text, re.IGNORECASE)
    if m:
        out["bytes"] = int(m.group(1).replace(",", ""))

    # tree digest row: | tree sha256 | `<64 hex>` |
    m = re.search(r"\|\s*tree sha256\s*\|\s*`([0-9a-f]{64})`", text, re.IGNORECASE)
    if m:
        out["tree_sha256"] = m.group(1).lower()

    return out


def walk_payload(data_dir: Path):
    """Yield (relpath, size) for every payload file, streaming.

    Excludes the git-tracked pointer and anything inside a nested `.git` (the archive drops
    git history; nothing reads it - all github_* tools resolve from the service JSONs).
    Uses os.walk with in-place pruning so the ~20k objects under nested `.git` trees are
    never even listed, and stat() only - no file is ever opened or read.
    """
    base = str(data_dir)
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for name in filenames:
            if name == POINTER_NAME:
                continue
            full = os.path.join(dirpath, name)
            try:
                size = os.stat(full).st_size
            except OSError:
                continue          # broken symlink / unreadable: counted by nothing
            yield os.path.relpath(full, base), size


def measure(data_dir: Path) -> dict:
    """Measure the payload on disk. O(files), reads zero payload bytes."""
    h = hashlib.sha256()
    count = 0
    total = 0
    for rel, size in sorted(walk_payload(data_dir)):
        h.update(rel.replace(os.sep, "/").encode("utf-8"))
        h.update(b"\0")
        h.update(str(size).encode("ascii"))
        h.update(b"\n")
        count += 1
        total += size
    dirs = sorted(p.name for p in data_dir.iterdir() if p.is_dir()) if data_dir.is_dir() else []
    return {"files": count, "bytes": total, "services": dirs,
            "service_dirs": len(dirs), "tree_sha256": h.hexdigest()}


def check_universe(name: str) -> list:
    issues = []
    consts = get_universe_constants(name)
    data_dir = ROOT / consts["base_path"] / "Services_Data"
    readme = data_dir / POINTER_NAME
    if not readme.is_file():
        return []                 # universe does not use the hydrate pattern

    pointer = parse_pointer(readme)

    # H1 - the manifest must parse. Every check below is guarded on these values, so an
    # unparsed manifest silently disables the whole gate.
    REQUIRED = ("files", "service_dirs", "services", "bytes", "tree_sha256")
    missing = [k for k in REQUIRED if pointer.get(k) is None]
    if missing:
        issues.append(
            f"FAIL: `{name}` hydration manifest {readme.relative_to(ROOT)} is UNREADABLE - "
            f"could not parse {', '.join(missing)}. Every downstream size/count/digest check "
            f"is guarded on these values, so an unparsed manifest silently disables the gate. "
            f"Fix the manifest format or parse_pointer(); do not ignore this."
        )
        return issues

    # H2 - hydrated at all?
    on_disk_dirs = sorted(p.name for p in data_dir.iterdir() if p.is_dir()) if data_dir.is_dir() else []
    if not on_disk_dirs:
        issues.append(
            f"FAIL: `{name}` payload is NOT HYDRATED. {data_dir} contains no service "
            f"directories. Downstream builders will report success against no data. "
            f"Hydrate per {readme.relative_to(ROOT)} before running the S0 chain."
        )
        return issues

    # H3 - the NAME SET, not just the count. A count check passes a wrong-version drop that
    # happens to carry the same number of directories.
    want_services = pointer["services"]
    if on_disk_dirs != want_services:
        extra = [d for d in on_disk_dirs if d not in want_services]
        absent = [d for d in want_services if d not in on_disk_dirs]
        detail = []
        if extra:
            detail.append(f"unexpected on disk: {', '.join(extra)}")
        if absent:
            detail.append(f"recorded but absent: {', '.join(absent)}")
        issues.append(
            f"FAIL: `{name}` service directories do not match the manifest "
            f"({'; '.join(detail)}). The hydrate is partial or the upstream drop changed shape."
        )

    if len(on_disk_dirs) != pointer["service_dirs"]:
        issues.append(
            f"FAIL: `{name}` has {len(on_disk_dirs)} service dir(s), manifest records "
            f"{pointer['service_dirs']}. The hydrate is partial or the drop changed shape."
        )

    # H4 - registry cross-check. Until this existed the gate compared README to disk and
    # never consulted universes.py, so the registry could declare 11 services against a
    # 13-directory payload and nothing in the repo would notice.
    registry_services = sorted(set(consts.get("services") or []))
    if registry_services:
        reg_extra = [d for d in on_disk_dirs if d not in registry_services]
        reg_absent = [s for s in registry_services if s not in on_disk_dirs]
        if reg_extra or reg_absent:
            detail = []
            if reg_extra:
                detail.append(f"on disk but not in the registry: {', '.join(reg_extra)}")
            if reg_absent:
                detail.append(f"declared by the registry but absent from disk: {', '.join(reg_absent)}")
            issues.append(
                f"FAIL: `{name}` payload disagrees with the universes.py registry "
                f"({'; '.join(detail)}). Registry `services` and the hydrated payload must "
                f"describe the same universe; one of the two is stale."
            )

    # H5..H7 - one walk answers count, bytes and digest.
    got = measure(data_dir)

    if got["files"] != pointer["files"]:
        issues.append(
            f"FAIL: `{name}` payload holds {got['files']} files, manifest records "
            f"{pointer['files']}. A partial hydrate produces the right service dirs and the "
            f"wrong file count."
        )

    if got["bytes"] != pointer["bytes"]:
        issues.append(
            f"FAIL: `{name}` payload is {got['bytes']} bytes, manifest records "
            f"{pointer['bytes']}. A truncated or half-written file keeps the file count "
            f"correct and changes only the size."
        )

    if got["tree_sha256"] != pointer["tree_sha256"]:
        issues.append(
            f"FAIL: `{name}` payload tree digest {got['tree_sha256'][:16]}... does not match "
            f"the manifest {pointer['tree_sha256'][:16]}.... Some file was renamed, moved or "
            f"resized - the upstream payload moved under you. Re-adjudicate rather than "
            f"silently accepting the new bytes."
        )

    # H8 - the retired V4 combined export must stay gone.
    if (data_dir / RETIRED_BLOB).exists():
        issues.append(
            f"FAIL: `{name}` carries {RETIRED_BLOB}, which the V5 drop does not ship. "
            f"The superseded payload has been hydrated over this one. Nothing reads that "
            f"file, and its presence means the tree is a mix of two drops."
        )

    return issues


def main() -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("universe", nargs="?", help="limit to one universe")
    ap.add_argument("--print-manifest", metavar="UNIVERSE",
                    help="measure the payload and print manifest rows to paste into "
                         "README_HYDRATE.md (reads zero payload bytes)")
    args = ap.parse_args()

    if args.print_manifest:
        name = args.print_manifest
        if name not in UNIVERSES:
            print(f"unknown universe: {name}", file=sys.stderr)
            return 2
        data_dir = ROOT / get_universe_constants(name)["base_path"] / "Services_Data"
        got = measure(data_dir)
        print(f"| payload | {got['files']:,} files across {got['service_dirs']} service directories |")
        print(f"| service dirs | `{', '.join(got['services'])}` |")
        print(f"| payload bytes | {got['bytes']:,} |")
        print(f"| tree sha256 | `{got['tree_sha256']}` |")
        return 0

    if args.universe is not None and args.universe not in UNIVERSES:
        print(f"unknown universe: {args.universe}", file=sys.stderr)
        return 2
    targets = [args.universe] if args.universe else sorted(UNIVERSES)

    issues, checked = [], 0
    for name in targets:
        consts = get_universe_constants(name)
        readme = ROOT / consts["base_path"] / "Services_Data" / POINTER_NAME
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
