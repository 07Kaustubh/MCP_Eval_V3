# Council B round 5: adversarial QC on the current bytes

Task: Tasks/46_6a62ccb6ce2323b4b9e0c8d8
Artifact: `6_Oracle_Events.txt`, 36 steps, 42189 chars (r4 state was 41315)
Universe: starpm, V4, dual-model, today 2026-07-01 America/Chicago
Method: file re-read fresh. Every query the file names was simulated against `_aux/Universe_Split/`
with Gmail bodies base64url decoded before matching. Prior rounds were read only to establish what
was promised, then set aside. Read-only except this report.

## SUB-DIM LINES

SUB-DIM OE Completeness -> SCORE 5/3-4-5 NON-FAIL -> REASON all seven prompt deliverables carry a covering step, seven of eight services carry named calls, five S3 decompose directives are present, and the 4C ownership and money leg that previously sat on no named call is now returned by four simulated legs (search_records on tblMaintenanceTickets, search_threads plus get_thread, search_bills, list_events on two calendars).

SUB-DIM OE Accuracy -> SCORE 5/3-4-5 NON-FAIL -> REASON Accuracy is now 5: the single false sentence that held r4 at 4 is deleted and the surviving claim measures true (exactly 3 records contain "207A", all in airtable.airtable_records, zero outside), all 98 identifiers resolve, zero unknown tool tokens across 34 named tools, and every added retrieval leg returns exactly what the file says it returns.

**Stated plainly, as asked: Accuracy is now 5.** The r4 deduction was attributed solely to the 207A
sentence. That sentence is gone. I re-derived the measurement rather than accepting it: sweeping the
literal string `207A` across all 33 stores with Gmail decoded returns 3 rows, all in
`airtable.airtable_records` (`reca4aa17f0755b55` selProg, `rec4081fd2ccde95a` selProg,
`rec591a0f70432651` selReady), and 0 rows outside Airtable. The surviving sentence "On 207A no record
on any other service names the unit at all" is therefore correct.

## 0. Closure of the thirteen unreachable identifiers

Each fix was simulated, not read. Every one closes.

| Fix | Simulated result |
|---|---|
| OE 13 names `search_estimates` query "Harris" | returns exactly 3 estimates and they are exactly `300730861679`, `308892996802`, `981816261186`. `search_invoices` query "Harris" returns 3 invoices and zero overlap with those ids, so the file's stated reason is exact |
| OE 30 names `search_records` on tblMaintenanceTickets query "Mesa Vista" | returns 3 rows including `reca424761ae15355` |
| OE 30 names `search_threads` query "make-ready" plus `get_thread` | returns 8 threads including `66132537181ecbe1`, subject "mesa vista 4c make-ready complete. cost summary for your records" |
| OE 30 names `search_bills` query "Mesa Vista" or "4C" | "Mesa Vista" returns 5 bills, "4C" returns exactly 4. All four cited bills return on both queries |
| OE 30 names `list_events` across carlos.mendez and wesley.tran | each calendar carries a row of base `0hjw400xgjb3j7ay7ynuaqbnpi`, both status confirmed, start 2026-07-15, location "Mesa Vista, Unit 4C" |
| the two Fernwood invoices are gone | `232547977309` and `509422853402` no longer appear in the file |

Two collateral checks on the fix text:

- Each of the four bills matches the label the step gives it, verified against the Line description:
  `195089456477` Sunshine Cleaning post-move-out deep clean 387.00, `696089964235` Permian interior
  repaint 1340.00, `546359391323` Permian bedroom closet trim touch-up 85.00, `991582431419` Alamo
  unit condition inspection and punch list 85.00.
- The stated reason the QC event is missed by earlier legs is exact. The three rows of
  `0hjw400xgjb3j7ay7ynuaqbnpi` contain neither "Ridgeview" (OE 19 fullText) nor "Portfolio Review"
  (OE 28 fullText), and none sits on lisa.smith (OE 27).
