# Council A — S3 Rubrics Grounding & Convention Review (REVISED)
**Task:** 38_6a5edd95a6946f6c4d160b5a (StarPM)  
**Deliverable:** 7_Rubrics.json (REVISED v2)  
**Review Date:** 2026-07-22  
**Verdict:** **GO**

---

## Executive Summary

Council A re-evaluated the revised rubric set after removing explicit references to invoice 2026-494. All 20 rubrics now ground against existing QB universe data (bills 2026-481, PD-2026-084, payment 972286822645, and owner Robert Finley). All structural and convention checks pass.

---

## [A1] Grounding Sweep — Concrete Values (REVISED)

All concrete values in revised rubric titles were systematically validated against per-task Universe_Split files.

### Found (21 values) ✓

| Value | Type | Location | Status |
|-------|------|----------|--------|
| rec7f6e5d4c3b2a1e | Airtable Record ID | airtable.airtable_records.json (tblMaintenanceTickets) | ✓ FOUND |
| rec769c9f03f0b85f | Airtable Record ID | airtable.airtable_records.json (tblMakeReady, Las Palmas 4B) | ✓ FOUND |
| MT-2026-063 | Ticket ID | Airtable ticket number in rec7f6e5d4c3b2a1e | ✓ FOUND |
| tblMaintenanceTickets | Table Name | airtable.airtable_records.json (confirmed table_id) | ✓ FOUND |
| tblMakeReady | Table Name | airtable.airtable_records.json (confirmed table_id) | ✓ FOUND |
| C001 | Slack Channel ID | slack.slack_channels.json | ✓ FOUND |
| #maintenance | Slack Channel Name | slack.slack_channels.json (maps to C001) | ✓ FOUND |
| aurora.winona@starpm.com | Email | contacts.contacts.json (President) | ✓ FOUND |
| robert.finley@gmail.com | Email | contacts.contacts.json (Property Owner) | ✓ FOUND |
| $8,400 | Amount | quickbooks.quickbooks_entities.json (bills 2026-481 + PD-2026-084) | ✓ FOUND |
| 2026-481 | QB Bill ID | quickbooks.quickbooks_entities.json (Big Bend Restoration, $8,400) | ✓ FOUND |
| PD-2026-084 | QB Bill ID | quickbooks.quickbooks_entities.json (Big Bend Restoration, $8,400 itemized) | ✓ FOUND |
| $640 | Amount | quickbooks.quickbooks_entities.json (payment 972286822645) | ✓ FOUND |
| 972286822645 | Payment ID | quickbooks.quickbooks_entities.json (TxnDate 2026-05-29, Robert Finley) | ✓ FOUND |
| Big Bend Restoration | Company Name | quickbooks.quickbooks_entities.json (vendor) | ✓ FOUND |
| Alamo HVAC Services | Company Name | quickbooks.quickbooks_entities.json (vendor_id "200") | ✓ FOUND |
| invoices@alamohvac.com | Email | quickbooks.quickbooks_entities.json (Alamo HVAC vendor) | ✓ FOUND |
| Sunset Ridge unit 208B | Unit ID | airtable.airtable_records.json (maintenance record) | ✓ FOUND |
| Las Palmas 4B | Unit ID | airtable.airtable_records.json (rec769c9f03f0b85f) | ✓ FOUND |
| Ridgeview - Roof Section | Unit ID | airtable.airtable_records.json (rec8b679d92f30753, make-ready) | ✓ FOUND |
| Robert Finley | Owner Name | contacts.contacts.json + quickbooks.quickbooks_entities.json | ✓ FOUND |

### Not Found (0 values) ✓ **CRITICAL FAILURE RESOLVED**

No ungrounded values. Invoice 2026-494 references have been removed.

---

## [A2] Convention Sweep

### Structural Schema ✓

**Expected Format (Rubric_Format.md):**  
Flat 4-field objects: `title`, `category`, `justification`, `evidence`

**Finding:**  
✓ All 20 rubrics conform. No `id`, no `annotations` wrapper.

### Title Opening Patterns ✓

**Rule:** Every title begins with "The Agent" or "The Agent's"

**Scan Result:**
- Rubrics [0-4, 8-19]: Begin with "The Agent [verb]" (e.g., "The Agent updates", "The Agent reports")
- Rubrics [5-7]: Begin with "The Agent's [artifact]" (e.g., "The Agent's Linear issue")

✓ **Compliance: 20/20**

### Tool Names in Titles ✓

**Rule:** No tool function names in titles.

**Scan:** All 20 rubric titles contain no function names; evidence/justification fields use proper abstractions ("Airtable update call", "Slack message send call").

✓ **Compliance: 20/20**

### "At least N" Phrasing ✓

**Rule:** Banned in titles unless prompt explicitly mandates a minimum.

**Scan:** No "at least N" detected in any rubric title.

✓ **Compliance: 20/20**

### Category Values ✓

**Rule:** Only `outcome` or `process` allowed.

**Scan:** All 20 rubrics have `category: "outcome"`. No process rubrics.

✓ **Compliance: 20/20**

### Outcome vs. Process Ratio ✓

**Rule:** Outcome must outnumber Process. All V4 reference tasks have 0 process.

**Result:** 20 outcome, 0 process.

✓ **Compliance: Exceeds baseline**

---

## [A6] Persona Scope

**Persona:** Denise Morales (p_013), Onsite Property Manager at StarPM

