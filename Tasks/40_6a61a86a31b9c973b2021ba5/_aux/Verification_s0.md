# S0 Cross-Source Verification

## Sources consulted

### Per-task data
- `3_UniverseDataForThisTask.json` :: 3892 rows across 33 service tables (sha256 `49556fce9808d236f04668faeac79ba84d28b67cdc0a89727f866a12d844545d`)
- `2_Persona.txt` :: Carlos Mendez / Onsite Property Manager
- `1_Business_Function.txt` :: Property Operations
- `_aux/Universe_Split/*` :: 33 per-service JSON files (post-split)
- `_aux/Universe_Index/*` :: service_inventory, entities_personas, graph_report, key_facts, today_horizon, accounts_per_entity
- `_aux/Fact_Ledger.json` :: emails=206, amounts=403, dates=192, personas=61, slack_channels=8
- `_aux/Feasible_Surface.json` :: 15 tables / 19 enum columns
- `StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md` :: persona `p_009` at line 38 (matches Carlos Mendez)

### Eval spec
- `Evals_starpm/*` :: S0 is infrastructure-only; no eval sub-dims apply at this phase. Downstream phases (S1/S2/S3/FINAL) will re-consult these evals for scoring.

### QC spec
- `Docs_starpm/*` :: S0 does not produce a scored deliverable; QC dims (Prompt / OE / Rubric / Trajectory) are checked at S1/S2/S3/S4 respectively. Confirmed the StarPM QC spec baseline location so downstream phases can find it.

## QC spec sub-dims relevant to this phase
- N/A — S0 produces infrastructure only (Universe_Split, Universe_Index, Fact_Ledger, Graph_Report, Feasible_Surface). Quality dims are checked at downstream phases.

## Verification statements
- [x] Universe split wrote 33 JSON files to `_aux/Universe_Split/` matching the source row counts (3892 total).
- [x] `Universe_Index` emitted `today_horizon.json` with `universe_today = 2026-07-01`, matching StarPM canonical (per AGENTS.md).
- [x] `Fact_Ledger.json` atom counts non-zero for the surface types that exist in StarPM (emails=206, amounts=403, dates=192, personas=61, slack_channels=8). GL / filesystem surfaces are correctly zero — StarPM has no `oracle_gl` and no filesystem MCP service.
- [x] Persona in `2_Persona.txt` (Carlos Mendez) matches one of the 13 StarPM authoring personas listed in `2_StarPM_PERSONA BRIEFS.md`.
- [x] `Feasible_Surface.json` covers 15 tables / 19 enum columns for S3 rubric cross-reference.
- [x] Universe detection wrote `_aux/Universe.txt = starpm`.

## Discrepancies surfaced
- `today_horizon.json.universe_timezone = "America/New_York"` but StarPM canonical zone per `AGENTS.md` is `America/Chicago` (SW Texas). The `universe_today = 2026-07-01` value is correct; only the tz label differs. Flag for HARDNESS: any lever anchored on a same-day cutoff must be resolved against America/Chicago wall-clock to avoid a 1-hour edge case.
- `records_dated_after_today = 59`. Note in `today_horizon.json` says this is expected for `future` fiscal-period rows / upcoming AP due_dates. HARDNESS should verify no post-today record is a stale scripted artifact before anchoring a lever inside those windows.

## Verdict
PASS — S0 infrastructure ready. Downstream phases (HARDNESS, INJECTION, S1) can proceed. Two flagged discrepancies (timezone label, post-today rows) are informational and do not block HARDNESS.
