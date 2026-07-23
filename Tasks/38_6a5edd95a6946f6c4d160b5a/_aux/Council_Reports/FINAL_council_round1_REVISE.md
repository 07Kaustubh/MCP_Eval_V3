# FINAL Council — Cross-Artifact Holistic Review (RE-RUN)

**Task:** 38_6a5edd95a6946f6c4d160b5a (StarPM)
**Artifacts:** 5_Prompt.txt (9 lines) / 6_Oracle_Events.txt (31 OE steps, ~15KB) / 7_Rubrics.json (22 rubrics, 22 outcome / 0 process)
**Review Date:** 2026-07-22 (re-run against artifacts modified ~06:02–06:03 today)
**Prior FINAL:** _aux/Council_Reports/FINAL_council_prev_0221.md — PASS at 02:21. **STALE.** Rubrics 13/15/20/21 and prompt line 7 were subsequently modified. Prior verdict does NOT carry.
**Validator sweep this pass:** em-dashes = 0 in all 3 files; 2026-494 references = 0; tool function names in rubric titles = 0; outcome/process = 22/0; `$16,800` appears only as intentional negative comparator (L11 trap value).
**Universe today:** 2026-07-01 America/Chicago

---

## DRIFT SUMMARY (vs prior FINAL 02:21)

| Area | Prior state | Current state | Verdict |
|---|---|---|---|
| Prompt line 7 (Tanya section) | "Look up Tanya move-out status; confirm which unit she's in" (implicit) | "Pull up her make-ready record and confirm where the eviction filing package stands, including the unit reference on that record" | **CHANGED — introduces answer-leakage on "eviction filing package"** |
| Rubric 13 (Gmail unit) | Required "Las Palmas 4B" | Accepts EITHER "Las Palmas 4B" OR "Unit 14 / Sunset Ridge Unit 14" | **CHANGED — dual-accept, L6 discriminator deleted** |
| Rubric 15 (Gmail Tanya status) | Required "payment plan active through July" | Requires "payment plan breached on June 23 installment AND eviction filing package coordinated with Justice of the Peace" | **CHANGED — new AND-bundle** |
| Rubric 20 (Final unit) | Required "Las Palmas 4B (not Unit 14)" | Accepts EITHER unit reference | **CHANGED — dual-accept, L6 discriminator deleted** |
| Rubric 21 (Final Tanya status) | Required "payment plan July" | Requires "breach + JP coordination" | **CHANGED — new AND-bundle** |
| OE27, OE30, OE31 | Direct agent to Las Palmas 4B + "payment plan active through end of July" | **UNCHANGED** — still directs agent to Las Palmas 4B + "payment plan active" | **NOT UPDATED — now contradicts current rubrics** |
| Hardness_Plan L6 | Las Palmas 4B = correct, Unit 14 = decoy | **UNCHANGED** — still names Las Palmas 4B as correct | **NOT UPDATED — inconsistent with current rubric dual-accept** |

The three changes are internally inconsistent with each other AND with the OE and Hardness_Plan. This is the drift the re-run was designed to catch.

---

## LENS 1 — Truthfulness

### Tight-identifier sweep
All emails (aurora.winona@starpm.com, tony.reyes@starpm.com, robert.finley@gmail.com, brooke.phillips@starpm.com, pete.donovan@gmail.com, service@alamohvac.com, billing@bigbendrestoration.com, tanya.mitchell@gmail.com) ✓ in Fact_Ledger.
All Airtable IDs (rec7f6e5d4c3b2a1e, recb4aeaed326f156, rec8b679d92f30753, rec769c9f03f0b85f, rec3782834f35df50, rec8005502043b755, rec91517a5acab558, reca8230a8fd9ff51, recc83c05d889b354, receee45491536859, rec46234590708b5c, recc0ecc885e9645e) ✓ in Fact_Ledger.
Slack channels C001/C002/C003 ✓. QB DocNumbers 2026-481, PD-2026-084 and payment 972286822645 ✓ (internal IDs 528539050604 / 301715729067 verified from prior). $8,400 ✓. $640 ✓. No reference to invoice 2026-494 anywhere ✓.

