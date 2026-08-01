# Council B round 4: convergence check on the applied round-3 fixes

Task: Tasks/46_6a62ccb6ce2323b4b9e0c8d8
Artifact: `6_Oracle_Events.txt`, 36 steps, 41315 chars (was 38305)
Universe: starpm, V4, dual-model, today 2026-07-01 America/Chicago
Method: file re-read fresh. Every claim re-derived from `_aux/Universe_Split/` by direct query.
My round-3 report was read only to establish what was promised, then set aside. Gmail bodies were
base64url decoded before every cross-service sweep in this round, which is the change in method that
produced the finding in section 0.

## 0. A correction I have to make against my own round-3 report

My BLOCKER 1 replacement text contained a false clause, and it is now in the file. I own this
without reservation, exactly as I owned the round-2 N2 error.

My round-3 report stated, inside Refinement 1, that "OE 30's 'On 207A no record on any other service
names the unit at all' is literally false (5 Gmail and 6 Slack rows carry 207A)". That is wrong.

Re-derived this round, with Gmail bodies decoded:

| Sweep | Result |
|---|---|
| rows containing `207A`, all 33 stores, Gmail decoded | **3, all in airtable.airtable_records** |
| rows containing `207A` outside Airtable | **0** |

The 5 and 6 counts came from a sweep on the bare string `207`, which matches HubSpot association
`{"id": 207`, a Gmail `history_id` of `1782851207000`, Linear `OPS-207`, Slack message ids such as
`5ec29e2300dc5ccda7dd295ae27207ae` and a Slack `ts` of `1779718656.000207`. None of those is a
reference to unit 207A. The original sentence was correct and my correction of it was not.

The consequence is section BLOCKER A below. The three 207A rows are `reca4aa17f0755b55` selProg,
`rec4081fd2ccde95a` selProg and `rec591a0f70432651` selReady, all created 2026-05-22, verified.

## 1. Closure of the four applied items

Every fact in every applied replacement was re-derived from the split this round, not accepted.

### BLOCKER 1 (OE 30 Mesa Vista 4C paragraph): CLOSED

| Claim in the applied text | Verification |
|---|---|
| closed ticket `reca424761ae15355` in tblMaintenanceTickets | exists, MR-4C-2026-08, fldCompletionDate 2026-05-01, text begins "All make-ready work at Mesa Vista 4C is complete" and ends "Unit status updated to market-ready in the make-ready record". Quoted verbatim |
| Gmail `66132537181ecbe1`, Carlos Mendez tells the owner market-ready and handed to leasing | resolves as a Gmail **thread** id carrying one message `5101c5a41dffa90a`, From carlos.mendez@starpm.com, To linda.castillo@gmail.com, 2026-06-02, body "The unit is market-ready and I've handed it off to the leasing team to begin showings". Verbatim |
| four QuickBooks vendor bills | all four exist as `bill` entities and each matches the label the step gives it: `195089456477` Sunshine Cleaning deep clean 387.00, `696089964235` interior repaint 1340.00, `546359391323` closet trim touch-up "following final QC walkthrough" 85.00, `991582431419` turnover punch list 85.00 |
| confirmed event `0hjw400xgjb3j7ay7ynuaqbnpi` 2026-07-15 on brooke, carlos and wesley, location "Mesa Vista, Unit 4C" | exactly 3 rows, all status confirmed, all start 2026-07-15T10:00:00-05:00, location "Mesa Vista, Unit 4C" on all three, description contains "confirm the unit is rent-ready and release it to leasing". Every element exact |
| `rec12969a3fdb0852` flags Linda Castillo on the turn | exists, MT-2026-084, flags "Tony Reyes, Carmen Delgado, Pete Donovan, Jaime Salinas, and Linda Castillo" |
| invoice `445653930748` bills the 4C pass-throughs to Castillo | CustomerRef Linda Castillo, DocNumber 2026-534, 1622.00, Balance 1622.00, TxnDate 2026-05-01, DueDate 2026-05-31, three Mesa Vista Unit 4C pass-through lines |
| 4C out of the graded set on the OE 18 ground, three agent behaviours accepted | present verbatim |

Independent re-check of the ownership premise: **zero records in the universe contain both "4C" and
"Finley"**, confirmed across all 33 stores with Gmail bodies decoded. The premise holds.

