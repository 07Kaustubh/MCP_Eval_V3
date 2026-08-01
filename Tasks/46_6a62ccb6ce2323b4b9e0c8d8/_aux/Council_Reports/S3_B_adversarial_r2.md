# S3 Council B (Adversarial QC) - Round 2

Task: `Tasks/46_6a62ccb6ce2323b4b9e0c8d8` | Universe: StarPM (V4) | Artifact: `7_Rubrics.json`, 32 criteria
Round 1 verdict: BLOCK (Major 0 / Moderate 4 / Minor 2). All round 1 findings accepted and applied.

Every factual claim below was re-derived from `_aux/Universe_Split/` in this round. Where a claim in a
justification field was checked and found sound, it is marked verified; where a finding I raised was
defeated by a universe fact, it is recorded as withdrawn with the fact quoted.

---

## R0. Round 1 closure audit

Six items. All six are genuinely closed. Two of the fixes introduced a new defect; both are logged in
the census below rather than here.

| R1 finding | Status | Verification performed this round |
|---|---|---|
| Mesa Vista count title vs evidence | **CLOSED** | Title 28 now reads "has more than one unit in a turn"; evidence accepts "any count from two to four". Title and evidence now assert the same proposition. `tblMakeReady` holds 8 Mesa Vista rows across 4 unit strings (107A x2, 207A x3, 310C x1, 4C x2), so the 2-to-4 band is the correct span between "still open on the latest row" (107A, 310C) and "any unit string with any row" (all four). Accept-set correctly preserved per Handoff section 3. |
| Harris duplicate over-specified direction | **CLOSED, new defect introduced** | Title 4 now grades the end state. Evidence now states both directions pass and that an RSVP must not be required. Verified against Handoff obligation 2: Lisa holds no row on `qqbwq3s2h7wh5udoek2940mffk`, so `respond_to_event` is unsatisfiable there. The direction fix is correct. It opened a degenerate-satisfaction hole: see **m1**. |
| Finley past-due DocNumbers | **CLOSED** | Title 10 now grades only `$10,980.00`. DocNumbers moved to justification. Re-verified in QuickBooks: `109367557444` (2026-494) Balance 8400.0, `129552155569` (2026-303) Balance 2190.0, `793996025934` (4421) Balance 390.0. Sum 10980.0. Fourth Finley invoice `110099741914` (5848) Balance 0.0, correctly excluded. |
| Occupancy-and-collections non-atomic | **CLOSED as a split, new defect introduced** | Now criteria 13 and 14. OE 33 directive mirrored: it now reads `... the occupancy correction, the collections correction ...` and separately `... Harris receivable position, Harris unapplied credits ...`. Mirroring confirmed by direct read of OE 33. Rule 14 satisfied. The collections half inherited a premise that does not hold for collections: see **M1**. |
| Slack open-item dependency | **CLOSED** | Criterion 24 now names both accept-set members by content, so it no longer passes on a bare reference to an issue that a failing antecedent never created. This is the rule 17 binding pattern applied correctly. |
| Water heater justification | **CLOSED, and correctly premised** | I opened this as a suspected regression and withdrew it. See the withdrawal in B8. |
| Council A: Sunset Ridge possessive | **CLOSED** | Titles 7 and 27 carry no ownership claim; both evidence fields carry "Do not require an owner attribution for Sunset Ridge". Consistent with the Handoff S3 obligation at line 244. |

---

## B1. Sub-dimension scoring

Sub-dimension names taken verbatim from `Docs_starpm/7_QC_Spec_Doc1.json`.

