# PIPELINE MATERIALIZE — Apply Review Fixes + Re-Verify

**Trigger:** `PIPELINE MATERIALIZE — Tasks/<TASK_DIR>`

**When to run:** AFTER `PIPELINE REVIEW` produces a `changes.md` with auto-marked Applied rows. BEFORE `PIPELINE FEEDBACK`. Runs in a fresh chat with zero prior context — bootstraps from the REVIEW output on disk.

## What this phase does

Applies the Applied rows from `changes.md` to produce corrected `14_Updated_Oracle_Events.txt`, `15_Updated_Rubrics.json`, and (if applicable) `_aux/REVIEW_prompt_draft.txt`. Then re-runs the full gate set (validator + Council A + Council B + AUDIT + FINAL) on the corrected set to verify the fixes didn't introduce regressions. Originals 5/6/7 stay untouched throughout — they remain the rated artifact for FEEDBACK.

## Required inputs

| File | Source |
|---|---|
| `Tasks/<TASK_DIR>/changes.md` | produced by PIPELINE REVIEW with Applied rows |
| `Tasks/<TASK_DIR>/5_Prompt.txt` | candidate original |
| `Tasks/<TASK_DIR>/6_Oracle_Events.txt` | candidate original |
| `Tasks/<TASK_DIR>/7_Rubrics.json` | candidate original |
| `Tasks/<TASK_DIR>/_aux/Universe_Split/` | per-task universe from REVIEW Step 1 (S0 setup) |
| `Tasks/<TASK_DIR>/_aux/Fact_Ledger.json` | from REVIEW Step 1 |
| `Tasks/<TASK_DIR>/_aux/Council_Reports/REVIEW_triage.md` | triage verdict (SALVAGEABLE vs REBUILD) |

## Forbidden inputs

| File | Reason |
|---|---|
| `Tasks/<TASK_DIR>/14_Updated_Oracle_Events.txt` | This phase WRITES this; cannot read its own output as input |
| `Tasks/<TASK_DIR>/15_Updated_Rubrics.json` | Same |
| `Tasks/<TASK_DIR>/_aux/REVIEW_prompt_draft.txt` | This phase WRITES this if prompt rows are Applied |
| `Tasks/<TASK_DIR>/13_Feedback.txt` | Written by FEEDBACK phase, not this one |

## Phase-readiness gate (run FIRST)

```
python Validators/phase_ready.py --phase materialize --task Tasks/<TASK_DIR>
```

Refuses if `changes.md` doesn't exist OR has no Applied rows OR REVIEW triage was REBUILD (in which case materialization is skipped — go straight to REBUILD via `PIPELINE REDO`).

## Step 0: Create your TODO list (MANDATORY)

Before any other action, create `Tasks/<TASK_DIR>/_aux/Todos_materialize.md` listing every step in the Procedure below as a discrete atomic todo. Mark `in_progress` / `completed` as you progress. v11 E1 operator-discipline gate.

## Procedure

1. **Read the triage verdict from `_aux/Council_Reports/REVIEW_triage.md`.**
   - If verdict = REBUILD: STOP. Do NOT materialize 14/15. The scenario itself is the problem — patching OE / rubric on top would ship a half-fixed task. Print the REBUILD reason + recommend `PIPELINE REDO — Tasks/<TASK_DIR>` to the operator and exit.
   - If verdict = SALVAGEABLE: proceed.

2. **Read `changes.md` and partition the rows by phase and status.** Build three change-sets:
   - Prompt rows where Status = Applied
   - OE rows where Status = Applied
   - Rubric rows where Status = Applied

   Skip any row marked Dismissed or Pending. (Operators flip Applied → Dismissed manually between REVIEW and MATERIALIZE to reject specific fixes; default is Applied per v17 auto-apply.)

