SHA256 6_Oracle_Events.txt = a8522f8daa4162ed6b9199a58b769b00dfb3fa55dfc3632c328451ba0f2e6785

# Council B, adversarial QC, closing round on the shipped bytes

Pin block, all hashes taken at entry to this round:

| File | SHA256 (first 16) |
|---|---|
| 6_Oracle_Events.txt | a8522f8daa4162ed |
| 5_Prompt.txt | 885750ecef51acc5 |
| _aux/6_Oracle_Events.pre_r1sweep.bak (the r5 era bytes, 12:28) | 5aa21a8eb179a677 |

Method. Every claim below was re-derived from `_aux/Universe_Split/` in this session with python3, double `json.loads` on `row_data`. No count, id or figure was carried forward from any earlier council round, from `Verification_s2.md`, or from the operator brief. 38 independent checks were run and all 38 agree with the shipped file. The one dependency I did accept from the brief is the statement that the file is frozen; the exit re-pin below confirms it held.

Why this round exists: my r5 GO carried no content hash and described bytes that were edited twice afterwards, so it did not describe this file. My r6 found a real defect and left nothing on disk. Neither B3 nor B4 had ever been evaluated on these bytes. This report supersedes both.

---

## 1. Sub-dimension scores on these bytes

SUB-DIM OE Completeness -> SCORE 5/5 -> REASON All six prompt deliverables carry a step (record corrections OE 30, meeting resolutions OE 31, email OE 33, tracker update OE 34, new item OE 35, channel post OE 36), every discovery step feeding them is present with its tool and discriminating parameters, and the dependency chain from Lisa's spring claim through its four independent refutations to the hand-off is unbroken.

SUB-DIM OE Accuracy -> SCORE 5/5 -> REASON All 38 re-derived checks match: 19 of 19 count claims, every cited record id resolves on the service the step names, all money figures reconcile ($10,980.00 / $0.00 / $3,655.00 / $1,975.00 / 117 of 117 credit memos unapplied), and following the steps literally produces a correct trajectory.

Scheme note: `Docs_starpm/7_QC_Spec_Doc1.json` carries no Fail band for either OE sub-dimension (both read "NA"), so the live scheme is Non-Fail 3/4 against Pass 5. Both are scored 5.

---

## 2. B2 adversarial alt-path

Thirteen alternative paths were pushed at the file. Twelve are explicitly licensed; the thirteenth is foreclosed by the universe rather than by the OE, which is the stronger position.

| # | Alternative an agent could defensibly take | Licensed? | Where |
|---|---|---|---|
| 1 | Read money by aged receivables rather than an invoice sweep | Yes | OE 23, OE 24 name `get_aged_receivables` |
| 2 | Treat Fernwood Gardens or Palomar Gardens as the Harris property | Foreclosed | see below |
| 3 | Leave the Mesa Vista 4C pair alone, or move either row | Yes, all three | OE 30 |
| 4 | Leave the Mesa Vista 207A rows alone, or correct them | Yes, both | OE 30 |
| 5 | Leave the Sunset Ridge Unit 14 row alone, or advance it | Yes, both | OE 30 |
| 6 | Raise the 309C utility blocker instead of the 310C subfloor | Yes | OE 15 and OE 35 |
| 7 | Cancel the Harris duplicate with delete rather than retitle with update | Yes | OE 31 |
| 8 | Replace the Finley review with a new event rather than move it | Yes | OE 31 |
| 9 | Move OPS-10 out of Backlog, or leave the state alone | Yes, ungraded | OE 34 |
| 10 | State the Mesa Vista make-ready count as 2, 3 or 4 | Yes | OE 33 |
| 11 | Surface invoice 2026-534 as a Mesa Vista billing question | Yes, if not added to the balance | OE 26 |
| 12 | Post the Slack summary in thread rather than top level | Yes, accept-set is "lands in C006" | OE 36 |
| 13 | Resolve "May Owner Report Review" as if it were the mid-year review | No, and correctly so | OE 29 distinguishes them |

