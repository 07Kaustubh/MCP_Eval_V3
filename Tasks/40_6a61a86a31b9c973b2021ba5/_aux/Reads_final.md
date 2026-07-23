# Reads — PIPELINE FINAL (Task 40, StarPM V4)

## Runbook + framework docs

- `Reference/Sessions/FINAL.md` :: 6-lens cross-artifact holistic council protocol (Truthfulness / Rubric Binding / Cross-Artifact Holism / Red-team / Narrative-State + Action-Prescription / Verifier-Fails-Spec Pre-Upload); hard rules table + BLOCKER/MAJOR severity map; iteration cap 3 REVISE rounds; STOP gate after PASS.
- `AGENTS.md` (root) :: hard rules 1-12; PIPELINE dispatch; StarPM V4 specifics (Opus + Gemini dual-verifier); OE Authority Rule (OEs = CB planning docs, universe SSOT); ML-July-2026 severity table (Over Specific = Moderate, Under Specific = Minor).
- `Reference/AGENTS.md` :: format-card + runbook index.

## Eval specs

- `Evals_starpm/1_Prompt_Eval.md` :: prompt sub-dims (12) applied at integration layer; anti-pattern binary-to-1/3/5 mapping (per pipeline deviations).
- `Evals_starpm/2_Oracle_Events_Eval.md` :: OE sub-dims; unordered-for-coverage + ordered-for-lifecycle-preconditions.
- `Evals_starpm/3_Rubrics_Eval.md` :: rubric sub-dims (5); Bucket 1/2/3 taxonomy for Lens 6 simulation. (hash drift WARN noted; no interpretation-affecting changes).
- `Evals_starpm/4_Verifier_Fails_Eval.md` :: bucket classification framework for Lens 6.

## QC specs

- `Docs_starpm/7_QC_Spec_Doc1.json` :: full sub-dim tree (Prompt 12, Universe 2, OE 2, Rubric 5, Trajectory T1 at FINAL, T2/T3 deferred to S4).
- `Docs_starpm/8_QC_Spec_Doc2.md` :: scoring rubric definitions.

## Reference cards

- `Reference/Council_Protocol.md` :: B3 tool-call density SSOT; Council A + Council B protocols.
- `Reference/Hardness_Playbook.md` :: L1/L2/L5/L7/L8/L9 lever definitions; StarPM adaptation section.
- `Reference/Prompt_Format.md` :: 500-word cap, no em-dashes, no tool names, no "at least N" without mandate.
- `Reference/OE_Format.md` :: opening-verb inventory, tool-parameter binding rules.
- `Reference/Rubric_Format.md` :: FLAT schema, qualifier rules, ML July 2026 severity swap, multi-recipient atomicity.
- `Reference/OE_Convention_Inventory.json` :: tool frequency + opening-phrase patterns extracted from V3 refs.
- `Reference/Strict_Convention_Inventory.json` :: allowed phrasings, verb inventory, evidence-field patterns.

## Learnings + cross-task logs

- `Tasks/_meta/Learnings.md` :: L1-L31 empirical Opus 4.8 failure modes; L31 real-run density underflow pattern (Task 39 avg 35-37 despite 50.5 midpoint).
- `Tasks/_meta/Hardness_Patterns_Log.md` :: prior-task lever combinations.

## Task inputs (all read)

- `Tasks/40_6a61a86a31b9c973b2021ba5/5_Prompt.txt` :: 11-line implicit prompt, water heater at Mesa Vista Unit 7B, ~450 words.
- `Tasks/40_6a61a86a31b9c973b2021ba5/6_Oracle_Events.txt` :: 19 OEs, discovery (1-11) + writes (12-19).
- `Tasks/40_6a61a86a31b9c973b2021ba5/7_Rubrics.json` :: 16 outcome rubrics, 0 process; 8 existence 1.1 rubrics + 8 content 1.2 rubrics on 8 write actions (Airtable + Linear-issue + Linear-comment + Slack-thread + 3 Gmail drafts + Calendar).
- `Tasks/40_6a61a86a31b9c973b2021ba5/_aux/Hardness_Plan.md` :: 6 selected levers (L1/L2/L5/L7/L8/L9); midpoint density 56 (generous) with THIN carry noted at ~49-50; injection plan for 7 records across 5 services.
- `Tasks/40_6a61a86a31b9c973b2021ba5/_aux/Fact_Ledger.json` :: 206 emails, 403 amounts, 192 dates, personas for Carlos/Tanya/Robert verified.
- `Tasks/40_6a61a86a31b9c973b2021ba5/_aux/Universe_Split/` :: 15 tables (airtable, contacts, gcalendar, gmail, hubspot, linear, quickbooks, slack); source-of-truth verified.
- `Tasks/40_6a61a86a31b9c973b2021ba5/_aux/Verification_s1.md`, `Verification_s2.md`, `Verification_s3.md` :: prior-phase PASS confirmed with THIN density carry flag propagated.
- `Tasks/40_6a61a86a31b9c973b2021ba5/_aux/Council_Reports/AUDIT_prompt.md`, `AUDIT_oe.md`, `AUDIT_rubrics.md` :: per-phase strict AUDIT PASS on all 3.
