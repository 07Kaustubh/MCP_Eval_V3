# FINAL Council — Cross-Artifact Holistic Review (ROUND 2)

**Task:** 38_6a5edd95a6946f6c4d160b5a (StarPM)
**Artifacts:** 5_Prompt.txt (9 lines) / 6_Oracle_Events.txt (31 OE steps, ~16KB) / 7_Rubrics.json (24 rubrics, 24 outcome / 0 process)
**Review Date:** 2026-07-22
**Universe today:** 2026-07-01 America/Chicago
**Prior FINAL:** _aux/Council_Reports/FINAL_council_round1_REVISE.md — REVISE (2 BLOCKER + 2 MAJOR).
**Validator sweep this pass:** em-dashes = 0 in all 3 files; "at least N" in rubric titles = 0; tool function names in rubric titles = 0; outcome/process = 24/0; `eviction filing package` in prompt = 0; `Las Palmas 4B` in rubric titles = 0; dual-accept ("either", " or ") in R13/R20 titles = 0; AND-bundle in split rubrics = 0.

---

## ROUND-1 FIXES VERIFIED

| # | Round-1 defect | Round-2 fix | Verify | Verdict |
|---|---|---|---|---|
| 1 | MAJOR 3 — "eviction filing package" leaked in prompt line 7 | Prompt line 7 replaced with "confirm her current status and the unit reference on that record." | `5_Prompt.txt`:7 — 0 hits for "eviction filing package" anywhere in prompt; 0 hits for "breach", "JP", "Justice of the Peace" | **PASS** |
| 2a | BLOCKER 2 — R13 dual-accept deleted L6 discriminator | R13 (index 12) rewritten: canonical Unit 14 only; justification cites record-freshness (rec91517a5acab558 2026-06-28 + recc83c05d889b354 2026-07-01 vs older rec769c9f03f0b85f 2026-06-12); evidence: "A draft that names Las Palmas 4B (the superseded pre-breach record) or names no unit at all fails this rubric" | `7_Rubrics.json`:75-78 — 0 hits for "either"/" or " (dual-accept) in title; Las Palmas 4B appears only in explicit negative-guard evidence | **PASS** |
| 2b | BLOCKER 2 — R20 same dual-accept | R20 (index 20) rewritten with same structure as R13; canonical Unit 14 only; same record-freshness justification; same negative-guard evidence | `7_Rubrics.json`:123-126 — 0 hits for dual-accept; canonical Unit 14 required | **PASS** |
| 3a | MAJOR 4 — R15 AND-bundle (breach + JP) | Old R15 split into R15a (index 14, breach only) + R15b (index 15, JP only). Each rubric tests exactly one claim; no AND coupling | `7_Rubrics.json`:87-96 — index 14 title: "…payment plan was breached on the June 23 installment." (atomic); index 15 title: "…eviction filing package is being coordinated with the Justice of the Peace." (atomic) | **PASS** |
| 3b | MAJOR 4 — R21 AND-bundle (breach + JP) | Old R21 split into R21a (index 21, breach only) + R21b (index 22, JP only). Same structure as R15 split | `7_Rubrics.json`:129-138 — index 21 title: "…payment plan was breached on the June 23 installment." (atomic); index 22 title: "…eviction filing package is being coordinated with the Justice of the Peace." (atomic). Total rubric count = 24 | **PASS** |
| 4 | BLOCKER 1 — OE26/27/29/30/31 said Las Palmas 4B was authoritative current-state | OE26 reframed as escalation-timeline enumeration (June 12 pre-breach → June 21 breach → June 28 3-day notice → July 1 JP). OE27 now names `recc83c05d889b354` (July 1) as "authoritative on current-state" and calls rec769c9f03f0b85f "pre-breach and no longer describes Tanya's current status." OE29 distinguishes June 12 pre-breach 4B Slack messages from June 28 / July 1 Unit 14 current-state messages. OE30 body: "unit Unit 14, payment plan breached on the June 23 installment…JP coordination underway." OE31 drafting section (3) matches. | `6_Oracle_Events.txt`:51,53,57,59,61 — 0 hits for "authoritative current-status" pointing at rec769c9f03f0b85f; 0 hits for "payment plan active through end of July" as a current-state claim; "authoritative on current-state" now points at recc83c05d889b354 (July 1) | **PASS** |
| 5 | Hardness_Plan L6 required refresh to match new rubric direction | L6 table row (line 20) reframed as "record-freshness discriminator" — "Wrong-record latching (accepting the older 4B row as current) = wrong current-state narrative"; Selected Levers line 39 aligned; Stump Hypothesis #3 (line 85) now predicts wrong = Las Palmas 4B, correct = Unit 14 via record-freshness; Hardness Brief line 99 aligned | `_aux/Hardness_Plan.md`:20,39,85,99 — 0 hits for "actual unit is Las Palmas 4B" or "correct Las Palmas 4B"; L6 explicitly names Unit 14 as canonical + Las Palmas 4B as pre-breach superseded row | **PASS** |
| 6 | Regression scan — new inconsistencies introduced? | OE31 drafting section (3) does name Unit 14 / breach / JP as expected agent-drafting content, but this is an OE prescription (agent-facing expected output), not a prompt or universe-artifact leak — per project convention this is allowed. Prompt line 7 remains implicit ("her current status and the unit reference on that record"). No new tokens or contradictions introduced. | Cross-checked prompt lines 1-9 vs OE1-31 vs rubrics 0-23 — no new state-implying claims that contradict universe atoms | **PASS** |
| 7 | Lever count — all 5 levers still triggered end-to-end? | L9/L11/L2/L8 unchanged from prior FINAL (intact). L6 reframed from "unit-label decoy" to "record-freshness discriminator": prompt "the unit reference on that record" (implicit ambiguity), OE26 (enumerates 7 Tanya records with timestamps), OE27 (reconciliation across 4 records + names July 1 as authoritative), OE29 (Slack timeline confirmation), R13 + R20 (require Unit 14). Fully triggered. | Prompt → OE → rubric trace confirmed for all 5 levers | **PASS** |
| 8 | Density recount after OE27 reconciliation expansion | Baseline Hardness_Plan midpoint: 50.0. OE27 now instructs reconciliation across 4 make-ready records (rec769c9f03f0b85f + rec8005502043b755 + rec91517a5acab558 + recc83c05d889b354) — most of these are already retrieved as the broad search-result set in OE26, so incremental cost is +2 to +4 defensive re-reads. New midpoint ~52-54. | Tier = **PASS (50+ design bar met)**. Improvement vs prior FINAL's THIN 43 midpoint | **PASS** |