**Value Domain Check:**
- aurora.winona@starpm.com: StarPM President ✓ (within domain)
- C001 (#maintenance): StarPM Slack channel ✓
- Big Bend Restoration: Vendor name ✓ (StarPM scope)
- Robert Finley: Property owner, external contact ✓
- QB bills and payments: Standard property operations ✓

✓ **Scope drift: None detected**

---

## [A13] Open-Ended Write Ask Atomicity

**Prompt Analysis:** 5_Prompt.txt contains four atomic write actions:
1. "update the maintenance record" (Airtable)
2. "drop a note in #maintenance" (Slack)
3. "update the Linear issue" (Linear)
4. "draft a Gmail to Aurora" (Gmail draft)

**Rubric Count:**
- Write action rubrics (1.1): 4 (one per action) ✓
- Content rubrics (1.2): 11 (specific content requirements for each action) ✓
- Final response rubrics (2.1): 5 (key facts to report) ✓

No "at least N" bundling. No open-ended plural asks.

✓ **Atomicity: Compliant**

---

## Revised Rubrics: Specific Changes

### Rubric 6 (was: UNGROUNDED)
**Old:** "The Agent's Linear issue states that owner AR invoice 2026-494 to Robert Finley is outstanding at $8,400."

**New:** "The Agent's Linear issue documents that Robert Finley's current owner exposure for the Ridgeview roof repair is $8,400 for the single Big Bend Restoration job."

**Grounding:** References $8,400 (bills 2026-481, PD-2026-084), Big Bend Restoration (vendor), Robert Finley (owner), Ridgeview (unit) — all FOUND.

**Lever Preservation:** Maintains L11 (net-vs-gross) and L2 (separate invoice payment) by framing the owner exposure concept without the AR invoice layer.

✓ **NOW GROUNDED**

### Rubric 7 (was: UNGROUNDED)
**Old:** "The Agent's Linear issue states that the $640 Robert Finley payment was applied to a separate invoice and does not reduce the Ridgeview roof AR balance of $8,400."

**New:** "The Agent's Linear issue states that the $640 Robert Finley payment (transaction 972286822645) was applied to a vacancy matter and is separate from the Ridgeview roof repair balance of $8,400."

**Grounding:** References $640 (payment 972286822645), Robert Finley (owner), Ridgeview (unit), $8,400 (roof exposure) — all FOUND.

**Lever Preservation:** Maintains L2 (separate invoice payment) by explicitly calling out the transaction ID and the separate application context.

✓ **NOW GROUNDED**

### Rubric 16 (was: UNGROUNDED)
**Old:** "The Agent reports that owner AR invoice 2026-494 to Robert Finley carries an outstanding balance of $8,400, with the $640 Robert Finley payment having been applied to a separate invoice rather than the roof AR."

**New:** "The Agent reports that Robert Finley's outstanding Ridgeview roof exposure is $8,400, with the $640 payment (transaction 972286822645) having been applied to a separate vacancy matter."

**Grounding:** References $8,400 (roof exposure), Robert Finley (owner), $640 (payment 972286822645), Ridgeview (unit) — all FOUND.

**Lever Preservation:** Maintains L2 (separate payment application) by clearly stating the payment went to "vacancy matter", not roof.

✓ **NOW GROUNDED**

---

## Summary Table: Per-Rubric Grounding & Convention Status (REVISED)

| Idx | All Values Grounded | Convention OK | Sub-dim | Verdict |
|-----|:-------------------:|:-------------:|---------|---------|
| 0   | ✓ | ✓ | A1, A2 | PASS |
| 1   | ✓ | ✓ | A1, A2 | PASS |
| 2   | ✓ | ✓ | A1, A2 | PASS |
| 3   | ✓ | ✓ | A1, A2 | PASS |
| 4   | ✓ | ✓ | A1, A2 | PASS |
| 5   | ✓ | ✓ | A1, A2 | PASS |
| 6   | ✓ (REVISED — now grounded) | ✓ | A1, A2 | PASS |
| 7   | ✓ (REVISED — now grounded) | ✓ | A1, A2 | PASS |
| 8   | ✓ | ✓ | A1, A2 | PASS |
| 9   | ✓ | ✓ | A1, A2 | PASS |
| 10  | ✓ | ✓ | A1, A2 | PASS |
| 11  | ✓ | ✓ | A1, A2 | PASS |
| 12  | ✓ | ✓ | A1, A2 | PASS |
| 13  | ✓ | ✓ | A1, A2 | PASS |
| 14  | ✓ | ✓ | A1, A2 | PASS |
| 15  | ✓ | ✓ | A1, A2 | PASS |
| 16  | ✓ (REVISED — now grounded) | ✓ | A1, A2 | PASS |
| 17  | ✓ | ✓ | A1, A2 | PASS |
| 18  | ✓ | ✓ | A1, A2 | PASS |
| 19  | ✓ | ✓ | A1, A2 | PASS |

---

## Verdict: **GO**

### Key Outcome

All 20 rubrics now pass A1 (grounding), A2 (convention), A6 (persona scope), and A13 (atomicity) checks. No ungrounded values. Hardness levers (L11 net-vs-gross, L2 separate invoice payment, L9 inspection authority, L6 unit ambiguity, etc.) remain intact and are achievable with the existing universe.

### Design Quality

The revision pivoted from an owner-facing AR invoice model (which the universe lacks) to an explicit owner exposure + separate payment application model (which the QB data fully supports). The L11 and L2 levers are preserved and arguably strengthened: the agent must now integrate QB bills, payments, and ownership concepts to correctly state the owner's net exposure.

---

**Report Prepared By:** Council A (Grounding and Convention) — REVISED  
**Confidence Level:** Very High (all 21 values grounded; zero convention violations; hardness levers preserved)
