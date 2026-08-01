# Council B - Adversarial QC + Density + Hardness Preservation

**Phase:** S2 (Oracle Events) - **Task:** `Tasks/46_6a62ccb6ce2323b4b9e0c8d8`
**Deliverable:** `6_Oracle_Events.txt` (36 OEs, 71 lines)
**Universe:** `starpm`, V4 framework, dual-model (Opus 4.8 + Gemini), universe today **2026-07-01** America/Chicago
**Mode:** read-only. No file was edited.

**VERDICT: BLOCK** - 6 MAJOR, 5 MODERATE, 6 MINOR. Both OE sub-dims score 3/5. One conditional `PROPAGATE TO S1`.

---

## Evidence provenance

Re-derived from `_aux/Universe_Split/` in this session, not copied from any prior report:

| Claim | Method | Result |
|---|---|---|
| Calendar row count | `len(gcalendar.gcalendar_events.json)` | **565 rows** |
| Events on/after 2026-07-01 | filter on `start_dt` | **27 rows / 9 distinct base ids** |
| Lisa on any future event | attendee scan across all 9 | **0 of 9** (confirms Hardness Plan) |
| 30 tool names used in the OE file | membership test against `StarPM_Base_Universe/7_Server_Tools_Details.json` (276 tools) | **30 of 30 exist** |
| Slack message count | `len(slack.slack_messages.json)` | **580** |
| OE 8 `message_ts` value | read row `831d2b6760205432a20487e2664a607e` | `ts` = **1780002480.000000**, matches OE 8 exactly |
| OE 23/24/25/26 arithmetic | recomputed | **all four totals correct** |

**Not re-derived in this session, and therefore not asserted either way:** OE 7's 43/36/7 message split, the "346 of 580 thread replies" figure, OE 27's "20 calendars", every OE parameter *name* (only tool *names* were verified), and the Linear `team_001` description text asserting Airtable primacy. These are handed to Council A / AUDIT rather than scored here.

---

## FINDINGS

### F1 - MAJOR - OE 15 - "the one genuinely unresolved item in either cluster" is false, and is falsified inside this same file

**Evidence.**

1. **Contradicted by OE 18, two OEs later.** OE 18 records `recb4aeaed326f156` (MT-2026-047), `fldPriority selHigh`, `fldCompletionDate` empty, described as roof damage that "appears to exceed routine patching and requires professional evaluation" and flagged "for priority assessment and licensed roofing contractor inspection". OE 18 then calls it "the only open ticket in either owner's scope". The file therefore asserts two different sole-open-item claims about the same two clusters.
2. **Contradicted by OE 19.** `rec8b679d92f30753` (Ridgeview - Roof Section, `selSched`) is an unfinished structural repair on a Finley property.
3. **Contradicted by OE 23 and OE 26.** Invoice `2026-494`, $8,400.00, DueDate 2026-05-31, is 31 days past due as of universe today and is explicitly called "the money question the prompt anticipates".
4. **Unreconciled against Calendar (hard rule 13(b) / F9 UNRECONCILED_FUTURE_EVT).** Verified this session, 9 confirmed events sit on or after 2026-07-01, three of which bear on the claim:

| base id | date | title | bearing |
|---|---|---|---|
| `42b119cbt7xd0vnhw6dwvdqizo` | 2026-07-13 09:30 | Vendor Walk-Through - Ridgeview Roof Repair Follow-Up | **Finley property.** Confirmed, 2 rows, `pete.donovan@gmail.com` still `needsAction`. Future work on a Finley asset. |
| `0hjw400xgjb3j7ay7ynuaqbnpi` | 2026-07-15 10:00 | Make-Ready QC Inspection - Mesa Vista 4C | Mesa Vista 4C is inside Finley's cluster (OE 14, `recbd087a4abd605b` / `recc8534b3fd13954`). A QC inspection still to occur means that turn is not closed. |
| `j3ulusavtqgvwge31s21ep5c8w` | 2026-07-08 14:00 | Mesa Vista HOA Management Review | Confirmed, 4 rows, Finley's property. |

The Hardness Plan pre-registered exactly this obligation: *"Any 'this is complete' or 'this is the only open item' framing in the OEs or rubrics must reconcile against these."* OE 15 does not.

**Why it is MAJOR rather than cosmetic.** OE 35 pins the new-issue write to this item on the strength of this claim. If the claim is false, the write's justification is false, and S3 will build a criterion on a premise the universe refutes.

**Fix - replacement wording for OE 15.** The real discriminator is *disposition*, not *openness*, and it is strong once stated:

> OE 15: Read rec88734a4fdfde57 (Mesa Vista 310C, selSched, fldMoveOut 2026-05-22, fldTargetReady 2026-05-22). Its fldNotes2 reads "Move-out inspection booked for July 16. Maintenance flagged possible subfloor issue under bathroom tile - needs assessment before scope is finalized." This is the only item in either cluster that is undispositioned: no assessment has been ordered, no vendor is named, no date is booked, and no record in any service closes it or advances it. It is distinct from the other open work in Finley's cluster, which is open but dispositioned: MT-2026-047 from OE 18 and the Ridgeview roof row rec8b679d92f30753 from OE 19 are the same structural repair, already carrying owner authorization from Robert Finley, Pete Donovan as approved vendor, a signed-off $8,400 estimate, invoice 2026-494 raised against it, and a follow-up vendor walk-through booked on the calendar for 2026-07-13. Mesa Vista 4C also carries a make-ready QC inspection booked for 2026-07-15. Those items need chasing; the 310C subfloor needs a decision that nobody has made. Mesa Vista 310C is a single-row unit string, so it is uniquely addressable.

**Optional enrichment (not required to clear this finding).** MT-2026-047 having an empty `fldCompletionDate` while the work it describes is authorized, vendored, priced and invoiced is itself a records-hygiene mismatch worth naming in the OE 33 draft body. It cannot be a write target: Handoff obligation 5 makes `tblMaintenanceTickets` read-and-report only.

---

### F2 - MAJOR - OE 35 - rule 13(c) naive-agent hit on the new-issue target

**Is this a rule-13(c) hit? Yes.** Reading `5_Prompt.txt` with the OE file closed, the operative clause is "open a separate item for whatever is still genuinely unresolved so it does not quietly disappear once this is handed over." Nothing in the prompt points at a subfloor. A competent agent that has just retrieved `recb4aeaed326f156` (MT-2026-047), a **high-priority ticket with an empty completion date** whose text says the damage "requires professional evaluation", will reasonably nominate that as the unresolved item. The OE file actively encourages the mistake: OE 18 labels it "the only open ticket in either owner's scope".

Two further defensible naive picks exist: invoice `2026-494` ($8,400, 31 days past due, OE 23/26) and the missing Finley review meeting itself (OE 29, "the meeting that comment describes does not exist"). The OE chain forecloses none of the three.

**Interaction with Handoff obligation 6b.** That obligation requires S3 to pin the cardinality at exactly one issue. Pinning "exactly one" while two or more targets are defensible manufactures the F8 NON_ATOMIC_ENUM shape from the other direction: the count is pinned but the identity is not.

**Fix - replacement wording for OE 35.**

