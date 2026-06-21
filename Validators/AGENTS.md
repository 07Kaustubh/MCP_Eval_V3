# Validators

Three Python scripts. All take `<path_to_task_dir>` or `--task <path>`. All exit non-zero on FAIL so runbooks can block.

## Scripts

### `split_universe.py`

Patched wrapper around the legacy `data.py`. Writes the per-task universe split into `<TASK_DIR>/_aux/Universe_Split/` instead of the shared `Brookfield_Base_Universe/Data/` directory.

```
python Validators/split_universe.py <TASK_DIR>
```

Reads `<TASK_DIR>/3_UniverseDataForThisTask.json`. Produces per-source `<service>.<table>.json` files + `Universe_complete_data.json` + `_aux/data_hash.txt` (sha256 of the input).

`data.py` at the project root is now a smart forwarder that routes to `Validators/split_universe.py` when given a per-task input file. The original behavior is preserved in `data.legacy.py` — do **not** call `data.legacy.py` directly; it writes to the shared `Brookfield_Base_Universe/Data/` and will overwrite parallel work.

### `build_universe_index.py`

Builds quick lookup summaries from `_aux/Universe_Split/`.

```
python Validators/build_universe_index.py <TASK_DIR>
```

Produces in `_aux/Universe_Index/`:
- `service_inventory.md` — record counts per service file
- `entities_personas.md` — every persona + NPC + contact with email + role
- `key_facts.md` — JE / recon / exception / AP / doc counts + state distributions
- `today_horizon.json` — universe today + last_event_timestamp_seen + records_dated_after_today
- `accounts_per_entity.md` — Oracle GL chart of accounts grouped by entity

### `validate.py`

Phase-aware validator. Block on any FAIL.

```
python Validators/validate.py --phase {prompt|oe|rubrics|all} --task <TASK_DIR>
```

Writes `_aux/Validator_Reports/<phase>.md`. Exits 0 clean, non-zero on any FAIL.

Checks per phase:

| Phase | Checks |
|---|---|
| **prompt** | em-dash / en-dash, 500-word cap, tool-name leakage, MCP-server mention, internal-ID leakage, pre-solving phrases (warn), relative date phrases (note), Prompt_Guidelines.md anti-patterns: QC-sample clichés / over-signaling / generic urgency (warn) |
| **oe** | em-dash / en-dash, numbered-prose format, OE step count >= 8 (warn), opening-verb coverage >= 60% (warn), tool-name existence vs `8_Server_Tools_Details.json`, `body` vs `content` for email tools, `text` vs `payload` for Slack |
| **rubrics** | schema (nested or flat), agent-centric phrasing, no tool names in title, no "at least N" without prompt mandate, category in {outcome, process}, outcome > process count, "approximately" / "(or similar)" usage rules, groundedness sweep against Universe_Split (with float / comma / dollar-sign variants) |

## Adding a check

Edit `validate.py`. Each check appends to a `Report` (`fail` / `warn` / `note`). Keep checks deterministic and dependency-free — no third-party Python packages, stdlib only.

## Adding a per-task summary

Edit `build_universe_index.py`. Use `rows_of(path)` to iterate parsed inner row dicts (the records use `{"row_data": "<JSON-string>", "source": "..."}` shape — `rows_of` handles parsing).