| Sub-dimension | Score | Basis |
|---|---|---|
| **Overall Rubric Quality** | **1 / 5** | Pass(5) requires zero major and zero moderate issues. Five moderate issues found (M1 to M5). Independently, the minor-or-worse band is breached: 9 of 32 criteria carry an issue, 28.1%, against a >20% fail threshold. Two independent routes to fail. |
| **All-Failing Rubrics** | **3 / 5 (projected)** | Measured at S4, projected here. Three criteria carry high all-fail risk (4, 32, 14). Of those, only criterion 14's risk is Bucket 1 (rubric invalid), which is 1 of 3 and under the >50% Bucket-1 fail threshold. The sub-dim therefore projects non-fail, while B9's own stated gate (2 or more predicted AF) fails. These are different tests and I am scoring them separately rather than collapsing them. |
| **Rubric Category Balance** | **5 / 5** | 32 Outcome, 0 Process. Outcome count exceeds Process count. This sub-dimension is binary with no 3/4 band; the condition is met. |
| **Process Rubrics** | **5 / 5** | Zero Process rubrics is correct here. I re-read `5_Prompt.txt` independently of the checker: the prompt contains no sequencing token. "once this is handed over" is a purpose clause on the new-item request, not a sequencing mandate, and "as well" is additive. Per rule 23 a Process rubric is required only for an ordering constraint, and there is none to grade. I am not recommending one. |
| **Agent Centric Phrasing** | **5 / 5** | All 32 titles open with "The Agent" followed by a present-tense act. No title names a tool. No title contains "at least N". Verified across all 32. |

---

## B2. Adversarial alternative-path attack

Three attacks run. Two are defended. One succeeds and is the sharpest structural finding in this round.

**Attack 1: answer from the chatter, skip the structured stores. DEFENDED.**
An agent that reconstructs the position from Slack C004/C006 and the Linear comments repeats 94% and
97% and reports the spring read as confirmed. It fails 13, 14, 25 and, having never opened QuickBooks,
fails 8, 9, 10, 11, 23, 29, 30, 31. Twelve criteria lost. L1 and L2 are both well defended against this.

**Attack 2: net the credits. DEFENDED.**
An agent that reports `$7,325.00` fails 10, 11, 23, 29 and 30 by explicit FAIL clause in each. Five
criteria. L11 is the best-carried lever in the set, which is the correct allocation given the Hardness
Plan rates its impact VERY HIGH.

**Attack 3: the competent agent that never leaves the persona's own calendar. SUCCEEDS.**
This is the task's designed hard core and it is the cheapest thing in the set to miss.

An agent that does all the Airtable correction work, all the QuickBooks arithmetic, all five spring-read
refutations, both Linear writes, the draft and the Slack post, and simply never enumerates calendars
Lisa Smith does not hold a row on, fails exactly two criteria: 4 and 32. It scores 30 of 32, 93.75%.

Against that, an agent that gets the `$10,980.00` arithmetic wrong loses three criteria (10, 23, 29),
9.4% of the set, because that one figure is graded three times across three artifacts.

So the set currently prices a single arithmetic slip higher than the entire off-persona calendar
enumeration that the Hardness Plan and the Handoff both identify as the task's distinguishing
difficulty. The score is weighted away from the design. This drives **M5** and **m5** below.

---

## B3. Tool-call density projection

Counted per service against the retrieval surface the OE file actually names, not against the step count.

| Service | Reads | Basis |
|---|---|---|
| Airtable | 8 to 12 | `tblMakeReady` (120 rows) and `tblMaintenanceTickets` (50 rows) each need list plus targeted `search_records`; OE 30 alone names a `tblMaintenanceTickets` query "Mesa Vista", and the graded rows require reading sibling rows per unit (104B x2, 309C x4, Ridgeview x1). |
| QuickBooks | 10 to 16 | 155 invoices, 117 credit memos, 54 payments, 123 estimates, 113 bills. OE names `search_invoices`, `search_credit_memos`, `search_payments`, `search_estimates` query "Harris", `search_bills` query "Mesa Vista"/"4C", plus per-entity gets to read `Balance`, `LinkedTxn` and `RemainingCredit`. The credit-memo lever cannot be resolved from a search summary alone. |
| Calendar | 7 to 12 | `list_calendars` plus `list_events` across at least brooke, patricia, teresa, and for the OE 30 4C check carlos and wesley. The Harris duplicate is unreachable without this fan-out. |
| Gmail | 4 to 7 | `search_threads` query "make-ready", `get_thread`, plus the Mitchell cure-deadline thread and the Castillo authorization message. |
| Slack | 4 to 6 | C004 spring-read thread (parent plus replies) and C006 month-end thread. Note the dangling `latest_reply` hazard at Handoff Hazards item 2 forces a second call on at least one thread. |
| Linear | 5 to 8 | 5 near-identical owner-review issues must be read to discriminate OPS-10; plus OPS-32, OPS-100 and comments. |
| HubSpot / Contacts | 2 to 4 | Brooke resolution and the Finley move-out ticket bridge. |
| Writes | 6 to 9 | 3 Airtable row updates (1 batched call or 3 separate), 1 to 2 calendar writes, 1 draft, 1 Linear comment, 1 Linear issue, 1 Slack post. |

