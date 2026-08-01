# Council B round 3 (final): adversarial QC + density + hardness preservation

Task: Tasks/46_6a62ccb6ce2323b4b9e0c8d8
Artifact: `6_Oracle_Events.txt`, 36 steps, 38305 chars
Universe: starpm, V4, dual-model, today 2026-07-01 America/Chicago
Method: file read fresh. Nothing carried forward from my round 1 or round 2 as fact. Every claim
re-derived from `_aux/Universe_Split/` by direct query. Prior reports read first only to establish
what was promised, then set aside.

## 0. Confirmation on the withdrawn round-2 N2 fix

I measured it myself. My round-2 N2 fix was wrong and its removal is correct. I accept it without reservation.

- ItemRef "Monthly Management Fee" appears on **24 distinct QuickBooks customers**. Harry Harris 9,
  Tanya Mitchell 3, Simone Okafor 2, and **Robert Finley 0**. Mesa Verde Investments carries the most, 12.
  Applied symmetrically my rule would have made Finley, the confirmed owner of the other portfolio in
  this same task, own nothing. The discriminator was worthless.
- The companion claim was also false. Harry Harris carries 12 QuickBooks records, of which 3 are
  payments with no lines and **9 carry property-naming line descriptions**. Invoice 113714702211 is
  one of nine, not one of one.
- OE 13 now states the bridge as weak, names the counter-evidence in the step, enumerates all eight
  further property-naming records, and instructs the estimate sweep. I re-derived all eight by id,
  entity type and property string. All eight are exact.

The current OE 13 is materially better than what I proposed. Recorded so this is not relitigated.

## What I re-verified clean

Every one of these was re-derived from the split, not accepted from a prior report.

| Area | Result |
|---|---|
| Identifiers | 90 extracted, **90 resolve verbatim**, zero misses |
| Tool names | 32 distinct, **32 resolve** in `7_Server_Tools_Details.json` |
| Tool parameters | every named parameter correct, incl. `slack_send_message.message` (not payload), `create_draft.body` (not content), `save_issue.team` (not teamId), `update_records_for_table.baseId/tableId/records`, `search_records.baseId/table/query`, `get_event.eventId`, `list_events.calendarId/fullText`, `list_issue_statuses.team`, `get_aged_receivables.customer` |
| Dashes | 0 em, 0 en, 0 minus, 0 non-breaking, 0 horizontal bar, **0 non-ASCII characters at all** |
| `validate.py --phase oe` | PASS, 0 fails, 0 warns |
| Slack structure | C006 = 43 rows, 12 top-level, 31 replies, 7 campaign + 5 owner cluster. Universe 346 of 580 are replies. All exact |
| `latest_reply` 1782860664.000001 | matches no message anywhere. Exact |
| Near-duplicate pair timing | 49b2873d and 5f60afa1 are 1140 seconds apart, **nineteen minutes**. Exact |
| Linear | OPS-10 is the only "Mid-Year" title. created_at == updated_at. OPS-39 has 0 comments, OPS-93 has 1. `next_issue_number` 1000. All exact |
| Comment authorship | all six cited comments resolve to **Brooke Phillips** via author_id |
| Calendar | Lisa holds exactly 16 rows, latest 2026-06-02, none on or after today. Harris original 5 rows all accepted, Rescheduled 4 rows with Aurora and Patricia declined and Lisa absent. Finley review 4 rows, 11:45 to 13:15 (90 min), Lisa and Aurora declined, Finley not an attendee. Zero Finley events 2026-06-01..09. All exact |
| The "casual 45-minute morning call late June" attribution to Slack | correct, two C004 messages from Teresa Wood carry it verbatim |
| Maintenance tickets | exactly 7 open, empty stored both as `''` (3) and `null` (4), no status field. Exact |
| Mitchell rows | exactly 7, all seven fldUnit strings exact, rec94e86a3007dd5e is Rio Bend and names Victor Rios not Mitchell, zero Mitchell rows name Mesa Vista. Exact |
| Gmail 2ae48555b3009a95 | To linda.castillo@gmail.com, and the June 6 / June 23 / June 25 / June 26 / June 29 sequence is verbatim. OE 30 and OE 33 now agree |
| QuickBooks money | Finley open 8400 + 2190 + 390 = **10,980** exact; 5848 settled with a matching payment; credit memos 2755 + 490 + 410 = **3,655** exact; Harris three invoices all Balance 0.00 each matched by an equal payment. All 117 credit memos share Balance == TotalAmt, RemainingCredit 0, no LinkedTxn |
| Search-result claims | `search_invoices "Harris"` returns exactly 3, `"Sunset Ridge"` exactly 2, and 110274597983 is genuinely absent from the Harris search. Both Unit 14 invoices share TxnDate 2026-05-13 and DueDate 2026-06-12. Exact |
| 104B outside Airtable | exactly the two Fernwood Gardens invoices 232547977309 and 509422853402. Exact |
| 309C / 310C / 107A outside Airtable | **zero rows on any service**. Exact |
| OE 35 accept-set | 310C appears in 1 row universe-wide; the 309C utility transfer appears in 1 row universe-wide. Both targets are single-record and genuinely carried nowhere |

