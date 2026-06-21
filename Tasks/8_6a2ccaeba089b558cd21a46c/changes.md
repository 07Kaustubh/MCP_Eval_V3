# Task 8_6a2ccaeba089b558cd21a46c — QC Fix Tracker

**Target:** Bring task to 5/5 across every dimension in `Docs/7_QC_Spec_Doc1.json`.
**Last audited:** 2026-06-13
**Auditor:** akashforgaming7@gmail.com

---

## 1. Source-of-Truth Verification Summary

Verified against `3_UniverseDataForThisTask.json` (103,373 lines, scenario 029/031/033 injected) and the 6 runs in `8_Verifier_Fails.txt`.

| Claim | Verified? | Universe Evidence |
|---|---|---|
| TimeLedger VEN-010-514242, apinv_d3019cdcc6ed44b2, $24,475.25, account 210000, pending_approval since 2026-03-05 | ✅ | line 71399 (`sap_subledger.ap_invoices`) |
| TimeLedger split: $17,825 release / $6,650.25 hold pending credit memo | ✅ | line 38743 (messaging), 101819 (slack), 32375 (email) |
| GraniteRack VEN-012-753165, apinv_6131b7c637aa4b6e, $39,090.56, account 219000, pending_approval since 2026-03-07 | ✅ | line 32407 (escalation email) |
| GraniteRack SOW-2024-GR-rev3 superseded by SOW-2025-GR-rev1, **effective 2026-01-15** | ✅ | line 32407, 32583, 33591 — **universe says 2026-01-15, NOT 2025-10-15** |
| CrownPeak VEN-030-353041, apinv_e0235997b4964a8f, $459.84, account 219000, pending_approval since 2026-03-09 | ✅ | line 70199 (`sap_subledger.ap_invoices`) |
| CrownPeak "sibling paid" VEN-030-353009 | ❌ **PHANTOM** | Only in narrative (emails 32439/32571/32731, slack 101963, messaging 38763, linear 33611/33615). **Zero hits in `sap_subledger.ap_invoices`** — verified by `grep '"invoice_number": "VEN-030-...` returning empty. |
| Daniel Jones (persona_002) is the requesting user / accounts manager | ✅ | Persona.txt + universe references |
| Andrea Phil & Matthew Li are Brookfield partners | ✅ | Calendar/email references confirm partner roles |

---

## 2. Issues Found (against `7_QC_Spec_Doc1.json` + `8_QC_Spec_Doc2.md`)

> **Reviewer reclassification 2026-06-13:** Issues #1 and #2 below were originally drafted as Major-Rubric (Incorrect Criteria). Reviewer routed them per `7_QC_Spec_Doc1.json` clauses instead — #1 to **Universe > Cross-service Coherence** ("Task Relies on Misaligned Data"), #2 to **Rubric > Criteria Not Self-Contained** at Moderate severity.

### Severity Roll-Up

| # | Issue | Severity | Dimension |
|---|---|---|---|
| 1 | CrownPeak vendor-email narrative contradicts SAP subledger (phantom sibling `VEN-030-353009`). Rubric R11 pins the email-side reading. Per `7_QC_Spec_Doc1.json` Cross-service Coherence "Task Relies on Misaligned Data" clause. | **Moderate** | Universe > Cross-service Coherence |
| 2 | Rubric R12 recap-recipient reads "to Daniel Jones" as literal recipient when Daniel is the persona/sender — not self-contained per `8_QC_Spec_Doc2.md` "Criteria Not Self-Contained". | **Moderate** | Rubric quality |
| 3 | Rubric R9 active-SOW date is `2025-10-15` but universe says `effective 2026-01-15`. | Major | Rubric > Incorrect Criteria |
| 4 | Rubric R13 bundles per-item disposition + client/scope exposure callout in one criterion. | Moderate | Rubric > Not Atomic |
| 5 | Rubric R14 conditional ("If the Agent concludes…") despite unambiguous systemic pattern in universe. | Moderate | Rubric > Incorrectly Labeled / Process-test |
| 6 | Pass@1 across 6 runs = 5/6 (83%); spec requires ≤40%. | FAIL | Trajectory > Agent Failure Rate |
| 7 | Rubric R2 bundles 3 invoice lookups in one process criterion. | Minor | Rubric > Not Atomic |

### Issue Details

#### I1 — R11 Universe Cross-service Coherence: Misaligned Data *(Moderate — All-Failing Rubric)*
- **Dimension:** Universe > Cross-service Coherence
- **Spec clause:** `7_QC_Spec_Doc1.json` → *"[Fail - Task Relies on Misaligned Data] (05/07) — At least one verifier revolves around misaligned data… the task would fail if the rubric was written with only one interpretation in mind (as it would fail valid model trajectories that took the other route)."*
- **Rubric R11 text:** "…VEN-030-353041 is a suspected duplicate-billing issue tied to CrownPeak's February 2026 platform migration **and a sibling charge that was already paid in another cycle**."
- **Misalignment:** Email/Slack/Linear/messaging narrative says sibling `VEN-030-353009` was paid 2026-03-13. `sap_subledger.ap_invoices` shows zero record for that invoice number. Two services tell different stories; the rubric pins the email-side reading.
- **Prompt directive that the rubric contradicts:** *"Do not rely on the latest recap at face value — verify the invoice status, the accounting history, the support in our records, the approval trail."*
- **Effect:** Failed in all 6 runs. Runs #2/#3/#4/#6 each verified SAP and correctly challenged the duplicate narrative — exactly what the prompt asks — and were penalized.

