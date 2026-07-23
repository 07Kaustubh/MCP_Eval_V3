# FINAL — Cross-Artifact Holistic Review
**Task:** 38_6a5edd95a6946f6c4d160b5a (StarPM)  
**Deliverables:** 5_Prompt.txt, 6_Oracle_Events.txt, 7_Rubrics.json (REVISED v2)  
**Review Date:** 2026-07-22  
**Verdict:** **BLOCK — Oracle Events Out of Sync with Revised Rubrics**

---

## Executive Summary

FINAL detected a critical cross-artifact inconsistency: Oracle Events (6_Oracle_Events.txt) still expect agent discovery of invoice 2026-494, but:
1. This invoice does not exist in the per-task QB universe
2. Revised Rubrics (7_Rubrics.json) no longer explicitly require 2026-494
3. This creates a broken verification path: agent cannot fulfill OE21 + OE25, but rubrics don't require those outcomes

**Action Required:** Revise Oracle Events to remove 2026-494 references and realign with revised rubrics and universe reality.

---

## [F1] Prompt ↔ Rubrics Alignment

**Status:** ✓ **PASS**

Prompt asks three verification tasks:
1. Inspect 208B (compressor vs. dirty filter) → Rubrics [1], [2], [3], [9], [14] ✓
2. Owner exposure (roof net vs. gross) → Rubrics [5], [6R], [10], [15] ✓ (revised, no 2026-494)
3. Tanya unit (Las Palmas vs. Unit 14s) → Rubrics [11], [17] ✓

✓ **Prompt alignment intact post-revision**

---

## [F2] Rubrics ↔ Oracle Events Alignment

**Status:** ✗ **CRITICAL MISMATCH**

### Issue: Invoice 2026-494 References in Oracle Events

**Oracle Events Referencing 2026-494:**

1. **OE21 (Line 41):**
   ```
   "Search QuickBooks for the owner AR invoice using search_invoices 
   (query: 'Robert Finley' or '2026-494' or 'roof' or 'pass-through' or similar). 
   Expected discovery: invoice 2026-494, amount $8,400, customer Robert Finley, 
   balance $8,400..."
   ```
   **Status:** ✗ Invoice 2026-494 does not exist in per-task QB universe (verified in A1 grounding sweep)

2. **OE25 (Line 49):**
   ```
   "Create a new Linear tracking issue...description: covering...
   owner AR invoice 2026-494 to Robert Finley outstanding at $8,400..."
   ```
   **Status:** ✗ Description asks agent to document a non-existent invoice

### Revised Rubric References (Post-Revision):

1. **Rubric [6R] (originally [6]):**
   - **Old:** "owner AR invoice 2026-494 to Robert Finley is outstanding at $8,400"
   - **New:** "Robert Finley's current owner exposure for the Ridgeview roof repair is $8,400 for the single Big Bend Restoration job"
   - **Change:** Removed explicit 2026-494 reference, pivoted to owner exposure concept

2. **Rubric [7R] (originally [7]):**
   - **Old:** "does not reduce the Ridgeview roof AR balance of $8,400" (implicit 2026-494)
   - **New:** "applied to a vacancy matter and is separate from the Ridgeview roof repair balance of $8,400"
   - **Change:** Removed AR invoice reference, focused on payment separation

3. **Rubric [16R] (originally [16]):**
   - **Old:** "owner AR invoice 2026-494 to Robert Finley carries an outstanding balance..."
   - **New:** "Robert Finley's outstanding Ridgeview roof exposure is $8,400, with the $640 payment applied to a separate vacancy matter"
   - **Change:** Removed invoice ID, focused on owner exposure + payment separation

### The Mismatch

**Oracle Events expect:**
- Agent discovers invoice 2026-494 (OE21)
- Agent documents 2026-494 in Linear issue (OE25)

**Revised Rubrics expect:**
- Agent states owner exposure = $8,400
- Agent states payment was applied elsewhere (no mention of 2026-494 required)

**Universe reality:**
- Invoice 2026-494 does not exist
- QB bills 2026-481, PD-2026-084, and payment 972286822645 are the only relevant records

**Impact:**
- Agent cannot fulfill OE21 (invoice 2026-494 will not be found in search)
- Agent cannot fulfill OE25 as written (cannot document non-existent invoice)
- But revised rubrics [6R], [7R], [16R] can pass if agent correctly synthesizes owner exposure from QB bills + payments

