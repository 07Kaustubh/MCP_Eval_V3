# Changes Tracker — Task 24_6a36e84723508b4e3f391cfc

**Task:** AP / Vendor Operations — pending-approval queue triage across Brookfield + Northstar Legal + Acme Cloud (compound age x outstanding $ ranking)
**Persona:** Lena Park (Procurement Officer)
**Business Function:** AP / Vendor Operations
**Reviewer:** QC reviewer (REVIEW flow that branched to REDO)
**Date opened:** 2026-06-21

---

## Baseline QC Snapshot (candidate submission, before any fixes)

| Dimension | Sub-Dimension | Initial Rating | Notes |
|---|---|---|---|
| Prompt | Unique Ground Truth | 4-5 | Categories and ownership defined; single end-state |
| Prompt | Feasibility / Explicit Tool Mention / Clarity | 4-5 | Narrative sound, no tool names, single coherent scenario |
| Prompt | Contrived / Truthfulness | 4-5 | Reads natural; minor Truthfulness wording risk on the "was patched" assertion, but defensible under design-intent reading |
| Prompt | Cross-service requirement | **3** | Reads spanned multiple services but only one write surface (Slack) was mandated |
| Prompt | Investigation | 4 | Required investigation but a shallower one than the framework targets |
| Prompt | Persona / Business Function / Alignment with Today | 5 | Lena Park, AP/Vendor Ops, 2026-06-12 all coherent |
| Universe | Data Exists (Universe Feasibility) | **2** | One rubric named an Acme Cloud `engagement_letter` document that does not exist in the universe (Acme's scope is split across `engagement_letter_addendum` doc_eb7cb30c59bd4f03 and `engagement_change_order` doc_2d85ac5a698745c5). Phantom-atom defect failed 3 of 6 agents for a rubric problem rather than a model gap. |
| Oracle Events | Coverage | 3 | Covered the critical path but only as far as the single-write surface |
| Rubrics | Atomicity / Self-containment / Phrasing | 4-5 | Mostly clean atomic outcome rubrics |
| Rubrics | Truthfulness / Grounding | **2** | Phantom atom on Acme engagement_letter (see Universe row above) |
| Trajectory | Tool Call Count (binding gate) | **2** | Measured avg 32.5 tool calls per run across 6 runs vs the 40 floor |
| Trajectory | Agent Failure Rate | 5 | pass@1 = 16.7% (within 40% ceiling) |
| Trajectory | Error Rate | 5 | 0 errored runs |

**Initial overall (grade-to-lowest):** **2 (Fail)**, capped by Universe → Data Exists (phantom atom) and Trajectory → Tool Call Count (32.5 vs 40 floor).

---

## Universe Verification Performed

Verified against `_aux/Universe_Split/*.json` (per-task split via `Validators/split_universe.py`) and recorded in `_aux/Fact_Ledger.json`:

- **320 of 320 pending_approval invoices** carry `approver = null` across all three entities. Systemic orphan-approver fingerprint confirmed.
- **3 scope documents exist, all `classification = restricted`**: `doc_eb7cb30c59bd4f03` (Acme addendum), `doc_2d85ac5a698745c5` (Acme change order), `doc_0036f5b991574808` (Northstar engagement letter). Zero access grants for Lena Park on any of them (verified 0 of 184 grants).
- **No Acme Cloud document of kind `engagement_letter`** exists. The candidate's rubric that required one is grounded in a non-existent atom.
- **Vendors confirmed**: GraniteRack Compute Services VEN-012-753165 ($39,090.56, deprecated SOW-2024-GR-rev3 vs active SOW-2025-GR-rev1), TimeLedger Nexus VEN-010-514242 ($24,475.25, Phase-3 missing credit memo, distinct from VEN-010-693199 W-9 hold), Pinecrest Workflow Works VEN-006-193120 ($1,040.63, 338 days, brookfield, active vendor dispute), CivicSquare Property Management VEN-024-891664 ($289,217.86, 302 days), VaultKey Access & Security VEN-029-961721 ($460,556.46, single largest dollar item), MetroShield Facility Services VEN-012-745157 / VEN-012-786680 / VEN-012-730094 (all dated 2026-05-31), VerityFile E-Sign Services VEN-028-492596 (dated 2026-05-18) — all present.
- **Linear tracking issue** `issue_378874ffeb8f4cb0b0417021f2d3d647` (Fix AP routing rule for departed approvers and sweep orphaned pending approvals) is `state = todo`, due 2026-05-22, assignee Mateo (npc_024). Linear cross-reference issues for GraniteRack (`issue_e5abbb9af74642eeb10a93426b0bbaa2`) and TimeLedger (`issue_e6fbc488077344c28cc7cd13640c54bc`) exist.
- **GL account split**: 210000 = AP - External Vendors (in scope), 219000 = AP - Employee Reimbursements (out of scope), confirmed across all three entities.

---

## Findings & Fixes

### Finding F-001 — Phantom atom on Acme Cloud `engagement_letter` [REBUILT]

- **File:** `7_Rubrics.json` (candidate version) + `5_Prompt.txt` (candidate version)
- **Issue:** The candidate's prompt and rubric expected the agent to find an Acme Cloud `engagement_letter` document in Records Vault. That kind does not exist for Acme in the universe. Acme's scope is split across `engagement_letter_addendum` doc_eb7cb30c59bd4f03 and `engagement_change_order` doc_2d85ac5a698745c5.
- **Impact:** 3 of 6 candidate runs failed this rubric not because the agent missed a reasoning step, but because the rubric named a non-existent atom. Classic Universe Feasibility violation.
- **Issue type:** Major Issue per `Docs/8_QC_Spec_Doc2.md` → "Universe Feasibility (Data Exists)" → "Fail - Missing Universe Data."
- **QC sub-dimension impacted:** Universe → Data Exists. Cascades to Rubrics → Truthfulness / Grounding.
- **Fix applied (via REDO rebuild):** New rubric set expects the agent to source Acme scope from the addendum + change order specifically, and to handle the restricted classification honestly (zero access grants for Lena, so the agent reports "exists, content access-gated" rather than "missing"). Northstar scope sources to the single executed engagement letter doc_0036f5b991574808.
- **Status:** Done (REDO rebuild).

### Finding F-002 — Trajectory density below floor [REBUILT]

- **Files:** `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json` (candidate versions)
- **Issue:** Candidate trajectories averaged 32.5 tool calls per run across 6 runs versus the 40 floor. Root cause: only one write action mandated (the Slack post). No Linear comment, no email draft, no reminder, no per-vendor cross-service diagnosis chain.
- **Impact:** Binding gate failure on Trajectory → Tool Call Count.
- **QC sub-dimension impacted:** Trajectory → Tool Call Count.
- **Fix applied (via REDO rebuild):** New prompt mandates four distinct write actions across four services (Slack post to C010 + Linear comment on the existing AP-routing orphan-approver tracking issue + email draft to Daniel Jones with Steven Perry on cc + 7-day follow-up reminder) plus a per-vendor 3-link diagnosis chain (SAP detail + Linear lookup + email escalation cross-reference for the top 3-5 worst offenders). Rebuilt OE 1 through OE 22 to cover the new surface. Rebuilt 24-rubric set (all Outcome) to verify each write action and each per-vendor classification.
- **Status:** Done (REDO rebuild). Post-rebuild trajectories: cycle 1 avg 68.7 tool calls, cycle 2 avg 60 tool calls. Both well above the 40 floor.

### Finding F-003 — Cross-service requirement (single write surface) [REBUILT]

- **File:** `5_Prompt.txt` (candidate version)
- **Issue:** Reads spanned multiple services but only one write surface was mandated, weakening the cross-service signal.
- **QC sub-dimension impacted:** Prompt → Tool use and Cross-service requirement.
- **Fix applied (via REDO rebuild):** Same as F-002. Four writes across four services lifts the cross-service score to 5.
- **Status:** Done (REDO rebuild).

### Finding F-004 — Compound ranking lens missing (smaller polish) [REBUILT]

- **File:** `5_Prompt.txt` (candidate version)
- **Issue:** Candidate ranked worst offenders by a fixed 60-day SLA window. A top-dollar-heavy agent could pass without engaging the harder long-aged-mid-dollar items.
- **Fix applied (via REDO rebuild):** Prompt now mandates compound (age in days x outstanding dollars) ranking with explicit anti-latch on VaultKey ($460,556.46 single-largest-dollar but not the most severe under compound). Surfaces CivicSquare, Clearpoint, and the long-aged mid-dollar tail that would otherwise drift past.
- **Status:** Done (REDO rebuild).

### Finding F-005 — Single-entity scope verification (smaller polish) [REBUILT]

- **File:** `5_Prompt.txt` (candidate version)
- **Issue:** Candidate only required scope verification on one managed-client entity (Acme), exercising only half the discovery surface.
- **Fix applied (via REDO rebuild):** Prompt now mandates scope verification on both Acme Cloud and Northstar Legal, forcing multi-doc-kind search (`engagement_letter` + `engagement_letter_addendum` + `engagement_change_order`).
- **Status:** Done (REDO rebuild).

### Finding F-006 — Truthfulness wording polish on routing-fix anchor [PATCHED]

- **File:** `5_Prompt.txt`, `6_Oracle_Events.txt` (OE 15), `7_Rubrics.json` (R7 + R22)
- **Issue:** Post-rebuild draft prompt asserted "Daniel posted... was patched last sprint". Under strict-literalist reading of QC Spec Truthfulness 5 ("no misleading statements"), this is a completed-action assertion that the universe contradicts (Daniel's actual Slack message attributes routing fix ownership to Mateo as in-progress, not as completed). Defensible under the project's design-intent reading (L9 authority-dismissal lever is sanctioned), but vulnerable to a strict reviewer.
- **Fix applied:** Swapped the verb from "was patched last sprint" to "was supposed to land last sprint", with cascading consistency updates: "whether that held" -> "whether it actually landed", "after that patch" -> "after that target". OE 15 picked up "held" -> "landed", "after the patch" -> "after the target", "did not hold" -> "did not land". Rubrics R7 + R22 picked up the same vocabulary swap in title / justification / evidence fields. Full diff in `_aux/Prompt_Truthfulness_Fix.md`.
- **Impact on hardness:** R22 fail rate moved from 3/6 (50%) to 2/6 (33%), still in the 30-50% effective stump band. L9 lever firing preserved.
- **Status:** Done (patched on top of REDO rebuild).

---

## REBUILD Path

Per `Reference/Sessions/REVIEW.md` decision table, the candidate hit two REBUILD triggers:

1. Universe → Data Exists scored 2 (phantom atom on Acme engagement_letter).
2. Trajectory → Tool Call Count scored 2 (avg 32.5 vs 40 floor).

Verdict: REBUILD. Recommend `PIPELINE REDO`. Original candidate deliverables archived to `_aux/Candidate_Originals/`. No `14_Updated_Oracle_Events.txt` / `15_Updated_Rubrics.json` emitted because the rebuild replaced rather than patched the deliverables (Applied rows would not be the right model here).

---

## Post-Rebuild + Post-Truthfulness-Fix QC Snapshot

| Dimension | Sub-Dimension | Final Rating |
|---|---|---|
| Prompt | Unique Ground Truth | 5 |
| Prompt | Feasibility | 5 |
| Prompt | Explicit Tool Mention | 5 |
| Prompt | Clarity / Specificity | 5 |
| Prompt | Contrived / Unnatural | 5 |
| Prompt | Truthfulness | 5 (clean under both strict-literalist and design-intent readings) |
| Prompt | Cross-service requirement | 5 (four writes across four services) |
| Prompt | Investigation | 5 |
| Prompt | Coherence | 5 |
| Prompt | Persona / Business Function | 5 |
| Prompt | Alignment with Today | 5 |
| Universe | Data Exists | 5 (27 of 27 atoms verified; phantom atom removed) |
| Oracle Events | Coverage | 5 (22 OEs cover all four writes + per-vendor 3-link chain + scope verification) |
| Rubrics | Quality | 5 (24 atomic Outcome rubrics, all self-contained, all grounded in Fact_Ledger) |
| Trajectory | Tool Call Count | 5 (cycle 1 avg 68.7, cycle 2 avg 60; both above the 40 floor) |
| Trajectory | Agent Failure Rate | 5 (pass@1 = 0/6 in both cycles, within the 40% ceiling) |
| Trajectory | Error Rate | 5 (0 errored runs across both cycles) |

**Final overall (grade-to-lowest):** **5 (Excellent Per QC Spec)** across all applicable sub-dimensions.

FINAL council verdict: PASS (re-run after the Truthfulness fix; 0 BLOCKERs, 0 MAJORs, 2 advisory MINORs about the VerityFile post-target example).
S4 verdict (both cycles): SHIP.
PIPELINE COMPARE: platform rubrics match local (no silent mutations).
