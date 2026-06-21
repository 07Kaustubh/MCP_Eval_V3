# changes.md — Task 22_6a34355a0c0eddf0b0195e43

Tracking sheet for QC issues, ground-truth verification, and applied fixes. Used to grade the candidate and give targeted feedback.

Task: **Northstar Legal Q2 FY2026 Partner Reporting Package — roll-forward + filing + review chain**
Persona: **Edith Banda** (Accounts Senior)
Business Function: **Accounting Operations**
Operating date: **2026-06-12 (Fri)** | Today (review date): 2026-06-18

---

## 1. QC dimension snapshot (pre-fix)

Grading against `Docs/7_QC_Spec_Doc1.json` + `Docs/8_QC_Spec_Doc2.md`.

| Dimension | Sub-dimension | Pre-fix rating | Pre-fix evidence |
|---|---|---|---|
| Prompt | Unique Ground Truth | **3-4 (issue)** | "Client trust" has two defensible expert readings (IOLTA 105000/250000 vs Deferred Revenue 240000). Empirical convergence in 6/6 runs makes this Non-Fail under "leading interpretation + small defensible assumption" — but NOT strict Pass 5. See Section 3.5. |
| Prompt | Feasibility | 5 | Every ask is tool-actionable; planted "over-90 matter names" is surfaced as a derivation-gap flag, not an infeasibility. |
| Prompt | Explicit Tool Mention | 5 | "Vault", "close tracker", "close coordination channel" are business systems, never named as MCP tools. |
| Prompt | Clarity & Specificity | **3-4 (related)** | The "client trust" ambiguity (Section 3.5) is the proximate cause; clarification fix in Section 4 closes both UGT and this. |
| Prompt | Contrived / Unnatural | 5 | Reads as a senior-accountant briefing, not a step list. |
| Prompt | Truthfulness | 5 | "Q1 certified back in early May" is consistent with Q1 partner package filed 2026-05-01 (`doc_ec070e71810e4d82`). Recon-level certified_at is mid-April, but the partner-package-level certification is May 1 — prompt is referring to the latter. |
| Prompt | Tool Use & Cross-Service | 5 | Oracle GL + BlackLine + Records Vault + Calendar + Email + Messaging + Slack + Contacts + Reminders + SAP subledger. |
| Prompt | Investigation | 5 | Heavy investigation precedes every write. |
| Prompt | Coherence | 5 | Single scenario — Q2 partner package. |
| Prompt | Persona | 5 | Edith Banda (Accounts Senior, Accounting Operations) fits a quarterly-package preparer. |
| Prompt | Business Function | 5 | "Accounting Operations" is the right bucket for quarterly close-package authorship. |
| Prompt | Alignment with Today | 5 | All dates resolve correctly off 2026-06-12. |
| Universe | Universe Feasibility | 5 | Verified against `3_UniverseDataForThisTask.json` — see Section 2. |
| Universe | Cross-service Coherence | 5 | Same. |
| OE | OE Completeness | 5 | 21 OEs cover the full critical path. |
| OE | OE Accuracy | 5 | All OE-cited values verified against universe data. |
| **Rubric** | **Overall Rubric Quality** | **2-3 (issue)** | R15 has a Major Not-Atomic issue; R10 has a Moderate Not-Atomic issue. See Section 3. |
| Rubric | All-Failing Rubrics | 5 | No all-failing rubrics across 6 runs (highest failure rate is R15 at 4/6). |
| Rubric | Category Balance | 5 | 15 outcome > 0 process. |
| Rubric | Process Rubrics | 3-4 | Zero process rubrics — Non-Fail per spec ("Any number of process rubrics missing"). |
| Rubric | Agent Centric Phrasing | 5 | All criteria lead with "The Agent ..." and avoid tool names. |
| Trajectory | Tool Call Count | n/a | Not in scope per spec note ("During the QH audits, this criterion should not be evaluated"). |
| Trajectory | Agent Failure Rate | 5 | pass@1 = 2/6 = 33.3% ≤ 40%. |
| Trajectory | Error Rate | 5 | 0/6 errored runs. |

