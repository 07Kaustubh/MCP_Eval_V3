# PIPELINE INJECT-CHECKER — Session Runbook

**Trigger:** `PIPELINE INJECT-CHECKER — Tasks/<TASK_DIR>`

**Universe:** StarPM (V4) only. Does not apply to Brookfield, Keystone, or MoveOps tasks.

**Position in pipeline:** Runs AFTER the CB executes `9_Universe_inject.sql` on the platform and pastes the exported universe data back into the task folder. BEFORE `PIPELINE S1`. On PASS, this phase also rebuilds `_aux/Universe_Split/` automatically so the CB does not have to.

---

## Purpose

Verify that every record in `9_Universe_inject.sql` landed correctly in the platform's universe. The CB can make copy-paste errors, the platform can silently drop records, or the exported snapshot can be partial. INJECT-CHECKER catches all of these before S1 grounding begins — a prompt grounded against an incomplete injection produces unverifiable rubrics.

On PASS, rebuilds `_aux/Universe_Split/`, `_aux/Universe_Index/`, and `_aux/Fact_Ledger.json` from the post-injection snapshot. On FAIL, reports exactly which records are missing or wrong so the CB can re-inject only the failed records.

---

## Prerequisites

Before invoking, verify ALL of these are true:

- [ ] `_aux/Universe.txt` contains `starpm`
- [ ] `Tasks/<TASK_DIR>/9_Universe_inject.sql` exists (the SQL the pipeline authored)
- [ ] `_aux/Council_Reports/INJECTION_report.md` shows `OVERALL VERDICT: PASS`
- [ ] At least one of these post-injection universe files is present and non-empty:
  - `Tasks/<TASK_DIR>/3_UniverseDataForThisTask.json` (full post-injection snapshot — preferred)
  - `Tasks/<TASK_DIR>/4_Changelog.json` (structured change manifest from the platform)

If any prerequisite is missing, STOP and print:
`INJECT-CHECKER BLOCKED: <missing item>. Paste the platform-exported universe data into Tasks/<TASK_DIR>/ before invoking INJECT-CHECKER.`

---

## Execution

### Step 1: Parse the SQL — build the expected record set

Read `Tasks/<TASK_DIR>/9_Universe_inject.sql`. For every SQL statement:

- **INSERT INTO `<table>`**: extract the table name, the primary key value, and every field-value pair.
- **UPDATE `<table>` SET ... WHERE id = `<id>`**: extract the table name, the record ID, and the fields being updated.
- **DELETE FROM `<table>` WHERE id = `<id>`**: note the table and ID (verify the record is absent from the post-injection data).

Build an **Expected Record Set**: a list of `{ table, id, operation, fields: { field: expected_value } }` objects. One entry per SQL statement.

### Step 2: Load the post-injection universe

Prefer `3_UniverseDataForThisTask.json` (full snapshot) over `4_Changelog.json` (change manifest). If only `4_Changelog.json` is present, use it to reconstruct which records were supposed to land and cross-reference against `StarPM_Base_Universe/Data/` for the base state.

Build a **Actual Record Map**: for each table, a map of `id → { field: actual_value }` from the post-injection data.

### Step 3: Compare expected vs actual — per-record verdict

For each entry in the Expected Record Set:

| Check | Verdict |
|---|---|
| Record ID is present in the Actual Record Map for that table | LANDED |
| Record ID is absent from the Actual Record Map | MISSING |
| Record ID is present but one or more field values differ from expected | WRONG_VALUE |
| DELETE: record ID is absent (expected) | LANDED |
| DELETE: record ID is still present | DELETION_FAILED |

For WRONG_VALUE records, report the specific field, the expected value, and the actual value.

### Step 4: Produce the INJECT-CHECKER report

Save to `Tasks/<TASK_DIR>/_aux/Council_Reports/INJECT_CHECKER_report.md`.