### Answer-leakage scan
| Correct answer | In prompt? | In OE bodies read by agent? | In rubric title/evidence readable by judge? | Verdict |
|---|---|---|---|---|
| "compressor failure" | No ✓ | Yes (OE7 expected discovery; agent sees the email content itself, which is designed leakage into universe not prompt) | Rubric titles/evidence — YES (rubrics 2,4,11,16 explicitly state "compressor failure") — this is normal (rubric criterion must name the correct value); leakage test is the PROMPT | PROMPT PASS ✓ |
| "$8,400" net exposure | Yes (line 5: `the "$8,400 approved scope" from the back-and-forth with Robert`) | Yes | Yes | **Intentional L13 first-framing anchor per Hardness_Plan** ✓ |
| "Las Palmas 4B" | No ✓ | Yes (OE26, OE27, OE29, OE31) | Yes (R13, R20) | PROMPT PASS ✓ |
| "$640 payment applied to separate invoice" | No ✓ | Yes (OE23) | Yes (R9, R19) | PROMPT PASS ✓ |
| **"eviction filing package"** | **YES — prompt line 7: "confirm where the eviction filing package stands"** | Yes (OE31 body) | Yes (R15, R21) | **[LEAKAGE — MAJOR]** — prompt tells agent the eviction filing package exists AND asks about its status. Signals to agent that a payment-plan-active reading is stale and pushes them toward the eviction-track records. Softens L1 latching, softens L6, and pre-solves half of R15/R21. |

**LENS 1: MAJOR** — prompt line 7 leaks "eviction filing package" as a state anchor. Combined with the corresponding rubric AND-bundle (breach + JP filing), the prompt is doing half the work the rubric is supposed to reward.

---

## LENS 2 — Rubric Binding

22 rubrics, all category `outcome`. Category counts correct (Outcome 22 : Process 0). No em-dashes. No tool function names in titles. No "at least N" in titles.

Focused audit on the delta rubrics vs prior FINAL:

| # | Title | Atomic | Too-tight | Too-loose | Self-contained | Evidence cites OE | Notes |
|---|---|---|---|---|---|---|---|
| R13 (index 12) | Gmail unit reference — accepts Las Palmas 4B **OR** Unit 14 | N | N | **YES — dual-accept** | Y | OE26/27/31 | Judge is told either passes. This is the classic Lens 6 Bucket-1 "dual-acceptance when prompt named a single canonical answer" anti-pattern. The prompt says "the unit reference on THAT record" (singular record); the rubric substitutes "any record." See Lens 3 lever regression. |
| R15 (index 14) | Gmail: breach on June 23 installment **AND** JP coordination | **N — 2 independent claims** | Marginal | N | Y | OE27/OE30/OE31 | AND-bundle. Agent that states breach without JP fails; agent that states JP without breach fails. Should be split into two atomic rubrics. |
| R20 (index 19) | Final unit reference — same dual-accept as R13 | N | N | **YES — dual-accept** | Y | OE26/27 | Same defect as R13. |
| R21 (index 20) | Final: breach + JP coordination | **N — 2 independent claims** | Marginal | N | Y | OE27/OE31 | Same defect as R15. |