**Low 42 | High 68 | Midpoint 55.**

**Verdict: PASS.** Midpoint 55 clears the V4 target of >= 40 with margin. Note the margin is not evenly
held: roughly 9 of the projected calls are the calendar fan-out, and an agent that skips it (Attack 3)
lands near 46, still above the gate. Density is not the exposure on this task.

---

## B4. Lever coverage

Lever definitions read from `_aux/Hardness_Plan.md` lines 52 to 56, not inferred.

| Lever | Definition (Hardness Plan) | Weight | Carrier criteria | Assessment |
|---|---|---|---|---|
| **L1** | Latching on the persona's own undispositioned claim | 6.5 | 13, 14, 15, 16, 17, 25, 28 | **Strong, 7 carriers.** Highest-weight lever in the plan and the measured cross-model differentiator. Carrier 14 is defective (M1) and the fix must not reduce the carrier count. |
| **L2** | Structured-DB skip (QuickBooks AR plus the unmirrored Calendar) | 5.5 | AR: 8, 9, 10, 11, 23, 29, 30, 31. Calendar: 4, 5, 32 | **Strong.** Both halves carried. Handoff section 15 records that L2's calendar half is knowingly attenuated by the prompt naming "review meetings"; that attenuation is a prompt property and is not re-litigated here. |
| **L7** | Multi-write diversification | 10.5 | 1, 2, 3 (Airtable), 4, 5 (Calendar), 6 (Gmail), 18, 20 (Linear), 21 (Slack) | **Strong, 6 services / 9 write carriers.** Highest weight in the plan. Two defects sit on this surface: M2 (criterion 20 cardinality) and M4 (Slack post content gap). |
| **L10** | Reversal / supersession (Harris double-booked review; **OPS-10 state vs its own narrative**; OPS-39 vs OPS-93) | 5.0 | 4, 32 **only** | **UNDER-CARRIED. See M5.** The Hardness Plan names three L10 instances. Only the Harris double-booking is carried, and both of its carriers depend on the single retrieval that the Handoff pre-registers as this task's highest all-fail risk. |
| **L11** | Net-vs-gross (117 unapplied credit memos) | 5.5 | 9, 11, 30, reinforced by FAIL clauses in 10, 23, 29 | **Strong, and correctly budgeted.** Handoff section 6 required L11 to be explicitly budgeted because it has no Outcome 1.1 carrier. Confirmed: 9, 11 and 30 are all written content criteria, none is a write-action criterion, and none was lost. |

---

## B5. Reverse coverage, both directions

**Forward, OE decompose directive to criterion.** Every directive was read from `6_Oracle_Events.txt`
this round.