> OE 35: Open one new issue for the work that survives the hand-off using save_issue with title naming the unresolved item, team "team_001", project "proj_002" and a description. The item is the Mesa Vista 310C subfloor assessment from OE 15. The competing candidate is MT-2026-047 from OE 18, and the discriminator must be applied rather than assumed: MT-2026-047 and the Ridgeview roof row rec8b679d92f30753 describe the same structural repair, which already carries owner authorization from Robert Finley, Pete Donovan as approved vendor, a signed-off $8,400 estimate, invoice 2026-494, and a vendor walk-through booked for 2026-07-13. That work is dispositioned and belongs in the hand-off as an item to chase, not in a new issue. The 310C subfloor has no assessment ordered, no vendor, no date and no decision anywhere in the universe, so it is the only item whose scope cannot be finalized. Exactly one issue is expected, matching the prompt's "a separate item"; S3 must pin that cardinality explicitly and must not write a criterion that passes on "one or more items". The created issue's own identifier cannot be predicted because team_001 has next_issue_number 1000, so it must be graded on title and description rather than on a number.

---

### F3 - MAJOR - OE 30 - the correction set is not closed, and "put those records right" produces zero writes on any Finley record

**Evidence.** OE 30 writes exactly two rows, `rec98bdfeec73545e` (Sunset Ridge 104B) and `rec987aae7d522057` (Sunset Ridge 309C). Both are Harris. The mismatch analysis that produced them runs in OE 16 (104B pair) and OE 17 (309C quartet), and it covers Sunset Ridge only.

- **OE 14 enumerates 8 Mesa Vista rows** (`rec23600780ef4053`, `rec35a6c4f2e50657`, `reca4aa17f0755b55`, `rec4081fd2ccde95a`, `rec591a0f70432651`, `rec88734a4fdfde57`, `recbd087a4abd605b`, `recc8534b3fd13954`) and never compares any `fldTurnStatus` against its `fldNotes2`.
- **OE 19 surfaces `rec8b679d92f30753`** (Ridgeview roof, `selSched`) and never tests it either.
- **The Hardness Plan names that exact row as a qualifying record.** Its CORRECTION block on the calendar clause states: *"Both owners have a qualifying row (`rec987aae7d522057` Sunset Ridge 309C, Harris, `selSched`, notes about confirming a July 21 vs July 23 crew slot; `rec8b679d92f30753` Ridgeview roof, Finley, `selSched`)."* OE 30 carries the Harris row and drops the Finley one, with no stated reason.

**Is the set as written complete and defensible? No, on both counts.** It is not complete because the sweep was never run on 9 of the 16 rows in scope. It is not defensible because the OE gives no reason for the asymmetry, while the upstream plan asserts a Finley row qualifies.

**Is zero writes on Finley records a defect? Yes, a compound one.**
1. It leaves the correction set **data-indeterminate**. An agent that does run the analysis on Mesa Vista or Ridgeview will write rows the OE does not name. At S3 that becomes either an unfair fail (agent did more correct work and scored less) or an unbounded accept-set. Handoff obligation 10 requires "one atomic criterion per genuinely-mismatching row", which is unwritable until the set is closed.
2. It makes the **contrast pair asymmetric in the action set**. The contrast (F-B4 below) is Harris operationally blocked versus Finley cash-blocked. If every operational *write* lands on Harris, the design silently teaches that Finley has no operational state, which is false: he holds 8 Mesa Vista rows plus a structural roof repair.
3. It is a live **B2(a) alt-path**, treated below.

**Constraint interaction S2 must resolve, not defer.** Handoff obligation 10 excludes **Mesa Vista 207A** (3 rows) and **Mesa Vista 4C** (2 rows) as pin targets. If the sweep finds a genuine mismatch on either, S2 has a direct conflict between "correct every mismatching row" and "never pin an ambiguous target". That must be adjudicated at S2, not pushed to S3.

**Fix.** Insert a new OE between 19 and 20 that closes the set, and make OE 30 inherit from it:

> OE 19a: Run the same fldTurnStatus-against-fldNotes2 comparison across Robert Finley's rows that OE 16 and OE 17 ran across Harry Harris's. Cover all 8 Mesa Vista rows from OE 14 and the Ridgeview row rec8b679d92f30753 from OE 19, and record a verdict for each: either the recorded status contradicts the notes, or it does not and the reason it does not. [S2 fills the per-row verdicts from the split before this OE ships.] This closes the corrected-row set so that S3 can write one atomic criterion per genuinely-mismatching row rather than an open-ended one.

OE 30 must then either add every Finley row that qualifies, or state in terms why none does. If S2 concludes `rec8b679d92f30753` does **not** qualify (a plausible reading: `selSched` is correct because the repair has not started and the walk-through is booked for 2026-07-13), the OE must say so explicitly, because the Hardness Plan asserts the opposite and the two artifacts would otherwise contradict each other on the record.

---

### F4 - MAJOR - OE 31 - "eventId set to the rescheduled instance" is an F7 AMBIGUOUS_TARGET

**Is it ambiguous? Yes, unambiguously so.** "The rescheduled instance" resolves to base id `qqbwq3s2h7wh5udoek2940mffk`. Calendar in this universe stores **one row per invitee calendar**, and every stored row id is suffixed (OE 28 and OE 29 both demonstrate the shape: `1pon50ds1aevem63td6f7emdn3-b0504ab4`, `8mwlxrq5w5oodwdpmvo83e00f2-b0504ab4`). The bare base id therefore matches **4 stored rows**, and `lisa.smith@starpm.com` holds **none** of them.

This is a direct hit on **Handoff obligation 1** ("Never pin a bare calendar base id (F7 AMBIGUOUS_TARGET) ... Pin the per-calendar row, or describe by content plus the calendar it sits on") and on the Hardness Plan's own CORRECTION block, which records that the original "safe to pin" certification of this exact pair "was FALSE".

OE 28 also prints both bare base ids, but OE 28 is a read step and it does name Lisa's row on the accepted instance. The write step, OE 31, is the hit.

**Fix - replacement wording, first half of OE 31.**

> OE 31: Resolve the duplicated Harris review on the calendar. Calendar stores one row per invitee calendar, so the rescheduled instance is not a single target: it carries 4 stored rows and lisa.smith@starpm.com holds none of them. The target must be described as the event titled "Harry Harris Mid-Year Portfolio Review (Rescheduled)", 2026-06-03 15:00 to 16:30, on whichever attendee calendar carries it, never by a bare base id. Because Lisa holds no row she cannot respond to it, so the accepted paths are delete_event or update_event, both of which are eventId-addressed with calendarId optional, so she is not gated by calendar ownership. Either resolution is correct provided the two confirmed instances stop standing as two separate live meetings and the instance that survives is the 2026-06-02 12:15 to 12:45 one that all four attendees accepted. S3 must pin this target by full title plus calendar and must not copy a bare base id into a criterion.

---

### F5 - MAJOR - OE 31 - `respond_to_event` "accepted" on a six-week-old event settles nothing, and "may use" conflates required with optional

