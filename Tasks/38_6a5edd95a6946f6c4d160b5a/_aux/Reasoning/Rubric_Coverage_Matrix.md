# Rubric Coverage Matrix — S3

**Task:** 38_6a5edd95a6946f6c4d160b5a (StarPM)
**Persona:** Denise Morales (p_013, Onsite Property Manager)
**Rubric count:** 22 outcome, 0 process (20 → 22 after post-Round-2 atomicity splits: old[3]→[3+4], old[16]→[17+18])
**AUDIT verdict:** PASS (STRICT) — Round 3 of 3 (see AUDIT_rubrics.md)

---

## Prompt → OE → Rubric Mapping

### Item 1: Sunset Ridge Unit 208B AC Status

**Prompt sentence:** "Check the actual inspection status of the Sunset Ridge unit 208B AC... find out what actually came back from the inspection and update the maintenance record with it. Then drop a note in #maintenance so the team is working from the right information."

**Tell-me cue:** "I want to know what actually came back from the inspection."

| OE Step | Action | Rubric(s) |
|---|---|---|
| OE2 | contacts_search_contacts Tony Reyes (establishes authority figure identity) | context |
| OE3 | list_bases + list_tables + search_records tblMaintenanceTickets → rec7f6e5d4c3b2a1e, MT-2026-063 | context |
| OE4 | slack_search Tony's 208B message → dirty filter claim in C001 (L9 trap setup) | context |
| OE5 | Gmail search_threads Alamo HVAC inspection | context |
| OE6 | get_thread b2f4e9a3c71d0856 (Tony email + tenant complaint) | context |
| OE7 | get_thread d7c3a1e5f20b9847 → "compressor failure" finding | context |
| **OE8** | **update_records_for_table rec7f6e5d4c3b2a1e tblMaintenanceTickets (WRITE)** | **rubric[0]** (1.1 action), **rubric[1]** (1.2 content: compressor failure, not dirty filter) |
| **OE9** | **slack_send_message C001 (WRITE)** | **rubric[2]** (1.1 action), **rubric[3]** (1.2 content: compressor failure + MT-2026-063 updated) |
| — | Final response | **rubric[14]** (2.1: reports compressor failure per Alamo HVAC, contradicts Tony) |

**Coverage check:** Prompt ask fully covered. L9 lever (authority-dismissal) discriminated by rubric[1], [3], [14].

---

### Item 2: Ridgeview Roof Owner Exposure

**Prompt sentence:** "Figure out what the real owner exposure is for the Ridgeview roof repair... update the Linear issue with the current status once you have it."

**Tell-me cue:** "Figure out what the real owner exposure is."

| OE Step | Action | Rubric(s) |
|---|---|---|
| OE10 | search_records tblMaintenanceTickets Ridgeview → recb4aeaed326f156, MT-2026-047 | context |
| OE11 | search_records tblMakeReady Ridgeview → rec8b679d92f30753, $8,400 estimate | context |
| OE12 | contacts_search Robert Finley (owner confirmation) | context |
| OE13 | contacts_search Brooke Phillips (coordinator confirmation) | context |
| OE14 | Gmail search_threads Ridgeview coordination → 4 threads | context |
| OE15 | get_thread 0133155c8a154ab1 → Finley approval "I'm comfortable, $8,400" | context |
| OE16 | get_thread aca02b07c749958d → one contractor, one job | context |
| OE17 | get_thread a293b24b7f85b0f0 + df187f8cb5c2b3f6 → scope confirmation | context |
| OE18 | search_bills Big Bend Restoration → 2026-481 + PD-2026-084 appear (L11 trap: looks like $16,800) | context |
| OE19 | get-bill 528539050604 (2026-481) → $8,400, PrivateNote: "mirror on owner-billable pass-through" | context |
| OE20 | get-bill 301715729067 (PD-2026-084) → $8,400 itemized, PrivateNote: "same scope as 2026-481" (L2: must read PrivateNote) | context |
| OE21 | search_bills + search_customers Robert Finley → surfaces owner billing exposure | context |
| OE22 | contacts + QB customer confirm Robert Finley identity | context |
| OE23 | search_payments Robert Finley → payment 972286822645 ($640), applied to invoice DocNumber 5848 (separate vacancy invoice) | context |
| OE24 | list_issues Ridgeview → no existing dedicated issue (OPS-10, OPS-100 not relevant) | context |
| **OE25** | **save_issue Linear (WRITE)** | **rubric[4]** (1.1 action), **rubric[5]** (1.2: $8,400 single Big Bend job, both bills same scope), **rubric[6]** (1.2: Robert Finley owner receivable $8,400 outstanding — relaxed from invoice 2026-494 per AUDIT Round 1), **rubric[7]** (1.2: $640 payment 972286822645 to separate invoice) |
| — | Final response | **rubric[15]** (2.1: $8,400 not $16,800, two bills same scope), **rubric[16]** (2.1: Robert Finley owner receivable $8,400 outstanding, $640 to separate invoice — relaxed from invoice 2026-494 per AUDIT Round 1) |

**Coverage check:** Prompt ask fully covered. L11 (net-vs-gross) by rubric[5],[15]; L2 (structured-DB skip) by rubric[5],[6],[7]; L8 (5-hop chain) by rubric[5],[6],[7].

