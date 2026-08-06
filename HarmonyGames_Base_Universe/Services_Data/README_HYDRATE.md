# Services_Data — hydration pointer (payload NOT in git)

## Hydrate

```sh
bash Validators/hydrate_harmonygames.sh
```

That is the whole procedure. It downloads the payload from the repo's own GitHub Release,
verifies every checksum, extracts, and runs `check_hydration.py`. Requires `gh` (authenticated)
and `zstd`. Re-running is safe: it verifies and exits if already hydrated.

## Why the payload is not in git

HarmonyGames inverts the usual boundary. For the other four universes the per-task
`3_UniverseDataForThisTask.json` carries the data. Here that file is a ~721-byte **pointer**
and this directory IS the source of truth — so it must stay *hydratable*, never deleted.

It cannot go into git: 8.1 GB, 316,543 files, and three files above GitHub's **100 MB hard
per-file limit** (`Base_Universe_Complete_Data.json` 359 MB, `snowflake/snowflake.tables.json`
125 MB, and a 100 MB packfile). Release assets are not part of a clone, so this costs a
teammate nothing until they actually need HarmonyGames.

## What you are getting

| | |
|---|---|
| release tag | `harmonygames-payload-v2` |
| assets | 7 parts (6 x 700 MB + 876 KB) + `MANIFEST.txt` |
| archive | `tar --exclude=.git --exclude=README_HYDRATE.md \| zstd -10`, 4,404,895,494 bytes | zstd -10`, 1,917,167,087 bytes |
| archive sha256 | `53be756d294362816acee99ca7a5ed2b4057a436e6f4308163cb185a7ac9e183` |
| payload | 296,543 files across 13 service directories (post-extract; the upstream tree also carries 20,000 files in 18 nested `.git` dirs, excluded from the archive) |
| `Base_Universe_Complete_Data.json` | 359,094,851 bytes, sha256 `31cb9ee54367c5b11c9896409ef3b8c021884710858636db28d4ba7fd1fc146b` |

Round-trip verified 2026-08-06: downloaded from the published release, reassembled to the
archive sha above, extracted, and the blob sha + 296,543 file count + 13 service dirs all
matched. Verified against the upstream drop: path+size identical for **all 316,543 upstream files** (296,543 after the `--exclude=.git` the archive applies), plus a
400-file sha256 sample with zero mismatches.

## Searching this payload — read this before you grep

Two traps here have already produced confident, wrong conclusions.

**1. `git grep`, `rg` and every ripgrep-backed search return ZERO matches by design.**
`.gitignore` carries `**/Services_Data/*`, and those tools honour it, so a search over this
directory silently reports "no matches" whether or not the string is there. Absence of
matches is NOT evidence of absence. Force it explicitly:

```sh
rg --no-ignore --hidden 'oliver@harmonygames.co' HarmonyGames_Base_Universe/Services_Data
```

**2. The service-level tables are not the whole universe.** The 118 files sitting directly
under each service directory hold only 234 MB. The records live deeper — `slack/messages/`
(901 MB), `gmail/threads/` (338 MB), `github/root/` (166 MB), `gdrive/root/` (54 MB) — 1.9 GB
of JSON across 71,021 files in all. A scan scoped to the top level misses most of the data
and will report real values as missing. This exact mistake made 11 of the 17 roster emails
look absent when every one of them is present.

**3. Two Windows-specific hazards.** Paths inside the Unity `PackageCache` trees exceed the
260-char `MAX_PATH` limit, so `open()` and `os.path.getsize()` raise on files `os.walk` just
listed — retry through the `\\?\` prefix. And the tarball carries macOS AppleDouble `._*.json`
siblings that are not valid UTF-8; skip any name starting with `._`.

The reference implementation of a correct scan is `Presence` in
`Validators/verify_universe_atoms.py`: one streaming pass, chunked with an overlap, constant
memory. Do not load this payload into memory — earlier attempts were OOM-killed.

## The one deliberate omission

The 17 nested git repositories (548 MB) are excluded. Their **working trees are fully
included** — 57,126 files in `rpg-prototype`, 49,586 in `GameOfDominoes`, and so on. Only
`.git` history is dropped, and nothing reads it: all 56 `github_*` tools resolve from the
service JSONs (`github.commits.json`, `github.commit_map.json`, `github.branches.json`, …),
never from `.git`. Copying them in would also create broken gitlinks inside this repo.

## If the upstream payload is ever re-issued

Bump the release tag **and** the two checksums in `Validators/hydrate_harmonygames.sh`
(`ARCHIVE_SHA256`, `BLOB_SHA256`) together with the manifest values above. Changing the tag
alone would silently hydrate a stale payload that still passes its own checksum.

## Until you hydrate

`check_hydration.py` exits 1 and **all six S0 builders refuse to run** —
`universe_data_source`, `split_universe`, `build_universe_index`, `build_fact_ledger`,
`build_graph_report`, `build_feasible_surface`. That is deliberate: four of them previously
exited 0 against no data and wrote artifacts whose every atom count was zero.

Only HarmonyGames needs this. The other four universes use the `per_task_json` contract and
carry their data with the task.
