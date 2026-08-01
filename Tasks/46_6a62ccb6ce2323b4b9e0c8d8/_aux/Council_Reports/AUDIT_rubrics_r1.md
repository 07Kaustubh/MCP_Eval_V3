# AUDIT - S3 rubrics - Tasks/46_6a62ccb6ce2323b4b9e0c8d8

Universe starpm (V4), read from `_aux/Universe.txt`. Mode: auto-fire S3 exit gate, strictest interpretation.
Artifact audited: `7_Rubrics.json`, 35 criteria, 35 outcome / 0 process.

Council A and Council B are treated as CLAIMS throughout (rule 18). Every atom below was re-derived from
`_aux/Universe_Split/` in this pass. Council B's report is written against a superseded **32-criterion**
numbering; its "criterion 29" is today's **31**, its "criterion 32" is today's **34**. All numbers in this
report are the CURRENT 35-criterion numbering unless labelled otherwise.

---

## Deterministic floor (cited, not re-argued)

| Gate | Exit |
|---|---|
| `validate.py --phase rubrics` | 0 fails, 17 warns, 5 notes |
| `validate.py --phase oe` / `submission_gate` / `injection` | 0 fails, 0 warns each |
| `check_qc_binary.py` | 6/6 measurable binary sub-dims PASS |
| `check_rubric_antipatterns.py` | 0 construction anti-patterns |
| `check_ordering_coverage.py` | 0 ordering language, zero Process is correct (rule 23 does not fire) |
| `check_oe_rubric_sync.py` | every decompose element has a carrier |
| `check_criterion_dependencies.py` | SKIP, no verifier export yet |

Everything those gates cover is settled and is not re-litigated here.

---

## Per-atom evidence table (v18 requirement for any Truthfulness 5/5)

Re-derived directly from `_aux/Universe_Split/`. This is the pass that would have caught a fabricated figure.

| Atom asserted | Universe query | Result | Verdict |
|---|---|---|---|
| Harris open receivable $0.00 (crit 8, 33) | qb invoices where CustomerRef.name=Harry Harris | 3 invoices, Balance 0.00 on all three | PASS |
| Harris credits $1,975.00 (crit 9) | qb credit_memo, same customer | 195.00 + 1250.00 + 530.00 = 1975.00, each Balance==TotalAmt, LinkedTxn None, RemainingCredit 0 | PASS |
| Finley past due $10,980.00 (crit 10, 24, 31) | qb invoices, CustomerRef.name=Robert Finley | 8400.00 + 2190.00 + 390.00 = 10980.00; 4th invoice 5848 settled at 0.00 and correctly excluded | PASS |
| Finley credits $3,655.00 (crit 11) | qb credit_memo, same customer | 2755.00 + 490.00 + 410.00 = 3655.00, all unapplied on the same shape | PASS |
| $1,622.00 decoy is Linda Castillo (crit 10, 31) | qb id 445653930748 | DocNumber 2026-534, CustomerRef Linda Castillo, three Mesa Vista Unit 4C pass-through lines | PASS, and a well-chosen trap |
| All 10 ids cited in justifications exist | id lookup across 625 qb entities | 10 of 10 resolve to the correct entity, customer and amount | PASS, no fabrication |
| Sunset Ridge: 7 rows, 3 unit strings, zero selReady (crit 7, 29) | airtable tblMakeReady | 104B x2, 309C x4, Unit 14 x1; statuses selSched/selProg only | PASS |
| Mesa Vista: 8 rows, 4 unit strings (crit 15, 30) | same | 107A x2, 207A x3, 310C x1, 4C x2 | PASS |
| Ridgeview rec8b679d92f30753 is the sole row (crit 3) | same | 1 row, selSched | PASS |
| 309C has exactly two selSched rows (crit 2) | same | rec987aae7d522057 (deep-clean question) and reca06d89f1a4ac5b (utility transfer) | PASS, graded row pinned by content per Handoff item 7 |
| MT-2026-047 open, 7 of 50 (crit 12, 28) | tblMaintenanceTickets, empty fldCompletionDate | exactly 7 of 50 open, split 3 empty-string + 4 null exactly as crit 28 evidence warns; MT-2026-047 is the ONLY open ticket naming Harris/Finley/Mesa Vista/Sunset Ridge/Ridgeview | PASS |
| OPS-10 Backlog vs comment narrative (crit 35) | linear_issues + comments | state_OPS_0, created_at == updated_at, two comments announcing In Progress and In Review | PASS |
| OPS-10 unique on "Mid-Year" (crit 18) | title scan, 230 issues | 1 of 230; OPS-11/13/20/23 confirmed as near-identical decoys | PASS |
| team_001 next_issue_number 1000 (crit 21) | linear_teams | 1000, so the identifier is genuinely unpredictable | PASS |
| Finley 05-19 declined by Lisa and Aurora; zero Finley events 06-01..09 (crit 5) | gcalendar | responseStatus declined for both; 0 events in window | PASS |
| Harris duplicate, June 3 unreachable on persona (crit 4, 34) | gcalendar per-calendar rows | June 2 on 5 calendars INCLUDING lisa.smith; June 3 "(Rescheduled)" on 4 calendars, NO lisa.smith row, Lisa not an attendee | PASS as an atom, and see F1 |

