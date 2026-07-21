# QC Score-3 Knowledge Extract (Tasks 25–37)

Consolidated QC failure dimensions from 13 score-3 tasks. All tasks scored 3 (non-fail) — these are quality issues the eval should catch pre-submission. Folders deleted after extraction.

---

## Summary by QC Dimension

| QC Dimension | Tasks Affected | Count |
|-------------|----------------|-------|
| Non-Atomic / Overlapping Rubrics | Task26, Task27, Task29 | 3 |
| Missing Outcome Criteria | Task25, Task28, Task30, Task37 | 4 |
| Inaccurate Oracle Events | Task26, Task31, Task33 | 3 |
| Incomplete Oracle Events | Task27, Task30 | 2 |
| Minor OE Inaccuracies | Task27, Task28, Task31 | 3 |
| Missing Process Rubric | Task26, Task28, Task36 | 3 |
| Overlapping / Redundant Criteria | Task32 | 1 |
| Overly Broad Criteria | Task35 | 1 |
| Rubric Wording Errors | Task35 | 1 |
| Minor Clarity / Specificity Issues | Task29, Task32, Task34 | 3 |
| Incorrectly Labeled Category | Task26 | 1 |

---

## Per-Task Detail

### Task25 — 6a36c0aa995298e63c9de7af | Accounting Operations
**QC Dimensions:** Up to 10% Major Errors
**Issue:** Missing criterion checking if the reconciliation has changed since sending the request to Daniel. Prompt and universe were clean — purely a rubric coverage gap.

---

### Task26 — 6a34f0d20a48e0f70232d235 | BlackLine Close-Discipline & Variance
**QC Dimensions:** Up to 15% Moderate Errors, Inaccurate Oracle Events, Missing Process Rubric
**Issues:**
- R13 not atomic — bundles updating a note AND keeping the status in one criterion. Also overlaps with R17 on the note update.
- R25 describes a verification behavior but mislabeled as outcome (should be process).
- OE1, OE2, OE11 treat a document reference incorrectly.

---

### Task27 — 6a34ca4ecb481794fca00da1 | Engagement Mgmt & Client Operations
**QC Dimensions:** Up to 10% Major, Up to 15% Moderate, 5-20% Minor, Incomplete OEs, Minor OE Inaccuracies
**Issues:**
- OE5 missed checking BL review notes for BL-C3D4E5F6A7B8 and BL-D4E5F6A7B8C9.
- OE14 states only items 3 and 4 have SOX implications, but OE4 established item 2 also does.
- OE15 should post to compliance-and-registration Slack channel per prompt ("the compliance team needs to be notified").

---

### Task28 — 6a3182d8e98f265303e151a2 | Audit
**QC Dimensions:** Missing Process Rubric, Up to 10% Major Errors, Minor OE Inaccuracies
**Issues:**
- 3 missing process rubrics: (1) discovering active items in Close Blocker Triage Log via Airtable, (2) checking underlying reconciliations in BlackLine, (3) looking up 4 affected GL accounts in Oracle GL.
- Major: missing criterion for a key finding.

---

### Task29 — 6a32621a5f3d2b59f9364ca2 | BlackLine Close-Discipline & Variance
**QC Dimensions:** Minor Clarity/Specificity Issues, Up to 10% Major Errors
**Issues:**
- C12 is non-atomic — bundles 6+ independent claims: email sent to Daniel+Ryan, Andrea CC'd, body states Helix Bio misclassification root cause, body says it wasn't the $9.56 rounding, body states corrective JE direction/amount (Dr 241000 / Cr 240000 for $18,412.04), body states JE submitted for approval.

---

### Task30 — 6a2dd32ea47a48dbc719523c | Accounting Operations
**QC Dimensions:** Incomplete Oracle Events
**Issues:**
- None of the OEs name the tool or parameters that should be used.
- OE13 missed stating the duplicate ~$74,220 of entries 0049 and 0043.
- Missing outcome criteria for Daniel Jones email summary: $2,550 cloud true-up shortfall (actual $21,300 vs $18,750 accrued), ~$194,850 duplicate revenue release.

