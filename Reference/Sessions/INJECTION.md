# PIPELINE INJECTION — Session Runbook

**Trigger:** `PIPELINE INJECTION — Tasks/<TASK_DIR>`

**Universe:** StarPM (V4) only. This phase does not apply to Brookfield, Keystone, or MoveOps tasks.

**Position in pipeline:** Runs AFTER universe injection (`9_Universe_inject.sql` populated, `4_Changelog.json` populated) and AFTER S0 completes, but BEFORE S1 (prompt authoring). It is a hard gate — no prompt work begins until INJECTION returns PASS.

---

## Purpose

Verify that the CB's universe edits are structurally sound, temporally consistent, cross-service coherent, naturalistic, reachable by MCP tools, appropriately obscured, and genuinely difficult. A broken injection poisons everything downstream — rubrics will reference phantom data, agents will hit dead ends, and QC will fail the task.

The eval produces a binary PASS/FAIL verdict (all 7 structural gates must pass) PLUS a composite difficulty score (minimum 3.5 required). One structural defect or difficulty score < 3.5 = BLOCKER.

---

## Prerequisites

Before invoking, verify ALL of these are true:

- [ ] `_aux/Universe.txt` contains `starpm`
- [ ] `9_Universe_inject.sql` is populated (non-empty)
- [ ] `4_Changelog.json` is populated with the CB's change manifest
- [ ] `S0_Setup_Report.md` exists in `_aux/` (S0 has completed)
- [ ] `_aux/Universe_Split/` is populated
- [ ] `_aux/Universe_Index/` is populated

If any prerequisite is missing, STOP and print: `INJECTION BLOCKED: <missing item> not yet available. Complete S0 and paste universe injection files before invoking INJECTION.`

---

## Required Inputs

| File | Role |
|---|---|
| `9_Universe_inject.sql` | PRIMARY — SQL INSERT/UPDATE/DELETE statements injecting scenario data |
| `4_Changelog.json` | CB's structured change manifest (added/modified/deleted records) |
| `3_UniverseDataForThisTask.json` | Task-specific snapshot (may be empty; use base + changelog as fallback) |
| `StarPM_Base_Universe/Data/` | Base universe for BEFORE-state comparison (all 9 service folders) |
| `StarPM_Base_Universe/8_Universe_Schema.json` | Schema — column names, types, constraints, foreign keys |
| `StarPM_Base_Universe/7_Server_Tools_Details.json` | MCP tool inventory for reachability checks |
| `5_Prompt.txt` | If already drafted — used for reachability chain tracing (optional at this stage) |

---

## Execution

Invoke as a single `oracle` sub-agent with the full eval from `Evals_starpm/0_Injection_Quality_Eval.md`. The sub-agent must execute ALL phases of the eval in order.

**Sub-agent prompt template:**

```
You are the INJECTION QUALITY EVALUATOR for a StarPM (V4) task.

TASK DIR: Tasks/<TASK_DIR>
EVAL SPEC: Evals_starpm/0_Injection_Quality_Eval.md
PRIMARY INPUT: Tasks/<TASK_DIR>/9_Universe_inject.sql
CHANGELOG: Tasks/<TASK_DIR>/4_Changelog.json
UNIVERSE SNAPSHOT: Tasks/<TASK_DIR>/3_UniverseDataForThisTask.json
BASE UNIVERSE: StarPM_Base_Universe/Data/
SCHEMA: StarPM_Base_Universe/8_Universe_Schema.json
TOOL CATALOG: StarPM_Base_Universe/7_Server_Tools_Details.json

TASK:
Execute every phase of the Injection Quality Eval in order (Phase 0 through Phase 9).
The mandatory TODO list in Phase 0 is a hard gate — create and track it before proceeding.
Produce a verdict for each of the 7 structural gates (Phase 1-7) plus the difficulty score
(Phase 8). Save the full report to:
  Tasks/<TASK_DIR>/_aux/Council_Reports/INJECTION_report.md

Final verdict format (at end of report):
  GATE 1 Schema & Structure: PASS / FAIL
  GATE 2 ID Format: PASS / FAIL
  GATE 3 Date & Time: PASS / FAIL
  GATE 4 Cross-Service Consistency: PASS / FAIL
  GATE 5 Naturalness: PASS / FAIL
  GATE 6 Reachability: PASS / FAIL
  GATE 7 Pre-Solve Check: PASS / FAIL
  DIFFICULTY SCORE: <composite 1.0-5.0> / RATING: <Too Easy|Medium|Hard|Very Hard>
  OVERALL VERDICT: PASS / FAIL
  BLOCKER ISSUES: <list, or "none">
```

---

## Exit Criteria

| Condition | Next step |
|---|---|
| All 7 gates PASS AND difficulty score >= 3.5 | `INJECTION PASS. Proceed to: PIPELINE S1 — Tasks/<TASK_DIR>` |
| Any gate FAILS OR difficulty < 3.5 | `INJECTION FAIL. Fix the listed blocker(s), re-inject, and re-run PIPELINE INJECTION.` |

**INJECTION FAIL is not a soft stop.** The CB must fix the injection and re-run this phase. Proceeding to S1 with a failed INJECTION is a pipeline policy violation.

---

## Output

`Tasks/<TASK_DIR>/_aux/Council_Reports/INJECTION_report.md`

Contains:
- Phase-by-phase findings for all 8 evaluation phases
- Per-record verdict table (schema / ID / temporal / cross-service / naturalness / reachability / pre-solve)
- Difficulty scoring breakdown (7 dimensions, composite score, rating band)
- Final gate summary + overall PASS/FAIL

---

## How INJECTION fits in the full StarPM pipeline

```
PIPELINE NEW       — scaffold task folder
PIPELINE S0        — split universe, build index + fact ledger
                   ← paste 9_Universe_inject.sql + 4_Changelog.json
PIPELINE INJECTION — this phase (hard gate)
PIPELINE HARDNESS  — lever identification
PIPELINE S1        — prompt authoring (BLOCKED until INJECTION PASS)
PIPELINE S1.5      — linter blocker handling (if needed)
PIPELINE S2        — oracle events
PIPELINE S3        — rubrics
PIPELINE FINAL     — cross-artifact holistic review
PIPELINE SUBMISSION_GATE — zero-tolerance final check
PIPELINE S4        — verifier fails (after platform runs, dual-model)
PIPELINE CLOSE     — final sanity check
```