**Does accepting it settle anything? No.** The Finley mid-year review `8mwlxrq5w5oodwdpmvo83e00f2` is dated **2026-05-19 11:45 to 13:15**, six weeks before universe today 2026-07-01. Three independent reasons the proposed action is void:

1. **The meeting is in the past.** Changing an RSVP on a meeting that already happened produces no future review and discharges nothing the prompt asked for. The prompt's clause is "if either of those did not end up properly settled", which is about the outcome, not the RSVP field.
2. **The owner was never invited.** OE 29 itself records "Robert Finley not an attendee at all". An owner review with no owner is not a review, so no RSVP state makes it one.
3. **It would flip the persona's own recorded position.** Lisa's row `8mwlxrq5w5oodwdpmvo83e00f2-b0504ab4` currently reads `declined` (Handoff obligation 1, row 3). "Accept a meeting you declined, six weeks after it did not happen" is not a defensible end state, and a rubric built on it would be graded against an action no competent agent takes.

**Does "may use" conflate required with optional? Yes.** OE 31's Finley sentence is entirely permissive ("the agent does hold a row and **may** use respond_to_event ... **or** update_event"), and it names no required end state. But the Hardness Plan CORRECTION block "the calendar defect is NOT Harris-only" and Handoff obligation 12 both make the Finley calendar beat **mandatory**: *"The prompt's 'if either of those did not end up properly settled' fires on BOTH owners, not just Harris. S2/S3 must not build the calendar workstream as a single-owner beat."* As written, an agent that touches only the Harris duplicate satisfies OE 31.

**Fix - replacement wording, second half of OE 31.**

> For Robert Finley the calendar defect is different and must not be discharged by responding to the existing event. His mid-year review 8mwlxrq5w5oodwdpmvo83e00f2 sits on 2026-05-19 11:45 to 13:15, six weeks before universe today, with Lisa already recorded declined on her own row and Robert Finley not an attendee at all, against an OPS-10 comment placing it in the first week of June for 60 minutes in the afternoon. Accepting a meeting that is six weeks past and that the owner was never invited to settles nothing, so respond_to_event is not an accepted path here. A Finley action is required, not optional: the accepted end state is that his mid-year review is moved to a date the package can actually be delivered against, using update_event on a row of 8mwlxrq5w5oodwdpmvo83e00f2, or is explicitly restated so the record no longer presents the 05-19 slot as the review that took place. Do not confuse it with ti5zt1xubdggbehtp79um9mim6 "May Owner Report Review - Finley Properties" (2026-05-28 11:45 to 12:15, 3 rows, Lisa declined), which is a different meeting that also looks unsettled; S3 must pin by full title so a criterion aimed at the mid-year review cannot be satisfied by the May report review.

---

### F6 - MODERATE - OE 28 - the stated result set is falsified by the Linda Castillo event

**Does `fullText "Portfolio Review"` sweep in Castillo? Yes.** "Linda Castillo Mid-Year Portfolio Review" (base id `epax0kiwoq0ygmqxezm2pax18l`, 2026-05-26, 4 rows, Lisa holds a row and accepted) matches the search string and sits on the very calendars OE 28 tells the agent to query (aurora, brooke, patricia, teresa).

**Does it sweep in Shea? No.** Handoff obligation 13: David Shea has **0 of 565** calendar rows, so no Shea event can return. That absence is itself lever material (H4) and is correctly not asserted as a finding here.

**Is OE 28 a false enumeration claim or merely incomplete? It is a false claim about the named call's result set,** and therefore an Accuracy defect rather than a Completeness one. OE 28 says "The agent finds two live events for the same owner one day apart". The call it specifies returns at least **four** Mid-Year Portfolio Review events across **three** owners. The two Harris events are a subset of the result, not the result.

**It is not a scope violation.** OE 28 issues no instruction to act on Castillo, and OE 3 explicitly excludes her package. The chain does **not** sweep her in. The risk is downstream: if S3 lifts OE 28's phrasing into an enumeration criterion, Castillo falsifies it.

**Fix - replacement wording for OE 28's opening.**

> OE 28: Call list_events with fullText "Portfolio Review" across the other participants' calendars (aurora.winona@starpm.com, brooke.phillips@starpm.com, patricia.nguyen@starpm.com, teresa.wood@starpm.com) and confirm each hit with get_event. The search returns mid-year portfolio reviews for three owners, not two: Harry Harris twice, Robert Finley once, and Linda Castillo once (epax0kiwoq0ygmqxezm2pax18l, 2026-05-26, 4 rows, Lisa holds a row and accepted). Linda Castillo is Patricia Nguyen's owner under the split recorded in OE 3, so she falls outside the prompt's possessive scope and must be filtered out rather than reported on; no criterion may require or permit action on her review. David Shea returns nothing at all, because he has no calendar presence anywhere in the universe. Within Lisa's two owners the agent finds two live events for the same owner one day apart, both status confirmed and neither cancelled: [remainder of OE 28 unchanged]

---

### F7 - MAJOR - OE 13 - OE_INCOMPLETE: nothing in the chain bridges Harry Harris to Sunset Ridge

**Evidence.** OE 10 is explicit that Airtable carries no owner field and that the Finley-to-Mesa-Vista link exists in exactly one place: *"Its description ties Robert Finley to the Mesa Vista portfolio, which is the only place in the universe that link is stated, since Airtable carries no owner field."* That is the bridge for Finley, and it is properly grounded on OPS-100.

**There is no equivalent step for Harris.** OE 13 opens with 'search_records ... query "Sunset Ridge" to pull Harry Harris's cluster'. The identification of Sunset Ridge as Harris's cluster is **asserted, never retrieved**. No OE before 13 names a record that states it. An agent following this chain literally cannot know which property to query for Harris, and Harris is half the task.

This is the single most load-bearing missing dependency in the deliverable: the entire Harris arc (OE 13, 16, 17, 30, and the Harris half of OE 33 and OE 36) hangs off it.

**Fix.** Add a discovery OE before OE 13 that names the record supplying the Harris-to-Sunset-Ridge link, in the same shape OE 10 uses for Finley. S2 must locate it in the split (candidate stores, in order of likelihood: a Linear issue or comment in `proj_002`, a HubSpot deal or company association, or a Slack message in C004/C006). If no such record exists, that is a **universe feasibility problem**, not an OE wording problem, and it escalates immediately: the task would be asking for a portfolio position on an owner whose portfolio is unknowable.

---

### F8 - MODERATE - OE 29 - the fourth Finley calendar event is never introduced

**Evidence.** Handoff obligation 8 requires that `ti5zt1xubdggbehtp79um9mim6` "May Owner Report Review - Finley Properties" (3 rows, 2026-05-28 11:45 to 12:15, Lisa declined) be pinned by **full title** so "a criterion aimed at the mid-year review cannot be satisfied by it". The OE chain never mentions it. S3 therefore has no basis in the OEs for writing that discrimination, and an agent that finds it may reasonably treat it as the Finley review that needs settling, since Lisa declined that one too.

