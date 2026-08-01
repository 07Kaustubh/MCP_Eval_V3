# S2 — Reads log (Task 45, StarPM V4)

v11 E2 compliance gate. One line per spec doc / reference card / eval read.

- Reference/Sessions/S2.md :: S2 runbook — procedure, exit criteria, AUDIT auto-fire conditions, StarPM param traps.
- Reference/OE_Format.md :: OE structure, hard rules (no em-dash, real tool/param names), OE→rubric map, StarPM traps (slack `message`, gmail draft-only `body`, linear `team`).
- Docs_starpm/9_Common_Error.md :: Part 2 OE errors — no skipping discovery steps; describe tool-use not findings.
- Tasks/45_.../5_Prompt.txt :: the S1-cleared prompt (Jaime QC pass on Mesa Vista 4C, sign-off OR kick-back).
- _aux/Hardness_Plan.md :: levers L2/L1+L10/L31 + L7/L9; anchor recbd087a4abd605b (selProg, current turn); 4-record census; 5-6 distinct writes mandate; per-model density 40+.
- _aux/Universe.txt :: starpm.
- StarPM_Base_Universe/7_Server_Tools_Details.json :: verified tool signatures — airtable update_records_for_table/create_record_comment, gcalendar list_events/get_event, gmail create_draft (to[],subject,body draft-only), linear save_issue(team)/save_comment(issueId,body), quickbooks get_aged_payables/get-bill, slack_send_message(channel_id,message).
- Reference/OE_Convention_Inventory.json :: OE opening-phrase + discovery/write phrasing patterns, conclude-clause form, anti-patterns (no structured JSON, no tool-name-without-params).
- Reference/Council_Protocol.md :: Council A (9 persp) + Council B (8 persp, S2: B1/B2/B3/B4/B6/B8/B9) structure + verdict criteria + sub-dim scoring scheme.
- _aux/Universe_Split/ (airtable records/fields/tables, quickbooks entities, gcalendar events, slack channels/messages/users, contacts, linear teams/states/users) :: grounded every OE id/amount/date/email/channel/tool-target.
