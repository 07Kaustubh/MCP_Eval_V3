# S3 Council B — Heaviest Adversarial QC Pass

**Task:** 45_6a6525d5201ac850ceb19a36 (StarPM V4) · **Artifact:** `7_Rubrics.json` (18 outcome, 0 process) · **Mode:** READ-ONLY (report only)
**Correct answer under test:** Mesa Vista 4C is NOT marketing-ready → HOLD / kick-back. Current in-progress turn = Airtable `recbd087a4abd605b` (selProg).
**Universe today:** 2026-07-01 America/Chicago.

## Ground truth re-verified from `_aux/Universe_Split/` (nothing taken on trust)

| Fact | Rubric(s) relying on it | Verified value |
|---|---|---|
| Current turn record | R1, R2, R3, R7, R17 | `recbd087a4abd605b` · fldTurnStatus **selProg** · fldMoveOut **2026-06-15** · fldTargetReady **2026-06-30** · created 2026-05-22 |
| Prior-turn decoy | R1/R2 anti-latching | `recc8534b3fd13954` · **selReady** · move-out 2026-06-01 · target 2026-06-14 · created **2026-05-29 (LATER)** → supersession trap confirmed real |
| Deep-clean bill | R5, R15 | `195089456477` Sunshine Cleaning DocNo 2026-SC-4C · Total **387.00** · **Balance 387.00** · due 2026-05-31 (past due, unpaid) |
| Interior-repaint bill | R6, R16 | `696089964235` Permian Make-Ready Crew DocNo PD-2026-09 · Total **1340.00** · **Balance 1340.00** · due 2026-05-31 (past due, unpaid) |
| QC re-inspection | R8, R18 | "Make-Ready QC Inspection - Mesa Vista 4C" **2026-07-15** 10:00 America/Chicago, status confirmed (future) |
| Channel | R9, R10 | C004 = **#make-ready** |
| Recipients | R11/R12, R13 | carlos.mendez@starpm.com (Onsite PM) · brooke.phillips@starpm.com (Supervisor) |
| Board | R4 | Operations team (OPS) |

All 18 rubrics' concrete values are grounded. `validate.py --phase rubrics` = PASS (0 fails, 8 benign grounding-substring warns on 387.00 / 1340.00 / ids — these ARE in the universe, not fabrications).

---

## 1. Sub-dimension scores (each /5)

