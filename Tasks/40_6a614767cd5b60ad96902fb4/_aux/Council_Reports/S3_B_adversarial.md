# Council B — S3 Adversarial Rubric Review (round 2 — revised 16-rubric set)

**Task:** `Tasks/40_6a614767cd5b60ad96902fb4` · **Universe:** StarPM (V4) · **Today:** 2026-07-01 America/Chicago
**Artifact:** `7_Rubrics.json` — 16 Outcome (0 Process) · **Persona:** Lisa Smith (onsite PM), delegating
**Reading:** STRICT (5/5 only when no defensible objection; every "should" read as "must") · **Mode:** read-only
**Timestamp:** 2026-07-23

## Supersession note (round 1 BLOCK → resolved)

A prior Council B round BLOCKed a **15-rubric predecessor** on 4 issues. The current file is the **revised 16-rubric set**; all 4 are confirmed resolved by direct comparison to the current file:

| Round-1 issue (15-rubric draft) | Severity | Resolution in current 16-rubric file |
|---|---|---|
| R9 bundled qualitative state + exact `$2,132.00` in one criterion | Moderate | **Split** → `[8]` (delinquent + active eviction, not resolved by 7214; **no amount**) + `[9]` (arrears `$2,132.00` on QR-2026-0441; **amount only**). The bundled text no longer exists. |
| R15 bundled turn-hold (S1) + account-eviction (S2) in the OPS-32 comment | Moderate | **De-bundled** → `[15]` now states turn-hold only ("held and not advanced because possession has not been returned"); account-eviction lives on Slack `[4]` + email `[8]`. |
| R13 date rigidity `"(the Monday)"` | Minor | **Fixed** → `[13]` accepts `2026-07-06 or 2026-07-07`; evidence matches OE17. |
| R2 demanded an explicit status write | Minor | **Fixed** → `[1]` evidence accepts `selSched` "whether left unchanged or explicitly set". |

The revision closed the loop. This round re-scores the current file from scratch under the strict reading and finds no residual defect.

## Rubric inventory (0-indexed array position)