One observation that strengthens the step rather than threatening it: the Gmail body names "owner
invoice 2026-537", and **no record with DocNumber 2026-537 exists**. The real record is 2026-534. The
step does not claim the numbers match, only that the same cost summary went to Castillo as owner,
which is accurate, so this is not a defect. It is additional evidence that 4C is Castillo's.

### BLOCKER 2a (OE 33 make-ready count): CLOSED

Applied text is present verbatim. Re-derived by the counting method the rest of the file teaches,
latest row on a unit governs:

| Unit | Rows | Latest row | State | Open on latest |
|---|---|---|---|---|
| Mesa Vista 107A | 2 | rec35a6c4f2e50657 | selProg | yes |
| Mesa Vista 207A | 3 | rec591a0f70432651 | selReady | no |
| Mesa Vista 310C | 1 | rec88734a4fdfde57 | selSched | yes |
| Mesa Vista 4C | 2 | recc8534b3fd13954 | selReady | no |

Four unit strings, **exactly two open on the latest row**. "At least two are still open on their
latest row" is true, and "any count from two to four is correct" is a sound accept-set that no
correct agent can fall outside. The L1 refutation of Lisa's "one unit still in make-ready" survives
intact, because every value in the accept-set is greater than one.

### BLOCKER 2b (OE 26 disposition of invoice 445653930748): CLOSED

Applied text present verbatim. Re-derived: `search_invoices` with query "Mesa Vista" returns
**exactly one invoice in the universe**, 445653930748, CustomerRef Linda Castillo. The step now names
it, prices it, dates it, assigns it to Castillo, refuses it a place in Finley's receivable, holds
10,980.00, and protects the agent that surfaces it. The alt-path I raised in round 3 is closed at
its source.

Finley's total re-derived independently: 8400.00 plus 2190.00 plus 390.00 equals **10,980.00** exact,
with 110099741914 at Balance 0.00 correctly excluded.

### Council A blocker (OE 13 reachability): CLOSED

Both records are now returned by calls the file actually makes.

| Leg | Verification |
|---|---|
| `list_issues` query "Harris" | returns **exactly 3** issues: OPS-10, **OPS-32**, OPS-38 |
| `list_issues` query "eviction" | returns **exactly 3** issues: **OPS-32**, OPS-38, OPS-54. Both offered queries reach the target and both return three, so the step's "returns three issues" is true either way |
| OPS-32 content | title "Eviction Hearing - Mitchell, Harris Property", project proj_003, description contains "the Tanya Mitchell eviction case at one of Harry Harris's units" verbatim |
| `list_events` fullText "Harris" across brooke, patricia, teresa | 9 matching rows resolving to **exactly 3 distinct base events**: the two Harris reviews and `nuh928ma4rwhwf1bnap30rmfli`. The step's "returns three events" is exact |
| `get_event` on `nuh928ma4rwhwf1bnap30rmfli-0f82233a` | row exists on brooke.phillips@starpm.com, status confirmed, title "Mitchell Eviction Court Hearing", description contains "JP court hearing for the Mitchell eviction at the Harris property" verbatim |
| Lisa holds no row | **0** Lisa rows on that base event, so the OE 27 persona-scoped read genuinely misses it |

### Refinement 1 (OE 30 opening enumeration): APPLIED and correct

The replacement is present verbatim and it is now true of all three rows. rec987aae7d522057 is
covered by the "question that row was waiting on has been answered and the vendor schedule locked in"
limb, which matches OE 17's own wording. The false "exactly the selSched rows the work has already
started on" claim is gone.

## 2. B1. Sub-dimension scores

SUB-DIM OE Completeness -> SCORE 5/3-4-5 NON-FAIL -> REASON the Mesa Vista 4C ownership and money leg that was previously swept on no service is now dispositioned in three places, invoice 445653930748 at OE 26, the ownership contest at OE 30 and the count accept-set at OE 33, and the two records Council A found unreachable are now returned by named calls at OE 13, so all six prompt deliverables and every must-take investigation step carry a covering step.

SUB-DIM OE Accuracy -> SCORE 4/3-4-5 NON-FAIL -> REASON 98 of 98 identifiers, 32 of 32 tools and 25 of 25 checked parameters resolve and both round-3 false assertions are corrected and independently re-verified, but OE 30 now carries two consecutive contradictory sentences about 207A and the first of them asserts Gmail and Slack rows that do not exist anywhere in the universe.