| OE | Directive elements | Carriers | Result |
|---|---|---|---|
| 30 | 3 (`rec98bdfeec73545e`, `rec987aae7d522057`, `rec8b679d92f30753` to selProg) | 1, 2, 3 | 3 / 3 complete |
| 31 | 2 (Harris duplicate no longer two live meetings; Finley review rescheduled or replaced) | 4, 5 | 2 / 2 complete |
| 33 | 12 (recipient, Harris make-ready, Harris receivable, Harris credits, Finley receivable, Finley credits, Finley maintenance, occupancy, collections, make-ready count, water heater, late payment) | 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 | **12 / 12 complete.** The round 1 split is fully mirrored in both directions. |
| 34 | none issued | 18, 19 | Covered, but 19 is non-atomic: see M3 |
| 35 | "S3 must write this as a single criterion" | 20 | 1 / 1, but cardinality contradicts the OE: see M2 |
| 36 | 4 (post lands in C006, both owners named, Finley past-due stated, open item named) | 21, 22, 23, 24 | 4 / 4 against the directive, **but the directive is short of the OE's own prose: see M4** |

**Reverse, criterion to OE.** All 32 criteria trace to an OE step. No orphan criterion. Criteria 25 to 32
are Outcome 2.1 restatements over OE 33, OE 31 and OE 26 content and are traceable.

**Gap found: OE 36 prose versus OE 36 directive.** OE 36 states the post carries "the two owners named,
**the Harris turn position**, the Finley past-due position, the one item still open, and **the fact that
the hand-off has gone to Brooke**". That is five content items. The decompose directive on the same line
names four and silently drops the Harris turn position and the hand-off statement. The rubric set
faithfully implements the directive, so the miss is inherited rather than introduced, but the effect is
that **no criterion requires the Slack post to carry any Harris substance at all**. Logged as M4.

---

## B6. Atomicity

Twenty-nine of 32 criteria are atomic. Three are examined; two are findings.

**Criterion 19 - NOT ATOMIC.** Title: "states in the OPS-10 comment that the Harry Harris and Robert
Finley half of the mid-year review has been handed to Brooke Phillips." Evidence requires "both owner
names **and** a statement that the hand-off has gone to Brooke Phillips", with an independent FAIL clause
on covering only one owner. That is two independently failable content elements conjoined in one
criterion, which is the F8 NON_ATOMIC_ENUM shape hard rule 13 forbids. It is also internally inconsistent
with the set's own convention: in the Slack group, "both owners named" is broken out as its own criterion
(22) separate from the other post content. Logged as **M3**.

**Criterion 30 - NOT ATOMIC.** "the credit memos on **both owners' accounts** are unapplied and do not
reduce **either** balance." The draft group splits exactly this content per owner (9 for Harris at
`$1,975.00`, 11 for Finley at `$3,655.00`); the final-response group re-bundles it. This creates a real
and slightly unfair fail: Harris carries `Balance 0.0` on all three invoices (`113714702211`,
`317923399822`, `879979204592`, each matched by a payment of identical amount), so for Harris the phrase
"do not reduce his balance" is vacuous. An agent that summarises the credit trap only where it changes
the answer, on Finley, fails 30 having reasoned correctly. Logged as **m6**.

**Criteria 9 and 11 - ATOMIC, examined and cleared.** Each requires an amount plus an unapplied
qualifier. I considered flagging these as conjunctions and withdrew it: the amount without the qualifier
is a materially different and incorrect claim (it is the netting error the lever exists to catch), so the
two parts are not separable into independently meaningful criteria. They are one proposition.

---

## B7. Overlap

**The final-response group is a 7-of-8 mirror of the draft group.** Mapping:

| Fact | Draft carrier | Final-response carrier | Third carrier |
|---|---|---|---|
| Sunset Ridge none Ready | 7 | 27 | |
| Harris `$0.00` receivable | 8 | 31 | |
| Finley `$10,980.00` | 10 | 29 | **23 (Slack)** |
| Credits unapplied | 9, 11 | 30 | |
| MT-2026-047 open | 12 | 26 | |
| Occupancy 94% unsupported | 13 | 25 | |
| Mesa Vista count > 1 | 15 | 28 | |
| Harris duplicate review | (none) | 32 | 4 (calendar write) |

Only criterion 32 is unique to the final-response group. These are formally distinct artifacts (a draft
body versus a final response), so this is not a guidelines violation, and the pipeline cannot check it
mechanically because `7_Rubrics.json` carries no `sub_category` field (rule 24). But the practical effect
is measurable: the eight final-response criteria will co-vary almost perfectly with their draft twins,
because an agent that computed a figure puts it in both places. The set's effective information content
is closer to 24 than 32.