- The replacement for the removed Fernwood sentence is true. Sweeping `104B` across all stores and
  excluding tblMakeReady returns exactly two rows, both QuickBooks, both carrying "Fernwood". And
  "No record outside Airtable carries 309C at all" measures true: zero hits in all non-Airtable stores.

Every one of the 98 id-shaped tokens in the file resolves to a real record. Zero unresolved.

## 1. The question asked directly: did the added legs introduce a new claim, move a graded target, or widen an accept-set?

**No, no, and no.** I answered this from a word-level diff of the immediately prior bytes against the
current bytes rather than by reading the new text sympathetically.

The diff contains exactly four substantive changes:

1. **OE 13** gains one retrieval sentence naming `search_estimates`. It asserts two things beyond
   retrieval, that the rows are entity_type estimate and that `search_invoices` does not return them.
   Both measured true. No new fact about the world, no target.
2. **OE 16 and OE 17** replace the correction basis with supersession and add the note that the July
   dates sit after universe today. This is a **tightening, not a widening**. The old basis at OE 16
   was "A unit whose repaint has started is not Scheduled", and the note it rests on says "Repaint
   started July 15", which is fourteen days after universe today 2026-07-01. The old text asserted a
   present-tense fact about a future event. The new text does not. Graded targets `rec98bdfeec73545e`
   and `rec987aae7d522057` are unchanged, both still to selProg.
3. **OE 30** gains the retrieval sentence for 4C and restates the same two corrections on the
   supersession basis. The graded set is character-for-character the same three rows, and the S3
   decompose directive is unchanged: `rec98bdfeec73545e` selProg, `rec987aae7d522057` selProg,
   `rec8b679d92f30753` selProg.
4. **OE 30** gains "As with 4C, an agent that leaves the 207A rows alone and an agent that corrects
   them are both acceptable." This is an **explicitation, not a widening**. The immediately preceding
   sentence already said "with no cross-service check on it neither direction of correction can be
   graded", and the paragraph already opened "Neither pair is graded". The new sentence states the
   consequence that was already binding. It brings 207A into line with the three-behaviour accept
   statement 4C already carried.

Nothing in the diff touches OE 31, OE 33, OE 34, OE 35 or OE 36, so no deliverable accept-set moved.
The prompt licenses each write the file grades: record correction, meeting resolution, email, tracker
comment, new item, channel post.

## 2. B2 adversarial alternate path

I looked for a defensible agent behaviour the file would mark wrong.

- **Ungraded pairs are explicitly released.** 4C names three acceptable behaviours, 207A now names
  two, Unit 14 names two, and the OE 35 target carries an either/or accept-set. The file uses
  "must not be marked down" three times, "are both acceptable" twice, "are all acceptable" once,
  "equally correct" once, "Either verb is correct" once.
- **OE 31 verb choice** is released for Harris (delete_event or update_event) and for Finley
  (update_event or create_event), each with the per-calendar-row id requirement stated.
- **OE 34** releases the OPS-10 state change as optional and forbids grading it.
- **One residual, carried below as R3.** An agent that raises the 2026-07-08 Mesa Vista HOA
  Management Review as an unresolved Finley item would fail OE 35's accept-set, and OE 35 gives no
  guidance on it.

No alternate path is punished except R3.

## 3. B3 per-model tool-call density

The file names 34 distinct tools across 66 raw tool mentions in 36 steps, plus 35 explicitly spelled
out fan-out legs (three Harris calendars, three Ridgeview calendars, four Portfolio Review calendars,
two OE 30 calendars, two search_invoices passes, four plus three read_invoice passes, six
get_credit_memo confirmations, two search_customers, two search_credit_memos).

The r4 finding stands and is strengthened: **the applied fixes only add calls.** The net change is
plus one `search_estimates`, plus one `search_records`, plus one `search_threads`, plus one
`get_thread`, plus one `search_bills`, plus two `list_events`, against minus zero (the two Fernwood
invoices were cited, never retrieved by a named call, so removing them removes no call).