## 3. B2. Adversarial alt-path

**No open alt-path.** The money path that was the round-3 blocker is closed at OE 26: the single
record a property-scoped money query returns is now named and dispositioned, and all three defensible
agent moves are explicitly accommodated, add-to-balance being the one ruled out with a reason the
agent can verify. The count path is closed at OE 33 by an accept-set that spans every value a correct
counting method can produce.

I re-ran the naive-agent simulation on all six writes with the prompt in view and the OE out of view.
All six are clean this round. The email body at OE 33, which failed two of ten content elements in
round 3, now passes on both: the count element accepts two through four, and the receivable element
is protected against the 1,622.00 intruder.

The Mesa Verde bridge remains the only residual, and it remains a refinement: QuickBooks customer 102
"Mesa Verde Investments" at ap@mesaverdeinv.com shares a domain with HubSpot `comp_mesaverde` where
Finley is filed, and carries 1,150.00 past due. Counter-evidence is strong because that HubSpot
company also contains StarPM's own Teresa Wood and Elias Navarro.

## 4. B3. Per-model tool-call density, counted separately, against the 40+ V4 target

Recounted from the current file. OE 13 grew by one `list_issues`, three `list_events` and one
`get_event`, and OE 26 grew by one `search_invoices`, so the floor moved up.

| Segment | Calls |
|---|---|
| OE 1 to OE 11 discovery | 10 |
| OE 12 Airtable surface | 3 |
| OE 13 Harris attribution, now including the Linear and Calendar legs | 16 |
| OE 14 to OE 17 clusters | 1 |
| OE 18 to OE 21 maintenance, Ridgeview, water heater, collections | 14 |
| OE 22 to OE 26 QuickBooks money both owners | 21 |
| OE 27 to OE 29 Calendar | 11 |
| OE 30 to OE 36 the six writes | 10 |
| **OE-implied floor** | **~86** |

That floor carries no exploratory overhead, no failed searches and no re-reads. 59 tool mentions are
distributed across 32 of the 36 steps, with only OE 4, OE 15, OE 16 and OE 17 naming none, and those
four are reasoning steps over rows already pulled.

**Opus 4.8 projection: 60 to 70, midpoint 65.** PASS against 40+, margin **+25**.
**Gemini projection: 65 to 80, midpoint 72.** PASS against 40+, margin **+32**.

Methodology unchanged from round 3: Opus batches and trusts a single search result, so it drops
roughly four of six `get_credit_memo` confirmations, two `get_event` confirmations and both
`get_aged_receivables` negatives, then adds six to ten exploratory calls. Gemini re-searches and
confirms individual records more often. The Hardness Plan's 63.5 and 66.0 remain consistent with the
independent count.

VERDICT B3: **PASS**, both models, comfortably. The applied fixes only add calls.

## 5. B4. Per-lever preservation, including the contrast pair

Levers re-read from `_aux/Hardness_Plan.md`. The selected set is L2, L10, L11, L1, L7, with L5 and L6
carried as sub-levers.

| Lever | Covering OE steps | Status |
|---|---|---|
| **L1 Latching** on Lisa's own undispositioned claim | OE 8 the claim reached by thread read, OE 11 the 94 traceable to Lisa alone, OE 14 four Mesa Vista units against "one", OE 20 water heater on the wrong portfolio, OE 21 the 97 with no source, OE 33 each refutation a named content element | **PRESERVED**. The count accept-set of two to four keeps every value above Lisa's "one", so the refutation is not softened |
| **L2 Structured-DB skip** | QuickBooks AR at OE 22 to OE 26, unmirrored Calendar at OE 19, OE 27, OE 28, OE 29, OE 31 | **PRESERVED and strengthened**. OE 26 adds a property-scoped invoice query and OE 13 adds a three-calendar `list_events` plus `get_event` |
| **L7 Multi-write diversification** | 6 writes across 5 services: Airtable OE 30, Calendar OE 31, Gmail OE 33, Linear comment OE 34, Linear issue OE 35, Slack OE 36 | **PRESERVED**, untouched |
| **L10 Reversal / supersession** | Harris double-booking OE 28 and OE 31, OPS-10 Backlog against two transition comments OE 4 and OE 34, OPS-39 In Review against OPS-93 Todo OE 11, the Finley review contradicting comment_79dc8383 on three counts OE 29 | **PRESERVED**, untouched |
| **L11 Net-vs-gross** | OE 25 Balance and LinkedTxn govern with RemainingCredit 0 named as the trap, OE 26 forbids netting to 7,325, OE 33 makes the unapplied credits a content element | **PRESERVED and strengthened**. Re-derived: 117 of 117 credit memos carry Balance equal to TotalAmt, RemainingCredit 0 and no LinkedTxn. Finley credits 3,655.00 exact, Harris 1,975.00 exact, four of the six wearing BILL- or INV- prefixes, so sub-lever L6 survives |