**Triple jeopardy on `$10,980.00`.** Criteria 10, 23 and 29 grade the identical figure. One arithmetic
slip costs 9.4% of the set, more than the entire L10 lever costs (6.25%). Logged as **m5** with a
recommendation to cut 29, which is the lowest-signal of the three: 10 and 23 grade prompt-mandated
artifacts (the email and the channel post), while 29 grades a restatement of both.

**No nested accept-sets found.** I checked specifically for the rule 17 shape, a criterion that can pass
in a run where the criterion creating its subject artifact failed. Criterion 24 was the round 1 instance
and is now bound by content. Re-checked 19 against 18 (19 grades comment body, 18 grades comment
existence; 19 cannot pass without the comment) and 22/23/24 against 21 (all grade the C006 message text,
none can pass without the post). Clean.

---

## B8. Severity census

Denominator 32. A criterion carrying more than one issue is counted once.

### Moderate (5)

**M1. Criterion 14 forbids the correct answer. Overly Specific.**
Evidence: "FAIL if the draft asserts a different collections percentage of its own."
This clause was lifted from the occupancy criterion, where it is correct, onto collections, where the
premise does not hold. The premise for occupancy is that no occupancy data of any kind exists: `airtable`
in this universe carries exactly two tables, `tblMaintenanceTickets` and `tblMakeReady`, with no unit
table, no lease table and no property table, so an occupancy rate is genuinely uncomputable. Collections
is different. It is computable from the same `Balance` and `TotalAmt` fields the set requires the agent
to sum elsewhere:

- Robert Finley: `$640.00` collected of `$11,620.00` billed = 5.5%.
- Both owners: `$2,555.00` collected of `$13,535.00` billed = 18.9%.

An agent that refutes the 97% claim **and** reports the real figure has done exactly what the prompt asks
("the real position ... plus anything on the money side either of them is likely to raise with me") and
is failed by this clause. The set simultaneously requires the agent to derive `$10,980.00`, `$3,655.00`
and `$1,975.00` from those fields and forbids deriving a ratio from them. That is an internal
contradiction, and the derived figure is not marginal: it is 18.9% against a claimed 97%, which is the
most forceful available refutation.
**Fix:** delete the second FAIL clause from criterion 14, or narrow it to "FAIL if the draft asserts a
collections percentage sourced from the spring read rather than computed from the invoice records". Do
not touch criterion 13, where the identical clause is sound. This must not reduce L1's carrier count.

