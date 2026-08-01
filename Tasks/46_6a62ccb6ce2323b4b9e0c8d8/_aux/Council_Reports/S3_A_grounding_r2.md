# S3 Council A (Grounding) - ROUND 2

Task: Tasks/46_6a62ccb6ce2323b4b9e0c8d8
Universe: StarPM (V4), universe today 2026-07-01 America/Chicago
Artifact: 7_Rubrics.json, 32 criteria
Source of truth: _aux/Universe_Split/ (34 service files, read directly, row_data json.loads per row)
Round 1 verdict: BLOCK (2 blockers). This round re-verifies every concrete value from scratch.

Method: every value below was resolved against the split independently. The rubric `justification`
field was NOT used as a source at any point. Titles were swept first at full priority, then
`evidence` and `justification` at lower priority.

---

## (a) VALUE TABLE

Legend: Y = grounded, D = derived (re-computed in section (c)), N = not grounded.

| idx | value | field | grounded? | where found |
|---|---|---|---|---|
| 1 | Sunset Ridge 104B | title | Y | airtable tblMakeReady rec98bdfeec73545e, rec7d202aed68c95c (fldUnit) |
| 1 | Scheduled (turn status) | title | Y | fldTurnStatus choice selSched, airtable_fields tblMakeReady |
| 1 | In Progress (turn status) | title | Y | fldTurnStatus choice selProg |
| 1 | 104B row that still reads Scheduled | title | Y | rec98bdfeec73545e = selSched; the only Sunset Ridge 104B row at Scheduled (other is rec7d202aed68c95c selProg). Single target holds. |
| 2 | Sunset Ridge 309C | title | Y | rec987aae7d522057, reca06d89f1a4ac5b, rec2471fac3f9ae51, recf50eb955a10651 |
| 2 | deep-clean crew availability unanswered | title | Y | rec987aae7d522057 fldNotes2: "Alicia to confirm whether deep-clean crew is available July 21 or if we need to push to July 23. Awaiting her input". Unique: recf50eb955a10651 has it ANSWERED ("Alicia confirmed deep-clean crew available July 21"), reca06d89f1a4ac5b is the utility-transfer row. Single target holds. |
| 3 | Ridgeview roof section | title | Y | rec8b679d92f30753 fldUnit "Ridgeview - Roof Section (Common/Structural)", selSched. Only Ridgeview row. |
| 4 | Harry Harris | title | Y | qb customer proj-e6adffd68bf9 DisplayName "Harry Harris"; sole match, no name collision across 40 customers |
| 4 | Mid-Year Portfolio Review | title | Y | gcalendar summary "Harry Harris Mid-Year Portfolio Review" |
| 4 | June 2, 2026 | title | Y | base 1pon50ds1aevem63td6f7emdn3, start_dt 2026-06-02T12:15:00-05:00, status confirmed |
| 4 | June 3, 2026 | title | Y | base qqbwq3s2h7wh5udoek2940mffk, "(Rescheduled)", start_dt 2026-06-03T15:00:00-05:00, status confirmed |
| 5 | Robert Finley | title | Y | qb customer proj-e59d4a436ed7 DisplayName "Robert Finley"; sole match |
| 5 | May 19, 2026 | title | Y | base 8mwlxrq5w5oodwdpmvo83e00f2 "Robert Finley Mid-Year Portfolio Review", start_dt 2026-05-19T11:45:00-05:00, confirmed. Only Finley review event. |
| 6 | brooke.phillips@starpm.com | title | Y | contacts.contacts c46d47256fd95ca6aca770c8dddda5eb, Brooke Phillips, Apartment Property Supervisor, is_user true |
| 7 | Ready (turn status) | title | Y | fldTurnStatus choice selReady |
| 7 | no Sunset Ridge record has reached Ready | title | Y | 7 of 7 Sunset Ridge rows, Ready count = 0. Full enumeration in section (d). |
| 8 | $0.00 Harris open receivable | title | D | 3 Harris invoices, all Balance 0.0. Sum = 0. See (c). |
| 9 | $1,975.00 Harris credit memos | title | D | 195.0 + 1250.0 + 530.0, all Balance == TotalAmt (unapplied). See (c). |
| 9 | not applied against anything | title | Y | all 3 Harris credit memos carry Balance equal to TotalAmt |
| 10 | $10,980.00 Finley past due | title | D | 8400.0 + 2190.0 + 390.0, all three DueDate < 2026-07-01. See (c). |
| 11 | $3,655.00 Finley credit memos | title | D | 2755.0 + 490.0 + 410.0, all Balance == TotalAmt. See (c). |
| 12 | MT-2026-047 | title | Y | airtable tblMaintenanceTickets recb4aeaed326f156 fldTicketNumber |
| 12 | roof damage on the Finley portfolio | title | Y | same row fldDescription verbatim: "Top-floor unit at Finley portfolio property showing missing shingles and interior ceiling water staining" |
| 12 | still open | title | Y | recb4aeaed326f156 fldCompletionDate = "" (empty). One of only 7 open tickets. |
| 13 | 94% occupancy | title | Y | slack C006 msg a6779a055eaf5fb1893d0ed6d92e3b39, Lisa Smith. Verbatim quote in section (d). |
| 13 | Mesa Vista portfolio | title | Y | same message scopes the figure to "Robert's Mesa Vista portfolio" |
| 14 | 97% collections | title | Y | same message, "Collections at 97%". Sole occurrence of "97%" in all 34 split files. |
| 15 | more than one Mesa Vista unit in a turn | title | Y | 4 distinct Mesa Vista units in tblMakeReady: 107A, 207A, 310C, 4C. 107A (In Progress x2) and 310C (Scheduled) have no competing Ready row. |
| 16 | closed water heater work | title | Y | MT-2026-1280 Pinecrest 12, fldCompletionDate 2026-05-11; and make-ready recca0da8f7416f51 "412 Mesquite Kitchen" selReady, "Ticket closed out as Completed" |
| 16 | property outside both owners' portfolios | title | Y | 412 Mesquite is Linda Castillo's: gmail 5b8b95b55b893525, Brooke Phillips to linda.castillo@gmail.com, "both repairs at your 412 Mesquite property". Castillo is a distinct owner per OPS-10. Neither "412 Mesquite" nor "Pinecrest" co-occurs with Harris or Finley in any row of any file. |
| 17 | no late payment cleared for either owner | title | Y | every paid Harris/Finley invoice was paid BEFORE its due date. Full timing table in (c). |
| 18 | OPS-10 | title | Y | linear_issues OPS-10, title "Mid-Year Owner Portfolio Reviews - June 2026", team_001, proj_002 |
| 18 | mid-year owner review issue | title | Y | OPS-10 title and description |
| 19 | Harris and Finley half of the mid-year review | title | Y | OPS-10 description names exactly four owners: "Harry Harris, David Shea, Linda Castillo, and Robert Finley". Harris + Finley = 2 of 4. |
| 20 | Operations team | title | Y | linear_teams team_001, name "Operations", key "OPS" |
| 20 | Mesa Vista 310C subfloor assessment | title | Y | rec88734a4fdfde57 fldNotes2: "Maintenance flagged possible subfloor issue under bathroom tile - needs assessment before scope is finalized". Only Mesa Vista 310C row. |
| 20 | Sunset Ridge 309C utility transfer confirmation | title | Y | reca06d89f1a4ac5b fldNotes2: "Waiting on final utility transfer confirmation before scheduling vendor access". Unique among the four 309C rows. |
| 21 | C006 | title | Y | slack_channels C006 |
| 21 | #owner-relations | title | Y | slack_channels C006 name "owner-relations", 21 members |
| 22 | Harry Harris, Robert Finley | title | Y | as idx 4, 5 |
| 23 | $10,980.00 | title | D | same derivation as idx 10 |
| 24 | both accept-set items | title | Y | as idx 20 |
| 25 | 94% | title | Y | as idx 13. See ADVISORY A1. |
| 26 | MT-2026-047 only open ticket in either owner's scope | title | Y | 7 open tickets total; only MT-2026-047 names Finley or Harris. Full enumeration in (d). See ADVISORY A2. |
| 27 | every Sunset Ridge turn at Scheduled or In Progress | title | Y | 7 of 7 rows, enumerated in (d). Ready count 0. |
| 28 | Mesa Vista more than one unit in a turn | title | Y | as idx 15 |
| 28 | single unit given in the spring read | title | Y | Lisa Smith message: "one unit still in make-ready targeting early June" |
| 29 | $10,980.00 open receivable | title | D | identical to past-due total because the only Finley invoice with Balance 0 is 5848 |
| 30 | credit memos unapplied on both accounts | title | Y | all 6 credit memos (3 Harris, 3 Finley) carry Balance == TotalAmt |
| 31 | Harris carries no open receivable | title | D | as idx 8 |
| 32 | two live Harris meetings, June 2 and June 3, 2026 | title | Y | both bases status confirmed, neither cancelled. 9 invitee rows total, all confirmed. |
| e/j | $7,325.00 (decoy in c10 evidence) | evidence | D | 10980.00 - 3655.00 = 7325.00. Arithmetic correct. |
| e/j | invoice 445653930748, $1,622.00, Linda Castillo (decoy in c10 evidence) | evidence | Y | qb invoice 445653930748, DocNumber 2026-534, CustomerRef Linda Castillo, TotalAmt 1622.0, Balance 1622.0, DueDate 2026-05-31. Lines are Mesa Vista Unit 4C pass-throughs. Correctly attributed. |
| e/j | teresa.wood@starpm.com, brooke.phillips@starpm.com hold June 3 rows (c4 evidence) | evidence | Y | June 3 rows sit on patricia.nguyen, aurora.winona, teresa.wood, brooke.phillips calendars, all confirmed |
| e/j | Lisa Smith holds no row on the June 3 event (c4 evidence) | evidence | Y | June 2 has 5 rows including lisa.smith@starpm.com (suffix b0504ab4); June 3 has 4 rows and no lisa.smith row. Claim verified exactly. |
| e/j | 412 Mesquite and Pinecrest 12 (c16 justification) | justification | Y | recca0da8f7416f51; MT-2026-1280 / MT-2026-1317 |
| e/j | $8,400.00, $2,190.00, $390.00 (c10 justification) | justification | Y | qb invoices 2026-494, 2026-303, 4421 |
| e/j | universe today 2026-07-01 (c10 justification) | justification | Y | registry value for StarPM; consistent with qb created_time 2026-07-01T14:00:00Z across entities |

