# PIPELINE AUDIT — Veteran QC Second-Opinion (Strictest Interpretation)

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Phase:** `rubrics` · **Universe:** starpm (V4, Star Property Management)
**Universe today:** 2026-07-01 (America/Chicago) · **Artifact:** `7_Rubrics.json`, 64 criteria, 64 `outcome` / 0 `process`
**Density scheme:** StarPM V4 — midpoint >= 40 PASS · 15-39 THIN · < 15 INSUFFICIENT, applied PER MODEL. The V3-family 50/40 scheme is NOT applied.
**Pass history:** Council A GO (r3) + Council B GO (r3) → **AUDIT round 1: REVISE** (2 Moderate, 2 Minor) → fixes applied → **AUDIT round 2 (this document, confirmation pass): PASS (STRICT)**.

---

## VERDICT SUMMARY

**PASS (STRICT).** All four round-1 findings are closed on the merits, not by rewording. Artifact re-read from disk; all 64 indices unchanged; the four edits verified verbatim. Zero Major, zero Moderate, zero Minor across 64. All five Rubric sub-dimensions score **5**. Zero BLOCKER on answer-leakage, 5/5 levers still traced, density band unchanged at PASS per model, 62/62 regression anchors, validator exit 0. Three coordinator questions adjudicated below — two confirmations and one decline-upheld-with-corrected-reasoning. One non-blocking OE wording note carried forward to FINAL.

---

# ROUND-1 FINDING DISPOSITION

| # | Sev | Finding | Applied fix verified on disk | Status |
|---|---|---|---|---|
| **F1** | MODERATE | idx 61's `FAIL only if` made omission a PASS, nullifying the criterion | evidence now reads `FAIL if the response does not report the electrical panel inspections as recorded finished, and FAIL if it asserts they were never completed.` Regex `FAIL only if` across 64×3 fields → **0 hits**; 13 additive `FAIL if` clauses remain across the set, all correctly additive. | **CLOSED** |
| **F2** | MODERATE | idx 23's accept-set nested idx 51 (`pass(51) ⟹ pass(23)`) | idx 23 evidence now scopes to "the tracking layer" and enumerates exactly two locations, closing with `The supervisor draft is graded separately and does not satisfy this criterion on its own.` Accept-sets are now **disjoint**: idx 23 = {East tracking item, spot-check note}, idx 51 = {draft}. | **CLOSED** |
| **F3** | MINOR | idx 27's "after July 1, 2026" excluded a valid same-day booking | title and evidence both `on or after July 1, 2026`; justification extended with "a slot booked later on the current date is as valid as one booked on a later date". Re-verified: Jaime has **0** calendar events on/after 2026-07-01, so the widened boundary cannot collide with a pre-existing event and the "new event, not an update" property is preserved. | **CLOSED** |
| **F4** | MINOR | idx 61's "South" scoping single-sourced on OPS-186's title | evidence now carries the accommodation verbatim: `a response that attributes the completion to the record titled Electrical panel inspections complete - South Cluster wrap-up without repeating the word South also satisfies this criterion.` Council A's retitle correctly not taken (it would newly *require* the record id). Note the new fail clause drops "South cluster" — this is correct and mutually reinforcing with the accommodation. | **CLOSED** |

**F1 root cause confirmed by the coordinator and consistent with the artifact history:** the `FAIL only if` construction was Council-A-requested one-directional residue from the deleted condensate-drain criterion, carried across without re-derivation when the electrical criterion replaced it. This is the same class as the F2 artifact (a round-2 accommodation surviving a round-3 replacement) — **two independent instances of un-re-derived residue crossing a criterion replacement.** Recorded as a process observation at N7, not a defect in the current set.

---

# LENS 1 — STRICT QC SCORING (re-run on the four changed criteria, re-derived on 64)

## Per-criterion re-score of the changed set

