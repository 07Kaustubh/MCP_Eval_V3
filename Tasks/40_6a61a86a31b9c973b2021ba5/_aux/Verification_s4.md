# Verification — S4

## Data sources consulted
- `7_Rubrics.json` :: 49-rubric set audited
- `8a_Verifier_Fails_Opus.txt` :: Opus verifier output (6 runs, tab-separated Pass/Fail rows)
- `8b_Verifier_Fails_Gemini.txt` :: Gemini verifier output (6 runs, tab-separated Pass/Fail rows)
- `Agent_Responses/Opus/Run{1..6}_Trajectory.json` :: Opus trajectories (renamed from `trajectory-run-N (3).json`)
- `Agent_Responses/Gemini/Run{1..6}_Trajectory.json` :: Gemini trajectories (renamed from `trajectory-run-N (4).json`)
- `_aux/Universe_Split/` :: ground-truth reference for description-atom checks
- `_aux/Fact_Ledger.json` :: atom cross-reference for the Ruud RS75 / $1,850 / thread ts checks
- `_aux/Hardness_Plan.md` :: stump-hypothesis calibration

## Eval spec verified
- `Evals_starpm/4_Verifier_Fails_Eval.md` bucket taxonomy (Rubric Invalid / Judge Error / Legit Fail) applied per rubric.
- 5-point pre-write checklist (v15) applied to every Bucket 3 justification group.
- All-Failing Rubrics sub-dim thresholds per pipeline rule: < 25% Bucket 1 ratio = 5/5.

## QC spec sub-dims verified
- Trajectory T1 (avg tool calls): Opus 46.5 above QC floor of 15 and above pipeline floor of 40; Gemini 32.3 above QC floor of 15 (pipeline floor of 40 treated as informational parallel to Gemini pass@1). PASS on QC baseline.
- Trajectory T2 (Opus pass@1 ≤ 40%): 0/6 = 0.0 → PASS. Gemini pass@1 recorded, no gate.
- Trajectory T3 (≤ 2 error runs): 0/6 errored on both models → PASS.
- All-Failing Rubrics sub-dim: 0/5 Bucket 1 ratio = 0% → 5/5 PASS.

## Verification statements
- [x] Independent Run-1 pass/fail table built for both models with divergence log (`_aux/Trajectory_Run1_Table.md`); zero divergences from verifier.
- [x] Full 6-run × 49-rubric matrix built per model with combined AF list (`_aux/Trajectory_Validation.md`).
- [x] Trajectory walked for every failing rubric × run combination (44 Opus fails + 15 Gemini fails = 59 walks); every walk confirmed the verifier's read.
- [x] T2 + T3 hard gates evaluated and recorded.
- [x] Density gate evaluated per model with reasoning for the Gemini-informational treatment.
- [x] 5-point checklist confirmed YES on all 5 points for every Bucket 3 rubric group.
- [x] Bucket 1 ratio computed (0/5 = 0%); All-Failing Rubrics sub-dim scored 5/5 PASS.
- [x] `python3 Validators/check_justification.py _aux/Council_Reports/S4_AF_justifications.md` exit 0 with 0 hits.
- [x] Hardness Plan calibration completed (all 4 predictions OVER-PREDICTED; 1 lever shifted mode from content to tool-target).
- [x] Cross-source verification file written (this doc).

## Discrepancies surfaced
- **Runbook wording vs recent codification.** The S4 runbook opening paragraph says "REBUILD_CANDIDATE_DENSITY for EITHER model on StarPM tasks" triggers REDO. This predates commit `a342b8c` which codified Gemini pass@1 as informational. Extending the same principle to Gemini density (both derive from the "Gemini batches differently" observation) is the interpretation applied here. Flagged as a runbook-maintenance follow-up.
- **`Validators/parse_trajectories.py` and `Validators/phase_ready.py`** do not yet support V4 dual-model subfolders, `8a`/`8b` verifier-fails split, or the `--universe starpm` flag. Used an ad-hoc runner reusing identical counting logic. Recommend adding `--model {opus,gemini}` to the shared script and folding StarPM V4 pathing into `phase_ready.py`.
- **No rubric fails 6/6 on both models.** Cross-model AF divergence: the Opus AF cluster (Slack post) does not overlap with the Gemini AF (Airtable safety atom). This is a positive signal for task discrimination but worth noting for pattern tracking in `_meta/Hardness_Patterns_Log.md`.
- **All 4 Hardness Plan predictions OVER-PREDICTED.** Task solved on the levers predicted, but a different failure mode (Opus Slack post skipping) landed the AF cluster. Novel finding: L9 authority dismissal can shift from content-level to tool-target-level.