The spine of this file is sound and the drafting quality is high. What follows is what survives that.

---

## B1. Sub-dimension scores

SUB-DIM OE Completeness -> SCORE 4/3-4-5 NON-FAIL -> REASON all six prompt deliverables have covering OE steps and every must-take step is covered, but the Mesa Vista Unit 4C ownership and money leg is swept on no service despite the Hardness Plan naming its key record as lever L8, so an agent that runs the single most natural money query for this portfolio reaches a graded quantity the chain does not accommodate.

SUB-DIM OE Accuracy -> SCORE 4/3-4-5 NON-FAIL -> REASON 90 of 90 identifiers, 32 of 32 tools, and every enumeration I recounted are exact, but OE 30 asserts which of the two Mesa Vista 4C rows fails against the ground and six services carry records saying the opposite, and OE 33 asserts a make-ready count derived by a counting method the rest of the file contradicts.

---

## B2. Adversarial alt-path

**Yes. One path the chain does not accommodate, and it is the money path.**

The prompt says "anything on the money side either of them is likely to raise with me". The portfolio
is Mesa Vista. The single most natural QuickBooks query is `search_invoices` with query "Mesa Vista".

That query returns **exactly one invoice in the entire universe**:

```
id 445653930748  DocNumber 2026-534  CustomerRef Linda Castillo
TotalAmt 1622.00  Balance 1622.00  TxnDate 2026-05-01  DueDate 2026-05-31  (31 days past due)
Line 1: Post-move-out deep clean - Mesa Vista Unit 4C (Sunshine Cleaning, vendor pass-through)
Line 2: Full interior repaint - Mesa Vista Unit 4C (Pete Donovan Painting, vendor pass-through)
Line 3: Paint touch-up, bedroom closet trim - Mesa Vista Unit 4C
```

An open, past-due invoice for work on a unit the OE assigns to Finley, billed to an owner the OE puts
out of scope. The agent now has three defensible moves: add 1,622 to Finley's position and report
12,602, exclude it silently, or report it as a mis-billing the owner will raise. Only the second
matches OE 26 and OE 33. The other two fail a criterion S3 is explicitly told to write.

This is not a hypothetical I constructed. `_aux/Hardness_Plan.md` lever 8 names this exact record:
"Multi-link chain ... invoice `445653930748` (billed **Linda Castillo**, not Finley)". The plan
identified it as a designed trap. The OE mentions it zero times.

Second alt-path, lower probability, same shape. HubSpot files contact Robert Finley under
`comp_mesaverde` "Mesa Verde Investments", domain `mesaverdeinv.com`. QuickBooks carries a separate
customer 102 "Mesa Verde Investments" at `ap@mesaverdeinv.com`, same domain, with three past-due
invoices totalling 1,150.00. OE 10 plants the company name and then uses it only as a negative. An
agent bridging on the domain inflates Finley's receivable again. Counter-evidence exists and is
strong (that company also contains StarPM's own Teresa Wood and Elias Navarro, so it is a CRM junk
drawer), which is why I rank this a refinement rather than a blocker.

