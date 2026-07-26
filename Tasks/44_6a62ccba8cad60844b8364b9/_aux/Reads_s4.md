# Reads — PIPELINE S4 · Task 44 (dual-model)

**Date:** 2026-07-26 · **Universe:** starpm (V4)

## Eval specs

- `Evals_starpm/4_Verifier_Fails_Eval.md` :: bucket taxonomy (Rubric Invalid / Judge Error / Legitimate Model Failure) and its "run this eval once per model" mandate; applied separately to the Opus and Gemini run sets rather than pooled.
- `Evals_starpm/3_Rubrics_Eval.md` :: All-Failing Rubrics sub-dim, used to score the Bucket 1 ratio on four bases.

## QC spec

- `Docs_starpm/1_Project_Instructions_Overall.md` :: density bar, "average tool call count of all agent runs must be 40+", applied per model (Opus 62.5, Gemini 79.8).
- `Docs_starpm/7_QC_Spec_Doc1.json` + `Docs_starpm/8_QC_Spec_Doc2.md` :: trajectory sub-dims T1 tool-call floor, T2 pass@1 <= 40%, T3 error runs <= 2. All three PASS on both models.
- `Docs_starpm/12_Always_Failing_Rubrics.md` :: what an all-failing justification has to establish; used as the shape check before writing the 31-entry batch.

## Reference cards

- `Reference/Sessions/S4.md` :: phase procedure, the mandatory trajectory walk before classification, the 5-point pre-write checklist, and the V4 dual-model section.
- `Reference/Linter_Playbook.md` :: justification voice (concise, human, no em-dashes, no references to guides or specs, name the concrete fact and the specific gap) and the pre-ship `check_justification.py` gate.
- `AGENTS.md` :: hard rule 11 (V4 density is 40+ per model, not the V3-family 50/40 bands), hard rule 14 (60-criterion ceiling, so no fix may add a criterion), hard rule 13 (single-target uniqueness, relevant to the accept-set fix).

## Per-task data re-read at this phase

- `_aux/Universe_Split/linear.linear_issues.json` + `linear.linear_workflow_states.json` :: every cited workflow state resolved by state id rather than by prose, for all 12 issues named in the classification.
- `_aux/Universe_Split/slack.slack_messages.json` :: the five load-bearing timestamps resolved to exact text and author.
- `_aux/Fact_Ledger.json` :: atom cross-reference for names and dates quoted in the justifications.
- `_aux/Hardness_Plan.md` :: the four pre-registered stump predictions and the pre-registered lever re-attribution rule, scored against actuals.

## Pass 3 (regrade, 2026-07-26 13:24 / 13:28 exports)

All of the above re-read. Additional reads specific to this pass:

- `AGENTS.md` :: hard rules 11 (V4 density 40+ per model), 13 (single-target uniqueness), 14 (60-criterion hard cap, confirmed the set is still at 60).
- `Reference/Sessions/S4.md` :: full runbook including the V4 dual-model section; procedure step 2 (trajectory walk mandatory before classification) applied to every criterion whose decision pattern changed.
- `Reference/Linter_Playbook.md` :: justification voice template, re-applied to the rewritten AF batch.
- `7_Rubrics.json` vs `_aux/7_Rubrics.pre_s4_b1fix.json` :: field-by-field diff establishing the 12:58 edit set (6 evidence fields, criteria 11 / 22 / 23 / 24 / 34 / 48).
- `_aux/Council_Reports/_superseded/pass2_2026-07-26_1245/*` :: prior pass read in full to establish what carries forward (trajectory walks, unchanged) and what does not (every per-cell count).
