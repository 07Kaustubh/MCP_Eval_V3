# Reads — S3 (Rubrics)

Log of every QC spec / Reference card / Eval spec / QC reference consulted.

- Reference/Sessions/S3.md :: full runbook; OE-write-action → 1.1, prompt tell-me → 2.1, three-condition test before any Process, atomicity, flat schema, coverage matrix, mandatory AUDIT auto-fire.
- Reference/Rubric_Format.md :: FLAT schema (4 fields), Outcome > Process, agent-centric phrasing, tool names forbidden in title (allowed in evidence/justification), atomicity rules, ML July 2026 severity swap (Overly Specific → Moderate; Under Specific → Minor), multi-recipient send rule.
- Reference/Strict_Convention_Inventory.json :: verb inventory by sub-type; qualifier rules (approximately for calculated; or similar for free-text; never for exact-match values); atomicity bundling rules.
- Evals_starpm/3_Rubrics_Eval.md :: hash-drift WARN observed at phase-ready; sub-dim scoring deferred to Council B.
- Docs_starpm/2_Rubrics_V3_Guidelines.md :: standing knowledge; StarPM V4 rubrics follow V3 conventions with July 2026 severity updates.
- Docs_starpm/12_Always_Failing_Rubrics.md :: standing knowledge; AF patterns applied preemptively (no "at least N", no tool names in titles, no channel lock-in without prompt mandate).
- QC_Tasks/V3_Tasks/Task11..Task14 :: 59 outcome rubrics, 0 process — voice/structure internalized.
- Tasks/40_6a61a86a31b9c973b2021ba5/_aux/Fact_Ledger.json :: every concrete value in rubric titles verified — emails (Tanya, Robert, ap@hillcountryplumbing), amounts (310.00 and 1850.00 both present), dates (2026-07-02 Thursday), slack channel C001, personas Carlos/Tony/Tanya/Robert.
- Tasks/40_6a61a86a31b9c973b2021ba5/_aux/Universe_Split/airtable.airtable_records.json :: rec92f4a1c8e17bd3 / MT-2026-1327 / fldPriority selMedium (pre-update) verified via row_data JSON parse.
- Tasks/40_6a61a86a31b9c973b2021ba5/_aux/Universe_Split/linear.linear_issues.json :: OPS-231 "Mesa Vista 7B water heater diagnostic and scope decision" / assignee Carlos / state_OPS_2 / priority 2 verified.
- Tasks/40_6a61a86a31b9c973b2021ba5/_aux/Universe_Split/quickbooks.quickbooks_entities.json :: bill 195836274018 / B2026-211 / VendorRef Hill Country Plumbing (201) / Line[0].Description carries "12 yr Ruud RS75 water heater at Mesa Vista Unit 7B... Full unit replacement recommended, approx 1850 dollars" verified.
- Tasks/40_6a61a86a31b9c973b2021ba5/_aux/Universe_Split/slack.slack_messages.json :: 3 injected messages verified — ts 1782789240.000301 (Tony authority) / ts 1782824160.000302 (Carlos parent) / ts 1782863220.000303 (Carlos reply, thread_parent_id links to 1782824160.000302) — all in C001.
- Tasks/40_6a61a86a31b9c973b2021ba5/_aux/Universe_Split/gmail.gmail_messages.json :: msg e2f3a4b5c6d789ab / thread d1e2f3a4b5c6789a / from ap@hillcountryplumbing.com / subject "Mesa Vista 7B water heater diagnostic summary and next steps" verified; body base64-decoded matches OE 5.
- Tasks/40_6a61a86a31b9c973b2021ba5/_aux/Verification_s2.md :: OE-phase verification PASS with THIN density flag carried forward.
- Tasks/40_6a61a86a31b9c973b2021ba5/_aux/Hardness_Plan.md :: 6 levers L1/L2/L5/L7/L8/L9; scope truth load-bearing in QB Line[0].Description.
- StarPM parameter traps (root AGENTS.md StarPM constants): `slack_send_message(channel_id, message)` NOT draft; Gmail `create_draft(to[], subject, body)` is draft-only; Linear `save_issue(..., team, ...)`, `save_comment(issueId, body)`; Airtable camelCase.