On path 2, the one the file admits is "not clean": I tested whether an agent that reads the money records rather than OPS-32 could land on a different Harris cluster. Harris is billed for Palomar Gardens ($510.00), Fernwood Gardens ($1,345.00, the largest Harris invoice), Maple Ridge Building 2, 4402 Larkspur Ave, 233 Elmsworth Blvd, 4722 Elmwood Ave, Elmwood Units 204 and 211, and Pinebrook Apartments. **Not one of those seven properties carries a single row in tblMakeReady.** Sunset Ridge is the only Harris-linked property in the universe with any turn record at all, so the make-ready deliverable is only writable against Sunset Ridge. An agent that picks Fernwood still reports $0.00 open receivable and $1,975.00 of credits correctly, because those are customer scoped and property independent, and fails only the make-ready element. That is the intended discrimination, not a defect.

On path 10 and the net-vs-gross trap: an agent that writes "gross $10,980.00, with $3,655.00 of credits on file that carry no LinkedTxn" satisfies both graded content elements. Only an agent that reports $7,325.00 as the balance fails, and it fails on the reasoning step rather than the retrieval step. That is L11 working as designed and it is fair.

**B2 verdict: no unlicensed defensible path found.**

---

## 3. B3 tool-call density, per model, scored separately

Three separate numbers matter here and the file was measured against all three.

**(a) Mandated-chain count on the shipped bytes.** Counting fan-out explicitly (list_events is per calendarId and the chain names 8 distinct calendars; read_invoice is per record and the chain names 7 invoices; get_credit_memo per record on up to 6), a literal walk of all 36 steps is **about 88 to 91 calls**. 35 distinct tools are named across 8 services.

**(b) Bare-deliverable floor.** An agent that produces all six writes with no cross-service verification at all lands near **30 calls**. This is the honest downside and I state it rather than hide it: density on this task is carried by the verification work, not by the writes. The mitigation is structural rather than hopeful: five of the six deliverables cannot be written correctly without the cross-checks, because the email must carry four corrections that each require a separate sweep, the record corrections require sibling-row comparison inside Airtable plus calendar and invoice evidence for Ridgeview, and the new item requires the post-today calendar sweep to establish that the candidate is carried nowhere.

**(c) Projection, per model.**

| Model | Hardness Plan range | Plan midpoint | Shipped-bytes adjustment | Revised midpoint | Gate (40+ design target, 15 fail floor) |
|---|---|---|---|---|---|
| Opus 4.8 | 50 to 77 | 63.5 | +7 mandated retrieval calls added since r5 | **65** | **PASS**, margin +25 |
| Gemini | 50 to 82 | 66.0 | same +7 | **68** | **PASS**, margin +28 |

The +7 is exact and auditable: the r5-to-ship edits added `search_crm_objects` (OE 10), `list_issues` on "reconciliation" (OE 11), `search_records` x3 (OE 18 on tblMaintenanceTickets, OE 21 x2 on tblMakeReady), and `list_events` across two calendars (OE 35). Every one is a read. No edit since r5 removed a call. The plan's midpoints are therefore a floor on these bytes rather than a centre.

The per-model sign of the delta follows the measured StarPM anchors: Gemini runs below Opus on single-entity tasks (39, 40, 41, 43, 45: 33.0 to 43.3 against 37.0 to 48.0) and well above on the one multi-entity task (44: 79.8 against 62.5). This is a 2-owner by 4-workstream sweep, genuine multi-entity but narrower than Task 44, so Gemini is projected modestly above Opus and both sit between the single-entity band and Task 44.

**B3 verdict: PASS on both models scored separately.**

---

## 4. B4 lever preservation, per lever, on these bytes