| Sub-dim | Score | Basis |
|---|---|---|
| **Atomicity** | **4/5** | 17/18 clean. R12 stacks two independently-failable content clauses (held + listing-condition). R2/R7/R17 multi-clause but single-data-point (bundling-exception eligible → not defects). |
| **Self-Containment** | **5/5** | Every expected value embedded in the title (record id, $387, $1,340, 6/30, 7/15, C004/#make-ready, both emails, OPS). Judge needs nothing external. |
| **Completeness** | **4/5** | All 7 prompt asks carried. One soft spot: ask (f) "email Carlos with the specifics" is graded only as held+listing-condition (R11/R12); the concrete outstanding items are graded on ticket (R5-R8) + final response (R15-R18) but not in the email itself. Acceptable, non-blocking (see 2.C). |
| **Flexibility** | **5/5** | R1 update-OR-comment; R13 email-OR-Slack (method-agnostic, matches prompt goal-not-method); amounts/dates correctly EXACT (static structured values, not "approximately"); record bound by content not bare id. No path-locking. |
| **Accuracy** | **5/5** | Every value matches the universe (table above). selProg/6-15/6-30, both balances, 7/15 event, channel, recipients, board all confirmed. |
| **Category Balance** | **5/5** | 18 outcome > 0 process (QC spec Pass-5: outcome > process, 05/22). `check_ordering_coverage.py` confirms no ordering language → 0 process is correct, no ungraded ordering/verification requirement. |
| **Agent-Centric Phrasing** | **5/5** | Every title = "The Agent" + action verb; zero passive; zero tool names in titles (issue tracker / make-ready channel / email / record are user-visible surfaces). |

**QC-spec Overall Rubric Quality cross-check:** 0 Major, 0 Moderate. Criterion-with-issue count = 1 (R12) → 1/18 = 5.6%, marginally over the <5% Pass(5) line for the strict percentage lens (Non-Fail 3/4 band); granting R12 the bundling exception → 0% → Pass(5). The email-specifics item (2.C) is a coverage observation, not a defective criterion, so it does not enter the percentage. The R12 fix is trivial and removes all doubt.

---

## 2. Adversarial findings

### MINOR-1 — R12 stacks two independently-failable clauses (Atomicity)
R12: *"...states that Mesa Vista 4C is being held rather than signed off, **and** that it does not go to listing until the outstanding scopes are closed and signed off."* Clause (a) held/not-signed-off and clause (b) listing-blocked-until-closed can fail independently — an email that states the hold but omits the listing condition fails R12 entirely, losing credit for the hold it did convey. The guidelines' judgment rule ("if two claims could plausibly fail independently, split them", Rule 2 / Mistake 6) points to a split. **Counterweight:** the prompt fuses them with a causal "because" (*"hold it, because it does not go to listing until every outstanding scope is closed and signed off"*), so they are tightly coupled facets of one proposition and in practice pass/fail together — bundling-exception-eligible. Borderline; flagged as MINOR (Overly-Broad-adjacent, not Overly-Specific). **Severity: MINOR.**
*Recommendation:* split into two 1.2 rubrics, or drop clause (b) from R12 (R14 already carries "should not be listed" in the final response) so R12 checks only the literal email ask "held rather than signed off."

### MINOR-2 — Email "with the specifics" only partially graded on its own artifact (Completeness)
Prompt ask (f): *"get an email together for Carlos with the specifics."* R11 grades the email exists; R12 grades held + listing-condition. No rubric requires the **email** to carry the concrete outstanding items ($387 / $1,340 / In-Progress-past-due / 7-15). An agent could send Carlos "4C is held, not to listing until scopes close" with no concrete specifics and still pass R11+R12. **Verdict: acceptable, non-blocking.** The specifics are graded in TWO other artifacts (ticket R5-R8, final response R15-R18), so the agent's ability to produce them is fully tested; forcing the same four items into a fifth artifact would inflate the set and dilute. Carlos is, however, the exact person who claimed in Slack that the bills were "closed out / entered", so the email correcting him is the most natural place for the vendor specifics. **Severity: MINOR.**
*Recommendation (optional polish):* add one 1.2 — *"The Agent's email to Carlos names the deep-clean and interior-repaint bills as still unpaid."* Not required for GO.

### 2.A ADVERSARIAL ALT-PATH — do the exact amounts over-specify? (the load-bearing adjudication)
**Sketch:** a competent agent sweeps QuickBooks, correctly concludes both carrying scopes are billed-but-unpaid, and reports *"the Sunshine Cleaning deep clean and the Permian interior repaint both have bills entered that remain unpaid and past due (due 2026-05-31)"* — naming scope + vendor + unpaid + due-date but **omitting the dollar figures**. R5/R6/R15/R16 fail this trajectory.
**Verdict: the exact amounts are a LEGITIMATE STRICT OUTCOME, not an over-specification.** Reasoning:
- `$387` and `$1,340` are **exact static values pulled from a structured source** (QuickBooks Balance field). The Rubrics Guidelines' own worked Example 1 makes this the textbook case: a precise structured value the agent "cannot fake without doing the underlying work" is *preferred* over a process rubric. Rule 4 correctly keeps them EXACT (not "approximately" — they are not calculated/rounded).
- The prompt explicitly demands the reconciliation that produces them: *"I want the vendor side reconciled too. A scope ... finished with the bill still sitting unpaid, does not count as closed"* and *"spelling out exactly what is still left"* and *"email ... with the specifics."* The unpaid balance IS "exactly what is still left."
- This is the carrier for the L2 structured-DB-skip and L11 net-vs-gross levers: the amount is the proof the agent went past the Slack "bill entered" chatter into QuickBooks. Dropping it would gut the stump.
- The residual alt-path (reconciled-but-omitted-figure) is a genuinely weak path, not a strong one: the balance is the very field the agent just read, and "spell out exactly what is still left / with the specifics" makes naming it the expected behavior. Requiring it does not penalize a competent trajectory — it enforces the reconciliation the prompt ordered.
The rubric evidence already anchors on the figure appearing *with the scope* ("deep-clean scope named with an unpaid / outstanding bill of $387"), so `$387` / `387.00` / "$387 balance" all pass. **No Moderate. No change required.**

### 2.B ATOMICITY stress (R2, R7/R17)
- **R2** (does-not-advance-to-Ready): bundles not-advanced-to-Ready + not-marked-marketing-ready + remains-In-Progress. These are three expressions of ONE observable — `fldTurnStatus != selReady` on `recbd087` (enum is {Scheduled, In Progress, Ready}; there is no "hold" value, correctly why R2 checks "did not advance to Ready" not a hold enum). They pass/fail together → single-data-point bundling exception → **atomic-enough**. The "does not otherwise mark marketing-ready" clause is scoped by the evidence to record updates ("Check every make-ready record update"), so it does not leak into cross-artifact grading. Wrong-pass check: a no-write / comment-only agent passes R2 (correctly — R2 is the negative anti-latching outcome), but fails R1 (must record the determination) and R3 (must state the hold), so "do nothing" earns no free overall pass. Correct decomposition.
- **R7 / R17** (In Progress + 6/30 past due): two facets of the same record's schedule state, single data point, inseparable → acceptable, no severity.

### 2.C FORWARD-COVERAGE — every prompt ask has a rubric
| Prompt ask | Carrier | Covered? |
|---|---|---|
| (a) record QC determination on the turn | R1 (records on recbd087) + R3 (states held) | ✅ |
| (b) give the call / hold plainly | R14 | ✅ |
| (c) not to listing until every scope closed+signed off | R12 (email condition) + R14 (should not be listed) | ✅ |
| (d) open ticket "spelling out exactly what is still left" | R4 + R5-R8 (4 items) | ✅ strong |
| (e) post where it lands in make-ready channel | R9 + R10 | ✅ |
| (f) email Carlos "with the specifics" | R11 + R12 | ⚠️ partial (MINOR-2) |
| (g) notify Brooke before she markets | R13 (method-agnostic) | ✅ |

### 2.D REVERSE-COVERAGE — every rubric maps to a prompt ask (no beyond-prompt rubric)
R1-R3→(a); R4-R8→(d); R9-R10→(e); R11-R12→(f); R13→(g); R14→(b)/(c). **R15-R18** (final response enumerates the 4 items) map to the prompt's first-paragraph direct-report asks: *"I need to know whether both are genuinely closed and signed off or still open, and I want the vendor side reconciled too"* (→ R15/R16 unpaid bills, R17 In-Progress) and *"a re-inspection ... factors into whether I can call this one done"* (→ R18). These are legitimate 2.1 key-fact rubrics, **not** beyond-prompt. No rubric exceeds the prompt.

### 2.E DILUTION — is the 2-artifact / 5-surface grading redundant or reward-diluting?
**Not diluting — each traces to a distinct explicit deliverable.**
- Each outstanding FACT graded in exactly 2 artifacts: the **ticket** (R5-R8, prompt: "spelling out exactly what is still left") and the **final response** (R15-R18, prompt: "I need to know whether..."). Different deliverables; they fail independently (perfect ticket + vague final response fails R15-R18 while R5-R8 pass). This is one-rubric-per-required-artifact, not filler.
- The DECISION (held) graded on 5 surfaces: Airtable R3 / Slack R10 / email R12 / Brooke R13 / final response R14 — each a distinct communication the prompt names by name. An agent could record the hold in Airtable but sign off in the Slack post; R3 passes while R10 fails. Independent, non-overlapping (no single error trips two). Matches the atomic-per-write-action pattern.

### 2.F PROCESS — 0 process rubrics
Confirmed correct. `check_ordering_coverage.py` independently reproduced: *"no ordering language detected in the prompt"* (0 process, 0 grading order). No ordering constraint, no verification step that an Outcome cannot cover (the reconciliation is captured by the exact-amount outcomes per 2.A). Category Balance binary → PASS.

**Severity census: 0 Major · 0 Moderate · 2 Minor (R12 stack; email-specifics coverage).**

---

## 3. B3 — Tool-call density projection (per model)

Rubric set forces **6 distinct writes** + a **7-service discovery sweep**, consistent with the Hardness Plan's competent trajectory:

| Writes forced by rubrics | Services swept for the reads behind the rubrics |
|---|---|
| Airtable update/comment on recbd087 (R1) · Linear issue (R4) · Linear comment enumerating 4 items (R5-R8) · Slack C004 post (R9) · Gmail draft to Carlos (R11) · Brooke notify (R13) | airtable (2 make-ready rows + 2 maint tickets) · quickbooks (aged payables + 2 open bills) · slack (C004) · gcalendar (7/15) · contacts/hubspot (Carlos, Brooke) · linear · gmail = **7 of 8** |

| Model | Competent projection | Verdict |
|---|---|---|
| Opus 4.8 | ~43-45 | meets StarPM 40+ design target |
| Gemini | ~41-43 | meets StarPM 40+ design target |
| Minimizing sketch | ~21 | THIN band, well above 15 floor |
| Empirical StarPM anchor (L33) | 33-38 | THIN band |

The rubric set aligns with a 40+ competent trajectory and does **not** imply a sub-15 or clearly-sub-40 path. Per the Hardness Plan's S1-AUDIT acceptance, this is **THIN (pre-accepted with per-task justification)**: clears the QC-spec 15 floor with wide margin; the 6-write mix (not collapsed to 3) is preserved exactly as the mandatory downstream mitigation requires. **Not a BLOCK.** (Standing hard S4 gate remains: per-model average < 40 on real runs → PIPELINE REDO.)

---

## 4. B4 — Hardness-lever coverage (carrier rubric per lever)

| Lever | Carrier rubric(s) — value depends on traversing the lever | Status |
|---|---|---|
| **L2 structured-DB skip** | R2 (not-advanced-to-Ready — only knowable from the selProg row, not the "done" chatter/tickets), R7/R17 (In-Progress + 6/30 past due — only in tblMakeReady), R15/R16 (unpaid balances — only in QuickBooks, not the Slack "bill entered" chatter) | ✅ carried |
| **L1/L10 latching / supersession (wrong-row / decoy)** | R1 (determination MUST land on recbd087; evidence fails it if written to the prior selReady turn or a maintenance ticket), R2 (must not flip to Ready — the latching payoff) | ✅ carried |
| **L31 explicit negative directive** | R14 (final response states NOT marketing-ready / held / should NOT be listed — the Gemini-selective negative crux); reinforced by R2/R3/R10/R12/R13 | ✅ carried |
| **L7 multi-write** | R1 + R4 + R5-R8 + R9 + R11 + R13 (6 write carriers across 5 services) | ✅ carried |
| **L9 future-event (7/15) + past-due (6/30)** | R8/R18 (7/15 re-inspection pending) + R7/R17 (6/30 target past due) | ✅ both sub-levers carried |

Every engaged lever has ≥1 Outcome carrier whose pass value depends on actually traversing it. **No lever without a carrier → no Major on lever coverage.**

---

## 5. Prompt / Coherence adjudication

`check_qc_binary.py` flags Prompt/Coherence **FAIL** on: *"Open a ticket on the issue tracker spelling out exactly what is still left on it, post where it lands in the make-ready channel, and get an email together for Carlos with the specifics."* — 24% shared vocabulary (1% under the 0.25 bolt-on threshold) + token "Open" unique.

**Applying the QC spec's ACTUAL bolt-on test** (Fail = "removing a sentence doesn't change the rest"; Pass = "one cohesive situation; stacked asks all tie back to the same purpose"):

- The sentence is **load-bearing**, not removable. It carries **3 of the task's deliverables** (ticket, make-ready post, Carlos email); the following sentence adds a 4th (Brooke). Remove it and the task collapses to "determine + give me the call" — more than half the required actions vanish.
- Every clause is **anaphoric to the QC hold** established earlier: "post where **it** lands," "email ... with **the specifics**," "If I am holding **it** back, Brooke needs to hear **it**." The communications ACT ON the determination — pure causal flow from one situation.
- Contrast the spec's own FAIL example ("Check the weather, update my calendar, email Daniel, pull the IOLTA balance" — four **unrelated** requests). Task 45's clauses are four **related** communications all conveying the **same** hold to the relevant stakeholders — the textbook Pass shape.
- The 24% lexical-overlap metric measures shared vocabulary as a proxy; being 1% under a heuristic threshold with a unique "Open" verb (the only ticket-creation word) does not evidence a bolt-on.

**Verdict: heuristic FALSE-POSITIVE, not a real coherence defect.** Coherence is genuinely PASS. This concurs with S1 AUDIT (Coherence PASS STRICT); the prompt is locked from S1 and Council B does not re-open it. The flag introduces no Major/Moderate on the rubric set and does not affect the rubric verdict.

---

## Verdict rationale

0 Major, 0 Moderate, 2 Minor (R12 clause stack; email-specifics soft coverage). Exact amounts adjudicated as legitimate strict outcomes (structured-source, prompt-demanded reconciliation). All 5 engaged levers carried. Density THIN but pre-accepted, 6 writes preserved, above floor and at the 40+ competent target. Coherence binary flag is a heuristic false-positive. Category Balance and ordering both clean. The two minors are trivial, non-blocking polish for a clean 5/5 before FINAL; neither trips the BLOCK trigger.

COUNCIL B VERDICT: GO