No atom failed. Truthfulness and Accuracy score 5/5 on evidence, not on narration.

---

## Lens 1 - Strict QC scoring

| Sub-dim | Score | Basis |
|---|---|---|
| Overall Rubric Quality | **4** | One Moderate (F2) and two Minor (F3, F5). Pass(5) requires zero Major AND zero Moderate (rule 27). One Moderate costs the 5. |
| All-Failing Rubrics | **3 (projected)** | 2 predicted AF (F1). Both are Bucket 3 defensible, so the >50% Bucket-1 route does not fail, but the Eval's own pre-submission gate does. |
| Rubric Category Balance | **5** | 35 outcome, 0 process. Binary, condition met. |
| Process Rubrics | **5** | Zero is correct. I re-read the prompt cold: no sequencing token. "once this is handed over" is a purpose clause, "as well" is additive. Rule 23 does not fire. |
| Agent Centric Phrasing | **5** | All 35 titles open "The Agent" + present-tense act. No tool name in any title. No "at least N". |
| Truthfulness / Universe grounding | **5** | Per-atom table above, 18 of 18 verified. |

Two sub-dims below 5. Both trace to findings listed below.

## Lens 2 - Answer-leakage sweep

The derived figures are $10,980.00, $1,975.00, $3,655.00, and the refutations of 94% and 97%.
I searched every artifact body and every record the prompt directs the agent to read.
No aggregate appears pre-computed in any readable record: the agent must sum three invoice Balances per
owner. The 94% and 97% appear ONLY in Lisa's own Slack message and its Linear echo, which is the designed
trap rather than leakage (the agent must refute them, not copy them). Arithmetic neighbours ($7,325.00 the
credit-netted figure, $1,622.00 the Castillo invoice) are present in the universe and are explicitly
FAIL-clause'd in criteria 10, 24 and 31. **No leakage. No BLOCKER.**

## Lens 3 - Hardness end-to-end

L1 (undispositioned own claim): prompt "a fair bit of this should just be confirming it" to OE 33 to criteria 13,14,15,16,17 plus 27,30. Carried.
L2 (structured-DB skip): AR half carried by 8,9,10,11,24,31,33; calendar half by 4,5,34. Carried.
L7 (multi-write diversification): 6 services, write carriers 1,2,3 (Airtable), 4,5 (Calendar), 6 (Gmail), 18,21 (Linear), 22 (Slack). Carried.
L10 (reversal/supersession): Harris double-booking by 4,34; OPS-10 state vs narrative by **35**, which is the Council B M5 add and is present. Carried on two instances, so F1's fix does not strip the lever.
L11 (net-vs-gross): 9,11,32, reinforced by FAIL clauses in 10,24,31. No write carrier, exactly as Handoff obligation 6 requires. Carried.

**No HARDNESS_REGRESSION.** All five levers trace prompt to OE to criterion to atom.

## Lens 4 - Strict density

