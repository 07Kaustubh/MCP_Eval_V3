# Reads — PIPELINE S3 (Rubrics) — Tasks/41_6a61a86a3453b3714bdc72ef

## Reference cards / format
- Reference/Rubric_Format.md :: FLAT 4-field schema {title, category, justification, evidence}; 1.1/1.2/2.1 sub-types; three-condition Process test; approximately/(or similar) rules; absolute-count dilution gates (Major>=3 FAIL).
- Reference/Sessions/S3.md :: phase procedure, exit criteria, Council A/B + AUDIT, coverage matrix.
- AGENTS.md :: hard rules (Outcome>Process, no tool names in titles, no "at least N", StarPM param traps, density 40+ per-model V4).

## Framework guidelines (StarPM v4 = V3 rubric model)
- Docs_starpm/2_Rubrics_V3_Guidelines.md :: two categories (Outcome default / Process rare); agent-centric phrasing 5 rules; verb cheat sheet; self-contained + atomic + approximately rules; service metadata (email recipient/CC/content; Slack channel+content items); Common Mistakes 1-12.
- Docs_starpm/12_Always_Failing_Rubrics.md :: valid vs invalid AF; delete process when outcome covers it; split bundled outcomes; use approximately for rounded; never enumerate tool alternatives in process.

## Eval + QC specs
- Evals_starpm/3_Rubrics_Eval.md :: 5 scored sub-dims (Overall Quality, All-Failing, Category Balance, Process Rubrics, Agent-Centric Phrasing); severity taxonomy Major/Moderate/Minor; HARD GATES: atomicity decomposition, forward coverage, final-response 2.1 coverage, OE-to-rubric xref, exclusion/decoy coverage, act-vs-defer, impossible-derivation, imported-constraint, prompt-vs-rubric action alignment, over-specificity/channel-lock-in (Major default), under-strict/overly-broad per-criterion; threshold table (PASS needs zero Major AND zero Moderate).
- Docs_starpm/7_QC_Spec_Doc1.json (Rubric dimension) :: Overall Rubric Quality (<5% minor, no major/moderate = PASS 5); All-Failing (assess at verifier); Category Balance (#Outcome>#Process binary); Process Rubrics (3-condition, FAIL at 2+ invalid); Agent-Centric Phrasing (FAIL only if non-agent-centric/tool-named, possessive forms valid 06/09).

## Reference corpus (V4 QC_Passed — read all four in full)
- QC_Tasks/V4_Tasks/QC_Passed/Task1/7_Rubrics.json :: 33 rubrics, all Outcome (0 process); 1.1 notify/create/update + 1.2 content + 2.1 final-response facts.
- QC_Tasks/V4_Tasks/QC_Passed/Task2/7_Rubrics.json :: 15 rubrics, all Outcome; email + vendor-outreach + 2.1 findings; heavy content decomposition.
- QC_Tasks/V4_Tasks/QC_Passed/Task3/7_Rubrics.json :: 14 rubrics, 13 Outcome + 1 Process (the sole justified independent-GL-verification process rubric); note the heavy FAIL-clause style in evidence listing decoy figures to reject.
- QC_Tasks/V4_Tasks/QC_Passed/Task4/7_Rubrics.json :: 24 rubrics, all Outcome; closest structural analog (2.1 reports + 1.1 notify + 1.2 content + written-record). Model for this task.

## Tool catalog (for evidence-field tool names only; never in titles)
- StarPM_Base_Universe/7_Server_Tools_Details.json :: create_draft(to[],subject,body) draft-only; slack_send_message(channel_id,message); save_comment(issueId,body); update_records_for_table(baseId,tableId,records[]); search_bills/read_invoice/search_customers etc.
