# Validators

39 Python scripts (see the ground-truth list below). Most take `<path_to_task_dir>` or `--task <path>` (compare_rubrics takes two file paths). All exit non-zero on FAIL so runbooks can block. All per-universe behavior routes through the `universes.py` registry keyed by `_aux/Universe.txt` - never hardcode Brookfield constants in a new check.

## Registry + framework core (read first)

- **`universes.py`** - the multi-universe registry (`UNIVERSES`: brookfield, keystone, moveops, starpm, harmonygames), `detect_universe()` (signal-scored, ties default brookfield, cached to `_aux/Universe.txt`; HarmonyGames resolves via an exclusive-marker short-circuit that runs BEFORE scoring, because its per-task universe file is a pointer and would otherwise be signal-starved into the brookfield tie-break), `get_universe_constants()`, and the `FRAMEWORKS` table (`v3`/`v3.1`/`v2.1`/`v4`/`hg`) with `get_framework_profile()`. Every other validator imports its constants from here.
- **`v4_gates.py`** - V4 deterministic phases `injection` (Evals_starpm/0) + `submission_gate` (Evals_starpm/5). Injection is presence-gated for ALL universes (runs whenever `9_Universe_inject.sql` carries executable statements; v3-family date ceiling = registry `today`).
- **`qc_verdict.py`** - deterministic QC verdict engine (`parse`/`classify`/`selftest`/`audit`/`feedback`); `selftest` is bucket-correct 138/138 across `QC_Tasks/{V3_Buckets,V3.1_Buckets,V2.1_Buckets,V4_Tasks,V5_HG_Buckets}` (16+16+80+16+10). Corpus size is NOT fixed at 16: HarmonyGames ships 10 in a 4/4/2/0 split with one legitimately empty bucket.
- **`check_regression.py`** + **`test_regression_anchors.py`** - the zero-regression gate (frozen report hashes for 7 snapshot tasks) and 78 behavior anchors, plus a `--dead-gate` self-check that neuters the validator's ability to emit any finding and asserts every non-allowlisted anchor then FAILS (anchor count is not anchor quality; two KeyStone anchors asserted nothing for several versions). `check_regression.py` runs it automatically. Run `check_regression.py` after ANY validator edit; PASS = anchors 78/78, reports 21/21 identical, verdicts 7/7 unchanged. The anchor total is NOT hardcoded in `check_regression.py`: it scrapes the suite's own summary and gates on `failed == 0 and passed == total`, so adding anchors needs no constant update here.
- **`check_source_sync.py`** + `source_sync_deviations.json` - diffs repo spec surfaces against an extracted upstream drop (hash pins only catch repo-side edits, never a new upstream release).
- **`check_eval_hashes.py`** / **`check_tool_catalog.py`** - repo-side drift pins for eval MDs and tool catalogs.
- **`new_task.py`** / **`close_task.py`** - scaffolder (per-universe templates, V4 dual-model shape) and CLOSE audit (V4-aware artifact sets).
- **`build_feasible_surface.py`** / **`verify_universe_atoms.py`** / **`calc_similarity.py`** / **`aggregate_verdicts.py`** / **`check_justification.py`** / **`check_verification.py`** - grounding surface, per-universe atom verification, similarity gate, verdict rollup, justification hygiene, per-phase verification gate.

## Scripts

### `split_universe.py`

Patched wrapper around the legacy `data.py`. Writes the per-task universe split into `Tasks/<TASK_DIR>/_aux/Universe_Split/` instead of the shared `Brookfield_Base_Universe/Data/` directory.

```
python Validators/split_universe.py Tasks/<TASK_DIR>
```

Reads `Tasks/<TASK_DIR>/3_UniverseDataForThisTask.json`. Produces per-source `<service>.<table>.json` files + `Universe_complete_data.json` + `_aux/data_hash.txt` (sha256 of the input).