---

### Item 3: Tanya Mitchell Unit Confirmation

**Prompt sentence:** "Confirm which unit she's in — I keep seeing different records. And look up her current status while you're in there."

**Tell-me cues:** "Confirm which unit she's in." "Look up her current status."

| OE Step | Action | Rubric(s) |
|---|---|---|
| OE26 | search_records tblMakeReady Tanya Mitchell → 7 Unit 14 decoy records + rec769c9f03f0b85f (Las Palmas 4B) (L6 trap) | context |
| OE27 | search_records tblMakeReady Las Palmas 4B → confirms rec769c9f03f0b85f as current status record | context |
| OE28 | search_records tblMaintenanceTickets Tanya → delinquency/eviction tickets (context) | context |
| OE29 | slack_search C003 Tanya unit → "unit 4B" confirmation + 2 Unit 14 decoy messages | context |
| OE30 | slack_search C002 ESA → message 07e57e41fb725c9f910b0f56cfe463da: ESA reasonable accommodation request | context |
| — | Final response | **rubric[17]** (2.1: Las Palmas 4B, not Unit 14), **rubric[18]** (2.1: payment plan through end of July), **rubric[19]** (2.1: ESA request on file) |

**Coverage check:** Prompt ask fully covered. L6 (near-miss entity) by rubric[17]; ESA/latching trap by rubric[19].

---

### Item 4: Gmail Draft to Aurora

**Prompt sentence:** "Draft a Gmail to Aurora with the full update — she'll want the actual situation on all three things."

| OE Step | Action | Rubric(s) |
|---|---|---|
| OE1 | contacts_search Aurora Winona → aurora.winona@starpm.com confirmed | context |
| **OE31** | **create_draft to aurora.winona@starpm.com (WRITE)** | **rubric[8]** (1.1 action), **rubric[9]** (1.2: compressor failure not dirty filter), **rubric[10]** (1.2: $8,400 single Big Bend job), **rubric[11]** (1.2: Tanya unit Las Palmas 4B), **rubric[12]** (1.2: ESA accommodation request), **rubric[13]** (1.2: payment plan through end of July) |

**Coverage check:** Prompt ask fully covered. All three items summarized in Gmail rubrics.

---

## Coverage Summary

| Prompt ask | Write action | 1.1 rubric | 1.2 rubrics | 2.1 rubrics |
|---|---|---|---|---|
| Update 208B maintenance record | OE8 (Airtable) | rubric[0] | rubric[1] | rubric[14] |
| Post in #maintenance | OE9 (Slack) | rubric[2] | rubric[3] | rubric[14] |
| Update Linear for Ridgeview | OE25 (Linear) | rubric[4] | rubric[5], [6], [7] | rubric[15], [16] |
| Draft Gmail to Aurora | OE31 (Gmail) | rubric[8] | rubric[9]-[13] | — |
| Report 208B finding | — | — | — | rubric[14] |
| Report Ridgeview exposure | — | — | — | rubric[15], [16] |
| Confirm Tanya's unit | — | — | — | rubric[17] |
| Report Tanya's status | — | — | — | rubric[18], [19] |

**Total:** 4 OE write actions × at least 1 × (1.1 rubric each) ✓  
**Total 1.2 rubrics:** 11 (content requirements for write-action outputs) ✓  
**Total 2.1 rubrics:** 6 (key facts for final response) ✓  
**No gaps:** every prompt ask has at least one rubric.  
**No surplus:** every rubric traces to a prompt sentence.

---

## Hardness Lever Coverage

| Lever | Prompt surface | OE chain | Discriminating rubric(s) |
|---|---|---|---|
| L9 — Authority-dismissal (Tony vs Alamo HVAC) | "check the actual inspection status" | OE4 (Tony Slack), OE7 (Alamo email) | rubric[1], [3], [9], [14] |
| L11 — Net-vs-gross ($8,400 vs $16,800) | "figure out the real owner exposure" | OE18-20 (two bills, PrivateNote) | rubric[5], [10], [15] |
| L2 — Structured-DB skip (QB PrivateNote) | "figure out the real owner exposure" | OE19-20 (must read PrivateNote) | rubric[5], [6] |
| L8 — Multi-link 5-hop chain | "figure out the real owner exposure" | OE10→OE11→OE18+OE19→OE21→OE23 | rubric[5], [6], [7] |
| L6 — Near-miss entity (Las Palmas 4B vs 7 Unit 14s) | "confirm which unit she's in" | OE26-27 (7 decoys → rec769c9f03f0b85f) | rubric[11], [17] |
| L1-ESA — Latching trap (delinquency vs ESA track) | "look up her current status" | OE30 (Slack C002 ESA) | rubric[12], [19] |

All 6 levers covered. Zero hardness regression.

---

## Density Note

Council B projected midpoint 43 (range 40-46). OE chain baseline: ~34 OE-covered calls. Opus exploration overhead: +6-12 calls. THIN_DENSITY flag carried from HARDNESS phase with per-task justification (lever quality compensates). Floor 40 met; 50+ design target not met. See Hardness_Plan.md for justification.
