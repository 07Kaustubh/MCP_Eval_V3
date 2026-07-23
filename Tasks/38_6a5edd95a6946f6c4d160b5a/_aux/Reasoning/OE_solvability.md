# OE_solvability.md — Oracle Events Solvability Analysis
## Task: 38_6a5edd95a6946f6c4d160b5a
## Phase: S2 (Oracle Events)
## Date: 2026-07-21

---

## Overview

31 OEs across 4 asks. Each ask has a clear evidence-chain → decision → write-action path. This document records the solvability judgment for each ask and documents the key non-obvious steps that a correct agent must navigate.

---

## Ask 1 — Sunset Ridge 208B AC True Status (OE1–OE9)

**Solvability verdict: Solvable with lever navigation**

**Trap (L9 — Authority-Figure Dismissal):**
Tony Reyes is the Lead Maintenance Technician and his informal dirty-filter assessment (Slack msg c7e3a2f5b4d1e9a8b3c2f7e4d5a1b9c8 + email f4a7b9c2e5d31a70) is repeated across two channels, giving it apparent authority. MT-2026-063 in Airtable also reflects only Tony's assessment. A model that accepts the highest-seniority internal voice without retrieving the professional inspection result will write the wrong status.

**Resolution path:**
The agent must search Gmail for Alamo HVAC (the contracted inspector), retrieve thread d7c3a1e5f20b9847, and read email a3b7c4f2e9d81065 which states "compressor failure." This is a professional third-party finding that supersedes Tony's informal pre-inspection assessment.

**Why solvable:**
The Alamo HVAC thread is discoverable via Gmail search on "Alamo HVAC" or "compressor" or "208B." The contradiction between Tony's Slack/email and the inspector's finding is explicit and resolvable. The correct update to MT-2026-063 follows directly from OE7.

**Correct answer atoms:**
- True status: compressor failure (not dirty filter)
- Ticket MT-2026-063: update to reflect Alamo HVAC finding
- #maintenance (C001): notify team of correction

---

## Ask 2 — Real Ridgeview Owner Exposure (OE10–OE25)

**Solvability verdict: Solvable with multi-link chain + billing dedup**

**Trap 1 (L8 — Multi-Link Chain):**
The owner authorization is not in a single email — it is distributed across a 5-hop chain (threads aca02b07c749958d → a293b24b7f85b0f0 → df187f8cb5c2b3f6 → 0133155c8a154ab1). A model that stops after retrieving 1–2 threads will lack the Finley formal approval email (4bcbe384bedfd26f) and may misreport authorization status.

**Trap 2 (L11 — Net-vs-Gross):**
QuickBooks surfaces two bill records for Big Bend Restoration (2026-481 at $8,400; PD-2026-084 at $8,400). Naive summation yields $16,800. PrivateNote on PD-2026-084 explicitly states it is an itemized restatement of the same job as 2026-481 — same scope, not additive. Correct vendor cost = $8,400.

**Resolution path:**
- Walk all 4 email threads to confirm single $8,400 scope and owner approval
- Retrieve both QB bills via get-bill and read PrivateNotes
- Verify owner AR (invoice 2026-494 = $8,400 outstanding)
- Verify the $640 Robert Finley payment (972286822645) was applied to doc 5848, a separate invoice — it does not reduce the roof AR
- Confirm no existing Ridgeview roof Linear issue (OE24: OPS-10 and OPS-100 are closest but not the same)
- Create new Linear issue via save_issue

**Why solvable:**
The L11 dedup signal is explicit in the PrivateNote on PD-2026-084. The L8 chain is discoverable via Gmail search; all 4 threads surface in OE14. The $640 mis-application is verifiable via search_payments. The "no existing issue" state makes OE25 a create (not update) — but this is the only correct interpretation given the universe surface.

**Correct answer atoms:**
- Vendor cost: $8,400 (single job; two QB records = same scope)
- Owner AR outstanding: $8,400 (invoice 2026-494; $640 payment does not offset it)
- Linear: new issue created (no existing Ridgeview roof issue found)

