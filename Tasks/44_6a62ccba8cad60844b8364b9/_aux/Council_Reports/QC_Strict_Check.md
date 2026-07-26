# Strict QC Check: prompt / OE / rubric parity against the 12 live trajectories

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm (V4) · **Date:** 2026-07-26
**Sources:** `3_UniverseDataForThisTask.json` (3,892 rows, queried directly, not via the split) · `Evals_starpm/1,2,3,4,5` · `Docs_starpm/7_QC_Spec_Doc1.json` · `Docs_starpm/8_QC_Spec_Doc2.md` · `8a`/`8b` verifier output in full (12 run blocks, 720 decisions) · all 12 trajectories in full.
**Interpretation rule:** strictest reading. Every "should" read as "must"; 5/5 only.

---

## 0. Fixes implemented this pass

| # | Artifact | Change | Impact on the 12 runs |
|---|---|---|---|
| **F1** | `7_Rubrics.json` idx 48 | Evidence now accepts a first-person self-reference as naming Jaime Salinas (the S4 Bucket 1 fix) | **+1 cell.** Opus run 2 Fail to Pass. Opus per-run 31/**37**/45/27/30/47. pass@1 unchanged at 0/6 both models |
| **F2** | `6_Oracle_Events.txt` OE 5, OE 6 | Removed the false claim that the two load-bearing replies need `slack_read_thread`; both routes named, neither required | 0 cells. No criterion depended on the tool |
| **F3** | `7_Rubrics.json` idx 34 | Evidence resolves the West status statement by the record's own title and states that naming the record or its date is not required | 0 cells. Retires a latent false-fail |
| **F4** | `7_Rubrics.json` idx 22, 23, 24 | Evidence accepts either the issue identifier or the record's internal id as the comment target | 0 cells. Retires a latent false-fail |

Post-fix gates: `--phase all` prompt 0F/1W (adjudicated), oe **0F/0W**, rubrics **0F/0W** · `--phase submission_gate` 0F/2W · `--phase injection` SKIP (comment-only, changelog empty) · `test_regression_anchors.py` **62/62** · `verify_universe_atoms.py` 0 fails, 1 warn (the reconciled 2026-07-15 event). Set stays at **60**.

---

## 1. Universe verification (done against `3_UniverseDataForThisTask.json` directly)

Every tight identifier and every OE count re-derived from the per-task file. **13 of 13 OE numeric claims exact, 0 discrepancies.**

| Claim | OE | Verified value |
|---|---|---|
| OPS-87 Todo · OPS-96 Todo · OPS-98 In Progress | 12/13/14 | exact, states resolved by `state_id` through `linear_workflow_states` |
| OPS-99 In Progress / OPS-108 Backlog, byte-identical titles | 21 | exact |
| OPS-186 Todo, created 2026-06-17, "West Cluster work still underway" | 20 | exact |
| OPS-97 Todo · OPS-56 In Progress · OPS-43 In Progress · OPS-35 In Progress | 17/18/19/20 | exact |
| OPS-40 Done · OPS-91 Done (the overclaim bound) | 15 | exact |
| Exactly 3 issues assigned to Jaime, all "spot-check" | 11 | exact: OPS-87, OPS-96, OPS-98 of 230 |
| Jaime created OPS-224/225/226 (the creator-filter near miss) | 11 | exact |
| 1 Jaime message in C001, 6 in C004 | 1 | exact |
| C001 = #maintenance, 104 messages, 8 channels | 1/2 | exact |
| proj_003 holds 60 issues · 36 Done board-wide | 10/15 | exact |
| "North cluster" returns 10 issues, 7 on titles alone | 16 | exact |
| OPS-16/17/18 are the Summer HVAC scope issues | 21 | exact |
| 50 ticket rows, 18 carry HVAC, 4 fields on the table | 24/25 | exact |
| 0 ticket rows reference a cluster, the push, 20x25, a hose bib or a condensate drain | 25 | exact |
| 156 Gmail threads, 0 mention the push | 27 | exact |
| 48 Linear comments | 18 | exact |
| Jaime has 0 events on/after 2026-07-01; 9 unique confirmed forward events universe-wide, none touches the push | 23 | exact, all 9 enumerated and checked |
| Contact job titles for all 6 named owners + Brooke | 26 | exact |

**Injection:** `9_Universe_inject.sql` carries 0 executable statements and `4_Changelog.json` is `[]`. This is a base-universe task, so Universe Cross-service Coherence is clean by construction and `Evals_starpm/0` correctly skips.

---

## 2. Prompt: strict scoring