`data.py` at the project root is now a smart forwarder that routes to `Validators/split_universe.py` when given a per-task input file. The legacy script that wrote to the shared `Brookfield_Base_Universe/Data/` directory has been archived to `_archive/data.legacy.py` (v21) — never call it directly; it overwrites parallel work.

### `build_universe_index.py`

Builds quick lookup summaries from `_aux/Universe_Split/`.

```
python Validators/build_universe_index.py Tasks/<TASK_DIR>
```

Produces in `_aux/Universe_Index/`:
- `service_inventory.md` — record counts per service file
- `entities_personas.md` — every persona + NPC + contact with email + role
- `key_facts.md` — JE / recon / exception / AP / doc counts + state distributions
- `today_horizon.json` — universe today + last_event_timestamp_seen + records_dated_after_today
- `accounts_per_entity.md` — Oracle GL chart of accounts grouped by entity

### `build_fact_ledger.py`

Emits the per-task atom surface that Council A and `validate.py --phase rubrics` use for groundedness.

```
python Validators/build_fact_ledger.py Tasks/<TASK_DIR>
```

Produces `Tasks/<TASK_DIR>/_aux/Fact_Ledger.json`:
- `emails` — every email address present anywhere (lowercased, deduped)
- `amounts` — canonical 2dp strings (Decimal-rounded)
- `dates` — every ISO date with day-of-week
- `ids` — typed buckets: je, exception, recon, doc, vendor, apinv, linear_issue, reminder, conversation, airtable_record, calendar_event, slack_channel, contact, persona
- `accounts_by_entity` — every Oracle GL account number → name, grouped per entity (captures the `105000` Brookfield/Northstar/Acme trap directly)
- `fiscal_periods` — status / locked_at / locked_by / bd3_lock_at / bd5_close_at / period_label / entity_id per period
- `personas` — email → name / title / contact_id / is_user
- `aliases` — first_name / last_name / full_name → emails (for fuzzy person lookups)
- `meta.source_hash` — sha256 of `3_UniverseDataForThisTask.json` (regenerate when this changes)

The ledger is the authoritative source for "does this email / amount / ID exist in this task?" — never re-grep the raw split.

### `build_graph_report.py`

Compact discovery map for HARDNESS lever selection.

```
python Validators/build_graph_report.py Tasks/<TASK_DIR>
```

Produces `Tasks/<TASK_DIR>/_aux/Universe_Index/graph_report.md` with: people-by-artifact-density (top 30), periods-by-JE-density (top 20), exceptions-by-entity-state, recons-by-entity-state, pending-AP-by-vendor (top 20), documents-by-kind / by-classification, densest (person, period) pairs (top 15).

HARDNESS reads this to pick the persona × period × system intersection with the most stump-able artifact density. No 30MB edge JSON — summary tables only.

### `compare_rubrics.py`

Per-index diff between local rubrics and platform paste-back.

```
python Validators/compare_rubrics.py Tasks/<TASK_DIR>/7_Rubrics.json Tasks/<TASK_DIR>/10_Rubrics_Platform.json
```

Catches silent platform-side mutations (reformatting, field stripping, reordering). Triggered by `PIPELINE COMPARE — Tasks/<TASK_DIR>`. Exits 0 on match, non-zero on any count mismatch or per-field diff.

### `parse_trajectories.py`

Parses real Claude Code SDK trajectories + verifier-fails text. Computes empirical hardness metrics — no manual JSON parsing.

```
python Validators/parse_trajectories.py Tasks/<TASK_DIR>
```

Reads `trajectory-runs/trajectory-run-*.json` (platform export) or falls back to `Agent_Responses/Run*.json` (template path). Counts `tool_use` blocks in assistant `message.content[]`, separates MCP (`mcp__*`) from internal scaffolding (Task, TaskCreate, TaskUpdate, etc.).

Parses `8_Verifier_Fails.txt` block headers (`Run #N` + `X/Y criteria passed`) to compute pass@1. A run passes iff X == Y.

