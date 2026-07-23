# Linter Invalidation Justification — Task 38 (6a5edd95)

**Date:** 2026-07-22  
**Validator status at time of writing:** PASS (0 fails, 3 warns, 5 notes)  
**Rubric set:** 7_Rubrics.json — 22 rubrics, all Outcome, 0 Process

This document records the spec-grounded justification for rejecting four linter atomicity flags raised during post-FINAL rubric review. Each finding was evaluated against `Evals_starpm/3_Rubrics_Eval.md` Phase 2.2 (Atomicity HARD GATE) and the acceptable-bundling decision rules.

---

## Finding 1 — Criterion 5 (id: bcc3858e-719b-48a9-af9e-c27a4be73d96)

**Criterion text:** "The Agent's Slack message to C001 (#maintenance) confirms that maintenance record MT-2026-063 has been updated to reflect the actual status."

**Linter claim:** Bundles two independent verifiable claims — (1) the message confirms the record was updated, and (2) the update reflects the "actual status" (implying correct diagnosis content).

**Ruling: INVALID — false positive.**

**Justification:**

The evidence field is the definitive grading target per the spec: *"It must confirm that maintenance record MT-2026-063 has been updated (or reference the ticket update in equivalent terms)."* The evidence narrows the criterion to ONE testable question: does the Slack message mention the update? The phrase "to reflect the actual status" is a contextual qualifier that characterizes the purpose of the update — it is not a second independently-testable claim about update content.

The spec's atomicity HARD GATE (Phase 2.2) asks: "If this criterion fails, is there exactly ONE clear reason why?" The answer is yes — the Slack message either confirms the record update or it does not. The content correctness of the Airtable update is already graded by rubric[1] ("The Agent's update to maintenance record rec7f6e5d4c3b2a1e reflects compressor failure as the diagnosis"). There is no double-grading here, and "to reflect the actual status" does not introduce a second independent grading dimension.

The spec's acceptable bundling rule applies: "Claims about different fields of the same write action are NOT independent." The qualifier and the confirmation are both about the same Slack message content — one write action, one destination, one assertion.

---

## Finding 2 — Criterion 9 (id: aca0beaa-3cac-4778-bbfd-7aa23232af72)

**Criterion text:** "The Agent's Linear issue states that the $640 Robert Finley payment (transaction 972286822645) does not reduce the $8,400 Ridgeview roof AR balance."

**Linter claim:** Bundles two independent facts — (1) the payment amount and transaction ID, and (2) the non-application to the AR balance.

**Ruling: INVALID — misreads identifier as independent claim.**

**Justification:**

The $640 amount and transaction ID 972286822645 are **identifying qualifiers required for self-containment**, not independent verifiable claims. The spec's Phase 2.1 (Self-Contained Check) explicitly requires that criteria embed specific values so the judge can evaluate the criterion without universe access. Removing these identifiers would produce: "The Agent's Linear issue states that the payment does not reduce the Ridgeview roof AR balance" — which fails self-containment because no specific payment is identified.

There is exactly ONE testable assertion: does the Linear issue state that this specific, identified payment does not reduce the $8,400 roof AR balance? The identifiers (amount, transaction ID) are the specificity mechanism required by the spec, not second independent claims. Treating identifiers as independent claims would make every self-contained criterion non-atomic by construction — a reductio ad absurdum that the spec does not support.

Per Phase 2.2 decision rule: "Claims from the same tool output / same record are NOT independent." The $640 amount and the non-application conclusion both come from the same QB payment record (972286822645). Same record = acceptable bundling.

---

## Finding 3 — Criteria 14 and 15 (ids: 362bef6d and 1177a4b5)

**Criterion 14 text:** "The Agent's Gmail draft to aurora.winona@starpm.com mentions Tanya Mitchell's emotional support animal reasonable accommodation request."

**Criterion 15 text:** "The Agent's Gmail draft to aurora.winona@starpm.com mentions that Tanya Mitchell's payment plan is active through the end of July."

**Linter claim:** These test independent facts about different aspects of Tanya Mitchell's status in the same email and should be separate criteria.

**Ruling: INVALID — linter misidentifies correctly-split rubrics as a bundling violation.**

**Justification:**

Criteria 14 and 15 are **already two separate rubrics**. Each tests exactly one atomic claim:
- Criterion 14: does the Gmail draft mention the ESA reasonable accommodation request? (one yes/no)
- Criterion 15: does the Gmail draft mention the July payment plan? (one yes/no)

The linter's finding is logically incoherent: it flags two SEPARATELY-WRITTEN criteria as non-atomic, but non-atomicity is a property of a SINGLE criterion that bundles multiple claims. Two already-separate criteria that independently test independent facts is the definition of correct atomicity. The solution the linter implicitly demands (separating them) is what has already been done.

Per the spec's acceptable bundling note (07/16 update): "Email content when the same email goes to multiple people — deficiencies in exploration/approach reflect in all copies, so content criteria pass/fail together." This note addresses bundled MULTI-RECIPIENT sends; it does not affect multi-criterion coverage of a single email's content. Multiple rubrics each testing one content element of the same Gmail draft is the correct V3 pattern.

The ESA request and payment plan are independent hardness-lever discriminating facts (L6 / L1 stump predictions). Keeping them as separate criteria allows the judge to score partial credit (agent surfaces one but not the other), which is precisely the design intent.

---

## Summary

| Finding | Criterion | Linter Claim | Ruling | Spec Basis |
|---------|-----------|--------------|--------|------------|
| 1 | Criterion 5 (bcc3858e) | Bundles update confirmation + content correctness | INVALID | Evidence field disambiguates; qualifier, not independent claim; one write action |
| 2 | Criterion 9 (aca0beaa) | Bundles payment ID + non-application | INVALID | Identifiers are self-containment requirements, not independent claims; same QB record |
| 3 | Criterion 14 (362bef6d) | Should be separate from criterion 15 | INVALID | Already a separate rubric; one claim, atomic |
| 4 | Criterion 15 (1177a4b5) | Should be separate from criterion 14 | INVALID | Already a separate rubric; one claim, atomic |

**No rubric edits required.** Validator passes 0 fails. All four linter signals are false positives arising from over-granular application of the atomicity rule to (a) contextual qualifiers, (b) self-containment identifiers, and (c) already-separated criterion pairs.