Framework-scoped. `Reference/Sessions/AUDIT.md` line 105 and AGENTS.md rule 11 both state the 50/40 scheme
is V3-family and say explicitly "Never apply the 50/40 scheme to a StarPM task"; the V4 bar is midpoint
>= 40 PASS, 15-39 THIN, < 15 INSUFFICIENT, per model. **The task brief's instruction to apply a 50+ bar
contradicts the project's own framework-scoped rule.** I report both rather than silently picking one.

My independent projection, strictest reading (minimising inferred exploration):

| Service | Low | High |
|---|---|---|
| Airtable (120 + 50 rows, list + targeted search + sibling reads) | 4 | 8 |
| QuickBooks (155 inv / 117 CM / 54 pay; per-entity gets needed for Balance, LinkedTxn, RemainingCredit) | 8 | 14 |
| Calendar (list_calendars + per-calendar list_events fan-out) | 3 | 11 |
| Gmail (search_threads + get_thread) | 3 | 6 |
| Slack (C004 spring-read thread + C006) | 3 | 5 |
| Linear (5 near-identical issues discriminated + OPS-10 + comments) | 5 | 8 |
| HubSpot / Contacts | 2 | 4 |
| Writes | 6 | 9 |

**Low 34 | High 65 | Midpoint 49.5.**

Verdict against the correct V4 bar (40+): **PASS** with margin.
Verdict against the 50 bar named in the brief: marginal, 49.5 sits just under.
**Coupling worth recording:** roughly 8 of the projected calls are the off-persona calendar fan-out. The
agent behaviour that produces F1 (skipping that fan-out) also removes those calls, taking the midpoint to
about 42. Still clears 40. The density margin and the AF risk are the same variable.

## Lens 5 - Adversarial veteran review

Framing preserved across all three artifacts: the prompt says "put those records right", the OE moves three
rows forward, the criteria grade exactly those three rows. No rubric demands a "flag it" step where the
prompt says "fix it".
No entity drift: Brooke resolves to one contact, criteria consistently use brooke.phillips@starpm.com.
No silent process rubrics: all 35 grade end states.
No tool names in titles, no em-dashes, no "at least N", no "approximately" near an id or date (the three
"approximately" uses sit on dollar totals where tolerance is intended and correct).
No channel lock-in beyond what the prompt itself names (the prompt names the email, the tracker and the
owner relations channel explicitly, so criteria 6, 18, 22 are prompt-mandated, not imposed).
Nested accept-sets: re-checked independently. 7-17 are bound to "the draft addressed to
brooke.phillips@starpm.com", 19-20 to "the comment on OPS-10", 23-26 to "the message text posted to C006".
None can pass in a run where its creating criterion failed. **Clean, and this is the rule 17 shape that bit
Task 44.**

## Lens 7 - Anti-rationalization

Re-scanned my own reasoning for talked-myself-out-of lines. Two survived and are promoted to findings
rather than dismissed: F2 (I first reasoned "a judge will probably read the title's 'one' as binding") and
F3 (I first reasoned "the criterion claim is scoped so the justification error is harmless"). Both are
logged below. No other suppressed finding.

## Lens 8 - Regression anchors

`check_regression` PASS at 62/62 anchors, re-confirmed green this pass by the operator's gate run.

## Lens 6 / Lens 9

Retired in v18. Not executed.

---

# FINDINGS

## F1 - [BLOCKER, verdict driver] Two predicted all-failing criteria, tripping the Eval's 2+ AF hard gate

Criteria **4** (retire one of the duplicated Harris reviews) and **34** (report that two Harris reviews
stand) both depend on a single retrieval: discovering the June 3 "(Rescheduled)" event.

