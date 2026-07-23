# S3 Council B — Adversarial QC + Density + Hardness Preservation

**Task:** Tasks/38_6a5edd95a6946f6c4d160b5a
**Universe:** StarPM (Star Property Management)
**Deliverable:** 7_Rubrics.json (20 outcome rubrics, 0 process)
**Phase:** rubrics
**Reviewer role composite:** Architect + Implementer + Red-team + Ground-truth + Integration

---

## [B1] QC sub-dim scoring (StarPM 7_QC_Spec_Doc1.json)

SUB-DIM Rubric Overall Quality -> SCORE 5/5 -> REASON Zero rubrics carry Major or Moderate defects; all 20 are grounded in the per-task universe (Fact_Ledger + Universe_Split) and phrased with tolerant evidence bands ("or equivalent language", "or similar phrasing", "or the July timeframe") that admit multiple valid wordings.
SUB-DIM Rubric All-Failing -> SCORE 5/5 (defer) -> REASON Verifier-stage sub-dim; at rubric-writing time no AF rubrics can exist yet. Rated 5 by convention; S4 will re-score.
SUB-DIM Rubric Category Balance -> SCORE 5/5 -> REASON 20 Outcome / 0 Process. Outcome > Process trivially satisfied per the 5/22 clarification.
SUB-DIM Rubric Process Rubrics -> SCORE 5/5 -> REASON Zero process rubrics; zero invalid; the three-condition test does not apply.
SUB-DIM Rubric Agent-Centric Phrasing -> SCORE 5/5 -> REASON Every rubric title opens with "The Agent" or "The Agent's". Zero tool names in any title. Systems / channel IDs / record IDs are allowed and used appropriately (rubric[0] cites `rec7f6e5d4c3b2a1e`, `tblMaintenanceTickets`; rubric[2] cites `C001` — none of these are tool names per StarPM tool catalog).

**B1 result:** all applicable rubric sub-dims land at 5/5.

---

## [B2] Adversarial alt-path

Per-rubric over-specificity analysis:

| # | Alt-path tested | Verdict |
|---|---|---|
| 0 | Agent updates a different Airtable record (e.g., a Tanya-flavored ticket) | APPROPRIATELY SPECIFIC — `rec7f6e5d4c3b2a1e` is the sole 208B maintenance ticket per OE3 discovery. |
| 1 | Agent describes as "AC unit needs replacement" instead of "compressor failure" | APPROPRIATELY SPECIFIC — evidence explicitly admits "equivalent language indicating the compressor has failed". Ground truth (Alamo HVAC email in OE7) uses "compressor failure" verbatim, so any reasonable agent quoting the inspection will use it. |
| 2 | Agent posts using channel name `#maintenance` instead of `C001` | APPROPRIATELY SPECIFIC — evidence explicitly admits either. |
| 3 | Agent posts diagnosis but omits `MT-2026-063` citation | APPROPRIATELY SPECIFIC — MT-2026-063 is the public ticket identifier the team uses; omitting it defeats the "so the team works from the right information" purpose. Two-fact join is defensible per Rubrics Eval Overall Quality (facts from the same corrective action pass/fail together). |
| 4 | Agent adds a comment to OPS-10 or OPS-100 instead of creating a new Linear issue | APPROPRIATELY SPECIFIC — OE24 documents no existing Ridgeview-roof issue and neither OPS-10 nor OPS-100 covers billing status. See B6 note below on prompt phrasing risk. |
| 5 | Agent cites $8,400 correctly but does not name both `2026-481` and `PD-2026-084` | APPROPRIATELY SPECIFIC — this is the L11+L2 discriminating rubric; without both bill IDs the agent has not demonstrated the pass-through reconciliation and could have guessed. |
| 6 | Agent cites `2026-494` outstanding but omits Robert Finley | APPROPRIATELY SPECIFIC — Finley is the pass-through payer; the owner AR narrative fails without him. |
| 7 | Agent doesn't mention the $640 payment at all | APPROPRIATELY SPECIFIC — the $640 payment is the L11 sub-trap; not addressing it leaves ambiguity about whether the agent found and correctly handled it. |
| 8 | Agent creates draft with the address slightly different (e.g., typo) | APPROPRIATELY SPECIFIC — `aurora.winona@starpm.com` is confirmed in Fact_Ledger. |
| 9 | Agent's draft says "AC issue" instead of "compressor failure" | APPROPRIATELY SPECIFIC — Aurora's brief must contain the correct diagnosis per the "actual situation" prompt directive. |
| 10 | Draft says "$8,400 total" without naming Big Bend Restoration | APPROPRIATELY SPECIFIC — vendor name proves the reconciliation. |
| 11 | Agent writes "Las Palmas, unit 4B" or "Las Palmas building unit 4B" instead of "Las Palmas 4B" | APPROPRIATELY SPECIFIC — evidence reads as "must state Tanya Mitchell's unit as Las Palmas 4B"; natural reading admits punctuation and article variants. Judge-level tolerance is standard. |
| 12 | Agent writes "reasonable accommodation for a service animal" instead of ESA | APPROPRIATELY SPECIFIC — evidence explicitly admits "ESA request or reasonable accommodation for an emotional support animal (or similar phrasing)". |
| 13 | Draft says "payment plan active in July" (no end date) | APPROPRIATELY SPECIFIC — evidence admits "or the July timeframe". |
| 14 | Final response only says "AC needs work on 208B" | TOO LENIENT — actually the evidence closes this loop: "A response that only repeats Tony Reyes's dirty-filter assessment fails this rubric." An agent that says only "AC needs work" without contradicting Tony would still fail on the "confirmed by Alamo HVAC" and "compressor failure" requirements. APPROPRIATELY SPECIFIC. |
| 15 | Final response says $8,400 without noting the $16,800 anti-trap | APPROPRIATELY SPECIFIC — the rubric wording asks for "not $16,800, because ... cover the same scope" which admits any framing that explains the reconciliation. |
| 16 | Final response says "$640 payment applied elsewhere" without naming the vacancy invoice | APPROPRIATELY SPECIFIC — evidence tolerates "applied to a different invoice". |
| 17 | Final response says "Sunset Ridge Unit 14" for Tanya | APPROPRIATELY SPECIFIC — this IS the failure mode being tested; evidence explicitly names it. |
| 18 | Final response says "on a payment plan" (no timing) | APPROPRIATELY SPECIFIC but evidence admits "or the July timeframe" — a bare "on a payment plan" without July would arguably fail. This is the intended discriminator. |
| 19 | Final response mentions "eviction" only | APPROPRIATELY SPECIFIC — this is the L1 latching failure being tested. |

**B2 result:** zero rubrics found TOO STRICT (all rejections of over-specific paths are grounded); zero rubrics found TOO LENIENT.

---

## [B3] Tool-call density projection

Representative Opus 4.8 trajectory (composite of OE1-OE31):

