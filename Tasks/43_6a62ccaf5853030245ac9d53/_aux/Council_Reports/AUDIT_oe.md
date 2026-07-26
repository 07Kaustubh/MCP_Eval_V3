# AUDIT (S2 auto-fire, --phase oe) - Veteran QC Re-Verification

**Task:** `Tasks/43_6a62ccaf5853030245ac9d53` | **Universe:** StarPM V4 (dual-model) | **today** 2026-07-01 America/Chicago
**Deliverable audited:** `6_Oracle_Events.txt` (28 OE steps, 24 read + 4 write). READ-ONLY on the deliverable.
**Trigger:** Track F condition (d) - the OE list was revised after both councils returned round-2 GO.
**Prior state:** Council A GO (round 2), Council B GO (round 2), both scoring OE Completeness 5/5 and OE Accuracy 5/5.

This audit re-derived every atom from `_aux/Universe_Split/` with `python3`, and additionally used real
harness output from the three prior StarPM V4 tasks (39/40/41) to settle retrievability and page-size
questions empirically rather than by assumption. That empirical step is what produced the two findings
both councils missed.

---

## LENS 1 - Strict QC scoring (Oracle Event dimension, `Docs_starpm/7_QC_Spec_Doc1.json`)

```
SUB-DIM OE Completeness -> SCORE 4/5 -> REASON The critical path, the dependency chain and all four
  write actions are covered with tools and key parameters, but three discovery gaps survive: (a) OE 22
  enumerates a sixth C004 message that none of its own three stated queries can return, so the step's
  discovery path is incomplete for the single record OE 19 leans on hardest; (b) OE 10's decoy inventory
  omits invoice 310712648304 (2547, 385.00, Linda Castillo, "Pass-through ... deep-clean"), the closest
  near-miss to the 387.00 line, and OE 21's wrong-answer catalog therefore omits the 1810.00 that a
  385/387 substitution produces; (c) the 1140.00 mirror decoy (bill 173322471681) is undisclosed while
  OE 16 disambiguates only the 1340.00 side.
  WHAT THE PRIOR COUNCIL MISSED: both councils verified that ts 1779501872.000004 EXISTS, is attributed
  to Jaime Salinas (U2CD1BC03B2) and is quoted verbatim, then signed the step off as "EXACT" (Council B
  round-2 Issue 2) and "RESOLVED" (Council A Major-3). Neither asked whether the step's own query
  parameters retrieve it. Council A even noted at its line 332 that `slack_read_channel(C004)` returns
  it, which is true, and then let that stand as clearance for OE 22's search as well. Same pattern on
  OE 10: both verified the listed decoys exist; neither checked that the listed queries return them, nor
  swept for a closer unlisted decoy.

SUB-DIM OE Accuracy -> SCORE 4/5 -> REASON Every count, id, DocNumber, amount, date, email, field id and
  select-option id in the OE is byte-exact against the universe (per-atom table below, 71 rows, zero
  empty cells, zero NOT FOUND), and all 25 referenced tools and every parameter name check out against
  `StarPM_Base_Universe/7_Server_Tools_Details.json`. Four expected-data / attribution defects remain:
  (a) OE 22's stated queries cannot produce the stated six-message result (empirically demonstrated);
  (b) OE 24 attributes to the prompt a foreclosure the prompt does not contain ("do not raise a credit
  memo ... the prompt forecloses it" - the prompt forecloses "a second bill") and supports it with a
  rationale that is wrong for the instrument named (a credit memo reduces a receivable, it does not
  "double-bill"); (c) OE 13's "No other bill or receivable in the ledger touches 4C" contradicts OE 10
  and OE 11, since invoice 445653930748 is a receivable that touches 4C; (d) OE 15's absolute "The
  1340.00 for this scope exists nowhere but on this bill ... and not in Slack" is true of Slack (0 hits,
  verified) but the enumeration omits Gmail, which carries two "$1,340" strings including one Carlos
  authored.
  WHAT THE PRIOR COUNCIL MISSED: Council B treated OE 24's credit-memo clause as a strengthening
  ("The negative guard strengthened ... closing round-1 alt-path D explicitly") without testing it
  against the prompt sentence, which is the exact Learnings L30 / 2026-07-24 item-5 defect class (a
  rubric grounded on OE language the prompt does not support). Council A logged the OE 15 family as
  Min-5 and accepted the partial fix without re-sweeping Gmail. OE 13's internal contradiction appears
  in neither report.
```

**Both sub-dims land at 4 under the strictest reading. 4 is a soft fail. Verdict is REVISE.**

Every finding is fix-in-place in `6_Oracle_Events.txt`. Nothing requires a re-derivation of the spine,
and nothing requires an S1 re-run (see the pivotal-question adjudication below).

### StarPM landmine checks

| Landmine | Status |
|---|---|
| Near-duplicate decoy records | **PARTIAL.** The 10-bill 1340.00 cluster and the twin 85.00 are disclosed exhaustively. Three further near-duplicates are not: invoice 310712648304 (385.00 pass-through deep-clean, same owner, same TxnDate/DueDate), bill 173322471681 (1140.00 with an "expected 1,140 / billed 1,380" note and the same AccountRef 63 as the 4C repaint), and the "Tommy Reyes" string on decoy 340207319849. See M3, m5, m7. |
| Cross-property unit ambiguity | **CLEAR.** OE 3 names Mesa Vista 107A, 207A and 310C as out of scope; verified 6 sibling rows across exactly those 3 units. OE 16 correctly assigns 686894936323 to "412 Garfield Ave, Unit 3C" (byte-exact, comma included). OE 6 correctly says the broader "Mesa Vista" query also pulls rec860db6b493af1e5b (MT-2026-1326, pool pump). |
| Airtable-is-source-of-record, Linear secondary | **CLEAR.** `airtable.airtable_tables.json` tblMaintenanceTickets description reads "System of record for maintenance work orders; Linear is secondary." The OE writes the make-ready state to Airtable (OE 25) and writes nothing to Linear. `_aux/Reasoning/OE_solvability.md` records the reasoning. No Linear step is missing. |
| This task's twin-85.00 near-miss | **ARMED and CORRECTLY DECIDED.** See the pivotal-question section. |

---

## Per-atom evidence table (MANDATORY)

All rows re-derived from `Tasks/43_6a62ccaf5853030245ac9d53/_aux/Universe_Split/` by parsing `row_data`.
Short forms: `qb` = `quickbooks.quickbooks_entities.json`, `at` = `airtable.airtable_records.json`,
`atf` = `airtable.airtable_fields.json`, `sl` = `slack.slack_messages.json`,
`gm` = `gmail.gmail_messages.json`, `gt` = `gmail.gmail_threads.json`, `ct` = `contacts.contacts.json`.

### The four 4C bills

| Atom asserted | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| Bill 195089456477 TotalAmt 387.00 | `qb` id == 195089456477 | `"TotalAmt": 387.0` | EXACT |
| Bill 195089456477 Balance 387.00 | same | `"Balance": 387.0` | EXACT (OE 14 does not state it; consistent) |
| Bill 195089456477 DocNumber 2026-SC-4C | same | `"DocNumber": "2026-SC-4C"` | EXACT |
| Bill 195089456477 VendorRef Sunshine Cleaning proj-d016366b403c | same | `"VendorRef": {"name": "Sunshine Cleaning", "value": "proj-d016366b403c"}` | EXACT |
| Bill 195089456477 AccountRef Contract Labor 62 | same, Line[0].AccountBasedExpenseLineDetail | `"AccountRef": {"name": "Contract Labor", "value": "62"}` | EXACT |
| Bill 195089456477 PrivateNote quoted in full (OE 14) | same | `"Carmen's invoice received by email and entered into QB by Carlos. Covers make-ready deep clean for Unit 4C turnover. Owner pass-through - paired receivable invoice to be issued to Pete Donovan for same scope and unit."` | EXACT, all four sentences |
| Bill 696089964235 TotalAmt 1340.00 | `qb` id == 696089964235 | `"TotalAmt": 1340.0` | EXACT |
| Bill 696089964235 Balance 1340.00 | same | `"Balance": 1340.0` | EXACT |
| Bill 696089964235 DocNumber PD-2026-09 | same | `"DocNumber": "PD-2026-09"` | EXACT |
| Bill 696089964235 VendorRef Permian Make-Ready Crew 204 | same | `"VendorRef": {"name": "Permian Make-Ready Crew", "value": "204"}` | EXACT |
| Bill 696089964235 line description (OE 15) | same, Line[0].Description | `"Interior repaint, full unit - Mesa Vista Apartments Unit 4C; walls, ceilings, and trim; labor and materials included per agreed scope"` | EXACT |
| Bill 696089964235 AccountRef 63 (asserted in OE 19 G4) | same | `"AccountRef": {"name": "Management Fee Income", "value": "63"}` | EXACT |
| Bill 696089964235 PrivateNote "came from Pete Donovan on completion", pass-through expected | same | `"Vendor invoice received via email from Pete Donovan upon job completion; entered as AP bill against Mesa Vista 4C make-ready turnover. Coordinate with owner billing - pass-through to property owner expected. ..."` | EXACT (paraphrase faithful) |
| Bill 546359391323 TotalAmt 85.00 | `qb` id == 546359391323 | `"TotalAmt": 85.0` | EXACT |
| Bill 546359391323 Balance 85.00 | same | `"Balance": 85.0` | EXACT |
| Bill 546359391323 DocNumber 2026-519 | same | `"DocNumber": "2026-519"` | EXACT |
| Bill 546359391323 VendorRef Permian 204 | same | `"VendorRef": {"name": "Permian Make-Ready Crew", "value": "204"}` | EXACT |
| Bill 546359391323 AccountRef Owner Reserve (Trust) 64 | same | `"AccountRef": {"name": "Owner Reserve (Trust)", "value": "64"}` | EXACT |
| Account 64 is a trust bank account (OE 19 G4 gloss) | `qb` id == 64 | `{"Name": "Owner Reserve (Trust)", "AccountType": "Bank", "AccountSubType": "TrustAccounts", "CurrentBalance": 70624.57}` | EXACT; gloss is understated, not overstated |
| Bill 546359391323 line description | same, Line[0] | `"Bedroom closet trim paint touch-up, Mesa Vista Unit 4C - same-day repair following final QC walkthrough"` | EXACT |
| Bill 546359391323 PrivateNote quoted in full (OE 17) | same | `"Internal labor charge for Tony Reyes touch-up on Mesa Vista 4C closet trim. Flagged during Jaime Salinas's QC inspection; completed same day. Routed and logged by Carlos Mendez. Pass-through to owner - pair with corresponding AR invoice to Pete Donovan's owner account for 4C make-ready close-out."` | EXACT, all four sentences, opening phrase included |
| Bill 991582431419 TotalAmt 85.00 | `qb` id == 991582431419 | `"TotalAmt": 85.0` | EXACT |
| Bill 991582431419 Balance 85.00 | same | `"Balance": 85.0` | EXACT |
| Bill 991582431419 DocNumber 2026-481-566 | same | `"DocNumber": "2026-481-566"` | EXACT |
| Bill 991582431419 VendorRef Alamo HVAC Services 200 | same | `"VendorRef": {"name": "Alamo HVAC Services", "value": "200"}` | EXACT |
| Bill 991582431419 AccountRef Supplies 61 | same | `"AccountRef": {"name": "Supplies", "value": "61"}` | EXACT |
| Bill 991582431419 line description "Unit condition inspection and punch list documentation - Mesa Vista Unit 4C, vacated turnover" | same | `"Unit condition inspection and punch list documentation - Mesa Vista Unit 4C, vacated turnover: deep cleaning scope, full interior repaint, kitchen faucet leak, bathroom GFCI fault, drywall patching at entry noted and recorded to shared drive."` | EXACT (OE quotes the leading clause) |
| Bill 991582431419 PrivateNote "Internal labor charge for Carlos Mendez's make-ready walk", punch list "will drive subsequent vendor bills and owner pass-through invoices" | same | `"Internal labor charge for Carlos Mendez's make-ready walk of Mesa Vista 4C. ... Punch list items will drive subsequent vendor bills and owner pass-through invoices as repair scopes are confirmed and scheduled. ..."` | EXACT |
| "Internal labor charge for" appears on ONLY these two records in the whole ledger (OE 19 G1) | `qb` all 625 entities, substring scan | 2 hits: 546359391323, 991582431419 | EXACT |

### Invoice 445653930748