I re-derived this rather than inheriting Council B's claim, and found stronger evidence than Council B had.
I swept **all five non-calendar services** for any on-persona pointer to a rescheduled Harris review, a
June 3 date, or a double-booking: Slack messages, Linear issues, Linear comments, Gmail messages, HubSpot
objects. **Zero hits.** Lisa's own calendar carries exactly one Harris event, on June 2, `status:
confirmed`, described benignly as a "Casual 45-minute morning call". The duplicate exists only as
per-calendar rows on aurora.winona, brooke.phillips, patricia.nguyen and teresa.wood, and Lisa is not an
attendee.

The prompt's trigger is conditional: "Do the same for their review meetings **if either of those** did not
end up properly settled." An agent that finds the Finley review plainly unsettled (declined by Lisa, six
weeks past, no June replacement) has satisfied the "either" reading and has no prompt-driven reason to keep
digging on Harris, whose single visible event affirmatively reads settled. The task therefore gives the
agent a positive reason to believe there is nothing more to find.

Both criteria are grounded, gradable, and reachable with the available tools, so they are **Bucket 3
defensible, not Bucket 1 invalid**. But the Eval's pre-submission gate counts criteria, not discoveries,
and 2 predicted AF is an automatic fail. **Council B's prediction is confirmed on independent evidence.**

**Confirming the fix to the third prediction.** Council B's third AF was old-numbering criterion 14
(collections), which it classified as the only Bucket 1 of the three because its evidence read "FAIL if the
draft asserts a different collections percentage of its own", forbidding a correct derived answer. I
verified the premise independently: a collections ratio **is** computable from the invoice records, and it
comes to **49.63%** by amount (150,329.19 billed, 75,717.25 outstanding) or 48.39% by count, and 18.9% for
these two owners. So the defect was real. Current criterion 14 now reads "A collections figure the agent
derives from the invoice records is acceptable and must not be failed, provided the draft does not present
the 97% itself as supported." **The fix is correct and the Bucket 1 candidate is removed.** The 97%
refutation itself stands: no record states a collections rate, and 49.63% is nowhere near 97%.

**Fix (in-phase, minimum to clear the gate):** cut criterion **34**, keep criterion **4**.
Rationale: 4 is the prompt-mandated act ("put those records right ... Do the same for their review
meetings"); 34 is a 2.1 restatement of the same discovery and adds no discrimination beyond it, which is a
rule 28 weak-assertion trim. This takes predicted AF from 2 to 1 and clears the gate.
Rule 14 is satisfied: L10 retains carrier 4 on the Harris instance and carrier 35 on the OPS-10 instance,
so no lever loses all carriers. Budget goes 35 to 34, far under the 60 ceiling.

**Alternative root-cause fix, if the operator prefers to keep both carriers - PROPAGATE TO S0/injection:**
V4 permits injection (AGENTS.md rule 4). Injecting one on-persona pointer, for example a Slack line in C006
or a comment on OPS-10 noting the Harris call was moved, converts both criteria from unmotivated-sweep to
fair-hard without stating the answer. This requires `validate.py --phase injection` to re-clear its 7 hard
gates plus difficulty >= 3.5, so it is a larger change than the cut and is out of scope for S3 to apply
unilaterally.

## F2 - [MODERATE] Criterion 21 pins its cardinality only in an editorial aside, with no FAIL clause

Criterion 21 title says "opens **one** new tracking issue". Its evidence says "Either target is correct;
the target is an accept-set but the count is not." That sentence is a meta-statement about the criterion's
design, not a gradeable instruction. The evidence's actual FAIL clauses are only: no issue created, and the
issue duplicates already-tracked work. **Neither fails a run that creates two issues.**

OE 35 states "Exactly one issue is expected, matching the prompt's 'a separate item'." So a judge grading
against the OE fails a two-issue run and a judge grading against criterion 21's FAIL clauses passes it.
That is grader-dependent behaviour on identical trajectories, which is the rule 29 wording-defect shape, and
the misgrade direction is Overly Specific, which rule 27 makes MODERATE.

This is also the one Handoff obligation that is only partly met. Obligation 6b says "S3 must pin the
expected count explicitly rather than leaving it open" and "Do not write a criterion that passes on 'one or
more items'." As written, criterion 21 does pass on one or more.

**Fix:** append to criterion 21's evidence, after the existing FAIL clauses:
`FAIL if more than one new tracking issue is created, because the prompt asks for a separate item and only one is expected.`
If the operator instead judges that raising both genuinely-unresolved items should pass (defensible, since
both the 310C subfloor assessment and the 309C utility transfer are carried nowhere else), then bless it
explicitly with `Creating one issue for each of the two items also passes.` and mirror that into OE 35,
which currently says the opposite. Either resolution is acceptable; leaving it ambiguous is not.

## F3 - [MINOR] Criteria 13 and 27 justifications assert an exhaustiveness the universe contradicts

Criterion 13's justification: "The 94% figure appears **only** in Lisa Smith's own Slack reply about the
Mesa Vista portfolio and in a Linear comment repeating it back."
Criterion 27's evidence: "FAIL if it supplies a different occupancy percentage, because **no such figure
exists in the data** to report."

A 94% occupancy figure does exist elsewhere in the universe. HubSpot carries: "Occupancy across the
**Oakfield Commons** units held at 94% through the week". The criteria's graded CLAIMS survive intact,
because both are scoped to "either portfolio" and Oakfield Commons is neither, so no grading behaviour
changes and this is not Overly Specific. But two justification sentences state a universal that is false as
written, and under the strictest reading a false statement in a justification is a defect. It also creates a
real risk that a grader who finds the Oakfield line concludes the criterion is wrong.

Separately, this is a genuinely good near-miss decoy and is worth keeping.

**Fix:** in criterion 13's justification replace "appears only in" with "appears for either of these two
portfolios only in". In criterion 27's evidence replace "because no such figure exists in the data to
report" with "because no record carries an occupancy figure for either of these portfolios; a 94% figure
elsewhere in the universe belongs to an unrelated property and does not support the claim."

## F4 - [MINOR, PROPAGATE TO S2] OE 34's decompose directive is short of its own prose

The S3 edits to the OE decompose directives are otherwise faithful mirrors and change no OE's meaning:

- **OE 33, 10 elements to 12.** The two added elements are "Harris unapplied credits" and "Finley unapplied
  credits", both of which were already present in OE 33's prose ("$1,975.00 of credit memos that are
  unapplied on the same terms as Finley's", "$3,655.00 of credit memos that are unapplied"). This is a
  decomposition refinement, not a meaning change. 12 elements map 1:1 onto criteria 6 to 17. **Faithful.**
- **OE 36, 4 elements to 5.** The added element is "the Harris position stated", which is the Council B M4
  fix and maps to criterion 26. **Faithful.**
- **OE 34, none to 2.** The added directive is "(both owners named, the hand-off to Brooke stated)", mapping
  to criteria 19 and 20. Faithful as far as it goes, **but OE 34's prose names four things the comment
  covers**: both owners, the make-ready corrections, the calendar resolution, and the hand-off to Brooke.
  Two of those have no directive element and no criterion.

This is the identical shape Council B logged as M4 against OE 36 and which was fixed there. It now sits
unfixed on OE 34. The budget case for NOT adding two more criteria to a single Linear comment (already
carrying three) is sound under rule 28, so the correct fix is to align the prose, not to add criteria.

**Fix:** in OE 34, change "The comment covers both owners, the corrections made to the make-ready records,
the calendar resolution, and the fact that the hand-off has gone to Brooke." to "The comment covers both
owners and the fact that the hand-off has gone to Brooke, and may also describe the make-ready and calendar
corrections, which are not graded here."

## F5 - [MINOR, PROPAGATE TO S2] OE 36 prose still names an ungraded content element

OE 36's prose lists five post contents: two owners named, Harris turn position, Finley past-due position,
the one item still open, **and the fact that the hand-off has gone to Brooke**. Its 5-element directive
substitutes "post lands in C006" (a delivery target, not a content element) for the hand-off element, which
therefore remains ungraded. Criterion 20 already grades the hand-off statement on the OPS-10 comment, so
grading it again on Slack would be low-signal.

**Fix:** drop "and the fact that the hand-off has gone to Brooke" from OE 36's prose.

## F6 - [MODERATE, work product] `v4_gates._derived_from_amounts` rejects the exemplar it cites

The F4 repair is directionally right and is a real improvement: requiring the rubric to SHOW its arithmetic,
with every component independently present in the universe, is both tighter than searching the universe
amount pool and is what a reviewer actually wants. I confirmed the tightening empirically: a fabricated
target against real components returns "" (no false accept).

**But the implementation handles only addition, and its own docstring justifies its existence with a
subtraction.** The docstring cites the rubric guidelines' worked example, "$264 overcharge, the difference
between the $792 Stripe charge and the $528 closing disclosure amount", and notes that a flat membership
test "marks the guidelines' own exemplar BROKEN". The replacement filters candidate components with
`0 < d < t_val`, which discards every component larger than the target, then tests only sums of 2 to 4
terms. For the $264 case both components (792, 528) exceed the target and are discarded.

Measured, not asserted:

```
_derived_from_amounts("264.00", {"792.00","528.00","264.00"}, "<the guidelines' own sentence>")  ->  ''   REJECTED
_derived_from_amounts("1500.00", {"5000.00","3500.00"}, "budgeted $5,000.00 against actual $3,500.00") -> '' REJECTED
_derived_from_amounts("10980.00", ...)  -> '390.00 + 2190.00 + 8400.00'   ACCEPTED
```

So the replacement reproduces the exact failure it was written to remove, for any variance, overcharge,
shortfall or net. It is **latent on this task**: all three aggregates here ($10,980.00, $1,975.00,
$3,655.00) are additive and all three are accepted, which is why `--phase submission_gate` is clean. It will
false-BROKEN the next task that grades a difference.

**Fix:** build `comps` without the `d < t_val` upper filter (keep `d > 0` and `d != t_val`), then add a
pairwise difference test `abs(comps[i] - comps[j]) == t_val` alongside the existing sum tests. Keep the
pool-membership requirement, which is the part doing the real work.
**Also remove the dead block** in the same function:
```
if comps[i] * 2 > t_val and comps[i] != t_val:
    pass