**Contrast pair, Harris operationally blocked against Finley cash-blocked.** Re-derived this round:
Sunset Ridge carries 7 make-ready rows across 3 unit strings with **zero in selReady**, against
Harris open receivable of **0.00** across three invoices each matched by an equal payment. Finley
carries **10,980.00** open across three past-due invoices. Both limbs verify exactly and the pair is
carried explicitly at OE 33 and supported at OE 13, OE 23, OE 24 and OE 26.

**The pair survives, and its Finley limb is now protected.** In round 3 I flagged that the limb rests
on a single number with an unswept past-due invoice sitting next to it. OE 26 now rules that invoice
out by owner with a reason the agent can check, so the number is defended rather than merely asserted.

## 6. B6. PROPAGATE TO S1 flags

**None.** The prompt is unchanged at 261 words, no tool names, no dashes, no pre-solving. The one
remaining blocker is a deletion inside `6_Oracle_Events.txt` and touches no prompt clause.

## 7. B8. OE completeness, must-take steps with no covering OE

All six prompt deliverables are covered: make-ready corrections OE 30, both review meetings OE 31,
the Brooke email OE 33 with the recipient resolved at OE 32, the tracker update OE 34, the new item
OE 35, the channel post OE 36.

**The round-3 completeness gap is closed.** The Mesa Vista 4C ownership and money reconciliation now
has three covering treatments, at OE 26, OE 30 and OE 33. No must-take investigation step is left
without a covering OE. Completeness moves 4 to 5.

## 8. B9. Service mapping

Seven services carry named calls and all resolve: linear, slack, airtable, quickbooks, gmail,
gcalendar, contacts. 32 of 32 tool tokens resolve against `7_Server_Tools_Details.json`, and 25 of 25
checked parameters are correct, including every StarPM trap: `slack_send_message.message` with no
`payload` or `text` in the schema, `create_draft.body` with no `content`, `save_issue.team` with no
`teamId`, `update_records_for_table.baseId/tableId/records`, `search_records.baseId/table/query`,
`get_event.eventId`, `list_events.calendarId/fullText`, `list_issue_statuses.team`,
`get_aged_receivables.customer`.

**One gap persists, unchanged from round 3.** HubSpot is the eighth service. OE 10 cites
`comp_mesaverde`, three deal ids and `ticket_87552e6b23bc5a92bd2641b9054b8c13` in prose, and no
HubSpot call is named anywhere in the file. Refinement 5, not a blocker, because the Finley to Mesa
Vista link is established three other ways inside the same step.

## 9. B-RULE13. Single-target uniqueness, every-service sweep, naive-agent simulation

**Single-target uniqueness: PASS on every write target.**

| Write target | Uniqueness check |
|---|---|
| rec98bdfeec73545e | one row by id. Unit "Sunset Ridge 104B" carries 2 rows, so the id is load-bearing and is used |
| rec987aae7d522057 | one row by id. Unit "Sunset Ridge 309C" carries 4 rows including reca06d89f1a4ac5b which must not move, so pinning by id is mandatory and is done |
| rec8b679d92f30753 | the only Ridgeview row in the table |
| Harris Rescheduled event | base `qqbwq3s2h7wh5udoek2940mffk` has **no bare row stored**; 4 per-calendar rows exist and OE 31 names two of them correctly, `-b6a1e41c` on teresa.wood and `-0f82233a` on brooke.phillips |
| Finley review row | `8mwlxrq5w5oodwdpmvo83e00f2-b0504ab4` verified as the lisa.smith row; bare base id not stored |
| Brooke Phillips | exactly one contact, `c46d47256fd95ca6aca770c8dddda5eb` |
| C006 | exactly one channel named #owner-relations |
| OPS-10 | the only issue carrying "Mid-Year" in its title |
| New issue | graded on title and description, not on a number, since next_issue_number is 1000 |

