# Evals

Phase eval specs. Each is a long prompt the original CB workflow uses to drive Cursor agents through structured quality checks.

## Files

| File | Phase | Pipeline invocation |
|---|---|---|
| `1_Prompt_Eval.md` | Prompt | Loaded by `Reference/Sessions/S1.md` and `Reference/Sessions/REVIEW.md`. The runbook hands this verbatim to Council B. |
| `2_OE_Eval.md` | Oracle Events | Loaded by `Reference/Sessions/S2.md` and `Reference/Sessions/REVIEW.md`. |
| `3_Rubrics_Eval.md` | Rubrics | Loaded by `Reference/Sessions/S3.md` and `Reference/Sessions/REVIEW.md`. |
| `4_Verifier_Fails_Eval.md` | Verifier-fails analysis | Loaded by `Reference/Sessions/S4.md`. |

## Relationship to the pipeline

Pre-pipeline, these were invoked directly by operators ("Evaluate `5_Prompt.txt` using `1_Prompt_Eval.md`"). The pipeline embeds them inside the PIPELINE S1/S2/S3/S4 runbooks so each phase runs end-to-end from a single trigger phrase. The eval specs themselves are unchanged — the runbooks just orchestrate their invocation and integrate validator + council outputs.

## What does NOT change here

These specs are stable per project version. Update only when the QC scoring matrix changes (`Docs/7_QC_Spec_Doc1.json`).