Hardness Plan projection is Opus 50 to 77, midpoint 63.5, and Gemini 50 to 82, midpoint 66.0, against
a V4 gate of 40. Margin plus 23.5 and plus 26.0 before this round's additions.

VERDICT B3: **PASS**, both models, with the margin moving in the safe direction.

## 4. B4 per-lever preservation

| Lever | Carrier in current bytes | Status |
|---|---|---|
| **L1 Latching** | Lisa's spring claim reached at OE 8 through `slack_read_thread`, then each limb dispositioned: 94 percent at OE 11 and OE 21, 97 percent at OE 21, "one unit still in make-ready" refuted at OE 14, water heater misattribution at OE 20, cleared late payment at OE 21 and OE 33 | PRESERVED |
| **L2 Structured-DB skip** | QuickBooks AR at OE 22 to OE 26 with `get_aged_receivables` named for the Harris negative; unmirrored Calendar at OE 27 to OE 29, plus the OE 30 leg on carlos.mendez and wesley.tran and the OE 19 leg on john.smith, all calendars the persona does not hold | PRESERVED and STRENGTHENED by the OE 30 addition |
| **L7 Multi-write diversification** | eight write tools named across five services: airtable `update_records_for_table`, gcalendar `update_event` / `delete_event` / `create_event`, gmail `create_draft`, linear `save_comment` / `save_issue`, slack `slack_send_message` | PRESERVED, matches the plan's six writes across five services |
| **L10 Reversal / supersession** | Harris double booking at OE 28 and OE 31 with both base ids present; OPS-10 in state_OPS_0 against two transition announcements at OE 4; OPS-39 against OPS-93 at OE 11 | PRESERVED |
| **L11 Net-vs-gross** | OE 25 carries Balance equal to TotalAmt, absent LinkedTxn and the RemainingCredit trap; OE 26 names the 7,325.00 netting error explicitly against 10,980.00 gross and 3,655.00 unapplied | PRESERVED |
| **Contrast pair** | OE 33 carries "operationally blocked" for Harris against 0.00 open receivable and "cash-blocked" for Finley against 10,980.00, and OE 24 names the "both owners are behind" collapse as the failure it guards | PRESERVED |

Re-derived independently: Finley open balances sum to exactly 10980.0 across `2026-494`, `2026-303`
and `4421` with `5848` settled at 0.0; Finley credit memos total exactly 3655.0 and Harris 1975.0,
and on all six Balance equals TotalAmt with no LinkedTxn.

## 5. B6 propagation

Nothing propagates back to S1. Every graded write maps to a prompt clause: record correction to
"put those records right", meeting resolution to "Do the same for their review meetings", email to
"Put an email together for Brooke", tracker comment to "Bring the mid-year review item up to date",
new item to "open a separate item", channel post to "Post a short version in the owner relations
channel". OE 31's both-meetings reading is sound because the prompt's condition is per meeting and
OE 29 establishes that neither settled.

## 6. B8 completeness

All seven prompt deliverables carry a covering step, and every must-take investigation step carries a
named call. Five S3 decompose directives are present, at OE 30, OE 31, OE 33, OE 35 and OE 36.

## 7. B9 service mapping

linear 6 of 6 tools, slack 5 of 5, airtable 5 of 5, quickbooks 8 of 8, gmail 3 of 3, gcalendar 6 of 6,
contacts 1 of 1. Seven of eight services carry named calls; hubspot appears only as prose at OE 10,
where it is named as a route that does **not** work, which matches the Hardness Plan's 0 to 2 call
allocation.

## 8. B-RULE13

- **Single-target uniqueness.** The three graded rows each resolve to one record. One caution:
  Sunset Ridge 309C carries **two** selSched rows, the graded `rec987aae7d522057` and the explicitly
  excluded `reca06d89f1a4ac5b`. The file distinguishes them by content and forbids touching the
  second. Carried to S3 as R6.