| Lever | State | Evidence re-derived this session | Prompt still withholds it? |
|---|---|---|---|
| **L1** latching on the persona's own undispositioned claim | **PRESERVED, strengthened** | The claim is a thread reply (`a6779a055eaf5fb1893d0ed6d92e3b39`, thread_parent_id `831d2b6760205432a20487e2664a607e`) and 346 of 580 Slack messages are replies. Refuted on four independent axes, all re-verified: "94%" appears in exactly two places tied to this portfolio (her own message and `comment_5a6d779a715f587392dd00b9c8dbbd4a` repeating it) and elsewhere only on unrelated objects including a HubSpot deal reporting Oakfield Commons occupancy; "97%" appears **nowhere else in the universe**; zero records combine "water heater" with "Mesa Vista"; Mesa Vista carries 8 make-ready rows across 4 unit strings against her "one unit" | Yes. The prompt invites confirmation ("a fair bit of this should just be confirming it"), never suspicion |
| **L2** structured-DB skip | **PRESERVED** | Money exists only in QuickBooks; customer rows carry only Active, CompanyName, DisplayName, PrimaryEmailAddr (OE 22). Calendar: 9 confirmed base events sit on or after 2026-07-01 and **Lisa holds a row on none of them**. 0 of 565 calendar rows carries a bare base id, so every event write needs a per-calendar row id | Yes. The prompt names no service and no record type |
| **L7** multi-write diversification | **PRESERVED** | 7 mandated writes across 5 services: `update_records_for_table`, `update_event` or `delete_event` (Harris), `update_event` or `create_event` (Finley), `create_draft`, `save_comment`, `save_issue`, `slack_send_message`. Six prompt clauses license them | Yes, by clause rather than by tool |
| **L10** reversal and supersession | **PRESERVED on three stores** | Calendar: `1pon50ds1aevem63td6f7emdn3` (06-02, five rows, all four attendees accepted) against `qqbwq3s2h7wh5udoek2940mffk` (06-03 "(Rescheduled)", four rows, Aurora and Patricia declined, **no Lisa row**), both confirmed, neither cancelled. Linear: OPS-10 sits in state_OPS_0 with created_at equal to updated_at at 2026-05-03T22:11:57.112604-05:00 against two comments announcing transitions; OPS-39 (In Review) against OPS-93 "Approved and Closed" (Todo, completed_at null), now reachable by the query added at OE 11 which returns 4 issues. Airtable: three selSched rows superseded by later same-unit rows, all three re-confirmed still selSched | Yes. "if either of those did not end up properly settled" names a condition, not the defect |
| **L11** net vs gross | **PRESERVED, now symmetric** | 117 of 117 credit memos carry Balance equal to TotalAmt, RemainingCredit 0, and **zero LinkedTxn**. Finley $3,655.00 against $10,980.00 gross across 2026-494, 2026-303 and 4421; Harris $1,975.00 against $0.00 | Yes. "anything on the money side either of them is likely to raise with me" |
| **Contrast pair** Harris operationally blocked against Finley cash blocked | **PRESERVED, sharper than at r5** | Harris: 7 rows across 3 unit strings, **zero in selReady**, $0.00 receivable, $1,975.00 unapplied, review double booked. Finley: $10,980.00 past due across three invoices, $3,655.00 unapplied, open roof ticket MT-2026-047, review held 2026-05-19 with him not an attendee and Lisa declined. OE 24 carries the discrimination in one sentence | Yes |

The r5-to-ship edit that most increases discrimination is the addition of Harris's $1,975.00 to OE 33. It makes the pair symmetric on the credit axis while leaving it asymmetric on the receivable axis, which forces the unapplied-credit reasoning onto an owner whose receivable is zero. That is where netting is most tempting, because netting there produces a negative balance.

**B4 verdict: all five levers plus the contrast pair preserved. No lever was weakened by any edit since r5.**

---

## 5. B6 propagation to S3

Mandated by the file's own decompose directives: OE 30 (3 elements), OE 31 (2), OE 33 (10), OE 35 (1 with a two-branch accept-set), OE 36 (4). That is **20 criteria before S3 writes anything of its own**, against the hard ceiling of 60. S3 has room but should budget from 20, not from zero.

Propagated constraints, each of which S3 must honour or the artifacts drift:

1. OE 30: grade three record ids separately. Do **not** write a criterion over "the make-ready records" as a set; that manufactures the F8 NON_ATOMIC_ENUM defect.
2. OE 30: 4C, 207A and Sunset Ridge Unit 14 must not appear in any accept-set as required corrections. All three are licensed in both directions.
3. OE 31: both limbs are required and independent. The Harris limb accepts either verb provided the reschedule no longer stands as a second live meeting; the Finley limb accepts move or replace.
4. OE 33: the Harris make-ready criterion must pass on **either** the 7-row framing or the 6-row framing that drops the Unit 14 row on the ownership ground stated at OE 18. Both give "zero in a Ready state". Do not pin a row count.
5. OE 35: graded on title and description only. The issue number cannot be predicted (team_001 carries next_issue_number 1000) and **project and team must not be pinned**, even though OE 35 names proj_002 and team_001 as expected parameters.
6. OE 36: the accept-set is "lands in C006". Do not require a top-level post; the precedent sentence is a justification, not a lock-in, and channel-or-method lock-in is Major by default.
7. Rule 23 ordering check, answered here so S3 does not have to guess: **the prompt carries no ordering constraint.** It uses "as well" rather than "then", and the only sequencing words ("once this is handed over") are purpose clauses. Run `Validators/check_ordering_coverage.py` at S3, but the expected result on this prompt text is no ordering requirement and therefore no mandated Process rubric.
8. Rule 14 mirroring: any element cut from an OE decompose directive at S3 must be removed from that directive in the same pass.

---

## 6. B8 completeness

| Prompt clause | Step | Covered |
|---|---|---|
| "work out where each one actually stands today ... occupancy" | OE 11, 13, 14, 21, 33 | Yes, and the honest answer is that the figures have no supporting record |
| "what maintenance is still outstanding" | OE 18, 19 | Yes, MT-2026-047 plus the two Mitchell records excluded with reasons |
| "where the turns have got to" | OE 13 to 17, 30 | Yes |
| "anything on the money side" | OE 22 to 26 | Yes |
| "confirming it and filling in the gaps" (the spring read) | OE 8, 9, 20, 21, 33 | Yes, four refutations |
| "put those records right" | OE 30 | Yes, 3 graded rows |
| "Do the same for their review meetings" | OE 31 | Yes, both owners |
| "an email together for Brooke" | OE 32, 33 | Yes, recipient resolved and draft-only stated |
| "Bring the mid-year review item up to date" | OE 34 | Yes |
| "open a separate item" | OE 35 | Yes, exactly one, two-branch accept-set |
| "Post a short version in the owner relations channel" | OE 36 | Yes |

Eleven of eleven. No prompt clause is unstepped, and no step exists that the prompt does not license.

**B8 verdict: complete.**

---

## 7. B9 service mapping

Distinct tool mentions in the file: 72 across 35 distinct tools and **8 of 8 services**.

| Service | Mentions | Share | Writes |
|---|---:|---:|---:|
| quickbooks | 17 | 23.6% | 0 |
| gcalendar | 16 | 22.2% | 2 |
| airtable | 13 | 18.1% | 1 |
| linear | 11 | 15.3% | 2 |
| gmail | 7 | 9.7% | 1 |
| slack | 6 | 8.3% | 1 |
| hubspot | 1 | 1.4% | 0 |
| contacts | 1 | 1.4% | 0 |

Six services carry 5% or more and none dominates past 24%. This is the cross-correlation shape rather than the false-positive pattern where one service is stacked to reach a midpoint. Every step points at the service that actually holds the data: the owner-to-property link is in Linear, Slack and QuickBooks prose because Airtable carries no owner field (stated at OE 10); money is only in QuickBooks; meeting state is only on the calendar; turn state is only in Airtable. HubSpot is correctly demoted to one call, and OE 10 now says so in as many words.

**B9 verdict: correct mapping, no service misdirection.**

---

## 8. B-RULE13: single-target uniqueness, every-service sweep, naive-agent simulation

**Single target.** The three graded write targets were checked for a unique match. rec98bdfeec73545e is the only selSched row on Sunset Ridge 104B. rec8b679d92f30753 is the only Ridgeview row in the table. rec987aae7d522057 shares its unit with a second selSched row, reca06d89f1a4ac5b, and the file handles this correctly: it grades the first on the ground that two later rows answer the question it records as open, and instructs that the second be left alone because nothing in the universe resolves its utility-transfer wait. Both are named by record id, and the distinction is by content rather than by position. F7 is clear.

**Every-service sweep including Calendar.** Nine confirmed base events sit on or after 2026-07-01. Reconciliation status of each against the file:

| Event | Date | Reconciled where |
|---|---|---|
| Mesa Vista HOA Management Review | 07-08 | OE 35 |
| Make-Ready QC Inspection, Mesa Vista 4C | 07-15 | OE 30 weighs it, OE 35 names it |
| Q3 Make-Ready Planning and Budget Review | 07-23 | OE 35 |
| Vendor Walk-Through, Ridgeview Roof Repair Follow-Up | 07-13 | OE 15, OE 19, OE 30, OE 35 |
| JP Court Eviction Filing Appointment | 07-01 | Not named. Names Unit 14 and Patricia, names neither Harris nor Sunset Ridge, and sits in the delinquency workstream OE 18 excludes |
| Las Vistas 9D kickoff, Tommy Reyes renewal, Las Palmas 8D walk-through, Sunridge move-in | 07-02 to 07-09 | Out of both portfolios |

I checked the Harris side independently: **the only post-today event touching Sunset Ridge, Ridgeview or Harris anywhere in the universe is the Ridgeview follow-up**, which is on the Finley side and is reconciled four times over. So OE 35's "two candidates are carried nowhere" claim survives the sweep. F9 is clear on substance; see refinement R3 for the presentational gap.

**Naive-agent simulation.** Reading 5_Prompt.txt with the OE file closed: the prompt names two owners, a missed end-of-June deadline, four investigation areas, two conditional correction clauses and four deliverables. It names no property, no figure, no record, no state, no service and no discrepancy. An agent that reads it cannot know that the spring read was wrong, that a meeting was double booked, that credits exist, or that a record contradicts the ground. Every discriminator survives as an inference. The L36 test passes on these bytes.

---

## 9. Post-r5 delta audit: new claims, moved targets, widened accept-sets

Eleven steps changed between the r5 bytes (5aa21a8eb179a677) and ship. Every change was diffed sentence by sentence and every new factual assertion was re-derived.

**New claims introduced, all verified true:**

| Claim | Step | Verified |
|---|---|---|
| `search_crm_objects` object_type tickets, query "Mesa Vista" returns three near-identical tickets, one names Finley | OE 10 | 3 returned; only ticket_87552e6b23bc5a92bd2641b9054b8c13 contains "Finley" |
| `list_issues` query "reconciliation" reaches the OPS-39 / OPS-93 pair | OE 11 | 4 issues returned, both present |
| reca06d89f1a4ac5b waits on two things, the second being John's HVAC filter scope answer | OE 15 | fldNotes2 confirms both |
| `search_records` tblMaintenanceTickets "Tanya Mitchell" returns exactly those two | OE 18 | exactly 2: rec46234590708b5c, recc0ecc885e9645e |
| `search_records` tblMakeReady "Tanya Mitchell" returns exactly seven | OE 21 | exactly 7 |
| `search_records` tblMakeReady "Unit 14" returns five | OE 21 | exactly 5, including Rio Bend |
| The 4C owner email cites invoice "2026-537", which matches no DocNumber | OE 30 | Gmail thread 66132537181ecbe1 body contains "2026-537"; no DocNumber "2026-537" exists; the record described is 445653930748, DocNumber 2026-534 |
| rec12969a3fdb0852 names Castillo only inside a five-name assignment list | OE 30 | MT-2026-084 lists Tony Reyes, Carmen Delgado, Pete Donovan, Jaime Salinas and Linda Castillo |
| Harris carries $1,975.00 of unapplied credits | OE 33 | 195.00 + 1,250.00 + 530.00, each Balance equal to TotalAmt, none with LinkedTxn |
| `list_events` fullText "Mesa Vista" on brooke.phillips and teresa.wood returns three confirmed post-today events | OE 35 | exactly 3: 07-08, 07-15, 07-23. **This is my r6 finding and the fix is correct**; the r5 bytes said two |

**Moved graded targets: none.** The graded set is identical to r5: rec98bdfeec73545e, rec987aae7d522057 and rec8b679d92f30753 for the corrections; both review meetings; one new issue; one draft; one comment; one channel post. All three record ids re-confirmed still selSched, so the "forward out of selSched into selProg" direction is still the only one any evidence supports.

