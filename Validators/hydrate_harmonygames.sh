#!/usr/bin/env bash
# Hydrate HarmonyGames Services_Data from the GitHub Release assets.
#
# HarmonyGames inverts the payload boundary: its per-task 3_UniverseDataForThisTask.json is
# a ~721-byte pointer and Services_Data/ IS the source of truth. It cannot live in git -
# 5.6 GB, ~294k files, and three files above GitHub's 100 MB per-file limit. So it ships as
# a compressed, split Release asset instead, which is not part of a clone.
#
# Usage:  bash Validators/hydrate_harmonygames.sh [--tag <release-tag>]
set -euo pipefail

TAG="harmonygames-payload-v1"
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
ARCHIVE_SHA256="8263e0324cc1c56521a52bb660131a23765ce03fc93c314a486406092d401a5a"
BLOB_SHA256="30751b6066af0ae5c84bf782dbceeb53c143902d3cee55542d8c611640858ebf"

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

if [ -f "$DEST/Base_Universe_Complete_Data.json" ]; then
  echo "Already hydrated. Verifying..."
  python3 "$ROOT/Validators/check_hydration.py" && exit 0
  echo "Existing payload failed verification; remove it and re-run." >&2; exit 1
fi

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
zstd -dc "$WORK/archive.tar.zst" | tar -xf - -C "$ROOT/HarmonyGames_Base_Universe"

echo "==> verifying payload"
got="$(shasum -a 256 "$DEST/Base_Universe_Complete_Data.json" | cut -d' ' -f1)"
[ "$got" = "$BLOB_SHA256" ] || { echo "FAIL: payload blob sha256 mismatch" >&2; exit 1; }

python3 "$ROOT/Validators/check_hydration.py"
echo "==> done. Removing the ~1.8 GB download cache; delete $ROOT/_dist yourself if you want it kept."
rm -rf "$WORK"
