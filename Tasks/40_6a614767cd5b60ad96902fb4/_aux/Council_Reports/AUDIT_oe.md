# AUDIT — S2 Oracle Events (StarPM V4) — STRICT VETERAN SECOND OPINION

**Task:** Tasks/40_6a614767cd5b60ad96902fb4 · **Persona:** Lisa Smith (Onsite PM, p_002) · **Universe:** starpm (V4)
**Deliverable:** `6_Oracle_Events.txt` (19 OEs) · **Phase:** `--phase oe` · **Mode:** on-demand strict second opinion (required S2 exit gate)
**Density framework (correct):** StarPM V4 — design target avg **40+ tool calls PER MODEL** (Opus + Gemini separately), floor 15. The V3-family 50+ midpoint bar is NOT applied.

Read-only. Every value below was re-grounded independently against `_aux/Universe_Split/` and `StarPM_Base_Universe/7_Server_Tools_Details.json`. Council reports were NOT trusted on their word.

---

## VERDICT: REVISE

One [Minor] Completeness defect (fix-in-place at the OE, PROPAGATES TO S3) + one [Nit] wording tightening. Zero BLOCKER, zero REBUILD. OE Accuracy is genuinely 5/5; OE Completeness is 4/5 solely because of the make-ready write-target lock-in. All 5 hardness levers trace end-to-end; density projects ~48/model >= 40 = PASS; no tool/param defect; no answer-leakage.

- **[Minor] OE 14 (+ OE 2) — make-ready write-target lock-in. PROPAGATES TO S3 (not S1).**
  OE 14 writes the hold to `recc83c05d889b354` and states "Only Tanya Mitchell's Sunset Ridge record recc83c05d889b354 is updated." Verified: `recc83c05d889b354` fldUnit is the bare **"Unit 14"** (it does NOT itself name the property); the ONLY record whose fldUnit literally reads **"Sunset Ridge Unit 14"** is `reca8230a8fd9ff51` (selSched, same Tanya turn, older note). Both are the same Sunset Ridge Unit 14 turn for Tanya; the Rio Bend decoy `rec94e86a3007dd5e` is correctly excluded. Because a real agent has a legitimate path to land the hold-update on `reca8230a8fd9ff51` (the record that unambiguously names the property — arguably the safer disambiguation choice), the OE must not lock the grader to a single rec id.
  **Exact fix (OE 14):** replace "Only Tanya Mitchell's Sunset Ridge record recc83c05d889b354 is updated, not the Rio Bend Unit 14 decoy." with: "The hold-update may validly target either recc83c05d889b354 (latest-modified, carries the current possession-hold note) or reca8230a8fd9ff51 (fldUnit literally 'Sunset Ridge Unit 14'); both are the same Tanya Sunset Ridge Unit 14 turn. The Rio Bend Unit 14 record rec94e86a3007dd5e must never be the target. Grade on the hold CONTENT plus correct-tenant/correct-property record, not the exact rec id."
  **PROPAGATE TO S3:** the Airtable-write rubric must accept EITHER recc83c05d889b354 OR reca8230a8fd9ff51 (and must still fail rec94e86a3007dd5e). No S1 change — the prompt ("Keep everything tied to Tanya Mitchell's unit specifically") is satisfied by both records and does not create the ambiguity.

- **[Nit] OE 9 — invoice-gloss precision (fix-in-place, does not change score).**
  OE 9 says invoice 7214 "shows TotalAmt 8173.44 with Balance 0.00 because a payment of 8173.44 is applied." Verified: the invoice nets to Balance 0.00 via a positive line "Partial payment plan credit applied to account" of 5885.94 (lines sum 1125 + 975 + 187.5 + 5885.94 = 8173.44); there is no discrete 8173.44 payment atom. The operative point (zero balance must NOT be read as resolved; PrivateNote states account "remains delinquent with no cure received") is exact and correct. Recommend tightening the gloss to: "shows TotalAmt 8173.44 with Balance 0.00 (the invoice nets to zero), yet its PrivateNote states the Mitchell account remains delinquent with no cure received, so the zero balance must NOT be read as resolved." Kept as a Nit (not an Accuracy fail) because Balance 0.00 legitimately implies the charge was satisfied and no cited exact value is wrong.

---

## OE Completeness: 4 / 5   ·   OE Accuracy: 5 / 5

Accuracy 5/5: every tool name, parameter, record id, status, amount, date, channel id, thread id, ticket id, OPS-N id, calendarId and email cited in the 19 OEs matches the Universe_Split exactly (per-atom evidence below). Completeness 4/5: the single write-target lock-in above is the only gap; it is fix-in-place.

---