- **Every-service sweep including Calendar.** Nine distinct confirmed events sit on or after
  universe today. Seven of the nine are on properties or people outside both owners' scope. Two are
  reconciled by name in the file (`42b119cbt7xd0vnhw6dwvdqizo` 07-13 Ridgeview follow-up,
  `0hjw400xgjb3j7ay7ynuaqbnpi` 07-15 Mesa Vista 4C QC). The two the Hardness Plan singled out are
  **not** reconciled by name. Carried as R3.
- **Naive-agent simulation.** Reading the prompt without the OE in view, the two owners, the four
  workstreams and the six writes are each unambiguous, and the "separate item" phrasing supports the
  either/or accept-set OE 35 defines.

## 9. BLOCKERS

**NONE.**

I applied one decisive test to the strongest candidate, R1 below: does any graded criterion S3 will
write depend on a record the file leaves unreachable? Traced end to end, the answer is no. The
detail is in R1.

## 10. REFINEMENTS, as notes for S3

**R1. A second cohort of the same reachability class the round-4 fix closed. Nine Airtable rows are
cited with accurate row-level facts that no named query returns.**

Seven tblMakeReady rows enumerated at OE 21 (`rec3782834f35df50`, `rec769c9f03f0b85f`,
`rec8005502043b755`, `rec91517a5acab558`, `reca8230a8fd9ff51`, `recc83c05d889b354`,
`receee45491536859`) and two tblMaintenanceTickets rows at OE 18 (`rec46234590708b5c`,
`recc0ecc885e9645e`). The named queries at those steps are `search_threads` on "collections" or
"past due" (OE 21) and `search_records` on "Finley" or "roof" (OE 18), and none of the nine comes
back from any of them. Only `reca8230a8fd9ff51` is reachable, via the OE 13 "Sunset Ridge" query.

Every fact asserted about the nine is correct. I verified the exact fldUnit strings on all seven, that
`rec94e86a3007dd5e` "Rio Bend - Unit 14" does not name her, that no Mitchell row sits on Mesa Vista,
that both tickets are selHigh with a null fldCompletionDate, and that seven rows in
tblMaintenanceTickets are open with the empty value stored four times as null and three times as an
empty string, exactly as OE 18 says.

**Why this is a refinement and not a blocker.** All nine are cited to keep something **out** of the
graded set, never to put something in. The one graded item that could have depended on them is OE 33's
late-payment correction, whose chain is "first notice on June 6 through a breached payment plan on
June 25 to a cure deadline that expired on June 29". I traced that chain and it does **not** depend on
the unreachable rows: message `2ae48555b3009a95` carries June 6, June 23, June 25 and June 29 together,
and it is reachable, because `search_threads` on "eviction" or on "authorization" returns thread
`621640f9e7aa6d46` ("eviction filing authorization. tanya mitchell. unit 14") which `get_thread` opens
to that message. Both queries are named at OE 18.

**Fix, one clause each, both simulated:** at OE 18 add `search_records` on tblMaintenanceTickets with
query "Tanya Mitchell", which returns exactly the two rows; at OE 21 add `search_records` on
tblMakeReady with query "Tanya Mitchell", which returns exactly the seven. No other text changes.

**R2. OPS-39 and OPS-93 are returned by no named `list_issues` query.** They are cited at OE 11 as an
illustrative parallel to the OPS-100 state-versus-narrative mismatch. Both exist and both are
described correctly. Neither bears on a graded target, so S3 writes nothing on them.