Other 18 rubrics inherit LOW/LOW-MED risk profile from prior FINAL (R7 requires both QB DocNumbers — discriminating, LOW-MED; R8/R9/R18/R19 use "owner receivable" vs OE's "billing exposure" terminology — LOW-MED). Prior FINAL analysis of these carries.

**LENS 2: FAIL (BLOCKER)** — R13, R15, R20, R21 each break either atomicity or the "no dual-accept for a single canonical answer" rule.

---

## LENS 3 — Cross-Artifact Holism

### Lever map (against Hardness_Plan.md, unchanged since S1)

| Lever | Prompt trigger | OE trigger | Rubric trigger | Status |
|---|---|---|---|---|
| L9 (authority dismissal — compressor vs filter) | Line 3 (Tony Slack, "want to know what actually came back from the inspection") | OE4–OE7 | R2, R4, R11, R16 | **INTACT** ✓ |
| L11 (net vs gross — $8,400 not $16,800) | Line 5 ("$8,400 approved scope"; "billing picture didn't come out clean") | OE18–OE20 | R7, R12, R17 | **INTACT** ✓ |
| L2 (structured-DB skip — PrivateNote only in QB) | Implicit ("real owner exposure") | OE18–OE21, OE23 | R7, R8, R9, R17, R18, R19 | **INTACT** ✓ |
| L8 (multi-link chain — Airtable → MT → 2× QB bill → payment) | Line 5 ("Figure out what the real owner exposure is") | OE10→11→14–17→18–20→23 | R7–R9, R17–R19 | **INTACT** ✓ |
| L6 (near-miss entity — Las Palmas 4B vs 7× Unit 14) | Line 7 ("the unit reference on that record") | OE26 (decoys returned), OE27 (Las Palmas 4B "authoritative"), OE29 | R13, R20 | **REGRESSED — DELETED by dual-accept in R13/R20; Hardness_Plan still calls Las Palmas 4B the correct answer and lists Unit 14 as Stump Hypothesis #3 failure mode; current rubrics reward the failure mode** |

**[BLOCKER B1] L6 lever regression.** Per drift-check instructions: "if rubrics accept BOTH 'Las Palmas 4B' and 'Unit 14' without prompt disambiguation, L6 is effectively DELETED and this is a lever-regression BLOCKER." Confirmed. Hardness_Plan.md lines 20, 39, 85 all designate Las Palmas 4B as the correct discriminator and enumerate Unit 14 as the wrong answer; current R13/R20 pass both. Reducing lever count from 5 → 4 drops the hardness bar below the 5-lever design target.

### Forward/reverse map
Every prompt ask still maps to ≥1 OE + ≥1 rubric ✓. Every OE/rubric still traces back to a prompt ask ✓.

### Entity consistency
All 11 named entities (208B, Tony, Alamo HVAC, Ridgeview, Robert Finley, Big Bend, QB bills, QB payment, Tanya, Las Palmas 4B, Aurora) match across prompt/OE/rubric namespaces ✓ **except** the Tanya unit reference which is genuinely ambiguous across the universe (see Lens 5).

### Density
No OE steps added/removed since prior FINAL. Direct OE tool-call count ~37; with retries/nav +15–20% → **midpoint ~43**, tier THIN_DENSITY (40–49). Per-task justification (5 stump vectors) carried from S2/Hardness — but see B1: L6 is now effectively deleted, so only 4 stump vectors remain, weakening the THIN-density justification.

**LENS 3: FAIL (BLOCKER B1 — L6 lever regression).** Density also weakens from 5-lever to 4-lever compensating complexity.

---

## LENS 4 — Red-Team Adversarial

### Shortcut path
An agent that reads OE27/OE30/OE31 literally (following the "authoritative Las Palmas 4B, payment plan active through July" framing baked into the OE) will:
- PASS R13 (Las Palmas 4B is accepted) ✓
- **FAIL R14** (ESA — must remember to include separately)
- **FAIL R15** (says "payment plan active"; rubric requires "breached + JP") ✗
- **FAIL R21** (same) ✗
- PASS R20 (Las Palmas 4B accepted) ✓
- **FAIL R22** (ESA — same as R14) unless included

An agent that instead reads the eviction-track records (rec3782834f35df50, rec8005502043b755, rec91517a5acab558, recc83c05d889b354, receee45491536859) will:
- PASS R13 (Unit 14 accepted) ✓
- PASS R15 (finds breach + JP) ✓
- PASS R20, R21 ✓
- **FAIL** the OE's "authoritative" designation

Both paths pass some rubrics and fail others depending solely on which storyline they latch onto **first**. This is now the entire task's Tanya-section outcome — a coin flip driven by L1 latching, not by the L6 discriminator the Hardness_Plan called for.

### Second-reading analysis
Prompt line 7 has TWO valid readings:
1. "The unit reference on that record" = the make-ready record (singular) → agent must pick ONE record → ambiguous (rec769c9f03f0b85f = 4B; recc83c05d889b354 = Unit 14; both are current-state make-ready records with different unit labels)
2. "The eviction filing package" is one specific artifact → agent looks for eviction-package records → Unit 14 records win → answer is Unit 14

Reading (2) is what the prompt actually pushes toward. But R13/R20 accept either — so the prompt says "look at the eviction record" while the rubric says "any record OK." Internally inconsistent.

### Drift sweep (all 3 files)
- Em-dashes: 0 ✓ (`--` and `-` only)
- "at least N" in rubric titles: 0 ✓
- Tool function names in rubric titles: 0 ✓ (Airtable/Slack/Linear/Gmail/QuickBooks are platform names, allowed)
- Keystone tokens (mortgage_los, stripe, @keystonemortgage.com): 0 ✓
- MoveOps tokens (`airtable_update_records`, `linear_create_issue`, `crm_create_engagement` in wrong places): 0 ✓
- Brookfield tokens (oracle_gl, sap_subledger, blackline, records_vault, brookfield, northstar_legal, acme_cloud, IOLTA, AICPA_SQMS_7Y, IRS_TAX_7Y, 105000, 120000): 0 ✓

**LENS 4: FAIL (BLOCKER — coin-flip pass rate from OE/rubric contradiction; MAJOR from prompt/rubric second-reading divergence).**

---

## LENS 5 — Narrative-State + Action-Prescription

### State-implying claims vs universe lifecycle

Universe atoms as of today (2026-07-01) — verified directly against Universe_Split:

| Airtable make-ready record | Created | fldUnit | fldNotes2 (excerpt) | State supported |
|---|---|---|---|---|
| rec769c9f03f0b85f | **2026-06-12** | Las Palmas 4B | "payment plan agreement... active repayment schedule... Holding this turn as Scheduled pending payment plan compliance through end of July" | payment plan active *as of 2026-06-12* |
| rec8005502043b755 | **2026-06-21** | Tanya Mitchell - Delinquency Escalation | "Payment plan status updated to Payment Plan Breached - No Response after the June 23 installment went unmet" | **breach confirmed** |
| rec91517a5acab558 | **2026-06-28** | Unit 14 | "3-Day Notice to Pay or Quit served June 26; compliance deadline June 29" | **3-day notice served** |
| recc83c05d889b354 | **2026-07-01** | Unit 14 | "Eviction petition for Tanya Mitchell is currently being coordinated with the Justice of the Peace" | **JP coordination underway (today)** |

Slack C003 timeline confirms the same progression:
- 2026-06-12: "unit 4B... payment plan is signed and filed"
- 2026-06-28: "Tanya Mitchell's payment plan is now breached... 3-day notice has been served to Tanya Mitchell in Unit 14"
- 2026-06-28: "If Tanya Mitchell doesn't pay or vacate by then, we move forward with the JP eviction filing"
- 2026-07-01: "Filing package is complete and owner-approved. JP coordination is underway"

**Ground-truth CURRENT state as of universe today 2026-07-01: payment plan BREACHED (June 23), 3-day notice EXPIRED (June 29 no cure), eviction filing package COMPILED AND OWNER-APPROVED, JP coordination UNDERWAY.**

Rubrics R15 and R21 test for this state exactly. **The rubrics are correct.**

But:
- **OE27 says:** "record rec769c9f03f0b85f is the **current-status entry**: unit Las Palmas 4B, status selSched, payment plan active, holding through end of July"
- **OE30 says:** "unit Las Palmas 4B, payment plan active through end of July, ESA request on file"
- **OE31 body says:** "unit is Las Palmas 4B (multiple Unit 14 records in the system are separate eviction/delinquency tracks, not her current unit); payment plan is active through end of July"

**[BLOCKER B2] OE ↔ Rubric contradiction on Tanya current state.** OE27/OE30/OE31 direct the agent to a June-12 record and label it "current-status" / "authoritative." Rubrics R15 and R21 require the agent to report the June-28 → July-1 state (breach + JP). An agent that follows the OE literally FAILS R15 and R21. An agent that ignores the OE and finds the correct current state PASSES R15/R21 but violates OE27's "authoritative" framing. This is a Lens 5 Narrative-State BLOCKER — rubric expected state does not match the OE's stated ground truth.

Additionally OE31's drafting instruction actively tells the agent to write "multiple Unit 14 records in the system are separate eviction/delinquency tracks, not her current unit" — a phrasing that is DIRECTLY WRONG per the July-1 Airtable record recc83c05d889b354 (which IS her current-unit eviction record).

### Action-prescription
- Airtable update rec7f6e5d4c3b2a1e — OE8 ✓
- Slack C001 send — OE9 ✓
- Linear save_issue with `team: "OPS"` — OE25 ✓ (StarPM param = `team`, not `teamId`)
- Gmail draft to aurora.winona@starpm.com — OE31 ✓ (StarPM `body`, not `content`; draft-only ✓)

### Tool-parameter binding (StarPM conventions)
- `slack_send_message(channel_id, message)` — OE9 uses `message` ✓
- `create_draft(to[], subject, body)` — OE31 uses `body` ✓
- `save_issue(..., team, ...)` — OE25 uses `team` ✓
- `update_records_for_table(baseId, tableId, records)` — OE8 ✓
- `search_records(baseId, table, query)` — OE3, 10, 11, 26, 27, 28 ✓
- `contacts_search_contacts(query)` — OE1, 2, 12, 13, 22 ✓

### Lifecycle preconditions
No GL, no locked period, no lifecycle-locked writes. NA ✓.

**LENS 5: FAIL (BLOCKER B2 — OE/Rubric ground-truth contradiction).**

---

## LENS 6 — Verifier-Fails-Spec Pre-Upload Check

Rubric-by-rubric Bucket-1 (Rubric Invalid) risk scan under strict interpretation:

| # | Rubric summary | Bucket-1 pattern hit | Risk |
|---|---|---|---|
| R1–R6 | Airtable update + Slack + Linear write-actions | none | LOW |
| R7 | Linear: $8,400 single job + names both bill DocNumbers | AND-adjacent (single reconciliation) — discriminating | LOW-MED (carried from prior) |
| R8, R9, R18, R19 | "owner receivable" / "AR balance" terminology vs OE's "billing exposure" | terminology gap | LOW-MED (carried) |
| R10–R12, R14, R16, R17, R22 | Standard atomic outcome rubrics | none | LOW |
| **R13** | **Gmail: unit reference — "either Las Palmas 4B OR Unit 14 / Sunset Ridge Unit 14"** | **Dual-acceptance pattern (explicit "either X or Y" when prompt used the singular "the unit reference on that record")** | **HIGH** |
| **R15** | **Gmail: "breach on June 23 installment AND eviction filing package with JP"** | **AND-bundle of two independent claims** — also **per-rubric cross-artifact mismatch** (OE says "payment plan active") | **HIGH** |
| **R20** | **Final: unit reference — same dual-accept as R13** | Same as R13 | **HIGH** |
| **R21** | **Final: breach + JP same as R15** | Same as R15 | **HIGH** |

**HIGH-risk Bucket-1 count: 4 / 22 = 18.2% — under the 20% REVISE threshold but only marginally.** Note that R15 and R21 additionally fail the per-rubric cross-artifact mismatch check (rubric value disagrees with matching OE step value at OE27/OE30/OE31) — that mismatch is called out separately as BLOCKER B2 above.

**LENS 6: MAJOR** (HIGH-risk count at 18.2%, below 20% threshold in absolute terms, but two HIGH rubrics also feed the OE/rubric contradiction BLOCKER — the fragility is not purely rubric-side; it is a systemic inconsistency).

---

## HARD RULES VERIFICATION

| # | Rule | Status | Evidence |
|---|---|---|---|
| 1 | Correct derived figure never in prompt/OE/rubric bodies (excluding intentional $8,400 anchor) | **MAJOR** | "eviction filing package" leaked in prompt line 7 (state anchor for R15/R21) |
| 2 | Every tight identifier exists in Fact_Ledger/Universe_Split | PASS | All emails, record IDs, QB IDs, Slack channels, payment ID verified |
| 3 | Every Hardness lever triggered end-to-end (L9, L11, L2, L8, L6) | **BLOCKER (B1)** | L9/L11/L2/L8 intact; L6 REGRESSED — R13/R20 dual-accept deletes discriminator |
| 4 | Integrated density: 50+/PASS, 40–49/THIN, <40/BLOCKER | THIN | ~43 midpoint (unchanged since prior FINAL); THIN justification weakens because L6 no longer contributes |
| 5 | Outcome > Process | PASS | 22:0 |
| 6 | No tool function names in rubric titles | PASS | 0 hits from tool-name scan |
| 7 | No em-dashes | PASS | grep count = 0 in all 3 files |
| 8 | Entity references consistent across prompt/OE/rubrics | **BLOCKER (B2)** | Tanya unit + payment-plan-status inconsistent between OE27/30/31 and R15/R21 |
| 9 | Implicit-prompt framing preserved (no rubric demands step prompt blocks) | PASS | No rubric requires an investigation step blocked by prompt |
| 10 | Every state-implying claim matches universe lifecycle | **BLOCKER (B2)** | OE27's "payment plan active, current-status" is stale by 19 days per universe atoms; OE31 body prescribes wrong prose to agent |
| 11 | Every prompt action aligns with universe record-prescribed action | PASS | All 4 writes have single valid target |
| 12 | Every OE tool-parameter binding on exact StarPM named tool | PASS | slack `message`, gmail `body`, linear `team`, airtable `baseId/tableId` all correct |
| 13 | Every lifecycle-locked write has prerequisite unlock | NA | StarPM has no GL period lock |
| 14 | ≤ 20% of rubrics surface as Bucket_1_Risk HIGH | PASS (marginal) | 4/22 = 18.2% HIGH — under threshold; noted that 2 of those 4 also drive BLOCKER B2 |

---

## VERDICT: REVISE

Two BLOCKERs plus one MAJOR answer-leakage. The three defects reinforce each other — B2 (OE/rubric contradiction) and the "eviction filing package" prompt leak both flow from a partial rubric revision that was applied to 7_Rubrics.json but not propagated back to 6_Oracle_Events.txt, and B1 (L6 regression) flows from patching the same rubrics to hedge the ambiguity created by that revision.

### Exact-fix items (numbered, keyed by artifact + location)

**[BLOCKER 1] — Fix OE/Rubric contradiction (Lens 5 B2). Choose ONE of Option A or Option B and apply consistently across OE + rubrics + Hardness_Plan.**

- **Option A — Rubrics are correct; OE must be updated to match universe truth as of 2026-07-01.**
  1. **6_Oracle_Events.txt OE27 (line 53):** Replace the "current-status entry" prose. New text should direct the agent to reconcile rec769c9f03f0b85f (June-12 payment plan) with rec8005502043b755 (June-21 breach), rec91517a5acab558 (June-28 3-day notice), and recc83c05d889b354 (July-1 JP coordination), and treat the July-1 record as authoritative. Expected discovery: payment plan BREACHED on June 23 installment; 3-day notice expired June 29 with no cure; eviction filing package compiled and owner-approved; JP coordination underway.
  2. **6_Oracle_Events.txt OE30 (line 59):** Replace "payment plan active through end of July" with "payment plan breached on the June 23 installment; eviction filing package compiled and owner-approved; JP coordination underway; ESA reasonable-accommodation request on file (parallel Fair Housing track)."
  3. **6_Oracle_Events.txt OE31 (line 61):** In the drafting instructions, replace "(3) Tanya Mitchell: unit is Las Palmas 4B (multiple Unit 14 records in the system are separate eviction/delinquency tracks, not her current unit); payment plan is active through end of July; ESA request is on file" with "(3) Tanya Mitchell: unit reference per current-state make-ready records; payment plan breached on June 23 installment; 3-day notice expired June 29 with no cure; eviction filing package compiled and owner-approved; JP coordination underway; ESA reasonable-accommodation request on file (parallel Fair Housing track)."
  4. **_aux/Hardness_Plan.md line 39 and Stump Hypothesis #3 (line 85):** Rebase L6 or remove L6 — see BLOCKER 2 below.

- **Option B — OE is correct; rubrics must be reverted to prior "payment plan active" reading.**
  1. **7_Rubrics.json rubric 15 (index 14):** Revert title to "The Agent's Gmail draft to aurora.winona@starpm.com states that Tanya Mitchell's payment plan is active through the end of July."
  2. **7_Rubrics.json rubric 21 (index 20):** Revert title to "The Agent's final response states that Tanya Mitchell's payment plan is active through the end of July."
  3. **5_Prompt.txt line 7:** Revert to a framing that does not name "eviction filing package" (e.g., "The Tanya Mitchell escalation also goes in the brief. Pull up her make-ready record and confirm her current status and unit reference.").
  4. Rubrics 13 and 20 also need revision — see BLOCKER 2.

*Recommendation: Option A. The universe atoms as of 2026-07-01 clearly support breach + JP filing; Option B would ship a task whose "correct" answer is 19 days stale relative to universe today, which will hit trajectory difficulty problems on real runs.*

**[BLOCKER 2] — Fix L6 lever regression (Lens 3 B1). Choose ONE of Option A or Option B.**

- **Option A — Keep L6 as a discriminator. Tighten rubrics 13 and 20 to require ONE specific unit reference.**
  1. **7_Rubrics.json rubric 13 (index 12):** Replace title with "The Agent's Gmail draft to aurora.winona@starpm.com names Unit 14 (per the eviction-track make-ready records) as Tanya Mitchell's unit reference." (Choose Unit 14 given that BLOCKER 1 Option A repositions the eviction-track records as authoritative. If Option B was taken above, choose Las Palmas 4B.)
  2. **7_Rubrics.json rubric 13 evidence:** Update to test only the chosen unit reference; remove the "or" clause and the dual-track discussion.
  3. **7_Rubrics.json rubric 20 (index 19):** Same tightening as R13.
  4. **_aux/Hardness_Plan.md line 20/39/85:** Update L6 designation to match the chosen canonical answer.

- **Option B — Retire L6 as a lever. Delete rubrics 13 and 20; renumber. Hardness_Plan drops to 4 levers; hardness score re-computed; density THIN justification re-issued on 4-lever basis.**

*Recommendation: Option A with Unit 14 as the canonical answer, since the eviction-track records are the authoritative current-state records per universe today.*

**[MAJOR 3] — Remove or soften prompt line 7 answer leakage (Lens 1).**
1. **5_Prompt.txt line 7:** Replace "confirm where the eviction filing package stands, including the unit reference on that record" with something that does not disclose that an eviction filing package exists. Example: "confirm her current escalation status and the unit reference on her active make-ready record." This preserves the ask while removing the "eviction filing package" pre-solve.
2. If BLOCKER 2 Option A is taken and Unit 14 becomes canonical, keep the prompt framing implicit — do not name the specific escalation stage.

**[MAJOR 4] — Split AND-bundle in R15 and R21.**
1. **7_Rubrics.json rubric 15 (index 14):** Split into two atomic rubrics: R15a "states payment plan was breached on the June 23 installment"; R15b "states eviction filing package is coordinated with the Justice of the Peace."
2. **7_Rubrics.json rubric 21 (index 20):** Same split (R21a / R21b).

### After fixes
Re-run FINAL. Expect PASS if (a) OE lines 53/59/61 match rubric ground-truth, (b) R13 and R20 name a single canonical unit reference matched by Hardness_Plan, (c) prompt line 7 no longer names "eviction filing package," and (d) R15/R21 are split into 4 atomic rubrics (final count 24 outcome / 0 process).

Also re-check density after OE27/OE30/OE31 revisions — the reconciliation-across-4-records instruction in OE27 (Option A) adds ~3 more tool calls, pushing midpoint from 43 → ~46 (still THIN but stronger). If the 4-lever fallback (BLOCKER 2 Option B) is taken instead, density THIN justification MUST be re-issued on the reduced lever count.
