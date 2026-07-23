# Hardness Plan — Tasks/38_6a5edd95a6946f6c4d160b5a

## Persona and Business Function
- Denise Morales (Onsite Property Manager, p_013, denise.morales@starpm.com)
- Business Function 1: Property Operations
- Universe: starpm (Star Property Management, San Antonio TX)
- Universe today: 2026-07-01 (America/Chicago)

---

## Levers Available

| # | Lever | Status | Evidence | Cost range |
|---|---|---|---|---|
| 1 | Latching | yes | Tanya Mitchell has two parallel narratives: ESA reasonable-accommodation track (Slack C002, Brooke/Lisa handoff) vs eviction/delinquency track (Slack C003, U9741B657FE / U98942EF210). Airtable tblMakeReady has both "Tanya Mitchell - Eviction Track" and "Tanya Mitchell - Delinquency Escalation" rows. Agent latches on whichever storyline is discovered first. | 5-8 |
| 2 | Structured-DB skip | yes | Ridgeview roof reconciliation ground truth (PrivateNote on QB bills 2026-481 and PD-2026-084 + AR invoice 2026-494) lives only in QuickBooks. Slack (C001) and Gmail (Brooke/Pete/Robert thread) discuss "$8,400 approved scope" but do not disclose duplicate-bill structure or pass-through invoice. Correct net figure only reachable via QB entity query. Also: credit memo CM-2026-0095 ($175 reversal of duplicate April coordination fee on Ridgeview Plaza) invisible without QB query. | 4-7 |
| 3 | Missing reply | partial | Slack C002 ESA package "ready for your review" (UADB2B4E045 to Brooke) has no response thread visible. Approval gap on ESA path. Weaker standalone lever. | 3-5 |
| 4 | Search-result-cap eviction | partial | C003 #general has 127 messages; Tanya threads scattered under "delinquency," "payment plan," "mitchell" — single-keyword grep misses the ESA track (C002) or Las Palmas 4B reference buried mid-thread. Moderate signal. | 3-5 |
| 5 | Thread-reply blindness | yes | Gmail thread "No AC - Sunset Ridge Apt 208B" (Gabriella Torres complaint) has Tony Reyes's casual Slack response ("Not an emergency; can get her in Thursday — probably a clogged filter") as the prominent signal. Alamo HVAC's formal reply confirming compressor failure is a separate email the agent must find. | 2-4 |
| 6 | Near-miss entity confusion (record-freshness discriminator) | yes | Tanya Mitchell's make-ready record set spans an escalation timeline: rec769c9f03f0b85f (2026-06-12, "Las Palmas 4B", payment plan active) is the earliest row; rec8005502043b755 (2026-06-21, payment plan breached), rec91517a5acab558 (2026-06-28, "Unit 14", 3-day notice), and recc83c05d889b354 (2026-07-01, "Unit 14", JP coordination underway) succeed it. As of universe today the Unit 14 rows are the current-state records; the Las Palmas 4B row is pre-breach and superseded. Wrong-record latching (accepting the older 4B row as current) = wrong current-state narrative and wrong unit reference in the brief. | 3-5 |
| 7 | Multi-write diversification | yes | Denise's natural Onsite PM brief workflow requires: Slack #maintenance update (C001), Linear issue create/update, Gmail draft to Aurora (President). 3 writes across 3 services for density. | 9-12 |
| 8 | Multi-link chain | yes | Ridgeview roof: Airtable tblMakeReady `Ridgeview - Roof Section` row -> tblMaintenanceTickets MT-2026-047 -> QB bill 2026-481 ($8,400, Big Bend Restoration) -> QB bill PD-2026-084 ($8,400, Big Bend, itemized restatement) -> QB invoice 2026-494 ($8,400, Robert Finley pass-through) -> QB payment 972286822645 ($640 partial payment, balance outstanding). Five hops; first link (Airtable MR row) findable via broad search. | 6-9 |
| 9 | Universe-grounded gotcha | yes | Gmail thread "HVAC Inspection Findings - Sunset Ridge Unit 208B" from service@alamohvac.com: compressor failed, unit cannot be restored. Tony Reyes (Lead Maintenance Technician, authority figure) told Denise on Slack it is a clogged filter with a Thursday fix. Agent that trusts Tony's dismissal writes the wrong status. This is the core L9 mechanism. | 3-5 |
| 10 | Reversal/supersession | yes | (a) QB credit memo CM-2026-0095 for -$175 reverses a duplicate maintenance coordination fee on Ridgeview Plaza April 2026 -- visible only in QB, not Slack/Gmail. (b) Bills 2026-481 and PD-2026-084 are both $8,400 for the same roof job; PrivateNote on both clarifies the itemized bill is a pass-through restatement, not additive. | 4-6 |
| 11 | Net-vs-gross framing | yes | Naive sum of Ridgeview vendor bills = $16,800. True vendor exposure = $8,400 (PrivateNote: one bill is the owner-billable AR pass-through, not separate spend). Owner receivable (invoice 2026-494) is $8,400. Agent anchored on email "$8,400 approved scope" doubles the figure when looking at QB bills. | 4-7 |

