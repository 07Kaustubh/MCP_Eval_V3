# Reads - S3 Rubrics (Tasks/39_6a602c8886ebb06f12354d77, universe=starpm/V4)

## Runbook + format cards
- Reference/Sessions/S3.md :: S3 procedure - outcome-first, three-condition Process test, flat schema, validator + Council A (grounding) + Council B (adversarial ultrabrain) + AUDIT, coverage matrix, StarPM density 40+ design target.
- Reference/Rubric_Format.md :: FLAT 4-field schema {title,category,justification,evidence}; outcome>process; agent-centric; no tool names in title; no "at least N"; self-contained; atomic; grounded substring sweep; flexibility patterns; absolute-count dilution gates when < 30 rubrics.

## StarPM V4 framework docs
- Docs_starpm/2_Rubrics_V3_Guidelines.md :: two categories (Outcome default / Process optional, zero-process norm); 1.1 write-action + 1.2 content + 2.1 key-facts; mixed task adds 2.1 only if prompt also asks to report findings directly (this prompt does); method-agnostic when the prompt names a goal not a method; approximately only for calculated/rounded (never counts/IDs/dates); service metadata (email recipient+content, slack channel+content items); atomic per item, split claims that could fail independently; pass@1 <= 40%.

## Reference corpus (V4 passed - voice)
- QC_Tasks/V4_Tasks/QC_Passed/Task2_6a27b70a80b7729ca5d6d88d/7_Rubrics.json :: 15 rubrics, all outcome, zero process; self-contained titles embedding emails/IDs/amounts; 1.1/1.2/2.1 mix; method-flexible tracking rubric ("may use a reminder, calendar event, Linear issue, or Airtable record").

## Task inputs
- 5_Prompt.txt :: James asks to (a) figure out where 8D really stands + confirm each piece landed, (b) advance whatever is still open, (c) square up the logged record, (d) post an update in the make-ready channel, (e) draft John a status email (stands / outstanding / what it takes).
- 6_Oracle_Events.txt :: 12 OEs. Writes: OE8 advance disposal blocker (Linear comment on OPS-227 or Slack to John), OE9 update tblMakeReady receb057b02f20052 selReady->selProg + notes rewrite, OE11 slack C004 #make-ready, OE12 gmail draft to john.smith@starpm.com.
- _aux/Hardness_Plan.md :: 5 levers - L10 supersession, L2 Airtable-SoR skip, L1 latching, L4 search-cap eviction, L3 missing reply; per-model density midpoint 48.5 (StarPM 40+ design PASS).
- _aux/Verification_s2.md :: S2 OE cross-source verification (section headers reconciled to check_verification.py at this phase).

## Grounding sources (per-task data)
- _aux/Fact_Ledger.json :: 206 emails / 403 amounts indexed; john.smith@starpm.com, OPS-227, MT-2026-1271, slack C001-C008 confirmed present.
- _aux/Universe_Split/ :: verbatim rows - receb057b02f20052 (stale selReady "cleared for leasing - available to show immediately"), recf7aecc318b2252 (in-house selProg), rec651427ec0d84dd5a (refrigerator swap 6/25, selProg, target 2026-06-26), recac236210094352 (MT-2026-1271, fldCompletionDate blank = OPEN), recb403fe04c2f97683 (Rio Bend 214 MT-2026-1325, done 2026-06-25, near-miss twin); linear comment_16a0a0c53f... (2026-06-22 "The 8D disposal is seized ... flywheel is frozen ... full unit replacement ... parts approval"); OPS-227 "Clear garbage disposal jam - Las Palmas 8D" team_001; contacts john.smith@starpm.com (Lead Maintenance Technician); slack C004 #make-ready, C001 #maintenance.

## Eval + QC spec (scored via Council B / AUDIT - see _aux/Council_Reports)
- Evals_starpm/3_Rubrics_Eval.md :: rubric sub-dims (Overall Rubric Quality, Category Balance, Process Rubrics, Agent-Centric Phrasing) - delegated to Council B for full scoring against this set.
- Docs_starpm/7_QC_Spec_Doc1.json :: Rubric dimension sub-dims + appendix issue types - delegated to Council B and AUDIT for scoring.
