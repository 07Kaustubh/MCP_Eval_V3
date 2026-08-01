# AUDIT: 6_Oracle_Events.txt (round 6, strict)

Task: 46_6a62ccb6ce2323b4b9e0c8d8 | Universe: StarPM (V4) | Universe today: 2026-07-01 America/Chicago
File audited: 6_Oracle_Events.txt, 36 steps, 6398 words, 42784 bytes
Method: mechanical simulation against `_aux/Universe_Split/` (double json.loads), tool and parameter
resolution against `StarPM_Base_Universe/7_Server_Tools_Details.json`. No spot checks.

## VERDICT: REVISE

Two blockers, both in reachability, both one-line fixes. Everything else in the file is clean:
every factual claim I tested against the split held, every edit since r5 landed and is correct,
and no edit introduced a new error.

---

## 1. Reachability, exhaustive and mechanical

### Method

I extracted every identifier-shaped token from all 36 steps (110 distinct: Airtable record ids,
Linear issue keys and comment ids, Slack message and channel ids, QuickBooks entity ids, calendar
base ids and per-calendar row ids, Gmail thread and message ids, HubSpot object ids, QuickBooks
customer ids). I then built the retrieval surface from the file's own literal query terms: 9
`search_records` calls, 7 `list_issues` queries, 2 `list_comments`, 4 Slack reads and searches, 12
QuickBooks searches, 13 per-calendar `list_events` expansions, 5 `search_threads` plus `get_thread`
fan-out to every message in each returned thread, and 1 contacts search. An identifier counts as
reachable if it is the id of a returned record or appears in the payload of one.

Calendar `fullText` was simulated over summary, title, description and location. Slack search was
simulated both as literal substring and as token-AND. Contacts and QuickBooks customer search were
simulated as token-AND, since neither `"Brooke Phillips"` nor several other cited strings occur as
literal substrings in the stored field layout.

### Result: 104 of 110 reachable, 6 not

**BLOCKER 1. Five HubSpot object ids are cited with no HubSpot call anywhere in the file.**

OE 10 cites `comp_mesaverde`, `comp_proj_fef06d5fa2b2`, `comp_proj_8a64d674466b`, `comp_riogrande`
and `ticket_87552e6b23bc5a92bd2641b9054b8c13`. OE 11 additionally cites, in prose, "a HubSpot deal
reporting Oakfield Commons occupancy" (`deal_9664cf85817555d0b1e0dfddfc054...`).

I resolved every tool-shaped token in the file against the catalog. Thirty-four distinct tools are
named, spanning seven of the eight services:

| service | distinct tools named |
|---|---|
| airtable | 5 |
| contacts | 1 |
| gcalendar | 6 |
| gmail | 3 |
| linear | 6 |
| quickbooks | 8 |
| slack | 5 |
| **hubspot** | **0** |

HubSpot is the only service in the universe with zero calls, and it is the only service whose
records the file cites without retrieving. Neither `search_crm_objects` nor `get_crm_objects` nor
any other HubSpot tool appears in any of the 36 steps.

Every HubSpot claim in OE 10 is factually correct. I verified each one:

- `comp_mesaverde` is "Mesa Verde Investments", and Finley's HubSpot contact
  `contact_5e77eae71d865fe38318e10facf62de9` carries `company_id: comp_mesaverde` with a live
  association both ways. Correct.
- The three deals whose names carry "Mesa Vista" are `deal_8cd04fe1...` (associated to
  `comp_proj_fef06d5fa2b2`, Sunshine Cleaning), `deal_f170c305...` (`comp_proj_8a64d674466b`, A Plus
  Carpet Cleaning and Repairs) and `deal_mesavista4a` (`comp_riogrande`, Rio Grande Holdings LLC).
  Correct, and the point the step draws from it is right: the company structure genuinely does not
  route to the owner.
- Exactly three tickets carry the subject "Move-Out - Connor Beaumont, Mesa Vista - Vacancy June 30"
  (`ticket_707d94dc97215448823`, `ticket_849dd11c9abf58c0afc`,
  `ticket_87552e6b23bc5a92bd2641b9054b8c13`), and only the last names Robert Finley. Correct.
- OE 11's Oakfield Commons deal exists and reports 94 percent occupancy. Correct.