**M2. Criterion 20 contradicts OE 35 on cardinality and reproduces the F8 shape.**
Criterion 20 evidence: "Creating a second issue for the other candidate does not fail this criterion."
OE 35, read verbatim this round: "**Exactly one issue is expected, matching the prompt's 'a separate
item'.**"
Handoff obligation 6b: "S3 must pin the expected count explicitly rather than leaving it open, or it
manufactures exactly the F8 NON_ATOMIC_ENUM shape hard rule 13 forbids. **Do not write a criterion that
passes on 'one or more items'.**"
The evidence field does precisely what the obligation forbids, and it contradicts the OE it implements.
The two are separable things and the criterion conflates them: the **target** accept-set is deliberately
broad (OE 35: "an agent that raises the 309C blocker instead has picked a defensible target and must not
be marked down") and must be preserved; the **cardinality** is pinned at one and is not an accept-set.
`check_oe_rubric_sync` cannot catch this because it reconciles decompose directives, not cardinality
prose, which is why it cleared.
**Fix:** delete the sentence blessing a second issue. If two issues really are acceptable, OE 35 must be
amended in the same pass per rule 14, but OE 35's own reasoning ("The prompt asks for one item") argues
against that.

**M3. Criterion 19 is a two-element conjunction.** See B6. F8 NON_ATOMIC_ENUM, and inconsistent with the
set's own treatment of identical content at criterion 22.
**Fix:** split into two criteria (both owners named in the OPS-10 comment; the hand-off to Brooke stated
in the OPS-10 comment) and add a matching decompose directive to OE 34, which currently issues none.
Budget permits: 32 to 33.

**M4. The Slack post has no Harris-substance carrier. Coverage gap.**
OE 36 prose requires the post to carry the Harris turn position and the hand-off statement; the OE's own
decompose directive drops both; no criterion grades either. A post reading "Harris and Finley update:
Finley is `$10,980.00` past due and the 310C subfloor assessment is still open" passes 21, 22, 23 and 24
while saying nothing whatsoever about where Harris sits. The prompt's stated purpose for the post is
"so Patricia and the rest of the team can see where my two sit without having to come and ask me", which
that post does not serve for one of the two.
**Fix:** add one criterion (the post states the Harris turn position, that no Sunset Ridge unit has
reached Ready, or that Harris carries no past-due balance; accept either) and mirror it into OE 36's
decompose directive. Budget permits.

**M5. L10 is carried only by the two criteria pre-registered as this task's highest all-fail risk.**
The Hardness Plan (line 53) defines L10 over three instances: the Harris double-booked review, the
**OPS-10 state versus its own narrative**, and OPS-39 versus OPS-93. Only the first is carried, by
criteria 4 and 32. Both of those depend on one retrieval, enumerating calendars Lisa Smith holds no row
on. The Handoff pre-registers that exact retrieval twice (section 14 and Hazards item 1) as "the most
likely place this task produces an all-failing criterion".
If S4 applies rule 21's default for an all-failing criterion, which is removal rather than justification,
**L10 loses every carrier it has**, and the set retains no trace of a lever weighted 5.0 with HIGH impact.
This is the precise hazard Handoff section 6 raised for L11 and that was correctly defended there by
budgeting L11 explicitly; L10 received no equivalent treatment.
Criterion 18's evidence compounds it: "Do not require any change to the issue state, which is optional
here." That is correct against OE 34, which does not expect the state change. But it means the OPS-10
half of L10, the contradiction between the issue's recorded state and its own comment narrative, is
graded nowhere.
**Fix:** add one criterion carrying L10 through the OPS-10 narrative contradiction. That instance sits
in Linear, a service the persona has full access to, so it is reachable without the off-persona calendar
fan-out and does not inherit the all-fail risk. This is a lever-preservation add, not a coverage add, and
rule 14 forbids ever cutting a lever carrier. Budget permits.

### Minor (6)

**m1. Criterion 4 admits two degenerate satisfactions. Overly Broad.**
Evidence: "Look for a calendar write that cancels, deletes or renames **one of** the two Harris review
events." FAIL clauses: both left standing as confirmed; a third created without retiring either.
Neither clause excludes **deleting both**. A grader operationalising the evidence sees that deleting both
includes deleting one, that the two events are not "left standing as confirmed", and that no third was
created, so it passes. Zero live reviews defeats the prompt, which asks for meetings that "did not end up
properly settled" to be settled, not erased. (Delete-both-then-create-one is a legitimate resolution and
already passes correctly; it is delete-both-and-stop that is wrong and ungraded.)
Second route: "renames" is blessed as a passing verb on its own. A bare rename of the June 2 event leaves
both instances confirmed and live, on five and four per-calendar rows respectively, with nothing retired.
**Fix:** add "FAIL if no Harris mid-year review remains on the calendar" and qualify the rename route as
a retitle that marks the instance cancelled or superseded.

**m2. Criterion 26 title asserts a universal the evidence never grades.**
Title: "the **only** open maintenance ticket in either owner's scope", which is a universal negative over
50 maintenance rows. Evidence asks only that MT-2026-047 be "identified as the outstanding maintenance
item for these two owners", with FAIL clauses on reporting no outstanding maintenance and on pulling the
Mitchell records into Harris's position. Neither requires exclusivity. Per rule 16, a title that induces a
stricter reading than the evidence intends is a rubric defect, not a judge error.
**Fix:** align the title to the evidence ("identifies MT-2026-047 as the outstanding maintenance item")
or add the exclusivity requirement to the evidence. The first is preferable given the scope caveats.