| Idx | Change | Re-check applied | Verdict |
|---|---|---|---|
| **23** | accept-set narrowed to two tracking-layer locations | Nesting broken — accept-sets are disjoint, so all four divergence cases are now reachable in both directions. Matches OE 33's "either location" **verbatim** (OE 33 names the tracking item and the OPS-98 note; it never names the draft). No new self-containment issue: the added term "the tracking layer" is immediately enumerated by the next sentence, so the judge resolves it from the criterion text alone. | **5** |
| **27** | boundary widened to "on or after" | Aligns with the universe's own today (2026-07-01) and with OE 36's permissive clause. Zero collision risk re-verified against Jaime's 10-event calendar. Justification statement is not graded. | **5** |
| **51** | unchanged | Now genuinely independent of idx 23; sole carrier of the prompt's draft-side "who is holding it" ask for East. | **5** |
| **61** | F1 + F4 both applied | Evidence is now internally coherent: one affirmative check, two **additive** fail conditions, one protective clause. The affirmative requirement is enforceable (omission fails), the attribution risk is accommodated, and the North double-tapped-breaker comment is still explicitly non-penalised. Cross-checked against idx 62's shape — both completion carriers now use additive `FAIL if`. | **5** |

**No new defect introduced by any edit.** Re-swept the full set post-edit: 0 duplicate titles · 0 tool names against the 276-name StarPM catalog · 0 em/en dashes · 0 `at least N` · 0 `approximately` · 3 `(or similar)` all on agent-generated free text · 0 blank fields · flat 4-key schema 64/64 · 64/64 titles begin "The Agent" · 64/64 `outcome`.

## Sub-dimension scores (`Docs_starpm/7_QC_Spec_Doc1.json`, Rubric dimension)

| Sub-dimension | R1 | **R2** | Reason |
|---|---|---|---|
| **Overall Rubric Quality** | 4 | **5** | 0 Major / 0 Moderate / 0 Minor across 64. Both Moderates closed structurally (an enforceable fail condition; disjoint accept-sets), both Minors closed by boundary-widening and an accommodation clause. |
| **All-Failing Rubrics** | 5 | **5** | Pre-verifier, N/A → 5. Zero predicted *invalid* all-fail. idx 61 is now genuinely AF-eligible (as it should be) rather than under-strict — the F1 fix moved it from "silence passes" to "silence fails", which is the correct direction. |
| **Rubric Category Balance** | 5 | **5** | 64 Outcome / 0 Process; `#Outcome > #Process`. |
| **Process Rubrics** | 5 | **5** | Zero Process; three-condition test re-applied to all 64 post-edit, no disguised Process criterion. |
| **Agent-Centric Phrasing** | 5 | **5** | 64/64 "The Agent", 0 tool names, 0 passive constructions. |

**Rubric dimension: 5 — PASS.** No sub-dimension below 5.

Adjacent dimensions re-checked and clean: **Universe Feasibility** 5 · **Cross-service Coherence** 5 · **Trajectory Tool Call Count** projected PASS · **OE Accuracy** 5 with one carried Non-Fail wording note (see N6).

## Threshold math on 64 (both % and absolute gates)

```
Total criteria:                            64
Criteria with Major issues:                 0   ->  0.00%   (>10% or >=3 abs = FAIL)   PASS
Criteria with Moderate issues:              0   ->  0.00%
Major + Moderate:                           0   ->  0.00%   (>15% or >=5 abs = FAIL)   PASS
Major + Moderate + Minor:                   0   ->  0.00%   (>20% or >=8 abs = FAIL)   PASS
Criteria with no issues:                   64

PASS(5) gate: "No Major AND no Moderate AND <5% Minor (and absolute Minor < 3)"  ->  SATISFIED  ->  score 5
```
Absolute-count gates do not activate (rubric count 64 > 30) and would not fire regardless (0 < 3, 0 < 5, 0 < 8).

---

# COORDINATOR QUESTIONS — ADJUDICATED

## Q1. Does narrowing idx 23 reintroduce Council B's round-2 Moderate #5 false-fail?

**No. The narrowing as applied is legitimate difficulty. Do NOT narrow further to the tracking item alone.**

Council B's round-2 Moderate #5 objected to a criterion that **pinned a single location** (the owner had to appear inside a Linear comment) while OE 33 permits two paths. The narrowed idx 23 does not pin a single location — it enumerates **both** OE-33 paths and accepts whichever one the agent actually used:

| Agent path | Where the East position lands | idx 23 |
|---|---|---|
| Raises an East tracking item, owner named on it | tracking item | **PASS** |
| Folds East into the OPS-98 note (OE 33's blessed alternative), owner named in the note | spot-check note | **PASS** |
| Records the East position on the tracking side, owner **only** in the draft | — | FAIL (and idx 51 PASS) |

The third row is the only failing path, and it is failing for the right reason. Three grounds:

1. **The prompt attaches the duty to the tracking-side record, not to the email.** *"Anything still open gets its own tracking item raised, **with the person who owns that work named on it**."* That is a separate clause from *"draft an email to Brooke, cluster by cluster, with what is open, **who is holding it**"*. Two prompt clauses, two artifacts, two criteria. An agent that records an open item on the tracking side and leaves the owner off it has missed the first clause.
2. **idx 23 is already more lenient than the prompt, not stricter.** The prompt's literal text names only the tracking item. Accepting the spot-check note at all is a leniency the rubric grants on OE 33's authority (recorded at N3). Requiring the owner on whichever tracking-side record the agent chose is the minimum faithful transposition of the prompt clause inside that leniency — tightening the leniency's *location* set while dropping its *content* requirement would be incoherent.
3. **OE 33 conformance is now exact.** OE 33: *"the S3 criterion must accept **either location** or a correct agent false-fails."* "Either location" = the East tracking item or the OPS-98 note. The draft was never one of OE 33's two locations; it was introduced into idx 23's accept-set in round 2 only as compensation for the deleted draft criterion, and round 3 restored that criterion without reversing the compensation. The narrowing removes the compensation now that the thing it compensated for is back.

**Explicitly rejecting the "tracking item alone" alternative you offered:** that would pin a single location and false-fail every agent that takes OE 33's folded path — i.e. it would re-create Council B's round-2 Moderate #5 exactly. Keep both locations.

**Optional zero-cost polish (clarifying, not changing — not a finding).** If you want the folded path spelled out for the judge rather than inferred, append to idx 23's evidence: *"If the Agent raised an East cluster tracking item, the owner must be named on that item; if it instead recorded the East position only as a note on a spot-check record, naming the owner in that note satisfies this criterion."* This restates the current accept-set without altering it. Take it or leave it; the criterion is gradeable as written.

## Q2. Does OE 36's internal ambiguity warrant a note for FINAL?

**Yes — carried as N6, non-blocking, with an exact one-line fix.** OE 36 contains both *"any future slot resolved from the current date of 2026-07-01"* and *"is dated after 2026-07-01"*. You took the permissive reading, which is correct: it is the reading that matches the universe's own today, matches OE 36's own first clause, and avoids the false-fail. The residual is an OE-internal inconsistency, not a rubric defect — it now has **zero grading impact** because idx 27 is the only criterion that reads on it and idx 27 has been aligned to the permissive branch.

Severity under `Docs_starpm/7_QC_Spec_Doc1.json` OE Accuracy: **`[Non-Fail - Minor OE Inaccuracies]`** ("substantively correct but contain minor imprecisions"). Does not gate this phase and does not gate FINAL.

**Exact fix for FINAL:** in `6_Oracle_Events.txt` OE 36, change the closing clause `is dated after 2026-07-01` → `is dated on or after 2026-07-01`. Tagged `PROPAGATE TO S2` (wording-only).

## Q3. N1 — should the North draft-holder criterion be added?

**Decline upheld. Do not add. But your stated reason is wrong, and the right reason matters because it protects the fix you just made.**

Your reason — *"sourced from cluster-level scope rather than from the flagged units themselves is weaker grounding than the other three holder criteria"* — does not survive comparison. **idx 5 and idx 50 (West holders) are sourced from exactly that kind of cluster-level scope**: OPS-35's description naming Lisa Smith as onsite lead and John Smith as maintenance execution lead for the West cluster, plus Brooke Phillips as assignee. A North accept-set built from OPS-16/17/18 ("Tony Reyes has the North cluster") plus OPS-40's assignee would be the *same grade* of grounding, not weaker. That reason is retired.

**The correct reason is overlap — and it is F2-shaped.** idx 49's accept-set is `{Carlos Mendez, Elias Navarro, Tony Reyes}` and is graded on the draft body. A North holder criterion's grounded accept-set would be `{Tony Reyes, Elias Navarro, Brooke Phillips}` — **two of three names shared, same artifact, same field**. An agent writing "Tony Reyes is holding the North cluster items" in the draft would satisfy both criteria with one act, and an agent omitting a North holder entirely would lose two criteria for one error. That is precisely the nesting/double-penalty defect class F2 just closed at idx 23/51. Adding this criterion would reopen it one criterion over.

Cluster-granularity holder coverage in the draft is already complete — idx 49 (access chain, covering South's open unit and North's access pair), idx 50 (West), idx 51 (East). **Conclusion upheld, reasoning replaced.** Not an overrule.

---

# LENS 2 — ANSWER-LEAKAGE SWEEP (re-affirmed)

Derived answer unchanged: the aggregate determination that Jaime's QC sign-off does not hold and the push is not closeable as of 2026-07-01. The four edits touched only grading instructions inside `7_Rubrics.json`; **no universe body was modified**, so the round-1 sweep stands. Re-affirmed against the full 4.4 MB `Universe_complete_data.json`: 19 conclusion phrasings and near-variants (`sign-off does not hold`, `does not stand`, `not closeable`, `cannot be closed`, `premature`, `never moved to done`, `still shows todo`, `push cannot close`, `retract`, `earlier sign-off`, …) → **0 hits, all**.

Single-call reveal test re-affirmed: the six load-bearing facts remain distributed across Linear `state_id`, Linear comments, Slack top-level posts, Slack thread replies and Calendar agendas. No single call returns the conclusion; the strongest conversational call (`slack_read_channel C001`) returns the loud *opposite* claim.

**LENS 2: CLEAN. 0 BLOCKERS.**

---

# LENS 3 — HARDNESS END-TO-END TRACE (re-verified post-edit)

None of the four edited criteria is a lever carrier, so no carrier was disturbed. Re-confirmed all five against the artifact on disk:

| Lever | Carrier index | Post-edit status |
|---|---|---|
| **2 — Structured-DB skip (Linear `state_id`)** | **54** (+ 15, 21, 26, 34, 45, 58) | Intact — untouched |
| **9 — Authority dismissal, persona-self** | **52** (+ 53; notes at 24/25/26) | Intact — untouched |
| **1 — Latching on the crew's wrap** | **56**, **55** (+ 3/35/47, 4/36, 11/31/41) | Intact — untouched |
| **8 — Multi-link chain off Jaime's field note** | **1** (+ 32, 43, 57) | Intact — untouched |
| **5 — Thread-reply blindness** | **8** (sole carrier; + 11) | Intact — untouched |

Anti-overclaim counterweight (idx 61, 62) is *strengthened* by F1: idx 61 now actually enforces the affirmative completion report it was added for, which is what keeps constraint 7a's "not everything is open" bound load-bearing rather than decorative.

**LENS 3: NO HARDNESS_REGRESSION. 5/5 traced.**

---

# LENS 4 — STRICT DENSITY PROJECTION (re-derived post-edit)

Neither edit changes the required call set. idx 23's narrowing removes no tool call (the East position is already forced by idx 20/21/22, and the owner rides in the same write). idx 27's widening removes no call. idx 61's fix adds no call (OPS-186 is already forced by idx 4 and idx 36).

**Working range 34-66, midpoint 50** — unchanged from round 1, and consistent with Council B's independent 34-63 / midpoint 48 and S2 Council B's Opus 50 / Gemini 42.

**Band (StarPM V4, applied PER MODEL): Opus PASS · Gemini PASS** (midpoint 50 >= 40).

Standing caveat carried, not waived: the minimising floor of 31-34 sits below 40, so a single maximally-efficient run could measure THIN in isolation. S4 run-level watch on the average, not a rubric defect — the set forces 11 write calls and at least 20 reads spanning Linear, Slack threads, Airtable and Calendar.

---

# LENS 5 — ADVERSARIAL VETERAN REVIEW (re-run post-edit)

| Check | Result |
|---|---|
| Implicit-prompt framing preserved across all 3 artifacts | **PASS** — no criterion demands a step the prompt forecloses; idx 52/53 grade the branch the prompt pre-authorises and the ground truth selects |
| Entity-drift seams | **CLEAN** — full names throughout; Tony Reyes / Tommy Reyes discriminated; all 10 persons resolve to `@starpm.com` |
| Silent process rubrics disguised as outcomes (three-condition test on all 64) | **CLEAN** — every criterion is 1.1, 1.2 or 2.1; none grades verification behaviour or an execution trace |
| Tool-name leaks in titles | **CLEAN** — 0 / 276 |
| "at least N" without prompt mandate | **CLEAN** — 0 |
| Single-channel lock-in where the prompt named only a goal | **CLEAN** — idx 29 accepts name or id; C001 uniquely determined (104 push messages vs 0 in C004) |
| "approximately" near IDs / dates / amounts | **CLEAN** — 0 |
| "(or similar)" near values that must be exact | **CLEAN** — 3, all on agent-generated free text |
| Non-atomic enumeration under a completeness predicate | **CLEAN** — idx 54's three ids derive from one `list_issues` output (spec-permitted grouping); idx 20 is one comparison over one record pair |
| Ambiguous single-target records (F7) | **CLEAN** — every write unique by construction; the three note targets are the complete enumeration of Jaime's 3-of-230 assigned records |
| Evidence over/under-specification vs the criterion | **CLEAN** — idx 61's evidence now matches its title in both directions; remaining `FAIL only if` count is 0 |
| Overlapping / nested criteria | **CLEAN** — idx 23 and idx 51 accept-sets disjoint; no other nested pair found on a full re-sweep of the 64 |
| Boundary-value over-specification | **CLEAN** — idx 27 aligned to the universe's own today |
| Em-dashes / subjective terms / passive voice / blank fields / schema drift | **CLEAN** — 0 / 0 / 0 / 0 / flat 4-key 64/64 |

## Four flagged high-risk areas — final adjudication (unchanged from round 1, re-verified)

1. **idx 61 / 62 coherence with 15/21/26/34/45/54** — coherent, and now *more* so. Both grade what a record **states** ("are recorded as finished", "the crew recorded … as complete"); the punishing family grades whether a record **is** in a completed state. Different claims about different objects. The F1 fix removed the one thing that made idx 61 incoherent as a set member: an evidence clause that let it grade nothing.
2. **Patricia Nguyen / idx 61 South attribution** — independently re-verified in round 1 (2 Patricia+cluster co-occurrences, neither naming one; 0 property→cluster mappings; OPS-16/17/18 put South under Elias Navarro). Closed by F4's accommodation, which removes the false-fail exposure without adding the record-id requirement Council A's retitle would have imposed.
3. **idx 23 vs idx 51** — adjudicated in Council A's favour; Council B's rebuttal applied the converse of the spec's redundancy test. Closed by F2. Q1 above confirms the narrowing does not reintroduce Council B's round-2 Moderate #5.
4. **Deleted condensate-drain criterion** — residue sweep `condensate|drain|compressor|recurring|flush` across 64 × 3 fields → **0 hits**, re-run post-edit. No coverage gap: the function transferred to idx 61 (now actually enforceable), idx 62 already carried it for East, and OE 28 leaves the second drain and the compressor as free-routing residuals no criterion may require or penalise.

## Hardness constraints 6, 7, 7a — re-verified across all 64 post-edit

| Constraint | Verification | Result |
|---|---|---|
| **7a** no claim that nothing on the push is closed | idx 54 id-scoped to OPS-87/96/98 with the explicit guard "FAIL if the response … generalises to a claim that no push work is in a completed state"; idx 63 grades closeability not completion; idx 61 and 62 affirmatively grade completed work — **and idx 61's counterweight is now enforceable rather than nominal** | **HOLDS** |
| **6** no rubric on OPS-91 | regex `OPS-91` across 64 × 3 → **0 hits** (`OPS-40` also 0) | **HOLDS** |
| **7** no graded criterion on an absence | every absence-shaped claim is either bounded-enumeration-derived (3 of 230 issues are Jaime's, none names West) or reframed positive with "corroboration but not required" guards; the three protective clauses at idx 12/33/44 forbid requiring an absence assertion | **HOLDS** |

---

# LENS 6 — RETIRED (v18). Not executed.

---

# LENS 7 — ANTI-RATIONALIZATION (re-run on round-1 reasoning + this round's)

Re-scanned round-1's own reasoning and this round's three adjudications for "considered flagging X but decided it's fine" lines. Six candidates. **Zero survive on likelihood arguments.**

**X1 — idx 36 does not name OPS-186.** **HARD EXCLUSION on spec text:** `Docs_starpm/8_QC_Spec_Doc2.md`, Criteria Not Self-Contained, states the judge sees *"all the rubric criteria (**one rubric item can be used as context for another**)"*, and idx 4 names "OPS-186, dated June 17, 2026". Re-affirmed.

**X2 — idx 11/31/41/56 grade the South unit "never serviced" while Elias's wrap two seconds later says "Every unit serviced".** **HARD EXCLUSION on spec text:** Universe > Cross-service Coherence note — *"if there is sufficient supporting evidence to support one piece of information against a contradicting low-supported piece of information, do not count that as a contradiction."* Open side: OPS-43 sits In Progress recording the no-access unit; both C001 thread replies ask Carlos to re-coordinate, the second saying "lock in access **for tomorrow**" (so a wrap posted 2 s later cannot cover it); nothing in 230 issues / 48 comments / 104 C001 messages / 50 Airtable rows records that unit being serviced. Closed side: one aggregate sentence by the same author. Asymmetric, not misaligned. Re-affirmed.

**X3 — the East open item has no 1.1 issue-creation criterion.** Excluded on the Overly Broad **exception** (the accepted alternative is a valid OE-33-blessed path, not an invalid one), not on likelihood. Now load-bearing for the Q1 adjudication and cross-referenced there. Recorded as **N3**.

**X4 — no draft-side holder criterion for the two flagged North HVAC units.** Round 1 rejected Council B's procedural excuse ("would be manufacturing a finding"). This round rejects the coordinator's replacement excuse ("weaker grounding" — false; idx 5/50 use the same cluster-level sourcing). Re-derived a third time on the merits and upheld on **overlap with idx 49** (two of three accept-set names shared, same artifact) — see Q3. Recorded as **N1** with the corrected reasoning.

**X5 (new) — the F2 narrowing could false-fail an agent that folds East into the note and names the holder only in the draft.** **NOT excluded on likelihood.** Excluded on the **prompt's literal text**: *"Anything still open gets its own tracking item raised, with the person who owns that work named on it"* attaches the owner duty to the tracking-side record, and idx 51 separately carries the draft's *"who is holding it"* duty. The accept-set covers **both** OE-33 paths symmetrically, so no agent is forced into a location it did not use. Text-based exclusion, fully written out at Q1.

**X6 (new) — OE 36's internal ambiguity ("any future slot resolved from the current date" vs "dated after 2026-07-01").** **NOT excluded.** Promoted to a carried note with an exact one-line fix and a `PROPAGATE TO S2` tag (**N6**). Recorded rather than suppressed even though its grading impact is now zero.

**Anti-rationalization output check: PASSED.** Every candidate is either excluded on cited spec/prompt text (X1, X2, X3, X5), re-derived on the merits with the invalid reasoning replaced (X4), or promoted and recorded (X6). No line reads "it's the most likely interpretation" or "a QC-passed task does the same".

---

# LENS 8 — REGRESSION ANCHOR VERIFICATION

Both re-executed by this audit **after** the fixes landed:

```
$ python3 Validators/validate.py --phase rubrics --task Tasks/44_6a62ccba8cad60844b8364b9
[PASS] rubrics: 0 fails, 0 warns, 5 notes    (exit 0)

$ python3 Validators/test_regression_anchors.py
Regression anchors: 62 passed, 0 failed out of 62
```

Validator NOTEs (all informational): universe=starpm · Feasible_Surface 15 tables · Fact_Ledger groundedness (403 amounts / 206 emails) · counts `outcome=64 process=0` · 0/64 Major, 0/64 Moderate+, 0/64 any.

Independent post-edit residue sweep by this audit, confirming the coordinator's: `FAIL only if` **0** · `at least` **0** · `approximately` **0** · `condensate|drain|compressor|recurring|flush` **0** · `OPS-91` **0** · `OPS-40` **0** · em/en dash **0** · duplicate titles **0** · tool-name leaks **0/276** · `supervisor draft` **1** (idx 23's new exclusion clause, expected).

**LENS 8: 62/62 PASS.**

---

# LENS 9 — RETIRED (v18). Not executed.

---

# FINDINGS

**None.** All four round-1 findings closed on the merits. No new finding introduced by the edits.

## Non-failing notes carried forward

**N1 — No draft-side holder criterion for the two flagged North HVAC units (idx 43).** Decline **upheld** on overlap with idx 49 (accept-sets share Tony Reyes and Elias Navarro; same artifact, same field), not on grounding strength. Adding it would reopen the F2 defect class. See Q3.

**N2 — idx 36 does not name OPS-186.** Permitted by the spec's explicit cross-criterion context allowance; idx 4 supplies it. Cosmetic parity only.

**N3 — The East open item has no 1.1 issue-creation criterion** (idx 20-23 accept a spot-check note as an alternative surface, looser than the prompt's "its own tracking item"). Retained deliberately: the alternative is an OE-33-blessed valid path, and tightening would false-fail a compliant agent. Now load-bearing for the Q1 adjudication.

**N4 — S4 verifier watch on idx 61 / idx 62.** Both require an affirmative completion report and share a correlated failure mode. Post-F1, idx 61 is genuinely AF-eligible. If **both** return all-fail across runs, the remedy is a prompt-side nudge on "work out what is actually finished", not rubric deletion — neither is invalid on its face.

**N5 — Hardness_Plan body figures.** The S2-appended corrections (37 thread parents not 15; 18 HVAC ticket rows not "20+"; "Oakdale" absent from `tblMaintenanceTickets`; Lisa's ask 7 days after Elias's wrap not 5) were independently re-confirmed in round 1. No rubric depends on any stale body figure.

**N6 (new) — OE 36 internal wording ambiguity.** `6_Oracle_Events.txt` OE 36 says both *"any future slot resolved from the current date of 2026-07-01"* and *"is dated after 2026-07-01"*. Non-blocking (`[Non-Fail - Minor OE Inaccuracies]`), zero grading impact now that idx 27 is aligned to the permissive branch. **Fix for FINAL:** change the closing clause `is dated after 2026-07-01` → `is dated on or after 2026-07-01`. Tagged **`PROPAGATE TO S2`** (wording-only, does not gate this phase or FINAL).

**N7 (new, process) — Residue-across-replacement pattern.** F1 and F2 are two independent instances of the same process failure: an accommodation added in round N (Council A's one-directional drain guard; idx 23's widened accept-set) survived a round-N+1 criterion replacement without being re-derived against the new criterion, and neither council re-read the round-N rationale. Worth a `Tasks/_meta/Learnings.md` entry: **when a criterion is replaced or restored, re-derive every accommodation clause attached to it and to its siblings, and re-read the prior round's iteration log before signing off.**

## Upstream propagation

**One, non-blocking:** `PROPAGATE TO S2` — N6, OE 36 wording only. No `PROPAGATE TO S1`. Nothing gates this phase.

---

## Lens roll-up

| Lens | Status |
|---|---|
| 1 — Strict QC scoring | **PASS** — all five Rubric sub-dims 5/5; 0 Major / 0 Moderate / 0 Minor on 64 |
| 2 — Answer-leakage sweep | **CLEAN — 0 BLOCKERS** |
| 3 — Hardness end-to-end | **PASS — 5/5 levers traced; no carrier disturbed by the edits** |
| 4 — Strict density | **PASS — midpoint 50; Opus PASS / Gemini PASS (StarPM V4 band, per model)** |
| 5 — Adversarial veteran review | **PASS — no finding** |
| 6 — Lifecycle + narrative state | **RETIRED (v18)** |
| 7 — Anti-rationalization | **PASS — 6 candidates, 4 excluded on cited spec/prompt text, 1 re-derived on merits, 1 promoted and recorded** |
| 8 — Regression anchors | **62/62 PASS** (validator exit 0, 0 fails, 0 warns) |
| 9 — Unique ground truth middle-band | **RETIRED (v18)** |

---

PASS (STRICT)
