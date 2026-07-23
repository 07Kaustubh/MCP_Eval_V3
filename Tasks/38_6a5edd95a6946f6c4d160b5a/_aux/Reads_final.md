# Reads_final.md — v11 E2 spec/reference reading log for FINAL phase

## Runbook + protocol
- Reference/Sessions/FINAL.md :: 6-lens cross-artifact holistic council spec; hard-rule table + STOP gate + verifier-fails Lens 6 threshold (20% Bucket_1_Risk)
- Reference/Council_Protocol.md :: council report format + B3 tool-call density SSOT (50+ design target, 40-49 THIN)
- AGENTS.md (root) :: 12 hard rules + Pipeline Deviations table + StarPM universe constants (Slack `message` param, Gmail draft-only `body`, Linear `team`, current-date 2026-07-01 America/Chicago)

## QC spec docs
- Docs_starpm/7_QC_Spec_Doc1.json :: sub-dim scoring rubric (Prompt / Universe / OE / Rubric / Trajectory)
- Docs_starpm/8_QC_Spec_Doc2.md :: prose amplification of scoring rules
- Docs_starpm/2_Rubrics_V3_Guidelines.md :: outcome > process rule, atomic write-action rubric convention, three-condition test for Process
- Docs_starpm/12_Always_Failing_Rubrics.md :: AF patterns not to test at write time (deferred to S4)

## Eval specs
- Evals_starpm/1_Prompt_Eval.md :: em-dash / tool-name / pre-solving / word-cap FAIL conditions
- Evals_starpm/2_Oracle_Events_Eval.md :: numbered-prose + opening-verb coverage + tool-name existence checks
- Evals_starpm/3_Rubrics_Eval.md :: agent-centric phrasing / "at least N" / naturalness heuristic
- Evals_starpm/4_Verifier_Fails_Eval.md :: bucket classification rules (Lens 6 simulation source)

## Reference cards
- Reference/Rubric_Format.md :: flat schema {title, category, justification, evidence}
- Reference/OE_Format.md :: `OE<N>:` prefix + expected-discovery pattern
- Reference/Prompt_Format.md :: implicit-vs-explicit framing + persona voice + word cap
- Reference/Strict_Convention_Inventory.json :: allowed phrasings extracted from V3 reference rubrics
- Reference/OE_Convention_Inventory.json :: tool frequencies + parameter traps + opening-phrase patterns
- Reference/Hardness_Playbook.md :: lever catalog (L1-L15) with StarPM-applicable subset

## QC reference examples
- QC_Tasks/V4_Tasks/QC_Passed/Task1-Task4/7_Rubrics.json :: phrasing patterns, evidence shapes, outcome-type usage for V4 framework

## Task-specific inputs
- Tasks/38_6a5edd95a6946f6c4d160b5a/5_Prompt.txt :: Denise Morales end-of-week brief to Aurora; 3 items (208B, Ridgeview roof, Tanya)
- Tasks/38_6a5edd95a6946f6c4d160b5a/6_Oracle_Events.txt :: 31 OEs; OE21/22/25 corrected to route via QB bills (no 2026-494)
- Tasks/38_6a5edd95a6946f6c4d160b5a/7_Rubrics.json :: 22 rubrics, all outcome, evidence cites OE for each write action
- Tasks/38_6a5edd95a6946f6c4d160b5a/_aux/Hardness_Plan.md :: 5 selected levers (L9, L11, L2, L8, L6) with stump hypothesis
- Tasks/38_6a5edd95a6946f6c4d160b5a/_aux/Fact_Ledger.json :: atom surface for grounding sweep
- Tasks/38_6a5edd95a6946f6c4d160b5a/_aux/Universe_Index/today_horizon.json :: 2026-07-01 America/Chicago
- Tasks/38_6a5edd95a6946f6c4d160b5a/_aux/Verification_s1.md / _s2.md / _s3.md :: prior phase verdicts + THIN_DENSITY carry rationale
- Tasks/38_6a5edd95a6946f6c4d160b5a/_aux/Council_Reports/FINAL_council_prev_0221.md :: archived stale FINAL council report used only as historical drift context
- Tasks/_meta/Learnings.md :: empirical Opus 4.8 failure modes L1-L16