| Atom asserted | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| Line Id 1 Amount 387.00, deep-clean description | `qb` id == 445653930748, Line[0] | `{"Id":"1","Amount":387.0,"Description":"Post-move-out deep clean - Mesa Vista Unit 4C (Sunshine Cleaning, vendor pass-through)"}` | EXACT |
| Line Id 2 Amount 1140.00, repaint description | Line[1] | `{"Id":"2","Amount":1140.0,"Description":"Full interior repaint - Mesa Vista Unit 4C (Pete Donovan Painting, vendor pass-through)"}` | EXACT |
| Line Id 3 Amount 95.00, closet-trim description | Line[2] | `{"Id":"3","Amount":95.0,"Description":"Paint touch-up, bedroom closet trim - Mesa Vista Unit 4C (QC correction, vendor pass-through)"}` | EXACT |
| TotalAmt 1622.00 / Balance 1622.00 | same | `"TotalAmt": 1622.0, "Balance": 1622.0` | EXACT |
| sync_token "0" (needed by OE 24) | same | `"sync_token": "0"` | EXACT |
| DocNumber 2026-534, TxnDate 2026-05-01, DueDate 2026-05-31 | same | `"DocNumber":"2026-534","TxnDate":"2026-05-01","DueDate":"2026-05-31"` | EXACT |
| CustomerRef Linda Castillo proj-4ae920b7c9e8 | same | `"CustomerRef": {"name":"Linda Castillo","value":"proj-4ae920b7c9e8"}` | EXACT |
| PrivateNote asserts all work complete per QC walkthrough | same | `"... All work confirmed complete per QC walkthrough."` | EXACT |
| CustomerMemo recites the same three scopes to Linda | same | `"Linda - this invoice consolidates the vendor costs billed through for the completed make-ready at Mesa Vista Unit 4C: post-move-out deep cleaning and full interior repaint, including the QC-flagged closet trim correction. ..."` | EXACT |
| No DocNumber 2026-537 exists (OE 7, OE 10) | `qb` DocNumber == "2026-537" | 0 hits; also ABSENT from `Fact_Ledger.ids.invoice` (all 20 other cited DocNumbers PRESENT) | EXACT |
| No payment applied to 445653930748 (OE 12) | `qb` payments, LinkedTxn scan | 0 hits | EXACT |
| Only Linda payment 931951074454 for 510.00 links to 247748966591 (OE 12) | `qb` payments, CustomerRef == Linda Castillo | 1 payment: `931951074454, TotalAmt 510.0, LinkedTxn [{"TxnId":"247748966591","TxnType":"Invoice"}]`; 247748966591 DocNumber INV-2026-0214 | EXACT |

### Airtable

| Atom asserted | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| recc8534b3fd13954 fldTurnStatus selReady | `at` id == recc8534b3fd13954 | `"fldTurnStatus": "selReady"` | EXACT |
| recc8534b3fd13954 fldMoveOut 2026-06-01, fldTargetReady 2026-06-14 | same | `"fldMoveOut":"2026-06-01","fldTargetReady":"2026-06-14"` | EXACT |
| recc8534b3fd13954 last modified 2026-05-29 14:26:59 | same | `"last_modified_time": "2026-05-29 14:26:59.557207"` | EXACT |
| recc8534b3fd13954 fldNotes2 content (Jaime QC, trim flagged, routed to Tony Reyes, resolved same day, confirmed ready) | same | `"QC walkthrough completed by Jaime Salinas - bedroom closet trim flagged for paint touch-up. Touch-up routed to Tony Reyes and resolved same day. Unit confirmed ready for leasing."` | EXACT |
| recbd087a4abd605b fldTurnStatus selProg | `at` id == recbd087a4abd605b | `"fldTurnStatus": "selProg"` | EXACT |
| recbd087a4abd605b fldMoveOut 2026-06-15, fldTargetReady 2026-06-30 | same | `"fldMoveOut":"2026-06-15","fldTargetReady":"2026-06-30"` | EXACT |
| recbd087a4abd605b last modified 2026-05-22 21:14:34 | same | `"last_modified_time": "2026-05-22 21:14:34.331831"` | EXACT |
| recbd087a4abd605b fldNotes2 (faucet cartridge, GFCI, drywall done in house; deep clean and repaint still tracking) | same | `"Internal punch list work underway. Tony has completed the kitchen faucet cartridge replacement, swapped the bathroom GFCI outlet, and patched the drywall. ... Deep clean and interior repaint still tracking on their respective schedules. ..."` | EXACT |
| Date fields invert against modification order (OE 3) | both rows | stale row (mod 05-22) carries the LATER 06-15 / 06-30; live row (mod 05-29) carries 06-01 / 06-14 | EXACT |
| exactly TWO tblMakeReady rows match "Mesa Vista 4C" | `at` table_id == tblMakeReady, substring "4C" | 2 rows: recbd087a4abd605b, recc8534b3fd13954 (case-insensitive scan also returns 2) | EXACT |
| sibling units 107A, 207A, 310C exist | same table, "Mesa Vista" | 6 rows across 3 units: 107A x2, 207A x3, 310C x1 | EXACT |
| tblMaintenanceTickets query "4C" returns exactly two records | `at` table_id == tblMaintenanceTickets, "4C" | 2 rows: rec12969a3fdb0852, reca424761ae15355 | EXACT |
| query "Mesa Vista 4C" returns only the completion record | same, "Mesa Vista 4C" | 1 row: reca424761ae15355 | EXACT |
| query "Mesa Vista" also pulls rec860db6b493af1e5b (MT-2026-1326) | same, "Mesa Vista" | 3 rows incl. rec860db6b493af1e5b `"Mesa Vista community pool closed ..."` | EXACT |
| intake text reads "unit 4C at Mesa Vista" | rec12969a3fdb0852 | `"Make-ready turn opened for unit 4C at Mesa Vista following previous tenant's vacate. ..."` | EXACT |
| reca424761ae15355 fldTicketNumber MR-4C-2026-08, fldPriority selHigh, fldCompletionDate 2026-05-01 | `at` id == reca424761ae15355 | `"fldTicketNumber":"MR-4C-2026-08","fldPriority":"selHigh","fldCompletionDate":"2026-05-01"` | EXACT |
| reca424761ae15355 states all 4C work complete, Jaime QC addressed trim, passed re-inspection, market-ready | same | `"All make-ready work at Mesa Vista 4C is complete. ... QC walkthrough by Jaime addressed the bedroom closet trim; touch-up passed re-inspection. Unit status updated to market-ready ..."` | EXACT |
| rec12969a3fdb0852 fldTicketNumber MT-2026-084 | `at` | `"fldTicketNumber": "MT-2026-084"` | EXACT |
| base appPropertyOps name "Property Operations" | `airtable.airtable_bases.json` | `{"id":"appPropertyOps","name":"Property Operations"}` | EXACT |
| tblMakeReady name "Make-Ready Turns"; tblMaintenanceTickets name "Maintenance Tickets" | `airtable.airtable_tables.json` | both present, plus tblMaintenanceTickets description "System of record for maintenance work orders; Linear is secondary." | EXACT |

### The nine field / select-option identifiers

| Atom asserted | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| fldUnit singleLineText, primary | `atf` + `airtable.airtable_tables.json` | `{"id":"fldUnit","type":"singleLineText","table_id":"tblMakeReady"}`; tblMakeReady `primary_field_id: "fldUnit"` | EXACT |
| fldTurnStatus singleSelect, exactly three choices | `atf` | `choices: [selSched "Scheduled" blue, selProg "In Progress" yellow, selReady "Ready" green]` | EXACT, exactly 3 |
| fldMoveOut date | `atf` | `{"id":"fldMoveOut","name":"Move-Out Date","type":"date"}` | EXACT |
| fldTargetReady date | `atf` | `{"id":"fldTargetReady","name":"Target Ready","type":"date"}` | EXACT |
| fldNotes2 multilineText | `atf` | `{"id":"fldNotes2","name":"Notes","type":"multilineText"}` | EXACT |
| NO cost field on tblMakeReady, NO "Closed" status option (OE 5, OE 25) | `atf` full 9-field list | tblMakeReady has exactly 5 fields, none numeric/currency; fldTurnStatus has no "Closed" choice | EXACT |
| fldTicketNumber singleLineText (primary of tblMaintenanceTickets) | `atf` | present; primary_field_id fldTicketNumber | EXACT |
| fldDescription multilineText | `atf` | present | EXACT |
| fldPriority singleSelect selLow/selMedium/selHigh; fldCompletionDate date | `atf` | present | EXACT |
| Independent harness cross-check of the schema | Task 41 Opus run 6 real `get_table_schema` tool_result | returns the identical 9 fields and the identical selSched/selProg/selReady choice set | EXACT |

### Slack

| Atom asserted | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| ts 1779501868.000000, Carlos Mendez U07E4512181 | `sl` ts | `user_id "U07E4512181"`, `"Turn is officially kicked off for Mesa Vista 4C, tagging Brooke Phillips to get the make-ready checklist moving."` | EXACT |
| ts 1779501869.000001, Carlos, faucet/GFCI/drywall | `sl` | `U07E4512181`, `"Tony knocked out the faucet cartridge, GFCI swap, and drywall patch on 4C. Updated the make-ready record with all three checked off."` | EXACT |
| ts 1779501870.000002, Carlos, Sunshine invoice in QuickBooks | `sl` | `U07E4512181`, `"Sunshine Cleaning invoice is in QuickBooks, Mesa Vista 4C deep clean is closed out."` | EXACT |
| ts 1779501871.000003, Carlos, Pete's repaint bill entered | `sl` | `U07E4512181`, `"Pete's repaint is done, bill entered in QuickBooks for Mesa Vista 4C. Good to move to the next punch item."` | EXACT |
| ts 1779501872.000004, Jaime Salinas U2CD1BC03B2, "Tony got it done today, Airtable updated" | `sl` | `user_id "U2CD1BC03B2"`, `"Jaime flagged a paint touch-up on the bedroom closet trim. Tony got it done today, Airtable updated."` | EXACT on existence, author and text; **NOT RETRIEVABLE by OE 22's stated queries - see M1** |
| ts 1779501873.000005, Carlos, 4C market-ready | `sl` | `U07E4512181`, `"4C is market-ready, Brooke. Just updated the make-ready record, unit is good to list whenever you're ready."` | EXACT |
| C004 == #make-ready | `slack.slack_channels.json` | `{"id":"C004","name":"#make-ready"}` | EXACT |
| C005 == #vendors, exactly six messages, none about 4C | `sl` channel_id == C005 | 6 messages, all A Plus Carpet / unit 4B; zero "4C" | EXACT |
| C006 == #owner-relations (OE 27 alternative) | `slack.slack_channels.json` | `{"id":"C006","name":"#owner-relations"}` | EXACT |
| No Slack message anywhere states an owner cost figure (OE 22, OE 23) | `sl` all 580, scan for 1340 / 1,340 / 1140 / 1622 / 1812 / $387 / $95 / $85 | 0 hits for every pattern | EXACT |

### Gmail

| Atom asserted | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| thread 66132537181ecbe1, msg 5101c5a41dffa90a, 2026-06-02 | `gt` + `gm` | subject_normalized `"mesa vista 4c make-ready complete. cost summary for your records"`; message Date 2026-06-02T22:47:34+00:00 | EXACT |
| From carlos.mendez, To linda.castillo, Cc tony.reyes / pete.donovan / carmen.delgado / brooke.phillips / jaime.salinas | `gm` headers | all six addresses match the OE list in the OE's order | EXACT |
| Body: "including a touch-up on the bedroom closet trim that came out of our QC walkthrough" | base64 body decoded | verbatim substring present | EXACT |
| Body: "Tony's team handled all internal repairs in-house" | same | verbatim substring present | EXACT |
| Body: "owner invoice 2026-537", "This covers the vendor work only" | same | `"I've put together owner invoice 2026-537 in QuickBooks ... This covers the vendor work only."` | EXACT |
| Body states no dollar figures at all (OE 7) | same, numeric scan of decoded body | zero currency figures | EXACT |
| thread 525641a76c00fbe0 / msg e845219255a2bdb4 (Sunshine deep clean scheduling) | `gt` + `gm` | subject `"Mesa Vista 4C Post-Move-Out Deep Clean - Scheduling and Scope"`, To carmen.delgado@sunshinecleaning.com | EXACT |
| thread c138c134b23d60d3 / msg ab11ac615e2563f8 (repaint quote request) | same | subject `"Interior Paint Quote and Schedule Request - Mesa Vista Unit 4C"`, To pete.donovan@gmail.com | EXACT |
| thread 83872812663ee5c9 / msg a88bb5b7d1eb215b (deep clean invoice to Tony) | same | subject `"Invoice for Mesa Vista 4C Deep Clean"`, To tony.reyes@starpm.com | EXACT (see m9 on the "my invoice" gloss) |
| thread f43fdaee4372a09b / msg 13385eee8206db79 (Brooke; "posted confirmation in the vendors channel") | same | subject `"Pete Donovan Painting Invoice Received and Entered - Mesa Vista 4C"`; body `"... I've entered it as a vendor bill in QuickBooks and posted confirmation in the vendors channel."` | EXACT |
| None of the four OE 8 messages carries a dollar amount | decoded bodies | zero currency figures in all four | EXACT |