**Fix.** Fold it into OE 29 (wording supplied in F5's replacement block, final sentence).

---

### F9 - MODERATE, conditional MAJOR - OE 8 - the reply's own timestamp contradicts the date OE 8 assigns it

**Evidence, measured this session.** Parent message `831d2b6760205432a20487e2664a607e` carries `ts` **1780002480.000000** with `created_at` **2026-05-28T21:08:00+00:00**, `reply_count` **1**, and `latest_reply` **1782860664.000001**. Because there is exactly one reply, `latest_reply` is `a6779a055eaf5fb1893d0ed6d92e3b39`'s own timestamp.

1782860664 minus 1780002480 = **2,858,184 seconds = 33 days, 1 hour, 56 minutes**. That places the reply's Slack timestamp at approximately **2026-06-30T23:04 UTC**, one day before universe today, not 2026-05-28 as OE 8 states.

**What I did not check, and what S2 must.** I did not read the reply row's own `created_at`. Two outcomes:

- If `created_at` is 2026-05-28 while `ts` is 2026-06-30, the row is internally inconsistent and **OE 8 must name which field it sources the date from** (Hardness Plan carry-forward risk 5 already imposes this discipline on `fldMoveOut`/`fldTargetReady`; the same discipline applies here).
- If `created_at` is also late June, **OE 8's date is simply wrong**, and the framing is wrong with it: OE 8 calls this "the spring read the prompt refers to", and `5_Prompt.txt` line 3 says "I gave Brooke a rough read on my two earlier in the spring". A claim posted on 2026-06-30 is not a spring read.

**Conditional propagation.** See B6. Note the mitigation: OE 9's C004 pair (`49b2873d46d55e4291a78d91d91a5054`, `5f60afa12c4c53b6b7694d59373acae8`, 2026-05-12, covering **both** owners) is genuinely spring-dated, so the prompt's sentence very likely survives on OE 9 even in the worst case. The OE 8 date claim does not.

---

### F10 - MODERATE - OE 27 - "makes both look settled" is false

**Evidence.** OE 27 says scoping the calendar to Lisa "shows exactly one review per owner and makes both look settled". Lisa's row on the Finley review `8mwlxrq5w5oodwdpmvo83e00f2-b0504ab4` reads `responseStatus: declined` (Handoff obligation 1, row 3; restated by OE 29 itself two OEs later). A declined meeting does not look settled. OE 27 and OE 29 contradict each other.

The sharper and true version of the point is the one Handoff obligation 14 pre-registered: the persona-scoped view shows two events, one per owner, which **positively confirms the prompt's "either of those"** and hides the Harris duplicate entirely.

**Fix - replacement for OE 27's final sentence.**

> Scoping the calendar to the persona alone shows exactly one review per owner, which positively confirms the prompt's "either of those" while hiding the Harris duplicate entirely, so the agent must widen the search to the other attendees' calendars.

---

### F11 - MODERATE - OE_INCOMPLETE: no OE establishes that occupancy has no independent source

**Evidence.** The prompt asks for "the real position on occupancy". OE 33 mandates that the draft say "the 94 percent occupancy and 97 percent collections figures have no supporting record". OE 11 supports half of this ("The 94 percent figure appears in exactly one Slack message and one Linear comment and nowhere else in the universe"). But no OE describes the sweep that would let an agent conclude occupancy is not independently derivable at all, and no OE addresses the 97 percent collections figure's provenance separately.

The design is defensible: the refutation *is* the deliverable. But an agent will hunt for an occupancy source, and S3 has no OE basis for grading a negative that no OE establishes.

**Fix.** Extend OE 11, or add an OE, stating which stores were swept for an occupancy and a collections source and that neither yields one (Airtable `tblMakeReady` has no occupancy field; QuickBooks carries invoices and payments, not a collections rate; no other store carries either). Name the sweep, so the negative is earned.

---

### F12 - MINOR - OE 20 - a universal negative supported by a partial enumeration

**Evidence.** OE 20 claims "no water heater record in the universe is associated with Mesa Vista or with either of Lisa's owners", then enumerates 412 Mesquite and Pinecrest 12. The Hardness Plan's H2 lists **four** destinations: *"every water-heater record in the universe resolves to 412 Mesquite, Pinecrest 12, Dunmore Unit 3, or 2214 Oleander."* OE 20 drops two.

**Fix.** Either enumerate all four, or drop the enumeration and keep the negative claim with the sweep method named. A partial list under a universal claim invites an agent to find Dunmore Unit 3 and conclude the OE is wrong.

---

### F13 - MINOR - OE 10 - a HubSpot fact asserted with no retrieval step

**Evidence.** OE 10 asserts "HubSpot files Finley under company comp_mesaverde 'Mesa Verde Investments' while the Mesa Vista deals sit under comp_riogrande". No OE anywhere in the chain calls a HubSpot tool. An agent following the chain never fetches this, so the claim is unreachable prose. The Hardness Plan's Service Breadth table allocates HubSpot 0-2 calls at 1%, so this is not a required path and not an OE_INCOMPLETE.

**Fix.** Either add the HubSpot lookup as a step (it is a genuine near-miss trap and would add 1-2 calls), or reduce the sentence to the part the chain can reach.

---

### F14 - MINOR - OE 34 - the permissive state transition risks inviting an incorrect write

**Evidence.** OE 34: "The agent may also move OPS-10 out of state_OPS_0 using save_issue, since the issue's own comment thread has claimed two transitions that never took effect." The justification clause reads as encouragement. OPS-10 is the **four-owner parent** and Lisa owns two of the four; Patricia's half is demonstrably not complete (Shea has zero calendar presence, Handoff obligation 13). Advancing OPS-10 on the strength of Lisa's half alone would be an incorrect write, and moving it to `state_OPS_4` would be plainly wrong.

The permissiveness is correct; the justification is what misleads. L10's OPS-10 carrier is a **reasoning** beat (notice the comments announce transitions that never took), not a **write** beat.

**Fix.** Replace the justification clause with a boundary: state that the transition is optional and must not be graded, that the comment is the required write, and that advancing OPS-10 to Done would be incorrect because two of its four owner packages belong to Patricia and are not complete.

---

### F15 - MINOR - OE 33 - the decompose directive omits a content element the body mandates

**Evidence.** OE 33's body text mandates four corrections: the occupancy and collections figures, the make-ready count, the water heater attribution, and *"the cleared late payment is a Sunset Ridge tenant rather than a Mesa Vista one"*. The `S3 must decompose this into one criterion per content element (...)` list carries nine elements and includes the first three corrections but **not** the late-payment one. The collections figure is also folded ambiguously into "the occupancy correction".

Rule 14 mirroring and `check_oe_rubric_sync.py` both key on this directive, so an element mandated in the body but absent from the directive drifts silently.

**Fix.** Add "the cleared-late-payment correction" to the list, and split "the occupancy correction" if the 97 percent collections figure is to be graded separately. Alternatively drop the late-payment sentence from the body. Do not leave the two out of sync.

---

### F16 - MINOR - HARDNESS_PARTIAL on L10 - the OPS-39 / OPS-93 carrier is absent

**Evidence.** The Hardness Plan's L10 row names three carriers: the Harris calendar double-booking, OPS-10 in Backlog against two comments announcing transitions, and *"OPS-93 'Approved and Closed' sitting in Todo while OPS-39 (same reconciliation) sits in In Review"*. The OE chain carries the first two (OE 28, OE 4 / OE 34) plus a fourth the plan added later (OE 29, the Finley review contradicting `comment_79dc83838bd65d678c48b5911f942412`), and carries a fifth in OE 11 (OPS-100 "moving this to Done" while `state_OPS_2`). **OPS-39 / OPS-93 appears nowhere.**

**Severity is MINOR, not a regression.** L10 has four live carriers in the chain. This is a note for S3's budget rather than a blocker: if criteria are trimmed toward the 60 ceiling, L10 has redundancy that L11 does not (Handoff obligation 6).

---

### F17 - MINOR - OE 18 - an unevidenced scoping claim of the same class as F1

**Evidence.** "This is the only open ticket in either owner's scope." Handoff obligation 5 records 7 of 50 `tblMaintenanceTickets` rows with a null `fldCompletionDate`, and 26 of 50 descriptions carrying a unit or property token. OE 18 gives no evidence of the scoping sweep that reduces 7 open tickets to 1 in-scope ticket, and MT-2026-047's own text names the property only as "Finley portfolio property".

**Fix.** State the sweep: which of the 7 open rows were examined and why 6 fall outside Harris's and Finley's clusters. This is the same defect class as F1 and should be fixed in the same pass.

---

## POSITIVES (recorded so a later phase does not re-litigate them)

- **All 30 tool names verified to exist** in the 276-tool catalog. Zero invented tools.
- **All four money totals recompute correctly.** Finley open AR 8,400 + 2,190 + 390 = **$10,980** (OE 23). Finley credits 2,755 + 490 + 410 = **$3,655** (OE 25). Harris credits 195 + 1,250 + 530 = **$1,975** (OE 25). Net 10,980 - 3,655 = **$7,325** (OE 26). Harris invoices 510 + 60 + 1,345 = 1,915, all at Balance $0.00, consistent with "no open receivable" (OE 24).
- **OE 8's `message_ts` parameter value is exactly right** (`1780002480.000000`), verified against the parent row.
- **OE 3 excludes Castillo and Shea explicitly**, which is the correct scope discipline and pre-empts a whole class of S3 error.
- **OE 33 states the Gmail draft-only constraint in terms**, which is a universe-specific trap the chain handles correctly.
- **OE 25 states the L11 mechanism precisely** (RemainingCredit 0, Balance equals TotalAmt, no LinkedTxn, BILL-/INV- prefixes on four of six). This is the strongest OE in the file.
- **OE 13 flags the "Unit 14" collision** and requires property qualification, satisfying that part of rule 13.

---

## [B1] QC sub-dim scoring

`SUB-DIM OE Completeness -> SCORE 3/5 -> REASON Two critical-path gaps: no OE supplies the Harris-to-Sunset-Ridge bridge that the entire Harris arc depends on (F7), and the Airtable correction set is never derived across Finley's 9 rows (F3), so one of the six required writes has an undetermined target set.`

`SUB-DIM OE Accuracy -> SCORE 3/5 -> REASON Five stated expected values do not match the universe: OE 15's sole-unresolved-item claim (F1), OE 27's "makes both look settled" against Lisa's recorded decline (F10), OE 28's two-event result set against the four events the named call returns (F6), OE 8's 2026-05-28 reply date against the parent's own latest_reply timestamp (F9), and OE 20's partial four-way enumeration under a universal negative (F12).`

Both sub-dims are 3/4/5 NON-FAIL-only, so neither is a QC fail on its own. Neither reaches PASS(5), which is the project bar (AGENTS.md rule 10) and the stated GO condition for this council.

Supporting note on Accuracy: every **tool name** and every **arithmetic total** checks out. The defects are in stated findings, not in the mechanics. That is a fixable-by-wording profile, not a rebuild profile.

---

## [B2] Adversarial alt-path

### (a) Could an agent discharge "put those records right" entirely inside Airtable on DIFFERENT rows than the two the OE names?

**Yes, and the OE chain neither accommodates nor forecloses it. It simply does not describe it.** That is the worst of the three outcomes.

The prompt's clause is "Where the unit and turn records do not line up with what you actually find on the ground, put those records right rather than working around them." It is data-determined: it names no row, no unit and no property. An agent that runs the mismatch analysis across Finley's cluster instead of Harris's, or across both, acts on a fully valid reading.

Concretely: `rec8b679d92f30753` (Ridgeview roof, `selSched`) is a live candidate, and the **Hardness Plan itself certifies it as qualifying** in its CORRECTION block. An agent that corrects that row and not the two Sunset Ridge rows has done defensible work and fails every OE-30-derived criterion. Nine rows (8 Mesa Vista + 1 Ridgeview) were never tested for mismatch at all, so the true size of the valid answer set is unknown to this deliverable.

**Would it be equally correct?** For `rec8b679d92f30753`, on the evidence available, arguably yes. For the Mesa Vista rows, unknown, which is the problem. See F3 for the fix.

### (b) Could an agent reasonably read "their review meetings" as covering only ONE owner?

**Yes, and the chain only partially forecloses it.**

The prompt reads "Do the same for their review meetings if either of those did not end up properly settled." "their" is plural-possessive over both owners, so both meetings are in scope. But **"either of those" is a two-item quantifier**, and the pre-registered failure mode (Handoff obligation 14) is that an agent scoping Calendar to Lisa sees exactly two events, one per owner, and reads that as confirmation. It then finds one problem (Harris looks fine, Finley shows a decline) and acts once.

**What forecloses it:** OE 27 and OE 28 explicitly direct the widening to calendars Lisa is not on. That is the correct instruction and it is present.

**What does not foreclose it:** OE 31's Finley half is entirely permissive ("may use ... or ..."), names no required end state, and offers an action that settles nothing (F5). As written, an agent that resolves only the Harris duplicate satisfies OE 31 on its face, in direct tension with Handoff obligation 12 and the Hardness Plan CORRECTION block, both of which make the Finley beat mandatory.

**Accepted-difficulty note:** the under-count in "either of those" (there are four Harris/Finley calendar events, not two) is *intended* difficulty, pre-registered by the Hardness Plan and Handoff obligation 14. It is not a prompt defect and is not propagated.

### (c) Is there a second reasonable reading of "whatever is still genuinely unresolved"?

**Yes, at least three, and the chain forecloses none of them.**

| Candidate | Why an agent picks it | Foreclosed by the OE chain? |
|---|---|---|
| **MT-2026-047** (`recb4aeaed326f156`) | Literally an open high-priority ticket, empty `fldCompletionDate`, text says it "requires professional evaluation". OE 18 calls it "the only open ticket in either owner's scope". | **No.** The chain actively points at it. |
| **Invoice 2026-494** ($8,400, 31 days past due) | OE 26 calls it "the money question the prompt anticipates". Unresolved, on the money side, on a Finley property. | **No.** |
| **The missing Finley review meeting** | OE 29 concludes "the meeting that comment describes does not exist" and "Neither owner's review ended up properly settled". | **No.** Though the prompt's separate calendar clause arguably absorbs this one. |

This is a **rule 13(c) hit**. The fix (F2) is to state the disposition discriminator in OE 35 rather than assert the subfloor.

---

## [B3] Tool-call density projection, PER MODEL

Trajectory sketched per model against the 36-OE chain as written.

### Opus 4.8

| Segment | OEs | Calls |
|---|---|---:|
| Linear discovery (list_issues, get_issue, list_comments, list_issue_statuses) | 1-5 | 4-6 |
| Slack (search_channels, read_channel, read_thread, search_public x2) | 6-9 | 5-7 |
| Linear downstream (list_issues, get_issue, list_comments on OPS-100) | 10-11 | 3-4 |
| Airtable enumeration (list_bases, list_tables_for_base, get_table_schema, search_records x4, per-row reads) | 12-19 | 8-14 |
| Water-heater cross-check (search_records + slack_search_public) | 20 | 2-4 |
| Gmail (search_threads + get_thread) | 21 | 2-4 |
| QuickBooks (search_customers x2, search_invoices x2, read_invoice x7, search_credit_memos x2, get_credit_memo x6, get_aged_receivables) | 22-26 | 12-18 |
| Calendar (list_calendars, list_events x4-5, get_event x4-6) | 27-29 | 8-12 |
| Writes plus supporting reads | 30-36 | 8-11 |
| **TOTAL** | | **52-80** |
| **MIDPOINT** | | **66.0** |

### Gemini

Gemini's count scales with explicit enumeration (Hardness Plan empirical anchor: 79.8 on Task 44's portfolio sweep against Opus 62.5, versus 33-43 on the four single-entity tasks). This chain is enumeration-heavy: 7 Sunset Ridge rows, 8 Mesa Vista rows, 7 invoices, 6 credit memos, 4-5 calendar listings. Gemini also issues more redundant searches and more per-item confirmations.