So this is not a factual defect. It is a retrieval defect, and it is the same one the file has
already cured five times. The standing treatment on this task is the one applied to the two Fernwood
invoices: a record used to prove a negative is either made reachable or removed. OE 30 shows the
removal pattern working well, keeping the substance ("the only rows outside it carrying 104B sit on
Fernwood Gardens rather than Sunset Ridge", which I confirmed against invoices 232547977309 and
509422853402) while dropping the unreachable ids. OE 10 kept the ids.

The ticket citation is worse than the company citations, because it is a positive claim with
record-level specificity. "It is one of three near-identical move-out tickets carrying that same
subject and the only one that names him" is a statement about a set the agent cannot enumerate with
any call the file makes.

Preferred fix: name a HubSpot retrieval in OE 10. `search_crm_objects` on the Mesa Vista or Finley
terms reaches the deals, the companies and the ticket, closes the last open hole in the every-service
sweep, and adds calls rather than removing content. Fallback fix: delete the five ids and OE 11's
deal reference, keeping the prose findings, exactly as the Fernwood pair was handled.

**BLOCKER 2. `rec94e86a3007dd5e` is cited in OE 21 with no call returning it.**

OE 21: "An eighth row, 'Rio Bend - Unit 14' on rec94e86a3007dd5e, carries the same bare unit number
and does not name her."

The row exists, `fldUnit` is "Rio Bend - Unit 14", `fldTurnStatus` is selReady. The file makes four
`tblMakeReady` searches: "Sunset Ridge", "Mesa Vista", "Ridgeview", "Tanya Mitchell". The row matches
none of them, and the step itself says why: it does not name her, so the query that produced the
other seven cannot produce it. It matches only "Unit 14" or "Rio Bend", neither of which the file
names anywhere.

Smaller than Blocker 1 and non load bearing (the step's conclusion, that no row places Tanya Mitchell
on Mesa Vista, holds on the seven rows alone). Fix: add `search_records` on `tblMakeReady` with query
"Unit 14", which returns exactly 5 rows (`rec91517a5acab558`, `rec94e86a3007dd5e`,
`reca8230a8fd9ff51`, `recc83c05d889b354`, `receee45491536859`) and makes the cross-property collision
the step is asserting directly observable rather than asserted. Or drop the id.

### The other four unreached identifiers are refinements, listed in section 4

`C003` and `C005` (OE 6), and by extension the OE 6 channel enumeration generally.

### Reachability confirmations worth recording

These were the r5 repairs. All five simulate correctly on the current bytes:

| step | named path | simulated result |
|---|---|---|
| OE 13 | `search_estimates` query "Harris" | returns exactly 3: 300730861679 (4722 Elmwood Ave), 308892996802 (Elmwood Units 204 and 211), 981816261186 (Pinebrook Apartments). `search_invoices` "Harris" returns 3 and none of the estimates, so the step's reason for the second call is right. |
| OE 18 | `search_records` tblMaintenanceTickets "Tanya Mitchell" | returns exactly 2: `rec46234590708b5c` (MT-2026-0184), `recc0ecc885e9645e` (DLQ-2026-0601). "exactly those two" is exact. |
| OE 21 | `search_records` tblMakeReady "Tanya Mitchell" | returns exactly 7, and the seven `fldUnit` strings match the step verbatim. |
| OE 11 | `list_issues` query "reconciliation" | returns 4 (OPS-39, OPS-55, OPS-57, OPS-93), including the cited pair. "4 issues including OPS-39 and OPS-93" is exact. |
| OE 30 | `search_records` tblMaintenanceTickets "Mesa Vista"; `search_threads` "make-ready" plus `get_thread`; `search_bills` "Mesa Vista" or "4C"; `list_events` across carlos.mendez and wesley.tran | all four deliver. The ticket search returns `rec12969a3fdb0852` and `reca424761ae15355`; thread `66132537181ecbe1` is in the make-ready result set; both bill queries cover all four of 195089456477, 696089964235, 546359391323, 991582431419; and `0hjw400xgjb3j7ay7ynuaqbnpi` sits on carlos.mendez and wesley.tran. |

Gmail message `2ae48555b3009a95` is reachable: it is a message inside thread `621640f9e7aa6d46`,
which both `search_threads` "eviction" and `search_threads` "authorization" return, so `get_thread`
surfaces it. The two Fernwood invoices are gone from the file and the claim they supported survives
in OE 30 without them.

---

## 2. Did the edits land, are they correct, did they introduce anything new