---

## B3. Per-model tool-call density, counted separately, against the 40+ V4 target

I counted the calls the OE chain itself requires, step by step, counting repeats where the step text
demands them (three `read_invoice` at OE 24, six `get_credit_memo` at OE 25, four `list_events` plus
per-hit `get_event` at OE 28, three calendars at OE 19).

| Segment | Calls |
|---|---|
| OE 1 to OE 11 discovery (Linear, Slack) | 10 |
| OE 12 Airtable surface | 3 |
| OE 13 Harris attribution incl. both invoice searches and the estimate sweep | 13 |
| OE 14 to OE 17 clusters | 4 |
| OE 18 to OE 21 maintenance, Ridgeview, water heater, collections | 14 |
| OE 22 to OE 25 QuickBooks money both owners | 20 |
| OE 27 to OE 29 Calendar | 13 |
| OE 30 to OE 36 the six writes | 8 |
| **OE-implied floor** | **~85** |

That floor carries no exploratory overhead, no failed searches and no re-reads.

**Opus 4.8 projection: 60 to 70.** Opus batches and trusts a single search result. Expect it to drop
roughly four of six `get_credit_memo` confirmations, two of four `get_event` confirmations at OE 28,
and both `get_aged_receivables` negatives, then add six to ten exploratory calls. Midpoint **65**.
PASS against 40+, margin +25.

**Gemini projection: 65 to 80.** Gemini re-searches more and confirms individual records more often.
It is likelier to run the full OE 25 credit-memo sweep and to re-query Airtable per unit string.
Midpoint **72**. PASS against 40+, margin +32.

Both clear the 40+ per-model target with wide margin. The Hardness Plan's 63.5 and 66.0 are
consistent with my independent count and I see no reason to move them.

Two observations rather than concerns. The pathological floor, an agent that skips every confirmatory
read and every negative check, is about 37, marginally under 40, but such a run fails most of the OE
chain and would be scored on the rubric long before density mattered. And both blockers below, if
fixed, **add** calls, so density only improves.

VERDICT B3: **PASS**, both models, comfortably.

---

## B4. Per-lever preservation

| Lever | Covering OE steps | Status |
|---|---|---|
| **L1 Latching** on Lisa's own undispositioned claim | OE 8 (the claim, reached by thread read), OE 11 (94 traceable to Lisa alone), OE 14 (four Mesa Vista units against "one"), OE 20 (water heater is the wrong portfolio, and the derivation now runs the right way, comment_5a6d779a at 2026-05-26 precedes her 2026-05-28 message), OE 21 (97 has no source, the late payment points elsewhere), OE 33 (each refutation is a named content element) | **PRESERVED**, but the "four units" element is the subject of Blocker 2 |
| **L2 Structured-DB skip** | QuickBooks AR at OE 22 to OE 26. Unmirrored Calendar at OE 19, OE 27, OE 28, OE 29, OE 31. OE 27's persona-scoped read failing to surface the Harris duplicate is intact | **PRESERVED** |
| **L7 Multi-write diversification** | 6 writes across 5 services: Airtable OE 30, Calendar OE 31, Gmail OE 33, Linear comment OE 34, Linear issue OE 35, Slack OE 36 | **PRESERVED** |
| **L10 Reversal / supersession** | Harris double-booking at OE 28 and OE 31 (both confirmed, neither cancelled, Lisa holds no row on the Rescheduled instance, verified). OPS-10 Backlog against two comments announcing transitions at OE 4 and OE 34. OPS-39 In Review against OPS-93 Todo at OE 11. The Finley review contradicting comment_79dc8383 on all three counts at OE 29 | **PRESERVED**, and the calendar defect is correctly built as a two-owner beat per the Hardness Plan correction |
| **L11 Net-vs-gross** | OE 25 states Balance and LinkedTxn govern and names RemainingCredit 0 as the trap, OE 26 forbids netting to 7,325, OE 33 makes the unapplied credits a content element. The BILL- and INV- prefixed credit memos (sub-lever L6) survive at OE 25 | **PRESERVED**, strongest lever in the file |