**8 of 8 round-2 checks PASS.**

---

## LENS 1 — Truthfulness

### Tight-identifier sweep
- Emails (aurora.winona@starpm.com, tony.reyes@starpm.com, robert.finley@gmail.com, brooke.phillips@starpm.com, pete.donovan@gmail.com, service@alamohvac.com, billing@bigbendrestoration.com, tanya.mitchell@gmail.com): all present in Fact_Ledger ✓
- Airtable record IDs (rec7f6e5d4c3b2a1e, recb4aeaed326f156, rec8b679d92f30753, rec769c9f03f0b85f, rec3782834f35df50, rec8005502043b755, rec91517a5acab558, reca8230a8fd9ff51, recc83c05d889b354, receee45491536859, rec46234590708b5c, recc0ecc885e9645e): all present in Fact_Ledger and confirmed in `airtable.airtable_records.json` ✓
- Slack channels C001/C002/C003 confirmed ✓; QB DocNumbers 2026-481, PD-2026-084 confirmed; payment 972286822645 confirmed at Universe_Split line 2403 (TotalAmt 640.0, Robert Finley, LinkedTxn to invoice 110099741914) ✓
- $8,400 present in amounts ledger; $640 present ✓
- Zero references to invoice 2026-494 in any of the 3 artifacts ✓

### Answer-leakage scan
| Correct answer | In prompt? | In OE bodies? | In rubric title/evidence? | Verdict |
|---|---|---|---|---|
| "compressor failure" | No | Yes (OE7 expected discovery, OE9 message content prescription) | Yes (rubrics 2, 4, 11, 16) — normal criterion binding | PROMPT PASS ✓ |
| "$8,400" net exposure | Yes (line 5, intentional L13 first-framing anchor per Hardness_Plan) | Yes | Yes | Intentional anchor ✓ |
| "Unit 14" (Tanya current unit) | **No** (prompt is now implicit — "the unit reference on that record") | Yes (OE26/27/29/30/31) | Yes (R13 index 12, R20 index 20) | PROMPT PASS ✓ |
| "$640 payment applied elsewhere" | No | Yes (OE23) | Yes (R9, R19) | PROMPT PASS ✓ |
| "eviction filing package" / "breach" / "JP" | **No** (round-2 fix landed) | Yes (OE30, OE31, R15b, R21b) | Yes | PROMPT PASS ✓ |