**m3 and m4. Criteria 15 and 28: "the spring read" is ambiguous between two real messages.**
Two Lisa Smith to Brooke Phillips messages qualify as a spring read, and they disagree:

- `49b2873d46d55e4291a78d91d91a5054` / `5f60afa12c4c53b6b7694d59373acae8`, C004, 2026-05-12, from
  `U6480117503` (lisa.smith): "quick status on **Harris and Finley**: occupancy is solid, **two
  make-readies** on track, no escalations to flag." This is the one that matches the prompt's phrase "a
  rough read on **my two**", and the Handoff pins it as L1 at line 62 to 64.
- `a6779a055eaf5fb1893d0ed6d92e3b39`, C006, 2026-05-28, same author: "**Robert's Mesa Vista portfolio**
  is sitting at 94% occupancy, **one unit still in make-ready** ... Collections at 97% ..." This is a
  reply to Brooke's request to start "Robert Finley's May report for Mesa Vista", so it covers one owner.

Criteria 15 and 28 refute "one unit", which comes only from the second message, while calling it "the
spring read", which the prompt's wording points at the first. An agent anchoring on the C004 pair finds no
single-unit claim to correct at all.
**Fix:** name the source in the title or evidence as the May month-end Mesa Vista report rather than "the
spring read". One phrase per criterion. No grading behaviour changes; this removes a grader ambiguity.

**m5. Criterion 29 is the third grading of `$10,980.00`.** See B7. Recommend cutting 29 and, per rule 14,
confirming it carries no lever alone before the cut (it does not; L2's AR half is carried by 8, 9, 10, 11,
23, 30, 31). This is a rule 28 weak-assertion trim, not a coverage cut.

**m6. Criterion 30 bundles both owners.** See B6.
**Fix:** either split per owner to match 9 and 11, or add "accept a statement scoped to Finley alone,
since Harris carries no balance for the credits to offset".

### Findings raised and withdrawn

Both are recorded because a decline must rest on a re-read fact, and because a future round should not
re-open them.

**Withdrawn: criterion 16's justification is not a regression.** I opened this on the round 1 fix, which
replaced "Tommy Reyes's unit" with "412 Mesquite and Pinecrest 12" on the premise that "both Reyes tickets
are open", while `rec8c69237d76b259`'s description reads "Water heater replacement **completed** in-house
by John Smith". Re-read of the field settles it: `rec8c69237d76b259` carries `fldCompletionDate` **null**
and `rec18899b6ec2a65f` carries `fldCompletionDate` **''**, so by the field test both Reyes tickets are
open and the round 1 premise holds. Separately, `recb5119334a90255` (Pinecrest 12) carries
`fldCompletionDate` **'2026-05-11'**, so it is genuinely closed water heater work and the replacement
justification is correct. The description-versus-field contradiction on `rec8c69237d76b259` is real but
harmless here, and criterion 26's evidence already handles the two null encodings explicitly.

**Withdrawn: the 2-to-4 Mesa Vista accept-set is not reward-hackable via the C004 message.** I opened
this on the theory that an agent could echo C004's "two make-readies on track" and pass a criterion whose
title claims it corrected the spring count. It fails on the message text: `49b2873d...` and `5f60afa1...`
name no property, and criteria 15 and 28 both require the count to be scoped to Mesa Vista. The echo path
requires the agent to also invent a scope. The accept-set stands and Handoff section 3 forbids narrowing
it. Only the title-source ambiguity survives, as m3/m4.

### Threshold math, denominator 32

| Band | Count | Share | Threshold | Result |
|---|---|---|---|---|
| Major | 0 | 0.0% | fail at >10% | PASS |
| Moderate or Major (criterion-attached: 14, 20, 19) | 3 | 9.4% | fail at >15% | PASS |
| Minor or worse (adds 4, 26, 15, 28, 29, 30) | 9 | **28.1%** | fail at >20% | **FAIL** |