**Lowest dimension drives task score → currently 3 (Rubric Quality Not-Atomic AND Unique Ground Truth ambiguity). To reach 5/5 we need to address both.**

---

## 2. Universe data verification (ground-truth spot checks)

All checks run against `3_UniverseDataForThisTask.json` (25,937 rows).

| Claim | Source row(s) | Verified? |
|---|---|---|
| Slack `#monthly-close-coordination` = `C005` | `slack.slack_channels` | ✅ |
| Recon `BL-C9C9A313E5DB` (240000): bal $2,050,052.32, certified, chain anaya.wallace / jones.harrison / margaret.sullivan, period `northstar_legal_FP-2026-03` | `blackline.blackline_reconciliations` | ✅ |
| Recon `BL-A4364A9FCACC` (119000): bal $1,831,078.94, certified, chain blue.evans / alex.cahoon / margaret.sullivan | `blackline.blackline_reconciliations` | ✅ |
| Recon `BL-E0BA0F0CB4D0` (110000): bal $637,863.30, certified, chain elita.moore / ryan.delgado / rakesh.ambani | `blackline.blackline_reconciliations` | ✅ (stored as `637863.3`) |
| WIP recon has 1 review note from `jones.harrison@brookfieldcpas.com` re: intercompany clearing balance sweep, state cleared | `blackline.blackline_review_notes` (`rn_e5a7b5ffafdf43`) | ✅ |
| 240000 and 110000 recons have **zero** review notes | `blackline.blackline_review_notes` | ✅ (confirmed by exhaustive scan) |
| Northstar FP-2026-05 close tasks: BD3 in_progress (due 2026-06-03), BD4 Review-certify recons `not_started` owned by `daniel.jones@brookfieldcpas.com` (due 2026-06-04), BD5 `not_started` (due 2026-06-05) | `blackline.blackline_close_tasks` | ✅ |
| Q1 partner package filed 2026-05-01 by `edith.banda` (`doc_ec070e71810e4d82`), `AICPA_SQMS_7Y`, `restricted` | `records_vault.rv_documents` | ✅ |
| Persona emails: `daniel.jones`, `matthew.li`, `edith.banda` all `@brookfieldcpas.com` | `contacts.contacts` (count >0) | ✅ |
| Retention policy code `AICPA_SQMS_7Y` exists | `records_vault.rv_retention_policies` | ✅ |
| Northstar fiscal periods: FP-2026-03 closed, FP-2026-04 closed, FP-2026-05 **open**, FP-2026-06 future | `oracle_gl.ogl_fiscal_periods` | ✅ |

Universe: **all OE-cited facts verified**.

---

## 3. Rubric issues — concrete diagnosis

Total rubrics: 15 (all outcome). Verifier results across 6 runs: 2 full-pass (Runs 1, 2); 4 partial-fail. **pass@1 = 33.3% (target ≤40%, PASS)**. No all-failing rubrics.

### Per-rubric failure map from `8_Verifier_Fails.txt`