| # | Step | Service | Calls |
|---|---|---|---|
| 1 | Contacts lookups: Aurora, Tony, Robert Finley, Brooke | contacts | 4 |
| 2 | Airtable orientation: list_bases + list_tables_for_base | airtable | 2 |
| 3 | search_records tblMaintenanceTickets for 208B | airtable | 1 |
| 4 | slack_search Tony 208B post in C001 | slack | 1 |
| 5 | Gmail search_threads Alamo HVAC | gmail | 1 |
| 6 | get_thread Tony thread b2f4e9a3c71d0856 | gmail | 1 |
| 7 | get_thread Alamo HVAC thread d7c3a1e5f20b9847 | gmail | 1 |
| 8 | update_records_for_table MT-2026-063 (WRITE) | airtable | 1 |
| 9 | slack_send_message C001 (WRITE) | slack | 1 |
| 10 | search_records tblMaintenanceTickets Ridgeview | airtable | 1 |
| 11 | search_records tblMakeReady Ridgeview | airtable | 1 |
| 12 | Gmail search_threads Ridgeview coordination | gmail | 1 |
| 13 | get_thread x4 (0133..., aca0..., a293..., df18...) | gmail | 4 |
| 14 | search_bills Big Bend | quickbooks | 1 |
| 15 | get-bill 528539050604 (2026-481) | quickbooks | 1 |
| 16 | get-bill 301715729067 (PD-2026-084) | quickbooks | 1 |
| 17 | search_invoices Robert Finley | quickbooks | 1 |
| 18 | search_customers Robert Finley | quickbooks | 1 |
| 19 | search_payments Robert Finley | quickbooks | 1 |
| 20 | list_issues Ridgeview | linear | 1 |
| 21 | save_issue (WRITE) | linear | 1 |
| 22 | search_records tblMakeReady Tanya Mitchell (surfaces 7 Unit 14 decoys + Las Palmas 4B) | airtable | 1 |
| 23 | search_records tblMakeReady Las Palmas 4B (disambiguation) | airtable | 1 |
| 24 | search_records tblMaintenanceTickets Tanya delinquency | airtable | 1 |
| 25 | slack_search C003 Tanya unit | slack | 1 |
| 26 | slack_search C002 ESA request | slack | 1 |
| 27 | create_draft to aurora.winona@starpm.com (WRITE) | gmail | 1 |
| — | Sub-total (OE-covered) | — | **34** |
| 28 | Natural Opus exploration buffer: 1-2 additional Slack channel scans for context, HubSpot owner-property mapping check, 1-2 additional get_thread on related Ridgeview emails, gcalendar read for Denise's leave window | mixed | +6-12 |
| — | **Projected range** | — | **40-46** |
| — | **Midpoint estimate** | — | **43** |

**B3 verdict: THIN_DENSITY** (midpoint ~43; floor 40 met; 50+ target NOT met).

This confirms the THIN_DENSITY carry from HARDNESS (which projected 50.0 optimistically) and S2 (which flagged 43 empirical). The rubric set at 20 items covers 8 discrete verifiable data points across 4 write actions + 6 final-response facts — this matches the projected trajectory. The rubric coverage is not under- or over-specified relative to the trajectory density.

Continuation justified: per-task justification for THIN_DENSITY (already logged in Hardness_Plan.md) is that lever quality (L9 + L11 + L2 + L8 + L6 + ESA-latching, six stump vectors) compensates for a density that sits between the floor and the target. Operator should be aware this task is at risk of underflowing on real Opus 4.8 platform runs; if it does, the pipeline REDO trigger applies.

---

## [B4] Hardness preservation

| Lever | Covered by rubric | Verdict |
|---|---|---|
| L9 — Authority-dismissal (Tony Reyes vs Alamo HVAC) | rubric[1] (Airtable update reflects compressor failure), rubric[3] (Slack message states compressor failure), rubric[9] (Gmail draft says compressor failure not dirty filter), rubric[14] (final response cites Alamo HVAC, contradicts Tony) | **PRESERVED** — 4 discriminating rubrics, one per write surface + final response. |
| L11 — Net-vs-gross ($8,400 vs $16,800) | rubric[5] (Linear says $8,400 single job), rubric[10] (Gmail says $8,400 single job), rubric[15] (final response says $8,400 not $16,800) | **PRESERVED** — 3 discriminating rubrics. |
| L2 — Structured-DB skip (QB PrivateNote) | rubric[5] ("two QB bill records represent the same scope, not additive" — only knowable via PrivateNote), rubric[6] (AR invoice $8,400 — QB entity) | **PRESERVED** — the "same scope, not additive" wording locks in that PrivateNote was read. |
| L8 — Multi-link 5-hop chain | rubric[5] (both bill IDs), rubric[6] (AR invoice 2026-494), rubric[7] (payment 972286822645 traversal) | **PRESERVED** — the three sub-rubrics collectively require the Airtable → MT → QB bill×2 → QB invoice → payment chain. |
| L6 — Near-miss entity (Las Palmas 4B vs 7 Unit 14) | rubric[11] (Gmail draft says Las Palmas 4B), rubric[17] (final response explicitly rejects Unit 14 variants) | **PRESERVED** — 2 discriminating rubrics; rubric[17] evidence explicitly names the failure mode. |
| ESA/latching trap (Fair Housing parallel track) | rubric[12] (Gmail mentions ESA), rubric[19] (final response mentions ESA) | **PRESERVED** — 2 discriminating rubrics. |