| Sub-dimension | Score | Basis |
|---|---|---|
| Unique Ground Truth | **5** | see the hard gate below |
| Feasibility | **5** | 6 services, every ask has both a tool and data; the draft-only Gmail constraint is honoured by asking for a draft |
| Explicit Tool Mention | **5** | 0 tool names, 0 parameter names, 0 internal ids. The channel is named descriptively ("the channel the push has been running in") |
| Clarity & Specificity | **5** | no "I'll [verb]" delegation ambiguity; every imperative is directed at the agent |
| Contrived / Unnatural | **5** | all difficulty is entity/record complexity, no format or timestamp demands |
| Alignment with Today's Date | **5** | "yesterday" resolves to 2026-06-30 = end of June; "as of today" = 2026-07-01; "early May" / "late May" absolute and populated |
| Truthfulness | **5** | every claim verified above. "I logged both cluster spot-checks as passing" is literally true of OPS-87's own title |
| Tool Use & Cross-service | **5** | slack, linear, airtable, gcalendar, gmail, contacts |
| Investigation + Action | **5** | 6 write actions across 5 services, each gated on a cross-service finding |
| Coherence (Bolt-on) | **5** | see the warn adjudication below |
| Persona | **5** | QC Inspector auditing her own sign-off is the in-role centre of gravity |
| Business Function | **5** | Quality Control & Field Services, matches `1_Business_Function.txt` and the persona |

**HARD GATE, UGT end-state divergence.** Enumerated the candidate final universe states under every reading I could construct. No act-vs-defer, no write-A-vs-write-B, no escalate-to-A-vs-B. The one candidate divergence is the scope of "my own spot-check records": two records or three. It resolves as follows and does **not** fail UGT.
- The count is not stated in the prompt; it is **determinable from the data** (exactly 3 issues on the whole 230-issue board carry Jaime as assignee, and all 3 carry "spot-check" in the title). That is a discovery question with one correct answer, not two readings of the prompt.
- "both cluster spot-checks" describes the two **cluster** spot-checks and is separate from "my own spot-check records", which governs the note requirement. OPS-96 is the portfolio filter check, not a cluster check, so the two phrases are consistent.
- **Convergence:** 12 of 12 runs left notes on all three records. Two Opus runs addressed them by internal record id rather than by identifier, which is why a naive identifier scan reads them as 0 of 3; resolved, they are 3 of 3. Unanimous convergence, which the hard gate treats as a strong signal against failing UGT.

**Bolt-on warn adjudicated as a false positive.** The validator flags sentence 1 for sharing no named entity with the rest of the prompt. Remove-sentence test: deleting it leaves the prompt opening on "Brooke started **this** in early May" with no antecedent for "this", and deletes the lapsed-deadline premise that criterion idx 28 grades. The sentence is load-bearing. Not a bolt-on.

**Prompt verdict: PASS (5).**

---

## 3. Oracle Events: parity against what the runs actually did

**38 OEs. 24 read/discovery, 14 write/action, 0 reasoning-only steps.** Every write-action OE maps to at least one 1.1 or 1.2 criterion, with one documented exception (below).

**Finding OE-1 [Accuracy, Non-Fail, FIXED as F2].** OE 5 and OE 6 asserted the two load-bearing replies sit where "a plain channel read may not surface" them and mandated `slack_read_thread`. **Falsified empirically.** `slack_read_channel(channel_id="C001", limit=100)` returns both replies inline as flat top-level messages carrying their own timestamps. Proof: in Opus run 1, which never called `slack_read_thread`, the tool result for `slack_read_channel` contains `Message TS: 1779569323.000012` with Brooke's stock-count text verbatim. Across all 12 runs both reply timestamps are present in context; Opus called `slack_read_thread` **0 times in 6 runs** and Gemini 9 times across 4 runs. The OE described a retrieval barrier that does not exist on this server. Fixed; no rubric depended on it.

**Trajectory parity, per write-action OE:**

| OE | Write action | Runs that performed it | Rubric coverage |
|---|---|---|---|
| 28 | Maintenance ticket | 12/12 | idx 1 (1.1) + idx 2 (1.2) |
| 29 | West QC-gap tracking item | Opus 2/6, Gemini 2/6 | idx 3-6 |
| 30 | Filter run tracking item | 0/12 | idx 7-10 |
| 31 | Tenant access tracking item | Opus 3/6, Gemini 0/6 | idx 11-14 |
| 32 | Plumbing tracking item | 12/12 | idx 15-19 |
| 33 | East QC tracking item | Opus 5/6, Gemini 0/6 | idx 20-21 (content only, see below) |
| 34/35 | 3 notes on the spot-check records | 12/12 | idx 22, 23, 24 (3 atomic) |
| 36 | Calendar slot | 12/12 | idx 25, 26 |
| 37 | Channel post to C001 | 12/12 | idx 27-36 |
| 38 | Draft to Brooke | 12/12 | idx 37-50 |

**Alternative paths the runs took, and whether the OEs bless them:**
- **Flipping a QC record to a completed state.** 4 Opus runs and all 6 Gemini runs moved one or more of OPS-87/96/98 to Done. OE 15 grading note two blesses it explicitly and idx 51's evidence grades on the as-found state. **Blessed.**
- **Routing plumbing to the ticket log instead of the board.** OE 32 blesses either destination and idx 15/16/17 accept both. **Blessed.**
- **Splitting tenant access into two items, or filing the South unit as a ticket.** OE 31 blesses both and idx 11/12/13 accept both. **Blessed.**
- **Folding the East position into the OPS-98 note instead of raising an item.** OE 33 blesses it and idx 20/21 accept either location. **Blessed.**
- **Addressing a comment by internal record id instead of the identifier.** Taken by 2 Opus runs, returned success, and the judge resolved it correctly in every cell. Not previously blessed anywhere. **Fixed as F4.**
- **Editing pre-existing issues** (OPS-35, OPS-43, OPS-44, OPS-66 reassignments and state changes). Taken by several runs, covered by no OE and penalised by no criterion. Correct: they are neither required nor forbidden.

