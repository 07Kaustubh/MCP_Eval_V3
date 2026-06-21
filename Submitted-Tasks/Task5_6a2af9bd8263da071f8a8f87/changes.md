# Changes Log — Task 5_6a2af9bd8263da071f8a8f87 (Northstar IOLTA Trust Shortfall)

> **Owner:** QC review + remediation
> **Goal:** Bring task to 5/5 across all QC Spec Doc dimensions.
> **Today's date in universe:** 2026-06-12 (US/Eastern)

---

## Task Snapshot (Pre-Change)

| Field | Value |
|---|---|
| Acting Persona | Daniel Jones (Accounts Manager) |
| Business Function | Cat 7 — BlackLine Close-Discipline & Variance (Reconciliation Variance Triage) |
| Entities Touched | `northstar_legal` (primary) |
| Services Required | BlackLine, Oracle GL, Records Vault, Email, Slack, Reminder, Contacts (7+) |
| Write Actions | (1) Memo upload to Records Vault, (2) Notification email to Matthew Li + Elita Moore |
| Ground Truth | $6,250 IOLTA shortfall traced to JE-northstar_legal-FP-2026-05-0061 (Hartmann v. Sterling), debited 101000 instead of 250000 |

---

## QC Audit Findings (Initial)

### Dimension 1 — Prompt: **5 PASS**
All 12 sub-dimensions clean. Natural manager voice (Daniel Jones), cross-service investigation, no tool mentions, no contrived constraints, no pre-solving.

### Dimension 2 — Universe: **5 PASS** *(pending Sandbox spot-check)*
Data referenced in OEs is internally coherent — BL recon, JE lines, GL balances, email/Slack red-herrings, reminder all align.

### Dimension 3 — Oracle Events: **5 PASS**
11 OEs cover the full critical path: discovery → root cause → corroboration → deadline → recipient resolution → 2 write actions. Tools, parameters, and expected values match.

### Dimension 4 — Rubric: **5 PASS** *(borderline)*
10 outcome rubrics, all self-contained, atomic, agent-centric, grounded.
- Category Balance: Outcome (10) > Process (0) → PASS.
- Process Rubrics: 0 present. Per spec, "missing process rubric" is *non-fail*, but with no invalid process rubrics, the sub-dimension scores PASS by default (only fails on 2+ invalid Process rubrics).

### Dimension 5 — Trajectory: **❌ FAIL (Too Easy)** ⚠️ **BLOCKER**
| Sub-Dimension | Required | Actual | Status |
|---|---|---|---|
| Tool Call Count | avg ≥ 15 | *(pending count)* | TBD |
| Agent Failure Rate | pass@1 ≤ 40% (≤2/6 runs pass) | **6/6 runs passed 10/10 criteria = 100% pass@1** | **FAIL** |
| Error Rate | < 3 errored runs | 0 errors | PASS |

**Root cause:** The investigation path is too discoverable. Even with a deceptive preparer note + Slack red-herring, every model in 6 runs found the right JE, traced the misposting, framed the regulatory issue, and produced both the memo + notification cleanly.

---

## Required Changes (To Reach 5/5 Overall)

### Change 1 — Increase task difficulty to reach pass@1 ≤ 40%
**Target:** At most 2 of 6 runs pass all 10 rubrics.

**Levers available (need user direction on which to combine):**

| Lever | What it does | Tradeoff |
|---|---|---|
| A. Noise JEs in the same period | Add 2–3 additional plausible-looking trust JEs that aren't the root cause; agent must distinguish | Doesn't change rubric set; pure universe edit |
| B. Multiple variance contributors | Make the headline -$6,250 the *net* of two offsetting issues (e.g., -$8,250 misposting + $2,000 legitimate timing), so naive agents report wrong figure | Changes ground truth; requires rubric tweaks |
| C. Competing red-herring (different matter) | Add a second matter (e.g., "Calloway estate distribution") that *also* looks suspicious but is actually a timing item — agent must rule it out | Pure universe edit; raises false-positive risk |
| D. Tighten rubrics to catch shallow work | Require specific elements: explicit reversal JE (DR 250000 / CR 101000), naming of `250000` account in memo, citation of three-way reconciliation framework | Easy to add; targets sloppy memos |
| E. Add a 3-way recon requirement | Require agent to also reconcile against the matter-ledger sub-ledger (individual client trust balances), not just GL 105000 vs 250000 | Adds genuine accounting complexity |
| F. Multi-period pattern check | Add a 2nd similar misposting from FP-2026-04 that hasn't been caught — agent must flag it as a pattern | Adds investigation depth; expands ground truth |

### Change 2 — (Optional defensive) Add one valid Process rubric
Per Process Rubric three-condition test, a candidate that passes:
> *"The Agent independently verifies the trust position by tying GL account 105000 (IOLTA trust cash) against GL account 250000 (IOLTA client-trust liability) for FP-2026-05 before drafting the memo conclusion."*

- (1) Required by every valid path — yes, must do the GL tie-out
- (2) Outcome can't capture — yes, outcome only checks memo conclusion, not whether agent verified independently before writing
- (3) Verification not execution trace — yes, behavior-level