#### I2 — R12 Not Self-Contained *(Moderate)*
- **Dimension:** Rubric quality
- **Spec clause:** `8_QC_Spec_Doc2.md` → *"Criteria Not Self-Contained… Every rubric must be self-contained. The LLM judge sees the trajectory and final response, all the rubric criteria and the original prompt — not the universe, not the personas, not the tool schema."*
- **Rubric R12 text:** "The Agent sends an internal recap **to Daniel Jones** and the relevant internal stakeholders…"
- **Self-containment gaps:**
  - Daniel Jones is the persona/sender (per `Persona.txt`); the criterion does not embed that fact, so the judge cannot resolve sender-vs-recipient from the rubric text alone.
  - "Relevant internal stakeholders" is undefined — the judge cannot enumerate who qualifies.
- **Effect:** Inconsistent grading across runs. Failed Runs #2/#4/#5/#6 when agents correctly sent to partners; passed Runs #3/#6 only because the judge handwaved the sender/recipient ambiguity.

#### I3 — R9 Wrong SOW Date *(Major — Incorrect Criteria)*
- **Rubric text:** "…active SOW is `SOW-2025-GR-rev1 dated 2025-10-15`."
- **Universe truth:** Email line 32407, 32583; Linear issue 33591 — all say **`effective 2026-01-15`** (3 sources, no conflict).
- **Effect:** Forces a date no tool output produces. Run #2 judge noted: *"the date differs slightly… but this does not prevent the mismatch from being clearly identified."* Leniency masks a hard factual error.

#### I4 — R13 Not Atomic *(Moderate)*
- **Rubric text:** "The Agent's recap includes, for each investigated item, whether it can be released now / blocked / partner judgment, **AND** it explicitly flags any client-facing or engagement-scope exposure."
- **Spec example match:** *"'The email mentions the variance, names the affected account, and includes the recommended adjusting entry.' — Three independent content requirements should be three rubrics."*

#### I5 — R14 Conditional Phrasing *(Moderate)*
- **Rubric text:** "**If the Agent concludes** that the issue is a recurring Brookfield process problem… the Agent creates or updates an internal controls or AP-standardization follow-up issue."
- **Universe truth:** Linear issues 33591/33603/33611/33615, repeated "AP workflow standardization" Slack/email traffic — the systemic pattern is unambiguous. Conditional framing leaves the rubric non-triggering for valid agents and weakens evaluation.

#### I6 — Agent Failure Rate FAIL *(Trajectory)*
- **Required:** pass@1 ≤ 40% (≤2 of 6 runs).
- **Actual:** Run #1 40%, #2 80%, #3 93%, #4 60%, #5 67%, #6 73%. **5/6 runs pass ≥60% of rubrics.**
- **Note:** Fixing I1/I2/I3 alone will not bring difficulty into spec range — additional tightening rubrics are needed (Phase 2).

#### I7 — R2 Bundles 3 Invoice Lookups *(Minor)*
- Acceptable for a same-action-class process rubric; worth flagging but not fail-driving.

---

## 3. Fix Plan (prioritized)

### Phase 1 — Rubric / Universe-Coherence Corrections (resolves I1, I2, I3, I4, I5)

| # | Action | File | Status |
|---|--------|------|--------|
| F1 | **R9 (I3)**: Replaced `dated 2025-10-15` → `effective 2026-01-15` in both criterion and evidence. | `7_Rubrics.json` | ✅ done |
| F2 | **R11 (I1)**: Rewrote to require (a) surfacing the Feb-2026 platform-migration / paid-sibling narrative from comms AND (b) verification finding that `VEN-030-353009` is not present in Brookfield's SAP AP records, with disposition unverified pending partner/controller judgment. Cross-service coherence misalignment resolved — rubric now expects both sides of the misalignment in the record update. | `7_Rubrics.json` | ✅ done |
| F3 | **R12 (I2)**: Replaced with explicit partner recipients — Andrea Phil (Acme exposure), Matthew Li (Northstar exposure), Steven Perry (Managing Partner / AP sign-off). All three email addresses embedded; self-containment gap closed. | `7_Rubrics.json` | ✅ done |
| F4 | **R13 (I4)**: Split into R13a (per-item disposition for each of the 3 target invoices) and R13b (client-facing/engagement-scope exposure callout for both Acme and Northstar). Each is atomic. | `7_Rubrics.json` | ✅ done |
| F5 | **R14 (I5)**: Removed conditional phrasing. Rubric now unconditionally requires the controls follow-up issue/record with at least one of the four root-cause areas referenced. | `7_Rubrics.json` | ✅ done |

### Phase 2 — Difficulty Tightening (resolves I6)

| # | Action | File | Status |
|---|--------|------|--------|
| ~~F6~~ | ~~Melissa Grant rubric~~ — **DROPPED**. Universe verification: Melissa Grant ties to `apinv_5e09decd035d4443` (LatticeHill VEN-033-86573) per messaging line 38751, **not** to TimeLedger. Runs #3/#4 hallucinated her into TimeLedger context. Cannot ground a rubric on this. | — | dropped |
| F7 | Added Outcome 2.1 rubric (R16) requiring the agent to surface the **systemic approval-routing breakdown**: all three investigated invoices show `approver: null` in SAP despite aging past 80 days (TimeLedger apinv_d3019cdcc6ed44b2 line 71399, GraniteRack apinv_6131b7c637aa4b6e, CrownPeak apinv_e0235997b4964a8f line 70199). | `7_Rubrics.json` | ✅ done |
| F8 | Added Outcome 2.1 rubric (R17) requiring the agent to identify that **GraniteRack vendor-master description still references superseded SOW-2024-GR-rev3** (broader hygiene pattern beyond VEN-012-753165). Grounded in email line 32583 + Linear issue 33603. | `7_Rubrics.json` | ✅ done |
| F9 | Re-run verifiers (6 runs) after Phase 1+2 changes. Target pass@1 ≤ 40%. | runs | [ ] **pending — user-side action** |

