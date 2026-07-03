# S4 Double-check against universe + Evals_keystone + QC spec docs — Task 37

**Trigger:** operator asked to double-check S4 findings against `3_UniverseDataForThisTask.json`, `Evals_keystone/*`, `Docs_keystone/7_QC_Spec_Doc1.json`, and `Docs_keystone/8_QC_Spec_Doc2.md`.

**Verdict:** all S4 findings hold. No corrections needed. One reasoning-path note added below.

---

## Universe atoms — every loan-level claim in the AF justifications

Queried `mortgage_los.loans` + `mortgage_los.document_checklist_items` from `3_UniverseDataForThisTask.json` (644 loan rows, 8841 document rows).

**21 loans referenced in the AF justifications — all atoms clean:**

| Loan | Rubric | Status | Lock exp | Amount | Universe match |
|---|---|---|---|---|---|
| LN-2026-00623 | A / F13 | clear_to_close | 2026-04-01 | $467,000 | OK |
| LN-2024-00123 | B / F7 | conditional_approval | 2024-10-07 | $267,000 | OK |
| LN-2026-00532 | B / F7 | underwriting | 2026-03-24 | $218,400 | OK |
| LN-2024-00103 | C / F5 | processing | 2024-09-08 | (present) | OK |
| LN-2025-00330 | C / F5 | processing | 2025-06-22 | (present) | OK |
| LN-2025-00380 | C / F5 | conditional_approval | 2025-08-30 | (present) | OK |
| LN-2026-00376 | C / F5 | processing | 2026-03-20 | (present) | OK |
| LN-2024-00125 | D / F15 | underwriting | 2024-10-17 | $246,600 | OK |
| LN-2026-00539 | D / F15 | conditional_approval | 2026-04-03 | $734,000 | OK |
| LN-2026-00010 | E / F9 | processing | 2026-04-24 | $519,200 | OK |
| LN-2025-00286 | F / F9 | clear_to_close | 2025-05-12 | $382,800 | OK |
| LN-2025-00344 | G / F11 | conditional_approval | 2025-07-05 | $800,000 | OK |
| LN-2025-00363 | G / F11 | processing | 2025-07-29 | $196,200 | OK |
| LN-2026-00541 | G / F11 | application | 2026-04-06 | $720,000 | OK |
| LN-2026-00611 | (context) | processing | 2026-04-10 | $214,000 | OK |
| LN-2026-00184 | (context) | processing | 2026-03-23 | $340,000 | OK |
| LN-2026-00613 | (context) | conditional_approval | 2026-04-14 | $433,000 | OK |
| LN-2025-00244 | (context) | processing | 2025-03-21 | $185,300 | OK |
| LN-2026-00008 | (context) | conditional_approval | 2026-03-11 | $276,400 | OK |
| LN-2026-00196 | (context) | processing | 2026-03-13 | $229,000 | OK |
| LN-2026-00632 | (context) | underwriting | 2026-04-04 | $268,000 | OK |

**Outstanding-document counts on the anomaly loans:**