---

## Ask 3 — Tanya Mitchell Current Status + Unit (OE26–OE30)

**Solvability verdict: Solvable with decoy separation**

**Trap (L6 — Near-Miss Entity Confusion):**
Airtable tblMakeReady contains 7 records matching "Tanya Mitchell": 6 are Unit 14 decoys (eviction/delinquency tracks across multiple properties) and 1 is the authoritative current-status record (rec769c9f03f0b85f, label "Las Palmas 4B"). Slack C003 also contains 2 Unit 14 decoy messages alongside 2 Las Palmas 4B authoritative messages. A model that accepts the first Airtable result (likely a Unit 14 decoy given they outnumber the correct record 6:1) will report the wrong unit.

**Resolution path:**
- OE26: broad tblMakeReady search surfaces all 7 records; agent must identify the one non-Unit-14 record
- OE27: targeted search on "Las Palmas 4B" isolates rec769c9f03f0b85f — payment plan active, holding through end of July
- OE28: tblMaintenanceTickets search adds delinquency context (MT-2026-0184, DLQ-2026-0601)
- OE29: Slack search confirms unit 4B via messages 54a3ac6bc5f55a5db665baccfd68b368 + 38aa0a611ea2537fa43ac0edecc70d81; agent must distinguish from Unit 14 decoy messages a718e828a5e85e16b037d8a3bd058d0c + 781f8bfa140f50e59cf8e8c9d1f1ff93
- OE30: Slack search surfaces ESA reasonable accommodation message 07e57e41fb725c9f910b0f56cfe463da in C002

**Why solvable:**
The Las Palmas 4B record is unambiguous once isolated — it is the only record with that property label. The Slack unit 4B messages are also explicit. The resolution requires the agent to notice the Unit 14 label mismatch across records and prefer Las Palmas 4B as the current-status record, which is verifiable cross-source (Airtable + Slack).

**Correct answer atoms:**
- Unit: Las Palmas 4B (not Unit 14; the 6 Unit 14 MR records are separate tracks)
- Status: payment plan active through end of July
- ESA: reasonable accommodation request on file

---

## Ask 4 — Draft Gmail to Aurora (OE1 + OE31)

**Solvability verdict: Solvable (terminal synthesis step)**

**No unique trap.** Ask 4 is a synthesis write: all atoms flow from Asks 1–3. The agent must integrate the correct compressor failure finding, the correct $8,400 net exposure (not $16,800), the correct unit (Las Palmas 4B, not Unit 14), and the correct payment plan / ESA status into a single create_draft to aurora.winona@starpm.com.

**Key constraint:** StarPM Gmail is draft-only (create_draft uses `body`, no send tool). If the agent calls a send tool, it will receive an error or no-op. The correct output is a draft only.

**Correct answer atoms:**
- Recipient: aurora.winona@starpm.com
- Body must include: compressor failure (208B); $8,400 single scope (Ridgeview); Las Palmas 4B + payment plan + ESA (Tanya)
- Tool: create_draft with `body` param (NOT `content`)

---

## Overall Solvability Assessment

**All 4 asks are solvable.** No ask requires information that is absent from the universe. Each lever has an explicit resolution path in the OE list. The difficulty lies in:

1. **Not short-circuiting** at Tony's informal assessment (L9)
2. **Not summing two bills** without reading PrivateNotes (L11)
3. **Walking all 4 email threads** in the Ridgeview chain (L8)
4. **Cross-referencing** the 6 Unit 14 decoys against the Las Palmas 4B record (L6)
5. **Checking Airtable before trusting Slack** as primary record source (L2 partial)

A correct agent that follows the evidence chain without anchoring on authority or first-hit results will produce 4 correct write-action outputs. Opus 4.8 failure modes targeted: L9 anchors on Tony (authority bias); L11 sums naively (arithmetic completion without PrivateNote read); L8 stops early (chain truncation); L6 accepts first Unit 14 result (entity resolution failure on imbalanced decoy set).

---

*Appended at S2 phase completion: 2026-07-21*
