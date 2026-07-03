# S4 Reads Log (v11 E2 compliance gate)

Task: `Tasks/35_6a4421ec8169e23828bb442d`

## QC spec / Reference / Eval docs consulted

- `Reference/Sessions/S4.md` :: full runbook — trajectory hard gates (T2/T3), rubric x run matrix, 5-point pre-write checklist, 3-bucket classification, All-Failing Rubrics sub-dim scoring, Bucket-1-ratio table.
- `Evals_keystone/4_Verifier_Fails_Eval.md` (via Docs framework) :: Bucket-1 / Bucket-2 / Bucket-3 taxonomy; pipeline extension per AGENTS.md deviation table (Phase 3.3 override — full trajectory access via `Agent_Responses/Run*.json`).
- `Docs_keystone/12_Always_Failing_Rubrics.md` (per Hardness_Plan reproduction) :: Valid-AF-rubrics guidance — Outcome-bundles-multiple-independent-facts pattern (item 3 in Rubric_Format), "split into separate atomic rubrics so each fact is evaluated on its own" rule.
- `Reference/Linter_Playbook.md` :: AF justification voice template — first person, cite concrete fact + specific gap, no em-dashes, no guide references. (Not authored this phase — Bucket 3 empty; see verdict.)
- `Docs_keystone/7_QC_Spec_Doc1.json` (referenced) :: All-Failing-Rubrics sub-dim ownership deferred to verifier stage; S4 v11 makes scoring explicit.
- `AGENTS.md` root :: Pipeline Deviations table item on "Rubrics Eval Phase 4.2 threshold math allows dilution"; item on "All-Failing Rubrics sub-dim defers to verifier stage" (pipeline scoring at S4 with 50%/25% thresholds).
- `_aux/Hardness_Plan.md` :: 5 selected levers (Learnings §L8 §L9 §L10 §L25 §L26) + stump hypothesis and lever-by-lever expected trajectory footprint; density mid 52 met (measured 59); §L25 supersession lever explicitly predicts the "3/20 preliminary plan superseded" failure mode.
- `_aux/Trajectory_Stats.json` :: 6/6 runs completed (T3 PASS), pass@1 = 0/6 = 0% (T2 PASS), avg 59 tool calls (density PASS well over 50 design target).
- `_aux/Verification_s1.md / Verification_s2.md / Verification_s3.md / Verification_final.md` :: prior-phase PASS verdicts, cross-source discipline record, PROPAGATE flags resolved.
- `Tasks/_meta/Stump_Hypotheses.md` :: cross-task lever calibration history — updated this phase with §L25 supersession-lever confirmation and DM-aggregate-count observation.
- `Tasks/_meta/Hardness_Patterns_Log.md` :: cross-task hardness pattern log — appended with "DM aggregate-count-plus-qualifier bundling" as the recurring rubric-defect pattern for short-status leadership messages.