### Contacts, customers, vendors

| Atom asserted | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| contact_id b47044b4ec775b318bac813d5fb1bf5d = Linda Castillo, linda.castillo@gmail.com, job "Property Owner" | `ct` | `{"contact_id":"b47044b4ec775b318bac813d5fb1bf5d","first_name":"Linda","last_name":"Castillo","email":"linda.castillo@gmail.com","job":"Property Owner"}` | EXACT |
| Pete Donovan, pete.donovan@gmail.com, job "Exterior Painter" | `ct` | `{"email":"pete.donovan@gmail.com","job":"Exterior Painter"}` | EXACT |
| John Castillo, john.castillo@gmail.com, job "Water Delivery Representative" | `ct` | `{"email":"john.castillo@gmail.com","job":"Water Delivery Representative"}` | EXACT |
| Carlos Mendez carlos.mendez@starpm.com is the acting persona | `ct` + `2_Persona.txt` | `{"email":"carlos.mendez@starpm.com","job":"Onsite Property Manager"}` | EXACT |
| Customer proj-4ae920b7c9e8 "Linda Castillo", linda.castillo@gmail.com | `qb` customers | `{"DisplayName":"Linda Castillo","PrimaryEmailAddr":{"Address":"linda.castillo@gmail.com"}}` | EXACT |
| Customer proj-f6f9edfeae5c "Pete Donovan", pete.donovan@gmail.com | `qb` customers | `{"DisplayName":"Pete Donovan","PrimaryEmailAddr":{"Address":"pete.donovan@gmail.com"}}` | EXACT |
| Third Castillo customer proj-e576b03e2b4c "John Castillo" (NOT disclosed by OE 9) | `qb` customers, "Castillo" | `{"id":"proj-e576b03e2b4c","DisplayName":"John Castillo","PrimaryEmailAddr":{"Address":"john.castillo@gmail.com"}}` | PRESENT, **undisclosed - see m4** |
| Vendor master holds exactly EIGHT vendors (OE 20) | `qb` entity_type == vendor | 8: 200 Alamo HVAC Services, 201 Hill Country Plumbing, 202 Lone Star Electric, 203 Big Bend Restoration, 204 Permian Make-Ready Crew, proj-8fd39a6550fe Lone Star Maintenance Supply, proj-a989f559245a A Plus Carpet Cleaning & Repairs, proj-d016366b403c Sunshine Cleaning | EXACT, count = 8 |
| Permian email billing@permianmakeready.com | `qb` vendor 204 | `{"Address":"billing@permianmakeready.com"}` | EXACT |
| Sunshine email ap@sunshinecleaning.com | `qb` vendor proj-d016366b403c | `{"Address":"ap@sunshinecleaning.com"}` | EXACT |
| Alamo email invoices@alamohvac.com | `qb` vendor 200 | `{"Address":"invoices@alamohvac.com"}` | EXACT |
| Neither Tony Reyes nor Jaime Salinas is in the vendor master | `qb` vendors, name scan | 0 hits for either | EXACT |
| No vendor is a StarPM employee | `qb` vendors vs `ct` starpm.com staff | 0 overlap | EXACT |

### Every count the OE asserts

| Count asserted | Universe query | Result | Verdict |
|---|---|---|---|
| 113 bills in the ledger (OE 16) | `qb` entity_type == bill | 113 | EXACT |
| 10 bills at TotalAmt exactly 1340.00 (OE 16) | `qb` bills, TotalAmt == 1340.0 | 10, and all ten ids match the OE list: 102111031436, 103013736254, 170950667066, 177091955583, 258920406326, 274398891317, 315183662554, 686894936323, 696089964235, 968953468344 | EXACT |
| 3 of the ten belong to A Plus (proj-a989f559245a) | same | 103013736254, 177091955583, 258920406326 | EXACT (name spelling: see m3) |
| Exactly 4 bills reference Unit 4C (OE 13) | `qb` all entities, regex `\b4C\b` | 4 bills + 1 invoice (445653930748) | bills EXACT; **the "or receivable" clause is wrong - see m1** |
| 8 vendors (OE 20) | above | 8 | EXACT |
| 6 messages in C005 (OE 22) | `sl` C005 | 6 | EXACT |
| 2 4C make-ready rows (OE 3) | above | 2 | EXACT |
| 3 fldTurnStatus choices (OE 5) | above | 3 | EXACT |
| 6 consecutive C004 4C messages (OE 22, OE 23) | `sl` C004, ts 1779501868-1779501873 | 6, consecutive, no gaps | EXACT on the set; retrieval claim defective (M1) |
| 3 invoice lines on 2026-534 (OE 11) | above | 3 | EXACT |
| 3 records attribute the trim fix to Tony Reyes (OE 19) | `qb` 546359391323 note + `at` recc8534b3fd13954 fldNotes2 + `sl` ts 1779501872.000004 | 3, and an independent sweep found no fourth | EXACT and exhaustive |
| Arithmetic: 387 + 1340 + 85 = 1812; +85 = 1897; 387 + 1340 = 1727 | recomputed | 1812 / 1897 / 1727 | EXACT |
| Variance: 1812 - 1622 = 190; repaint 1340 - 1140 = 200 under; trim 95 - 85 = 10 over; 200 - 10 = 190 | recomputed | consistent | EXACT |

Zero empty cells. Zero NOT FOUND. 71 atom rows.

---

## LENS 2 - Answer-leakage sweep (deeper than FINAL's)

Method: every file in `_aux/Universe_Split/` loaded, `row_data` parsed, **and every Gmail
`payload.body.data` base64 field decoded and appended to the searched text**. Regex sweep for
`1812 | 1,812 | 1812.00 | 1 812`, `1897 | 1,897`, `1727 | 1,727`, and a boundary-anchored `190`
(`(?<![\d.,])190(?:\.0+)?(?![\d])`). Then a numeric sweep of every QuickBooks `TotalAmt`, `Balance`
and `Line[].Amount`.

| Target | Raw string hits | Adjudication |
|---|---|---|
| 1812 / 1,812 / 1812.00 | 11 (airtable 2, gmail messages 3, gmail threads 3, slack 3) | **ALL SPURIOUS.** Every hit is a substring of a timestamp or record id: `history_id`/`internal_date` values 1780181254000, 1781218127000, 1781812211000; Airtable `created_time` fractional seconds `...48.518124`; Slack `latest_reply` 1781812060.000184. Zero hits in any human-readable field. |
| 1897 / 1,897 | 6 | ALL SPURIOUS: `history_id` 1778851897000; entity id 328611897179. |
| 1727 / 1,727 | 3 | ALL SPURIOUS: entity ids 141727759080, 695617271495. |
| 190 (boundary-anchored) | 9 | 1 hubspot association `id: 190`; 4 Linear OPS-190 tokens; **3 real 190.00 line amounts** (see below). |
| Numeric: any TotalAmt or Line Amount == 1812.00 / 1897.00 / 1727.00 | **0** | The derived figure and both decoy figures exist nowhere as money in the universe. |
| Independent corroboration | `Fact_Ledger.amounts` (403 formatted amounts, auto-extracted from the universe) | `1812.00` ABSENT, `1897.00` ABSENT, `1727.00` ABSENT, `10.00` ABSENT; `85.00 / 95.00 / 190.00 / 387.00 / 1140.00 / 1340.00 / 1622.00 / 200.00` all PRESENT |

The three real 190.00 amounts: bill 330747391806 (Alamo HVAC, 1207 Ridgecrest Blvd exterior lighting),
invoice 210266819067 (Aiden Kowalski, "Interior paint touch-up labor - 334 Elmwood Dr Unit 2A"),
invoice 618793969708 (Pete Donovan, 2026-419, "Service call fee - diagnostic visit, 4408 Elmwood Ave").
None is on Mesa Vista 4C, none is billed to Linda Castillo, and none is described as a net variance.
No agent can read "the net understatement is 190.00" off any of them. Logged as m10, not a BLOCKER.

**Synthesis requirement confirmed.** No single record contains all three of 387, 1340 and 85 (scan of
all 625 QuickBooks entities: 0 candidates). The corrected total requires reading at minimum three
distinct bill records; the variance requires a fourth read (the invoice). Cross-surface money sweep:
`$1,340` appears twice in Gmail and zero times in Slack; `$1,140` once in Gmail (an unrelated
mass-email figure); `1622` zero times in Gmail and zero in Slack; `2026-534` appears in **no** email,
which independently confirms OE 7's claim that the invoice must be located by owner and unit.
The belief email's "a copy is attached here" is a phantom: `has_attachments: false`, `parts: []`.

Prompt sweep: `5_Prompt.txt` contains **no numeral of any kind**. Zero leakage.

**LENS 2 verdict: PASS. No BLOCKER. The derived 1812.00 and the 190.00 net are unreadable and
unstateable from any single tool call.**

---

## LENS 3 - Hardness end-to-end trace

| Lever | Prompt sentence that surfaces it | OE step that exercises it | Fact_Ledger / universe atoms the agent must touch | Rubric forward-mappable? |
|---|---|---|---|---|
| **L2 structured-DB skip (symmetric flagship)** | "Go back to what each vendor charged us for the 4C work and set it against the line items I sent her." | OE 13 (find the four bills), OE 15 (the 1340.00), OE 17 (the 85.00), OE 21 (the sum) | bills 195089456477 / 696089964235 / 546359391323; the 1340.00 and 85.00 exist on no other surface (Slack 0 hits, invoice 0 hits, summary email 0 figures) | **YES.** Outcome 2.1: "reports the corrected owner pass-through as 1812.00, not 1622.00, not 1897.00, not 1727.00" (Learnings L18). Traversal-dependent: unreachable without opening the AP side. |
| **L10 reversal / supersession** | "because that summary is the record she keeps"; "Correct the invoice she is holding so it carries the right figure" | OE 3 (live vs stale make-ready row), OE 7 (unreliable summary email), OE 11 (authoritative-looking AR), OE 24 (amend in place), OE 27 (supersede the old figure) | invoice 445653930748 (1622.00, sync_token 0); recc8534b3fd13954 vs recbd087a4abd605b; phantom DocNumber 2026-537 | **YES.** Outcome 1.1 on `update_invoice` against 445653930748 with no `create_invoice`; Outcome 1.2 requiring the Slack post to name 1622.00 as superseded. |
| **L6 near-miss entity (Opus-asymmetric)** | "Linda Castillo owns that unit."; "to the dollar, no more and no less" | OE 1 (Linda vs Pete vs John), OE 9, OE 10, OE 16 (the ten-bill cluster), OE 19 (twin 85.00) | contact b47044b4ec775b318bac813d5fb1bf5d; customers proj-4ae920b7c9e8 / proj-f6f9edfeae5c; all ten 1340.00 bill ids; both 85.00 bill ids | **YES.** Outcome 1.2 binding the repaint figure to bill PD-2026-09 / 696089964235 and the owner to Linda Castillo. |
| **L11 / L9 net-vs-gross (Gemini-leaning)** | "Only outside vendor work belongs on her side. Anything that was our own time on the unit, an internal walk or a condition check we handled in house, stays off her bill entirely." | OE 18, OE 19, OE 21, OE 25, OE 28 | bill 991582431419 (AccountRef 61, "Unit condition inspection ...") vs 546359391323 (AccountRef 64, "Pass-through to owner") | **PARTIAL - see the displacement finding below.** A criterion is writable ("excludes the 85.00 condition walk and retains the 85.00 closet trim") but it cannot fail independently of L2. |
| **L1 latching (reserve)** | "When the turn wrapped back in the spring I billed her for the work and sent her a summary calling it done" | OE 3, OE 4, OE 6, OE 7 | recc8534b3fd13954 selReady; reca424761ae15355 "market-ready"; belief email "fully wrapped up" | **YES**, as a reserve. Outcome 1.2 on OE 25 graded on content (final owner cost + closed state in fldNotes2), which per OE 25 is explicitly not id-bound. |

**`HARDNESS_REGRESSION`: NONE.** All four selected levers plus the reserve trace prompt sentence to OE
step to universe atom with cited evidence. Nothing is "probably triggered".

### Learnings item 9 (Task 41) applied to L11 - plainly stated

**L11 IS DISPLACED.** It cannot produce its own observable fail. But the mechanism differs from Task 41
in a way worth recording, because it changes the remedy.