---

### Task31 — 6a2dbcac3d95fe4eb6041bed | HR & People Operations
**QC Dimensions:** Inaccurate Oracle Events, Minor OE Inaccuracies
**Issues:**
- OE5 missing inclusion of Daniel Jones and Margot Reyes in emails from March to May.
- OE1 states it needs to pull contact details for Yusuf and Reshma for write actions, but their emails aren't actually needed per the prompt. OE11 is not needed to satisfy the prompt.

---

### Task32 — 6a2c8eeb219bdaea0af79de7 | Compliance & Internal Controls
**QC Dimensions:** Up to 15% Moderate Errors, Minor Clarity/Specificity Issues
**Issues:**
- C5, C9 restate facts the prompt presents as given premises rather than things the agent must discover. Overlapping/redundant — checking things already stated in the prompt as background context.

---

### Task33 — 6a2c363d93e5f48806f56502 | AP / Vendor Operations
**QC Dimensions:** Inaccurate Oracle Events
**Issues:**
- The subledger AP invoices table is empty, so OE1's reference to using the AP tool would not provide the expected information. OE references data that doesn't exist in the universe.
**Failing Rubrics:** R1 (amount determination $9,069.60), R5 ($4,000 unapplied overpayment credit), R6 ($1,815.40 disallowed add-on module), R9+.

---

### Task34 — 6a29f21ab1491944f25590b1 | Accounting Operations
**QC Dimensions:** Minor Clarity/Specificity Issues, Up to 10% Major Errors
**Issues:**
- Prompt says "give them a polite nudge" — communication channel unspecified (email vs Slack vs DM). Classic channel ambiguity.

---

### Task35 — 6a269bb29f66f3cd90ea035d | Tax
**QC Dimensions:** 5-20% Minor Errors, Up to 15% Moderate Errors
**Issues:**
- Rubric wording errors: C9, C10, C11 mention "Ming Chang 1" (extra "1" is a typo).
- C11 is overly broad — tests "not ready for release" recommendation but the quantifier is looser than needed.
**Failing Rubrics:** R1 (SALT accrual shortfall ~$2,800 vs $4,820.30 posted), R3 ($504.80 R&D credit), R5 (reverse/rebook Tom's placeholder JE).

---

### Task36 — 6a26af7cea851736c2413a34 | AP / Vendor Operations
**QC Dimensions:** Missing Process Rubric
**Issues:**
- R3 should be process (checks invoice details for vendor identification).
- R4 should be process (checks duplicate invoice identification).
- R7 should be process (checks recognition of additional approval requirement).

---

### Task37 — 6a26858be4c3e50c45930d74 | AP / Vendor Operations
**QC Dimensions:** Up to 10% Major Errors
**Issues:**
- Missing outcome criterion: OE24 requires updating the Linear handoff issue to add NovaCrest as omitted item. R20 only checks the agent reports the omission in final response, not that the agent actually updated/commented on the Linear issue. Missing 1.1 write-action rubric.
**Failing Rubrics:** R20 (NovaCrest gap in Linear handoff issue).

---

## Key Patterns for Eval Improvement

1. **Non-atomic criteria** (Task26, Task29) — bundling independent checks remains the top rubric defect.
2. **Missing outcome criteria for email/response content** (Task25, Task30, Task37) — CBs create write-action rubrics but miss content coverage.
3. **OE references to empty/non-existent data** (Task33) — OEs reference AP invoices that don't exist in the universe.
4. **Channel ambiguity not flagged** (Task34) — prompt says "nudge" without specifying channel; eval should flag this.
5. **Rubric wording typos** (Task35) — "Ming Chang 1" should be caught by a surface-level review.
6. **Redundant criteria restating prompt premises** (Task32) — rubrics checking things the prompt already stated as given context.
7. **Process vs Outcome mislabeling** (Task26, Task36) — verification behaviors labeled as outcomes.