**Contrast pair, Harris operationally blocked against Finley cash-blocked.** Carried explicitly at
OE 33 ("Harris is operationally blocked ... against 0.00 of open receivable; Finley is cash-blocked").
Supported at OE 13 (7 Sunset Ridge rows, 3 unit strings, zero in selReady, verified), OE 24 (Harris
0.00, confirmed with the aged-receivables negative), OE 23 and OE 26 (Finley 10,980).

**The pair survives.** It is the best-constructed part of this file. One caution: its Finley limb is
a single number, and Blocker 2 sits directly on that number.

---

## B6. PROPAGATE TO S1 flags

**None.** The prompt is 261 words, no tool names, no em-dashes, no pre-solving. Both blockers below
are OE-level reconciliation gaps and are fixable inside `6_Oracle_Events.txt`. Neither requires a
prompt change, and I specifically checked that neither can be cured by adding a prompt clause without
crossing into pre-solving.

---

## B8. OE completeness, must-take steps with no covering OE

All six prompt deliverables are covered: make-ready corrections OE 30, both review meetings OE 31,
the Brooke email OE 33 with the recipient resolved at OE 32, the tracker update OE 34, the new item
OE 35, the channel post OE 36.

One must-take **investigation** step has no covering OE: the Mesa Vista Unit 4C ownership and money
reconciliation. See Blocker 1 and Blocker 2. This is a completeness gap, not a missing deliverable,
which is why Completeness scores 4 and not 3.

---

## B9. Service mapping

Seven services carry named calls and all resolve: linear, slack, airtable, quickbooks, gmail,
gcalendar, contacts. All 32 tool tokens and every named parameter verify against
`7_Server_Tools_Details.json`.

**One gap.** HubSpot is the eighth service. OE 10 cites `comp_mesaverde`, three deal ids and
`ticket_87552e6b23bc5a92bd2641b9054b8c13` in prose, and **no HubSpot call is named anywhere in the
file**. The catalog offers `search_crm_objects` and `get_crm_objects`. AUDIT round 3 recorded check 7
("every record the file cites is reachable by a call the file actually makes") as PASS. On the
HubSpot limb it is not. Refinement, not a blocker, because the Finley to Mesa Vista link is
established three other ways inside the same step.

---

## B-RULE13. Single-target uniqueness, every-service sweep, naive-agent simulation

**Single-target uniqueness: PASS on every write target.**

| Write target | Uniqueness check |
|---|---|
| rec98bdfeec73545e | one row, pinned by id, unit string 104B carries 2 rows so the id is load-bearing and is used |
| rec987aae7d522057 | one row. 309C carries 4 rows including reca06d89f1a4ac5b which must NOT move, so pinning by id is mandatory and is done |
| rec8b679d92f30753 | the only Ridgeview row in the table |
| Harris Rescheduled event | pinned as per-calendar rows, `qqbwq3s2h7wh5udoek2940mffk-b6a1e41c` and `-0f82233a`, never a bare base id. Verified: no stored row carries a bare base id |
| Finley review row | `8mwlxrq5w5oodwdpmvo83e00f2-b0504ab4`, one row, on Lisa's calendar |
| Brooke Phillips | exactly one contact, `c46d47256fd95ca6aca770c8dddda5eb`, verified |
| C006 | exactly one channel named #owner-relations |
| OPS-10 | the only issue in the workspace with "Mid-Year" in the title |
| New issue | correctly graded on title and description, not on a number, since next_issue_number is 1000 |

**Every-service sweep including Calendar: one FAIL.** I swept all nine split stores for every unit
string in both clusters. 309C, 310C and 107A are Airtable-only, exactly as OE 30 claims. 104B is
Airtable plus two Fernwood invoices, exactly as OE 30 claims. 207A is 14 rows across Airtable, Gmail
and Slack, and OE 30's claim that "no record on any other service names the unit at all" is
**wrong on its face** for Gmail and Slack, though I checked the five Gmail and six Slack hits and
none bears on the turn status, so the operative conclusion survives and I record this as part of
Refinement 1 rather than separately. **Mesa Vista Unit 4C is the failure**: 13 rows across four
stores outside Airtable, plus a second Airtable table the OE never opens on this unit. See Blocker 1.

