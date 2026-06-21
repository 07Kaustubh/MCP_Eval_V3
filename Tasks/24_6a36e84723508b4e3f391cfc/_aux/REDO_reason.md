# REDO reason — Tasks/24_6a36e84723508b4e3f391cfc

Decision: REBUILD as fresh CB. Failure dimension: DENSITY.

## Source of truth

- Trajectory stats: `_aux/Trajectory_Stats.json` (verdict: `REBUILD_CANDIDATE_DENSITY`)
- 6 trajectory files under `trajectory-runs/`:
  - `trajectory-run-1 (11).json` — 35 total tool calls (29 MCP), 6/10 rubrics passed
  - `trajectory-run-2 (11).json` — 23 total tool calls (18 MCP), 10/10 rubrics passed
  - `trajectory-run-3 (13).json` — 27 total tool calls (20 MCP), 8/10 rubrics passed
  - `trajectory-run-4 (11).json` — 42 total tool calls (24 MCP), 7/10 rubrics passed
  - `trajectory-run-5 (11).json` — 38 total tool calls (21 MCP), 7/10 rubrics passed
  - `trajectory-run-6 (11).json` — 30 total tool calls (14 MCP), 5/10 rubrics passed

## Computed numbers

- `avg_tool_calls_total = 32.5` (min 23, max 42)
- `avg_tool_calls_mcp_only = 21.0`
- `density_ok_at_40 = false` — fails the 40+ floor by 7.5 calls on the total metric
- `pass_at_1 = 0.167` (1 of 6 runs passed all rubrics)
- `difficulty_ok_at_40pct = true` — difficulty is acceptable

## What this means

The scenario is hard enough for Opus 4.8 (pass@1 well below the 40% ceiling), but it does
not force the agent through enough tool surface. Average 32.5 calls puts it 7.5 short of
the 40-call density floor, and only one of six runs even reached 40 (run 4 at 42). Runs
that cleared more rubrics still hit ceilings around 35–38 calls, so the gap is structural,
not a single-run anomaly. The candidate's design lets the agent satisfy the prompt with a
narrow query path (Slack history, one SAP pull, one Records Vault sweep, one email check)
and stop. The rebuild has to introduce levers that pull the agent through more services
or more verification loops without weakening the difficulty.

## Density gaps observed in trajectories (signal for HARDNESS to use)

- Records Vault checks resolve in 2–4 calls per run because the agent settles for one
  entity scope (acme_cloud) and a single document-kind list.
- Slack history searches almost always come up empty and the agent does not pivot to
  email or Linear to cross-confirm.
- Vendor-master / SAP queries collapse into one big batch instead of per-vendor
  drill-downs followed by SOW / PO / W-9 cross-checks.
- No prompt pressure to read individual document contents, traverse approver chains, or
  verify exception ticketing in Linear, so the agent skips entire MCP surfaces.

## Retained vs rebuilt

- Retained: per-task universe (`3_UniverseDataForThisTask.json`), persona
  (`2_Persona.txt`), business function (`1_Business_Function.txt`), all
  `_aux/Universe_Split/`, `_aux/Universe_Index/`, `_aux/Fact_Ledger.json` outputs.
- Archived as rating evidence: `_aux/Candidate_Originals/5_Prompt.txt`,
  `6_Oracle_Events.txt`, `7_Rubrics.json`, `13_Feedback.txt`, `changes.md`.
- Rebuilt from scratch: `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json` via
  the CB sequence HARDNESS -> S1 -> S2 -> S3 -> FINAL.