**R3. Two post-today confirmed events the Hardness Plan named for reconciliation are not reconciled
in the file and are reachable by no calendar leg it specifies.** `j3ulusavtqgvwge31s21ep5c8w`
(2026-07-08, Mesa Vista HOA Management Review) and `232wqgjdsa2cyz9mv4qtx5mncy` (2026-07-23, Q3
Make-Ready Planning and Budget Review, covering Las Vistas, Las Palmas and Mesa Vista). Both sit on
teresa.wood and brooke.phillips, but every OE leg touching those two calendars is fullText filtered on
"Harris", "Ridgeview" or "Portfolio Review", and neither event carries any of those terms. The three
unfiltered `list_events` legs are lisa.smith, carlos.mendez and wesley.tran, and neither event is on
those.

Neither event falsifies an OE claim. OE 18's "only open repair ticket" is scoped to tickets, and OE 15
and OE 35 turn on work being "carried nowhere", which a booked calendar event is not. The exposure is
narrow and belongs to S3: an agent that raises the Mesa Vista HOA review as the unresolved Finley item
lands outside OE 35's accept-set. S3 should grade OE 35 on the two named candidates only, and the
cleanest closure is one clause at OE 35 saying a booked meeting is carried and therefore not the
target.

**R4. Mixed identifier convention on Gmail.** "Gmail `2ae48555b3009a95`" at OE 13, OE 18, OE 21 and
OE 30 is a **message** id (its thread is `621640f9e7aa6d46`), while "Gmail `66132537181ecbe1`" at
OE 30 is a **thread** id. `get_thread` takes a threadId. Both are reachable, so this costs nothing at
grading time, but S3 should quote content rather than either id.

**R5. One loose clause survives the OE 16 and OE 17 tightening.** OE 30 still opens the three
corrections with "whether because the work has started or because the question that row was waiting on
has been answered". "The work has started" is true for `rec8b679d92f30753`, whose repair event
`whd6zys0hw7zbsh11m9vqv4m4i` sits on 2026-06-08 in the past, and false for the two Sunset Ridge rows,
whose July dates are after universe today. The step then restates each of the three correctly, so the
disjunction is not false across the set. Worth tightening for consistency with the OE 16 and OE 17
notes rather than for correctness.

**R6. F7 caution for S3 on 309C.** Sunset Ridge 309C carries two selSched rows. Only
`rec987aae7d522057` is graded; `reca06d89f1a4ac5b` must be left alone. S3 must pin the graded row by
content, the deep-clean crew question answered on two later rows, rather than by "the 309C scheduled
row", which matches both.

## 11. Standing gates re-run on the current bytes

| Gate | Result |
|---|---|
| em-dash / en-dash | 0 / 0 |
| step count | 36 |
| identifiers resolving | 98 of 98 |
| unknown tool-shaped tokens | none, 34 tools all in the StarPM catalog |
| tool parameter names against the catalog | every parameter checked matches, including `search_records` baseId / table / query, `update_records_for_table` baseId / tableId / records, `get_thread` threadId, `list_events` calendarId / fullText |
| money totals | Finley 10980.0 open and 3655.0 credits, Harris 0.0 open and 1975.0 credits, all re-derived |

## Verdict rationale

The one defect that held Accuracy at 4 in round 4 is gone, and the claim that replaced it measures
true. All thirteen unreachable identifiers now return from calls the file names, every one confirmed
by simulation rather than by reading. The additions are retrieval only: they introduce no new claim
about the universe beyond two statements I measured true, they leave all three graded record targets
and both graded calendar targets exactly as they were, and the one accept-set sentence they add makes
explicit a release that the preceding sentence already granted. The OE 16 and OE 17 rewrite moves the
correction basis off a future-dated present-tense assertion, which raises accuracy rather than
widening anything.

Six refinements remain. The largest, R1, is a genuine second cohort of the reachability class and I
am not going to soften it: the round-4 fix closed thirteen named identifiers rather than sweeping the
class, and nine more sit in the file. I traced its worst case to ground before calling it a
refinement, and the graded late-payment chain it could have compromised is independently reachable
through a thread the file already names. None of the six moves a graded target, an accept-set or a
deliverable, and each has a one-clause fix.

VERDICT: GO
