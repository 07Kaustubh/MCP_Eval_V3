# REVIEW — Triage

**Triage verdict: REBUILD.**

## Trigger row fired

> ANY QC sub-dim on prompt or universe scores 1-2 (FAIL band) — feasibility, unique-ground-truth end-state divergence, ..., >=2 Major truthfulness errors, universe data missing.

Three of those conditions fire simultaneously. The scenario itself is the defect; in-place fixes on `6_Oracle_Events.txt` or `7_Rubrics.json` cannot rescue it.

## Per-sub-dim QC scoresheet (Prompt + Universe + OE + Rubrics)

### Prompt (12 sub-dims per Docs/7_QC_Spec_Doc1.json)

| Sub-dim | Score | One-line reason (cites per-task universe) |
|---|---|---|
| Persona-match | 5 | Ben Arinzo as bookkeeper anchoring a senior's variance check is on-pattern; linter pushback documented in `_aux/Linter_Decision.md` is sound. |
| Business-function fit | 5 | Bookkeeper context-pull on a payroll-cash variance is in-tier. |
| Naturalness / voice | 5 | Reads as a real Slack ask from "Blue". No prompt-engineering register. |
| Achievable | 5 | All write actions (Slack to C005, email reply to disposition thread, message to Blue/Ryan, reminder) are within available tools. |
| Feasibility (end-state reachable from data) | **2** | The end-state the rubric demands — identifying `brookfield_6000001115` as a real SAP item carrying debit 28.59 on account 102000 — is **not in the per-task universe** (confirmed: 0 hits for `28.59` or `brookfield_6000001115` across `sap_subledger.subledger_transactions.json`, `sap_subledger.ap_invoices.json`, `oracle_gl.ogl_journal_entries.json`). |
| Single seat-bound voice | 5 | Stays in Ben's voice throughout. |
| Tool-name leakage | 5 | None in prompt. |
| Em-dash / "at least N" | 5 | Clean per validator. |
| Word count | 4 | 389 words; sits inside the 500 cap but the validator suggests tightening; not material. |
| Relative-date hygiene | 4 | "this week" present (validator NOTE); resolvable against universe today 2026-06-12 but introduces a small ambiguity. |
| Multi-service coverage | 5 | BlackLine, GL feeds/feeds-runs, SAP subledger, Slack, email, messaging, reminder — comfortably multi-service. |
| Investigation pre-solved | 5 | Prompt sets up the contradiction but does not state the answer. |

**Worst Prompt sub-dim: Feasibility = 2 (FAIL band).**

### Universe (alignment to scenario)

| Sub-dim | Score | Reason |
|---|---|---|
| Universe data present for the rubric-mandated answer | **1** | `brookfield_6000001115` does not exist; no $28.59 SAP item exists on account 102000 in the May window. |
| Universe data present for thread / exception / recon | 5 | exc_aade06f6129e43, BL-333FF9956BC6, run_1fb45b81237648 all confirmed. |
| Universe data present for precedent | 4 | BL-8DCA6908E272 confirmed (variance -3.42, certified, no feed-drop exception); FP-2025-11 payroll feed run_9e4afe5f93d549 is `status: retried` (not the clean "success" the candidate's OE6 implies, although it did post 119/119/0). Moderate, not Major. |

**Worst Universe sub-dim: 1 (CRITICAL FAIL band).**

### Oracle Events

| Sub-dim | Score | Reason |
|---|---|---|
| Completeness | 5 | 12 OEs cover thread, exception, feeds, GL, precedent, all writes, reminder, response. |
| Accuracy (groundedness) | **1** | OE5b states `brookfield_6000001115` is a real SAP transaction with debit 28.59 / posting_date 2026-05-29T16:42:00-04:00 / description "Payroll bank funding adjustment - May cycle..." — **none of these are in the universe**. OE5c builds remediation guidance on this fabricated record. |
| Tool-name placement | 5 | Tool names appear in OE bodies as allowed. |
| Action-verb opening | 3 | Validator WARN: only 3/12 OE lines start with action verbs (Send/Search/Call/etc.). Reference tasks open consistently with action verbs. |
| Write-action explicitness | 5 | C005 post, email reply, DM, reminder all explicit. |
| Lever preservation across OEs | 4 | The "discriminator" lever (real SAP item) does not exist, so the lever the OEs were built around collapses. |

**Worst OE sub-dim: Accuracy = 1 (CRITICAL FAIL band).**

### Rubrics

| Sub-dim | Score | Reason |
|---|---|---|
| JSON validity | **1** | Validator FAIL: `Invalid \escape: line 1 column 1871` — `\~$42` in rubric 3's title. The file does not parse. Platform upload would reject it. |
| Atomicity | 4 | Most rubrics are atomic; rubrics 10 and 11 each target a single named recipient, which is good. |
| Self-containment | 5 | Each rubric carries its own justification + evidence. |
| Outcome vs Process balance | 5 | 13 outcome rubrics, 0 process. Matches V3 reference posture. |
| Groundedness | **1** | Rubric 6: "identification of a real ~$28.59 subledger/bank-side item on account 102000 (a payroll funding adjustment posted ~late May) that exists on the supporting side but has no Oracle GL journal entry, accounting for the supporting-minus-GL difference of $28.59" — **demands a record the universe does not contain**. Rubric 7: "book/journalize the missing $28.59 item to the GL (account 102000)" — recommends a corrective JE for a non-existent item. |
| Title hygiene (tool names / "at least N") | 5 | Clean. |
| Evidence specificity | 5 | Each rubric tells the verifier what string / channel / recipient to match. |

**Worst Rubrics sub-dim: Groundedness = 1, JSON validity = 1 (both CRITICAL FAIL band).**

## Hardness numbers (measured)

| Metric | Value | Pass? |
|---|---|---|
| avg_tool_calls_total | 53 | YES (>= 40) |
| pass@1 | 0.0 | YES (<= 0.40) |

Hardness does not gate; truthfulness does.

## Why REBUILD, not SALVAGEABLE

The "discriminator" the prompt was built around (a real SAP item under a fake feed-drop thread) is not in the data. Patching OE5b/5c and rubrics 6/7 to remove the fabricated record would collapse the scenario to "the thread's feed-drop story is unsupported, no further finding" — which the candidate's own OE5b explicitly disqualifies ("A trajectory that only disproves the thread and stops at 'unsupported / needs tie-out' has found the easy conflict and MISSED this real cause"). Either:

- the universe was supposed to contain a real $28.59 SAP item and someone forgot to inject it, or
- the discriminator was always imagined and was never grounded.

Either way the fix is a rebuild that re-introduces a real discriminator (either by injecting the missing universe record or by pivoting the scenario's true cause to something the data actually supports), not by editing rubrics around a hole.

## Next step

`PIPELINE REDO — Tasks/27_6a39fd19048f9213281ec7b` in a fresh chat. Per the runbook: rebuild 5/6/7 from scratch as a full CB build. Originals stay untouched. `13_Feedback.txt` carries the candidate-facing FAIL verdict.