In Task 41 the displacement was two-hop: no run opened the bill at all, so the credit-disposition step
never ran. Here L2's gate and L11's decision surface are **co-located in a single tool call**. Verified
empirically: QuickBooks `search_*` returns the complete properties envelope, not a summary. Task 41
Opus run 1's real `search_invoices(query: "Mitchell")` tool_result carries `Line[]` with `Amount` and
`Description`, `Balance`, `TotalAmt`, `DocNumber`, `CustomerRef`, `PrivateNote`, `CustomerMemo` and
`SyncToken`. So one `search_bills(query: "Mesa Vista 4C")` hands the agent all four 4C bills complete
with `TotalAmt`, `AccountBasedExpenseLineDetail.AccountRef` and `PrivateNote` - the entire twin-85.00
decision surface arrives in the same call that breaks L2.

The consequence is unchanged, though: L11 has **zero observable surface among agents that fail L2**.
Under the Hardness_Plan's own [HIGH] prediction that L2 sweeps ~0/12, L11's expected observable-fail
count is **0**, exactly as in Task 41. The plan already concedes this in Stump Hypothesis 3, which is
to its credit. What the OE does **not** do is exploit the co-location that Learnings item 9 prescribes
as the remedy ("pair it with an EASY path to the figure so agents reach the disposition step"). The
easy path exists in this universe and is one call wide, and the OE routes past it through five
`get-bill` calls that add no information. S4 should expect to measure one stump, not two, and should
not credit L11 with any fail it cannot separate from L2.

---

## LENS 4 - Strict density projection (StarPM per-model scheme: >= 40 PASS, 15-39 THIN, < 15 INSUFFICIENT)

I did not accept the Hardness_Plan's or Council B's projections. I built empirical anchors from all 18
completed trajectories of the three prior StarPM V4 dual-model tasks, which share this base universe,
this harness and a 3-to-4-write OE shape.

| Task | Opus runs | Opus mean | Gemini runs | Gemini mean |
|---|---|---:|---|---:|
| 39 | 46, 52, 46, 46, 45, 26 | 43.5 | 33, 37, 28, 31, 36, 33 | 33.0 |
| 40 | 31, 40, 47, 39, 47, 45 | 41.5 | 47, 45, 37, 38, 33, 40 | 40.0 |
| 41 | 51, 38, 61, 44, 34, 60 | 48.0 | 37, 30, 49, 39, 41, 37 | 38.8 |
| **Pooled** | min 26 | **44.3** | min 28 | **37.3** |

Note that this pooled Gemini figure is not a solved-run figure: pass@1 on all three tasks was at or
near 0, so these ARE stumped-run counts. The Hardness_Plan's assumed uniform "Gemini runs 9-10 fewer
calls than Opus" holds on tasks 39 and 41 but not on task 40 (delta only 1.5), so the pooled delta is
about **7**, not 9.5.

Task 43 adjustments: **+2 to +4** reads for a wider disambiguation surface than any of the three anchors
(113 bills, the ten-bill 1340.00 cluster, six Mesa Vista sibling rows, three Castillo/Donovan
customers, two 85.00 twins); **-4 to -6** on the stumped branch for the shed conditional writes.

### The conditional-write shed

The prompt's third paragraph opens: *"If her charges come out clean against what we paid, log 4C closed
and that is the end of it."* Only then: *"If they do not ... Correct the invoice ... get our 4C
make-ready record in Airtable updated ... Then email Linda ... And drop a line in our channel."*
So **three of the four writes are conditional on the agent finding the discrepancy**. An agent that
trusts the visible invoice concludes "clean" and executes exactly one write (OE 25), shedding OE 24,
OE 26 and OE 27.

### Per-model projection

| Model | Branch | Band | Midpoint | Gate |
|---|---|---|---:|---|
| **Opus 4.8** | solving (all 4 writes, opens the bills) | 42-52 | **47** | PASS |
| **Opus 4.8** | stumped (trusts the invoice, 1 write) | 30-46 | **38** | THIN |
| **Opus 4.8** | blended at the plan's own predicted 1-solve / 5-stump mix | 30-52 | **39.5** | THIN, marginal |
| **Gemini** | solving | 35-45 | **41** | PASS, at the line |
| **Gemini** | stumped | 26-36 | **31** | THIN |
| **Gemini** | blended at 1-solve / 5-stump | 26-45 | **32.7** | THIN |

**Headline midpoints on the intended (OE-described, solving) trajectory, which is the gating
convention: Opus 47 -> PASS. Gemini 41 -> PASS at the line; blended 33 -> THIN.**
Gate call: **Opus PASS, Gemini THIN** - the same position the Hardness_Plan accepted, reached
independently. No INSUFFICIENT risk: the empirical floor across 18 same-harness runs is 26 (Opus) and
28 (Gemini), both far above 15.

### Strict-minimizing floor, stated for completeness

Counting each OE step exactly once, with the five `get-bill` calls in OE 14/15/17/18/19 collapsed to
zero because one `search_bills` already returns their entire payload: stumped Opus **16-21**, stumped
Gemini **13-18**. The Gemini figure dips below the 15 INSUFFICIENT line. I treat this as theoretical
rather than expected, because no run in 18 prior same-harness runs came within 10 calls of it. It is
recorded as a band floor, not as an INSUFFICIENT call.

**Correction to Council B (M4 below):** its Round-2 Opus midpoint of 46, described as "further clear
of the line", is a solved-branch figure that (a) takes +2 density credit for the two OE 19 `get-bill`
re-reads that return data the agent already holds, and (b) does not model the conditional-write shed on
the branch the plan itself predicts will be modal. Blended, Opus is at 39.5, not 46.

### Service breadth (against the 47-call Opus solving sketch)

| Service | Calls | Share |
|---|---:|---:|
| quickbooks | 21 | 44.7% |
| airtable | 9 | 19.1% |
| gmail | 8 | 17.0% |
| slack | 5 | 10.6% |
| contacts | 4 | 8.5% |
| **Distinct** | **5** | dominant 44.7% < 60%, all >= 5% |

**Breadth: PASS.**

---

## LENS 5 - Adversarial veteran review

| Check | Finding |
|---|---|
| Is the prompt's implicit framing preserved, or does the OE smuggle in explicitness? | **ONE VIOLATION.** The framing itself is preserved: no OE claims the prompt hints at an error, and OE 7/11 correctly treat the summary and the invoice as the belief anchors under test. But **OE 24 asserts "the prompt forecloses it" of a credit memo, and it does not** (M2). Everything else traces to prompt language: OE 12's "corrected in place rather than credited or re-issued" to "I do not want a second bill created next to the one she already has"; OE 19's exclusion to "an internal walk or a condition check we handled in house"; OE 21's "to the dollar" test to "no more and no less". |
| Entity-drift seams | **Linda / Pete / John Castillo: HANDLED** - OE 1 names all three with correct jobs and emails, OE 9 resolves the customer side. **Permian Make-Ready Crew vs Pete Donovan Painting: HANDLED** - OE 15 states VendorRef Permian 204 while the invoice line and the Gmail subject say "Pete Donovan Painting"; both forms verified present in the universe, so both quotations are grounded. There is no vendor record named "Pete Donovan Painting", and the OE never claims one. **Tony Reyes vs Tommy Reyes: NOT SURFACED** (m5). Tommy Reyes is a real separate contact (a4c863c4d92d53a59c310bb29abd6d0c, tommy.reyes@gmail.com, Tenant), and the string "Tommy Reyes unit" sits on decoy invoice 340207319849 - the same 1340.00 amount, the same owner Linda Castillo. Zero occurrences of "Tommy" in the OE. Also unsurfaced: Gmail 6f2669a41401485a, Carlos to Dave, "Tony flagged the Reyes Plumbing invoice ... The invoice total is $1,340". |
| Single-channel lock-in | **CLEAR.** The prompt names only a goal ("drop a line in our channel for the crew and front office"). OE 27 names C004 but explicitly admits C005 and C006 and says the step "is graded on the corrected figure and the supersession of the old one, not on the channel id". |
| "Approximately" near ids / dates / amounts | **CLEAR.** Zero occurrences of "approximately", "approx", "about", "roughly" anywhere in the OE. |
| "(or similar)" near values that must be exact | **CLEAR.** Zero occurrences. Where alternatives are offered they are enumerated exactly (OE 12's two report tools, OE 7/8/13's alternative query strings), and every alternative tool was confirmed to exist with the stated parameters. |
| OE meta-tags | **CLEAR.** No `[BLOCKER]`, no lever ids, no rubric ids, no "Hardness", no "stump", no markdown. 28 sequential steps, all opening with an action verb. Pure ASCII (0 non-ASCII code points). |
| OE step that is pure reasoning with no tool anchor | **OE 28** names no tool. Excluded as a finding on a hard exclusion: `Reference/OE_Format.md`, section "Final paragraph (optional)", explicitly sanctions a closing summary OE for a write-heavy finale, and OE 28 is exactly that. **OE 19** is a 484-word / 12-sentence argument whose only tool anchor is a re-read of two records already retrieved in OE 17 and OE 18, which returns nothing new. Not a bare reasoning step, but the anchor is cosmetic; folded into M4 (Council B took density credit for it) and m8 (convention). |
| Any count, id or quoted string not matching byte-for-byte | **ONE.** OE 16 writes "A Plus Carpet Cleaning and Repairs" in its enumeration where the universe DisplayName is "A Plus Carpet Cleaning & Repairs" (the correct ampersand form does appear later in the same step) - m3, carried unfixed from Council A Min-1. Everything else in the 71-row table is byte-exact, including the comma in "412 Garfield Ave, Unit 3C", all four full PrivateNotes, the six Slack ts values and all 20 DocNumbers. |
| Instruction impossible on the real harness | **NONE.** All 25 tools exist in `StarPM_Base_Universe/7_Server_Tools_Details.json` with the exact names and parameter spellings used: `get-bill(id)` hyphenated; `search_records(baseId, table, query)` versus `list_records_for_table(baseId, tableId, recordIds)` versus `update_records_for_table(baseId, tableId, records)`; `get_table_schema(baseId, tables[])`; `update_invoice(id, SyncToken, properties)`; `create_draft(..., body, replyToMessageId)` and the OE says so explicitly; `slack_send_message(channel_id, message)` and the OE says "not payload and not text"; `get_customer_balance(customer, start_date, end_date)`; `read_invoice(invoice_id)`; `contacts_get_contact(contact_id)`; `get_vendor_expenses(vendor, start_date, end_date)`. No phantom tool, no wrong service, no unreachable record. |
| Page size too small to return what the step claims | **TWO CHECKS, ONE FAILS.** OE 16's own pagination handling is correct: 113 bills, `max_results: 200` or `start_position` paging, and it says why a 50-page cannot reach them. OE 23's bare `slack_read_channel(channel_id: "C004")` **clears empirically**: C004 holds 144 rows of which 48 are `is_activity_message: true`, and Task 40's Opus run 1 issued exactly `slack_read_channel(channel_id: "C004")` against this same base universe and received **96 messages newest-first from ts 1782415250.000193 down to 1777838404.000049, including all six 4C ts values**. No truncation. **OE 22's search does NOT clear - M1.** |

### Act-vs-defer HARD GATE (`Evals_starpm/2_OE_Eval.md` Phase 2.4)

No write-action OE rests on a `proposed_resolution` or a system-suggested remediation; all four writes
come from explicit prompt directives. Scanned all eight Slack channels and the whole of Carlos's
mailbox for a documented defer / accept-timing / do-not-act decision touching 4C, Linda Castillo, Mesa
Vista or owner billing: **zero hits**. No defer path is foreclosed. **PASS.**

---

## The pivotal question - adversarial audit of OE 19's five grounds

The question: is the 85.00 closet trim (546359391323, Permian, AccountRef 64) owner-billable while the
85.00 condition walk (991582431419, Alamo HVAC, AccountRef 61) is not, giving 1812.00 rather than the
1727.00 or 1897.00 decoys?

### Are the five grounds true in the data?