**Unreconciled future confirmed events (F9).** Nine distinct confirmed events sit on or after
2026-07-01. The OE names two of them, the Ridgeview follow-up `42b119cbt7xd0vnhw6dwvdqizo` on 07-13
and the Mesa Vista 4C QC `0hjw400xgjb3j7ay7ynuaqbnpi` on 07-15. One further event is on an in-scope
portfolio and is named nowhere: `j3ulusavtqgvwge31s21ep5c8w` "Mesa Vista HOA Management Review",
2026-07-08. Refinement 4 below. I also confirmed the Mesa Vista 310C "Move-out inspection booked for
July 16" has **no** calendar event, which strengthens rather than weakens OE 15 and OE 35.

**Naive-agent simulation, prompt only, OE not in view.** I ran this on all six writes. Five are
clean. The sixth, the email body at OE 33, fails on two of its ten content elements, which is
Blocker 2.

---

# BLOCKERS

## BLOCKER 1. OE 30's Mesa Vista 4C paragraph names the wrong row as failing, and six services say the opposite.

**This is a blocker.**

OE 30 currently says:

> On 4C the row that fails against the ground is the selReady one, recc8534b3fd13954, and the record
> that fails it sits outside Airtable: confirmed calendar event 0hjw400xgjb3j7ay7ynuaqbnpi ... is a
> "Final make-ready QC inspection" whose description is to "confirm the unit is rent-ready and
> release it to leasing", so the release that row reports as done is still standing as booked work on
> another service. Correcting 4C therefore means moving recc8534b3fd13954 back to selProg, not moving
> recbd087a4abd605b forward

Everything quoted about the calendar event is true. The conclusion drawn from it is not. Six records
across five services state that Mesa Vista 4C is finished, and one of them is a **closed ticket in
the same Airtable base the agent is already inside**:

1. `airtable:reca424761ae15355`, table **tblMaintenanceTickets**, ticket MR-4C-2026-08,
   fldCompletionDate 2026-05-01, so closed: *"All make-ready work at Mesa Vista 4C is complete. Deep
   clean, interior repaint, faucet cartridge replacement, GFCI outlet swap, and drywall patch all
   finished and confirmed. QC walkthrough by Jaime addressed the bedroom closet trim; touch-up passed
   re-inspection. Unit status updated to market-ready in the make-ready record."*
2. Gmail `66132537181ecbe1` (and its near-duplicate `5101c5a41dffa90a`), Carlos Mendez to
   **linda.castillo@gmail.com**, 2026-06-02, subject "Mesa Vista 4C Make-Ready Complete. Cost Summary
   for Your Records": *"the make-ready on Mesa Vista Unit 4C is fully wrapped up ... The unit is
   market-ready and I've handed it off to the leasing team to begin showings."*
3. Slack `91063dec92fa598fa387e9e8539b852f`: *"Sunshine Cleaning invoice is in QuickBooks, Mesa Vista
   4C deep clean is closed out."*
4. Slack `ed12902ee46751c6a89bc4bf6334742a`: *"Pete's repaint is done, bill entered in QuickBooks for
   Mesa Vista 4C."*
5. Four QuickBooks vendor bills entered for the work: 195089456477 deep clean, 696089964235 interior
   repaint, 546359391323 the closet trim touch-up "following final QC walkthrough", 991582431419 the
   turnover punch list.
6. QuickBooks owner invoice 445653930748 consolidating the pass-throughs.

So `recc8534b3fd13954` selReady is the row that **matches** the ground. The 2026-07-15 QC event is
the outlier, and reca424761ae15355 records that a QC walkthrough by Jaime was already performed and
passed, which is what the selReady row's own notes also say.

