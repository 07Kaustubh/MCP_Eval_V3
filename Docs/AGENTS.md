# Docs

V3 framework specs and guidelines. Stable per project version. The QC spec docs are the **authoritative** source for pass/fail bands — `Reference/Council_Protocol.md` cites them directly.

## Files (by intent)

| File | Used by |
|---|---|
| `1_Project_Instructions_Overall.md` | Background / orientation — the original CB-facing instructions. |
| `2_Rubrics_V3_Guidelines.md` | Authoritative source for V3 rubric framework (Outcome/Process, three-condition test, agent-centric phrasing). Cited by `Reference/Rubric_Format.md` and `Reference/Sessions/S3.md`. |
| `3_Rubrics_V3_One_Pager.md` | Quick reference summary of V3 rubric rules. |
| `4_Prompt_Hard_Tips.md` | Empirical tips on what defeats Opus 4.8. Cited by `Reference/Hardness_Playbook.md`. |
| `5_Prompt_Diversity_Business_Function.md` | Reference for business-function categories and write-tool diversity. |
| `6_Prompt_Relative_Time_Updates.md` | Fixed-date rules (universe today = 2026-06-12), relative-time resolution logic. |
| `7_QC_Spec_Doc1.json` | **Authoritative QC scoring matrix.** Every council scores against this. |
| `8_QC_Spec_Doc2.md` | QC severity definitions + auditor notes. Cited alongside `7_QC_Spec_Doc1.json`. |
| `9_Common_Error.md` | Catalog of common prompt / OE / rubric mistakes with fixes. Used by REVIEW intake. |
| `10_How_To_Load_and_Edit_Universe.md` | Universe loading instructions. Background only — this pipeline does not edit universes. |
| `11_Taxonomy.md` | Task version taxonomy. |
| `12_Always_Failing_Rubrics.md` | AF rubric patterns. Cited by `Reference/Sessions/S4.md` for AF justification reasoning. |

## When to consult Docs

- **Pass / fail bands:** `Docs/7_QC_Spec_Doc1.json` + `Docs/8_QC_Spec_Doc2.md`. These are the SOLE source of truth for scoring. If a runbook description conflicts with the QC spec, the QC spec wins.
- **Rubric framework:** `Docs/2_Rubrics_V3_Guidelines.md` + `Docs/3_Rubrics_V3_One_Pager.md`. `Reference/Rubric_Format.md` is the operational distillation; the docs are the original.
- **Hard tips:** `Docs/4_Prompt_Hard_Tips.md`. `Reference/Hardness_Playbook.md` is the operational lever catalog; the doc is the empirical observation source.

## What does NOT change here

These are project-stable. Update only when the upstream framework changes (new V3 sub-version, new universe major release).
