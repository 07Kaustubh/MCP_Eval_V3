# Council A — Grounding and Convention · S2 Oracle Events

**Task:** 40_6a614767cd5b60ad96902fb4 · **Universe:** starpm (V4) · **Deliverable:** 6_Oracle_Events.txt (19 OEs)
**Method:** independent Read/Grep of `_aux/Universe_Split/*` + `StarPM_Base_Universe/7_Server_Tools_Details.json`. Every value confirmed in the data, not taken from the OE's own assertions.
**(Report persisted by orchestrator; the explore sub-agent ran read-only and returned the report in its final message.)**

## [A1 — Grounding] every concrete value GROUNDED

Airtable structure: base `appPropertyOps` ("Property Operations"); tables `tblMakeReady` ("Make-Ready Turns", primary `fldUnit`) + `tblMaintenanceTickets` ("Maintenance Tickets", primary `fldTicketNumber`); fields `fldUnit/fldTurnStatus/fldNotes2/fldMoveOut/fldTargetReady/fldPriority/fldCompletionDate`; selects `selSched`=Scheduled, `selProg`=In Progress, `selReady`=Ready, `selHigh`=High. All grounded in airtable_bases/tables/fields.json.

8 Airtable records (all confirmed in airtable_records.json):
- reca8230a8fd9ff51 = "Sunset Ridge Unit 14", selSched, mod 2026-06-07 (identity anchor).
- recc83c05d889b354 = "Unit 14", selSched, fldMoveOut 2026-05-02, mod 2026-07-01 11:18:57; notes = JP coordination / "cannot begin until possession is formally returned".
- rec94e86a3007dd5e = "Rio Bend - Unit 14", selReady, "back to rent-ready" (decoy, different property).
- rec769c9f03f0b85f = "Las Palmas 4B", selSched, "payment plan agreement / active repayment" (stale).
- rec8005502043b755 = "Tanya Mitchell - Delinquency Escalation", selProg, "Payment Plan Breached - No Response" after June 23.
- rec91517a5acab558 = "Unit 14", selSched, "3-Day Notice served June 26, deadline June 29"; Brooke approved escalation.
- recc0ecc885e9645e = DLQ-2026-0601, selHigh, "Past Due - Grace Period Expired", $75 late fee.
- rec922b9a2d1b9451 = EVF-2026-014, selHigh, fldCompletionDate 2026-06-30, "Owner Approved - Ready to File", Linda Castillo.

Cross-service (all grounded): HubSpot ticket_8faab56c663352cfb8d61c994b2bae88 (tickets, OPEN, HIGH, owner owner_brooke_phillips -> Brooke Phillips); Gmail threads cfabf41121992633 (Tanya ESA request), 37a90450b4c2de2c (Sandra forwards to Lisa), 9f2b3cd66c907597 (Lisa: "approved, effective immediately"); Slack C003=#general (ts 1782673915 breach, 1782673930 3-day served, 1782881568 "filing complete, owner-approved, JP coordination underway", 1781018061 superseded payment commit), C004=#make-ready; QuickBooks customer proj-2e48c594aab7 (Tanya, tanya.mitchell@gmail.com), invoice DocNumber 7214 / id 283231782926 TotalAmt 8173.44 Balance 0.00 PrivateNote "remains delinquent with no cure received" (line 1979), bill QR-2026-0441 / id 232176553533 Balance 2132.00 (line 275), bill 2026-EV-047 / id 146128608253 Balance 185.00 (line 123); Linear OPS-32 ("Eviction Hearing - Mitchell, Harris Property", team_001, priority 1, state_OPS_2 In Progress), siblings OPS-38 (Todo) + OPS-54 (In Progress); calendar lisa.smith@starpm.com (primary, owner, America/Chicago); contacts Brooke Phillips (brooke.phillips@starpm.com, Apartment Property Supervisor) + Tanya Mitchell (tanya.mitchell@gmail.com, Tenant). Amounts 75.00 / 8173.44 / 2132.00 / 185.00 all grounded.

VERDICT A1: zero ungrounded claims.

## [A2 — Convention] PASS
Numbered-prose, discovery-first (OE 1-13) then writes (OE 14-18) then content synthesis (OE 19). No em-dash / en-dash (grep clean). Every tool name exists in the catalog; every parameter key real on the exact tool. StarPM traps correct: slack_send_message(channel_id, message); create_draft(to, subject, body) draft-only; save_comment(issueId, body); airtable camelCase baseId/tableId/records; bare catalog names except slack_/contacts_. OE 19 is a content-requirements synthesis (acceptable in V4 format, matches reference OE 22 pattern). Zero convention drift.

## [A3 — Narrative State] all CONSISTENT
possession NOT returned (recc83c05d889b354 notes + Slack 1782881568 "before the petition goes in"); turn held/Scheduled (selSched); plan breached (rec8005502043b755 + Slack 1782673915); active eviction (rec91517a5acab558 3-day notice + EVF-2026-014 + OPS-32); ESA approved on record (Gmail 9f2b3cd66c907597 "approved, effective immediately"); filing owner-approved but in JP coordination (EVF-2026-014 + Slack 1782881568). Zero contradictions.

## [A4 — Action-vs-Universe-Prescription] no divergence
The OE 14 hold (keep selSched, do NOT advance) is prescribed by recc83c05d889b354 notes. fldMoveOut=2026-05-02 correctly treated as a stale planning field, NOT possession-returned. The "Ready to File" (EVF-2026-014) and "mobilize if vacates by June 29" (rec91517a5acab558) records are superseded by the 2026-07-01 possession-hold record (temporal supersession). Lisa Smith (onsite PM) has authority for all 5 writes (grounded via her ESA handling + inspection records). No ACTION_DIVERGENCE, no AUTHORITY_GAP.

## [A11 — Solvability] no break
Full dependency chain from Hardness_Plan materialized: make-ready records, delinquency/eviction chain, HubSpot ESA ticket, Gmail approval, Slack breach/filing messages, QuickBooks customer+invoices, Linear OPS-32, Lisa's calendar, Brooke/Tanya contacts. Every source row present.

## Non-blocking notes
- HubSpot ESA ticket's associated contact contact_b30b8045f674569c9f15298ab9ce95d8 resolves to Maria Lopez (leasing agent who filed it), NOT Tanya. OE 10 lists it only as "associated contact" without misattributing to Tanya -> accurate.
- Property-name variance across services: Airtable "Sunset Ridge Unit 14" = QuickBooks "Sunridge Apartments" (bill 2026-EV-047) = Linear OPS-32 "Harris Property". Universe inconsistency; the OEs do not rely on the name matching, so not an OE error.

## VERDICT: GO
Zero ungrounded claims (A1), zero convention drift (A2), zero narrative-state contradictions (A3), zero unjustified action-divergence / authority-gap (A4), zero solvability breaks (A11).