| # | Sub-cat | One-line | OE | Prompt ask |
|---|---|---|---|---|
| [0] | 1.1 | Update Sunset Ridge Unit 14 record (recc83c05d889b354 **or** reca8230a8fd9ff51), not Rio Bend rec94e86a3007dd5e | OE14 | pull/keep tied to Tanya's unit |
| [1] | 1.2 | Keep turn status Scheduled; do not advance to In Progress/Ready | OE14 | "not marked further along" |
| [2] | 1.2 | Update notes: turn held; no work/marketing until possession returned | OE14 | "tight and true to actual state" |
| [3] | 1.1 | Post status to #make-ready (C004) | OE15 | "post a clean status in the make-ready channel" |
| [4] | 1.2 | Slack states account in active eviction, plan breached, not on active plan | OE15/OE19.2 | "where her account really landed" |
| [5] | 1.2 | Slack states turn held at Scheduled, cannot begin until possession returned | OE15/OE19.3 | "so we are all aligned" (#make-ready) |
| [6] | 1.1 | Draft (no send) email to brooke.phillips@starpm.com re Unit 14 | OE16 | "draft me an email to Brooke ... Do not send it" |
| [7] | 1.2 | Email identifies Sunset Ridge Unit 14, not Rio Bend | OE16/OE19.1 | "where Unit 14 sits end to end" |
| [8] | 1.2 | Email: account delinquent + active eviction; not resolved by invoice 7214 zero balance | OE16/OE9/OE19.2 | "the account" |
| [9] | 1.2 | Email includes $2,132.00 arrears on bill QR-2026-0441 | OE16/OE9 | "the account" |
| [10] | 1.2 | Email: turn held at Scheduled, no begin/market until possession returned | OE16/OE19.3 | "the turn" |
| [11] | 1.2 | Email: eviction filing owner-approved (EVF-2026-014) but still in JP coordination, not closed | OE16/OE19.4 | "anything still open on it" |
| [12] | 1.2 | Email: approved reasonable-accommodation (ESA) on record, fair-housing before turnover/adverse action | OE16/OE19.5 | "anything still open on it" |
| [13] | 1.1 | Calendar reminder 2026-07-06 or 2026-07-07 to revisit Unit 14 | OE17 | "reminder ... early next week" |
| [14] | 1.1 | Comment on OPS-32 (not a new issue) | OE18 | "update the ticket we have open on it" |
| [15] | 1.2 | OPS-32 comment reflects turn held/not advanced, possession not returned | OE18 | "so it is not sitting there stale" |

Distribution: **Outcome 16 (5×1.1 write-action + 11×1.2 content) / Process 0.** No 2.1 rubric is required — the prompt routes every finding into a write deliverable (email/Slack/ticket), not a standalone "report back to me" response ("lay it all out in that email ... and I will take it from there").

---

## 1. Per-sub-dim score table (STRICT)

| QC Rubric sub-dim | Score | One-line evidence |
|---|---|---|
| **Overall Rubric Quality** | **5** | 0 Major / 0 Moderate / 0 Minor. Thresholds: Major 0% ≤10, Maj+Mod 0% ≤15, +Minor 0% ≤20; "no Major and no Moderate, <5% Minor" ⇒ PASS(5). |
| **Rubric Category Balance** | **5** | 16 Outcome > 0 Process; 0% Process < 50%; Outcome ≠ 0. Binary PASS. |
| **Process Rubrics** | **5** | Zero Process present; zero required (three-condition test in §12 fails for every candidate). No invalid Process rubric to count. |
| **Agent-Centric Phrasing** | **5** | All 16 criteria are "The Agent …" / valid possessive "The Agent's email/message/update/comment …" (06/09 valid). Zero tool names in any criterion. |
| **Atomicity** | **5** | Every criterion = one write-action / one content-judgment. The round-1 bundles are now split ([8]/[9], [15]). Three watch-items ([2],[8],[11]) resolve to acceptable bundling — see §10. |
| **Self-Containment** | **5** | Every value embedded (rec ids, brooke.phillips@starpm.com, $2,132.00, QR-2026-0441, EVF-2026-014, OPS-32, C004/#make-ready, 2026-07-06/07, selSched/selProg/selReady). [0]'s "recc83c05d889b354 or reca8230a8fd9ff51" is a CLOSED named set, not an open catch-all. |
| **Completeness / Coverage** | **5** | All 6 prompt asks covered; all 5 write OEs → a 1.1; all 3 decoys have an exclusion rubric ([0] bars Rio Bend, [8] bars 7214, [9] keys content-not-vendor). No user-facing 2.1 gap. |
| **Flexibility** | **5** | Exact for structured one-correct values (emails, ids, dates, $2,132.00 literal Balance, status enums); dual-accept where the universe is open (either Sunset Ridge rec id; either 07-06/07-07). No spurious "approximately" on a literal Balance; no "at least N of M". |
| **Accuracy** | **5** | Every embedded literal verified against `_aux/Universe_Split/` (see §3). Zero fabricated values. |

**Rubric dimension = 5/5 (grade-to-lowest; all sub-dims 5).**

---

## 2. Predicted All-Failing check

No rubric is a predicted AF: every target exists and is reachable — make-ready record write (Airtable), Slack C004, Gmail draft, gcalendar event, Linear OPS-32 comment, and all read-graded literals ($2,132.00, EVF-2026-014, invoice 7214, ESA ticket) are present in the split. All-Failing Rubrics sub-dim → N/A → 5 (re-assessed at verifier stage).

---

## 3. Two flagged validator warns — independently verified (NOT fabricated)

**(a) $2,132.00 arrears on bill QR-2026-0441** — GROUNDED.
- `quickbooks.quickbooks_entities.json` id `232176553533`: `"Balance": 2132.0`.
- Four line items, every `Description` = "… Tanya Mitchell, Unit 14": $847.00 carried-forward May rent arrears + $925.00 June 2026 rent + $210.00 accumulated late fees through June 29 + $150.00 partial payment-plan-credit line (sum = 2132.00).
- `_aux/Fact_Ledger.json` amounts contains `"2132.00"`. OE 9 cites `bill QR-2026-0441 … Balance 2132.00`.
- VendorRef `Alamo HVAC Services` is the decoy; content unambiguously keys to Tanya/Unit 14. **Real universe atom, correctly grade-on-content (§11).**

**(b) EVF-2026-014** — GROUNDED.
- `airtable.airtable_records.json` `rec922b9a2d1b9451` (tbl `tblMaintenanceTickets`): `fldTicketNumber "EVF-2026-014"`, `fldDescription "Owner authorization received from Linda Castillo … Owner Approved - Ready to File. Filing package is staged …"`, `fldCompletionDate 2026-06-30`.
- R11's companion "still in JP coordination" half is grounded in `recc83c05d889b354` notes ("coordinated with the Justice of the Peace") + OE 6 Slack (Brooke ts 1782881568). Both halves real.

Both warns are exact-literal-in-OE notices, not accuracy defects.

---

## 4. B3 — Tool-call density projection (PER MODEL)

StarPM design target **40+ average per model**; QC fail floor 15; pass@1 ≤ 40%. The rubric set forces the full read surface: [8] (invoice 7214), [9] (QR-2026-0441), [11] (EVF-2026-014 + JP), [12] (ESA) each require distinct cross-service reads, and the 1.1/1.2 rubrics enforce all 5 writes.

| Component | Reads | Note |
|---|---|---|
| Base/table discovery (OE1) | 2 | list_bases + list_tables |
| Unit 14 disambiguation (OE2) | 1-2 | search/list make-ready |
| Read hold record recc83c05d889b354 (OE3) | 1 | notes-derived hold |
| Delinquency chain rec769/rec8005/rec91517 (OE4) | 1-3 | supersession trace |
| Maintenance tickets DLQ/EVF (OE5) | 1-2 | |
| Slack eviction + earlier-commit (OE6/7) | 2-3 | C003 |
| QB customer + invoice 7214 + QR-2026-0441 + 2026-EV-047 (OE8/9) | 3-5 | forced by [8]/[9] |
| HubSpot ESA + Gmail approval (OE10/11) | 3-5 | forced by [12] |
| Linear OPS-32 (OE12) | 1-2 | forced by [14] |
| Contacts Brooke/Tanya (OE13) | 1-2 | |
| **Writes** ([0]/[3]/[6]/[13]/[14]) | **5** | Airtable + Slack + Gmail draft + gcalendar + Linear |
| Cross-service verify buffer | 4-8 | correlate before writing |

Independent midpoint: **≈ 40-45 per model.**
- **Opus: ~40-42 → PASS (≥40 design target), thin margin — flagged honestly.** Consistent with S1 AUDIT re-projection.
- **Gemini: ~42-46 → PASS.** Consistent with S1 (~46).
- Both **>> 15 floor**. **B3 verdict: PASS per model; Opus at-target/thin. The rubric set does not reduce density (it enforces every read each content rubric depends on).**

---

## 5. B4 — Lever coverage (6 hardness levers)

| Lever | Covering rubric(s) | Covered? |
|---|---|---|
| 1. Cross-property Unit 14 (Sunset Ridge vs Rio Bend decoy) | [0] (bars rec94e86a3007dd5e) + [7] (email disambiguates) | ✅ |
| 2. Hold from NOTES not selSched / stale fldMoveOut 2026-05-02 | [1] (status stays Scheduled — refuses to read selSched as advanceable) + [2] (asserts possession NOT returned, defeating any stale-fldMoveOut misread) | ✅ |
| 3. Invoice 7214 zero-balance decoy | [8] ("not resolved by invoice 7214 showing a zero balance"; FAIL if cleared-via-7214) | ✅ |
| 4. QB bill QR-2026-0441 vendor-label decoy (Alamo HVAC) | [9] ("grade on the amount and tenant, not the bill's vendor label") | ✅ |
| 5. Approved-ESA fair-housing | [12] | ✅ |
| 6. Payment-plan-breached supersedes earlier commitment | [4] (Slack: breached, not on active plan) + [8] (email: delinquent + active eviction) | ✅ |

**No uncovered lever.** Each lever's pass/fail depends on traversing it (latch the stale plan → fail [4]/[8]; grab Rio Bend → fail [0]/[7]; fooled by 7214/Alamo decoys → fail [8]/[9]; skip HubSpot → fail [12]).

---

## 6. B7 — Cross-artifact consistency (rubric == OE == prompt)

Every rubric literal matches the OE and prompt: [0] rec-id triplet = OE14; [1] selSched/selProg/selReady = OE14; [2]/[5]/[10]/[15] hold language = OE14/15/16/18 + OE19.3; [3] C004 #make-ready = OE15; [4]/[8] account-state = OE15/16 + OE19.2 + OE9; [6] brooke.phillips@starpm.com draft-only = OE16; [7] Sunset Ridge≠Rio Bend = OE16/OE19.1; [9] $2,132.00/QR-2026-0441 = OE9/OE16; [11] EVF-2026-014 owner-approved + JP = OE16/OE19.4; [12] ESA = OE16/OE19.5; [13] 2026-07-06/07 = OE17; [14] OPS-32 = OE18/OE12. Zero drift. Draft-only (no-send), Slack `message` param, no em-dashes — all deviation-compliant.

---

## 7. B10 — OE-write-action → 1.1 map (5 writes, each ≥1 Outcome 1.1)

| OE write | Action | 1.1 | Content 1.2 |
|---|---|---|---|
| OE14 | Update make-ready record | **[0]** | [1], [2] |
| OE15 | Slack #make-ready | **[3]** | [4], [5] |
| OE16 | Gmail draft to Brooke | **[6]** | [7], [8], [9], [10], [11], [12] |
| OE17 | Calendar reminder | **[13]** | — (date folded into [13]) |
| OE18 | OPS-32 comment | **[14]** | [15] |

**All 5 write actions have a covering 1.1.** ✅

## 8. B11 — Prompt-ask map (forward + reverse)

**Forward (every ask → rubric):** (1) pull/confirm record tied to Tanya → [0]; (2) update tight/true, not further along → [1]+[2]; (3) post make-ready status on account → [3]+[4]+[5]; (4) draft email to Brooke (account/turn/open), do not send → [6]+[7]+[8]+[9]+[10]+[11]+[12]; (5) calendar reminder early next week → [13]; (6) update the open ticket → [14]+[15]. **No forward gap.**

**Reverse (every rubric → ask):** all 16 tie to a prompt ask. The three surplus-scrutiny items clear:
- **[5]** (make-ready-channel turn-hold): justified — it is the *#make-ready* channel; "post a clean status … so we are all aligned" makes the crew's actionable point (turn on hold) in-scope. OE19.3-mandated. Not surplus.
- **[7]** (email unit disambiguation): justified — the whole universe hardness is the cross-property Unit 14 ambiguity; "where Unit 14 sits end to end … so she is not caught off guard" requires the correct property. OE19.1-mandated. Evidence grades "identification of Sunset Ridge Unit 14 as the subject unit" (does NOT force an explicit Rio Bend mention) → no over-specification. Not surplus.
- **[15]** (OPS-32 content): justified — "update … so it is not sitting there stale" is a content ask (a stale-ticket update with no current state is a no-op); [15] grades the single load-bearing current fact (turn held/possession). OE18-mandated. Not surplus.

**No surplus rubric (no reverse gap).**

---

## 9. Adversarial alt-path (false-negative via over-specificity)

**Result: no realistic false-negative alt-path exists.** Method-agnostic exactly where the prompt is open; exact only where a single grounded truth exists:
- [0] accepts **either** Sunset Ridge rec id → writing reca8230a8fd9ff51 instead of recc83c05d889b354 still passes.
- [1] accepts status **left unchanged** → an agent that confirms selSched and writes only the note passes; only advancing to selProg/selReady fails.
- [6] draft-only: with no send tool, "not sent" cannot fail a correct agent.
- [13] accepts **either** 07-06 or 07-07 → both natural "early next week" resolutions pass.

Candidates examined and dismissed:
- **[14] pins OPS-32.** Would updating a different "open ticket" (Airtable EVF record, sibling OPS-38/54) validly fulfill "the ticket we have open on it … not sitting stale" yet fail [14]? No — the EVF Airtable record is `Owner Approved - Ready to File` (completed 2026-06-30, not stale), the make-ready record is already write #1's target, and OPS-38/54 are subordinate subtasks. OPS-32 ("Eviction Hearing - Mitchell", In Progress) is the unique open, stale-able eviction tracker; a correct agent lands on it. Selection-logic pin (title + id), OE18-mandated. Not a false-negative.
- **[9] pins $2,132.00** (rebutting the round-1 false-negative claim). The round-1 scenarios are WRONG computations, not valid alternatives: **$2,317** = 2132 + 185, but bill 2026-EV-047's $185 is *eviction-filing-package prep*, not rent arrears — labeling it "rent arrears" is an error; **$2,207** = 2132 + 75, but the $75 June late fee is already inside QR-2026-0441 (its line "$210 accumulated late fees through June 29") — adding it double-counts. [9] is scoped to "rent arrears balance **on bill QR-2026-0441**" = the Balance field = 2132.00 exactly. A correct agent reports 2132.00. Post-split, even a wrong figure only loses [9], not the delinquency call [8]. Not a false-negative.

---

## 10. Adversarial atomicity (could each fail for two unrelated reasons?)

No rubric bundles cross-service or cross-write-action claims (the eval's Major "Not Atomic" trigger). The round-1 bundles are split ([8] state / [9] amount; [15] turn-hold only). Three intra-content watch-items examined under the strict reading and cleared as **acceptable bundling** (same write action, single judgment):
- **[8]** — "delinquent + active eviction" *and* "not resolved by invoice 7214". The 7214 clause is a **FAIL-guard, not a second required element**: PASS = "delinquent and in active eviction"; FAIL = "reports cleared on the basis of invoice 7214's zero balance". An email stating delinquent+eviction without naming 7214 passes. Single "is the account cleared?" judgment. Atomic.
- **[11]** — "owner-approved (EVF-2026-014)" *and* "still in JP coordination, not closed". One contrastive status ("approved to file but not resolved"); one "approved-but-open" determination. Atomic.
- **[2]** — "held because possession not returned" *and* "work and marketing cannot begin until possession returned". Two facets of one hold rationale in the same notes field; tightly-coupled required elements of one content criterion. Atomic (closest to splittable; still same-write-action bundling).

**No split required.**

## 11. Grade-on-content-not-vendor ([9]) — confirmed

[9] pins "$2,132.00 on bill QR-2026-0441"; evidence: "Grade on the amount and tenant, not the bill's vendor label." Verified: QR-2026-0441 Balance 2132.00, all four line descriptions "Tanya Mitchell, Unit 14"; VendorRef "Alamo HVAC Services" is the planted decoy. The rubric keys on **amount + tenant linkage**, immune to the vendor decoy. Honors the S2 binding carry. ✅

## 12. Zero-Process design — three-condition test (correct, not a gap)

Confirmed **no Process rubric is required.**

| Candidate Process behavior | (1) Every valid path? | (2) Outcome can't capture? | (3) Verification not trace? | Required? |
|---|---|---|---|---|
| "Read make-ready record before writing" | No (reachable via Slack too) | **No** — [0]+[1]+[2] prove correct record/state/hold | trace-risk | **No** |
| "Derive hold from fldNotes2 not fldTurnStatus" | No | **No** — [1] (status kept Scheduled) + [2] (possession-not-returned) capture the result | trace-risk | **No** |
| "Trace breach superseding stale plan" | No | **No** — [4]/[8] grade the end-state | — | **No** |
| "Open HubSpot for the ESA" | No | **No** — [12] grades the ESA-on-record outcome | — | **No** |

Ordering: the 5 writes are mutually independent; no write must precede another. No shallow-source verification escapes a tightened Outcome. **Outcome 16 > Process 0 is correct** (AGENTS.md hard rule 8; default zero). Not a Major gap.

---

## FINAL VERDICT: **GO**

**Issue tally — Major: 0 · Moderate: 0 · Minor: 0.**

| Sub-dim | Score |
|---|---|
| Overall Rubric Quality | 5 |
| All-Failing Rubrics | N/A → 5 (verifier stage) |
| Rubric Category Balance | 5 |
| Process Rubrics | 5 |
| Agent-Centric Phrasing | 5 |
| Atomicity / Self-Containment / Completeness / Flexibility / Accuracy | 5 / 5 / 5 / 5 / 5 |

**Rubric dimension = 5/5.** The revised 16-rubric set resolves the round-1 BLOCK in full (state/amount split; OPS-32 comment de-bundled; date range widened; unchanged-status accepted). B3 density PASS per model (Opus ~40-42 at-target/thin, Gemini ~42-46; both ≥40 design target, far above the 15 floor). B4 all 6 levers covered. B7/B10/B11 fully consistent — no coverage gap, no surplus. Both flagged validator warns ($2,132.00/QR-2026-0441, EVF-2026-014) confirmed grounded, not fabricated. Zero-process design correct under the three-condition test. No false-negative alt-path; no atomicity split required.

**Non-scoring watch-note (informational, no fix required):** Opus density sits right at the 40 target; the rubric set itself enforces the full read surface, so any residual density risk is upstream at S1/hardness, not in the rubrics. Council B raises no blocking or non-blocking issue against the current `7_Rubrics.json`.

BLOCK → **GO** (round 2, revised set).