Token sweep of `evidence` and `justification`: every rec id, OPS id, ticket number, channel id,
email, percentage and DocNumber appearing in those fields resolves verbatim in the split. The only
two tokens absent from the split are `$10,980.00` and `$3,655.00`, which are derived sums and are
expected to be absent. No em-dash or en-dash characters anywhere in the file (0 and 0).

---

## (b) BLOCKERS

None. Zero blockers.

Both round-1 blockers are resolved and no new ungrounded value was found in any title.

---

## (c) DERIVED VALUES, RE-DERIVED INDEPENDENTLY

Re-computed from qb entities by CustomerRef.name, without reading any rubric justification.

### $10,980.00 (Robert Finley, past due and open receivable)

| DocNumber | TotalAmt | Balance | TxnDate | DueDate | past due vs 2026-07-01 |
|---|---|---|---|---|---|
| 2026-494 | 8400.00 | 8400.00 | 2026-05-01 | 2026-05-31 | yes |
| 2026-303 | 2190.00 | 2190.00 | 2026-05-06 | 2026-06-05 | yes |
| 4421 | 390.00 | 390.00 | 2026-05-13 | 2026-06-12 | yes |
| 5848 | 640.00 | 0.00 | 2026-05-20 | 2026-06-19 | paid, excluded |

