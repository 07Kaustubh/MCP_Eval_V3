# TODOs — PIPELINE S4 · Task 43_6a62ccaf5853030245ac9d53 (StarPM V4, dual-model)

Every step of `Reference/Sessions/S4.md` Procedure as a discrete atomic todo. v11 E1 operator-discipline gate.

| # | Step | State |
|---|---|---|
| 0 | Create this TODO file | completed |
| 1 | `phase_ready.py --phase s4` | completed (blocked on upstream `Verification_final.md` heading contract; normalized, re-run clean) |
| 2 | `parse_trajectories.py` — measured pass@1 + density per model | completed |
| 3 | T3 Error Rate gate (erroneous runs per model) | completed |
| 4 | T2 Agent Failure Rate gate (pass@1 <= 40%) per model | completed |
| 5 | T1 density gate per model (StarPM 40 design target / 15 fail floor) | completed |
| 6 | Build rubric x run matrix (25 rubrics x 12 runs, both models) | completed |
| 7 | Re-derive ground truth from `_aux/Universe_Split/` (bills, invoice, summary email, Airtable make-ready) | completed |
| 8 | Trajectory walk — AF cluster R1/R6/R8/R10/R12/R19/R21/R24 (closet-trim root) | completed |
| 9 | Trajectory walk — AF R16 (make-ready record final owner cost) | completed |
| 10 | Trajectory walk — partial fails R4, R7, R15, R17, R22, R25 | completed |
| 11 | Trajectory walk — R18 (parser normalization, platform markdown-linked title) | completed |
| 12 | Classify every failing rubric into exactly one bucket, with `Run X, tool call Y` citation | completed |
| 13 | Apply v15 5-point pre-write checklist before every AF justification | completed |
| 14 | Confirm every Bucket 1 / Bucket 2 call against `_aux/Universe_Split/` re-grep | completed |
| 15 | Compute Bucket 1 ratio + score All-Failing Rubrics sub-dim | completed |
| 16 | Write `_aux/Council_Reports/S4_fixes.md` (Bucket 1) | completed |
| 17 | Write `_aux/Council_Reports/S4_judge_errors.md` (Bucket 2) | completed |
| 18 | Write `_aux/Council_Reports/S4_AF_justifications.md` (Bucket 3) | completed |
| 19 | `check_justification.py` exit 0 on the AF batch | completed |
| 20 | Update `_aux/Hardness_Plan.md` calibration vs actual AF set | completed |
| 21 | Append calibration delta to `Tasks/_meta/Hardness_Patterns_Log.md` | completed |
| 22 | Confirm / correct predictions in `Tasks/_meta/Stump_Hypotheses.md` | completed |
| 23 | Write `_aux/Council_Reports/S4_verdict.md` (matrix + classifications + calibration) | completed |
| 24 | Write `_aux/Verification_s4.md` cross-source check (v16) | completed |
| 25 | Append novel finding to `Tasks/_meta/Learnings.md` | completed |
| 26 | STOP gate — hand back to operator, do not loop S4 in this chat | completed |