**Widened accept-sets: one, and the prompt licenses it.** OE 30's opening disjunction was rewritten from "the work has started or the question has been answered and the vendor schedule locked in" to a form that is true of all three graded rows, because the old wording did not describe the Ridgeview row (which is corrected on an invoice and a past event rather than on a sibling row). This narrows the mismatch between the stated rationale and the graded set rather than widening what an agent may do. No accept-set now admits an act the prompt does not license: every widened branch (4C either way, 207A either way, Unit 14 either way, 309C-utility left alone, delete or update on Harris, update or create on Finley, 310C or 309C as the new item) is a case where the universe genuinely underdetermines the answer.

**Scope creep check.** OE 10's HubSpot paragraph was converted from background prose into an actual step. That adds a call rather than a claim, and it is the correct direction: the file previously asserted a HubSpot fact without telling the agent how to reach it.

---

## 10. Findings

### Blockers: NONE.

No finding in this round meets the blocker test, which I state so the bar is visible: a blocker is a step that misses a critical path element, or that points at the wrong tool, service, parameter or expected data such that a literal walk produces a wrong trajectory. All 38 checks passed and no step fails that test.

### Refinements, for S3 or a later editing pass. None gate this deliverable.

**R1. OE 30 labels bill 991582431419 "the punch list".** Its PrivateNote is an internal labor charge for Carlos Mendez's make-ready walk of 4C, whose condition report says punch list items will drive *subsequent* bills. So the bill originates the punch list rather than paying it. I considered scoring OE Accuracy at 4 on this and did not, for a reason I will state rather than assume: the sentence is a four-item gloss on a set, not an expected-value claim, it sits in an explicitly non-graded aside (4C is out of the graded set), and a literal walk of the step (`search_bills` with "Mesa Vista" or "4C", four bills returned, turn corroborated) is correct either way. Suggested replacement for the tail of that sentence: "and the make-ready walk that filed the condition report". This is the closest call in the file and the operator should see it named.

**R2. OE 13 omits the cleanest disambiguator in the universe.** The step concedes the Sunset Ridge attribution "is not clean" and rests it on OPS-32, the hearing event and invoice 4422. It does not say that **none of the seven other properties Harris is billed for carries a single make-ready row**, which converts "weight of evidence" into "the only cluster with any turn record at all". Adding one sentence would strengthen the weakest link in the chain without changing any graded target.

**R3. OE 35's post-today sweep is asymmetric on its face.** It sweeps "Mesa Vista" and reconciles three events, but runs no equivalent sweep on the Harris side. I verified the claim survives (the Harris cluster carries zero post-today calendar work, and the JP Court filing on 07-01 names Unit 14 and Patricia but neither Harris nor Sunset Ridge, sitting in the workstream OE 18 already excludes). One sentence stating that would close the sweep symmetrically and pre-empt an F9 challenge from a reviewer who checks the calendar and finds an eviction appointment on a unit inside Harris's cluster enumeration.

**R4. S3 accept-set note, from section 5 item 4.** The Harris make-ready criterion must pass on both the 7-row and the 6-row framing. Both yield zero in a Ready state.

**R5. S3 pinning note, from section 5 item 5.** OE 35 names proj_002 and team_001 as parameters but grades on title and description. S3 must not lift those parameters into an accept-set condition.

---

## VERDICT: GO

Both sub-dimensions score 5 of 5 on the shipped bytes. B2 finds no unlicensed defensible path. B3 passes on both models scored separately, with revised midpoints of 65 Opus and 68 Gemini against a 40 design target and a 15 fail floor. B4 finds all five levers and the contrast pair preserved, with L11 and the contrast pair strictly stronger than at r5. B6 propagates eight constraints and a 20-criterion floor to S3. B8 finds eleven of eleven prompt clauses stepped. B9 finds 8 of 8 services correctly mapped with no service past 24%. B-RULE13 clears on single-target uniqueness, on the every-service calendar sweep and on naive-agent simulation. No edit since r5 introduced a false claim, moved a graded target, or widened an accept-set past what the prompt licenses. Five refinements are recorded above as notes for S3; none of them gates this file.