8400.00 + 2190.00 + 390.00 = 10980.00. Confirmed.
Past-due total and open-receivable total coincide because the only zero-balance Finley invoice is 5848.
This makes criteria 10 and 29 numerically identical by construction, which is a fact about the ledger,
not a defect in either value.

### $3,655.00 (Robert Finley, unapplied credit memos)

| DocNumber | TotalAmt | Balance | TxnDate | unapplied? |
|---|---|---|---|---|
| 2026-B-317 | 2755.00 | 2755.00 | 2026-05-07 | yes |
| INV-2026-0718 | 490.00 | 490.00 | 2026-05-16 | yes |
| BILL-2026-0335 | 410.00 | 410.00 | 2026-05-23 | yes |

2755.00 + 490.00 + 410.00 = 3655.00. Confirmed. Balance equals TotalAmt on all three, so none is
applied against any invoice, and none reduces the 10980.00.

### $1,975.00 (Harry Harris, unapplied credit memos)

| DocNumber | TotalAmt | Balance | TxnDate | unapplied? |
|---|---|---|---|---|
| 2026-CM-089 | 195.00 | 195.00 | 2026-05-08 | yes |
| INV-2026-0841-572 | 1250.00 | 1250.00 | 2026-05-16 | yes |
| BILL-2026-0336 | 530.00 | 530.00 | 2026-05-23 | yes |