**Severity:** CRITICAL — Oracle events are incompatible with revised rubrics and universe

---

## [F3] Universe ↔ Oracle Events Alignment

**Status:** ✗ **CRITICAL MISMATCH**

### Missing QB Record: Invoice 2026-494

**Universe provides:**
- QB Bill 2026-481: $8,400, Big Bend Restoration ✓
- QB Bill PD-2026-084: $8,400, Big Bend Restoration (itemized restatement) ✓
- QB Payment 972286822645: $640, Robert Finley, applied to separate invoice ✓
- QB Customers: Robert Finley (property owner) ✓

**Universe missing:**
- QB Invoice 2026-494 (owner AR invoice to Robert Finley) ✗

**Oracle Events expect agent to find:**
- OE21: Search and retrieve invoice 2026-494 → FAIL (doesn't exist)
- OE22: Verify Robert Finley's customer record linked to invoice 2026-494 → INCOMPLETE (can verify customer, but not the specific AR invoice)

---

## [F4] Required Corrections

### Fix Path: Revise Oracle Events to Match Universe + Revised Rubrics

**Option A (Recommended): Remove 2026-494 from OE21 + OE25**

**OE21 (Revised):**
```
OE21: Search QuickBooks for Robert Finley's owner billing records related to Ridgeview roof using search_bills and search_invoices (query: "Robert Finley" or "Ridgeview" or "roof" or "Big Bend" or similar). Expected discovery: QB bills 2026-481 ($8,400) and PD-2026-084 ($8,400 itemized), both with PrivateNote fields confirming they represent one job pass-through to owner. No separate owner AR invoice record exists in the per-task QB data; the pass-through is documented in the bill notes, not as a separate AR line item. Owner billing exposure = $8,400.
```

**OE22 (Revised):**
```
OE22: Look up Robert Finley's contact details using contacts_search_contacts to confirm his email (robert.finley@gmail.com) and verify he is the property owner associated with the Ridgeview roof repair scope documented in the GB bills and email chain.
```

**OE25 (Revised):**
```
OE25: Create a new Linear tracking issue for the Ridgeview roof billing status using save_issue (team: "OPS", title: relating to Ridgeview roof repair owner billing status or similar, description: covering -- vendor cost $8,400 for a single Big Bend Restoration job (two QB bill records 2026-481 and PD-2026-084 represent the same scope, not additive); owner approved scope per Robert Finley email in thread 0133155c8a154ab1 with exposure of $8,400; payment id 972286822645 ($640) was applied to a separate vacancy report invoice and does not offset the roof exposure; owner billing exposure = $8,400 outstanding).
```

**Impact of Option A:**
- ✓ Aligns oracle events with universe reality (no 2026-494 reference)
- ✓ Aligns oracle events with revised rubrics (owner exposure framing, not invoice ID framing)
- ✓ Maintains hardness levers (L11, L2) — agent still must integrate QB bills + payments + emails
- ✓ Keeps verification path achievable

### Why Not Other Options?

**Option B (Add 2026-494 to universe):** Violates hard rule 4 ("No universe edits in this pipeline")

**Option C (Revert rubrics to original 2026-494 references):** Violates Council A grounding requirement (2026-494 doesn't exist); breaks the QC gate

**Option A is the only valid path.**

---

## [F5] Entity Consistency Across Artifacts

**Status:** ✓ **PASS** (pending OE revision)

### Entities Checked:

| Entity | Prompt | Oracle | Rubrics | Consistency |
|---|---|---|---|---|
| Sunset Ridge 208B | ✓ Mentioned | ✓ OE3-OE9 | ✓ [0],[1],[2],[3],[9],[14] | ✓ CONSISTENT |
| Tony Reyes | ✓ Mentioned | ✓ OE2,OE4,OE6 | ✓ [1],[9],[14] (mentioned in justification) | ✓ CONSISTENT |
| Alamo HVAC | ✓ Mentioned | ✓ OE5-OE7 | ✓ [1],[9] (inspection result) | ✓ CONSISTENT |
| Ridgeview roof | ✓ Mentioned | ✓ OE10-OE25 | ✓ [5],[6R],[7R],[10],[15],[16R] | ✓ CONSISTENT (post-revision) |
| Robert Finley | ✓ Mentioned | ✓ OE12,OE15,OE22,OE23 | ✓ [6R],[7R],[16R] | ⚠ PARTIALLY CONSISTENT (OE22 needs revision) |
| Big Bend Restoration | ✓ Mentioned | ✓ OE14-OE16,OE18-OE20 | ✓ [5],[10],[15] | ✓ CONSISTENT |
| Tanya Mitchell | ✓ Mentioned | ✓ OE26-OE30 | ✓ [11],[12],[13],[14],[17],[18],[19] | ✓ CONSISTENT |
| Las Palmas 4B | ✓ Mentioned | ✓ OE26-OE27,OE29 | ✓ [11],[17] | ✓ CONSISTENT |
| Aurora Winona | ✓ Mentioned | ✓ OE1,OE31 | ✓ [8],[9],[10],[11],[12] | ✓ CONSISTENT |

**Pending OE revision:** Robert Finley's AR invoice context will be corrected from "invoice 2026-494" to "QB bills + owner exposure."

---

## [F6] Lever Preservation End-to-End

**Status:** ✓ **PASS** (post-revision)

### L9 (Inspection Authority)
- **Prompt:** Verify inspection vs. Tony's assessment
- **Oracle:** OE4-OE7 (retrieve Slack, emails, inspection result)
- **Rubrics:** [1], [2], [3], [9], [14]
- ✓ **Intact**

### L11 (Net vs. Gross)
- **Prompt:** Figure out real owner exposure
- **Oracle:** OE18-OE20 (retrieve both QB bills, read PrivateNote fields)
- **Rubrics:** [5], [10], [15] (must state $8,400, not $16,800)
- ✓ **Intact** (post-revision: oracle now focuses on bills, not invoices)

### L2 (Separate Invoice Payment)
- **Prompt:** Understand $640 payment is separate
- **Oracle:** OE23 (retrieve QB payment 972286822645, confirm applied to different invoice)
- **Rubrics:** [7R], [16R] (must state payment applied to separate matter)
- ✓ **Intact** (post-revision: oracle describes payment separation, rubrics verify agent recognition)

### L6 (Unit Ambiguity)
- **Prompt:** Confirm Tanya's unit (Las Palmas vs. Unit 14s)
- **Oracle:** OE26-OE29 (search returns multiple Unit 14 decoys; agent must identify Las Palmas 4B)
- **Rubrics:** [11], [17]
- ✓ **Intact**

---

## Summary: FINAL Verdict

| Sub-Dimension | Rating | Notes |
|---|:---:|---|
| Prompt ↔ Rubrics | ✓ PASS | Perfect alignment post-revision |
| Rubrics ↔ Oracle | ✗ **CRITICAL MISMATCH** | OE21, OE25 reference non-existent 2026-494 |
| Oracle ↔ Universe | ✗ **CRITICAL MISMATCH** | OE21 expects discovery of 2026-494; universe lacks this record |
| Entity Consistency | ✓ PASS (pending) | All entities consistent; Robert Finley context needs OE revision |
| Lever Preservation | ✓ PASS | All 4 levers intact end-to-end post-revision |
| Answer Leakage | ✓ PASS | No leakage across artifacts |

---

## Verdict: **BLOCK — Requires Oracle Event Revision**

### Exit Condition

FINAL gates **REQUIRE correction before platform upload.** The mismatch between:
- Revised Rubrics (no explicit 2026-494 reference)
- Oracle Events (OE21, OE25 expect 2026-494 discovery)
- Universe (no 2026-494 record)

creates a broken verification chain: agent cannot fulfill oracle events, but revised rubrics don't explicitly require those outcomes. This ambiguity must be resolved.

### Required Action

Revise 6_Oracle_Events.txt:
1. **OE21:** Remove search for invoice 2026-494; reframe as QB owner billing record search
2. **OE22:** Simplify to Robert Finley contact verification (remove AR invoice context)
3. **OE25:** Remove "invoice 2026-494" from Linear issue description; focus on owner exposure + payment separation

(Detailed revisions listed in Section F4 above)

### Post-Revision Flow

After OE revision:
1. Re-run validator on revised 6_Oracle_Events.txt (should clear PASS)
2. Re-run FINAL on all three artifacts (should return GO)
3. Task eligible for platform upload

---

**Report Prepared By:** FINAL (Cross-Artifact Holistic Review)  
**Confidence Level:** Very High (mismatch is clear and correctable; revised rubric design is sound, oracle just needs alignment pass)  
**Blocking Issue:** Oracle Events ↔ Universe ↔ Rubrics inconsistency on 2026-494; correctable via OE revision (no prompt/rubric/universe edits required)
