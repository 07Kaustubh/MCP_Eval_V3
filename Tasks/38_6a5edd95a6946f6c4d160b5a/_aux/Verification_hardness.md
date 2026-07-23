# Verification — HARDNESS phase — Tasks/38_6a5edd95a6946f6c4d160b5a

## Sources consulted

### Per-task data
- _aux/Universe_Split/airtable.airtable_records.json :: tblMakeReady (120 records) and tblMaintenanceTickets (51 records) scanned for make-ready status, unit assignments, vendor assignments, costs, and "Unit 14" variant rows; MT-2026-047 cited as load-bearing record for Ridgeview roof chain; 7 "Unit 14"-flavored rows identified as L6 lever.
- _aux/Universe_Split/quickbooks.quickbooks_entities.json :: bills (114), invoices (155), credit_memos (118), payments (54) scanned; QB bills 2026-481 and PD-2026-084 identified as the double-bill L11 lever; QB invoice 2026-494 as owner pass-through; QB payment 972286822645 ($640 partial) as outstanding-balance signal; QB credit memo CM-2026-0095 (-$175) as L10 reversal lever.
- _aux/Universe_Split/slack.slack_messages.json :: C001 #maintenance scanned for Tony Reyes authority-dismissal message on Sunset Ridge 208B AC ticket; C002 #leasing for ESA reasonable-accommodation Tanya thread; C003 #general for "unit 4B is now two months past due" Tanya Las Palmas 4B confirmation.
- _aux/Universe_Split/gmail.gmail_messages.json :: "HVAC Inspection Findings - Sunset Ridge Unit 208B" thread from service@alamohvac.com identified as L9 ground-truth source; "No AC - Sunset Ridge Apt 208B" from Gabriella Torres as complaint anchor; Brooke/Pete/Robert Finley "$8,400 approved scope" thread as L13 first-framing anchor.
- _aux/Universe_Split/linear.linear_issues.json + linear.linear_comments.json :: 231 issues, 48 comments scanned for open Sunset Ridge 208B and Ridgeview roof issues; Linear confirmed as secondary (mirror) to Airtable.
- _aux/Fact_Ledger.json :: amounts list (403 entries) checked for $8,400, $16,800, $175, $640 presence; all confirmed. Personas list confirmed Tony Reyes (Lead Maintenance Technician), Aurora Winona (President), Gabriella Torres (Tenant), Tanya Mitchell (Tenant).

### Eval spec
- Evals_starpm/0_Injection_Quality_Eval.md :: not applicable for CB task (no injection). Noted.
- Evals_starpm/5_Submission_Gate.md :: density floor 40 avg tool calls, pass@1 <= 40%; projected midpoint 50.0 meets the design target.

### QC spec
- Docs_starpm/7_QC_Spec_Doc1.json :: Trajectory T1 Tool Call Count sub-dim checked; projected midpoint 50.0 falls in PASS band (>= 50 design target).
- Reference/Hardness_Playbook.md :: All 11 levers considered. Levers 2, 6, 8, 9, 11 selected. Levers 1/3/4/5 assessed as partial or weaker-standalone; lever 7 incorporated as write-action density requirement; lever 10 incorporated as secondary signal under L2.
- Tasks/_meta/Learnings.md :: L9 (authority-figure dismissal, ~100% fail) cited for Lever 9 selection. L10 (structured-DB skip analog) cited for Lever 2 (QB as invisible structured DB). L11 + L13 cited for net-vs-gross + first-framing trap. L8 cited for multi-link chain. L4 + L13 cited for near-miss entity (combined lever, not standalone). L15 + L16 cited as prompt design rules.

## Verification statements

- [x] At least 3 levers selected (5 selected: L2, L6, L8, L9, L11); each cites a Learnings.md entry.
- [x] Density midpoint projection is PASS (>= 50): midpoint = 50.0.
- [x] Service breadth table populated (v11 G1): 8 services, 6 above 5%, dominant QB at 22%.

## Discrepancies surfaced
- none

## Verdict
PASS — 5 levers selected (L2, L6, L8, L9, L11), each grounded in per-task universe atoms. Density midpoint 50.0 meets the 50+ design target. Service breadth 8 services with no dominant service above 60%. All verification statements confirmed.