There is a second limb. `airtable:rec12969a3fdb0852` (MT-2026-084) opens the 4C turn and flags
"Tony Reyes, Carmen Delgado, Pete Donovan, Jaime Salinas, and **Linda Castillo**". Together with the
owner-directed Gmail and the Castillo-billed invoice, **Mesa Vista Unit 4C's owner is documented as
Linda Castillo**, who OE 3, OE 18 and OE 28 all place out of scope. The OE assigns all eight Mesa
Vista rows to Finley at OE 14 and never names the contest.

Why it matters even though 4C is ungraded: OE 30 states a fact about which row fails, S3 writes
evidence fields from this step, and an evidence field asserting that recc8534b3fd13954 fails against
the ground would be contradicted by a closed ticket in the same base. This is the same defect class
AUDIT round 3 escalated on the Ridgeview sentence, one paragraph away.

**Exact replacement.** Replace, in OE 30, the text from "Mesa Vista 207A and Mesa Vista 4C each carry"
through "and an agent that leaves the pair alone are both acceptable." with:

> Mesa Vista 207A and Mesa Vista 4C each carry selProg rows alongside a selReady row stating the unit
> is finished and cleared for leasing. Neither pair is graded, and the two have separate reasons. On
> 4C the weight of the record supports the selReady row rather than contradicting it, and most of
> that record sits outside tblMakeReady: closed ticket reca424761ae15355 in tblMaintenanceTickets
> reports "All make-ready work at Mesa Vista 4C is complete" and that unit status was updated to
> market-ready, Gmail 66132537181ecbe1 has Carlos Mendez telling the owner the unit is market-ready
> and handed to leasing, and four QuickBooks vendor bills 195089456477, 696089964235, 546359391323
> and 991582431419 are entered for the deep clean, the repaint, the closet trim touch-up and the
> punch list. One record points the other way, confirmed calendar event 0hjw400xgjb3j7ay7ynuaqbnpi on
> 2026-07-15, carried on brooke.phillips@starpm.com, carlos.mendez@starpm.com and
> wesley.tran@starpm.com at location "Mesa Vista, Unit 4C", a "Final make-ready QC inspection" whose
> description is to "confirm the unit is rent-ready and release it to leasing", which stands as
> booked work after the date the record says the unit was released. That single event is not enough
> to overturn the other six, and the unit's ownership is itself contested, because rec12969a3fdb0852
> flags Linda Castillo on the turn and QuickBooks invoice 445653930748 bills the 4C pass-throughs to
> her rather than to Robert Finley while Gmail 66132537181ecbe1 is addressed to her as the owner.
> Castillo is Patricia's owner under the OE 3 split, so 4C stays out of the graded set on the same
> ground as the Unit 14 delinquency records at OE 18, and an agent that leaves the pair alone, an
> agent that moves recbd087a4abd605b forward, and an agent that moves recc8534b3fd13954 back are all
> acceptable. On 207A the only rows in the universe carrying that unit string outside tblMakeReady
> are Gmail and Slack messages that do not bear on turn status, so the only reading available is that
> the later row supersedes the earlier ones, and with nothing to check it against neither direction of
> correction can be graded.

That replacement is entirely re-derived. Every id, quotation and count in it was verified before I
wrote it. It contains no dashes.

## BLOCKER 2. OE 33's graded "make-ready count correction" asserts four by a counting method the rest of the file contradicts, and its Finley receivable element is exposed by an unswept past-due invoice.

**This is a blocker.**

OE 33 instructs S3 to decompose the email body into "one criterion per content element", and names
"the make-ready count correction" as one of them. The asserted correction is: *"Mesa Vista has four
units in make-ready rather than one"*.

Count it the way OE 16, OE 17 and OE 30 teach the agent to count, which is that the later row on a
unit governs:

| Unit | Rows | Latest row by created_time | State |
|---|---|---|---|
| 107A | 2 | rec35a6c4f2e50657 | selProg |
| 207A | 3 | rec591a0f70432651 14:02:59 | **selReady**, "Unit cleared for leasing as of July 17" |
| 310C | 1 | rec88734a4fdfde57 | selSched |
| 4C | 2 | recc8534b3fd13954 2026-05-29 | **selReady**, "Unit confirmed ready for leasing" |