| Ground | Claim | Verification | True? |
|---|---|---|---|
| **G1** | "Internal labor charge for" opens BOTH PrivateNotes (Tony Reyes on 2026-519, Carlos Mendez on 2026-481-566) and appears on only these two records in the whole ledger, so it marks who performed or routed the work, not who was paid | Substring scan of all 625 entities: exactly 2 hits, both as claimed | **TRUE, exactly** |
| **G2** | The genuinely in-house 4C items (faucet cartridge, GFCI swap, drywall patch) produced NO vendor bill, so our own time on this unit generated no payout; both 85.00 records by contrast are real third-party payouts with an open balance | No bill in the ledger bills those three items as work; both 85.00 bills carry `Balance: 85.0` and third-party VendorRefs (204, 200) | **TRUE.** Note the subtlety the OE handles correctly: 991582431419's own line description *enumerates* those three items as punch-list observations, which reinforces rather than undercuts the reading |
| **G3** | 2026-481-566 is literally a unit condition inspection and punch list write-up of Carlos Mendez's make-ready walk, matching the prompt's excluded category almost word for word; 2026-519 is a same-day physical trim repaint | Line description `"Unit condition inspection and punch list documentation - Mesa Vista Unit 4C, vacated turnover"` versus prompt `"an internal walk or a condition check we handled in house"`; 2026-519 line `"Bedroom closet trim paint touch-up ... same-day repair"` | **TRUE.** The strongest ground: it is the only one anchored in prompt language rather than in ledger metadata |
| **G4** | 2026-519 posts to Owner Reserve (Trust) 64, a trust bank account holding the owner's own funds, and is the only one of the four 4C bills coded there; 2026-481-566 posts to Supplies 61, an operating expense; and this is a twin-85 tiebreaker only, not a general billability test | Account 64 = `AccountType "Bank"`, `AccountSubType "TrustAccounts"`, `CurrentBalance 70624.57`. Across the four 4C bills: 62, 63, 64, 61 - 64 used once. Across all 113 bills account 64 is used 31 times, so the OE's self-limiting caveat is necessary and correct | **TRUE, and the gloss is understated.** The OE's honest scoping of this ground is the right call |
| **G5** | 2026-519 says "Pass-through to owner - pair with corresponding AR invoice", whereas 2026-481-566 positions itself as the intake whose punch list will DRIVE later vendor bills and owner pass-through invoices, i.e. upstream of the pass-through | Both quoted byte-exact from the PrivateNotes | **TRUE, exactly** |

All five are true. The three disclosed counter-evidence records are also true, correctly quoted, and
exhaustive (an independent sweep found no fourth Tony-attribution record).

### Is the argument sufficient to make 1812.00 the unique end-state?

Yes. The adversarial stress test is the symmetry objection: G1 and G2 neutralise rather than
discriminate, because both bills carry the same template phrase AND both are genuine third-party
payables with open balances. The OE says so itself, which is why it does not rest on them. What
actually discriminates is G3, G4 and G5, and they are independent of each other: one is prompt-textual,
one is a hard ledger fact, one is the operative instruction on each record. Two further convergent
vectors sit outside OE 19 and are supplied by OE 11, OE 18 and OE 24: the closet trim **already has a
line on 2026-534** at 95.00 so correcting it to 85.00 is squarely "correct the invoice she is holding",
whereas the condition walk **has no line at all** so adding it would create a charge Carlos never
billed; and the summary email places the trim inside Pete Donovan's vendor repaint scope while bucketing
Tony's work separately. That is five independent vectors pointing one way against one ambiguous
template phrase that appears on both records.

I record the residual honestly: a well-reasoned run can still read "our own time on the unit" as a
general category that swallows the trim (three records say Tony did it) and land on 1727.00. That is
the designed L11 decoy and its reachability is a feature. The OE now discloses every record that
supports it and answers each, so a 1727.00 run fails on substance rather than on OE concealment.
**1812.00 is the uniquely best-supported end-state.**

### Root-cause adjudication

The residual ambiguity is created by **designed universe data** - a bill that is simultaneously an
"Internal labor charge" and a payable to Alamo HVAC Services - not by any prompt sentence. The prompt's
carve-out names the excluded bill's line description nearly word for word ("an internal walk or a
condition check" against "Unit condition inspection and punch list documentation"), and its general rule
("Only outside vendor work belongs on her side") keeps the three vendor payouts in. A carve-out
following a general rule reads as an exception to it, which is the resolution the OE adopts. The prompt
is adequate.

**`PROPAGATE TO S1`: NOT EMITTED.** M2 is an OE over-reading of prompt language, repaired in the OE.
No S1 re-run. The pipeline does not STOP.

---

## LENS 8 - Regression anchor verification (run independently)

```
python3 Validators/test_regression_anchors.py
 -> Regression anchors: 62 passed, 0 failed out of 62
  (independently reproduced; matches the 62/62 reported)

python3 Validators/validate.py --phase oe --task Tasks/43_6a62ccaf5853030245ac9d53
 -> [PASS] oe: 0 fails, 0 warns, 3 notes

python3 Validators/verify_universe_atoms.py --task Tasks/43_6a62ccaf5853030245ac9d53
 -> [PASS] verify_universe_atoms: 0 fails, 0 warns, 16 atoms checked (universe: starpm)
```

Every NOTE listed as a hard issue per the strictest reading:

| # | NOTE | Strict adjudication |
|---|---|---|
| N1 | `universe: starpm` | Informational. Correct: `_aux/Universe.txt` = "starpm", and the detector's StarPM anchors (SP-1 through SP-9, wave2/wave3) all pass. No issue. |
| N2 | `OE step count: 28` | Informational. 28 equals the maximum in the V3 reference distribution (`Reference/OE_Convention_Inventory.json`: Task13 = 28, mean 16.5). At the ceiling but not over it. Related convention drift is the word count, not the step count - see m8. |
| N3 | `no closed fiscal periods in Fact_Ledger.lifecycle.closed_periods - skipping lifecycle precondition check` | **Real, and it under-reports.** StarPM legitimately has no fiscal periods (`atom_counts.fiscal_periods: 0`), so the skip is correct in kind. But `Fact_Ledger.lifecycle.today` is also `null`, while `_aux/Universe_Index/today_horizon.json` carries `"universe_today": "2026-07-01"`, `"universe_timezone": "America/Chicago"`. The ledger is dropping a date it has. Folded into M5. |

**Additional validator finding not surfaced by any NOTE - M5.** The `verify_universe_atoms` PASS covers
**16 atoms: 5 Airtable record ids and 11 email addresses.** It touches none of the OE's load-bearing
identifiers. `collect_atoms_from_text` has no pattern for a 12-digit QuickBooks entity id and no pattern
for a Slack `ts`, and `Fact_Ledger.ids` has no key for either (`ids.invoice` holds 504 **DocNumbers** --
`1053`, `PD-2026-09`, `QR-2026-0441` -- not entity ids; `entities` is `[]` with `atom_counts.entities: 0`).
So all five QuickBooks entity ids, all six Slack ts values, both customer ids, all eight vendor ids and
every asserted count went unverified by the validator. The 71-row table above is the only verification
of record. Confirmed by direct membership test: `445653930748`, `546359391323`, `991582431419`,
`696089964235`, `195089456477` are all ABSENT from `Fact_Ledger.ids.invoice`, while all 20 cited
DocNumbers are PRESENT and the phantom `2026-537` is correctly ABSENT.

---

## LENS 7 - Anti-Rationalization Rule and explicit self-scan

I re-read my own reasoning for every "I considered flagging X but decided it is fine because..." line.
Nine such lines existed. Five were **PROMOTED** to findings. Four are **EXCLUDED**, each on a hard
exclusion, stated below so the exclusion can be checked rather than trusted.

**Promoted:**

1. "The 190.00 line amounts are a coincidence, not a leak." -> promoted to **m10**. The collision is
   undisclosed and one of the three sits on a decoy OE 10 puts in front of the agent.
2. "Bill 173322471681's 1140-vs-1380 note does not mention 4C, so it is out of scope." -> promoted to
   **m7**. It is the mirror of the 4C repaint variance, on the same AccountRef 63, and OE 16 claims to
   disambiguate the amount-cluster trap while naming only the 1340.00 side.
3. "OE 16 also gives the correct '&' spelling later in the same step, so the 'and' form is harmless."
 -> promoted to **m3**. Strictest reading requires byte-exact entity names; Council A logged this and
   it was not fixed.
4. "OE 19's `get-bill` re-reads are harmless redundancy." -> promoted into **M4** and **m8**. Not
   harmless: Council B converted them into +2 density credit, and the calls return nothing new.
5. "Invoice 310712648304 does not reference 4C, so OE 10's controlling sentence excludes it." ->
   promoted to **M3**. A 385/387 substitution yields 1810.00, a wrong figure absent from OE 21's
   catalog and therefore from any rubric derived from it.

**Excluded, with hard exclusions:**

6. OE 23's bare `slack_read_channel(C004)` and a possible default page cap. **HARD EXCLUSION:**
   empirically disproved. Task 40 Opus run 1, same base universe, C004 with 144 rows, issued exactly
   `{"channel_id": "C004"}` and received 96 messages spanning ts 1782415250.000193 down to
   1777838404.000049 including all six 4C ts values. 144 minus the 48 `is_activity_message: true` rows
   equals 96, so the harness filters activity rows and truncates nothing.
7. OE 28 having no tool anchor. **HARD EXCLUSION:** `Reference/OE_Format.md` section "Final paragraph
   (optional)" explicitly sanctions a closing summary OE for a write-heavy finale.
8. Bill 696089964235 posting an AP expense to account 63 "Management Fee Income", an Income account.
   **HARD EXCLUSION:** this is a no-injection task, the coding is base-universe data the CB may not
   alter, and OE 19 G4 already discloses it by name. Not an OE defect.
9. OE 16's "a query of '1340' will not match on amount". **HARD EXCLUSION:** verified true. No bill's
   DocNumber, line Description or PrivateNote contains the substring "1340", so a text query returns
   nothing, which is exactly what the step says.

---

## Findings

### BLOCKER
None.

### MAJOR

**[MAJOR] M1 - OE 22's stated queries cannot return the sixth C004 message it enumerates, and that
message is OE 19's third disclosed counter-evidence record.**
`Tasks/43_6a62ccaf5853030245ac9d53/6_Oracle_Events.txt:43` (OE 22).
The message text is `"Jaime flagged a paint touch-up on the bedroom closet trim. Tony got it done today,
Airtable updated."` It contains no "4C", no "Mesa Vista" and no "make-ready", and it is unthreaded
(`thread_parent_id: null`, `reply_count: 0`), so `include_context` cannot pull it in as a reply.
Harness semantics, established from real tool_results in the same base universe: the search is an
AND over query tokens (Task 41 Opus run 1, `"Mitchell eviction"` -> 4 messages; `"Mitchell eviction
payment plan"` -> 0), and `slack_search_public_and_private(query: "make-ready")` returns
`"## Channels (1 results)"` with **zero** messages in all six Task 40 Opus runs. Therefore, of the
three queries OE 22 names: `"Mesa Vista 4C"` returns 3 of the 6 (ts ...868, ...870, ...871),
`"4C"` returns 5 of the 6 (adds ...869, ...873), `"make-ready"` returns 0 messages. **None returns
ts 1779501872.000004.**
*Exact fix:* in OE 22, replace the query list with `query: "Mesa Vista 4C"` or `"4C"` or
`"bedroom closet trim"`, and add: "Note that the Jaime Salinas post at ts 1779501872.000004 contains
neither the unit token nor the phrase make-ready, so it is reached by a query on "closet trim" or by
the direct channel read in OE 23, not by a unit-scoped search. A query of "make-ready" matches the
channel name and returns no messages."

**[MAJOR] M2 - OE 24 attributes to the prompt a foreclosure the prompt does not contain, and supports
it with a rationale that is wrong for the instrument named.**
`Tasks/43_6a62ccaf5853030245ac9d53/6_Oracle_Events.txt:47` (OE 24).
OE 24: *"do not raise a credit memo alongside 2026-534 either. A second owner document beside the one
she already holds would double-bill Linda for the same turn, and the prompt forecloses it."*
The prompt says: *"I do not want a second bill created next to the one she already has."* A credit memo
is not a bill; and a credit memo **reduces** a receivable, so it cannot "double-bill". The invoice is
under-stated by 190.00, which makes a credit memo the wrong instrument on its own terms without any
appeal to prompt language. `_aux/Reasoning/OE_solvability.md` already previews the rubric this will
become ("the negative-guard rubric: does NOT create a second owner invoice or credit memo"), so the
defect is one S3 step away from an ungrounded negative-guard criterion. This is the Learnings L30 /
2026-07-24 item-5 defect class.
*Exact fix:* replace the clause with: "Do not raise a credit memo either. 2026-534 is understated, not
overstated, so a credit memo is the wrong instrument, and OE 12 established that no payment has been
applied, so the invoice is still amendable in place. The prompt forecloses a second bill; the credit
memo is foreclosed by the direction of the variance and by the open balance, not by the prompt."