| Segment | Calls |
|---|---:|
| Linear discovery | 5-8 |
| Slack | 4-8 |
| Linear downstream | 3-5 |
| Airtable enumeration (per-row confirmation inflates this most) | 10-18 |
| Water-heater cross-check | 2-5 |
| Gmail | 2-4 |
| QuickBooks (per-record `read_invoice` / `get_credit_memo` inflates this most) | 14-20 |
| Calendar | 8-13 |
| Writes plus supporting reads | 8-12 |
| **TOTAL** | **56-93** |
| **MIDPOINT** | **74.5** |

### Verdict against the V4 bands

| Model | Hardness Plan projection | This OE chain | V4 band (>=40 PASS) | Delta |
|---|---:|---:|---|---:|
| Opus 4.8 | 63.5 | **66.0** | **PASS**, +26.0 margin | **+2.5** |
| Gemini | 66.0 | **74.5** | **PASS**, +34.5 margin | **+8.5** |

**The OE list has not thinned density; it has slightly enriched it.** The enrichment source is identifiable: the plan budgeted 7-11 QuickBooks calls, while OE 23 through OE 25 specify per-record confirmation (`read_invoice` on each of 7 invoices, `get_credit_memo` on each of 6), which alone is 13 calls before any search. Calendar is likewise specified per-event (`get_event` confirmation on each hit) against a plan budget of 5-8.