```markdown
# INJECT-CHECKER Report

## Per-Record Results

| Table | ID | Operation | Verdict | Notes |
|---|---|---|---|---|
| <table> | <id> | INSERT | LANDED / MISSING / WRONG_VALUE | <field: expected vs actual> |
| <table> | <id> | UPDATE | LANDED / WRONG_VALUE | <field: expected vs actual> |
| <table> | <id> | DELETE | LANDED / DELETION_FAILED | — |

## Summary
- Total records checked: <n>
- LANDED: <n>
- MISSING: <n>
- WRONG_VALUE: <n>
- DELETION_FAILED: <n>

## OVERALL VERDICT: PASS / FAIL
PASS = all records LANDED with correct values.
FAIL = one or more records MISSING, WRONG_VALUE, or DELETION_FAILED.

## Blocker details (FAIL only)
<per-record fix instructions, or "none">
```

---

## Exit Criteria

### PASS — all records LANDED

1. Print the per-record table from the report.
2. Rebuild the universe split from the post-injection snapshot:
   ```
   python data.py Tasks/<TASK_DIR>
   ```
   This rebuilds `_aux/Universe_Split/`, `_aux/Universe_Index/`, and `_aux/Fact_Ledger.json`. Confirm the command exits 0. If it errors, report the error and STOP.
3. Print:
   ```
   INJECT-CHECKER PASS — all <n> injected records verified. Universe split rebuilt.

   Proceed to:
     PIPELINE S1 — Tasks/<TASK_DIR>
   ```

### FAIL — one or more records missing or wrong

Print the blocker details from the report. Tell the CB:

```
INJECT-CHECKER FAIL — <n> record(s) did not land correctly.

Fix options:
  (a) Re-run only the failed INSERT/UPDATE/DELETE statements on the platform,
      re-export the updated universe, paste the new 3_UniverseDataForThisTask.json
      into Tasks/<TASK_DIR>/, then re-invoke:
        PIPELINE INJECT-CHECKER — Tasks/<TASK_DIR>
  (b) If the platform silently rejected the SQL (e.g., schema mismatch), re-run
      PIPELINE INJECTION in a fresh chat to revise 9_Universe_inject.sql, then
      re-inject on the platform and re-run INJECT-CHECKER.
```

Do NOT proceed to S1 until INJECT-CHECKER returns PASS.

---

## Output Files

| File | Written by | When |
|---|---|---|
| `Tasks/<TASK_DIR>/_aux/Council_Reports/INJECT_CHECKER_report.md` | This session | Step 4 |
| `Tasks/<TASK_DIR>/_aux/Universe_Split/*` | `python data.py` (PASS only) | After verification |
| `Tasks/<TASK_DIR>/_aux/Universe_Index/*` | `python data.py` (PASS only) | After verification |
| `Tasks/<TASK_DIR>/_aux/Fact_Ledger.json` | `python data.py` (PASS only) | After verification |

---

## How INJECT-CHECKER fits in the full StarPM pipeline

```
PIPELINE NEW           — scaffold task folder
PIPELINE S0            — split base universe, build index + fact ledger
PIPELINE HARDNESS      — lever identification + injection planning → _aux/Hardness_Plan.md
PIPELINE INJECTION     — author 9_Universe_inject.sql, oracle audit (7 gates + difficulty ≥ 3.5)
                       ← CB takes 9_Universe_inject.sql to platform, executes it
                       ← CB pastes back 3_UniverseDataForThisTask.json and/or 4_Changelog.json
PIPELINE INJECT-CHECKER — THIS PHASE: verify all records landed → rebuild Universe_Split
PIPELINE S1            — prompt authoring (grounded on verified post-injection universe)
PIPELINE S1.5          — linter blocker handling (if needed)
PIPELINE S2            — oracle events
PIPELINE S3            — rubrics
PIPELINE FINAL         — cross-artifact holistic review
PIPELINE SUBMISSION_GATE — zero-tolerance final check
PIPELINE S4            — verifier fails (after platform runs, dual-model)
PIPELINE CLOSE         — final sanity check
```

## Bootstrap

Read root `AGENTS.md` first. `9_Universe_inject.sql` is the ground truth for what should have been injected. `3_UniverseDataForThisTask.json` is the ground truth for what actually landed. Discrepancies between the two are the only thing this phase cares about.
