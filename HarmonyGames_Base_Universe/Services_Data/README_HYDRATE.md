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
`3_UniverseDataForThisTask.json` carries the data. Here that file is a ~940-byte **pointer**
and this directory IS the source of truth — so it must stay *hydratable*, never deleted.

It cannot go into git: 6.80 GiB across 316,500 files, including one file above GitHub's
**100 MB hard per-file limit** — a 105,206,509-byte packfile at
`github/root/harmonygames-Games/liveops/.git/objects/pack/`. Release assets are not part of a
clone, so this costs a teammate nothing until they actually need HarmonyGames.

## What you are getting

| | |
|---|---|
| release tag | `harmonygames-payload-v3` |
| archive | `tar --exclude=.git --exclude=README_HYDRATE.md \| zstd -10` |
| archive sha256 | `60c797474999771f70a96430ef1b043125fa16e628d796b2a58106e0f47bfe2c` |
| payload | 296,500 files across 11 service directories |
| service dirs | `contacts, gcal, gdocs, gdrive, github, gmail, gsheets, gslides, linear, slack, trello` |
| payload bytes | 6,734,069,813 |
| tree sha256 | `40d7873a596d9433cd4f03fc2995f95ab2a02bc194ee6f5fe12a98b54b446c62` |

`archive sha256` is the sha256 of the reassembled archive published under release tag
`harmonygames-payload-v3`. `hydrate_harmonygames.sh` refuses to extract anything whose
checksum does not match it, and still refuses outright if a future drop resets it to the
`TODO-UNPUBLISHED-FILL-AT-PUBLISH-TIME` placeholder.

The four manifest rows below `archive sha256` are what `check_hydration.py` enforces. All
four were measured from disk with `check_hydration.py --print-manifest harmonygames` and
cross-checked independently with `find | wc -l` and `stat -f%z`. Counts EXCLUDE the 20,000
files inside 19 nested `.git` directories (dropped by the archive's `--exclude=.git`) and
this pointer file. The full tree as rsync'd from the drop is 316,500 files / 7,302,587,458
bytes; 296,500 files / 6,734,069,813 bytes remain after that exclusion.

`tree sha256` is a digest over the sorted `relpath\0size` listing of every payload file, not
over their contents. It pins the shape of all 296,500 files for the cost of a stat() each and
reads zero payload bytes, so it stays inside the constant-memory rule. It replaced a sha256 of
the old combined export, which pinned one 359 MB file and said nothing about the rest.

### V5 re-hydrate: what changed from `harmonygames-payload-v2`

| | v2 (V4 drop) | v3 (V5 drop) |
|---|---|---|
| service dirs | 13 | **11** — `snowflake/` and `confluence/` are gone |
| `Base_Universe_Complete_Data.json` | 359,094,851 bytes | **not shipped** |
| files >100 MB | 3 | **1** (the packfile above) |
| per-service filenames | doubled (`slack/slack.files.json`) | flat (`slack/files.json`) |
| version pin | blob sha256 | tree digest over all 296,500 files |

Removing the combined export changes nothing downstream:
`universe_data_source._stream_base_export` walks the per-service JSON and never read it. An
HG task resolves to the same record count with and without it.

## Searching this payload — read this before you grep

Two traps here have already produced confident, wrong conclusions.

**1. `git grep`, `rg` and every ripgrep-backed search return ZERO matches by design.**
`.gitignore` carries `**/Services_Data/*`, and those tools honour it, so a search over this
directory silently reports "no matches" whether or not the string is there. Absence of
matches is NOT evidence of absence. Force it explicitly:

```sh
rg --no-ignore --hidden 'oliver@harmonygames.co' HarmonyGames_Base_Universe/Services_Data
```

**2. The service-level tables are not the whole universe.** Only 16 files sit directly under
the service directories, holding 126.3 MB. The records live deeper — `linear/root` (2.3G,
2,027 files), `gdrive/root` (2.1G, 30,436), `github/root` (1.8G, 257,399), `slack/messages`
(871M, 5,371), `gmail/threads` (374M, 21,209), `trello/root` (49M, 42). The scan streams
70,979 JSON files totalling 1.48 GiB. A scan scoped to the top level misses most of the data
and will report real values as missing. This exact mistake made 11 of the 17 roster emails
look absent when every one of them is present.

**3. Two Windows-specific hazards.** Paths inside the Unity `PackageCache` trees exceed the
260-char `MAX_PATH` limit, so `open()` and `os.path.getsize()` raise on files `os.walk` just
listed — retry through the `\\?\` prefix. On AppleDouble `._*.json` siblings: this drop
carries **zero** of them (`find -name '._*'` returns 0), unlike v2. The `name.startswith("._")`
skip in `Presence._scan_roots` stays as defense, because a macOS tar round-trip can
reintroduce them and they are not valid UTF-8.

The reference implementation of a correct scan is `Presence` in
`Validators/verify_universe_atoms.py`: one streaming pass, chunked with an overlap, constant
memory. Do not load this payload into memory — earlier attempts were OOM-killed. The `.json`
extension filter in `_scan_roots` is load-bearing, not cosmetic: it is the only thing keeping
the 105 MB packfile and the other ~225,500 non-JSON files out of the byte stream.
`test_memory_bounds.py` G1(c) guards it, and `--self-check` mutates it to prove that guard
can fail.

## The one deliberate omission

The 19 nested git repositories are excluded — 20,000 files, 568,517,645 bytes of `.git`
history. Their **working trees are fully included**. Only `.git` history is dropped, and
nothing reads it: all 56 `github_*` tools resolve from the service JSONs, never from `.git`.
Copying them in would also create broken gitlinks inside this repo.

## If the upstream payload is ever re-issued

Bump the release tag **and** `ARCHIVE_SHA256` in `Validators/hydrate_harmonygames.sh`,
together with the four manifest rows above. Changing the tag alone would silently hydrate a
stale payload that still passes its own checksum. Regenerate the manifest rows with:

```sh
python3 Validators/check_hydration.py --print-manifest harmonygames
```

There is no longer a `BLOB_SHA256` to bump: the combined export is not part of this payload.

## Until you hydrate

`check_hydration.py` exits 1 and **all six S0 builders refuse to run** —
`universe_data_source`, `split_universe`, `build_universe_index`, `build_fact_ledger`,
`build_graph_report`, `build_feasible_surface`. That is deliberate: four of them previously
exited 0 against no data and wrote artifacts whose every atom count was zero.

Only HarmonyGames needs this. The other four universes use the `per_task_json` contract and
carry their data with the task.