**One downward pressure, named for honesty.** OE 12's `list_bases` + `list_tables_for_base` + `get_table_schema` is three calls of pure plumbing that a competent agent may skip by going straight to `search_records`. Worst case that is -3 on both models, leaving Opus 63.0 and Gemini 71.5. Still far above 40.

**No fix recommended in this report reduces density.** F3 (add the Finley mismatch sweep), F7 (add the Harris bridge lookup), F11 (add the occupancy sweep) and F13 (add the HubSpot lookup) each **add** calls. If all four are applied, expect roughly +6 to +12 per model.

---

## [B4] Hardness preservation

| Lever | Status | OE steps that exercise it |
|---|---|---|
| **L1** Latching on the persona's own undispositioned claim | **PRESERVED (strong)** | OE 7 (parent message), **OE 8 (the claim itself, reachable only by thread read)**, OE 9 (the C004 near-duplicate pair, extending the claim to both owners), OE 11 (propagation into `comment_5a6d779a715f587392dd00b9c8dbbd4a`), OE 14 (four Mesa Vista units refute "one unit still in make-ready"), OE 20 (water heater refuted), OE 21 (late payment refuted), OE 33 (all four corrections mandated in the draft) |
| **L2** Structured-DB skip | **PRESERVED** | QuickBooks half: OE 22-26 (`search_customers`, `search_invoices`, `read_invoice`, `search_credit_memos`, `get_credit_memo`, `get_aged_receivables`). Calendar half: OE 27 (`list_calendars`, persona-scoped list), OE 28 (`list_events` across calendars Lisa is not on), OE 29 (`get_event`) |
| **L7** Multi-write diversification | **PRESERVED AT RISK** | Six writes across five services, matching the plan: OE 30 airtable, OE 31 gcalendar, OE 33 gmail, OE 34 linear comment, OE 35 linear issue, OE 36 slack. **Two of the six are compromised as written:** OE 30's target set is underdetermined (F3) and OE 31's target is an ambiguous bare base id with an unsatisfiable proposed action on the Finley half (F4, F5) |
| **L10** Reversal / supersession | **PRESERVED, one carrier missing** | Harris double-booking: OE 28. OPS-10 state contradiction: OE 4 (both narration comments) + OE 34. OPS-100 "moving this to Done" while `state_OPS_2`: OE 11. Finley review contradicting `comment_79dc83838bd65d678c48b5911f942412` on month, duration and time of day: OE 29. **Absent: OPS-39 vs OPS-93** (F16, MINOR, four other carriers remain) |
| **L11** Net-vs-gross | **PRESERVED (strong)** | OE 25 (all six credit memos with `RemainingCredit` 0, `Balance` equal to `TotalAmt`, no `LinkedTxn`, four of six wearing `BILL-`/`INV-` prefixes), OE 26 (explicitly names the $7,325 netting error), OE 33 (draft must state the credits are unapplied and do not reduce the balance). Correctly carried with **no write carrier**, per Handoff obligation 6 |

**No HARDNESS_REGRESSION.** One HARDNESS_PARTIAL (L10 / OPS-39 vs OPS-93, F16) and one PRESERVED-AT-RISK (L7, contingent on F3/F4/F5 being fixed).

### The contrast pair: does Harris-operationally-blocked stay separable from Finley-cash-blocked?

**In the written deliverable: yes, explicitly and well.**

- **OE 24 states it directly:** "The two owners are behind for different reasons, and reporting them as a single 'both owners are behind' position loses that distinction."
- **OE 33 mandates the separation in the draft body:** "Harris is operationally blocked, with 7 make-ready rows across 3 Sunset Ridge units and none of them in a Ready state, against $0.00 of open receivable; Finley is cash-blocked, with $10,980.00 past due ... plus $3,655.00 of credit memos that are unapplied".

That is the strongest hardness-preserving passage in the file, and the arithmetic behind both halves verifies.

