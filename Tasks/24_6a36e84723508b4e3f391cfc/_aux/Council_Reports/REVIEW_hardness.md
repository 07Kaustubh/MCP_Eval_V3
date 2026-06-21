# REVIEW Hardness Report

Task: `24_6a36e84723508b4e3f391cfc`
Source: **measured** (6 trajectories present in `trajectory-runs/`).

## Measured numbers (from `_aux/Trajectory_Stats.json`)

| Metric | Value | Threshold | Verdict |
|---|---:|---|---|
| Avg total tool calls | **32.5** | >= 40 (hard rule #11) | **FAIL** |
| Avg MCP tool calls | 21 | n/a | n/a |
| Min / Max total | 23 / 42 | n/a | only 1/6 runs cleared 40 |
| pass@1 | **0.167** (1 of 6 all-rubrics-pass) | <= 0.40 | OK (difficulty is fine) |

## Per-run

| Run | Total | MCP | Rubric pass | All-pass |
|---:|---:|---:|---:|---|
| 1 | 35 | 29 | 6/10 | FAIL |
| 2 | 23 | 18 | 10/10 | PASS |
| 3 | 27 | 20 | 8/10 | FAIL |
| 4 | 42 | 24 | 7/10 | FAIL |
| 5 | 38 | 21 | 7/10 | FAIL |
| 6 | 30 | 14 | 5/10 | FAIL |

## Diagnosis

**Density is the dominant failure mode.** Difficulty is fine (only 1/6 perfect-pass = 16.7%, well below the 40% pass@1 ceiling). The task IS hard for Opus 4.8 - agents miss BeaconPay enumeration, the specific invoice IDs, and the prior-conversation finding - but they get to that failure in too few tool calls.

Root causes of low density (visible in the candidate artifacts):

1. **OE step count is 7**, vs the V3 reference range of 11-28. Sparse OEs cap the expected discovery surface.
2. **OE lines lack action-verb openings** (0/7 begin with Search/Send/Call/Post). V3 references use action-first openings to telegraph multi-step decomposition.
3. **Prompt under-decomposes the investigation**. "Pull the pending-approval queue... figure out which... check if there's any earlier conversation in email or Slack" reads as a single ask, not as a multi-stage triage. Agents collapse it.
4. **No mandated write actions beyond one Slack post.** No Linear ticket, no reminder, no calendar event, no draft email, no Records Vault filing. Single-write tasks consistently project low density.

Verdict: density cannot be patched by OE / rubric edits alone - needs new lever combination + scenario restructure. Triggers REBUILD per the REVIEW decision table.
