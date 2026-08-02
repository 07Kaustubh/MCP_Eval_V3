# Services_Data — hydration pointer (payload NOT in git)

HarmonyGames inverts the usual payload boundary. For the other four universes the per-task
`3_UniverseDataForThisTask.json` carries the data. Here that file is a ~721-byte **pointer**
and this directory IS the source of truth — so it must stay *hydratable*, never deleted.

It is gitignored because it cannot go into git: 5.6 GB, ~314k files, and **three files above
GitHub's 100 MB hard limit** (`Base_Universe_Complete_Data.json` 223 MB,
`snowflake/snowflake.tables.json` 125 MB, and a 100 MB packfile). Only this README is tracked.

## Identity of the payload you need

| | |
|---|---|
| upstream drop | `MCP_Eval_V3_HarmonyGames` → `HarmonyGames_Base_Universe/Services_Data/` |
| total size | 5.6 GB |
| service directories | 13 (confluence, contacts, gcal, gdocs, gdrive, github, gmail, gsheets, gslides, linear, slack, snowflake, trello) |
| `Base_Universe_Complete_Data.json` | 233,946,251 bytes |
| sha256 of that file | `30751b6066af0ae5c84bf782dbceeb53c143902d3cee55542d8c611640858ebf` |

`Validators/check_hydration.py` verifies all four of those properties. It FAILs when the
payload is absent, when the blob is missing while the manifest records a hash, when the byte
count differs, and when the sha256 differs.

## Where to get it

**This is site-specific and is not recorded here on purpose** — an absolute path from one
machine is useless to everyone else, which is exactly the bug this rewrite fixes. Obtain the
upstream `MCP_Eval_V3_HarmonyGames` drop from wherever your team stores it (shared bucket,
internal mirror, or the original delivery), then point `SOURCE` at its `Services_Data`.

## Hydrate

```sh
SOURCE=/path/to/MCP_Eval_V3_HarmonyGames/HarmonyGames_Base_Universe/Services_Data
rsync -a --exclude=.git "$SOURCE"/ HarmonyGames_Base_Universe/Services_Data/
python3 Validators/check_hydration.py     # must print OK
```

`--exclude=.git` is required, not cosmetic: the payload contains **17 nested git
repositories** (under `github/root/harmonygames-Games/` and one under
`gdrive/root/marcus.bennett@harmonygames.co/`). Copying them in makes them broken gitlinks
rather than content, and one of their packfiles alone exceeds GitHub's file limit.

## Until you hydrate

`check_hydration.py` exits 1, and **all six S0 builders refuse to run** — `universe_data_source`,
`split_universe`, `build_universe_index`, `build_fact_ledger`, `build_graph_report` and
`build_feasible_surface`. That is deliberate: four of them previously exited 0 against no data
and wrote artifacts whose every atom count was zero, which downstream phases then trusted.

Only HarmonyGames needs this. The other four universes use the `per_task_json` contract and
carry their data with the task.