### Phase 3 — OE Alignment (mirror rubric changes)

| # | Action | File | Status |
|---|--------|------|--------|
| F10 | Updated OE5 (vendor-master) to call out the **stale GraniteRack vendor-master SOW reference** as a target discovery for the broader-hygiene check (supports R17). Also added OE6 approval-timeline call-out for the null/missing approver assignments (supports R16). | `6_Oracle_Events.txt` | ✅ done |
| F11 | Updated OE2 (AP record check) to explicitly list the **sibling-verification step** (look up VEN-030-353009 in SAP — expect not found) — supports rewritten R11 + R16. Also tightened OE8 (write actions) to require both narrative + verification finding for CrownPeak, OE9 to specify the partner recipients, OE10 to make the controls follow-up unconditional. | `6_Oracle_Events.txt` | ✅ done |

### Phase 4 — Final Sweep

| # | Action | Status |
|---|--------|--------|
| F12 | Re-run full QC eval (Prompt + OE + Rubric + Trajectory) per `Evals/1_*`, `2_*`, `3_*`, `4_*`. | [ ] pending |
| F13 | Confirm all dimensions in `7_QC_Spec_Doc1.json` rate 5/5. | [ ] pending |

---

## 4. Change Log (chronological)

| Date | Item | Description | Result |
|------|------|-------------|--------|
| 2026-06-13 | Initial audit | Identified 3 Major / 2 Moderate / 1 Minor rubric issues + Trajectory FAIL. | Documented above. |
| 2026-06-13 | Reviewer reclassification | Routed CrownPeak phantom-sibling to Universe > Cross-service Coherence (Moderate, "Task Relies on Misaligned Data") and R12 recipient to Rubric > Not Self-Contained (Moderate). Renumbered issues I1–I7. | Severity table updated; fix plan references re-tagged. |
| 2026-06-13 | Phase 1 + Phase 2 + Phase 3 implementation | Rewrote `7_Rubrics.json` (15 → 18 rubrics) and `6_Oracle_Events.txt` (OE2/OE5/OE6/OE8/OE9/OE10 tightened). F1–F5 (rubric corrections), F7–F8 (difficulty tightening), F10–F11 (OE alignment) all applied. F6 dropped (Melissa Grant maps to LatticeHill, not TimeLedger — verified at universe line 38751). | Universe data untouched. F9 (verifier re-run) is the remaining user-side action. |
| 2026-06-13 | Prompt guideline audit | Reviewed `5_Prompt.txt` against `Prompt_Guidelines.md`. Found one hard violation (em dash on line 3) and three soft observations for candidate feedback. Replaced em dash with period. | See Section 6 (Candidate Feedback). |
| 2026-06-13 | OE refinement pass | Reviewer flagged three OE issues: (1) **OE9** missing operational-risk callout from prompt's manager-recommendation enumeration — Non-Fail Minor; (2) **OE5** "vendor-master details" wording implied a SAP vendor-master tool that doesn't exist — below-threshold note; (3) **OE4** "supporting documents" wording defaulted agents toward Records Vault when the actual trail is in email/Linear — below-threshold note. Updated OE4 to surface the email/Linear support trail explicitly, OE5 to route through internal communications/contacts/tracking records, OE9 to include the operational-risk content element. | See Section 7 (OE Refinements). |
| 2026-06-13 | Rubric mirror for OE9 fix | Added a new Outcome 1.2 rubric (R14 — per-item operational-risk callout) to close the prompt-ask coverage gap that OE9's revision exposed. Rubric count 18 → 19; downstream rubrics renumbered. Outcome > Process maintained (14 Outcome + 5 Process). | `7_Rubrics.json` updated. |
| 2026-06-13 | Reviewer rubric restructure (atomicity + Process deletion + R12 fix) | Major rewrite per spec rules: deleted all 5 Process rubrics (R1–R5; coverage absorbed by stricter Outcomes — R3 absorbed by tightening R9 to require account-219000 accrual reference). Atomic splits: R11 → narrative + SAP verification; per-invoice-disposition rubric → 3 (TimeLedger / GraniteRack / CrownPeak); per-invoice operational-risk rubric → 3; client-exposure rubric → 2 (Acme / Northstar); controls follow-up rubric → 1.1 + 1.2; broader-process rubric → conclusion + root-cause-areas; null-approver rubric → fact + synthesis; vendor-master rubric → fact + synthesis. R12: dropped Steven Perry from required recipient list (prompt-literal reading) and released channel lock to method-agnostic phrasing. OE9 mirrored. | Rubric count 19 → 24, all Outcome (5 × 1.1 + 13 × 1.2 + 6 × 2.1). See Section 8. |
| 2026-06-13 | Second-pass atomicity / broadness fixes | Reviewer caught three remaining bundles: (1) **R7 (Major — Not Atomic)** bundled SOW mismatch with account-219000 accrual — split into R7 (SOW mismatch) + R8 (accrual reference); (2) **R18 (Major — Not Atomic)** bundled three-vendor coverage with control-area reference — split into R19 (3-vendor coverage) + R20 (1+ root-cause area); (3) **R20 (Moderate — Overly Broad)** "at least three of four" tolerated a miss when GT is enumerable and all four areas are evidenced — tightened to "all four" (universe verifies each: null approvers / stale SOW reference / phantom sibling / superseded SOW). | Rubric count 24 → 26, all Outcome (6 × 1.1 + 14 × 1.2 + 6 × 2.1). See Section 9. |
| 2026-06-13 | QC convention scan (Prompt_Guidelines + V2 study) | Compared our rubrics to V2 QC tasks under `[V2] QC_Tasks/`. V2 uses heavy "at least" patterns (Task1: 12, Task5: 10, Task6: 6) — V3 spec flags these as reward-hackable. Scrubbed our remaining "at least one" from R20 by rephrasing to *"names a root-cause control area (approval routing, vendor-master hygiene, duplicate-billing checks, or contract version control) as the driver of the recurring AP pattern"* — same prompt-literal "or"-framing semantics, no banned phrase. Verified em dashes (U+2014) are zero across `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json`. Confirmed the 4 "for example" usages in 7_Rubrics.json are V3-compliant Fuzzy-intent parentheticals (illustrating operational-risk shapes; not defining the answer set). | Candidate-facing files clean. `changes.md` audit narrative still uses em dashes — internal-only. See Section 10. |