By that method **two** Mesa Vista units are still in make-ready, not four. Four is the count of unit
strings carrying any row at all, which is the one counting method the file never teaches. OE 14 words
it carefully and correctly as "Four Mesa Vista units carry make-ready rows". OE 33 converts that into
a claim about state. An agent that reasons the way the file trains it to reason writes two or three
and fails a criterion S3 has been told to write.

Compounding it, one of the four is Castillo's per Blocker 1, so a fully correct agent may legitimately
report three units in Finley's Mesa Vista scope.

The second limb is the money element. OE 33 requires "10,980.00 past due across invoices 2026-494,
2026-303 and 4421". `search_invoices` with query "Mesa Vista" returns exactly one record in the whole
universe, invoice **445653930748**, DocNumber 2026-534, **Balance 1,622.00, DueDate 2026-05-31, 31
days past due**, for Mesa Vista Unit 4C work, **billed to Linda Castillo**. That is the most natural
single query for the Finley money question and the OE mentions the record zero times. `_aux/Hardness_Plan.md`
lever 8 names it explicitly as a designed trap.

**Exact replacements, two of them.**

First, in OE 33, replace "Mesa Vista has four units in make-ready rather than one" with:

> Mesa Vista carries make-ready rows on four units rather than one, of which at least two are still
> open on their latest row, so any count from two to four is correct provided the agent states that
> more than one unit is involved

Second, add to the end of OE 26, before the final sentence:

> One further record has to be dispositioned before this total is stated, because it is what a
> property-scoped money query returns. search_invoices with query "Mesa Vista" returns exactly one
> record in the universe, invoice 445653930748 (DocNumber 2026-534, 1,622.00, TxnDate 2026-05-01,
> DueDate 2026-05-31, so 31 days past due), which bills the Mesa Vista Unit 4C post-move-out deep
> clean, interior repaint and closet trim touch-up. Its CustomerRef is Linda Castillo, not Robert
> Finley, and Gmail 66132537181ecbe1 has Carlos Mendez sending the same cost summary to her as the
> owner of that unit. It therefore does not belong in Finley's receivable and 10,980.00 stands, but an
> agent that surfaces it as a billing question on the Mesa Vista portfolio has found something real
> and must not be marked down for naming it, provided it is not added to Finley's balance.

Both replacements were re-derived before writing and contain no dashes.

---

# REFINEMENTS

**Refinement 1 (recommended, one sentence).** OE 30 opens "Three rows across the two owners qualify,
and they are exactly the selSched rows that the surrounding record shows the work has already started
on." That is true of rec98bdfeec73545e (sibling records the repaint started) and of rec8b679d92f30753
(the repair event is in the past and invoiced), but **false of rec987aae7d522057**: its siblings
recf50eb955a10651 and rec2471fac3f9ae51 record that a scheduling question was answered and vendor
work is booked for July 21 and July 22, not that work started. OE 17 itself says only "The scheduling
question is settled and vendor work is booked". This is an "exactly" enumeration claim that is false
for one of three, the same shape AUDIT round 3 escalated, introduced by AUDIT round 3's own
replacement. The step already states the correct discriminator in its closing sentence, so the
opening one is both wrong and redundant. Replace with:

> Three rows across the two owners qualify, and they are exactly the selSched rows that the
> surrounding record has moved past, whether because the work has started or because the question
> that row was waiting on has been answered and the vendor schedule locked in.

Also within this refinement: OE 30's "On 207A no record on any other service names the unit at all"
is literally false (5 Gmail and 6 Slack rows carry "207A"), though none bears on turn status. The
Blocker 1 replacement text above already corrects this wording.

**Refinement 2 (optional).** The Ridgeview 8,400 is billed three times: owner invoice 109367557444
plus **two open vendor bills** for the same job, 528539050604 (2026-481) and 301715729067
(PD-2026-084), both 8,400.00 and both open. An agent sweeping QuickBooks for "Ridgeview" gets six
hits and may surface a 16,800 duplicate-pay exposure. OE 26 says "The money question the prompt
anticipates is the 8,400.00 Ridgeview roof invoice 2026-494", which is not wrong but is incomplete.
One sentence in OE 26 noting the duplicate vendor bills as payables rather than owner receivables
would close it.