3. **Materialize the corrected deliverables (triage-aware)**:
   - **`Tasks/<TASK_DIR>/14_Updated_Oracle_Events.txt`** — written ONLY if any OE-phase row is Applied. Read the candidate's original `6_Oracle_Events.txt`, apply each Applied OE-phase fix in-place (replace `original_text` with `proposed_text` per the changes.md row), write the full corrected OE list.
   - **`Tasks/<TASK_DIR>/15_Updated_Rubrics.json`** — written ONLY if any rubric-phase row is Applied. Read the candidate's original `7_Rubrics.json`, apply each Applied rubric-phase fix (replace, split, or remove rubrics per the changes.md row), write the full corrected JSON array. Use flat schema per v9 mandate.
   - **`Tasks/<TASK_DIR>/_aux/REVIEW_prompt_draft.txt`** — written ONLY if any prompt-phase row is Applied. Apply each Applied prompt-phase fix to the candidate's original prompt, write the corrected prompt for the operator to paste back to the platform.

   Do NOT touch `5_Prompt.txt`, `6_Oracle_Events.txt`, or `7_Rubrics.json`. The originals stay pristine for FEEDBACK rating.

4. **Re-run the gate set on the corrected materialization (parity with CB per-phase gates)**:

   ```
   # Set up temp dir mirroring the corrected artifacts as 5/6/7 for validator compatibility
   ```

   For each corrected artifact:
   - **`14_Updated_Oracle_Events.txt`**: `python Validators/validate.py --phase oe` (point at temp copy named `6_Oracle_Events.txt`), then Council A, Council B, **AUDIT `--phase oe`**, then FINAL.
   - **`15_Updated_Rubrics.json`**: `python Validators/validate.py --phase rubrics` (point at temp copy named `7_Rubrics.json`), then Council A, Council B, **AUDIT `--phase rubrics`**, then FINAL.
   - **`_aux/REVIEW_prompt_draft.txt`** (if any prompt row Applied): `python Validators/validate.py --phase prompt` (point at temp copy named `5_Prompt.txt`), then Council A, Council B, **AUDIT `--phase prompt`**.

   Save reports to `_aux/Council_Reports/AUDIT_<phase>.md` (overwrite any prior corrected-phase audit since the artifact has changed). Verdict handling matches CB S1/S2/S3:
   - `PASS (STRICT)` → proceed.
   - `REVISE` → apply the AUDIT fixes to the corrected artifact + re-run gate set (cap 3 rounds).
   - `REBUILD` → STOP. The corrected version itself has structural issues — REVIEW's triage verdict was wrong; recommend `PIPELINE REDO` as the actual fix path.

   AUDIT auto-fires for the same reason it auto-fires in CB S1/S2/S3: catching defects at the producing phase (here, the corrected version is the produced artifact) is cheaper than catching them at FEEDBACK or at platform-reviewer time.

5. **Any BLOCKER on the corrected version means the fix introduced a new issue** — iterate until clean. Originals 5/6/7 stay untouched throughout.

## Exit criteria

- `Tasks/<TASK_DIR>/14_Updated_Oracle_Events.txt` exists IFF any OE-phase row in `changes.md` is Applied.
- `Tasks/<TASK_DIR>/15_Updated_Rubrics.json` exists IFF any rubric-phase row in `changes.md` is Applied.
- `Tasks/<TASK_DIR>/_aux/REVIEW_prompt_draft.txt` exists IFF any prompt-phase row is Applied.
- `_aux/Council_Reports/AUDIT_oe.md` / `AUDIT_rubrics.md` / `AUDIT_prompt.md` exist with `PASS (STRICT)` verdicts for every produced corrected artifact.
- Originals `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json` are UNTOUCHED.

## STOP gate

This phase ends here. End your response. Next-trigger: `PIPELINE FEEDBACK — Tasks/<TASK_DIR>` in a fresh chat to write the candidate-facing 13_Feedback.txt rating the ORIGINAL submission against QC spec, then `PIPELINE CLOSE`.

If MATERIALIZE produced REBUILD verdict OR any AUDIT verdict was REBUILD after 3 REVISE rounds: skip FEEDBACK and route to `PIPELINE REDO — Tasks/<TASK_DIR>`.

Do NOT modify the task contents in this chat beyond what the corrected materialization requires.

## Bootstrap

Read root `AGENTS.md` first. MATERIALIZE is invoked AFTER `PIPELINE REVIEW` produces `changes.md` with Applied rows. It runs the materialization + re-verification that REVIEW used to do inline (pre-v17); the split was made to keep the REVIEW chat context clean and the MATERIALIZE chat focused on apply-and-verify only.
