# Reads — S2 (reference-doc reading log, v11 E2)

## QC + Eval specs
- `Docs/7_QC_Spec_Doc1.json` :: Oracle Event dimension sub-dims (OE Completeness, OE Accuracy) re-checked for scoring contract; MoveOps V2.1 has no separate OE QC spec, Brookfield-V3 spec used per AGENTS.md Pipeline-Deviations table.
- `Evals/2_Oracle_Events_Eval.md` :: OE Completeness Phase 3.2 forward+reverse coverage protocol confirmed; OE Accuracy tool-name + parameter-name + expected-value grounding confirmed.
- `Docs_moveops/2_Rubrics_V3_Guidelines.md` :: MoveOps V2.1 delta read; no OE-phase deltas surfaced (deltas concentrate in rubric scoring; OE accuracy/completeness scoring same as Brookfield-V3).

## Reference cards
- `Reference/Sessions/S2.md` :: this runbook (Procedure 1-9, Exit criteria, STOP gate, AUDIT auto-fire conditional triggers per Track F v21).
- `Reference/OE_Format.md` :: numbered prose; exact `verb_noun_subject` tool tokens; parameter traps (`content` not `body` for email/messaging; `payload` not `text` for Slack; Linear comment uses `issueId + body`; airtable_update_records takes `base_id + table_id + fields`); discovery-step phrasing voice; final-paragraph summary OK.
- `Reference/OE_Convention_Inventory.json` :: auto-extracted V3 convention frequencies (tool-usage, opening-phrase patterns); Council A convention sweep reads this.
- `Reference/Council_Protocol.md` :: Council A (Grounding, 9 perspectives) + Council B (Adversarial QC, 8 perspectives: B1 QC scoring, B2 second-reading, B3 density, B4 lever preservation, B5 entity weave, B6 process-rubric propagation, B7 fabricated-IDs, B8 forward-map to rubrics, B9 reverse-map prompt-to-OE).
- `Reference/Hardness_Playbook.md` :: 11-lever catalog; selected levers L1/L2/L7/L8/L11 confirmed for OE preservation (every selected lever must be exercised by at least one OE step per Council B-B4).

## Tool catalog
- `MoveOps_Base_Universe/6_Server_Tools_Details.json` :: MoveOps tool definitions verified for email_send_email (content), email_reply_to_email (content), email_search_emails, email_get_email, messaging_send_message (content), slack_conversations_search_messages, slack_conversations_get_messages, slack_conversations_add_message (payload), airtable_list_records, airtable_get_record, airtable_update_records (base_id + table_id + fields), quickbooks_get_bill, quickbooks_list_bills, quickbooks_get_vendor, quickbooks_get_account, quickbooks_get_customer, quickbooks_list_invoices, linear_get_issue, linear_create_comment (issueId + body), linear_list_comments, contacts_search_contacts, contacts_get_contact, crm_search_companies, crm_get_company, crm_get_deal, crm_search_engagements, reminders/calendar tool path (calendar_create_event / reminders create).

## Per-task data
- `_aux/Universe_Split/*` :: 25 sources; key targets cross-verified (email.emails 494, slack.slack_messages 354, airtable.records 167, quickbooks.bills 17, linear.linear_issues 69).
- `_aux/Universe_Index/today_horizon.json` :: universe today = 2026-04-26 (America/New_York).
- `_aux/Universe_Index/service_inventory.md` :: service breadth confirmed.
- `_aux/Universe_Index/key_facts.md` :: slack channel C006 #operations is Blessing's home channel (91 msgs, second-busiest).
- `_aux/Fact_Ledger.json` :: 216 emails / 64 amounts / 154 dates / 132 personas atomized; every OE concrete value cross-grounded.
- `_aux/Hardness_Plan.md` :: 5 levers (L1/L2/L7/L8/L11) + 4 stump hypotheses (HIGH HIGH MED MED) + L29 escape-valve mitigation + answer-leak audit.
- `5_Prompt.txt` :: 380 words; 6 implicit writes; 5 services; AUDIT-cleared PASS (STRICT).
- `PersonaBrief.txt` :: Blessing Okafor (Relocation Coordinator); active threads include Emilia Cruz piano damage + walkup-assessment admission.

## V3 reference voice
- `QC_Tasks/V3_Tasks/Task11_6a2202b85b24c47c08dd2e6b/Oracle_Events.txt` :: opening-phrase patterns, numbered structure, discovery-step phrasing, final-paragraph summary style.