Diffed against `_aux/6_Oracle_Events.pre_r1sweep.bak`. Five steps changed: OE 11, 18, 21, 30, 35.
Earlier edits (OE 13's estimates path, OE 30's retrieval block, OE 16 and 17 supersession framing,
OE 30's 207A accept set) were already in that backup and I verified them directly on current bytes.

**OE 16, 17, 30 supersession framing.** Landed and correct. OE 16 now rests on
`rec7d202aed68c95c` superseding `rec98bdfeec73545e`, OE 17 on `recf50eb955a10651` and
`rec2471fac3f9ae51` answering `rec987aae7d522057`, and both say so explicitly because the July dates
sit after universe today. OE 30's rewrite matches: "whether because a later row on the same unit
answers the question that row was waiting on, as on the two Sunset Ridge rows, or because the work is
already done and invoiced, as on Ridgeview". I read all seven Sunset Ridge rows and all eight Mesa
Vista rows; every quoted `fldNotes2` fragment is verbatim.

The Ridgeview correction is the one that cannot rest on supersession (single row in the table), and
OE 30 says so and grounds it outside Airtable instead: calendar `whd6zys0hw7zbsh11m9vqv4m4i` on
2026-06-08 (confirmed, past) and invoice 109367557444. Both verified.

**OE 30, 207A accept set.** Landed. "an agent that leaves the 207A rows alone and an agent that
corrects them are both acceptable", with the reason stated (no record on any other service names the
unit). I tested that negative across all eight services: "207a" occurs on exactly 3 records,
all Airtable. Correct. The parallel 4C claim is also correct: six records support the selReady row
(closed ticket `reca424761ae15355`, Gmail `66132537181ecbe1`, four vendor bills) against one that
points the other way (`0hjw400xgjb3j7ay7ynuaqbnpi`, 2026-07-15, confirmed, location "Mesa Vista, Unit
4C"). `rec12969a3fdb0852` does flag Linda Castillo, verbatim.

**OE 35, booked meetings excluded.** Landed. Both events exist, both confirmed:
`j3ulusavtqgvwge31s21ep5c8w` "Mesa Vista HOA Management Review" on 2026-07-08 and
`232wqgjdsa2cyz9mv4qtx5mncy` "Q3 Make-Ready Planning & Budget Review" on 2026-07-23. The step's
reasoning (a booked meeting is carried work, so neither is the target) is sound and it is what
reconciles the "carried nowhere" claim against Calendar.

**Nothing new introduced.** The five diffs are additive or clarifying. No new identifier, count,
date or amount appears in them that I could not verify.

### Factual verification performed on current bytes

Every one of these matched the split exactly. Listing them because the r4 history means an assertion
of "checked" is worth less than the list.

- OPS-10: only issue with "Mid-Year" in title; team_001, proj_002, state_OPS_0, assignee Brooke
  Phillips; `created_at` equals `updated_at` at 2026-05-03T22:11:57.112604-05:00.
- The four OPS-10 comments and their quoted fragments, including "locked in for the first week of
  June, 60 minutes in the afternoon" and "occupancy rates, outstanding maintenance backlog, and
  make-ready status".
- OPS-100 state_OPS_2, four comments, and comment_42a514c0's "so I'm moving this to Done".
- OPS-39 state_OPS_3 with 0 comments; OPS-93 state_OPS_1, `completed_at` null, 1 comment. The step's
  point (the issue claiming closure is the one in the earlier state and carrying the only comment)
  is exact.
- Five workflow states, one team, `next_issue_number` 1000.
- C006: 43 rows, 12 top level, 31 replies. Universe wide: 346 of 580 Slack messages are thread
  replies. Parent `831d2b67...` carries `latest_reply` 1782860664.000001, which matches no message
  anywhere; its one reply carries ts 1780002480.000000 and is dated 2026-05-28 on both fields.
- All nine calendar events: base ids, dates, times, row counts, per-row calendars, and every
  attendee response. The Harris original has five rows with all four attendees accepted; the
  rescheduled has four rows with Aurora and Patricia declined and Teresa accepted and no Lisa row;
  the Finley review has four rows with Lisa and Aurora declined and Finley not an attendee. Lisa
  holds 16 rows, latest 2026-06-02, none on or after universe today. A 2026-06-01 to 2026-06-09
  sweep returns no Finley event. Zero of the 565 rows carry a bare base id.
- Money: 8400 + 2190 + 390 = 10,980 with all three past due and 5848 settled; all three Harris
  invoices at Balance 0.00; credit memos 2755 + 490 + 410 = 3,655 and 195 + 1250 + 530 = 1,975, every
  one with Balance equal to TotalAmt, LinkedTxn null and RemainingCredit 0, and all 117 credit memos
  in the universe sharing that shape; four of the six carrying BILL- or INV- prefixes; invoice
  445653930748 billed to Linda Castillo with the three 4C pass-through lines and 31 days past due.
- The eight further QuickBooks records naming Harris properties, all eight attributions correct.
- ItemRef "Monthly Management Fee": present on Simone Okafor (2), Tanya Mitchell (3) and Connor
  Beaumont (3), and on Robert Finley zero times.
- Airtable: 7 open rows in tblMaintenanceTickets, with the empty completion value stored 4 times as
  null and 3 times as empty string; MT-2026-047 the only open repair ticket in either owner's scope;
  "Mesa Vista 310C" a single row unit string; zero selReady rows in the Sunset Ridge cluster.
- The 94 percent figure appears in connection with Finley or Mesa Vista only in Lisa's own message
  and the comment repeating it; elsewhere only on unrelated objects including the Oakfield Commons
  deal. The 97 percent figure appears exactly once in the entire universe, in Lisa's own message.
- Tanya Mitchell delinquency dates on `rec8005502043b755` (June 23 installment unmet, plan breached)
  and `rec3782834f35df50` (did not cure before the June 29 three-day notice deadline), consistent
  with the Gmail timeline of June 6 first notice, June 11 plan, June 23 missed, June 25 breached,
  June 26 three-day notice.

---

## 3. Other checks

**Tools and parameters.** All 34 named tools resolve against the catalog. Every parameter name
resolves and is correct for StarPM specifically, including the three places the universe differs
from its siblings: `slack_send_message` uses `message` (OE 36), `create_draft` uses `body` with no
send tool (OE 33), `save_issue` uses `team` (OE 35). `search_records` uses `table` while
`update_records_for_table` uses `tableId`, which is right for both. No phantom tool: I checked every
underscore token in the file that is not a catalog tool and all nine are legitimate field or
parameter names.

**Single-target uniqueness.** The three graded write targets in OE 30 are distinct record ids, and
the file names an accept set or an explicit leave-alone for every row that could compete. The one
case that could have gone wrong is 309C, which carries two selSched rows: `rec987aae7d522057` is
graded and `reca06d89f1a4ac5b` must be left alone. OE 30 discriminates them on content that is on the
rows themselves (one row's open question is answered on two later rows; the other waits on a utility
transfer that no record in the universe resolves, which I confirmed). That is hard but fair, and it
is stated, not assumed. OE 31's two targets, OE 33's recipient, OE 34's issue and OE 36's channel are
each unique. OE 35 is correctly graded on title and description with a two-candidate accept set,
since the new issue number cannot be predicted.

**Completeness claims against Calendar.** Every one is reconciled. OE 15's "two items unresolved and
carried nowhere" explicitly discharges MT-2026-047 and the 2026-07-13 booked walk-through. OE 35
repeats it and now also discharges the two confirmed July meetings. OE 30's 4C reasoning names the
2026-07-15 QC inspection as the record pointing the other way rather than ignoring it. OE 19's
Ridgeview correction is made against a past confirmed event and an issued invoice with the future
follow-up named. OE 28 and OE 29 both rest on sweeps I re-ran and confirmed.

**Internal contradictions.** None found. I checked the cross-step arithmetic and state claims that
could drift: the Sunset Ridge "none in a Ready state" in OE 33 against the seven rows in OE 13;
the "four units rather than one, at least two still open on their latest row" in OE 33 against the
eight Mesa Vista rows (107A and 310C are open on their latest row, exactly two, and the stated
accept range of two to four covers the 4C and 207A accept sets); the 10,980.00 in OE 23, 26 and 33;
the 3,655.00 in OE 25, 26 and 33; the two-candidate open item in OE 15 and OE 35.

**Density.** 69 tool-name mentions across 32 of the 36 steps, before expansion. The per-calendar
sweeps alone expand 5 mentions into 13 calls, and the QuickBooks reads expand 8 mentions into roughly
15. Comfortably above the 50 design target. Fixing Blocker 1 by naming a HubSpot call adds to this
rather than subtracting.

**Validator.** `validate.py --phase oe` exits 0, 36 steps, 0 fails, 0 warns. Zero em-dashes, zero
en-dashes, zero non-ASCII characters in the file.

---

## 4. Refinements (not blocking)

**R1. OE 9 names two queries and only one delivers.** The step says
`slack_search_public` with query "Harris Finley" or "make-ready", and claims the result includes
`49b2873d46d55e4291a78d91d91a5054` and `5f60afa12c4c53b6b7694d59373acae8`. Those two messages read
"two make-readies on track" and "two make-readies wrapping on schedule". The literal string
"make-ready" is not a substring of "make-readies", so the second named query returns 20 messages and
neither of the two. "Harris Finley" read as tokens returns exactly the three messages the step
describes, which is almost certainly the intent, but an agent that takes the second option gets a
result the step does not describe. Naming "Harris" instead would return all three under either
reading.

**R2. OE 6 enumerates channels the named call does not return.**
`slack_search_channels` with query "owner" returns only C006. C001, C002, C004, C007 and C008 do
appear as `channel_id` on messages other steps return, but C003 and C005 appear nowhere in any
returned payload. The enumeration is expository and no conclusion rests on it, so this is cosmetic,
but a broader query term would make it literal.

**R3. OE 35's two excluded meetings are not returned by any call.**
`j3ulusavtqgvwge31s21ep5c8w` and `232wqgjdsa2cyz9mv4qtx5mncy` sit on teresa.wood, brooke.phillips,
tony.reyes and elias.navarro. The file's calendar reads are fullText "Harris", fullText "Ridgeview",
fullText "Portfolio Review", Lisa's own calendar, and unfiltered reads of carlos.mendez and
wesley.tran. None reaches either event. This is the safe direction, since they are named as
exclusions rather than as evidence, but it is the same shape as the blockers.

**R4. OE 20's "412 Mesquite" attribution is outside its own two calls.** The step calls
`search_records` on tblMaintenanceTickets and `slack_search_public`, both with "water heater". The
412 Mesquite string lives on a tblMakeReady row (`recca0da8f7416f51`) and on QuickBooks records, none
of which those two calls return. The Tommy Reyes and Linda Castillo link is fully reachable from the
Slack results, so the conclusion stands; only the property name is unsupported by the named path.

**R5. OE 25 produces Harris's credit memos and nothing consumes them.** The step establishes
$1,975.00 of unapplied credits for Harris, and the RemainingCredit trap applies to them identically.
OE 33's email content spec and its S3 decompose list mention Finley's unapplied credits but not
Harris's, so S3 will write no criterion for them. Given the prompt asks for "anything on the money
side either of them is likely to raise", either add Harris's unapplied credits to OE 33's element
list or state in OE 25 that they are established for the trap and not graded. Worth settling before
S3 rather than after.

**R6. OE 29 attributes to Slack a detail that is partly on the event.** "Slack described it as a
casual 45-minute morning call in late June while the event is 30 minutes at midday on 2026-06-02."
The 45-minute morning framing is in the event's own description, reachable through OE 28 plus
`get_event`, and the contradiction against the actual 12:15 to 12:45 slot is therefore fully
observable. The "late June" element exists only in Slack messages `2b4b2265ca...` and
`7e8901f944...`, which neither OE 9 query returns. Consider sourcing the sentence to the event
description, which is stronger and already reachable.

---

## 5. Observation, not a finding

If the platform's `list_events` `fullText` indexes attendee addresses as well as summary,
description and location, then OE 13's "which returns three events" becomes four: harry.harris@gmail.com
is an attendee of "Mitchell Eviction Case-Prep Review" (`vwdtvhm1y7ukp2v2vm5ytr9dpi`, 2026-05-21,
teresa.wood and brooke.phillips). Under the standard summary, description and location reading the
count of three is exact, and I have scored it correct. Flagging only because the fourth event would
reinforce the Harris and Mitchell association rather than disturb it, so no conclusion in OE 13 is at
risk either way.

---

## 6. What to change

1. OE 10: name a HubSpot retrieval (`search_crm_objects`) that reaches the companies, the three Mesa
   Vista deals and the move-out ticket, or delete the five ids and OE 11's deal reference and keep
   the prose. Naming the call is the better trade: it closes the only service with zero calls.
2. OE 21: add `search_records` on tblMakeReady with query "Unit 14", or drop `rec94e86a3007dd5e`.
3. Optional, in the same pass: R1 (swap OE 9's query to "Harris"), R5 (settle Harris's credit memos
   in OE 33 or OE 25), R6 (source OE 29's 45-minute detail to the event description).

Re-run `validate.py --phase oe` after the edit. Nothing in items 1 to 3 touches a graded record, an
amount, a date or an S3 decompose directive, so no downstream artifact needs revisiting.

---

## VERDICT: REVISE