**LENS 1: PASS** — no answer leakage in prompt; all intentional anchors accounted for.

---

## LENS 2 — Rubric Binding

- 24 rubrics, all category `outcome`. Category counts correct (Outcome 24 : Process 0). No em-dashes. No tool function names in titles. No "at least N" in titles.
- Delta-rubric focused audit:

| # | Title (summary) | Atomic | Dual-accept | Self-contained | Evidence cites OE | Verdict |
|---|---|---|---|---|---|---|
| Index 12 (R13) | Gmail names Unit 14 as Tanya's unit | Y | N — canonical Unit 14 only | Y | OE26/27/29/31 | PASS |
| Index 14 (R15a) | Gmail states payment plan breached on June 23 installment | Y — single claim | N | Y | OE27/OE29/OE30 | PASS |
| Index 15 (R15b) | Gmail states eviction filing package coordinated with JP | Y — single claim | N | Y | OE27/OE30/OE31 | PASS |
| Index 20 (R20) | Final response names Unit 14 as Tanya's unit | Y | N — canonical Unit 14 only | Y | OE26/27/29 | PASS |
| Index 21 (R21a) | Final response states payment plan breached on June 23 installment | Y — single claim | N | Y | OE27/OE29/OE30 | PASS |
| Index 22 (R21b) | Final response states eviction filing package coordinated with JP | Y — single claim | N | Y | OE27/OE30/OE31 | PASS |

Other 18 rubrics inherit LOW / LOW-MED risk profile from prior FINAL (unchanged): R7 requires both QB DocNumbers (LOW-MED, discriminating); R8/R9/R18/R19 use "owner receivable" terminology vs OE's "billing exposure" (LOW-MED — carried).

**LENS 2: PASS** — all delta rubrics atomic; dual-accept eliminated; AND-bundle split.

---

## LENS 3 — Cross-Artifact Holism

### Lever map

| Lever | Prompt trigger | OE trigger | Rubric trigger | Status |
|---|---|---|---|---|
| L9 (authority dismissal — compressor vs filter) | Line 3 (Tony Slack "want to know what actually came back from the inspection") | OE4–OE7 | R2, R4, R11, R16 | INTACT ✓ |
| L11 (net vs gross — $8,400 not $16,800) | Line 5 ("$8,400 approved scope"; "billing picture didn't come out clean") | OE18–OE20 | R7, R12, R17 | INTACT ✓ |
| L2 (structured-DB skip — PrivateNote only in QB) | Implicit ("real owner exposure") | OE18–OE21, OE23 | R7, R8, R9, R17, R18, R19 | INTACT ✓ |
| L8 (multi-link chain — Airtable → MT → 2× QB bill → payment) | Line 5 ("Figure out what the real owner exposure is") | OE10→11→14–17→18–20→23 | R7–R9, R17–R19 | INTACT ✓ |
| L6 (near-miss entity via record-freshness) | Line 7 ("the unit reference on that record" — implicit) | OE26 (7 records enumerated with timestamps), OE27 (July 1 record authoritative), OE29 (Slack pre-breach vs current-state disambiguation) | R13 (index 12) + R20 (index 20) — canonical Unit 14, evidence fails Las Palmas 4B | INTACT (REFRAMED) ✓ |

All 5 levers triggered end-to-end. L6 reframed from unit-label decoy count to record-freshness discriminator — still discriminates: agent that picks the 2026-06-12 pre-breach Las Palmas 4B record without reconciling against 2026-06-28 and 2026-07-01 Unit 14 records fails R13/R20/R15a/R15b/R21a/R21b.

### Forward/reverse map
Every prompt ask maps to ≥1 OE + ≥1 rubric ✓. Every OE/rubric traces back to a prompt ask ✓.

### Entity consistency
All 11 named entities (208B, Tony, Alamo HVAC, Ridgeview, Robert Finley, Big Bend, QB bills, QB payment, Tanya, Unit 14, Aurora) now consistent across prompt / OE / rubric namespaces. Tanya unit + payment-plan state resolved consistently: unit = Unit 14, status = breach + JP coordination underway.

### Density
Baseline midpoint: 50.0 (per Hardness_Plan). OE27 reconciliation adds +2 to +4 defensive re-reads → **midpoint ~52-54, tier PASS (50+)**. Improvement over prior FINAL's THIN 43.