## Per-OE strict verification table

| OE | Core claims | Ground-truth check | Verdict |
|---|---|---|---|
| 1 | base appPropertyOps "Property Operations"; tblMakeReady (primary fldUnit); tblMaintenanceTickets (primary fldTicketNumber) | bases: id appPropertyOps name "Property Operations"; tables + fldUnit/fldTicketNumber primaries confirmed. list_bases()/list_tables_for_base(baseId) params correct | PASS |
| 2 | reca8230a8fd9ff51 "Sunset Ridge Unit 14" selSched lastmod 2026-06-07; recc83c05d889b354 "Unit 14" selSched lastmod 2026-07-01 11:18:57; rec94e86a3007dd5e "Rio Bend - Unit 14" selReady = decoy; search_records uses `table`, list uses `tableId` | All fldUnit/status/timestamps exact. search_records params baseId/table/query correct; list_records_for_table baseId/tableId correct | PASS (see Minor: reca8230a8fd9ff51 is co-valid write target) |
| 3 | recc83c05d889b354 selSched; fldNotes2 = JP-coordination + "cannot begin until possession formally returned"; fldMoveOut/fldTargetReady 2026-05-02 are stale | Note verbatim match; both date fields = 2026-05-02; list_records_for_table recordIds param valid | PASS |
| 4 | rec769c9f03f0b85f "Las Palmas 4B" stale "plan compliance"; rec8005502043b755 selProg "Payment Plan Breached - No Response" post June 23; rec91517a5acab558 "3-Day Notice ... June 26 ... deadline June 29" | All three notes + statuses + labels exact | PASS |
| 5 | DLQ-2026-0601 (recc0ecc885e9645e) selHigh "Past Due - Grace Period Expired" $75 late fee; EVF-2026-014 (rec922b9a2d1b9451) fldCompletionDate 2026-06-30 "Owner Approved - Ready to File" by Linda Castillo | Exact; $75 in DLQ desc; EVF authorized by Linda Castillo, package staged | PASS |
| 6 | C003 #general: Patricia 1782673915 (breach/recommend 3-day); 1782673930 (3-day served/ticket open/June 29 reminder); Brooke 1782881568 (filing complete owner-approved/JP coordination) | Channel C003=#general; ts, authors, and text all exact | PASS |
| 7 | Patricia 1781018061.000002 "Tanya Mitchell, Sunset Ridge Unit 14 ... committed to a payment date" (superseded) | Exact text + author | PASS |
| 8 | customer proj-2e48c594aab7 "Tanya Mitchell" tanya.mitchell@gmail.com; no aggregate balance on object | DisplayName/email exact; Balance=None (null) confirmed | PASS |
| 9 | inv 7214 (283231782926) TotalAmt 8173.44 Balance 0.00 PrivateNote delinquent; bill QR-2026-0441 (232176553533) Balance 2132.00 "Tanya Mitchell, Unit 14"; bill 2026-EV-047 (146128608253) Balance 185.00 eviction-package | All amounts/ids/DocNumbers/PrivateNote exact. QR-2026-0441 VendorRef="Alamo HVAC Services" (uncited quirk) but all 4 line descriptions read "Tanya Mitchell, Unit 14" rent arrears/June rent/late fees — OE characterization grounded, not misleading | PASS (invoice-gloss = Nit) |
| 10 | ticket_8faab56c...bae88 "Reasonable Accommodation Request - ESA (Tanya Mitchell)" OPEN HIGH owner owner_brooke_phillips assoc contact_b30b8045... | Ticket status/priority/owner/subject/contact_id exact. contact_b30b8045 = Maria Lopez (maria.lopez@starpm.com, Weekend Leasing Agent, internal). OE gives opaque id + calls ticket "for this tenant" (Tanya via subject line) — does NOT misattribute the contact to Tanya | PASS |
| 11 | thread cfabf41121992633 (Tanya's ESA request, cat); 37a90450b4c2de2c (Sandra Allen -> Lisa forward); 9f2b3cd66c907597 (Lisa notifies Tanya "approved, effective immediately" + conditions) | Snippets confirm: Tanya->Sandra request (cat); "Hi Lisa ... forwarding"; "Hi Tanya ... approved, effective immediately ... conditions". Approver = Lisa Smith (persona) | PASS |
| 12 | OPS-32 "Eviction Hearing - Mitchell, Harris Property" In Progress prio 1 Urgent; OPS-38 Todo; OPS-54 In Progress; team_001 | Titles/states exact; priority 1; team_001=Operations. state map: state_OPS_2=In Progress, _1=Todo | PASS |
| 13 | Brooke Phillips brooke.phillips@starpm.com Apartment Property Supervisor; Tanya Mitchell tanya.mitchell@gmail.com | contacts confirm both name/email/title; contacts_search_contacts(query) correct | PASS |
| 14 | update_records_for_table(baseId appPropertyOps, tableId tblMakeReady, records[recc83c05d889b354]); keep selSched; update fldNotes2 hold; do NOT advance to selProg/selReady; exclude Rio Bend | Params baseId/tableId/records all required+correct; status-hold logic correct; Rio Bend exclusion correct | REVISE (Minor: also bless reca8230a8fd9ff51; PROPAGATE TO S3) |
| 15 | slack_send_message(channel_id C004, message ...); C004=#make-ready; text param is message | C004=#make-ready confirmed; slack_send_message params channel_id + message exact (NOT payload/text) | PASS |
| 16 | create_draft(to[brooke.phillips@starpm.com], subject, body); draft-only, no send; cites QR-2026-0441 2132.00 + inv 7214 books-vs-note conflict + EVF-2026-014 + ESA + Sunset/Rio disambiguation | create_draft params to/subject/body correct (body NOT content); no send tool exists; all cited values grounded | PASS |
| 17 | create_event(summary, startTime 2026-07-06T09:00, endTime 2026-07-06T09:30, calendarId lisa.smith@starpm.com); "early next week" from 2026-07-01 America/Chicago | 2026-07-01=Wed; 2026-07-06=Mon (fact ledger); calendar lisa.smith@starpm.com exists (tz America/Chicago); params summary/startTime/endTime required + calendarId optional correct; "not the literal string primary" is a valid trap note | PASS |
| 18 | save_comment(issueId "OPS-32", body ...); issueId is OPS-N not uuid | save_comment params issueId/body exist; linear_comments store issue_id in OPS-N form (e.g. "OPS-34") -> OPS-32 input form CONFIRMED correct | PASS |
| 19 | content-requirements consolidation for OE 15 + OE 16 (5 facts) | All 5 facts grounded; non-tool consolidation OE = grading aid, acceptable by design | PASS |

---

## Per-atom evidence table (contested atoms — v18 required for 5/5)

| Atom asserted (OE) | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| inv 7214 TotalAmt 8173.44 / Balance 0.00 / delinquent (OE9,16) | quickbooks_entities id=283231782926 | TotalAmt 8173.44, Balance 0.0, PrivateNote "...remains delinquent with no cure received", CustomerRef Tanya Mitchell proj-2e48c594aab7 | PASS |
| bill QR-2026-0441 Balance 2132.00 = Tanya rent arrears (OE9,16) | id=232176553533 | Balance 2132.0, lines "...arrears/June rent/late fees - Tanya Mitchell, Unit 14"; VendorRef "Alamo HVAC Services" (uncited) | PASS |
| bill 2026-EV-047 Balance 185.00 = eviction filing prep (OE9) | id=146128608253 | Balance 185.0, line "Eviction filing package preparation ... Tanya Mitchell" | PASS |
| $75 late fee (OE5) | airtable recc0ecc885e9645e | "...$75 late fee applied per lease terms" DLQ-2026-0601 | PASS |
| recc83c05d889b354 = "Unit 14" + possession-hold (OE3,14) | airtable rec | fldUnit "Unit 14"; "cannot begin until ... possession is formally returned"; selSched; lastmod 2026-07-01 11:18:57 | PASS |
| reca8230a8fd9ff51 = "Sunset Ridge Unit 14" (identity anchor / co-target) (OE2) | airtable rec | fldUnit "Sunset Ridge Unit 14"; selSched; note stale (payment timeline) | PASS (must be blessed as co-valid write target) |
| rec94e86a3007dd5e = Rio Bend decoy rent-ready (OE2,14) | airtable rec | fldUnit "Rio Bend - Unit 14"; selReady; "back to rent-ready condition" | PASS (correctly excluded) |
| ESA ticket OPEN + owner brooke + assoc Maria Lopez (OE10) | hubspot ticket_8faab56c...bae88 | status OPEN, priority HIGH, hubspot_owner_id owner_brooke_phillips, contact_id contact_b30b8045... = Maria Lopez (internal) | PASS (no misattribution to Tanya) |
| gmail 9f2b3cd66c907597 = "approved, effective immediately" by Lisa (OE11) | gmail thread/messages | "Hi Tanya ... approved, effective immediately ... conditions"; sender Lisa Smith | PASS |
| OPS-32 In Progress prio1 team_001 (OE12,18) | linear issue | title "Eviction Hearing - Mitchell, Harris Property"; state_OPS_2 In Progress; priority 1; team_001 Operations | PASS |
| C003 #general / C004 #make-ready (OE6,15) | slack channels | C003 #general; C004 #make-ready | PASS |
| early-next-week -> 2026-07-06 (OE17) | fact ledger dates | 2026-07-01 Wed; 2026-07-06 Monday | PASS |
| calendarId lisa.smith@starpm.com (OE17) | gcalendar calendars | id lisa.smith@starpm.com, tz America/Chicago | PASS |

---

## Tool / parameter verification (5 write actions + traps)

| OE | Tool | Params asserted | Catalog truth | Verdict |
|---|---|---|---|---|
| 14 | update_records_for_table | baseId, tableId, records | baseId/tableId/records all required; camelCase | PASS |
| 15 | slack_send_message | channel_id, message | channel_id + message required (NOT payload/text) | PASS |
| 16 | create_draft | to[], subject, body | to/subject/body optional; body is plain text (NOT content); no send tool | PASS |
| 17 | create_event | summary, startTime, endTime, calendarId | summary/startTime/endTime required; calendarId optional | PASS |
| 18 | save_comment | issueId, body | issueId/body params exist; OPS-N input form confirmed via linear_comments.issue_id="OPS-34" | PASS |

Read-side param traps also verified: OE2 search_records uses `table` (correct) while list_records_for_table uses `tableId` (correct); OE10 get_crm_objects uses object_type + object_ids (both required); OE12 list_issues supports `team` filter. No tool-name/em-dash violations (tool names are permitted in OE bodies).

---

## Lens summary

- **Lens 1 (strict QC scoring):** OE Accuracy 5/5; OE Completeness 4/5 (make-ready write-target lock-in). -> REVISE.
- **Lens 2 (answer-leakage):** PASS. The task answer is a multi-source synthesis (hold turn / active eviction / surface ESA / disambiguate Unit 14). No single tool call reveals it; derived figures (2132.00, 8173.44/0.00) require cross-source reads (airtable + slack + hubspot + quickbooks). The agent-visible prompt carries the WRONG "cleared" framing and states none of the conclusions. No leakage.
- **Lens 3 (hardness end-to-end):** PASS. S1 possession-hold -> OE3/14/15/16/19; S2 supersession/latching -> OE4/6/7/9; S3 HubSpot ESA skip -> OE10/11; S4 Unit 14 near-miss -> OE2/14; S5 authority/ready-to-file anchor -> OE5/6 (genuine records, not planted false dismissal). All 5 exercised with cited atoms.
- **Lens 4 (density, StarPM 40+/model — correct bar):** PASS. Hardness plan projects midpoint ~48; Council B Opus ~46 / Gemini ~43; conservative 4-lever floor 44.5. 19 OEs across 8 services sustain 40+/model. V3 50+ bar deliberately NOT applied.
- **Lens 5 (adversarial veteran):** One seam — the OE14 rec-id lock-in (folded into Lens 1). Source-of-record landmine handled correctly (Airtable authoritative write in OE14; Linear treated as secondary mirror in OE18). No entity drift, no single-channel lock-in beyond the noted rec-id case, no over-specification of exact figures near IDs.
- **Lens 6 / Lens 9:** RETIRED (v18) — subsumed into Lens 1 per-atom evidence + Lens 5.
- **Lens 7 (anti-rationalization):** Applied. The reca8230a8fd9ff51 co-target was NOT excused as "the newest record is obviously the one" — promoted to a Completeness finding because a valid alternate write path exists that a rec-id-locked rubric would fail. The QR-2026-0441 "Alamo HVAC" VendorRef and the Maria-Lopez associated contact were checked as potential misattributions and cleared (OE cites neither as Tanya). The OE9 invoice gloss kept as a Nit with explicit accounting reasoning, not talked away.
- **Lens 8 (regression anchors):** NOT executed this pass — out of scope for an OE-CONTENT audit (the suite tests validator-regex integrity, not OE facts); `validate.py --phase oe` was run by the S2 councils and passed. Flagged for transparency; does not affect the OE-content verdict.

---

## Bottom line

The OE set is factually airtight (Accuracy 5/5) and every hardness lever, tool, parameter, and derived figure is grounded. It falls one point short on Completeness for a single fix-in-place reason: OE 14 locks the make-ready write to `recc83c05d889b354` when `reca8230a8fd9ff51` (the record literally named "Sunset Ridge Unit 14") is an equally-valid target for the same Tanya turn. Add the co-target clause to OE 14 and flag PROPAGATE TO S3 so the Airtable-write rubric accepts either id (still failing the Rio Bend decoy). Apply the OE 9 wording nit. Re-run the S2 validator + councils on the revised OE; no S1 change required.
