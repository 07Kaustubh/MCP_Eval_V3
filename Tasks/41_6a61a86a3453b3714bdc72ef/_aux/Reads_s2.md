# Reads — S2 (Oracle Events) — Tasks/41_6a61a86a3453b3714bdc72ef

## Spec / eval / QC docs
- Evals_starpm/2_OE_Eval.md :: OE Completeness (5 = full critical path: discovery + dependency chains + write actions) and OE Accuracy (5 = tools/services/params/expected values all match universe); OE issues are NON-FAIL only; T9 act-vs-defer HARD GATE for write-action OEs; per-OE sign-off table is the enforcing mechanism.
- AGENTS.md :: hard rules (Opus 4.8 under test; per-task universe is the only SoT; no em-dashes; StarPM v4 density 40+ per model; StarPM param traps).
- Reference/OE_Format.md :: numbered prose, real tool names only, real param names (StarPM: Slack `message`, Gmail draft-only `body`, Linear `save_comment(issueId, body)`, Airtable camelCase baseId/tableId), discovery-then-writes, no em-dash.
- Reference/Sessions/S2.md :: phase procedure, councils, AUDIT auto-fire conditions, exit criteria.

## Tool catalog (SSOT for tool names + params)
- StarPM_Base_Universe/7_Server_Tools_Details.json :: verified every tool name used exists (search_customers, search_invoices, read_invoice, search_bills, list_bases, list_tables_for_base, search_records, list_records_for_table, update_records_for_table, list_issues, get_issue, save_comment, slack_search_public_and_private, slack_read_channel, slack_send_message, search_threads, get_thread, contacts_search_contacts). Confirmed param signatures: search_records(baseId, table, query), list_records_for_table(baseId, tableId, recordIds), update_records_for_table(baseId, tableId, records[{id,fields}]), slack_send_message(channel_id, message), create_draft(to, subject, body), save_comment(issueId, body), read_invoice(invoice_id), search_bills(query). Confirmed NO read_bill/get_bill (bills read via search_bills).

## Upstream task artifacts
- 5_Prompt.txt :: Patricia Nguyen closing Tanya Mitchell filing package; verify balance (net clean number) + eviction state + make-ready release; 4 writes (make-ready record, eviction-ticket note, make-ready channel Slack, owner email draft).
- _aux/Hardness_Plan.md :: 5 levers (L2 flagship structured-DB skip, L10 supersession, L1 latching, L11 net-vs-gross, L31 negative-directive omission); density ~50 Opus / ~43 Gemini.
- _aux/Reasoning/prompt_design.md :: S1 lever-to-sentence mapping; S1.5 persona reassignment Lisa->Patricia; two S2 carries (eviction-ticket note surface; stale validator date default).
- _aux/Fact_Ledger.json + _aux/Verification_s1.md :: atom surface + prior-phase cross-source check.

## Reference OE corpus / sibling task
- Tasks/40_6a614767cd5b60ad96902fb4/6_Oracle_Events.txt :: sibling StarPM Tanya Mitchell OE (Lisa version) - structural reference for voice/param usage; task 41 differs (owner-email recipient Linda Castillo not Brooke; no calendar reminder; net-$1,832 derivation centered; ESA accommodation EXCLUDED as out-of-scope for Patricia's rent/eviction lane).