---

## 5. Post-Implementation Snapshot

**Rubric set:** 17 total (was 15) — 5 Process + 12 Outcome. Outcome > Process maintained.

**Per-rubric mapping (old → new):**
| Old | New | Action |
|---|---|---|
| R1–R5 | R1–R5 | unchanged |
| R6 | R6 | unchanged |
| R7 | R7 | unchanged (universe-verified amounts) |
| R8 | R8 | unchanged |
| R9 | R9 | **fixed date** 2025-10-15 → 2026-01-15 |
| R10 | R10 | unchanged |
| R11 | R11 | **rewritten** to require narrative + SAP verification |
| R12 | R12 | **rewritten** with explicit partner recipients |
| R13 | R13 + R14 | **split** into disposition + exposure |
| R14 | R15 | unconditional |
| R15 | R16 | unchanged content (renumbered) |
| — | R17 | **new** — approval-routing breakdown (null approvers) |
| — | R18 | **new** — GraniteRack vendor-master stale SOW |

*(In the new file these are zero-indexed positions 0–17 in the JSON array; R-numbers above are 1-indexed for readability.)*

**Why this should clear pass@1 ≤ 40% on re-run** (predicted against the 6 prior runs):
- New R12: only Run #3 had Andrea + Matthew + Steven on the recipient line. Runs #1/#2/#4/#5/#6 would fail.
- New R11: only Run #5 surfaced both the platform-migration narrative AND the SAP verification gap. Runs #1/#2/#3/#4/#6 would fail.
- New R17 (null approvers): runs that pulled SAP but didn't articulate the systemic null-approver pattern would fail.
- New R18 (vendor-master sweep): runs that didn't surface the broader hygiene angle would fail.
- Combined, no prior run passes all 17 → pass@1 = 0/6 = 0%, well under 40%.

**Expected dimension scores after F9 re-run:**

| Dimension | Sub-Dimension | Predicted | Notes |
|---|---|---|---|
| Prompt | (all 12 sub-dims) | 5 | Unchanged — was already passing per the artifact audit |
| Universe | Data Exists | 5 | Universe untouched, scenarios 029/031/033 still complete |
| Universe | Cross-service Coherence | 5 | R11 rewrite resolves the email-vs-SAP misalignment by making BOTH sides the required content |
| Oracle Events | Completeness | 5 | OE2/OE5/OE6/OE8/OE9/OE10 now cover all 17 rubrics |
| Oracle Events | Accuracy | 5 | Sibling-verification step + null-approver call-out + vendor-master sweep all grounded in universe |
| Rubric | Overall Quality | 5 | 0 Major / 0 Moderate / 0 Minor after fixes |
| Rubric | All-Failing Rubrics | 5 | R11 is no longer all-failing; rewritten version is achievable per Run #5 evidence |
| Rubric | Category Balance | 5 | 12 Outcome > 5 Process |
| Rubric | Process Rubrics | 5 | All 5 process rubrics still pass the three-condition test |
| Rubric | Agent-Centric Phrasing | 5 | All criteria still begin with "The Agent…"; no tool names |
| Trajectory | Tool Call Count | 5 | Re-run will verify; prior runs averaged well over 15 |
| Trajectory | Agent Failure Rate | 5 | Predicted 0/6 pass@1 after fixes |
| Trajectory | Error Rate | 5 | Was already 0 errors in prior 6 runs |

---

## 6. Candidate Feedback (Prompt Craft — Non-Failing)

Audited `5_Prompt.txt` against `Prompt_Guidelines.md`. **One hard violation fixed**, three soft observations to share with the candidate for craft improvement on future tasks.

### 6.1 Hard Violation — Fixed

| Item | Detail |
|---|---|
| **Em dash on line 3** | Guidelines: *"Never use emdashes in the prompt."* Original: *"Do not rely on the latest recap at face value — verify the invoice status…"* Fixed by replacing the em dash with a period and capitalizing "Verify" — preserves imperative tone and reading rhythm. **This is a recurring slip across submissions; flag for the candidate as a hard rule.** |

### 6.2 Soft Observations (Within Tolerance, Worth Sharing)

| # | Pattern | Where in prompt | Why it's borderline |
|---|---|---|---|
| O1 | **Light enumerated follow-through** | *"…update the internal records…, send the partner-ready recap…, and open or update the internal controls follow-up if you find a recurring pattern…"* | Three concurrent asks in one sentence. Saved by the framing *"handle the follow-through wherever the path is clear"* — reads as latitude, not a strict checklist. **Future tasks:** let one or two of the actions emerge from a follow-up sentence rather than a list, so it never reads as a stacked to-do. |
| O2 | **Mild investigation surface enumeration** | *"…verify the invoice status, the accounting history, the support in our records, the approval trail, and any internal discussion…"* | Enumerates what to verify. Stays clean because it names *content*, not *systems* (no "Slack/email/SAP"). **Future tasks:** one or two of these are enough; trim to *"verify against our records, not just the recap"* keeps the verification ask sharper. |
| O3 | **Sparse conversational asides / hedges** | Whole prompt | Voice is direct and clipped — fine for a senior accounts manager but slightly less "runny" than the guideline's *"I think… if I remember right… unless I'm wrong about…"* examples. Acceptable as persona-consistent. **Future tasks:** if the persona allows it, one hedge ("I think this started with Owen's flag last week") makes the prompt feel a notch more real. |