**LENS 3: PASS.**

---

## LENS 4 — Red-Team Adversarial

### Shortcut path
An agent that follows the updated OE literally (OE27 reconciliation across 4 records + July 1 as authoritative):
- PASS R13 (Unit 14) ✓
- PASS R14 (ESA — mentioned in OE30) ✓
- PASS R15a (breach — OE27, OE30) ✓
- PASS R15b (JP coordination — OE27, OE30, OE31) ✓
- PASS R20/R21a/R21b (same) ✓
- PASS R22 (ESA — OE30) ✓

An agent that latches on the older Las Palmas 4B record without reconciling:
- FAIL R13 / R20 (evidence explicitly fails Las Palmas 4B or no unit) — L6 stump triggered as intended
- Likely FAIL R15a/R15b/R21a/R21b (agent thinks payment plan is still active)

No coin-flip anymore — the OE and rubric now agree; latching-vs-reconciling is a real hardness discriminator, not a rubric ambiguity.

### Second-reading analysis
Prompt line 7 ("the unit reference on that record") is intentionally ambiguous (implicit hardness). OE26/OE27 direct the agent to enumerate all Tanya records and reconcile by timestamp; if the agent skips reconciliation, they fail L6. This is by design and matches Hardness_Plan L6 framing.

### Drift sweep (all 3 files)
- Em-dashes: 0 ✓
- "at least N" in rubric titles: 0 ✓
- Tool function names in rubric titles: 0 ✓
- Keystone tokens (mortgage_los, stripe, keystonemortgage.com): 0 ✓
- MoveOps tokens (crm_create_engagement in wrong places, teamId variant): 0 ✓
- Brookfield tokens (oracle_gl, sap_subledger, blackline, records_vault, IOLTA, AICPA_SQMS_7Y, IRS_TAX_7Y, 105000, 120000, brookfield, northstar_legal, acme_cloud): 0 ✓

**LENS 4: PASS.**

---

## LENS 5 — Narrative-State + Action-Prescription

### State-implying claims vs universe lifecycle

Universe atoms as of 2026-07-01 (verified directly against `airtable.airtable_records.json`):

| Record | Created | fldUnit | State supported | OE alignment |
|---|---|---|---|---|
| rec769c9f03f0b85f | 2026-06-12 | Las Palmas 4B | payment plan active *as of 2026-06-12* | OE26/OE27 mark as pre-breach, superseded ✓ |
| rec8005502043b755 | 2026-06-21 | Tanya Mitchell - Delinquency Escalation | payment plan BREACHED after June 23 installment | OE26/OE27 include in reconciliation timeline ✓ |
| rec91517a5acab558 | 2026-06-28 | Unit 14 | 3-day notice served June 26, compliance deadline June 29 | OE26/OE27 include as current-state ✓ |
| recc83c05d889b354 | 2026-07-01 | Unit 14 | Eviction petition being coordinated with JP | OE27 names as **authoritative on current-state** ✓ |

Ground-truth CURRENT state as of universe today 2026-07-01: payment plan BREACHED (June 23 installment), 3-day notice EXPIRED (June 29 no cure), eviction filing package COMPILED AND OWNER-APPROVED, JP coordination UNDERWAY, ESA reasonable-accommodation request on file (parallel Fair Housing track).

Rubrics R15a / R15b / R20 / R21a / R21b / R14 / R22 test for this state exactly. OEs now match. Zero contradictions.

### Action-prescription binding to StarPM conventions
- Airtable update rec7f6e5d4c3b2a1e — OE8 uses `update_records_for_table(baseId, tableId, records)` ✓
- Slack C001 send — OE9 uses `slack_send_message(channel_id: "C001", message: ...)` ✓ (StarPM `message`, not `payload`)
- Linear save_issue with `team: "OPS"` — OE25 ✓ (StarPM `team`, not `teamId`)
- Gmail draft to aurora.winona@starpm.com — OE31 uses `create_draft(to, subject, body)` ✓ (StarPM `body`, not `content`; draft-only ✓)

### Lifecycle preconditions
No GL, no locked period, no lifecycle-locked writes. NA ✓.

**LENS 5: PASS.**

---

## LENS 6 — Verifier-Fails-Spec Pre-Upload Check

Rubric-by-rubric Bucket-1 (Rubric Invalid) risk scan under strict interpretation:

| Range | Description | Bucket-1 pattern | Risk |
|---|---|---|---|
| Indices 0-5 | Airtable update + Slack + Linear write-actions (R1-R6) | none | LOW |
| Index 6 (R7) | Linear: $8,400 single job + names both bill DocNumbers | AND-adjacent (single reconciliation) — discriminating | LOW-MED (carried from prior) |
| Indices 7-8, 17-18 | R8, R9, R18, R19 use "owner receivable" vs OE "billing exposure" | terminology gap | LOW-MED (carried) |
| Indices 9-13, 16, 19, 23 | Standard atomic outcome rubrics (R10-R14, R16, R19, R22) | none | LOW |
| Index 12 (R13) | Gmail: canonical Unit 14 (evidence fails Las Palmas 4B) | Single canonical answer matched by OE + Hardness_Plan; record-freshness discriminator is intentional hardness | LOW |
| Index 14 (R15a) | Gmail: payment plan breached on June 23 | Atomic, single claim, matches OE27/OE29/OE30 | LOW |
| Index 15 (R15b) | Gmail: eviction filing with JP | Atomic, single claim, matches OE27/OE30/OE31 | LOW |
| Index 20 (R20) | Final: canonical Unit 14 (same as R13) | LOW | LOW |
| Index 21 (R21a) | Final: payment plan breached on June 23 (same as R15a) | LOW | LOW |
| Index 22 (R21b) | Final: eviction filing with JP (same as R15b) | LOW | LOW |

**HIGH-risk Bucket-1 count: 0 / 24 = 0%** — well under 20% REVISE threshold. Zero HIGH-risk rubrics after round-2 fixes; the 4 HIGH-risk rubrics from round 1 (R13/R15/R20/R21) all became atomic and canonical.

**LENS 6: PASS.**

---

## HARD RULES VERIFICATION

| # | Rule | Status | Evidence |
|---|---|---|---|
| 1 | Correct derived figure never in prompt (excluding intentional $8,400 anchor) | PASS | "eviction filing package", "breach", "JP", "Unit 14" all absent from prompt |
| 2 | Every tight identifier exists in Fact_Ledger / Universe_Split | PASS | All emails, record IDs, QB IDs, Slack channels, payment ID verified against raw universe data |
| 3 | Every Hardness lever triggered end-to-end (L9, L11, L2, L8, L6) | PASS | All 5 levers intact; L6 reframed as record-freshness, still discriminates |
| 4 | Integrated density: 50+/PASS, 40–49/THIN, <40/BLOCKER | PASS | ~52-54 midpoint post round-2 OE27 expansion (up from THIN 43 in round 1) |
| 5 | Outcome > Process | PASS | 24:0 |
| 6 | No tool function names in rubric titles | PASS | 0 hits |
| 7 | No em-dashes | PASS | 0 hits in all 3 files |
| 8 | Entity references consistent across prompt / OE / rubrics | PASS | Tanya unit = Unit 14, breach + JP consistent everywhere; older 4B row explicitly framed as pre-breach superseded |
| 9 | Implicit-prompt framing preserved | PASS | Prompt line 7 is implicit ("her current status and the unit reference on that record"); no rubric demands a step the prompt blocks |
| 10 | Every state-implying claim matches universe lifecycle | PASS | OE27's "recc83c05d889b354 (2026-07-01) is authoritative on current-state" matches universe atoms exactly |
| 11 | Every prompt action aligns with universe record-prescribed action | PASS | All 4 writes (Airtable update, Slack C001 send, Linear create, Gmail draft) have single valid target |
| 12 | Every OE tool-parameter binding on exact StarPM named tool | PASS | slack `message`, gmail `body`, linear `team`, airtable `baseId/tableId` all correct |
| 13 | Every lifecycle-locked write has prerequisite unlock | NA | StarPM has no GL period lock |
| 14 | ≤ 20% of rubrics surface as Bucket_1_Risk HIGH | PASS | 0/24 = 0% |

**14 of 14 hard rules PASS (13 PASS + 1 NA).**

---

## VERDICT: PASS

All 5 round-1 defects fully resolved with zero new BLOCKER regressions. All 6 lenses PASS. All 14 hard rules PASS. Density improved from THIN (43) to PASS (~52-54) as a side benefit of the OE27 reconciliation expansion. Rubric count 24 outcome / 0 process. L6 lever restored via record-freshness reframing — Unit 14 canonical, evidence fails Las Palmas 4B or no-unit responses. OE ground-truth now consistent with rubric expected state and with universe atoms.

Ready for platform upload.