**Every-service sweep including Calendar.** The round-3 FAIL is fixed: Mesa Vista 4C is now swept
outside tblMakeReady and the 13 rows across four stores are adjudicated at OE 30 and OE 26. 309C,
310C and 107A remain Airtable-only, verified. 104B remains Airtable plus the two Fernwood invoices,
verified. **207A is Airtable-only, verified with Gmail decoded**, which is the finding in section 0.

**Unreconciled future confirmed events (F9).** Nine distinct confirmed events sit on or after
2026-07-01. The OE names two, `42b119cbt7xd0vnhw6dwvdqizo` on 07-13 and `0hjw400xgjb3j7ay7ynuaqbnpi`
on 07-15. `j3ulusavtqgvwge31s21ep5c8w` "Mesa Vista HOA Management Review" on 2026-07-08 is on an
in-scope portfolio and is still named nowhere. Refinement 4, carried forward.

**Naive-agent simulation.** All six writes clean, see section 3.

## 10. Hygiene and validator

| Check | Result |
|---|---|
| Identifiers | 98 extracted, **98 resolve verbatim**, zero misses |
| Tool names | 32 distinct, **32 resolve** |
| Tool parameters | 25 of 25 checked correct, 4 of 4 traps avoided |
| Em dash, en dash, minus, non-breaking hyphen, figure dash, horizontal bar, non-breaking space | **0 of each** |
| Non-ASCII characters | **0 in the whole file** |
| `validate.py --phase oe` | **PASS, 0 fails, 0 warns**, 3 notes |
| Exact duplicate sentences | 0 |
| Semantic duplicate sentences | **1**, see BLOCKER A |

# BLOCKERS

## BLOCKER A. OE 30 carries two consecutive contradictory sentences about 207A, and the first one is false.

**This is a blocker, and it is my own error.**

The BLOCKER 1 replacement was inserted but the sentence it was supposed to replace was not removed.
OE 30 now reads, consecutively:

> On 207A the only rows in the universe carrying that unit string outside tblMakeReady are Gmail and
> Slack messages that do not bear on turn status, so the only reading available is that the later row
> supersedes the earlier ones, and with nothing to check it against neither direction of correction
> can be graded. On 207A no record on any other service names the unit at all, so the only reading
> available is that the later row supersedes the earlier ones, and with no cross-service check on it
> neither direction of correction can be graded.

The **second** sentence is the original and it is **true**. The **first** is mine and it is **false**:
there are no Gmail or Slack rows carrying 207A, and there are no rows outside tblMakeReady carrying it
at all. Verified across all 33 stores with Gmail bodies base64url decoded, result 3 rows, all Airtable.
The clause "so the only reading available is that the later row supersedes the earlier ones" appears
twice in the file, which is the mechanical signature of the unremoved duplicate.

Why this is a blocker rather than a note, on the same standard I applied in round 3: it is a false
statement of universe fact in an OE step that S3 writes evidence fields from, it directly contradicts
the sentence immediately after it, and it is the same defect class AUDIT round 3 escalated on the
Ridgeview sentence in this same step. I validated the claim as false by direct query, so I cannot
record it as a note and decline it.

Why it is cheap: 207A is ungraded in both sentences, the operative conclusion is identical and correct
in both, no criterion can rest on it, and the correct text is **already present in the file**.

**Exact fix, a deletion with no replacement.** In OE 30, delete the sentence beginning "On 207A the
only rows in the universe carrying that unit string outside tblMakeReady" and ending "neither
direction of correction can be graded.", keeping the sentence that begins "On 207A no record on any
other service names the unit at all". Nothing else in the step changes. No other phase re-runs.

After that deletion I would score OE Accuracy 5/5 and the file is GO.

# REFINEMENTS, carried to S3 as notes

None of these blocks. All five were re-verified this round and all five still stand.

**Refinement 2.** The Ridgeview 8,400.00 is billed three times: owner invoice 109367557444 to Finley,
plus two open vendor bills to Big Bend Restoration, 528539050604 (2026-481) and 301715729067
(PD-2026-084), both 8,400.00 and both open. Neither is named in the file. An agent sweeping QuickBooks
for "Ridgeview" gets six hits and may surface a 16,800.00 duplicate-pay exposure. One sentence in
OE 26 naming them as payables rather than owner receivables would close it.

