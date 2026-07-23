# Todos — S4

- [x] Phase-ready gate: per-model trajectory parsing via ad-hoc runner (Opus + Gemini) writing `_aux/Trajectory_Stats_Opus.json` + `_aux/Trajectory_Stats_Gemini.json`.
- [x] T3 Error Rate Gate: 0/6 errored on both models → PASS.
- [x] T2 Agent Failure Rate Gate: Opus 0/6 pass@1 = 0.0 → PASS (≤ 40%); Gemini 0.0 informational.
- [x] Density Gate: Opus 46.5 THIN (above 40 floor); Gemini 32.3 informational (parallel to Gemini pass@1 per commit `a342b8c`); density STOP reversed after user override + review of QC criteria.
- [x] Independent Run-1 Pass/Fail Table (both models) written to `_aux/Trajectory_Run1_Table.md`; 0 divergences from verifier.
- [x] Full Trajectory Validation matrix (6 runs × 49 rubrics × 2 models) written to `_aux/Trajectory_Validation.md` with divergence summary + combined AF list.
- [x] Trajectory walked for every failing rubric × run: 44 Opus fails + 15 Gemini fails = 59 walks. All verifier reads confirmed.
- [x] Bucket 1 fixes drafted to `_aux/Council_Reports/S4_fixes.md`: 0 hard defects, 2 soft atomicity refinement suggestions (non-blocking).
- [x] Bucket 2 judge errors drafted to `_aux/Council_Reports/S4_judge_errors.md`: 0 entries; every verifier decision matched independent read.
- [x] Bucket 3 AF justifications drafted to `_aux/Council_Reports/S4_AF_justifications.md`: 14 justification groups covering all failing rubric × model combinations.
- [x] `check_justification.py` exit 0 with 0 hits on the AF batch.
- [x] All-Failing Rubrics sub-dim scoring: Bucket 1 ratio 0/5 = 0% → 5/5 PASS.
- [x] Hardness Plan calibration: 0/4 direct hits (all OVER-PREDICTED), 1 lever shifted mode; novel findings documented.
- [x] `_meta/Stump_Hypotheses.md` append (L9-payoff-shift + Gemini safety-atom-drop patterns).
- [x] `_meta/Hardness_Patterns_Log.md` append (cross-model AF divergence + Opus Slack thread-anchor stump).
- [x] `S4_verdict.md` written with full classification.
- [x] `Verification_s4.md` written with cross-source verification.