**Documented single deviation from the OE-to-rubric hard gate.** OE 33's write action has 1.2 content criteria (idx 20, 21) but **no 1.1**. This is deliberate and OE 33 states the reason: folding the East position into the OPS-98 note is an accepted alternative, so a 1.1 requiring an issue-creation call would false-fail a correct agent. idx 20/21 both read "the Agent's tracking item for the East cluster, **or** the note left on one of Jaime Salinas's spot-check records. Either location satisfies this criterion." Coverage is intact; the gate's purpose is served by a different mechanism. **Not scored as Missing Criteria.**

**OE verdict: Completeness 5 / Accuracy 5** after F2. Before F2, Accuracy was 4 on the OE-1 finding.

---

## 4. Rubrics: strict scoring

**60 criteria, 60 outcome / 0 process.**

| Sub-dimension | Score | Basis |
|---|---|---|
| Overall Rubric Quality | **5** | 0 Major, 0 Moderate, 0 Minor after the four fixes. Validator: 0/60 with any issue |
| All-Failing Rubrics | **5** | Bucket 1 ratio 1/52 = 1.9% pre-fix, 0/52 post-fix, against a 25% threshold |
| Rubric Category Balance | **5** | 60 Outcome > 0 Process |
| Process Rubrics | **5** | zero Process rubrics, so nothing to invalidate |
| Agent-Centric Phrasing | **5** | all 60 open "The Agent" or "The Agent's"; 0 tool names in any criterion; possessive forms are valid per the 06/09 update |

**Atomicity, full decomposition run on all 60.** Two criteria carry the deterministic F6.1 NOT_ATOMIC soft warn, both council-confirmed as split candidates:

- **idx 20** ("OPS-99 and OPS-108 carry the same title while sitting in two different workflow states") is a **single comparative claim**. A comparison between two records cannot be split without destroying what it grades. Not a violation.
- **idx 51** ("none of OPS-87, OPS-96 and OPS-98 was in a completed state as found") enumerates three records under one predicate. This is the closest call in the set. Kept, for three reasons: it is a **single aggregate determination**, which is the answer the prompt asks for rather than three separate facts; OE 15 deliberately specifies that the state-versus-prose determination "is graded once, at portfolio scope, on Jaime's own three records"; and empirically it manufactures no false fail, because all 10 fail cells across both models are runs that did not report as-found states **at all**, not runs that got two of three. Splitting it would also push the set to 62 against the 60 hard cap.

**Under-strict test, run per criterion in isolation.** No criterion admits a factually wrong response on a plausible path. The 1.1 container criteria (idx 3, 7, 11, 15) accept an item existing without correct content, which is the designed 1.1/1.2 split and is listed as acceptable overlap in the spec, not overly broad.

**Over-specification triage.** All 60 classified. 56 `valid`. Four were `over_specified` and all four are now fixed: idx 48 (first-person accept-set, F1), idx 34 (unresolvable superlative, F3), idx 22/23/24 (identifier-form lock-in, F4). Zero `incorrect_factually`.

**Coverage, forward and reverse.** All 8 prompt deliverables covered. Every user-facing ask has a 2.1: what is finished and what is not (idx 51-59), the closeability verdict (idx 60). Reverse check: every one of the 60 traces to explicit prompt language; no fabricated literal; every embedded value verified in section 1.

**Per-deliverable repetition is required, not redundant.** The same fact is graded on the channel post, the draft and the final response (for example the South no-access unit at idx 29 / 38 / 53). These co-fail in practice, but the spec is explicit that a fact required inside one deliverable is not covered by a criterion on a different deliverable and that this is not to be waved away as duplication. Correct as built.

**Rubric verdict: PASS (5).**

---

## 5. Carry-forward, not fixed

**idx 58 and idx 59 remain judge-fragile.** The "are recorded as finished" / "the crew recorded as complete" framing drew 6 judge errors across the two models. There is no safe fix: dropping the record-hedge would assert as verified fact a completion that lives in a record still sitting in Todo, which is the overclaim the hedge exists to prevent. The evidence fields already grant more latitude than the judge applied. Appeal the cells; do not edit the criteria.

---

## FINAL STRICT VERDICT

| Dimension | Score |
|---|---|
| Prompt (12 sub-dims) | **5** |
| Universe (2 sub-dims) | **5** |
| Oracle Events (2 sub-dims) | **5** |
| Rubrics (5 sub-dims) | **5** |
| Trajectory (T1 density, T2 pass@1, T3 error rate, both models) | **5** |

**PASS (5/5) on every scored sub-dimension.** Lowest dimension: none below 5. Four defects were found and fixed in this pass; one is carried forward as an appeal rather than an edit, with the reason recorded.