195.00 + 1250.00 + 530.00 = 1975.00. Confirmed.

### $0.00 (Harry Harris, open receivable) and the late-payment claim

| DocNumber | TotalAmt | Balance | DueDate | payment date | paid before due? |
|---|---|---|---|---|---|
| B2026-086 | 510.00 | 0.00 | 2026-06-05 | 2026-05-18 | yes, 18 days early |
| 4422 | 60.00 | 0.00 | 2026-06-12 | 2026-05-20 | yes, 23 days early |
| 2026-057 | 1345.00 | 0.00 | 2026-06-19 | 2026-05-30 | yes, 20 days early |
| 5848 (Finley) | 640.00 | 0.00 | 2026-06-19 | 2026-05-29 | yes, 21 days early |

Harris open receivable = 0.00. Confirmed.
Every settled invoice on both accounts was paid before its due date, and every unpaid invoice is
still unpaid. There is no instance anywhere in the ledger of a payment arriving after a due date and
then clearing. Criterion 17 is grounded at the ledger level.

---

## (d) CHANGED CRITERIA, ROUND 1 TO ROUND 2

### 1. Criterion 7 title, Harris attribution dropped

Now reads: "The Agent states in the draft to Brooke Phillips that no Sunset Ridge make-ready record
has reached a Ready turn status."

Grounded. No ownership relation asserted. Ready count across Sunset Ridge is 0 (table below).

### 2. Criterion 27 title, Harris attribution dropped

Now reads: "The Agent reports that every Sunset Ridge turn is still at Scheduled or In Progress."

EXACTLY TRUE across all 7 rows. Required enumeration:

| row id | fldUnit | fldTurnStatus | resolved name |
|---|---|---|---|
| rec2471fac3f9ae51 | Sunset Ridge 309C | selProg | In Progress |
| rec7d202aed68c95c | Sunset Ridge 104B | selProg | In Progress |
| rec987aae7d522057 | Sunset Ridge 309C | selSched | Scheduled |
| rec98bdfeec73545e | Sunset Ridge 104B | selSched | Scheduled |
| reca06d89f1a4ac5b | Sunset Ridge 309C | selSched | Scheduled |
| reca8230a8fd9ff51 | Sunset Ridge Unit 14 | selSched | Scheduled |
| recf50eb955a10651 | Sunset Ridge 309C | selProg | In Progress |

7 rows, 4 Scheduled, 3 In Progress, 0 Ready. The claim is exactly true, not approximately true.

Note for the record, not a blocker: criteria 1 and 2 direct the agent to move rec98bdfeec73545e and
rec987aae7d522057 from Scheduled to In Progress. Both post-write states remain inside the
{Scheduled, In Progress} set, so criteria 7 and 27 stay true after the agent's own writes.

### 3. Sunset Ridge plus Harris co-occurrence scan, re-run