**In the action set: no, it is asymmetric in a way the design did not intend.** Because OE 30 writes only on Harris's rows (F3), every operational correction lands on Harris and none on Finley. Finley holds 8 Mesa Vista make-ready rows and a structural roof repair, so he plainly has operational state; the chain simply never tests it. The risk is that S3 grades "operational" exclusively on Harris and "cash" exclusively on Finley, which collapses the contrast from *two owners each assessed on both axes* into *two owners each assessed on one axis*. That is a weaker and more guessable shape than the plan designed.

**Fix:** F3. Closing the mismatch sweep across Finley's rows restores the symmetry whichever way the data falls, because a reasoned "no Finley row qualifies, and here is why" is itself the assessment.

---

## [B6] Upstream propagation

**One conditional flag. No unconditional flags.**

`PROPAGATE TO S1 (CONDITIONAL, pending F9 verification): the prompt's "spring read" framing may not match the universe -- 5_Prompt.txt:3 ("I gave Brooke a rough read on my two earlier in the spring") -- recommended upstream fix: none required if the C004 pair carries it; if OE 8's reply is confirmed late-June AND the C004 pair is judged not to carry the clause, reword to a time-neutral phrase such as "I gave Brooke a rough read on my two a while back".`

Resolution procedure: read `a6779a055eaf5fb1893d0ed6d92e3b39`'s own `created_at`. If it is spring-dated, close the flag and fix OE 8's sourcing note only (F9). If it is late-June, the prompt sentence still very likely survives on OE 9's `49b2873d46d55e4291a78d91d91a5054` / `5f60afa12c4c53b6b7694d59373acae8` pair (2026-05-12, both owners, genuinely spring), in which case close the flag and fix OE 8. Only if both fail does the prompt need rewording. **This is BLOCKING until resolved**, because "Alignment with Today's Date" is a binary QC sub-dim (AGENTS.md rule 26).

### Write-licensing audit: does the prompt license all six writes?

**Yes, all six. No propagation on licensing.**

| Write | Licensing clause in `5_Prompt.txt` | Verdict |
|---|---|---|
| Gmail draft (OE 33) | line 7: "Put an email together for Brooke covering both owners with the specifics in it." | Licensed |
| Linear comment on OPS-10 (OE 34) | line 7: "Bring the mid-year review item up to date on the issue tracker with where my half has landed." | Licensed |
| New Linear issue (OE 35) | line 7: "open a separate item for whatever is still genuinely unresolved" | Licensed. Singular determiner supports the cardinality-one pin |
| Slack post to C006 (OE 36) | line 7: "Post a short version in the owner relations channel" | Licensed |
| Airtable corrections (OE 30) | line 5: "Where the unit and turn records do not line up with what you actually find on the ground, put those records right" | Licensed. Data-determined, which is exactly why F3 matters |
| Calendar resolution (OE 31) | line 5: "Do the same for their review meetings if either of those did not end up properly settled." | Licensed. This is the S1 AUDIT F1 rewording, purpose-built to carry it; "review meetings" has no Airtable field counterpart, so it denotes calendar events only |

**No OE step goes beyond what the prompt asks.** OE 34's optional OPS-10 state transition is the only borderline case, and it is correctly framed as optional (see F14 for the wording risk, which is an OE defect, not a prompt defect).

---

## [B8] OE Completeness semantic - dependency walk

Requested checks:

| Required step | Present? | Where |
|---|---|---|
| Contact lookup **before** the draft | **Yes** | OE 32 (`contacts_search_contacts`, resolves `c46d47256fd95ca6aca770c8dddda5eb`), immediately preceding OE 33 |
| Bridge from owner name to property cluster - **Finley** | **Yes** | OE 10, correctly grounded on OPS-100's description and correctly noting it is the only place the link is stated |
| Bridge from owner name to property cluster - **Harris** | **NO** | See below |
| Reading the thread reply rather than only the channel | **Yes** | OE 7 (channel read shows the parent only) then OE 8 (`slack_read_thread`, correct `message_ts`) |
| Enumerating calendars the persona is not on | **Yes** | OE 27 (persona scope shown to be insufficient) then OE 28 (explicit list of the four other calendars) |

**Gaps:**

`OE_INCOMPLETE: prompt requires establishing which property cluster belongs to Harry Harris, but no OE covers it -- OE 13 asserts "Harry Harris's cluster" while searching "Sunset Ridge", with no prior OE naming the record that states the link. OE 10 does exactly this job for Finley. Half the task hangs off this. (F7, MAJOR)`

`OE_INCOMPLETE: prompt requires "put those records right" across all unit and turn records, but no OE runs the mismatch analysis on the 8 Mesa Vista rows from OE 14 or the Ridgeview row rec8b679d92f30753 from OE 19, so the corrected-row set is open rather than closed. (F3, MAJOR)`

`OE_INCOMPLETE: prompt requires "the real position on occupancy", but no OE establishes that occupancy has no independent source in this universe, while OE 33 requires the draft to assert exactly that. The negative is mandated but never earned. (F11, MODERATE)`

`OE_INCOMPLETE: Handoff obligation 8 requires "May Owner Report Review - Finley Properties" (ti5zt1xubdggbehtp79um9mim6) be introduced and discriminated from the mid-year review, but no OE mentions it. (F8, MODERATE)`

---

## [B9] OE Service Mapping

**ZERO `OE_SERVICE_MISMATCH`.** Every step's service matches the StarPM data-type map.

| OEs | Service | Data type | Correct? |
|---|---|---|---|
| 1-5, 10-11, 34-35 | linear | Coordination/project items (the review parent, the owner report, comments, the new issue) | Yes. These are project items, not maintenance tickets |
| 6-9, 36 | slack | Chat | Yes |
| 12-17, 19, 30 | airtable | Make-ready / unit / property records, system of record | Yes |
| **18** | **airtable** (`tblMaintenanceTickets`) | **Maintenance tickets** | **Yes.** Correctly placed in Airtable, not Linear |
| 20 | airtable + slack | Cross-check | Yes |
| 21 | gmail | Tenant correspondence | Yes |
| 22-26 | quickbooks | Customers, invoices, credit memos | Yes. Read-only throughout, per Handoff obligation 4 |
| 27-29, 31 | gcalendar | Events | Yes |
| 32 | contacts | Recipient resolution | Yes |
| 33 | gmail | `create_draft`, and OE 33 states the draft-only constraint explicitly | Yes |

**Two notes, neither a mismatch.**
1. OE 10 asserts a HubSpot fact without any HubSpot retrieval step (F13, MINOR). That is an unreachable-prose defect, not a misrouted step.
2. I did **not** independently verify the Linear `team_001` description text asserting that Airtable is the system of record for maintenance. OE 18's placement is nonetheless correct against the AGENTS.md StarPM universe card ("Airtable is source of record for make-ready/unit/property state; Linear is secondary"). Flagged for Council A rather than scored here.

---

## [B-RULE13] Hard rule 13 audit

### (a) Does any OE pin a target that two or more universe records satisfy?

**HIT - OE 31.** "eventId set to the rescheduled instance" resolves to bare base id `qqbwq3s2h7wh5udoek2940mffk`, which matches **4 stored rows**, none of them Lisa's. Direct violation of Handoff obligation 1 and of the Hardness Plan's own CORRECTION block. **F7 AMBIGUOUS_TARGET.** See F4 for replacement wording.