M4 and M5 are coverage absences with no criterion to attach to and are therefore excluded from the
percentage denominators, but they are counted in the headline census and both independently prevent
Overall Rubric Quality from reaching 5, which requires zero moderate issues of any kind.

**Census: Major 0 / Moderate 5 / Minor 6.**

---

## B9. Pre-submission all-fail prediction

| Criterion | Risk | Root cause | Bucket if it lands |
|---|---|---|---|
| **4** | HIGH | `qqbwq3s2h7wh5udoek2940mffk` carries four per-calendar rows and Lisa Smith holds none of them. An agent scoping Calendar to the persona sees exactly two review events, one per owner, which positively confirms the prompt's "either of those" while the double-booking stays invisible. Pre-registered at Handoff section 14 and Hazards item 1. | 3 (desired difficulty) |
| **32** | HIGH | Identical root cause. An agent that never finds the duplicate cannot report it. | 3 |
| **14** | HIGH | **Self-inflicted.** Both natural agent behaviours fail: repeating 97% fails the first clause, computing the real 18.9% fails the second. Only the narrow "unconfirmable, and I will give you no number" passes. See M1. | **1 (rubric invalid)** |

**Predicted all-failing criteria: 3. B9 gate is 2 or more. B9 = FAIL.**

Two qualifications, stated because they change what should be done rather than softening the result:

1. Criteria 4 and 32 are one root cause, not two. A single successful `list_calendars` plus `list_events`
   fan-out unlocks both. They are genuinely reachable (both tools exist, OE 13 names the query) and the
   difficulty is by design, so under rule 21 they are an S4 judgment, not an S3 fix. Their AF risk is not
   grounds to weaken them.
2. Criterion 14's AF risk is **not** by design. It is manufactured by the evidence field and is fully
   removable at S3 today, at no cost to L1. Fixing M1 drops the prediction to 2, still at the gate, but
   removes the only Bucket 1 candidate, which is what the All-Failing Rubrics sub-dimension actually
   measures.

M5's fix bears directly on this section: adding an OPS-10 L10 carrier means that if 4 and 32 are removed
at S4 under rule 21, the lever survives.

---

## B10. Verdict

**VERDICT: BLOCK**

**Major 0 / Moderate 5 / Minor 6**

Round 1's six findings are all genuinely closed and the OE mirroring was performed correctly in the same
pass. Two of the fixes opened new defects (M1 from the occupancy/collections split, m1 from the
direction-agnostic duplicate criterion), which is the specific thing this round was asked to check.

Blocking items, in fix order:

1. **M1** (criterion 14 forbids the correct answer) - one clause deletion, and the only Bucket 1 all-fail
   candidate in the set.
2. **M2** (criterion 20 contradicts OE 35 on cardinality) - one sentence deletion.
3. **M5** (L10 carried only by the pre-registered all-fail pair) - add one criterion.
4. **M4** (no Harris substance required in the Slack post) - add one criterion, mirror into OE 36.
5. **M3** (criterion 19 non-atomic) - split into two, add a decompose directive to OE 34.
6. **m1, m2, m3, m4, m6** - wording repairs, no structural change.
7. **m5** - recommended trim of criterion 29, not blocking.

Net criterion count after the recommended changes: 32 minus 1 (m5 trim) plus 3 (M3 split, M4 add, M5 add)
= **34**, well inside the 60 ceiling. No lever carrier is cut. The four deliberate accept-set breadths
recorded in Handoff section 3 are preserved in every recommendation above, and no recommendation requires
naming the owner of Sunset Ridge Unit 14, asserts an occupancy figure, or rests a Sunset Ridge correction
on elapsed time rather than supersession.

Re-run required after fixes: `validate.py --phase rubrics`, `--phase submission_gate`,
`check_oe_rubric_sync` (OE 34 and OE 36 both change), `check_rubric_antipatterns`, `check_qc_binary`.