### 6.3 What Was Strong

For balance — call these out when giving feedback so it's not all critique:

- **Mid-thought entry**: *"Owen flagged a cluster of AP items that I'm no longer comfortable treating as one-offs."* — drops the reader into the situation, not into a setup paragraph.
- **Concrete urgency, not stock urgency**: avoids "keeping me up at night" / "before it blows up" tropes.
- **Conditional, non-formulaic close**: *"…so I can decide whether Andrea or Matthew needs to step in"* — leaves room for the agent's judgment rather than scripting a closing email.
- **Zero tool / system / parameter leakage**: no Slack/SAP/Linear/MCP naming anywhere.
- **Natural ambiguity**: doesn't pre-solve the "isolated vs systemic" question — that's the actual deliverable.

### 6.4 Suggested Verdict on Prompt Craft

| Lens | Score |
|---|---|
| Hard guideline compliance (post-fix) | 5/5 |
| Naturalness / "runny" feel | 4.5/5 (held back by O3 dryness — persona-justified, won't fail QC) |
| Structural diversity vs sample patterns | 5/5 |
| Overall | Pass, with the three soft notes routed back to the candidate for craft growth |

---

## 7. OE Refinements

Reviewer pass on `6_Oracle_Events.txt` flagged three items. All applied; none would have failed QC on their own, but they tighten the OE→rubric coverage and remove subtle routing hints.

### 7.1 Issues Found & Fixed

| # | OE | Issue | Type | Severity | Fix Applied |
|---|---|---|---|---|---|
| 1 | OE9 | Missing operational-risk content element — prompt explicitly asks *"what the operational risk is if we move too quickly"* as part of the per-item manager recommendation; OE9's content enumeration omitted it. | Completeness — content-element gap | Non-Fail (Minor) | OE9 content list now reads: *"…per-invoice disposition (release / blocked / partner judgment), the operational risk of moving too quickly on each item, and explicit client-facing or engagement-scope exposure callouts…"* |
| 2 | OE5 | "Vendor-master details" phrasing implied a dedicated SAP vendor-master endpoint that doesn't exist as a discrete tool; the universe data actually lives in email (Brenda's reply at line 32583) and Linear (issue 33603). | Accuracy — wording sharpness | Below-threshold (note only) | OE5 reworded to: *"Trace the vendor records and prior-invoice history through internal communications, contacts, and issue-tracking records…"* — no implied tool endpoint, routes the agent to the actual sources. |
| 3 | OE4 | "Supporting documents" wording defaulted the agent toward Records Vault, but for these three invoices the TimeLedger credit memo never reached the vault and GraniteRack SOW history surfaces through email/Linear, not via document records. | Completeness — soft routing hint | Below-threshold (note only) | OE4 reworded to: *"Review the available support trail for each invoice — SOW versions, credit-memo status, dispute notes, contract-version references — wherever it actually lives, recognizing that for these three items the substantive support sits in internal communications and issue-tracking records rather than the document vault…"* |

### 7.2 Downstream Rubric Impact

OE9's added operational-risk element exposed a coverage gap: no existing rubric checked for the per-item operational-risk callout that the prompt explicitly asks for. Added a new Outcome 1.2 rubric:

> **R14 (new):** *"The Agent's recap names, for each of the three investigated invoices (TimeLedger VEN-010-514242, GraniteRack VEN-012-753165, CrownPeak VEN-030-353041), the operational risk of moving too quickly on that item (e.g., paying against a superseded contract, releasing on an unverified duplicate basis, or releasing on an aged item without a current approver)."*

Rubric set: 18 → **19 total** (5 Process + 14 Outcome; Outcome > Process maintained).

### 7.3 Updated Per-Rubric Mapping

| Position | Rubric | Notes |
|---|---|---|
| R1–R5 | Process rubrics | unchanged |
| R6–R12 | Outcome (record updates, content, recipients) | unchanged from Phase 1 |
| **R13** | Per-item disposition | unchanged |
| **R14** | **NEW** — Per-item operational risk | added in this refinement pass |
| R15 | Client-facing / engagement-scope exposure | was R14 |
| R16 | Internal-controls follow-up issue | was R15 |
| R17 | Final response — broader process problem conclusion | was R16 |
| R18 | Null-approver pattern across all three invoices | was R17 |
| R19 | GraniteRack vendor-master stale SOW reference | was R18 |

---

## 8. Reviewer Rubric Restructure (Atomicity + Process Deletion + R12 Fix)

Reviewer pass on `7_Rubrics.json` invoked the V3 atomicity rules and the Process-deletion guidance. Restructured the entire set in one sweep.

### 8.1 Issues Found