Writes `_aux/Trajectory_Stats.json` with per-run table + verdict (`OK` / `REBUILD_CANDIDATE_DENSITY` / `REBUILD_CANDIDATE_DIFFICULTY`). Exits 0 on OK, non-zero otherwise.

Used by `PIPELINE REVIEW` step 3 (hardness pre-assessment) and `PIPELINE S4` phase-readiness gate.

### `phase_ready.py`

Refuses to start a phase if upstream artifacts are missing. Architectural enforcement layer on top of the STOP-gate convention — catches the case where an agent silently skipped a previous phase.

```
python Validators/phase_ready.py --phase {hardness|s1|s1.5|s2|s3|final|s4|review|materialize|redo|compare} --task Tasks/<TASK_DIR>
```

Every runbook except S0 invokes this as step 1. If it STOPs with a missing-artifact list, the agent must run the named upstream phase before continuing. Exits 0 when all required artifacts exist + are non-empty, non-zero otherwise.

### `validate.py`

Phase-aware validator. Block on any FAIL.

```
python Validators/validate.py --phase {prompt|oe|rubrics|all|injection|submission_gate} --task Tasks/<TASK_DIR>
```

Writes `_aux/Validator_Reports/<phase>.md`. Exits 0 clean, non-zero on any FAIL. `injection` + `submission_gate` are V4 gates handled in `v4_gates.py` (SKIP cleanly when not applicable). All checks read constants from the `universes.py` registry, so the tables below describe behavior for every universe - the Brookfield-flavored examples (Oracle GL / `105000` trap) apply only when `_aux/Universe.txt` == brookfield.

Checks per phase:

| Phase | Checks |
|---|---|
| **prompt** | em-dash / en-dash, 500-word cap, tool-name leakage, MCP-server mention, internal-ID leakage, pre-solving phrases (warn), relative date phrases (note), Prompt_Guidelines.md anti-patterns: QC-sample clichés / over-signaling / generic urgency (warn) |
| **oe** | em-dash / en-dash, numbered-prose format, OE step count >= 8 (warn), opening-verb coverage >= 60% (warn), tool-name existence vs `8_Server_Tools_Details.json`, `body` vs `content` for email tools, `text` vs `payload` for Slack |
| **rubrics** | schema (nested or flat), agent-centric phrasing, no tool names in title, no "at least N" without prompt mandate, category in {outcome, process}, outcome > process count, "approximately" / "(or similar)" usage rules, naturalness heuristics (subjective terms FAIL, non-agent voice WARN, awkward negation WARN), groundedness sweep against `_aux/Fact_Ledger.json` when present (falls back to raw blob substring match) |

## Adding a check

Edit `validate.py`. Each check appends to a `Report` (`fail` / `warn` / `note`). Keep checks deterministic and dependency-free — no third-party Python packages, stdlib only.

## Adding a per-task summary

Edit `build_universe_index.py`. Use `rows_of(path)` to iterate parsed inner row dicts (the records use `{"row_data": "<JSON-string>", "source": "..."}` shape — `rows_of` handles parsing).

## Matching rules that return the expected number

Three separate defects in this repo shared one shape: a matching rule that produced the
number someone expected, while matching the wrong thing.

1. Parity was measured with `grep 'universe == "hg"'`. `hg` is the FRAMEWORK key; the
   universe key is `harmonygames`, so the probe could not match anything and reported clean.
2. The replacement grep matched only `==`, so `if universe != "starpm"` in `v4_gates.py` was
   invisible. The inventory said ten branches; there were eleven, and the eleventh is why F9
   is unavailable for HarmonyGames.
3. The dead-gate allowlist matched with bare `startswith`, so the entry `"v22 HG-1"` absorbed
   `HG-10`, `HG-11`, `HG-12` and `HG-13`. A real leak was printed as "allowlisted" and the
   gate returned 0.

Each looked right because the count looked right. When a check reports clean, confirm it can
report dirty: feed it a case that MUST fail. `--dead-gate` and the `[STALE]` allowlist check
exist for exactly this, and both were themselves verified by injecting a failure.

