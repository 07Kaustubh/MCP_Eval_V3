# S4 AF Justifications (POST-FIX, 2026-07-22) — Tasks/38_6a5edd95a6946f6c4d160b5a

3 AF rubrics remain post-fix (down from 7). All classified Bucket 3 (Legitimate Model Failure). 5-point checklist confirmed YES on all 5 before each justification was written.

The 4 previously-AF Tanya-cluster rubrics (R13, R15, R20, R21) were reclassified out of the AF bucket after the 2026-07-22 QC fix rewrote them to match universe reality (see S4_verdict.md "Post-Fix Change Summary"). Justifications for those rubrics are removed from this file.

---

## Linear issue: $640 Robert Finley payment (transaction 972286822645) does not reduce the $8,400 Ridgeview roof AR balance

**5-point checklist:**
1. Self-contained, atomic, grounded in universe: YES. QB payment record 972286822645 ($640, TxnDate 2026-05-29, CustomerRef Robert Finley) is applied via LinkedTxn to invoice DocNumber 5848 (Elmwood vacancy report, Balance $0 confirming paid), not to the Ridgeview roof AR (invoice 2026-494, Balance $8,400).
2. Flexible enough to allow valid alternative approaches: YES. The criterion does not prescribe a specific tool path or document citation; it requires only that the Linear issue clarify the payment went elsewhere.
3. Required by prompt: YES. The prompt asks Denise to "figure out what the real owner exposure is," which requires tracing whether any payment has been received against the roof AR.
4. Uses real tool names and valid parameters: YES. Linear issue creation via save_issue is the valid write path.
5. Could a capable agent realistically pass: YES. Querying the QB payment record after confirming the AR balance would surface the DocNumber 5848 application.

**Classification: Bucket 3 — Legitimate Model Failure**

**Trajectory citation:** All 12 runs (Opus Run 1-6, Gemini Run 1-6): agent did not query QB payment transaction 972286822645 in the Linear issue creation call. Agents completed the reconciliation through the two vendor bills and the AR invoice but stopped at confirming the $8,400 outstanding balance. No run performed the additional payment record lookup that would reveal application to DocNumber 5848.

**AF Justification:** The $640 Robert Finley payment (transaction 972286822645) is the only cash transaction against the Ridgeview property owner account. All 12 runs traced the multi-hop QuickBooks chain through bills 2026-481 and PD-2026-084 and the $8,400 AR invoice but stopped before querying the payment record itself. Every run either reported the AR balance as outstanding without addressing the payment, or did not trace the payment to its actual application target (invoice DocNumber 5848, a separate Elmwood vacancy report invoice). The reconciliation chain requires one final step that no agent completed: the payment lookup confirming the transaction went to an unrelated invoice and does not affect the roof repair balance.

---

## Final response: Robert Finley's Ridgeview roof owner receivable is outstanding at $8,400

**5-point checklist:**
1. Self-contained, atomic, grounded in universe: YES. The QuickBooks AR record for Robert Finley (invoice 2026-494) shows an $8,400 outstanding balance for the Ridgeview roof repair.
2. Flexible enough: YES. The rubric does not require specific invoice numbers, just the correct outstanding amount with an explicit outstanding qualifier.
3. Required by prompt: YES. The prompt asks "what is the real owner exposure," requiring the outstanding AR status.
4. Uses real tool names: YES. QuickBooks queries via appropriate tools.
5. Could a capable agent realistically pass: YES. A QB AR query against Robert Finley's account would return the outstanding $8,400 balance on invoice 2026-494.

**Classification: Bucket 3 — Legitimate Model Failure**

**Trajectory citation:** Opus Run 1: action not completed (did not finish QB reconciliation). Opus Runs 2-6: final response collapsed vendor cost and owner AR into a single "$8,400 single job" entry without the explicit "outstanding" AR qualifier. Gemini Run 1: final response capture uncertain (extractor limitation). Gemini Runs 2-6: either omitted the AR outstanding distinction or used early-termination patterns that never reached the AR discussion.

**AF Justification:** Every run that completed the QB reconciliation chain reported the net vendor figure as $8,400 for a single Big Bend Restoration job but did not separately state that Robert Finley's owner receivable for that job is currently outstanding at $8,400. Agents treated the net-vs-gross reconciliation as complete once the single-job figure was confirmed and did not issue a separate AR query to surface the outstanding balance as a distinct financial status. Runs with early termination (Gemini G3, G5, G6) never reached the AR discussion. The distinction between "vendor cost $8,400" and "owner AR outstanding $8,400" requires a deliberate second query that no run performed.

---

## Final response: the $640 Robert Finley payment does not reduce the $8,400 Ridgeview roof AR balance

**5-point checklist:**
1. Self-contained, atomic, grounded in universe: YES. QB payment 972286822645 ($640) is applied to invoice DocNumber 5848 (Elmwood vacancy report), not to the roof repair AR (invoice 2026-494).
2. Flexible enough: YES. The rubric allows any phrasing that makes clear the payment went to a separate invoice.
3. Required by prompt: YES. Required to state the "real owner exposure" accurately.
4. Uses real tool names: YES.
5. Could a capable agent realistically pass: YES. Tracing the payment record would surface the DocNumber 5848 application.

**Classification: Bucket 3 — Legitimate Model Failure (cascade from Linear issue payment-tracing gap)**

**Trajectory citation:** All 12 runs: final response did not mention the $640 payment's application to a separate invoice. No run queried QB payment transaction 972286822645 at the Linear issue creation stage, and the same gap appears in the final response.

**AF Justification:** All 12 runs failed to state in the final response that the $640 Robert Finley payment (transaction 972286822645) does not apply to the Ridgeview roof AR. No run traced the payment to invoice DocNumber 5848 in the Linear issue creation, and the final response reflects the same omission. Every agent either did not address the payment at all or mentioned the $8,400 outstanding balance without clarifying whether any payment against it had been received.

---

## Reclassified (no longer AF, no justification required)

The following 4 rubrics were previously classified as Bucket 3 AF but are no longer in the AF bucket after the 2026-07-22 rubric revision. Justifications removed. See S4_verdict.md "Post-Fix Change Summary" for the reclassification reasoning.

- **R13** (Gmail unit reference) — post-fix: 9/12 pass
- **R15** (Gmail eviction status) — post-fix: 9/12 pass
- **R20** (Final unit reference) — post-fix: 6/12 pass
- **R21** (Final eviction status) — post-fix: 4/12 pass