**Refinement 3.** QuickBooks customer 102 "Mesa Verde Investments" at ap@mesaverdeinv.com shares its
domain with HubSpot `comp_mesaverde` where Finley is filed, and carries 1,150.00 past due. One clause
in OE 10 noting it is a separate customer, and that the HubSpot company also contains StarPM's own
Teresa Wood and Elias Navarro, would close the bridge.

**Refinement 4.** Confirmed future event `j3ulusavtqgvwge31s21ep5c8w` "Mesa Vista HOA Management
Review" on 2026-07-08 sits on an in-scope portfolio inside the horizon and is named nowhere. OE 35
asserts that exactly two items are carried nowhere. Naming this event and explaining why a booked
meeting is not unresolved work would protect that assertion.

**Refinement 5.** OE 10 cites `comp_mesaverde`, three deal ids and
`ticket_87552e6b23bc5a92bd2641b9054b8c13` but no HubSpot call is named anywhere in the file. Adding
`search_crm_objects` or `get_crm_objects` to the step would make the cited records reachable.

**Refinement 6, new and minor.** The Gmail body in thread `66132537181ecbe1` names "owner invoice
2026-537", and no record with that DocNumber exists; the real record is 2026-534. OE 26 and OE 30 do
not claim the numbers match, so nothing is wrong, but S3 must not write a criterion requiring the
agent to reconcile 2026-537, because it is unreconcilable by design.

## What is NOT a defect, recorded so it is not rediscovered

- **`66132537181ecbe1` is a Gmail thread id, not a message id.** The message is `5101c5a41dffa90a`.
  This is correct usage, not a defect: OE 18 and OE 21 both reach Gmail with `search_threads` and
  `get_thread`, and `get_thread` takes a thread id, so citing threads is the internally consistent
  choice. My round-3 description of the two ids as "near-duplicates" was wrong; one contains the other.
- **The four 4C vendor bills are `bill` entities, not invoices**, and QuickBooks rows nest their
  fields under `properties` with a lowercase `id`. A sweep keyed on `Id` returns nothing and can look
  like a missing record. All four exist.
- **OE 33's count accept-set does not weaken L1.** Every value in "two to four" exceeds Lisa's "one".
- **207A being Airtable-only is a property of the universe**, not an omission, and the original
  sentence says so correctly.

## Verdict rationale

Both of my round-3 blockers are closed, and closed properly. Every fact in every applied replacement
was re-derived this round from the split rather than accepted: the closed ticket, the owner email, all
four vendor bills, the QC event with all three calendar rows, the Castillo flag, the Castillo-billed
invoice, and the zero co-occurrence of "4C" and "Finley" across all 33 stores with Gmail decoded. The
make-ready count resolves to exactly two open on the latest row, so the accept-set is sound and the
lever survives. Council A's blocker is closed on both legs, with both offered Linear queries returning
three issues including OPS-32 and the three-calendar `list_events` returning exactly three distinct
base events including the eviction hearing, whose per-calendar row and description are exact.

Nothing else broke. 98 of 98 identifiers, 32 of 32 tools and 25 of 25 parameters resolve, all four
StarPM parameter traps are avoided, there is not a single non-ASCII character in the file, the
validator passes with zero fails and zero warns, all five selected levers are preserved with L2 and
L11 strengthened, the contrast pair is intact and its Finley limb is now defended rather than merely
asserted, RULE13 passes on every write target, and density clears the V4 40+ per-model target with
margins of +25 on Opus and +32 on Gemini against a floor that rose from 85 to 86.

One thing stops it, and it is mine. My BLOCKER 1 replacement text carried a false clause about Gmail
and Slack rows on 207A, built on a sloppy substring sweep of "207" that matched HubSpot ids, a Gmail
history_id, OPS-207 and Slack timestamps. It was applied verbatim as I wrote it, the sentence it was
meant to replace was left in place, and OE 30 now states both a false claim and its true contradiction
back to back. The fix is to delete my sentence and keep the original, which is already there.

That is a one-line deletion in one step, requiring no re-derivation, no universe work, no prompt
change, no lever change and no downstream re-run.

VERDICT: BLOCK