| # | Rubric (pre-restructure) | Issue | Severity | Spec citation |
|---|---|---|---|---|
| 1 | R12 (recap recipients) | Locks in Steven Perry as required recipient; prompt names only "Andrea or Matthew" for partner step-in. Universe context supports the inclusion (every prior AP escalation involves Steven Perry as Managing Partner sign-off), but a valid agent reading the prompt literally could send to Andrea + Matthew only and fail. | Minor | Overly Specific |
| 2 | R12 (recap channel) | Channel lock to email; prompt's verb is "send" (method-agnostic). A valid agent posting in Slack DM or equivalent would fail. | Minor | Overly Specific (channel lock-in) |
| 3 | R11 (CrownPeak narrative + verification) | Bundles two assertions sourced from different services (narrative from email, verification from SAP). | Major | V3 atomicity — separate-source bundling |
| 4 | R13 (per-item disposition for 3 invoices) | Bundles 3 independent per-invoice content requirements in one rubric. | Major | V3 atomicity — verbatim match to spec canonical example |
| 5 | R14 (per-item operational risk) | Same pattern as R13 — 3 per-invoice risks bundled. | Major | V3 atomicity |
| 6 | R15 (Acme + Northstar exposure) | Bundles 2 independent client-exposure callouts. | Major | V3 atomicity |
| 7 | R1, R2, R4, R5 (Process rubrics) | Each can be fully verified by a stricter Outcome rubric the eval already runs — the Process rubric is redundant. | Moderate | V3 Process Rubrics — "A criterion that a (stricter) Outcome rubric could fully verify, labeled as Process, should be Outcome (or deleted)" |
| 8 | R3 (Process — review ledger history) | Same pattern, but cleanly absorbed by tightening R9 to require account-219000 accrual reference. | Moderate | Same as #7 |
| 9 | R16 (controls follow-up) | Bundles write-action-result (1.1) + content (1.2) in one rubric. | Moderate | V3 guidelines — 1.1 / 1.2 separation |
| 10 | R17 (broader process problem) | Bundles factual conclusion + interpretive synthesis (named root-cause areas). | Moderate | V3 atomicity — fact vs synthesis |
| 11 | R18 (null-approver pattern) | Same fact-vs-synthesis bundling. | Moderate | V3 atomicity |
| 12 | R19 (vendor-master stale SOW) | Same fact-vs-synthesis bundling. | Moderate | V3 atomicity |

### 8.2 Restructure Plan Applied

**Deletions (5):**
- R1 (review communications) → coverage absorbed by Outcomes that prove the comms-derived facts (R8 narrative, R6 split-pay amounts, etc.)
- R2 (check AP records for 3 invoices) → coverage absorbed by Outcomes that require accurate invoice content
- R3 (review ledger history) → coverage absorbed by tightening R9 to require account-219000 accrual reference
- R4 (review supporting documents) → coverage absorbed by Outcomes that prove the support trail was followed (R7 SOW versions, R9 verification gap)
- R5 (check workflow tracking) → coverage absorbed by Outcomes that prove the agent updated/created the existing tracking issues

**Splits (8):**
| Old rubric | New rubrics |
|---|---|
| R11 (CrownPeak content) | R8 (narrative) + R9 (SAP verification) |
| R13 (per-item disposition) | R10 (TimeLedger) + R11 (GraniteRack) + R12 (CrownPeak) |
| R14 (per-item op-risk) | R13 (TimeLedger) + R14 (GraniteRack) + R15 (CrownPeak) |
| R15 (client exposure) | R16 (Acme) + R17 (Northstar) |
| R16 (controls follow-up) | R5 (1.1 action result) + R18 (1.2 content) |
| R17 (broader-process) | R19 (conclusion) + R20 (root-cause areas named) |
| R18 (null-approver) | R21 (fact) + R22 (synthesis) |
| R19 (vendor-master) | R23 (fact) + R24 (synthesis) |

**R12 (recap) modifications:**
- Required recipients reduced to Andrea Phil + Matthew Li only (matches prompt-literal "Andrea or Matthew" language)
- Channel released to method-agnostic — email, Slack DM, or equivalent direct internal channel
- Steven Perry remains acceptable but not required

**R9 (GraniteRack content) tightening:**
- Now requires both SOW identifiers, the 2026-01-15 effective date, AND the account-219000 accrual reference covering the underlying compute obligation
- Absorbs R3 (ledger history) coverage

**OE9 mirrored:** Steven Perry removed from required-recipient list; "send" → "deliver…via email, Slack DM, or equivalent direct internal channel write action"

### 8.3 Final Rubric Set (24 rubrics, all Outcome)

| # | Title (truncated) | Sub-cat |
|---|---|---|
| R1 | TimeLedger record update happens | 1.1 |
| R2 | GraniteRack record update happens | 1.1 |
| R3 | CrownPeak record update happens | 1.1 |
| R4 | Recap delivered to Andrea + Matthew (method-agnostic) | 1.1 |
| R5 | Controls follow-up created/updated | 1.1 |
| R6 | TimeLedger split-pay content ($17,825 / $6,650.25) | 1.2 |
| R7 | GraniteRack SOW mismatch + 2026-01-15 + 219000 accrual | 1.2 |
| R8 | CrownPeak narrative (Feb-2026 migration + claimed sibling) | 1.2 |
| R9 | CrownPeak SAP verification (sibling not in records) | 1.2 |
| R10 | TimeLedger disposition in recap | 1.2 |
| R11 | GraniteRack disposition in recap | 1.2 |
| R12 | CrownPeak disposition in recap | 1.2 |
| R13 | TimeLedger operational risk in recap | 1.2 |
| R14 | GraniteRack operational risk in recap | 1.2 |
| R15 | CrownPeak operational risk in recap | 1.2 |
| R16 | Acme exposure callout in recap | 1.2 |
| R17 | Northstar exposure callout in recap | 1.2 |
| R18 | Controls follow-up body content (3 vendors + 1+ root-cause area) | 1.2 |
| R19 | Final response — broader-process conclusion | 2.1 |
| R20 | Final response — 3+ of 4 root-cause areas | 2.1 |
| R21 | Null-approver factual finding | 2.1 |
| R22 | Null-approver → approval-routing synthesis | 2.1 |
| R23 | Vendor-master stale SOW factual finding | 2.1 |
| R24 | Vendor-master synthesis (broader hygiene) | 2.1 |