**NEAR-HIT - OE 28 and OE 29 print bare base ids** (`1pon50ds1aevem63td6f7emdn3`, `qqbwq3s2h7wh5udoek2940mffk`, `8mwlxrq5w5oodwdpmvo83e00f2`). Both are read steps and both do name Lisa's per-calendar row where one exists (`-b0504ab4`). Acceptable as reads, but S3 must not lift the bare ids into criteria.

**SOFT HIT - OE 30 / OE 35.** Neither pins a colliding record, but both leave the target *set* underdetermined (F3) or the target *identity* undiscriminated (F2). Different mechanism, same downstream consequence.

**CLEAN:** OPS-10 (OE 1 correctly identifies "Mid-Year" as the sole discriminator against the byte-identical OPS-11/OPS-13 pair, per Handoff obligation 3), OPS-100, invoices `2026-494` / `2026-303` / `4421`, `rec88734a4fdfde57` (only Mesa Vista 310C row), and OE 13's explicit "Unit 14" collision warning requiring property qualification.

### (b) Any "complete" or "only open item" claim not reconciled against Calendar?

**HIT - OE 15.** "the one genuinely unresolved item in either cluster", tested against every service:

| Service | Contradicting evidence |
|---|---|
| Airtable (tickets) | `recb4aeaed326f156` MT-2026-047, `selHigh`, `fldCompletionDate` empty (**OE 18, same file**) |
| Airtable (make-ready) | `rec8b679d92f30753` Ridgeview roof, `selSched`, unfinished structural repair (**OE 19, same file**) |
| QuickBooks | Invoice `2026-494`, $8,400, 31 days past due (**OE 23/26, same file**) |
| **Calendar** | `42b119cbt7xd0vnhw6dwvdqizo` 2026-07-13 **Vendor Walk-Through - Ridgeview Roof Repair Follow-Up** (Finley property, `pete.donovan@gmail.com` still `needsAction`); `0hjw400xgjb3j7ay7ynuaqbnpi` 2026-07-15 **Make-Ready QC Inspection - Mesa Vista 4C** (Finley cluster); `j3ulusavtqgvwge31s21ep5c8w` 2026-07-08 **Mesa Vista HOA Management Review**; `232wqgjdsa2cyz9mv4qtx5mncy` 2026-07-23 Q3 Make-Ready Planning and Budget Review, covering Mesa Vista |
| Gmail | not swept (no completeness claim rests on it) |

**The claim is too strong. F9 UNRECONCILED_FUTURE_EVT.** Exact replacement wording is given in F1.

**WEAKER HIT - OE 18** ("the only open ticket in either owner's scope"), unevidenced against the 7 open rows Handoff obligation 5 records. F17.

**WEAKER HIT - OE 20** (universal negative on water heaters supported by a two-of-four enumeration). F12.

**CLEAN - OE 32** ("exactly one Brooke Phillips in contacts, in Slack and in HubSpot") is a uniqueness claim about a recipient, not a completeness claim about open work. Low risk.

### (c) Naive-agent simulation, prompt read without the OE file

**HIT, three ways.**

1. **New issue target (F2).** "whatever is still genuinely unresolved" points a reasonable agent at MT-2026-047 before it points anywhere near a subfloor note buried in one row's `fldNotes2`.
2. **Airtable correction rows (F3, B2(a)).** "the unit and turn records" names no property. Finley's 9 untested rows are as reachable as Harris's 7.
3. **Calendar, single-owner reading (B2(b)).** The persona-scoped view confirms "either of those" and hides the duplicate.

### Linda Castillo cross-owner bleed check

**Does the OE chain sweep her in? NO. This is handled correctly.**

- OE 2 names her as one of OPS-10's four owners. Correct and necessary.
- **OE 3 excludes her explicitly:** "This scopes the work to Harris and Finley and excludes the Shea and Castillo packages."
- OE 20 references "412 Mesquite (Tommy Reyes, a Linda Castillo property)" only as an *exclusion*, which is the correct use.
- No write step touches any Castillo record.

**Does any OE make an enumeration claim she would falsify? YES, one.** OE 28's "The agent finds two live events for the same owner one day apart" describes the result of a `fullText "Portfolio Review"` search that also returns **"Linda Castillo Mid-Year Portfolio Review"** (`epax0kiwoq0ygmqxezm2pax18l`, 2026-05-26, 4 rows, Lisa holds a row and accepted) on the very calendars OE 28 names. Shea returns nothing, since he has 0 of 565 calendar rows.

This is **F6, MODERATE**: an inaccurate result-set description, not a scope violation. The fix in F6 states the full result set and the exclusion rule in terms, which both corrects the accuracy defect and pre-empts S3 writing an enumeration criterion Castillo falsifies.

---

## VERDICT

`VERDICT: BLOCK`

GO required all of: both OE sub-dims at 5, no adversarial divergence, both per-model density midpoints >= 40, every Hardness lever triggered, no PROPAGATE flags, zero `OE_INCOMPLETE`, zero `OE_SERVICE_MISMATCH`, zero rule-13 hits.

| Gate | Result |
|---|---|
| OE Completeness = 5 | **FAIL** (3/5) |
| OE Accuracy = 5 | **FAIL** (3/5) |
| No adversarial divergence | **FAIL** (all three B2 probes diverge) |
| Density Opus >= 40 | **PASS** (66.0) |
| Density Gemini >= 40 | **PASS** (74.5) |
| Every Hardness lever triggered | **PASS with caveats** (L7 at risk, L10 one carrier short) |
| No PROPAGATE flags | **FAIL** (one conditional, blocking until resolved) |
| Zero OE_INCOMPLETE | **FAIL** (4) |
| Zero OE_SERVICE_MISMATCH | **PASS** (0) |
| Zero rule-13 hits | **FAIL** (a: 1 hit + 2 soft; b: 1 hit + 2 weak; c: 1 hit) |

### Iteration guidance for S2

This is a **wording-and-coverage** rebuild, not a redesign. The scenario, the lever selection, the service mapping, the write set and both density projections are all sound. Nine of the seventeen findings are fixed by pasting the replacement wording supplied above.

Ordered work:

1. **F7** - find and add the Harris-to-Sunset-Ridge bridge record. **Do this first**: if no such record exists, it is a feasibility escalation, not an OE fix, and everything downstream changes.
2. **F3** - run the mismatch sweep across the 8 Mesa Vista rows and `rec8b679d92f30753`; close the correction set; resolve the Handoff-obligation-10 pin conflict at S2 if a Mesa Vista 207A or 4C row qualifies.
3. **F9** - read `a6779a055eaf5fb1893d0ed6d92e3b39`'s `created_at` and clear or escalate the conditional PROPAGATE.
4. **F1, F2** - paste the OE 15 and OE 35 replacements (they share the disposition discriminator, so do them together).
5. **F4, F5** - paste the OE 31 replacement, both halves.
6. **F6, F10** - paste the OE 28 and OE 27 replacements.
7. **F8, F11, F12, F13, F14, F15, F16, F17** - the remaining MODERATE and MINOR items.

No fix in this list reduces projected density; four of them increase it.