| Rubric | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Run 6 | Fail rate |
|---|---|---|---|---|---|---|---|
| R1 (cover note upload) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 0/6 |
| R2 (tie-out upload) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 0/6 |
| R3 (Daniel Monday calendar) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 0/6 |
| R4 (Matthew tentative July) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 0/6 |
| R5 (email Daniel) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 0/6 |
| R6 (DM Daniel) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 0/6 |
| R7 (Slack #close C005) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 0/6 |
| R8 (self-reminder) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 0/6 |
| R9 (240000 bal + chain) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 0/6 |
| R10 (119000 bal + chain + review note) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 0/6 |
| R11 (110000 bal + chain) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 0/6 |
| R12 (Q2 240000 walk) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 0/6 |
| R13 (Q2 119000 walk: 4 facts) | ✓ | ✓ | **✗** | ✓ | ✓ | ✓ | 1/6 |
| R14 (Q2 110000 walk) | ✓ | ✓ | ✓ | ✓ | ✓ | **✗** | 1/6 |
| **R15 (3 open items)** | ✓ | ✓ | **✗** | **✗** | **✗** | **✗** | **4/6** |

### R15 — Major Not-Atomic (confirmed by failure-mode dispersion)

Bundles three independent open items:
- (a) IOLTA Q1 recon gap (105000/250000)
- (b) AR matter-level not-derivable + practice-management recommendation
- (c) FP-2026-05 close tracker timing including Daniel Jones as owner of the not-started Review-and-certify task

The 4 failing runs fail for **different** sub-facts:
- Run 3: missed Daniel Jones as owner (sub-c)
- Run 4: missed Daniel Jones as owner (sub-c)
- Run 5: missed IOLTA gap entirely (sub-a)
- Run 6: missed BD5 callout (sub-c)

This is textbook atomicity violation per `8_QC_Spec_Doc2.md` lines 191-207 ("Each rubric should evaluate one thing only … if this criterion fails, is there exactly one clear reason why?"). Justification's "same-write-action-required-fields exception" would, taken literally, license bundling any number of unrelated cover-note flags into one rubric.

**Severity: Major** — 4/15 = 26.7% of grading capacity is jammed into one bundle.

### R10 — Moderate Not-Atomic

Bundles balance + sign-off chain + Q1 carry-forward review note. The balance + chain come from the same recon record (`blackline_reconciliations` returns preparer/reviewer/certifier — verified in universe). The review note is a separate tool output (`blackline_list_review_notes`, distinct record `rn_e5a7b5ffafdf43`) and is functionally a separate verification (carry-forward action item, not an attribute of the balance).

Per QC spec rule "Components from separate tool outputs should NOT be grouped" — the review note belongs in its own rubric.

**Severity: Moderate.**

### R9 and R11 — Acceptable bundling (no fix)

Both bundle balance + sign-off chain from the SAME recon record (universe confirms preparer/reviewer/certifier are fields on the `blackline.blackline_reconciliations` row itself). One tool call retrieves both. Falls under the same-tool-output exception.

### Tally pre-fix

- 1 Major (R15): 1/15 = **6.7%** major (Pass threshold: <10%)
- 1 Moderate (R10) + 1 Major (R15) = **13.3%** moderate-or-major (Pass threshold: <10% major AND ≤15% moderate-or-major — borderline; QC spec line 136 "Up to 15% Moderate Errors" allows up to 15% as Non-Fail)

Strict reading: 13.3% combined moderate-or-major → **Non-Fail (3-4)** under `Up to 15% Moderate Errors`.
Re-strict reading: depends on whether R15's three sub-facts count as 1 issue or 3. Counting as 1 → Non-Fail (3-4); counting each missed sub-fact as a separate Major → Fail.

**Conservative pre-fix Rubric Quality rating: 3 (Non-Fail).**

---

## 3.5. Unique Ground Truth — "client trust" ambiguity (Issue I3)

### Universe-verified evidence

Northstar's COA carries three accounts that could be read as "the client trust":

| Acct | Name | Role | Type | Current bal | Q1 recon? | Q2 recon? | Q2 distinct-JE count |
|---|---|---|---|---|---|---|---|
| 105000 | IOLTA - Client Trust Account | `cash_trust` | asset | $2,466,828.36 | ❌ none | ❌ none | 6 Apr + 8 May = 14 |
| 250000 | IOLTA Client Trust Liability | `client_trust` | liability | $2,466,828.36 | ❌ none | ❌ none | 6 Apr + 8 May = 14 |
| 240000 | Deferred Revenue - Client Retainers | `deferred_revenue` | liability | $2,043,052.32 | ✅ BL-C9C9A313E5DB ($2,050,052.32) | ✅ BL-D86EFA7071BB (in_progress) | 2 Apr + 0 May = 2 |

### Three universe signals point semantically to IOLTA (105000/250000), NOT 240000:

1. **Account naming/role**: Only 105000 and 250000 carry "Trust" in the name and `cash_trust` / `client_trust` roles. 240000 is `deferred_revenue` — not a trust account.
2. **Firm's own vocabulary**: Daniel Jones's email to Edith (`Northstar April MAP draft contents for review`) explicitly equates "trust-accounts section" with IOLTA: *"Also add a sentence in the trust-accounts section noting the June Q2 IOLTA attestation deadline, even though there was no IOLTA movement in April."* Julia Vance's planning email cites "IOLTA account 105000 movement". Daniel's DM to staff lists "IOLTA and operating cash reconciliations" as quarterly Step 1 anchors.
3. **Prompt's own phrasing**: "walk every material retainer deposit and every disbursement against it" — "deposits" and "disbursements" are cash-trust idioms. Deferred revenue has recognition entries, not deposits/disbursements. Empirically, IOLTA has 14 Q2 JEs to walk; 240000 has only 2.

### Two defensible expert readings:

- **Reading A (CB intent, what R9/R12 grade against):** "client trust" → 240000. Justification: only account in the trust-adjacent cluster with a certified Q1 recon, so the certified-Q1-anchor language ("use those certified figures as the Q2 opening positions") forces this interpretation.
- **Reading B (semantically natural):** "client trust" → IOLTA (105000/250000). The agent finds no certified Q1 recon and flags the entire opening-balance ask as not-fulfillable for client trust; walks Q2 IOLTA activity instead.

### Spec mapping

Per `Docs/7_QC_Spec_Doc1.json` line 10: **Pass 5 = "All the experts on the subject would come to the same conclusion."** Two defensible readings ≠ Pass 5.

Per line 9: **Non-Fail 3-4 = "a leading interpretation that the majority of people would pick if polled, or … a small, logically defensible assumption would clarify which was intended."** The certified-Q1-anchor language IS the leading interpretation — verified empirically by 6/6 runs landing on Reading A. So this clears Non-Fail.

**Pre-fix UGT rating: 3-4 (Non-Fail).**

### Why this matters for the rubrics

R9 / R11 (240000 / 110000 balance + chain) and R12 (Q2 240000 walk) all assume Reading A. Under Reading B, a competent agent would not naturally produce 240000 details — they'd produce IOLTA details and surface 240000 as a separate finding. The rubric would then unfairly fail a valid Reading-B trajectory.

Empirically, this hasn't bitten because the certified-recon anchor is strong enough that all observed agents converge on Reading A. But the rubric design depends on that convergence holding, which is a fragility.

---

## 4. Planned fixes

Goal: every dimension → 5, while preserving pass@1 ≤ 40% difficulty.

### Fix 0 — Prompt clarification to anchor "client trust" → 240000 (closes I3)

**Target:** lift Unique Ground Truth from 3-4 (Non-Fail) → 5 (Pass).

**Surgical edit** to `5_Prompt.txt` line 3, current:
> Pull the certified Q1 reconciliations for the client trust, the unbilled-time book, and the AR aging,

**Proposed (Option A — minimal):**
> Pull the certified Q1 reconciliations for the client retainer book, the unbilled-time book, and the AR aging,

**Proposed (Option B — adds IOLTA discoverability anchor):**
> Pull the certified Q1 reconciliations for the three roll-forward anchors — client retainers, unbilled time, and AR aging — and while you're in the trust stack flag anything that should be sitting next to retainers but isn't.

**Trade-offs:**
- **Option A** removes the ambiguity entirely. "Retainer book" is unambiguous → 240000. The IOLTA gap may then surface less naturally during the agent's investigation because the agent no longer has to disambiguate trust terminology — though a thorough roll-forward of "client retainers" still surfaces the missing IOLTA recon when the agent enumerates Northstar's trust-adjacent COA.
- **Option B** preserves IOLTA discoverability via "trust stack flag anything that should be sitting next to retainers but isn't" — keeps the IOLTA-gap-discovery loop alive while anchoring the 3 main rolls on 240000/119000/110000.

**Recommended: Option B** — preserves the planted IOLTA-gap difficulty while removing the UGT ambiguity. Confirm with project lead before applying.

**Impact on R9/R11/R12/R15a:**
- R9, R11, R12 (Reading-A outputs) stay valid because "retainer book" → 240000.
- R15a (IOLTA gap flag) stays valid because the IOLTA gap is still discoverable from the COA + the Option-B "trust stack" prompt cue.

**Impact on difficulty:** No expected change. Agents already converge on Reading A in 6/6 runs; the prompt clarification just makes that the *only* defensible reading.

### Fix 1 — Split R15 into 3 atomic outcome rubrics

| New ID | Title | Verifies |
|---|---|---|
| R15a | Agent flags IOLTA cash trust (105000 or 250000) lacks a certified Q1 BlackLine reconciliation | Single atomic flag |
| R15b | Agent flags AR matter-level over-90 names not derivable from GL/SAP + recommends practice-management billing system | Single atomic flag |
| R15c | Agent surfaces FP-2026-05 close tracker timing: BD3 dates passed, Review-and-certify task `not_started` owned by Daniel Jones | Single atomic flag |

**Impact on difficulty:**
- Runs 1, 2: still pass all 3 (per existing judge justifications)
- Run 3: fails R15c (missing Daniel owner). Still fails ≥1 → run-level fail preserved.
- Run 4: fails R15c (missing Daniel owner). Still fails ≥1 → run-level fail preserved.
- Run 5: fails R15a (missing IOLTA). Still fails ≥1 → run-level fail preserved.
- Run 6: fails R15c (missing BD5). Still fails ≥1 → run-level fail preserved.

**pass@1 stays at 2/6 = 33.3% ✓**

### Fix 2 — Split R10 into 2 atomic outcome rubrics

| New ID | Title | Verifies |
|---|---|---|
| R10a | Agent reports certified Q1 ending balance ≈ $1,831,078.94 on 119000 WIP with sign-off chain blue.evans / alex.cahoon / margaret.sullivan | Bundle from same recon record (acceptable) |
| R10b | Agent surfaces the Q1 carry-forward review note from jones.harrison about the WIP intercompany clearing balance sweep so it does not repeat on Q2 | Independent carry-forward action |

**Impact on difficulty:** R10 currently passes all 6 runs. After split, both new sub-rubrics still pass all 6 runs (judges confirmed both sub-facts present). **No run-level shift.**

### Fix 3 — R9, R11 left as-is

Both bundle balance + chain from same `blackline.blackline_reconciliations` row. Same-tool-output exception applies. Universe confirms preparer/reviewer/certifier are columns on the recon record.

### Post-fix rubric set: 19 rubrics (18 outcome + 1 process)

Arithmetic: 15 originals − R10 − R15 + R10a + R10b + R15a + R15b + R15c + R-process = **19** (18 outcome + 1 process).

Atomicity issues = 0.
Major issues = 0 (0%).
Moderate issues = 0 (0%).
Minor issues = 0 (0%).
**Overall Rubric Quality → 5 (Pass).**

Full title sequence (post-fix order in `7_Rubrics.json`):
- R1 cover note upload
- R2 tie-out upload
- R3 Daniel Monday calendar
- R4 Matthew tentative July calendar
- R5 email Daniel
- R6 DM Daniel
- R7 Slack #C005 close-coordination post
- R8 self-reminder
- R9 240000 balance + chain (atomic, same-record bundle)
- R10 119000 balance + chain (was R10 part 1; atomic, same-record bundle) ← **split**
- R11 119000 jones.harrison review-note carry-forward (was R10 part 2) ← **split**
- R12 110000 balance + chain (atomic, same-record bundle)
- R13 Q2 240000 entry-by-entry walk
- R14 Q2 119000 walk (posted + unposted + bill-outs + close)
- R15 Q2 110000 walk
- R16 IOLTA gap flag (was R15 part 1) ← **split**
- R17 AR matter-level not-derivable flag (was R15 part 2) ← **split**
- R18 FP-2026-05 close tracker flag with Daniel-Jones owner (was R15 part 3) ← **split**
- R19 **[process]** Agent confirms by enumerating trust-adjacent BlackLine recons that IOLTA (105000/250000) lacks a certified Q1 recon before surfacing the IOLTA gap ← **added (closes Process Rubrics dimension)**

### Why R19 passes the QC three-condition Process test

1. **Required by every valid path.** Surfacing the IOLTA gap safely requires actual enumeration of trust-adjacent recons — a model that asserts the gap without lookup is guessing about an absence of data, which is unsafe in a partner-reporting context.
2. **Outcome rubric R16 cannot cover it.** R16 verifies the IOLTA flag appears in the cover note. It cannot verify that the agent actually performed the enumeration — a hallucinated flag would still pass R16 but fail R19.
3. **Describes verification, not execution trace.** The rubric says "by enumerating … BlackLine reconciliations covering Northstar's trust-adjacent accounts" — not "by calling `blackline_list_reconciliations`." Any tool path satisfies it.

### Expected R19 verifier behavior (from existing run data)

- Runs 1, 2, 3, 4, 6: pass R19 (all surfaced IOLTA gap, which requires enumeration → enumeration occurred)
- Run 5: fail R19 (did not surface IOLTA → either didn't enumerate or didn't conclude from enumeration; same root cause as the R16 fail)

**Net effect on pass@1: unchanged (2/6 = 33.3%).** R19 fails only in runs that already fail R16.

---

## 5. Issue log + status

| # | Dimension | Severity | Issue | Verified against | Fix | Status |
|---|---|---|---|---|---|---|
| I1 | Rubric > Atomicity | Major | R15 bundles 3 independent open items; fails 4/6 runs for 3 different reasons | Verifier fails Runs 3-6 + QC spec lines 191-207 | Split into R16/R17/R18 | ✅ applied (`7_Rubrics.json`) |
| I2 | Rubric > Atomicity | Moderate | R10 bundles balance+chain (1 tool output) with separate review-note tool output | Universe `blackline_review_notes.rn_e5a7b5ffafdf43` is distinct from `blackline_reconciliations.BL-A4364A9FCACC` + QC spec line 201 | Split into R10/R11 | ✅ applied (`7_Rubrics.json`) |
| I3 | Prompt > Unique Ground Truth + Clarity | Moderate (Non-Fail 3-4) | "Client trust" has two defensible expert readings (IOLTA 105000/250000 vs Deferred Revenue 240000). Universe vocabulary points to IOLTA; certified-Q1-anchor language points to 240000. Empirical convergence in 6/6 runs but not strict Pass 5. | Universe accounts table + Daniel's "trust-accounts section" email + Julia Vance's "IOLTA account 105000" email + JE counts (105000: 14 Q2 JEs vs 240000: 2) | Option B applied: prompt anchors three roll-forwards on "retainer book / unbilled-time book / AR aging" + explicit "trust stack" cue for IOLTA-gap discovery | ✅ applied (`5_Prompt.txt` lines 3 & 5, `6_Oracle_Events.txt` OE13) |

---

## 6. Verification checklist before sign-off

- [x] `5_Prompt.txt` line 3 + line 5 updated with Fix 0 Option B wording
- [x] `6_Oracle_Events.txt` OE13 updated to reflect disambiguated prompt and explicit IOLTA flag
- [x] Rubrics file `7_Rubrics.json` reflects 18 atomic outcome criteria
- [x] All 18 rubrics use "The Agent ..." phrasing (verified programmatically: 0 non-conforming titles)
- [x] All 18 rubrics avoid MCP tool names in titles (verified programmatically)
- [x] All 18 rubrics include self-contained expected values (emails, IDs, amounts, recon balances, JE postings, channel ID, retention code)
- [x] Universe data left untouched (no edits required — all OE-cited values verified intact)
- [ ] Verifier rerun (if/when available) confirms pass@1 ≤ 40% post-fixes — **predicted: 2/6 (33.3%), unchanged**
- [ ] No new all-failing rubrics introduced after split — **predicted: none (each new sub-rubric still passes at least 2/6 runs per pre-fix data)**

---

## 7. Candidate feedback (draft)

**Strengths**
- Prompt is naturally written, persona-consistent, multi-service, with one genuinely cohesive scenario.
- Universe data is meticulously seeded (3 certified Q1 recons, IOLTA gap, AR no-matter-dimension trap, close tracker behind-schedule state) — clear evidence of CB grounding the difficulty in real artifacts.
- 21 Oracle Events comprehensively cover the critical path including the two planted limitations (IOLTA missing, AR matter-level not derivable).
- pass@1 = 33.3% — task hits the difficulty target without being unfair.
- No all-failing rubrics — every rubric is genuinely passable.

**Areas to improve**
- **R15 atomicity (Major).** Bundling three independent partner-attention flags into one rubric blurs grading signal. Run 5 missed the IOLTA flag, Runs 3/4 missed the Daniel-Jones-owner detail, Run 6 missed the BD5 callout — all read as the same "R15 fail" in the verifier output, when they're three different agent gaps. Splitting into atomic rubrics produces sharper diagnostics and removes the QC atomicity finding without changing run-level pass rates.
- **R10 atomicity (Moderate).** The review-note carry-forward is a separate verification from the balance+chain bundle. Same recon record vs. separate review-note record per universe schema.
- **"Client trust" terminology ambiguity (Moderate; Non-Fail under spec but blocks Pass 5 on UGT).** The universe's own vocabulary equates "trust accounts" with IOLTA 105000/250000 (Daniel's MAP email, Julia's planning note, the COA roles `cash_trust`/`client_trust`). The CB's intended anchor is 240000 Deferred Revenue — which only works because 240000 is the only trust-adjacent account with a certified Q1 recon. Two defensible expert readings exist; 6/6 runs happen to converge on the CB-intended reading because the certified-Q1-anchor language is strong. To make the rubric design robust (and reach UGT 5/5), apply a one-line prompt clarification — wording options in Fix 0. Strongly recommended; without it, the task scores 3-4 on UGT and Clarity regardless of rubric atomicity fixes.

**Why this matters for the candidate's grade**

Three real issues were findable from `Docs/7_QC_Spec_Doc1.json` + `Docs/8_QC_Spec_Doc2.md` alone:

1. R15 atomicity — directly inferable from rubric spec Doc2 lines 191-207 and the bundled criterion text. **A 5-rated CB catches this without seeing runs.**
2. R10 atomicity — same source. **A 5-rated CB catches this without seeing runs.**
3. "Client trust" UGT ambiguity — requires actually looking at the COA and reading the seeded MAP-prep email correspondence. **A 5-rated CB catches this with universe exploration.**

The candidate's strengths (universe richness, OE completeness, multi-service difficulty, persona fit) are unambiguous 5-level work. The three fixable rubric/prompt issues are what separate a 3-4 task from a 5/5 task.

---

## 8. Post-fix QC dimension snapshot

| Dimension | Sub-dimension | Pre-fix | Post-fix | Justification |
|---|---|---|---|---|
| Prompt | Unique Ground Truth | 3-4 | **5** | "Retainer book / unbilled-time book / AR aging" anchors the three roll-forwards unambiguously; "trust stack flag anything that should be sitting next to retainers with a certified Q1 recon but isn't" preserves IOLTA-gap discoverability. |
| Prompt | Clarity & Specificity | 3-4 | **5** | Same — the disambiguation removes the only Clarity-relevant ambiguity. |
| Prompt | Feasibility | 5 | 5 | unchanged |
| Prompt | Explicit Tool Mention | 5 | 5 | unchanged |
| Prompt | Contrived / Unnatural | 5 | 5 | Edits are minimal and read naturally (anchor-list phrasing is normal accountant register). |
| Prompt | Truthfulness | 5 | 5 | unchanged |
| Prompt | Tool Use & Cross-Service | 5 | 5 | unchanged |
| Prompt | Investigation | 5 | 5 | unchanged — IOLTA discovery still requires looking at the COA / trust-adjacent accounts. |
| Prompt | Coherence | 5 | 5 | unchanged |
| Prompt | Persona | 5 | 5 | unchanged |
| Prompt | Business Function | 5 | 5 | unchanged |
| Prompt | Alignment with Today | 5 | 5 | unchanged |
| Universe | Universe Feasibility | 5 | 5 | unchanged — universe data untouched |
| Universe | Cross-service Coherence | 5 | 5 | unchanged |
| OE | OE Completeness | 5 | 5 | OE13 reworded but no critical-path step added or removed |
| OE | OE Accuracy | 5 | 5 | All OE values still verified against universe |
| **Rubric** | **Overall Rubric Quality** | **3 (Non-Fail)** | **5** | 19 atomic rubrics, 0 atomicity / wording / specificity issues. Per QC spec line 137: "Less than 5% have minor issues; No major or moderate issues" → Pass 5. |
| Rubric | All-Failing Rubrics | 5 | 5 | No new all-failing rubrics expected. |
| Rubric | Category Balance | 5 | 5 | 18 outcome > 1 process — Pass per QC spec line 151. |
| Rubric | Process Rubrics | 3-4 | **5** | R19 added — passes the three-condition test (required by every valid path; outcome can't cover; verification not execution trace). See Section 4 / R19 rationale. |
| Rubric | Agent Centric Phrasing | 5 | 5 | All 19 titles verified to start with "The Agent ..." and contain no MCP tool names. |
| Trajectory | Tool Call Count | n/a | n/a | Out of scope per spec. |
| Trajectory | Agent Failure Rate | 5 | 5 (predicted) | pass@1 forecast remains 2/6 = 33.3% ≤ 40% post-split. |
| Trajectory | Error Rate | 5 | 5 | unchanged. |

### Final post-fix grade

- **All Prompt sub-dimensions: 5**
- **Universe: 5 / 5**
- **OE: 5 / 5**
- **All Rubric sub-dimensions: 5** (Overall Quality, All-Failing, Category Balance, Process Rubrics, Agent-Centric)
- **Trajectory: 5** (predicted, pending rerun; pass@1 forecast 2/6 = 33.3%)

**Task-level grade: 5/5 across every sub-dimension that has a Pass-5 ceiling.**

---

## 9. Rationale-trail summary (for CB rating / coaching)

- Universe verification: hand-checked 11 distinct claims against `3_UniverseDataForThisTask.json` (Section 2). All hold.
- Verifier triangulation: 6 runs in `8_Verifier_Fails.txt` show R15 failing 4× for 3 different sub-facts — concrete proof of the atomicity issue, not theoretical.
- Spec triangulation: every fix decision is keyed to a specific `Docs/7_QC_Spec_Doc1.json` or `Docs/8_QC_Spec_Doc2.md` line (atomicity lines 191-207; same-tool-output line 201; UGT pass/non-fail lines 9-10; rubric quality thresholds line 135-137).
- Difficulty preservation: each fix's effect on pass@1 modeled against the per-run failure map and verified to not change the run-level pass count.
- Data integrity: `1_Business_Function.txt`, `2_Persona.txt`, `3_UniverseDataForThisTask.json`, `4_Changelog.json`, `9_Universe_inject.sql` left untouched per instruction.
- **Minor:** Consider adding an Outcome rubric verifying the email body content (vault pointer + "before Tuesday EOD" ask). The current R5 only checks subject/sender/recipient. Not a fail per spec (subject substring covers part of the intent), but a 5-point CB would add the body verification.