```
It is a no-op left in the loop.

**Scope note on the other repairs.** (a) `check_oe_rubric_sync.py` case-sensitivity: correct, and the gate
now reports every decompose element carried, which I independently confirmed against OE 33's 12 elements.
(b) `check_qc_binary.py` sentence-initial and month-name proper-noun false positives: correct, and it
matters because Prompt/Coherence is BINARY with no 3/4 band (rule 26), so a false positive there was an
outright FAIL on four load-bearing sentences. (c) The brief describes three repairs, but `v4_gates.py`
carries **two** changes: `_derived_from_amounts` (F4) and a new `_FUTURE_ACK_RE` that downgrades
future-as-future from FAIL to a council note. The F2 change is defensible on its own terms, since
Evals_starpm/5 Phase 2 defines the F2 defect as future-AS-PAST and acknowledging a grounded future event as
still pending is the spec-correct opposite, but it was outside the stated scope and should be recorded as a
fourth repair rather than travelling unlogged.

---

# Judgement on the m5 decline (requested)

Council B m5 recommended cutting the criterion "The Agent reports Robert Finley's open receivable as
$10,980.00" (old numbering 29, **current 31**) as the third grading of that figure, after the draft (10)
and the Slack post (24).

The decline was made on this ground: the prompt's paragraph 2 is a direct tell-me, and cutting the criterion
"would leave that ask with no final-response carrier."

**The conclusion is correct. The stated reasoning is wrong, and must not stand in the record.**

The reasoning is wrong on a fact checkable against the artifact, which is precisely the rule 19 standard.
Cutting 31 would NOT leave the money ask with no final-response carrier: criterion **32** (credit memos on
both owners unapplied) and criterion **33** (Harris carries no open receivable) are both final-response
money criteria and both survive. The decline asserted a property of the artifact that the artifact
contradicts.

The conclusion nonetheless holds, on two grounds re-read from the artifacts rather than from precedent:

1. **This is not Phase 3.3 overlap.** Criteria 10, 24 and 31 grade three DIFFERENT artifacts: the Gmail
   draft body, the C006 message text, and the final response. Each of the first two is independently
   mandated by its own prompt sentence ("Put an email together for Brooke ... with the specifics in it" and
   "Post a short version in the owner relations channel"). Phase 3.3 targets two criteria grading the same
   artifact. Grading one fact across three separately mandated artifacts is ordinary 1.2/1.2/2.1 practice.
2. **Cutting 31 specifically trips the Eval's Gap 3 hard gate.** "Enumerate every fact the prompt asks the
   agent to report to the user; verify each has a 2.1 Outcome rubric; missing = Major." Finley's $10,980.00
   past-due is the single most material fact under "anything on the money side either of them is likely to
   raise with me". Criteria 32 and 33 cover the credit-memo semantics and the Harris position; neither
   carries the Finley figure. Cutting 31 leaves that specific fact with no 2.1 carrier.

Council B's real concern, that one arithmetic slip costs three criteria, is a **weighting** objection, not a
validity objection, and the remedy for weighting is not to delete a prompt-mandated carrier. I note the
weighting is now less lopsided than when m5 was written: at 35 criteria the triple costs 8.6%, and the
Council B M5 fix added criterion 35, which increased L10's carriage independently.

**Verdict on the decline: UPHELD, reasoning corrected.** No artifact change required for this item.

---

# Severity census

Stated as a claim, not a measurement (rule 18): this is my own count of my own findings and cannot see my
own blind spot. Where the shape was mechanically detectable I cited a checker instead.

Denominator 35. Moderate 1 (F2). Minor 2 (F3, plus F4/F5 which are OE-side and do not count against the
rubric denominator). Major 0. Rubric-side issue rate 3 of 35 = 8.6%, under every percentage band. The
binding failure is not the census: it is F1 against the Eval's absolute 2+ AF gate, and F2 against the
zero-Moderate requirement for Overall Rubric Quality Pass(5).

`check_council_yield.py` on this task's report set: 232 findings raised, 76 declined (33%), 3.56 findings per
10 KB. Two prior reports are flagged as rule 20 defects and are worth the operator's attention:
`AUDIT_oe_r7.md` records **zero** findings across 15.2 KB, and two S2 grounding rounds are DECLINE-HEAVY.

Operator-discipline gates: `_aux/Todos_s3.md` 48 lines with per-step status, `_aux/Reads_s3.md` 26 lines with
per-document confirmations naming the specific rules relied on. Both substantive. **v11 E1/E2 satisfied.**

---

# VERDICT: REVISE

Three items must be applied. F1 is the binding one.

1. **F1 [BLOCKER]** - `7_Rubrics.json`, criterion 34 ("The Agent identifies two live Harry Harris mid-year
   review meetings standing on the calendar, one on June 2 and one on June 3, 2026"): **delete it.** Keep
   criterion 4. This takes predicted all-failing criteria from 2 to 1 and clears the Eval's 2+ gate. L10
   retains carriers 4 and 35, so rule 14 is not violated. Set goes to 34 criteria.
   Then re-run `check_oe_rubric_sync.py`, and mirror the cut into **OE 31**, whose directive currently reads
   "(the duplicated Harris review no longer stands as two live meetings, the Finley review is rescheduled or
   replaced)" and remains correct as-is because criterion 4 still carries the first element. No OE 31 edit is
   needed, but the sync gate must be re-run to confirm.
   If the operator prefers to keep both carriers, take the injection route instead and tag it
   **PROPAGATE TO S0/injection**; that path requires `validate.py --phase injection` to re-clear.

2. **F2 [MODERATE]** - `7_Rubrics.json`, criterion 21 evidence: append
   `FAIL if more than one new tracking issue is created, because the prompt asks for a separate item and only one is expected.`
   (or take the bless-two variant and mirror it into OE 35, as set out in F2).

3. **F6 [MODERATE, work product]** - `Validators/v4_gates.py`, `_derived_from_amounts`: drop the
   `d < t_val` component filter, add the pairwise difference test, delete the `if ...: pass` dead block.
   Re-run `check_regression` (62 anchors) and `validate.py --phase submission_gate` on this task to confirm
   the three additive aggregates still accept.

Optional, no grading behaviour changes, apply if cheap:

4. **F3 [MINOR]** - criteria 13 and 27 justification/evidence rewording as specified.
5. **F4 [MINOR, PROPAGATE TO S2]** - OE 34 prose alignment.
6. **F5 [MINOR, PROPAGATE TO S2]** - OE 36 prose, drop the ungraded hand-off element.

Not required: the m5 decline stands, with its reasoning corrected in this report.

Density clears the correct V4 bar (midpoint 49.5 against 40+) and is noted as coupled to F1.
All five hardness levers trace end-to-end. No answer leakage. No universe atom failed.