Zero HARDNESS_REGRESSION findings. All 5 selected levers + the L1 latching sub-trap have at least one Outcome rubric that fails if the agent misses the lever.

---

## [B6] Upstream propagation

**Potential-flag (Minor, non-blocker):** the prompt says "update the Linear issue with the current status once you have it" — the definite article "the" implies an existing issue. OE24 discovery confirms no such issue exists, and OE25 creates a new one. Rubric[4] locks in the create-path.

Under the 06/09 Unique-Ground-Truth spec update, "two reasonable readings → different write actions" is a Prompt-1.4 FAIL. Two reasonable readings here would be: (a) create a new Ridgeview-roof Linear issue [locked by OE25/rubric[4]], (b) add a comment to OPS-10 or OPS-100 (the nearest related issues per OE24).

However, OE24 documents that neither OPS-10 nor OPS-100 covers billing status — an agent reading Linear would conclude a new issue is the natural action. The universe-state ground-truth disambiguation is defensible; this is more of a S1 Prompt Clarity concern than a rubric-phase blocker.

Recommendation: **do NOT propagate**. Note as a soft observation. If S4 verifier fails cluster on "agent commented on OPS-10 instead of creating an issue", re-evaluate at that time.

All other upstream artifacts check out:
- OE8 `update_records_for_table` uses StarPM camelCase (`baseId`, `tableId`, `records[]`) — correct.
- OE9 `slack_send_message` uses `channel_id` + `message` (StarPM convention, NOT `payload`/`text`) — correct.
- OE25 `save_issue` uses `team` (NOT `teamId`) — correct StarPM parameter.
- OE31 `create_draft` uses `to[]` + `subject` + `body` (NOT `content`, and draft-only per StarPM) — correct.
- Airtable table name `tblMaintenanceTickets` and record `rec7f6e5d4c3b2a1e` cross-check to Fact_Ledger IDs — record present in the airtable_record ID list at line 1526.

No hard PROPAGATE flags.

---

## [B7] Per-rubric cross-artifact consistency

