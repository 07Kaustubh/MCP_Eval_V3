#!/usr/bin/env bash
# Hydrate HarmonyGames Services_Data from the GitHub Release assets.
#
# HarmonyGames inverts the payload boundary: its per-task 3_UniverseDataForThisTask.json is
# a ~940-byte contract descriptor and Services_Data/ IS the source of truth. It cannot live
# in git - 6.8 GiB and one file above GitHub's 100 MB per-file limit. So it ships as a
# compressed, split Release asset instead, which is not part of a clone.
#
# v3 (2026-08 MCP_Eval_V5_HarmonyGames drop): 11 service dirs, 296,500 files /
# 6,734,069,813 bytes post-extract. No combined export: the V4 payload's 359 MB
# Base_Universe_Complete_Data.json is not shipped, and nothing read it.
#
# The archive is built from INSIDE Services_Data, so its entries are `./<service>` with no
# Services_Data/ prefix - it must be extracted with -C "$DEST", not into the parent.
#
# Usage:  bash Validators/hydrate_harmonygames.sh [--tag <release-tag>]
set -euo pipefail

TAG="harmonygames-payload-v3"
REPO="07Kaustubh/MCP_Eval_V3"
while [ $# -gt 0 ]; do
  case "$1" in
    --tag) TAG="$2"; shift 2 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="$ROOT/HarmonyGames_Base_Universe/Services_Data"
WORK="$ROOT/_dist/download"

# Filled at publish time by whoever builds and uploads the v3 archive. Until then the
# download path below cannot verify what it fetched, so it must refuse to run rather than
# extract 6.8 GiB of unverified bytes over the payload. See the guard further down.
ARCHIVE_SHA256="60c797474999771f70a96430ef1b043125fa16e628d796b2a58106e0f47bfe2c"

# There is deliberately no BLOB_SHA256 any more. The v2 script pinned the payload on the
# sha256 of one 359 MB combined export; v3 does not ship that file. check_hydration.py now
# pins the whole tree (file count, total bytes, and a digest over every path+size), which is
# strictly more than the blob hash ever covered.

# Verify-if-present comes FIRST, before the gh/zstd probes: a hydrated checkout must be
# verifiable with no network, no GitHub auth, and no release published at all. That is the
# state the repo is in between an upstream drop landing and the archive being uploaded.
if [ -d "$DEST/slack" ] && [ -d "$DEST/github" ]; then
  echo "Already hydrated. Verifying..."
  python3 "$ROOT/Validators/check_hydration.py" && exit 0
  echo "Existing payload failed verification; remove it and re-run." >&2; exit 1
fi

if [ "$ARCHIVE_SHA256" = "TODO-UNPUBLISHED-FILL-AT-PUBLISH-TIME" ]; then
  echo "FAIL: this script cannot hydrate yet - ARCHIVE_SHA256 is still the placeholder." >&2
  echo "      The v3 payload ($TAG) has not been built or published, so a download could" >&2
  echo "      not be verified and would extract unchecked bytes over Services_Data/." >&2
  echo "" >&2
  echo "      To publish: build the archive from inside Services_Data, upload it under the" >&2
  echo "      tag above, put its sha256 in ARCHIVE_SHA256 here, and mirror it into the" >&2
  echo "      'archive sha256' row of Services_Data/README_HYDRATE.md." >&2
  echo "      To hydrate now without a release: rsync the drop's" >&2
  echo "      HarmonyGames_Base_Universe/Data/ into Services_Data/ and run check_hydration.py." >&2
  exit 1
fi

command -v gh >/dev/null 2>&1 || { echo "FAIL: gh CLI not found. brew install gh && gh auth login" >&2; exit 1; }

# A GITHUB_TOKEN/GH_TOKEN in the environment OVERRIDES the gh keyring. If it belongs to an
# account without access to this private repo, gh reports a bare "release not found", which
# reads like the asset is missing rather than an auth problem. Detect it and say so.
if ! gh repo view "$REPO" --json name >/dev/null 2>&1; then
  if [ -n "${GITHUB_TOKEN:-}${GH_TOKEN:-}" ]; then
    echo "FAIL: cannot see $REPO as the token in GITHUB_TOKEN/GH_TOKEN." >&2
    echo "      That env var overrides your gh login. Retry with:" >&2
    echo "        env -u GITHUB_TOKEN -u GH_TOKEN bash Validators/hydrate_harmonygames.sh" >&2
    echo "      or unset it in your shell profile." >&2
  else
    echo "FAIL: cannot see $REPO. Run: gh auth login  (and ensure the account has access)" >&2
  fi
  exit 1
fi
command -v zstd >/dev/null 2>&1 || { echo "FAIL: zstd not found. brew install zstd" >&2; exit 1; }

mkdir -p "$WORK"
echo "==> downloading release assets (tag: $TAG)"
gh release download "$TAG" --repo "$REPO" \
   --pattern 'harmonygames-services-data.tar.zst.part-*' --dir "$WORK" --clobber

echo "==> reassembling"
cat "$WORK"/harmonygames-services-data.tar.zst.part-* > "$WORK/archive.tar.zst"

echo "==> verifying archive checksum"
got="$(shasum -a 256 "$WORK/archive.tar.zst" | cut -d' ' -f1)"
if [ "$got" != "$ARCHIVE_SHA256" ]; then
  echo "FAIL: archive sha256 $got != expected $ARCHIVE_SHA256 (truncated or corrupt download)" >&2
  exit 1
fi

echo "==> extracting into $DEST"
mkdir -p "$DEST"
# Entries are `./<service>/...` relative to Services_Data (built with `tar -cf - .` from
# inside it), so extract INTO $DEST. Extracting into the parent would scatter 11 service
# directories alongside Services_Data/ instead of inside it.
zstd -dc "$WORK/archive.tar.zst" | tar -xf - -C "$DEST"

echo "==> verifying payload"
# check_hydration.py is the whole verification now: it checks the service-dir name set, the
# registry cross-check, the file count, the total bytes, the tree digest, and that the
# retired combined export has not come back.
python3 "$ROOT/Validators/check_hydration.py"
echo "==> done. Removing the download cache; delete $ROOT/_dist yourself if you want it kept."
rm -rf "$WORK"