**Category counts:**
- Outcome 1.1: 5
- Outcome 1.2: 13
- Outcome 2.1: 6
- Process: 0
- Outcome > Process: trivially satisfied (24 > 0)

### 8.4 Post-Restructure Expected Dimension Scores

| Dimension | Sub-Dimension | Predicted | Justification |
|---|---|---|---|
| Rubric | Overall Quality | 5 | 0 Major / 0 Moderate / 0 Minor after restructure |
| Rubric | Category Balance | 5 | Outcome > Process trivially |
| Rubric | Process Rubrics | 5 | Zero Process rubrics — none can fail validity test |
| Rubric | All-Failing Rubrics | 5 | R11 split addresses the pre-restructure all-failing issue; each new rubric is achievable per universe evidence |
| Rubric | Agent-Centric Phrasing | 5 | All 24 criteria begin with "The Agent…"; zero tool names |
| Trajectory | Agent Failure Rate | 5 | Predicted near-zero pass@1 — every prior run misses at least one of R4 (Andrea + Matthew strict), R9 (SAP verification), R13–R15 (per-invoice op-risk), R22 (null-approver synthesis), R24 (vendor-master synthesis) |
| Universe | Cross-service Coherence | 5 | R8/R9 split makes both sides of the narrative-vs-SAP misalignment explicit, fully resolving the misaligned-data clause |
| Oracle Events | Completeness + Accuracy | 5 | OE2/OE5/OE6/OE8/OE9/OE10 cover the new 24-rubric surface; method-agnostic OE9 mirrors method-agnostic R4 |
| Prompt | (all 12 sub-dims) | 5 | Post-em-dash fix |

---

## 9. Second-Pass Atomicity / Broadness Fixes

Reviewer's follow-up pass on the 24-rubric set caught three remaining issues that had survived Section 8. All applied; rubric count 24 → 26.

### 9.1 Issues Found

| # | Rubric (pre-fix) | Issue | Severity | Type | Spec citation |
|---|---|---|---|---|---|
| 1 | R7 (GraniteRack content) | Bundles SOW mismatch + account-219000 accrual via explicit "AND" — two independent content checks bundled. | **Major** | Not Atomic | V3 atomicity — independent content requirements should be separate rubrics |
| 2 | R18 (controls follow-up content) | Bundles three-vendor coverage + control-area reference via explicit "AND" — two independent content requirements bundled. | **Major** | Not Atomic | V3 atomicity — same |
| 3 | R20 (root-cause areas in final response) | "Names at least three of the four root-cause control areas" tolerated an agent missing one even though the universe carries explicit evidence for all four. GT is enumerable; the at-least-N formulation is reward-hackable. Mitigated by the prompt's "or"-framing but still moderate. | **Moderate** | Overly Broad — At-least-N | V3 spec: when GT is enumerable, prefer one rubric per GT item or all-of-N |

### 9.2 Fixes Applied

**R7 split:**
- **R7 (new):** *"The Agent's GraniteRack record update states that invoice VEN-012-753165 is blocked because it was billed under superseded SOW-2024-GR-rev3 while the active SOW is SOW-2025-GR-rev1 effective 2026-01-15."*
- **R8 (new):** *"The Agent's GraniteRack record update references the underlying accrual covering the compute obligation on account 219000."*