| Rubric | OE mapping | Value under test | OE-side value | Match |
|---|---|---|---|---|
| rubric[0] | OE8 | Airtable update to rec7f6e5d4c3b2a1e in tblMaintenanceTickets | OE8: `records: [{id: "rec7f6e5d4c3b2a1e"}]` in tblMaintenanceTickets | ✓ |
| rubric[1] | OE8 (fields) + OE7 (source) | Compressor failure diagnosis supersedes dirty-filter | OE7: Alamo email "compressor failure -- the unit cannot be restored by filter replacement" | ✓ |
| rubric[2] | OE9 | Slack channel C001 (#maintenance) | OE9: `channel_id: "C001"` | ✓ |
| rubric[3] | OE9 | Message: compressor failure + MT-2026-063 updated | OE9: message covers both facts | ✓ |
| rubric[4] | OE25 | Linear issue creation for Ridgeview roof billing | OE25: `save_issue` create | ✓ |
| rubric[5] | OE25 (desc) + OE19+OE20 (source) | $8,400 single Big Bend job, both bills 2026-481 + PD-2026-084 same scope | OE19+OE20: PrivateNote fields confirm same scope; OE25 description carries both IDs | ✓ |
| rubric[6] | OE25 (desc) + OE21 | AR invoice 2026-494 outstanding $8,400 to Robert Finley | OE21: invoice 2026-494 balance $8,400 to Robert Finley | ✓ |
| rubric[7] | OE25 (desc) + OE23 | $640 payment 972286822645 applied to separate invoice | OE23: payment $640 applied to invoice DocNumber 5848 | ✓ |
| rubric[8] | OE31 | Gmail draft to aurora.winona@starpm.com | OE31: `to: ["aurora.winona@starpm.com"]` | ✓ |
| rubric[9] | OE31 (body item 1) | Compressor failure not dirty filter | OE31 body item 1 states this | ✓ |
| rubric[10] | OE31 (body item 2) | $8,400 single Big Bend job | OE31 body item 2 states this | ✓ |
| rubric[11] | OE31 (body item 3) + OE27 | Tanya's unit Las Palmas 4B | OE27: rec769c9f03f0b85f = Las Palmas 4B | ✓ |
| rubric[12] | OE31 (body item 3) + OE30 | ESA reasonable accommodation | OE30: Slack C002 ESA request message | ✓ |
| rubric[13] | OE31 (body item 3) + OE26/OE27 | Payment plan through end of July | OE26/OE27: "payment plan active, holding through end of July" | ✓ |
| rubric[14] | final response + OE7 | Compressor failure per Alamo | OE7 grounds | ✓ |
| rubric[15] | final response + OE19+OE20 | $8,400 not $16,800 | OE19+OE20 ground | ✓ |
| rubric[16] | final response + OE23 | $640 to separate invoice | OE23 grounds | ✓ |
| rubric[17] | final response + OE26/OE27/OE29 | Las Palmas 4B not Unit 14 | OE26/OE27/OE29 ground; OE26 explicitly enumerates 6 Unit 14 decoys | ✓ |
| rubric[18] | final response + OE26/OE27 | Payment plan end of July | OE26/OE27 ground | ✓ |
| rubric[19] | final response + OE30 | ESA request | OE30 grounds | ✓ |

**Zero CONSISTENCY_GAP findings.**

---

## Summary

### B3 Density Verdict
**THIN_DENSITY** — midpoint 43, range 40-46; floor 40 met; 50+ target NOT met. Carried from HARDNESS/S2. Continuation justified per Hardness_Plan.md — lever quality (6 stump vectors: L9, L11, L2, L8, L6, L1-ESA) compensates. Operator warning: task at risk of underflowing on real platform runs.

### B4 Lever Preservation
| Lever | Covered by | Status |
|---|---|---|
| L9 (authority dismissal) | rubric[1], [3], [9], [14] | PRESERVED |
| L11 (net vs gross) | rubric[5], [10], [15] | PRESERVED |
| L2 (structured-DB skip) | rubric[5], [6] | PRESERVED |
| L8 (5-hop chain) | rubric[5], [6], [7] | PRESERVED |
| L6 (near-miss entity) | rubric[11], [17] | PRESERVED |
| L1 (ESA/latching) | rubric[12], [19] | PRESERVED |

Zero HARDNESS_REGRESSION.

### Overall Verdict

**GO**

Reason summary: all 5 rubric-applicable QC sub-dims land 5/5. Zero adversarial rubrics found TOO STRICT or TOO LENIENT. All 6 hardness levers preserved with at least one discriminating Outcome rubric each. Zero CONSISTENCY_GAP findings between rubric and OE. Zero hard upstream PROPAGATE flags (one soft observation on prompt "update the Linear issue" phrasing — not blocker-severity, defensible via OE24 universe-state ground truth). Density is THIN_DENSITY (43 midpoint) but ≥ 40 floor with per-task justification carried from HARDNESS.

Ready for S3 AUDIT (strict veteran second pass), then FINAL.
