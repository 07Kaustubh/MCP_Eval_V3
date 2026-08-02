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

It cannot go into git: 5.6 GB, 294,512 files, and three files above GitHub's **100 MB hard
per-file limit** (`Base_Universe_Complete_Data.json` 223 MB, `snowflake/snowflake.tables.json`
125 MB, and a 100 MB packfile). Release assets are not part of a clone, so this costs a
teammate nothing until they actually need HarmonyGames.

## What you are getting

| | |
|---|---|
| release tag | `harmonygames-payload-v1` |
| assets | 3 parts (700 + 700 + 428 MB) + `MANIFEST.txt` |
| archive | `tar --exclude=.git \| zstd -10`, 1,917,167,087 bytes |
| archive sha256 | `8263e0324cc1c56521a52bb660131a23765ce03fc93c314a486406092d401a5a` |
| payload | 294,512 files across 13 service directories |
| `Base_Universe_Complete_Data.json` | 233,946,251 bytes, sha256 `30751b6066af0ae5c84bf782dbceeb53c143902d3cee55542d8c611640858ebf` |

Verified against the upstream drop: path+size identical for **all 294,512 files**, plus a
400-file sha256 sample with zero mismatches.

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