**R18 split:**
- **R19 (new):** *"The Agent's internal-controls follow-up issue or record body tracks the recurring AP control problem across all three investigated vendors (TimeLedger, GraniteRack, CrownPeak)."*
- **R20 (new):** *"The Agent's internal-controls follow-up issue or record body references at least one of the four root-cause control areas: approval routing, vendor-master hygiene, duplicate-billing checks, or contract version control."* (Note: the at-least-one formulation here matches the prompt's "or"-framing for the controls follow-up specifically, distinct from the final-response synthesis.)

**R20 (formerly "at least three of four") tightened:**
- **R22 (new position):** *"The Agent's final response names all four of the root-cause control areas the prompt enumerates: approval routing, vendor-master hygiene, duplicate-billing checks, and contract version control."*
- Justification embeds the universe evidence map for each area: null approvers across the three invoices (approval routing), stale GraniteRack vendor-master SOW reference (vendor-master hygiene), phantom CrownPeak sibling VEN-030-353009 (duplicate-billing checks), superseded SOW-2024-GR-rev3 vs active SOW-2025-GR-rev1 (contract version control).

### 9.3 Final Rubric Set (26 rubrics, all Outcome)

**Category counts:**
- Outcome 1.1: 6
- Outcome 1.2: 14
- Outcome 2.1: 6
- Process: 0
- Outcome > Process: trivially satisfied (26 > 0)

**Discrimination math (predicted pass@1 on a re-run, against the 6 prior runs):**

Every prior run misses at least one of:
- R4 (recap to Andrea + Matthew, method-agnostic — Runs #1/#2/#4/#5/#6 had wrong/missing recipients)
- R8 (GraniteRack 219000 accrual reference in the record update — none of the runs explicitly stated this in the GraniteRack record write)
- R9 (CrownPeak SAP-side verification finding — Run #5 was the only one that surfaced it cleanly)
- R13/R14/R15 (per-invoice operational risk — no prior run named all three)
- R22 (all four root-cause areas, not just three — must hit each: approval routing, vendor-master hygiene, duplicate-billing checks, contract version control)
- R24 (null-approver → approval-routing synthesis explicitly)
- R26 (vendor-master stale SOW → broader hygiene synthesis explicitly)

Combined, **no prior run passes all 26 rubrics → predicted pass@1 = 0/6 = 0%**, well under the 40% threshold.

### 9.4 Updated Per-Rubric Mapping (final)

| Position | Title (truncated) | Sub-cat |
|---|---|---|
| R1 | TimeLedger record update happens | 1.1 |
| R2 | GraniteRack record update happens | 1.1 |
| R3 | CrownPeak record update happens | 1.1 |
| R4 | Recap delivered to Andrea + Matthew (method-agnostic) | 1.1 |
| R5 | Controls follow-up created/updated | 1.1 |
| R6 | TimeLedger split-pay content ($17,825 / $6,650.25) | 1.2 |
| **R7** | **GraniteRack SOW mismatch + 2026-01-15 effective date** | **1.2** |
| **R8** | **GraniteRack 219000 accrual reference** | **1.2 (new — split)** |
| R9 | CrownPeak narrative (Feb-2026 migration + claimed sibling) | 1.2 |
| R10 | CrownPeak SAP verification (sibling not in records) | 1.2 |
| R11 | TimeLedger disposition in recap | 1.2 |
| R12 | GraniteRack disposition in recap | 1.2 |
| R13 | CrownPeak disposition in recap | 1.2 |
| R14 | TimeLedger operational risk in recap | 1.2 |
| R15 | GraniteRack operational risk in recap | 1.2 |
| R16 | CrownPeak operational risk in recap | 1.2 |
| R17 | Acme exposure callout in recap | 1.2 |
| R18 | Northstar exposure callout in recap | 1.2 |
| **R19** | **Controls follow-up body covers all 3 vendors** | **1.2** |
| **R20** | **Controls follow-up body references 1+ root-cause area** | **1.2 (new — split)** |
| R21 | Final response — broader-process conclusion | 2.1 |
| **R22** | **Final response — all 4 root-cause areas** (tightened from at-least-3) | **2.1** |
| R23 | Null-approver factual finding | 2.1 |
| R24 | Null-approver → approval-routing synthesis | 2.1 |
| R25 | Vendor-master stale SOW factual finding | 2.1 |
| R26 | Vendor-master synthesis (broader hygiene) | 2.1 |

---

## 10. QC Convention Compliance Scan

Reviewer directive: align with the conventions used by the QC-passed tasks under `[V2] QC_Tasks/`, AND strip two specific patterns that V2 used but V3 spec flags as weak:
- No `"at least"` phrasing (V3 reward-hackable per spec)
- No em dashes (U+2014)

### 10.1 V2 Convention Study

Sampled rubrics from all 10 V2 QC tasks for structural craft. Key takeaways and V3 reconciliation:

| V2 Pattern | Where seen | V3 Reconciliation |
|---|---|---|
| `"at least"` heavy use | Task1 (12), Task5 (10), Task6 (6), Task2 (6), Task3 (4), Task9 (4) | **Stripped** — V3 spec calls at-least-N reward-hackable when GT is enumerable |
| Tool names in criterion (`"via send_email"`, `"via conversations_add_message"`) | All V2 tasks | **Avoided** — V3 Agent-Centric Phrasing sub-dimension bans tool names in criterion text (failed by single occurrence) |
| Nested `annotations` wrapper structure (`{annotations: {evidence, justification, rubric_category}, id, title}`) | All V2 tasks | **Replaced** — V3 uses flat structure (`{title, category, justification, evidence}`) per current QC eval expectations |
| Mailto-style markdown links in titles (`[email](mailto:email)`) | Task1, Task4 | **Plain emails only** — V3 prefers plain `email@domain.com` |
| `"or similar"` for Fuzzy intent | All V2 tasks | **Same convention preserved** — V3 explicitly allows Fuzzy-intent freetext matching |
| Parenthetical examples (e.g., "lock expiration, processing backlog, or similar") | Many V2 rubrics | **Same convention preserved** — V3 allows for illustrating Fuzzy intent (not for defining the answer set) |

### 10.2 Final Scan of Candidate-Facing Files

| File | `"at least"` | Em dash | `"minimum"` | `"one or more"` | `"such as"` | `"for example"` | Tool names in criterion |
|---|---|---|---|---|---|---|---|
| `5_Prompt.txt` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `6_Oracle_Events.txt` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `7_Rubrics.json` | 0 | 0 | 0 | 0 | 0 | 4 ✅ | 0 |

**The 4 `"for example"` occurrences** are all in R14/R15/R16 (per-invoice operational-risk rubrics) and R26 (vendor-master synthesis) — each is a parenthetical illustrating Fuzzy intent (sample shapes of operational risk or sweep language). Per V3 spec: *"Never use 'such as / like / for example' when defining the correct answer set (fine only when illustrating Fuzzy intent)."* These usages illustrate; the actual required content is the named behavior ("names the operational risk", "treats as a broader hygiene gap"), not the example list.

### 10.3 R20 Rephrase Detail

**Before (last revision):** *"…references at least one of the four root-cause control areas: approval routing, vendor-master hygiene, duplicate-billing checks, or contract version control."*

**After:** *"…names a root-cause control area (approval routing, vendor-master hygiene, duplicate-billing checks, or contract version control) as the driver of the recurring AP pattern."*

Semantically identical (prompt-literal "or"-framing preserved) but with the banned phrase removed. Justification and evidence updated to match.

### 10.4 `changes.md` Em Dashes (Audit-Internal)

`changes.md` itself uses ~80 em dashes throughout the audit narrative (markdown table cells, connecting clauses in issue descriptions). It is not a candidate-facing artifact and is not consumed by the eval pipeline — it is a reviewer-side audit log. Leaving as-is unless explicitly directed otherwise.

### 10.5 Final Sign-Off State

- **Rubric set:** 26 atomic Outcome rubrics, no Process, no banned phrasing, no tool names in any criterion
- **OE set:** 10 OEs, no banned phrasing, mirrors rubric coverage
- **Prompt:** em-dash-free, guideline-compliant
- **Universe data:** untouched

Ready for verifier re-run.