This is a hedge — if the task is on the bubble, this lifts Process Rubrics sub-dimension from "vacuous pass" to "demonstrated pass."

---

## Decision Log

*(append entries here as decisions are made)*

| Date | Decision | Rationale |
|---|---|---|
| 2026-06-11 | Created changes.md; identified Agent Failure Rate as primary blocker | 6/6 verifier runs all passed 10/10 criteria, far exceeding pass@1 ≤ 40% threshold |
| 2026-06-11 | User approved adding 1 Process rubric (defensive hedge) | Lifts Process Rubrics sub-dimension from vacuous-pass to demonstrated-pass; validates against three-condition test |
| 2026-06-11 | User deferred difficulty-lever decision; planning phase first | Want to think through tradeoffs before committing to universe/rubric edits |
| 2026-06-11 | Reviewed 6 agent trajectories (~50 tool calls each); identified universal easy-path | Every Opus 4.6 (low) run found Hartmann via single `oracle_gl_list_journal_entries` + keyword match. Confirmed no rubric tightening alone can drive pass@1 ≤ 40%. |
| 2026-06-11 | Web-searched Opus 4.6 (low) failure modes | Documented: pattern-matches first plausible frame; "local coherence" overrides "distant constraints"; lazy on tool calls; premature stops once plausible answer reached |
| 2026-06-11 | User rejected universe edits; instructed restrategize | Constraint: solve difficulty problem without touching `3_UniverseDataForThisTask.json` |
| 2026-06-11 | Selected prompt+OE+rubric expansion targeting Opus 4.6 (low) "premature stop" failure mode | Trajectory data already shows Opus 4.6 (low) signature — agents complete memo+email then stop, skipping the BlackLine paper-trail step inconsistently (review_note in 4/6, attach_evidence in 3/6, exception in 5/6). Adding an explicit "paper trail on the recon" ask in the prompt converts these into rubricable outcomes. |

---

## Change History

*(append entries when files are modified)*

| Date | File | Change | Status |
|---|---|---|---|
| 2026-06-11 | changes.md | Created tracking file with initial audit | Done |
| 2026-06-11 | 7_Rubrics.json | Added rubric #11 (Process): "Agent independently verifies 105000 vs 250000 balances for May 2026 from the GL rather than relying solely on the BlackLine reconciliation's reported balances." Passes three-condition test (required by every valid path; outcome can't capture; verification, not execution trace). | Done |
| 2026-06-11 | 7_Rubrics.json | Tightened rubric #6 (corrective action). Old wording allowed vague "reclass to client-trust liability"; new wording requires explicit naming of account 101000 (operating cash) AND either 105000 (trust cash, reverses bad JE) OR 250000 (liability, books the real disbursement). Both accounting-valid paths accepted. Closes ambiguity that let Verifier Run #3 pass a cash-to-cash narrative that never named the liability. | Done |
| 2026-06-11 | 5_Prompt.txt | Added 1 sentence at end of paragraph 2: "While we figure this out, make sure that reconciliation cannot quietly get certified on the existing note — leave a clear paper trail on the recon itself so anyone walking up to it sees the issue and stops." Natural Daniel Jones voice (managerial, standards-emphasizing). Hint without giving away (goal-named, method-agnostic per Hard_Tips.md). Targets Opus 4.6 (low) "premature stop" failure mode by extending the deliverable beyond memo+email. | Done |
| 2026-06-11 | 6_Oracle_Events.txt | Added OE 7.5 (formally flag the recon via BlackLine review note + exception) and OE 7.6 (attach supporting evidence to the recon) between current OE 7 and OE 8. Maps the BlackLine paper-trail behavior into the critical path so the new outcome rubrics have a grounded OE basis. | Done |
| 2026-06-11 | 6_Oracle_Events.txt | Accuracy fixes to OE 7.5 and OE 7.6 parameter signatures (user QC audit): blackline_create_review_note uses `author` (was `created_by`) and required `body`; blackline_create_exception uses `type` (was `exception_type`), required `description` + `identified_by`, optional `related_reconciliation_id` (was `recon_id`), and removed the fabricated `amount` parameter (amount now belongs in `description` text); blackline_attach_evidence now specifies required `kind` and `document_id` pointing at the existing doc_b94f2a17c8e34d6a or a fresh upload. Rubrics #12/#13/#14 unaffected — they're agent-behavior-centric, not parameter-specific. | Done |
| 2026-06-11 | 7_Rubrics.json | Appended outcome rubric #12 (review note on BL-7C2A9F4E1B83 superseding preparer's note), #13 (exception created on BL-7C2A9F4E1B83 documenting ~$6,250 shortfall), #14 (evidence attached to BL-7C2A9F4E1B83 corroborating finding). Each is self-contained, atomic, agent-centric, grounded in the new prompt sentence. Predicted: 4/6 of the historical Opus 4.6 (low) runs miss at least 1 of these (review_note skipped in runs 1, 3; attach_evidence skipped in runs 1, 2, 3; exception skipped in run 6) → ~33% pass rate. | Done |
| 2026-06-11 | changes.md | Logged all decisions + change history; updated audit table for new outcome and process rubric counts. | Done |