**[MAJOR] M3 - OE 10's decoy inventory does not match what its own queries return, and it omits the
closest decoy in the ledger, leaving a wrong answer out of OE 21's catalog.**
`Tasks/43_6a62ccaf5853030245ac9d53/6_Oracle_Events.txt:19` (OE 10) and `:41` (OE 21).
(a) OE 10 says *"The same search surfaces decoys that must not be used ... plus Pete Donovan receivables
240572546619 (2026-STD-042), 618793969708 (2026-419) and 328611897179 (INC-2026-041)."* None of the
three stated queries (`"Linda Castillo"`, `"Mesa Vista 4C"`, `"2026-534"`) returns any of them: all
three are `CustomerRef` Pete Donovan (proj-f6f9edfeae5c) on unrelated properties.
(b) A `"Linda Castillo"` query DOES return invoice **310712648304**, which OE 10 omits: `DocNumber 2547`,
`TotalAmt 385.00`, `CustomerRef Linda Castillo proj-4ae920b7c9e8`, `TxnDate 2026-05-01`,
`DueDate 2026-05-31`, line `"Pass-through: A Plus Carpet Cleaning & Repairs - deep-clean and seam
re-stretch, Rio Bend unit (owner-billable vendor cost)"`, PrivateNote `"Owner pass-through invoice ...
(same $385 amount) ..."`. Same owner, same dates, same pass-through framing, same "deep-clean" scope
word, 385.00 against the true 387.00. Substituting it yields **1810.00**, which appears nowhere in
OE 21's wrong-figure list (1622.00 / 1897.00 / 1727.00) and would therefore be missing from any
Outcome 2.1 rubric written from OE 21.
*Exact fix:* in OE 10, split the decoy list by the query that surfaces it: under `"Linda Castillo"`
list 340207319849 (2026-AP-0184, 1340.00, 412 Mesquite) **and 310712648304 (2547, 385.00, Rio Bend
pass-through deep-clean, not to be confused with the 387.00 4C deep clean)**; move the three Pete
Donovan receivables under a separate sentence noting they surface on a `"Pete Donovan"` query, which an
agent will run because the bill notes point at him. In OE 21, add 1810.00 to the wrong-figure list with
its cause ("comes from taking the 385.00 Rio Bend pass-through instead of the 387.00 4C deep clean").