Scan across all 34 split files: exactly ONE row in the entire universe contains both "Sunset Ridge"
and "Harris". It is qb invoice 113714702211, DocNumber 4422, CustomerRef Harry Harris, $60.00, line
description "Lease document scanning and filing fee - Unit 14, Sunset Ridge Apartments, October
2026". That is a single-unit management fee, not a portfolio ownership record.

The contradicting evidence round 1 cited still stands: Unit 14 eviction authorization comes from
Linda Castillo (ticket EVF-2026-014, "Owner authorization received from Linda Castillo to proceed
with eviction filing for Unit 14"), and Castillo is a separate owner in the OPS-10 four-owner set.

Scan of the 32 rubric titles: ZERO titles contain both "Sunset Ridge" and "Harris". The attribution
is genuinely gone. Six titles mention Sunset Ridge (1, 2, 7, 20, 24, 27); none attaches an owner.

Owner-to-property co-occurrence matrix, whole universe, row counts:

| owner | Sunset Ridge | Mesa Vista | Ridgeview | Las Vistas | Las Palmas | Rio Bend | 412 Mesquite | Pinecrest |
|---|---|---|---|---|---|---|---|---|
| Harry Harris | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Robert Finley | 0 | 3 | 6 | 0 | 0 | 0 | 0 | 0 |
| Linda Castillo | 0 | 2 | 0 | 0 | 0 | 2 | 3 | 0 |
| David Shea | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Harris has effectively no property attribution in this universe beyond that one $60 line. Removing
the possessive was correct.

### 4. Criterion 4, direction-agnostic duplicate resolution

Now reads: "so that only one of the June 2 and June 3, 2026 events remains live on the calendar."

Both Harris events are status `confirmed` and neither is cancelled, so retiring either one leaves
exactly one live review. The end state is achievable in either direction.

| base event id | summary | start_dt | status | invitee rows |
|---|---|---|---|---|
| 1pon50ds1aevem63td6f7emdn3 | Harry Harris Mid-Year Portfolio Review | 2026-06-02T12:15:00-05:00 | confirmed | 5 |
| qqbwq3s2h7wh5udoek2940mffk | Harry Harris Mid-Year Portfolio Review (Rescheduled) | 2026-06-03T15:00:00-05:00 | confirmed | 4 |

All 9 invitee rows carry status confirmed. Per-calendar breakdown, which also verifies the
addressability claim in the criterion's evidence field:

June 2: patricia.nguyen, aurora.winona, teresa.wood, brooke.phillips, lisa.smith
June 3: patricia.nguyen, aurora.winona, teresa.wood, brooke.phillips (no lisa.smith row)

The evidence field's statement that Lisa Smith holds no row on the June 3 instance is exactly
correct. Since the persona is Lisa Smith, the June 3 instance is reachable only through another
attendee's calendar row, and the evidence field already says an RSVP action must not be required
there. Consistent with the one-row-per-invitee shape.

### 5. Criterion 10, invoice DocNumbers dropped from the title

Title now grades only the $10,980.00 total. Confirmed programmatically: none of "2026-494",
"2026-303" or "4421" appears anywhere in criterion 10. The three component amounts remain in the
justification as corroboration, which is where they belong. Total re-derives exactly, section (c).

### 6. Occupancy and collections split into two criteria

Criterion 13 grades the 94% occupancy figure, scoped to the Mesa Vista portfolio.
Criterion 14 grades the 97% collections figure. This is the 32nd criterion.

Lisa Smith's message, quoted verbatim, slack C006 #owner-relations, message id
a6779a055eaf5fb1893d0ed6d92e3b39, user U6480117503 Lisa Smith, ts 1780002481.000001:

  "Robert's Mesa Vista portfolio is sitting at 94% occupancy, one unit still in make-ready targeting
  early June. Collections at 97%, one late payment cleared after first notice. Closed out three
  tickets this month including a water heater leak, and the turn is on track."

Portfolio named: Mesa Vista, attributed to Robert. Criterion 13's scoping to "the Mesa Vista
portfolio" matches the source exactly. The criterion drops the "Robert's" possessive, which is a
weaker claim than the source and therefore safe.

97% appears in exactly ONE row across all 34 split files, and it is this message. The collections
figure appears in the same message and nowhere else, as required.

94% is NOT unique to this message. It appears in 5 rows. See ADVISORY A1.

### 7. Criteria 15 and 28, "more than one" replaces "four"

Mesa Vista distinct units in tblMakeReady and their row statuses:

| unit | statuses across rows |
|---|---|
| Mesa Vista 107A | In Progress, In Progress |
| Mesa Vista 207A | In Progress, Ready, In Progress |
| Mesa Vista 310C | Scheduled |
| Mesa Vista 4C | In Progress, Ready |

"More than one unit in a turn" is robustly true. 107A and 310C alone establish it, and neither has a
competing Ready row. The earlier "four" was fragile because 207A and 4C each carry both a Ready row
and a non-Ready row, so a defensible reading could put the count at 2, 3 or 4. The change removes
that fragility. Correct fix.

### 8. Criterion 16, water heater justification no longer says "Tommy Reyes's unit"

Confirmed programmatically: the string "Tommy" does not appear anywhere in criterion 16.

The title's claim that the closed water heater work sits outside both portfolios is grounded:
- 412 Mesquite belongs to Linda Castillo. gmail 5b8b95b55b893525, from brooke.phillips@starpm.com to
  carlos.mendez@starpm.com and linda.castillo@gmail.com, subject "Water Heater and Flooring Repair
  Completed at 412 Mesquite, Unit 4", body "both repairs at your 412 Mesquite property are complete.
  John handled the water heater replacement".
- Linda Castillo is a distinct owner from Harris and Finley, per OPS-10's four-owner list, and holds
  her own Mid-Year Portfolio Review on 2026-05-26.
- Pinecrest 12, the other closed water heater record (MT-2026-1280, completed 2026-05-11), has zero
  co-occurrence with Harris or Finley anywhere in the universe.

Either candidate satisfies the claim, so the criterion does not depend on which one the agent picks.

### 9. Criterion 24, both accept-set items named by content

Both are grounded and both are unique rows:
- Mesa Vista 310C subfloor assessment: rec88734a4fdfde57, the only Mesa Vista 310C row.
- Sunset Ridge 309C utility transfer confirmation: reca06d89f1a4ac5b, the only 309C row mentioning
  utility transfer.

Worth noting that criterion 2's target (rec987aae7d522057, deep-clean unanswered) and criterion 24's
309C item (reca06d89f1a4ac5b, utility transfer) are DIFFERENT rows that are both at Scheduled. The
disambiguating clause in criterion 2 is doing necessary work and does it correctly.

---

## ADVISORIES

These are grounding observations, not values defects. Every value involved is grounded. I am raising
them because they bear on whether the criteria can be graded as written, and I would rather state
them plainly than let them pass silently. They are outside my values-only remit to adjudicate, so I
am reporting rather than blocking.

### A1. Criteria 13, 17 and 25 assert universal negatives that a Linear comment contradicts textually

Criterion 13: "no record supports the 94% occupancy figure"
Criterion 17: "no record supports a late payment being cleared for either owner"
Criterion 25: "no record in either portfolio carries an occupancy figure"

Against the systems of record these are all true. tblMakeReady and tblMaintenanceTickets are the only
two Airtable tables and neither has an occupancy field, so no occupancy figure is computable
anywhere. The QuickBooks ledger shows no late payment ever cleared, per the timing table in (c).

However, linear comment comment_5a6d779a715f587392dd00b9c8dbbd4a on OPS-100, authored by Brooke
Phillips 2026-05-26, reads in part:

  "occupancy section runs unit by unit across Mesa Vista with the 94% figure and context on the one
  unit still vacant, rent collection notes the late payment from last month and confirms it's been
  resolved"

That is a record, about Finley's portfolio, that carries a 94% occupancy figure and asserts a late
payment was resolved. OPS-100 is titled "May Monthly Owner Report - Finley Properties". Three further
OPS-100 comments by the same author echo the same narrative.

Read literally, "no record supports X" is therefore false for 13, 17 and 25; read as "no system of
record supports X", all three are true. An agent that surfaces OPS-100 may well report the narrative
rather than the negative, and grade as a fail while being substantively correct.

I flag this rather than block because the values themselves are grounded and the substance is true
against Airtable and QuickBooks. The distinction between a narrative restatement and a system of
record is exactly the trap this task appears to be built on, so the wording may be deliberate. If it
is, the evidence fields should say so explicitly.

Separately, hubspot deal_9664cf85817555d0b1e0dfddfc054c96 carries "Occupancy across the Oakfield
Commons units held at 94%". That is a real occupancy figure at the same percentage, but for Oakfield
Commons under company comp_mesaverde (Mesa Verde Investments), which is neither owner's portfolio, so
it does not contradict criterion 25. Note the Mesa Verde versus Mesa Vista name similarity as a
distinct near-miss hazard.

### A2. Criterion 26 depends on the Unit 14 attribution

Criterion 26 claims MT-2026-047 is the only open maintenance ticket in either owner's scope. The
complete open-ticket set (fldCompletionDate empty or absent) is 7 rows:

| ticket | subject | attributable to |
|---|---|---|
| DLQ-2026-0601 | Tanya Mitchell delinquency | Unit 14, see below |
| MT-2026-0184 | Tanya Mitchell second-month delinquency | Unit 14, see below |
| MT-2026-047 | roof damage, Finley portfolio property | Robert Finley |
| MT-2026-0519 | Las Vistas 9D QC rework | Las Vistas, no owner link |
| MT-2026-1211 | water heater leak, Tommy Reyes unit | 412 Mesquite, Linda Castillo |
| MT-2026-1256 | water heater and flooring follow-up | 412 Mesquite, Linda Castillo |
| MT-2026-1271 | Las Palmas 8D move-out walk | Las Palmas, no owner link |

Only MT-2026-047 names Harris or Finley, so the criterion holds. The residual risk is that invoice
4422 bills Harry Harris for "Unit 14, Sunset Ridge Apartments", and two of the seven open tickets
concern Tanya Mitchell in a "Unit 14". An agent that joins those could place two more open tickets in
Harris's scope.

Two things weigh against that reading: the Unit 14 eviction authorization comes from Linda Castillo
(EVF-2026-014), and both Mitchell tickets are delinquency and collections items rather than
maintenance work. "Unit 14" is also the known cross-property ambiguity in this universe, appearing as
"Unit 14", "Rio Bend - Unit 14", "Sunset Ridge Unit 14" and "Unit 14 - Tanya Mitchell Eviction"
across four make-ready rows.

### A3. Criterion 16's affirmative phrasing exceeds what the universe enumerates

The universe never enumerates either owner's portfolio, so "belongs to a property outside both of
these owners' portfolios" is strictly stronger than what can be proven by enumeration. It survives
here only because 412 Mesquite carries a positive attribution to a different named owner. Had the
water heater work landed on an unattributed property, the claim would not have been provable. Noting
this because the criterion's robustness rests on that one email, not on a portfolio join.

---

## THINGS I COULD NOT VERIFY

- Whether "Robert's Mesa Vista portfolio" in Lisa Smith's message is a complete statement of Finley's
  holdings. Finley also co-occurs with Ridgeview 6 times, so Mesa Vista is not his only property. No
  record enumerates any owner's full portfolio. This does not affect any value in the set, since no
  title claims a portfolio is complete.
- David Shea has zero property co-occurrences and no Mid-Year review event on the calendar, despite
  appearing in OPS-10's four-owner list. Out of scope for this set, recorded for completeness.

---

## (e) VERDICT

VERDICT: GO

Blocker count: 0

All 32 criterion titles are fully grounded. Both round-1 blockers are resolved: the Harris to Sunset
Ridge ownership attribution appears in zero titles, confirmed by a re-run co-occurrence scan over all
34 split files and over all 32 titles. All eight listed changes are grounded, and each was verified
against the split rather than against the rubric's own justification fields. The three derived dollar
figures re-derive exactly from their components. Three advisories above are recorded for S3 and AUDIT
to weigh; none of them is a values-grounding failure.