| Loan | Rubric | Verifier claim | Universe count | Types outstanding |
|---|---|---|---|---|
| LN-2026-00623 | A | 5 outstanding (pay stub, current + prior W-2s, current-year tax return, driver's license) | **5** | drivers_license, paystub_1, tax_return_current, w2_current, w2_prior |
| LN-2026-00010 | E | 7 outstanding (max in pipeline) | **7** | VOE, W2s, appraisal, credit_report, homeowners_insurance, pay_stubs, tax_returns |
| LN-2026-00196 | (materialize row #1) | 1 outstanding (w2_current) | **1** | w2_current |
| LN-2026-00376 | C | 3 outstanding | **3** | drivers_license, hoi_binder, tax_return_prior |
| LN-2026-00611 | (context) | 1 outstanding | **1** | drivers_license |

All 5 doc-count claims match. LN-2026-00010 = 7 outstanding is grounded and the highest count I found on the queried anomaly loans.

**Naming alignment on LN-2026-00623's 5 outstanding docs vs the rubric title language:**
- Universe field names: `paystub_1`, `w2_current`, `w2_prior`, `tax_return_current`, `drivers_license`
- Rubric title language: "a pay stub, current and prior W-2s, current-year tax return, and driver's license"
- Match: paystub_1 → pay stub; w2_current + w2_prior → current and prior W-2s; tax_return_current → current-year tax return; drivers_license → driver's license. Clean 1:1 mapping.

---

## Bucket 2 tool-name check (Rubric H, Run 4)

**Query result on `Mortgage_Base_Universe/6_Server_Tools_Details.json`:**
- `mortgage_los_add_activity` → **present** (real Keystone tool)
- `activity_create` → **absent** (phantom name the Run 4 verifier grepped for)

**Direct trajectory inspection on `trajectory-runs/trajectory-run-4 (23).json`:**
- 26 `mortgage_los_add_activity` tool_use nodes
- 26 matched tool_result payloads, each returning a unique `id` (activity id) + `created_at` timestamp
- First matched pair confirmed with full JSON (tool_use_id `toolu_01H7bjy51EPRGcEvy1JDCJ4B`, tool_result id `2adca2f7-1100-465b-8934-1226953d249c`)

Runs 1, 2, 3, 5, 6 verifier justifications on the same rubric all name the tool correctly (`mortgage_los_add_activity`) and mark Pass. Run 4's verifier is the only outlier and it used the wrong grep string. **Bucket 2 (Judge Error) verdict holds.**

---

## QC spec threshold alignment (Docs_keystone/7_QC_Spec_Doc1.json + 8_QC_Spec_Doc2.md)

| Sub-dim | Spec threshold | Task 37 measurement | Verdict |
|---|---|---|---|
| Tool Call Count (T1) | PASS if avg ≥ 15 | avg 216.8 | PASS |
| Agent Failure Rate (T2) | PASS if 0-2 of 6 runs pass all rubrics (pass@1 ≤ 40%) | 1/6 = 16.7% | PASS |
| Error Rate (T3) | PASS if fewer than 3 runs errored | 0/6 errored | PASS |
| All-Failing Rubrics | **"If no rubrics failed all completed runs, this dimension is automatically a 5"** — spec verbatim | 0 AF rubrics (every failing rubric has ≥ 3 passing runs of 6) | PASS (automatic 5) |

**Reasoning-path note on All-Failing Rubrics sub-dim.** `S4_verdict.md` scored this sub-dim at 5/5 via the pipeline v11 Bucket-1-ratio rule (0 / 8 failing rubrics = 0% Bucket 1 ratio → 5/5). The strict QC spec reaches the same 5/5 via a simpler path: no rubric failed all 6 completed runs, so the dimension is automatically 5 and does not need to be audited at all. Both paths converge on 5/5 PASS. The pipeline-exceeds-spec ratio scoring is retained in the verdict file as defense-in-depth in case a future rubric revision converts a partial fail into a full AF.

---

## Verifier Fails Eval (Evals_keystone/4_Verifier_Fails_Eval.md) — bucket taxonomy alignment

Spec bucket names → pipeline Bucket 1/2/3 mapping:

| Spec name | Pipeline bucket | Task 37 count |
|---|---|---|
| Rubric Invalid | Bucket 1 | 0 |
| Judge Error | Bucket 2 | 1 (Rubric H, Run 4) |
| Legitimate Fail | Bucket 3 | 7 unique rubrics × 12 fail-instances |
| Excluded | (not applied — 0 errored runs) | 0 |

Alignment: exact. Also verified against Verifier Fails Eval Phase 2 Rubric Validity checks:
- **Tool existence** — Rubric H's real tool exists (`mortgage_los_add_activity`); rubric text does not name a tool, so no phantom-tool issue on the rubric itself. Judge error, not rubric invalid.
- **Expected value existence** — all 21 loans + 5 anomaly-doc-count atoms exist in universe. No unfounded expected values.
- **Prompt grounding** — every failing rubric traces to a prompt ask (per-LO update, final response summary, LOS activity note).
- **Environment / tool-error fail (T7)** — 0/6 errored, no server-side tool failure explains any AF.

Verifier Fails Eval Phase 3 Judge Accuracy: Bucket 2 finding on Rubric H Run 4 is exactly the "trajectory shows the agent did satisfy the criterion and the judge missed it" scenario described in the eval intro.

---

## Prompt Eval / OE Eval / Rubrics Eval cross-references

These evals are pre-S4 gates. S4 does not re-run them but the Bucket-1 empty result implicitly confirms that no rubric-invalid pattern (over-specific wording, phantom tool, beyond-prompt scope, unfair to valid alternative) surfaced in the 6-run empirical evaluation. This aligns with the AUDIT_rubrics_original.md verdict at REVIEW time (rubric set was structurally clean).

---

## Deltas vs `S4_verdict.md`

1. **All-Failing Rubrics sub-dim reasoning path** — added a note that the QC spec's simpler "no AF rubrics → automatic 5" path reaches the same verdict. Retained the pipeline v11 Bucket-1-ratio scoring for defense-in-depth. **No score change (both = 5/5).**
2. **Nothing else changes.** Bucket 1/2/3 counts, gate verdicts, atom claims, tool-name-grep judge error, calibration deltas, and shippable AF batch all pass the double-check.