**Refinement 3 (optional).** QuickBooks customer 102 "Mesa Verde Investments" (`ap@mesaverdeinv.com`)
shares its domain with HubSpot company `comp_mesaverde`, which is where HubSpot files contact Robert
Finley. It carries 1,150.00 past due. OE 10 plants the company name. One clause noting that the
QuickBooks customer of that name is a separate customer, and that the HubSpot company also contains
StarPM's own Teresa Wood and Elias Navarro so it is not Finley's entity, would close the bridge.

**Refinement 4 (optional).** Confirmed future event `j3ulusavtqgvwge31s21ep5c8w` "Mesa Vista HOA
Management Review", 2026-07-08, sits on an in-scope portfolio inside the horizon and is named nowhere
in the file. OE 35 asserts that exactly two items are carried nowhere. Naming this event and
explaining why a booked meeting is not unresolved work would protect that assertion.

**Refinement 5 (optional).** OE 10 cites `comp_mesaverde`, three deal ids and
`ticket_87552e6b23bc5a92bd2641b9054b8c13` but no HubSpot call is named anywhere in the file. Add
`search_crm_objects` or `get_crm_objects` to the step so the cited records are reachable by a call
the file makes.

---

## What is NOT a blocker, recorded so it is not rediscovered

- **OE 35's accept-set is coherent after six rounds.** Both targets verify as single-record and
  genuinely carried nowhere: 310C appears in exactly 1 row universe-wide, the 309C utility transfer in
  exactly 1. The July 16 move-out inspection has no calendar event, so the subfloor item really is
  unreconciled. The decompose directive matches the two-target accept-set. No change needed.
- **OE 30's three graded rows are correct.** All three are selSched, all three move to selProg, and no
  record anywhere opposes that direction. AUDIT round 3's Ridgeview replacement landed and reads
  correctly. Only the umbrella sentence and the 4C paragraph need work.
- **The future-dated notes (July 14, 15, 18, 21, 22) are a property of the data, not a defect.** The
  corrections rest on sibling row status, not on dates, so they are date-independent. AUDIT round 3's
  warning to S3 against date-versus-today criteria stands and should be carried into the handoff.
- **The Mesa Vista / Mesa Verde and Castillo / Finley near-collisions are good hardness**, not noise.
  My blockers ask for them to be adjudicated in the OE, not removed from the universe.

---

## Verdict rationale

The file is in good shape. Ninety of ninety identifiers resolve, thirty-two of thirty-two tools and
every parameter resolve, the validator passes with zero fails and zero warns, there is not a single
non-ASCII character, and every enumeration I recounted independently is exact, including the seven
Mitchell rows, the eight further Harris records, the exactly-3 and exactly-2 invoice searches, the
nineteen-minute gap, the 43/12/31 channel shape and the 346-of-580 reply ratio. All five selected
levers are preserved and the contrast pair, which is the shape this task is built on, is intact and
well carried. Density clears the V4 40+ per-model target with a margin of +25 on Opus and +32 on
Gemini. My own round-2 error is properly excised and the replacement is better than what I proposed.

Two things stop it. Both are the same failure: Mesa Vista Unit 4C was never swept outside
tblMakeReady. Inside that gap sit a closed ticket in the same Airtable base that flatly contradicts
what OE 30 asserts about which row fails, an owner-directed email and an open past-due invoice that
together document the unit as Linda Castillo's rather than Robert Finley's, and a graded content
element in OE 33 whose asserted count contradicts the counting method the rest of the file teaches.
The Hardness Plan named the key record, invoice 445653930748, as lever 8. The OE mentions it zero
times. This is exactly the every-service reconciliation the project rule exists to force, and it was
missed by three AUDIT rounds and by both of my earlier passes because every pass swept 4C only within
the make-ready table.

Neither blocker requires new universe work, neither touches the prompt, neither weakens a lever, and
replacement text is supplied and pre-verified for both. This is a revise, not a rebuild.

VERDICT: BLOCK