---

## Selected Levers (5)

- **Lever 9 (Universe-grounded gotcha / Authority-figure dismissal)** -- Tony Reyes dismissed the Sunset Ridge 208B AC ticket as a clogged filter (Thursday fix); Alamo HVAC's formal email confirms compressor failure requiring unit replacement. L9 is the single most reliable stump mechanism (~100% fail rate, L9 citation). Projected cost midpoint: **4**

- **Lever 11 (Net-vs-gross framing)** -- Ridgeview roof owner exposure reported as $16,800 (double-count of vendor bills) vs the correct $8,400 (one bill is a pass-through AR invoice, not additional spend). QB PrivateNote is the only source of this disambiguation. L11 + L13 citations. Projected cost midpoint: **5.5**

- **Lever 2 (Structured-DB skip)** -- The Ridgeview reconciliation truth (PrivateNote fields, credit memo CM-2026-0095) lives entirely in QuickBooks. Slack/Gmail chatter anchors on "$8,400 approved scope" without disclosing the pass-through structure. Agents that read conversational surfaces and stop will double-count. L10 analog citation (Airtable/QB as StarPM's invisible structured DB). Projected cost midpoint: **5.5**

- **Lever 8 (Multi-link chain)** -- Ridgeview roof is a 5-hop reconciliation: Airtable MR row -> maintenance ticket MT-2026-047 -> QB bill 2026-481 -> QB bill PD-2026-084 (pass-through restatement) -> QB invoice 2026-494 -> payment 972286822645 ($640 partial, balance outstanding). First link findable via Airtable search on "Ridgeview." L8 citation. Projected cost midpoint: **7.5**

- **Lever 6 (Near-miss entity confusion / record-freshness discriminator)** -- Tanya Mitchell's make-ready record set spans an escalation timeline: an older Las Palmas 4B row (2026-06-12, pre-breach) and current-state Unit 14 rows (2026-06-28 3-day notice, 2026-07-01 JP coordination). Agent must recognize record freshness and select the Unit 14 rows as authoritative on current-state unit + status; latching on the older 4B row = wrong current-state narrative in the brief. Combined with L9 for structural difficulty (not relied on alone). L4 + L13 citations (combined with other levers, not standalone). Projected cost midpoint: **4**

---

## Tool-Call Density Projection

| Component | Range | Midpoint |
|---|---|---|
| Base discovery (Airtable broad scan, Slack channel survey, contact lookups) | 5-8 | 6.5 |
| Lever 9 -- authority dismissal (Slack Tony msg + Gmail Alamo HVAC thread + ticket cross-check) | 3-5 | 4.0 |
| Lever 2 -- structured-DB skip (QB entity queries: bills, invoice, credit memo, payment, PrivateNote) | 4-7 | 5.5 |
| Lever 11 -- net-vs-gross (read PrivateNote fields, reconcile two bills vs AR invoice) | 4-7 | 5.5 |
| Lever 8 -- multi-link chain (Airtable MR -> MT -> QB bill x2 -> invoice -> payment) | 6-9 | 7.5 |
| Lever 6 -- near-miss entity (Tanya Unit 4B vs Unit 14 x7 Airtable rows, Slack confirmation) | 3-5 | 4.0 |
| Write actions (3 writes x ~3 supporting reads each: Slack update, Linear update, Gmail draft) | 9-12 | 10.5 |
| Cross-service triangulation buffer (contacts, gcalendar, HubSpot owner lookup, Linear state read) | 5-8 | 6.5 |
| **TOTAL projected** | **39-61** | **50.0** |

**Gate (tiered):** midpoint = 50.0 -- **PASS** (design target >= 50 met).

---

## Service Breadth (v11 G1)

| Service | Calls | % of total |
|---|---|---|
| airtable | 9 | 18% |
| quickbooks | 11 | 22% |
| gmail | 9 | 18% |
| slack | 8 | 16% |
| linear | 6 | 12% |
| contacts | 3 | 6% |
| gcalendar | 2 | 4% |
| hubspot | 2 | 4% |
| **Distinct services** | **8** | -- |

**Breadth gate: PASS** -- 6 distinct services above 5%, dominant service (quickbooks) at 22%, well under 60%.

---

## Stump Hypothesis (4 predictions)

1. **[HIGH] Agent reports Sunset Ridge 208B AC status as "clogged filter -- Tony will visit Thursday"** instead of "compressor failure -- unit replacement required." Mechanism: L9 authority-figure dismissal. Tony Reyes (Lead Maintenance Technician) is the credible authority; his Slack message is the first signal Denise would relay. The Alamo HVAC formal email confirmation of compressor failure requires a separate Gmail search that most agents skip once they have Tony's answer. Reasoning: L9 ~100% single-mechanism fail rate documented across Brookfield tasks; same pattern applies in StarPM universe. Expected ~5-of-6 runs fail this rubric.

2. **[HIGH] Agent reports Ridgeview roof owner exposure as $16,800 (double-count) or cites gross $8,400 without disclosing the $640 partial payment and outstanding balance.** Mechanism: L11 net-vs-gross + L2 structured-DB skip + L13 first-framing (email anchors "$8,400 approved scope" which agent reads and accepts verbatim, then adds second QB bill without reading PrivateNote). The pass-through distinction is only in QB PrivateNote fields -- invisible on any conversational surface. Expected ~4-of-6 fail.

3. **[HIGH] Agent identifies Tanya Mitchell's unit as "Las Palmas 4B"** from the older pre-breach Airtable make-ready record (rec769c9f03f0b85f dated 2026-06-12) instead of the current-state Unit 14 from the eviction-track records (rec91517a5acab558 dated 2026-06-28 and recc83c05d889b354 dated 2026-07-01) and matching late-June and July-1 Slack C003 messages. Wrong unit leads to a stale current-state narrative in the brief (payment plan reported as active when it is breached; JP coordination missed). Mechanism: L6 near-miss entity confusion driven by record-freshness (agent takes the first record returned as authoritative rather than reading the timestamps) + L2 structured-DB skip (Airtable timeline is only visible if the agent reconciles all records rather than picking one). Expected ~3-of-6 fail this rubric.

4. **[MED] Agent addresses only the eviction/delinquency track for Tanya Mitchell** and omits the parallel ESA reasonable-accommodation request in the brief to Aurora. Missing the ESA context creates Fair Housing risk that the rubric tests. Mechanism: L1 latching on eviction narrative (first Airtable/Slack signal found). Expected ~2-of-6 fail.

---

## Hardness Score

5/5 -- **PASS**

---

## Hardness Brief for the Prompt Writer

Design Denise Morales's end-of-week Onsite PM status brief for Aurora Winona (President) covering three live items across her properties. Item one: the Sunset Ridge Unit 208B AC ticket where Tony Reyes (Lead Maintenance Technician) told Denise on Slack it is a clogged filter with a Thursday fix, but Alamo HVAC's formal email states the compressor has failed and the unit cannot be restored -- L9 authority-figure dismissal, projected ~5-of-6 fail rate. Item two: the Ridgeview roof owner-exposure figure where naive summation of two QB vendor bills reads $16,800, but the correct net is $8,400 because one bill is an owner pass-through AR invoice mirrored in QB -- L11 net-vs-gross + L2 structured-DB skip + L8 five-hop reconciliation chain (Airtable -> maintenance ticket -> two QB bills -> QB invoice -> payment), projected ~4-of-6 fail rate. Item three: Tanya Mitchell's current-state unit reference where an older Las Palmas 4B make-ready record (2026-06-12, pre-breach) is superseded by current-state Unit 14 eviction-track records (2026-06-28 and 2026-07-01, breach + JP coordination) -- L6 near-miss entity resolved by record-freshness rather than by unit label alone. Require three writes (Slack #maintenance update, Linear issue update, Gmail draft to Aurora) to enforce cross-service breadth. Density target: 50 tool calls midpoint across 8 services -- **PASS at the 50+ design bar**.