**[MAJOR] M4 - the Hardness_Plan's THIN-density mitigation does not hold on the branch the plan itself
predicts, and Council B's Opus midpoint is over-credited.**
`Tasks/43_6a62ccaf5853030245ac9d53/_aux/Hardness_Plan.md` (section "THIN density acceptance", item 2)
and `_aux/Council_Reports/S2_B_adversarial.md` (Round-2 [B3]).
The plan accepts Gemini THIN on the reasoning that "Writes execute on BOTH models" and that a 4-write OE
"pulls the Gemini midpoint toward ~40". But the prompt makes three of the four writes conditional
("If her charges come out clean against what we paid, log 4C closed and that is the end of it"), and
Stump Hypothesis 1 predicts ~0/12 solve, so on the modal branch only OE 25 executes and the mitigation
delivers nothing. Separately, Council B's Round-2 Opus midpoint of 46 takes +2 credit for the two OE 19
`get-bill` re-reads, which return data the agent already holds: QuickBooks `search_*` returns the full
properties envelope including `Line[].Amount`, `AccountBasedExpenseLineDetail.AccountRef`, `PrivateNote`
and `SyncToken` (verified against Task 41 Opus run 1's real `search_invoices` tool_result), so one
`search_bills(query: "Mesa Vista 4C")` already yields everything OE 14/15/17/18/19 re-fetch. Blended
across the predicted 1-solve / 5-stump mix, Opus lands at **39.5**, not 46.
*Exact fix:* no OE text change is required and none should be invented to pad the number. Amend the
Hardness_Plan's THIN acceptance to state that the write-count mitigation applies only to the solving
branch, and carry to S4: expect modal Gemini near 31 and modal Opus near 38, with the actionable anomaly
threshold below 24 on Gemini rather than below 30.

**[MAJOR] M5 - the `verify_universe_atoms` PASS gives zero coverage of the OE's load-bearing
identifiers, and `Fact_Ledger` is under-populated in three ways.**
`Validators/verify_universe_atoms.py` (`collect_atoms_from_text`) and
`Tasks/43_6a62ccaf5853030245ac9d53/_aux/Fact_Ledger.json`.
The reported "0 fails, 16 atoms checked" is 5 Airtable record ids plus 11 email addresses. The extractor
has no pattern for a 12-digit QuickBooks entity id and none for a Slack `ts`, and the ledger has no key
for either: `ids.invoice` holds 504 DocNumbers rather than entity ids, `entities` is `[]`
(`atom_counts.entities: 0`), and `lifecycle.today` is `null` even though
`_aux/Universe_Index/today_horizon.json` carries `2026-07-01` / `America/Chicago`. Verified by
membership test: all five 4C-relevant QuickBooks entity ids are ABSENT from `ids.invoice`. So the four
bill ids, the invoice id, the six Slack ts values, both customer ids, all eight vendor ids and every
asserted count were never machine-checked, and NOTE N3 is the only visible symptom.
*Exact fix:* add to `collect_atoms_from_text` a `qb_entity_ids` pattern (`\b\d{12}\b`) and a
`slack_ts` pattern (`\b17\d{8}\.\d{6}\b`) with StarPM verifiers that resolve them against
`quickbooks.quickbooks_entities.json` ids and `slack.slack_messages.json` ts values; populate
`Fact_Ledger.ids.qb_entity` and `ids.slack_ts`; and set `lifecycle.today` from
`Universe_Index/today_horizon.json`. Until then, treat the manual per-atom table as the verification of
record and do not cite the 16-atom PASS as atom coverage.

### MINOR

| # | Issue | Location | Exact fix |
|---|---|---|---|
| m1 | Self-contradiction. "No other bill or receivable in the ledger touches 4C" is false: invoice 445653930748 is a receivable that touches 4C, as OE 10 and OE 11 establish. | `6_Oracle_Events.txt:25` (OE 13) | "No other vendor bill in the ledger touches 4C, and the only receivable that does is 2026-534 itself, so these four bills are the entire universe of what was paid out on the unit." |
| m2 | False absolute. "The 1340.00 for this scope exists nowhere but on this bill, not on invoice 2026-534, not in the summary email, and not in Slack." Slack verified clean (0 hits for 1340 or 1,340 across all 580 messages) and the two named documents are clean, but the enumeration omits Gmail, where "$1,340" appears twice: 4a20c7c433db278a (Tony to Isela, a monthly rent rate) and 6f2669a41401485a (Carlos to Dave, "Tony flagged the Reyes Plumbing invoice ... The invoice total is $1,340"). | `6_Oracle_Events.txt:29` (OE 15) | "The 1340.00 as the 4C repaint cost exists only on this bill. It is not on invoice 2026-534, not in the summary email and not anywhere in Slack. Two unrelated Gmail messages do mention a 1,340 figure (4a20c7c433db278a, a rent rate; 6f2669a41401485a, a Reyes Plumbing invoice), and neither concerns 4C." |
| m3 | Entity name not byte-exact: "A Plus Carpet Cleaning and Repairs" versus the universe DisplayName "A Plus Carpet Cleaning & Repairs" (proj-a989f559245a). The correct form appears later in the same step. Council A Min-1, carried unfixed. | `6_Oracle_Events.txt:31` (OE 16) | Use the ampersand form in the enumeration. |
| m4 | OE 9 names Pete Donovan as the only near-miss customer and omits the third Castillo customer proj-e576b03e2b4c (John Castillo, john.castillo@gmail.com), which a `search_customers(query: "Castillo")` returns and which OE 1 already flags at the contacts layer. | `6_Oracle_Events.txt:17` (OE 9) | Add: "A third customer proj-e576b03e2b4c (DisplayName John Castillo, john.castillo@gmail.com) also exists, so a query on the surname alone returns two Castillos; the 4C owner is proj-4ae920b7c9e8." |
| m5 | The Tony / Tommy Reyes seam is never surfaced. Decoy invoice 340207319849 carries "412 Mesquite, Tommy Reyes unit" while being 1340.00 and billed to Linda Castillo: a triple collision (amount, owner, Reyes surname) against the 4C repaint bill, on a task whose pivotal argument turns on Tony Reyes attribution. Tommy Reyes is a real separate contact (a4c863c4d92d53a59c310bb29abd6d0c, tommy.reyes@gmail.com, Tenant). Zero occurrences of "Tommy" in the OE. | `6_Oracle_Events.txt:19` (OE 10), `:31` (OE 16) | Add to OE 10's description of 340207319849: "its line text names a Tommy Reyes unit, a different person from Tony Reyes (Lead Maintenance Technician); the surname collision is a decoy, not a link to the 4C trim work." |
| m6 | OE 21 offers `get_vendor_expenses(vendor: "Permian Make-Ready Crew", start_date: "2026-05-01", end_date: "2026-05-31")` as corroboration without warning that the window returns 12 Permian bills totalling 6,992.00, including a SECOND 1340.00 Permian bill (102111031436, B2026-418, grounds maintenance at 4821 Oleander Dr, TxnDate 2026-05-04). Following it literally can corroborate the wrong record. | `6_Oracle_Events.txt:41` (OE 21) | Add: "Note that this report returns twelve Permian bills for May including a second 1340.00 Permian bill (102111031436, grounds maintenance at 4821 Oleander Dr), so read it by unit and not by amount." |
| m7 | Undisclosed mirror decoy on the AR-line side. Bill 173322471681 (Hill Country Plumbing, INV-2026-0417, TotalAmt 1140.00, AccountRef 63 Management Fee Income, PrivateNote "Disputed Pinnacle Plumbing invoice. Internal expected amount was $1,140; vendor billed $1,380. Awaiting vendor correction or credit memo before closing.") has the same expected-versus-billed shape as the 4C repaint variance and the same account code as bill 696089964235. An agent searching bills for the AR line amount 1140 lands here. OE 16 disambiguates only the 1340.00 side. | `6_Oracle_Events.txt:31` (OE 16) | Add one sentence: "The mirror trap runs on the other amount too: bill 173322471681 (INV-2026-0417, Hill Country Plumbing) is a 1140.00 bill whose note recites an expected 1,140 against a billed 1,380 for a Riverside water line, unrelated to 4C. Bind by unit, never by amount, in either direction." |
| m8 | Convention drift. `Reference/OE_Format.md` Structure specifies "OE1: <one or two sentences describing the step>". OE 19 is 484 words / 12 sentences; OE 16 is 232 / 8; OE 22 is 227 / 7. File total is 4,167 words against the QC_Passed reference band of 1,002-1,675 and Task 41's 2,095. Council A Min-8, grew in the revision. Compounding it, OE 19's only tool anchor is a re-read of two records already retrieved in OE 17 and OE 18 that returns nothing new. | `6_Oracle_Events.txt:37` (OE 19), file-wide | Split OE 19's five grounds across OE 17 and OE 18 where each record is first opened, and keep OE 19 as the two-sentence decision step that names the discriminators and cites the three answered counter-evidence records. This also removes the cosmetic re-read. |
| m9 | OE 8 describes a88bb5b7d1eb215b as "the 4C deep clean invoice handed to tony.reyes@starpm.com for processing" without noting the base-universe oddity that the message is From carlos.mendez@starpm.com and its body says "my invoice", which reads as if Carmen Delgado wrote it. Council A Min-4, carried unfixed. | `6_Oracle_Events.txt:15` (OE 8) | Add: "note that the message is sent from Carlos's own account although its body says my invoice, so it is a hand-off record and not evidence about who the payee is." |
| m10 | Arithmetic-neighbour collision, no leak. 190.00, the net understatement, appears as a line amount on three unrelated records, one of which (618793969708, 2026-419, Pete Donovan, "Service call fee - diagnostic visit, 4408 Elmwood Ave") is a decoy OE 10 puts in front of the agent. No synthesis-free path to 1812.00 or to "net 190.00" exists, so this is not a BLOCKER, but the collision is undisclosed. | `6_Oracle_Events.txt:19` (OE 10) | Optional. If OE 10 is being edited for M3 anyway, note that 2026-419 happens to carry a 190.00 service-call line that is unrelated to the 4C variance. |

### NOTE
N1, N2, N3 as adjudicated in LENS 8.

---

## Lens status summary

| Lens | Status |
|---|---|
| LENS 1 Strict QC scoring | **REVISE** - OE Completeness 4/5, OE Accuracy 4/5 |
| LENS 2 Answer-leakage sweep | **PASS** - no BLOCKER; 1812.00 / 1897.00 / 1727.00 exist nowhere as money; synthesis across 3+ records required |
| LENS 3 Hardness end-to-end trace | **PASS on levers** - no HARDNESS_REGRESSION; all 5 trace with cited evidence. **L11 is DISPLACED** (co-located with L2's gate, zero independent observable fail) |
| LENS 4 Strict density, per model | **Opus PASS (47 intended, 39.5 blended) | Gemini THIN (41 intended, 33 blended)** - with M4 correcting the mitigation rationale and Council B's midpoint |
| LENS 5 Adversarial veteran review | **REVISE** - one prompt-framing over-reading (M2), one non-byte-exact entity name (m3), one unsurfaced entity-drift seam (m5); channel lock-in, meta-tags, hedge words, tool feasibility and page sizes all clear |
| LENS 7 Anti-Rationalization | **APPLIED** - 9 candidate rationalizations, 5 promoted to findings, 4 excluded on stated hard exclusions |
| LENS 8 Regression anchors | **PASS** - 62/62 reproduced; validate.py oe 0/0/3; verify_universe_atoms 0/0 but only 16 atoms, see M5 |

---

## Round-1 verdict

Five MAJOR and ten MINOR findings, every one fix-in-place in `6_Oracle_Events.txt` apart from M4
(Hardness_Plan note plus an S4 carry-forward) and M5 (a validator coverage gap). The spine is sound:
1812.00 is uniquely derivable and appears nowhere in the universe, all 71 audited atoms are byte-exact,
all 25 tools and every parameter name are correct, all four writes are covered with tools and key
parameters, the act-vs-defer gate passes, and no lever regressed. That rules out REBUILD. But both
Oracle Event sub-dims sit at 4 under the strictest reading, and a 4 is a soft fail.

`PROPAGATE TO S1`: **NOT EMITTED.** The pivotal exclusion is adequately grounded in the prompt's own
carve-out language, and M2 is an OE over-reading to be repaired in the OE.

**ROUND-1 VERDICT: REVISE** (superseded by round 2 below).

---
---

# ROUND 2 - re-verification after coordinator fixes

`6_Oracle_Events.txt` re-read fresh, 28 steps, 4,529 words. Every fix re-verified from
`_aux/Universe_Split/` with `python3`. I did not accept any fix on the coordinator's description of it.

## Fix verification

| # | Round-1 finding | Fix as applied | Independent re-verification | Status |
|---|---|---|---|---|
| **M1** | OE 22's queries could not return ts 1779501872.000004 | The Jaime post is REMOVED from OE 22's enumeration. OE 22 lists only the five Carlos posts that name the unit and states a keyword search will not surface the sixth because its text names neither unit nor property. OE 23 is now where it surfaces, quoted and attributed | **CORRECT, and the reasoning is exactly right.** Token audit of all six: ts ...872 has `4C:N Mesa:N Vista:N` - the OE's stated reason is byte-true. All five listed posts contain "4C" and all five are authored by U07E4512181. A simulated AND-of-tokens query on `"4C"` returns **exactly those five and nothing else workspace-wide** (5 hits, all C004). `slack_read_channel(channel_id: "C004")` reaches ts ...872: re-confirmed against Task 40 Opus run 1's real tool_result, which returned 96 of C004's 144 rows (the 48 `is_activity_message: true` rows filtered) including all six ts values. OE 23's quote is byte-identical to the record and the U2CD1BC03B2 attribution is correct | **RESOLVED** (one residual, R2-a) |
| **M2** | OE 24 attributed a credit-memo foreclosure to the prompt and justified it with "double-bill" | `create_invoice` is now what the prompt forecloses (a second owner invoice would double-bill); the credit memo is separately excluded because it reduces a receivable while this correction must raise one from 1622.00 to 1812.00 | **CORRECT.** The prompt says "I do not want a second bill created next to the one she already has", which a second owner invoice is. The credit-memo ground is now the direction of the variance, which is a fact, not a prompt reading: 1622.00 to 1812.00 is an increase | **RESOLVED** |
| **M3** | OE 10's decoys did not match its queries; invoice 310712648304 and the 1810.00 wrong figure were absent | Decoy inventory rebuilt by query. 310712648304 added and named the closest trap; Pete Donovan receivables re-attributed to a broader search; 1810.00 added to OE 21 | **CORRECT, and more precise than I asked for.** Re-derived all six Linda Castillo invoices: exactly the two named decoys (310712648304, 340207319849) share 2026-534's TxnDate 2026-05-01 AND DueDate 2026-05-31, while the other three do not, so "both sharing" is a true discriminator rather than a gloss. 310712648304 = DocNumber 2547, TotalAmt 385.00, line "Pass-through: A Plus Carpet Cleaning & Repairs - deep-clean and seam re-stretch, Rio Bend unit" - byte-exact. 385 + 1340 + 85 = 1810 recomputed. The three Pete Donovan receivables are correctly no longer attributed to an owner-name query | **RESOLVED** |
| **M4** | THIN mitigation invalid on the modal branch; Council B's Opus 46 over-credited | Recorded in `_aux/Reasoning/OE_solvability.md` as a documentation correction plus S4 carry-forward; OE 19's cosmetic `get-bill` re-reads removed so the +2 credit is gone | **CORRECT.** Read the file: it carries my per-model table verbatim (Opus 47 / 38 / 39.5 PASS, Gemini 41 / 31 / 32.7 THIN), states the plan's uniform minus-9.5 Gemini delta does not hold empirically with Task 40's delta at 1.5, flags "writes execute on BOTH models" as failing on the modal branch, and sets the actionable Gemini threshold below 24. OE 19 confirmed to contain no `Use` imperative, so the re-reads are gone | **RESOLVED** (introduces R2-b) |
| **M5** | Atom-verifier PASS covers 16 atoms and cannot reach the load-bearing ids | Recorded as a discrepancy in `_aux/Verification_s2.md`; flagged to the operator as a Fact_Ledger builder gap; deliberately not patched mid-task to protect the frozen regression baseline | **CORRECT, and the not-patching call is right.** The record states the gap accurately (16 atoms = 5 Airtable ids + 11 emails; no pattern for 12-digit QB entity ids or Slack ts; `ids.invoice` holds DocNumbers so all five 4C ids are absent; `entities` empty; `lifecycle.today` null) and does not cite the PASS as coverage. Touching the extractor mid-task would move the 62-anchor baseline, which is the correct trade | **RESOLVED as documented** |
| m1 | OE 13 self-contradiction | "No other vendor bill in the ledger touches 4C, and the only receivable that does is 2026-534 itself" | Exactly the prescribed wording; consistent with OE 10 and OE 11 | **RESOLVED** |
| m2 | OE 15 false absolute | Rescoped to the 4C repaint cost, Slack confirmed clean, both Gmail messages named | Re-verified: 4a20c7c433db278a is "His current rate is $1,340 per month" (a rent rate) and 6f2669a41401485a is "The invoice total is $1,340" on a Reyes Plumbing invoice. Slack sweep for 1340 and 1,340 across all 580 messages: 0 hits | **RESOLVED** |
| m3 | "A Plus Carpet Cleaning and Repairs" | Ampersand form used | `"Cleaning and Repairs"` now occurs 0 times; `"A Plus Carpet Cleaning & Repairs"` occurs 3 times | **RESOLVED** |
| m4 | John Castillo customer omitted | proj-e576b03e2b4c added to OE 9 | Verified: a surname query returns exactly two Castillos (Linda proj-4ae920b7c9e8, John proj-e576b03e2b4c) | **RESOLVED** |
| m5 | Tommy Reyes seam unsurfaced | Added to OE 10 as a tenant and a decoy | Verified: contact a4c863c4d92d53a59c310bb29abd6d0c, tommy.reyes@gmail.com, job "Tenant"; the string sits on 340207319849's line text | **RESOLVED** |
| m6 | Permian window warning absent | Twelve bills, 6992.00, the second 1340.00, plus 167365280749 and 358082173277 | **All four numbers exact.** Permian bills with TxnDate in 2026-05: count 12, sum 6992.00 recomputed. 167365280749 = "Interior paint touch-up, Cascade Hills Dr Unit 7C - walls and trim" 610.00; 358082173277 = "Drywall patch and paint touch-up, Elm Street unit 3" 310.00; 102111031436 = 1340.00 grounds maintenance 4821 Oleander Dr | **RESOLVED** |
| m7 | 1140.00 mirror decoy undisclosed | bill 173322471681 added to OE 16 | Every detail exact: INV-2026-0417, Hill Country Plumbing (201), TotalAmt 1140.00, AccountRef "Management Fee Income" (63) which is indeed the same code bill 696089964235 carries, note "Internal expected amount was $1,140; vendor billed $1,380", line "Plumbing repair - water line replacement, Riverside Portfolio Building B" | **RESOLVED** |
| m8 | Verbosity and OE 19's cosmetic anchor | Restructured as prescribed: three discriminators moved into OE 17 and OE 18; OE 19 cut 484 to 257 words; OE 16 edited. File grew 4,167 to 4,529 words | Restructure confirmed by per-step measurement: OE 17 164 to 248, OE 18 150 to 240, OE 19 484 to 257. See my judgment below - **I withdraw the verbosity finding** | **PARTIALLY RESOLVED, finding withdrawn** (introduces R2-b) |
| m9 | OE 8's "my invoice" oddity | Noted in OE 8 | Present and accurate | **RESOLVED** |
| m10 | 190.00 line on 2026-419 | Noted in OE 10 | Present and accurate | **RESOLVED** |

All five Majors and all ten Minors are discharged. Nothing was fixed by weakening a claim that was true,
and nothing was fixed by deleting a fact: the only removal is ts 1779501872.000004 from OE 22's search
enumeration, and that record now appears in OE 23 with a fuller treatment than it had before.

## Round-2 LENS 1 re-score

```
SUB-DIM OE Completeness -> SCORE 5/5 -> REASON Nothing is missing. Every discovery step, the dependency
  chain and all four write actions are present with tools and key parameters, and all three round-1
  completeness gaps are closed: the sixth C004 message now has a correct discovery home (OE 23), the
  closest decoy 310712648304 and its 1810.00 consequence are in the inventory and the wrong-figure
  catalog, and the 1140.00 mirror decoy 173322471681 is disclosed. The QC spec's Completeness Non-Fail
  band is defined as "OEs are missing critical steps needed to solve the task", and after re-deriving the
  full critical path against the prompt's twelve asks I found no step missing.
  WHAT THE PRIOR COUNCIL MISSED (round 1, now closed): both councils verified that the enumerated atoms
  EXISTED and never asked whether the step's own query parameters retrieved them, and neither swept for a
  decoy closer than the ones already listed. The round-2 text closes both.

SUB-DIM OE Accuracy -> SCORE 5/5 -> REASON Every tool, service, parameter and expected value matches the
  universe, and following the OE list literally now produces a correct trajectory including the record
  that round 1 left unreachable. Re-verified this round: 25 catalog tools with the only non-catalog
  snake_case tokens being four genuine parameter names (channel_id, contact_id, end_date, invoice_id);
  the six Linda Castillo invoices with the shared-date discriminator; the 12-bill / 6992.00 Permian
  window; bill 173322471681 in full; both Gmail 1,340 messages; the ampersand entity name; the two-Castillo
  customer claim; the 385 / 1340 / 85 = 1810 arithmetic; and the byte-identity of OE 23's Slack quote and
  its U2CD1BC03B2 attribution. The four round-1 accuracy defects (the unretrievable enumeration, the
  prompt misattribution, the query-decoy mismatch, the OE 13 self-contradiction) are all gone, and the
  OE 15 absolute is now correctly bounded with its two counterexamples named.
  WHAT THE PRIOR COUNCIL MISSED (round 1, now closed): Council B praised OE 24's credit-memo clause as a
  strengthening without testing it against the prompt sentence. The clause is now grounded on the
  direction of the variance instead, which is a ledger fact.
```

Both sub-dims are at 5. Two residuals are logged below; neither meets either sub-dimension's Non-Fail
band as that band is written in `Docs_starpm/7_QC_Spec_Doc1.json`, and I state the reasoning explicitly
so it can be checked rather than trusted.

## Round-2 residuals

**[MINOR] R2-a - two of OE 22's three query alternatives do not return the five posts the step
enumerates.** `6_Oracle_Events.txt:43` (OE 22).
Simulated AND-of-tokens against all 580 Slack messages: `"4C"` returns exactly the five listed posts and
nothing else workspace-wide, which is a clean match. `"Mesa Vista 4C"` returns only three of the five
(ts ...868, ...870, ...871; ts ...869 and ...873 carry the unit token without the property name).
`"make-ready"` is worse: 20 messages contain the token workspace-wide of which only three are in the 4C
sequence, and empirically the harness does not even return them - Task 40's Opus runs 1 through 6 each
issued `slack_search_public_and_private(query: "make-ready")` and received a channels-only result block
with no Messages section at all, because the query matches the channel name.
*Why this does not hold Accuracy below 5:* `Reference/OE_Format.md`, section "Discovery-step phrasing",
establishes the multi-alternative query menu as the sanctioned convention and its own worked example
offers three query strings that plainly do not return identical result sets. The OE never claims each
alternative returns the same five; it names three plausible strings an agent might pass, and the QC spec's
Pass(5) test is "Following the OEs literally would produce a correct trajectory", which OE 22 followed by
OE 23 does under any of the three. That is a hard exclusion grounded in the controlling convention, not a
judgement call. Logged anyway per the Anti-Rationalization Rule.
*Exact fix (one line, and it shortens the step):* change the parameter to
`query: "4C"` or `"Mesa Vista 4C"`, drop `"make-ready"`, and add "a query on "make-ready" matches the
channel name rather than message text and returns no messages, and a query on "Mesa Vista 4C" returns
only the three posts that carry the full property name."

**[MINOR] R2-b - OE 19 is now a pure reasoning step with no tool call of its own, which is an
anti-pattern the OE eval spec names explicitly. This is a regression introduced by my own round-1
prescription and I own it.** `6_Oracle_Events.txt:37` (OE 19).
Round 1 I flagged OE 19's `get-bill` re-reads as a cosmetic anchor and prescribed "keep OE 19 as the
two-sentence decision step". The coordinator did exactly that, and the result is a step whose only tool
reference is the back-reference "already returned by the get-bill calls in OE 17 and OE 18". Confirmed
mechanically: OE 19 contains no `Use` imperative. `Evals_starpm/2_OE_Eval.md` Phase 1.1 says "Reasoning -
Agent performs deduction with NO tool call -> FLAG THIS (not an OE step)", its Phase 1.2 anti-pattern
table lists "Pure reasoning step" with the fix "Fold into the relevant lookup OE", and its Quick
Reference table classifies "Reasoning without tool" as Non-Fail (Completeness). My round-1 prescription
was underspecified and this is the cost of it.
*Why this does not hold Completeness below 5:* the QC spec is the scoring authority, and its Completeness
Non-Fail band is defined solely as "OEs are missing critical steps needed to solve the task". A tool-less
step does not remove a step; it adds a non-step. Nothing on the critical path is missing, and the eval
spec itself states that OE issues "are NON-FAIL only - they cannot fail a task by themselves". Hard
exclusion cited; logged anyway.
*Exact fix, which satisfies both constraints at once and loses no content:* dissolve OE 19. Its decision
sentence ("keep the 85.00 closet trim on the owner side and keep the 85.00 internal walk off it", plus
the account-ground caveat) belongs as the closing two sentences of OE 18, which is already the step where
the excluded bill is opened and where three grounds already sit. Its counter-evidence answer already has
two tool-anchored homes: the "Internal labor charge on both bills" fact is in OE 18, the Airtable
"routed to Tony Reyes" note surfaces in OE 4, and the Jaime post surfaces in OE 23, which already carries
the sentence "That post is the third record attributing the trim fix to Tony Reyes". Renumber 20 to 28
as 19 to 27. No tool call is duplicated and no tool-less step remains.

## Round-2 m8 judgment: I withdraw the verbosity finding

The coordinator's read is correct and I am reversing myself on this one. Reasons, in order of weight:

1. **My own accuracy findings caused the growth.** M3, m2, m5, m6 and m7 all demanded more grounding,
   and the added text is roughly 500 words of verified universe fact. Penalising the file for carrying
   fixes I demanded would be incoherent.
2. **The convention is thinner than I treated it as.** `Reference/OE_Format.md` sets no word budget. The
   "one or two sentences" phrasing appears in a schematic Structure illustration, and the same document's
   own worked examples run longer. `Reference/OE_Convention_Inventory.json` records no word statistic at
   all, only a step-count distribution, and 28 steps sits inside it (Task13 = 28).
3. **The reference band is the wrong yardstick.** 1,002 to 1,675 words is drawn from four V3 Brookfield
   sample tasks. This task carries a ten-bill amount cluster, twin same-amount bills on one unit, three
   same-surname customers, two same-owner same-date decoy invoices and a mirror variance bill. There is
   no honest way to disclose that decoy surface inside 1,675 words.
4. **No validator gates it, and the downstream consumer is S3.** `validate.py --phase oe` is clean at
   0/0/3 with the step count as an informational note only. Rubric accuracy is what the words buy.

The restructure I did ask for was executed and did what it was for: OE 19 dropped 484 to 257 words and
the discriminators now sit in OE 17 and OE 18 where each record is first opened, which is better for S3
than the monolith was regardless of the total.

**If forced to cut, these are the specific clauses I would cut, and only these.** They total roughly 250
words, which lands the file near 4,280 and still nowhere near the reference band, which is itself the
proof that the band is not the right target: (a) OE 22's `"make-ready"` alternative and its clause, which
R2-a removes anyway; (b) OE 1's closing "Carlos Mendez (carlos.mendez@starpm.com) is the acting persona",
which duplicates `2_Persona.txt`; (c) OE 6's two-clause explanation of why the narrower and broader
queries behave differently, keeping only the pool-pump exclusion; (d) OE 20's final sentence, which
restates OE 19's conclusion rather than adding a payee fact; (e) roughly half of OE 28, whose figure
catalog duplicates OE 21 and whose write recitals duplicate OE 24 through OE 27, keeping only the facts
that appear nowhere else. I would not cut any decoy id, amount, date, account code or quoted note.

## Round-2 LENS 2 re-check on the newly added figures

Swept for 1810, 1,810, 1380, 1,380, 6992, 6,992, 385 and 1140 across every file in
`_aux/Universe_Split/` with Gmail bodies base64-decoded, then re-ran the numeric sweep over every
`TotalAmt`, `Balance` and `Line[].Amount` in all 625 QuickBooks entities.

| Figure | Result |
|---|---|
| 1810.00 | **0** TotalAmt / Balance / Line-amount hits. The four raw string hits are id and header substrings: gmail message id `ab81ee44**1810**74` and its Message-ID header, slack message id `80c504ecc4a352**61810**e139f19ce495c` and the thread_parent_id that repeats it, quickbooks estimate id `5351731**810**03`. Exactly one record in 625 contains the digit run at all, and it is an id |
| 1380.00 | **0** amount hits. The only human-readable occurrence is the intentional `"vendor billed $1,380"` inside bill 173322471681's PrivateNote, which OE 16 now discloses by design. Remaining hits are ids (`198110713800`, `223138034361`), an Airtable record id (`rec1380f41ec09a51`) and two Linear uuids |
| 6992.00 | **0** hits of any kind. It is a report total the agent computes, stated nowhere |
| 385.00 | Present as intended on invoice 310712648304, now disclosed as the closest decoy. Other 385 hits are unrelated amounts and id substrings |
| 1140.00 | Present on invoice 445653930748 line 2 and on bill 173322471681, both disclosed |
| Re-confirmed | 1812.00, 1897.00, 1727.00: **0** TotalAmt / Balance / Line-amount hits across all 625 entities |

**No new leakage vector opened. LENS 2 remains PASS with no BLOCKER.** The synthesis requirement is
unchanged: no single record contains 387, 1340 and 85 together, and the round-2 additions are all decoy
disclosures rather than new statements of the answer.

## Round-2 LENS 5 re-run

| Check | Round-2 result |
|---|---|
| Implicit framing preserved, no smuggled explicitness | **CLEAR.** The round-1 violation is gone. OE 24 now attributes to the prompt only what the prompt says (a second owner invoice), and OE 18's quotation of "internal walk or a condition check" is a byte-exact substring of the prompt sentence |
| Entity-drift seams | **CLEAR.** Tommy Reyes now surfaced in OE 10 with the correct role (Tenant) and the correct adjudication (surname collision, not a link to the trim work). Linda / Pete / John Castillo covered at both the contacts layer (OE 1) and the customer layer (OE 9). Permian Make-Ready Crew versus Pete Donovan Painting handled in OE 15, with both strings verified present in the universe |
| Single-channel lock-in | **CLEAR.** OE 27 unchanged: C005 and C006 admitted, graded on the corrected figure and the supersession |
| "Approximately" and hedges near ids, dates, amounts | **CLEAR.** Zero occurrences of approximately, approx, roughly. The three "about" hits are ordinary prose ("about who the payee is", "about who executed the repair", "about who is billed for it"), none near a value |
| "(or similar)" near values that must be exact | **CLEAR.** Zero occurrences |
| OE meta-tags | **CLEAR.** No lever ids, no rubric references, no "Hardness", no "stump", no severity tags, no markdown. Pure ASCII, 28 steps, sequential 1 to 28 |
| Pure-reasoning step with no tool anchor | **ONE: OE 19** - finding R2-b. OE 28 remains sanctioned by the OE_Format final-paragraph convention |
| Count, id or quoted string not byte-for-byte | **CLEAR.** The round-1 ampersand defect is fixed (`"Cleaning and Repairs"` now 0 occurrences). Everything re-checked this round is byte-exact, including the 12-bill / 6992.00 Permian window, bill 173322471681's five attributes, the shared TxnDate and DueDate on both named decoys, OE 23's Slack quote, and the 1810.00 arithmetic |
| Instruction impossible on the real harness | **CLEAR.** 25 catalog tools referenced; the only non-catalog snake_case tokens in the file are `channel_id`, `contact_id`, `end_date` and `invoice_id`, all genuine parameter names. No new tool was introduced by the revision. OE 23's channel read is empirically proven to return the record it now claims |
| Page size too small for the claimed result | **CLEAR.** OE 16's pagination handling is intact and its softened claim holds (bill 696089964235 sits at file-order index 101 of 113, beyond a 50-row page). OE 23 empirically clears at 96 of 144 rows returned with all six 4C messages present |

**LENS 5 round-2: PASS**, with R2-b as the one logged residual.

## Round-2 LENS 8

Re-run after the revision, all three identical to round 1: `test_regression_anchors.py` **62 passed, 0
failed out of 62**; `validate.py --phase oe` **PASS, 0 fails, 0 warns, 3 notes** (same three notes, same
adjudication); `verify_universe_atoms.py` **PASS, 0 fails, 0 warns, 16 atoms** (coverage gap unchanged
and now documented in `_aux/Verification_s2.md` per M5). The revision moved no baseline.

## Round-2 LENS 7 self-scan

Four "I considered flagging X but decided it is fine because" lines this round. Two promoted, two excluded
with hard exclusions stated in place above.

- Promoted: the OE 22 query-alternative residual, promoted to **R2-a** even though the OE_Format menu
  convention excuses the "or" form, because the `"make-ready"` alternative empirically returns no
  messages at all and that is worth an operator's eye.
- Promoted: the tool-less OE 19, promoted to **R2-b** even though it descends from my own round-1
  prescription, because self-inflicted defects still count and the eval spec names the anti-pattern.
- Excluded: "OE 10 says a Linda Castillo query surfaces two decoys, but the query actually returns six
  invoices." **HARD EXCLUSION:** re-derived all six. 247748966591 is separately named in OE 12; the
  remaining two are 643035627727 (1091, 295.00, Hartwell payment-plan admin fee) and 833723847278
  (2255, 365.00, monthly management fee at 99 Sycamore Lane), neither a pass-through, a deep clean or a
  repaint, and neither within 20.00 of any 4C figure. The OE does not claim "only two", and the two it
  names are precisely the two that share 2026-534's TxnDate and DueDate. Not a gap.
- Excluded: "OE 16's claim that a 50-row page would miss the repaint bill is server-order-dependent."
  **HARD EXCLUSION:** the claim was already softened from "cannot reach them all" to "would miss", the
  bill sits at file-order index 101 of 113, and OE 16 offers `max_results: 200` and `start_position`
  paging as the actual instruction. Not an inaccuracy.

## Round-2 verdict rationale

The state has changed in kind, not just in degree. Round 1's four accuracy defects were false statements
about the universe or the prompt (a step claiming a return it could not produce, a foreclosure the prompt
does not contain, a decoy set its queries do not return, a sentence contradicting two earlier steps), and
its completeness gap was a genuinely missing decoy that left a reachable wrong answer uncatalogued. Every
one of those is now byte-verified correct, and the fixes were made by adding verified fact rather than by
softening claims. What remains is one suboptimal query alternative inside a convention-sanctioned menu
and one step that reasons over data already retrieved. Neither is a false claim about anything, and
neither removes a step from the critical path, so neither satisfies the Non-Fail band as
`Docs_starpm/7_QC_Spec_Doc1.json` defines it for either sub-dimension. Both residuals are worth folding
in on the next touch and neither is a reason to hold S3.

Levers unchanged and unregressed, with L6 and L11 measurably deeper than at round 1 (three new grounded
decoys and a fourth catalogued wrong figure). L11 remains DISPLACED and `OE_solvability.md` now records
that so S4 will not double-count it. Density bands unchanged: Opus 47 intended / 39.5 blended, Gemini 41
intended / 32.7 blended. LENS 2 clean on the new figures. No Major remains.

`PROPAGATE TO S1`: **NOT EMITTED** (unchanged from round 1).

PASS (STRICT)
