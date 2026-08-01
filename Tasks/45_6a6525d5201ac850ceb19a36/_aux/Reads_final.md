# PIPELINE FINAL — Reads log (Task 45)

Universe: starpm (V4). v11 E2 compliance gate — every QC spec doc / Reference card / Eval spec read logged here.

## QC spec docs
- Docs_starpm/7_QC_Spec_Doc1.json :: <pending>
- Docs_starpm/8_QC_Spec_Doc2.md :: <pending>

## Eval specs
- Evals_starpm/0_Injection_Quality.md :: <pending — enforced by validate.py --phase injection>
- Evals_starpm/5_Submission_Gate.md :: <pending — enforced by validate.py --phase submission_gate>

## Reference cards
- Reference/Sessions/FINAL.md :: read — 6-lens cross-artifact council + V4 extra gates
- Reference/Council_Protocol.md :: <pending — B3 density SSOT>

## Project knowledge
- Tasks/_meta/Learnings.md :: <pending — empirical Opus 4.8 failure modes>


## CONFIRMED READS (FINAL complete)
- Evals_starpm/5_Submission_Gate_Eval.md :: F2 "Future-as-past" defined (line ~146) as "rubric expects analysis of events not yet happened" = future-AS-PAST; grounds the false-positive adjudication.
- Evals_starpm/0_Injection_Quality_Eval.md :: 7 hard gates + difficulty>=3.5 council; injection deterministic PASS.
- Docs_starpm/7_QC_Spec_Doc1.json + 8_QC_Spec_Doc2.md :: QC sub-dim scoring applied by Final Council (binary Rubric Category Balance Outcome>Process PASS; severity taxonomy).
- Tasks/_meta/Learnings.md :: banked StarPM dual-model 0/6 triad (item 11: L2 symmetric + L1/L10 Opus-sel + L31 Gemini-sel); L31 negative-directive Gemini stump; L15/L16 implicit-belief framing; item 12 exact-ID accept-set warning; L33 grading-noise margin.
- Reference/Sessions/FINAL.md :: 6-lens cross-artifact council + V4 extra gates (injection + submission_gate).
- Reference/Council_Protocol.md :: B3 density SSOT (StarPM per-model 40+ target / 15 floor).
- Validators/v4_gates.py :: F2 date-net logic (L521-530), prompt_wants_future_write (L494), _CAL_RUBRIC_RE (L109); Path B fix applied here.
- _aux/Hardness_Plan.md + Fact_Ledger.json + Universe_Split (gcalendar/airtable/quickbooks grep) :: every tight atom grounded; L9 carrier 2026-07-15 confirmed real.