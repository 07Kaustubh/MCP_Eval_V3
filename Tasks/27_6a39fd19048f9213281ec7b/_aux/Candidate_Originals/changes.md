# changes.md — Tasks/27_6a39fd19048f9213281ec7b

Review intake date: 2026-06-23. Triage verdict: **REBUILD** (recommendation: `PIPELINE REDO — Tasks/27_6a39fd19048f9213281ec7b`).

Severity tiers follow Docs/7_QC_Spec_Doc1.json + Docs/8_QC_Spec_Doc2.md: Major / Moderate / Minor.

| # | Phase | Dimension | Severity | Before | After (proposed) | Why | Verified | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | OE | Truthfulness (Accuracy) | Major | OE5b: "There is exactly ONE: brookfield_6000001115 -- sap_module=treasury, debit 28.59, credit 0, posting_date 2026-05-29T16:42:00-04:00, description 'Payroll bank funding adjustment - May cycle...'" | Remove. The discriminator record does not exist; the scenario needs a new (real) discriminator to be designed. | Zero hits for both `brookfield_6000001115` and the string `28.59` across `sap_subledger.subledger_transactions.json`, `sap_subledger.ap_invoices.json`, and `oracle_gl.ogl_journal_entries.json`. The candidate fabricated this record. | yes — direct grep on `_aux/Universe_Split/*` | Pending (REBUILD) |
| 2 | OE | Truthfulness (Accuracy) | Major | OE5c: "the correct disposition is to journalize the missing $28.59 to the GL on account 102000... A trajectory that only disproves the thread and stops at 'unsupported / needs tie-out' has found the easy conflict and MISSED this real cause." | Remove. With the discriminator gone, the trajectory the OE5c paragraph disqualifies ("stops at unsupported / needs tie-out") is in fact the correct end-state in the data we have. | The remediation is built on the fabricated OE5b record. | yes — inherited from finding #1 | Pending (REBUILD) |
| 3 | OE | Truthfulness (Accuracy) | Major | OE10 (final response): "the REAL cause of the -$28.59 is a genuine unjournalized SAP cash item (brookfield_6000001115...) sitting on the 102000 subledger with no Oracle GL journal line... so the correct fix is to book that item to the GL" | Remove. With #1 and #2 gone, the final response can only assert: feed did not drop, GL had zero activity, FX explanation is unsupported, precedent does not hold, so accept-timing is not supported and the variance needs a real supporting-side tie-out before disposition. | The "real cause" claim is fabricated and cannot honestly be reported. | yes — inherited from finding #1 | Pending (REBUILD) |
| 4 | Rubrics | Groundedness | Major | Rubric 6: "identification of a real ~$28.59 subledger/bank-side item on account 102000 (a payroll funding adjustment posted ~late May) that exists on the supporting side but has no Oracle GL journal entry, accounting for the supporting-minus-GL difference of $28.59. A response that never names a specific reconciling item and only concludes 'unsupported / needs tie-out' does not satisfy this." | Remove. No agent can earn this honestly. | The rubric demands the agent identify the fabricated OE5b record. | yes — inherited from finding #1 | Pending (REBUILD) |
| 5 | Rubrics | Groundedness | Major | Rubric 7: "recommendation to book/journalize the missing $28.59 item to the GL (account 102000) to clear the variance, as opposed to accept-timing or relying on a feed retry." | Remove. There is no missing item to book. | The remediation rubric is built on the fabricated record. | yes — inherited from finding #1 | Pending (REBUILD) |
| 6 | Rubrics | JSON validity | Major | Rubric 3 title contains literal `\~$42`: `...had a variance of about -$3.42 (not the \~$42 feed-drop residual being claimed)...` | Replace `\~$42` with `~$42` (drop the backslash; tilde does not need escaping in JSON strings). | Validator FAIL: `Invalid \escape: line 1 column 1871 (char 1870)`. The file does not parse. | yes — validator output + raw-byte inspection | Pending (REBUILD) |
| 7 | OE | Accuracy (precedent shading) | Moderate | OE6: "the FP-2025-11 payroll feed run run_9e4afe5f93d549 posted 119/119 with 0 rejected" | Tighten the verbal claim. The 119/119/0 row counts are correct, but the universe records the run with `status: "retried"`, not `success` — so saying the feed "ran clean" overstates. Prefer "posted 119/119/0; the run is marked as retried in the system of record, which is a finer point than the precedent narrative claims." | Universe `oracle_gl.ogl_subledger_feed_runs.json` line for `run_9e4afe5f93d549`: `status: "retried"`, `rows_in: 119`, `rows_posted: 119`, `rows_rejected: 0`. | yes — direct grep | Pending (REBUILD) |
| 8 | Rubrics | Groundedness (precedent shading) | Moderate | Rubrics 3, 9, 12 each carry "FP-2025-11 payroll feed ran clean (119/119, 0 rejected)" | Anchor the rubric wording on the row counts only ("119/119, 0 rejected"). Drop "ran clean." | Same as finding #7. | yes — inherited | Pending (REBUILD) |
| 9 | OE | Convention (action-verb opening) | Minor | Only 3/12 OEs lead with an action verb (Search / Send / Call / Post / etc.). | Bring all 12 OEs onto action-first openings in the rebuild. | Validator WARN; V3 reference tasks (Task11–14) lead consistently with action verbs. | yes — validator output | Pending (REBUILD) |
| 10 | Prompt | Word count | Minor | Prompt is 389 words. | Trim to <= 350 in the rebuild. Sweet spot tightening. | Validator note. The 500-word cap is not breached; this is style polish, not block. | yes — validator output | Pending (REBUILD) |
| 11 | Prompt | Relative-date hygiene | Minor | "It's bounced around a few places this week" | Pin to "over the FP-2026-05 close cycle" or similar absolute frame against universe today 2026-06-12. | Validator note. | yes — validator output | Pending (REBUILD) |

## Status legend

- **Pending**: review's recommended change, awaiting user disposition.
- **Pending (REBUILD)**: the recommended path is a full rebuild via `PIPELINE REDO`, not an in-place edit. These rows are documented for the candidate-rating record; they are not staged for materialization.
- **Applied**: user accepted; review will materialize on a follow-up pass.
- **Dismissed-with-proof**: user reviewed and disagreed; include a one-line counter-citation here.

## Why no 14/15 emitted on this pass

Triage = REBUILD. Per the runbook: "If triage = REBUILD: do NOT emit 14/15 even if rows are Applied. The scenario is the problem — patching OE/rubric on top would ship a half-fixed task."

## Dismissed council concerns (Council was wrong)

None. Every council finding above survived re-grep against the per-task universe.
