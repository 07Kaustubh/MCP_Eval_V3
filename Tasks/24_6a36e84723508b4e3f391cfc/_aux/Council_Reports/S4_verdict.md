# Verifier Fails — S4 verdict (Post-Truthfulness-Fix Run)

**Task:** `24_6a36e84723508b4e3f391cfc` (REDO rebuild + Truthfulness softening)
**Date:** 2026-06-21 (second S4 cycle)
**Trajectory stats:** 6/6 runs evaluated, avg_tool_calls_total = **60** (min 52, max 70) — density PASS at 40 floor (margin +20). Full-pass rate (pass@1) = 0/6 = 0% — difficulty PASS at 40% ceiling. Per-rubric avg pass rate = **68.8%** (up from 64.6% pre-fix).

**vs prior cycle (pre-Truthfulness-fix):** density dropped 8.7 (68.7 -> 60); per-run distribution tightened (was 13–22, now 12–20); avg pass rate up 4.2pp. Net: still well in spec, slightly easier overall but still 0/6 full-pass.

## Run-level scores

| Run | Outcome pass | Other pass | Total | % |
|---:|---:|---:|---:|---:|
| 1 | 20 / 24 | n/a | 20 / 24 | 83.3 |
| 2 | 20 / 24 | n/a | 20 / 24 | 83.3 |
| 3 | 13 / 24 | n/a | 13 / 24 | 54.2 |
| 4 | 17 / 24 | n/a | 17 / 24 | 70.8 |
| 5 | 16 / 23 | 1 / 1 | 17 / 24 | 70.8 |
| 6 | 12 / 24 | n/a | 12 / 24 | 50.0 |
| **avg** | | | **16.5 / 24** | **68.8** |

No outlier (prior cycle had Run 2 at 22/24); distribution is now more balanced.

## Rubric x Run matrix (P = pass, F = fail)

| # | Rubric (short) | R1 | R2 | R3 | R4 | R5 | R6 | P/F | Δ vs prior |
|---:|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | Slack post to C010 | P | P | P | P | P | P | 6/0 | = |
| 2 | Slack GraniteRack stale SOW (procurement) | P | P | F | P | F | F | 3/3 | **+2P** |
| 3 | Slack TimeLedger missing credit memo (AP) | P | F | F | P | F | F | 2/4 | **+1P** |
| 4 | Slack characterizes acme as approval chains AP | P | P | P | P | P | F | 5/1 | = |
| 5 | Linear comment on issue_378874... | P | P | P | P | P | P | 6/0 | = |
| 6 | Linear records 320/320 null-approver | P | P | F | F | P | F | 3/3 | **+1P** |
| 7 | Linear notes post-target invoices orphaned | F | P | P | P | P | P | 5/1 | = (different run failed) |
| 8 | Email lena to daniel cc steven | P | P | P | P | P | P | 6/0 | = |
| 9 | Email GraniteRack void-and-rebill | F | F | F | F | F | F | **0/6** | **-1P (worse)** |
| 10 | Email TimeLedger partner sign-off | F | F | F | F | F | F | **0/6** | **-1P (worse)** |
| 11 | Reminder due 2026-06-19 | P | P | P | P | P | P | 6/0 | = |
| 12 | Ranks by compound exposure | P | P | P | P | P | P | 6/0 | **+1P** |
| 13 | VaultKey largest-$ but not most severe | P | P | F | F | P | P | 4/2 | = |
| 14 | CivicSquare leading compound offender | P | P | P | P | P | P | 6/0 | **+1P** |
| 15 | GraniteRack stale SOW (analytical) | P | P | F | P | F | F | 3/3 | **+2P** |
| 16 | TimeLedger missing credit memo (analytical) | P | F | F | P | F | F | 2/4 | **+1P** |
| 17 | Pinecrest active vendor dispute | P | P | F | P | F | F | 3/3 | **+1P** |
| 18 | High-compound acme as approval chains AP | P | P | P | P | P | F | 5/1 | = |
| 19 | Acme scope from addendum + change order | P | P | F | F | P | F | 3/3 | **-2P (worse)** |
| 20 | Northstar scope from engagement letter | P | P | P | P | P | P | 6/0 | = |
| 21 | Acme/Northstar scope restricted not missing | P | P | F | F | P | F | 3/3 | **-2P (worse)** |
| 22 | Routing fix did not land | F | P | P | F | P | P | 4/2 | **+1P (Truthfulness fix worked)** |
| 23 | Distinguishes 210000 vs 219000 | P | P | P | P | P | P | 6/0 | = |
| 24 | Defers approval/routing | P | P | P | P | P | P | 6/0 | = |

## Classifications

### Bucket 1 — Rubric invalid: **0 rubrics**

Phase 2 was already cleared in the prior cycle (all 24 rubrics confirmed valid; all 6 tool families exist; all atoms ground in `Fact_Ledger.json`). No regressions from the Truthfulness wording change — `validate.py` PASS on prompt + OE + rubrics. No `S4_fixes.md` entries.

### Bucket 2 — Judge error: **0 hard, 0 borderline**

Every Fail verdict cites a concrete agent omission verifiable in the trajectory:
- R7 Run 1 Fail: agent explicitly wrote MetroShield items are "within the normal approval window — so no evidence of a new post-fix orphan flood" (judge correctly read agent's conclusion as opposite of rubric).
- R6 Fails: agents reference 215 or 214 filtered subsets without the systemic 320 claim.
- R13 Run 3/4 Fail: agents ranked by compound correctly but omitted the explicit "VaultKey is the largest single-dollar item" anti-latch callout.
- All R9 / R10 Fails: GraniteRack / TimeLedger absent from email body text (verified previously via Phase 3 trajectory dumps; pattern repeats here).

No platform appeals recommended.

### Bucket 3 — Legitimate model failure: **45 cells across 15 rubrics**

The strongest AF cluster is now even sharper than pre-fix:
- **R9 (Email GraniteRack) + R10 (Email TimeLedger): both 0/6.** Every agent across both cycles dropped these vendors from the email body. The previously-passing Run 2 (pre-fix) dropped them too in this cycle. This is a structural failure mode — agents anchor the email on a dollar-threshold filter (e.g. $50K+) that excludes the partner-sign-off items by amount.
- **R2 / R3 / R15 / R16 (Slack + analytical GraniteRack / TimeLedger):** still failing 3-4 of 6. The multi-link chain (SAP -> Linear -> email) continues to stump agents who don't pull cross-service context.
- **R17 (Pinecrest dispute) 3/3 fail rate**: confirms the small-dollar / high-age lever fires reliably.
- **R6 (320 systemic) 3/3 fail rate**: agents continue to narrow to filtered subsets.
- **R19 / R21 (Acme scope + restricted framing) 3/3 fail rate each**: these declined from pre-fix (was 5/1 and 5/1, now 3/3). Correlation with lower density (60 vs 68.7) — agents doing less thorough Records Vault search and falling into the "no plain engagement_letter so it's missing" trap that the prompt explicitly warns against.
- **R22 (Routing fix did not land) IMPROVED to 4/2 from 3/3**: the Truthfulness verb swap from "was patched" to "was supposed to land" made the prompt's framing less assertive, but did not break the lever. R22 fail rate moved from 50% to 33% — still in the 30-50% effective stump band.

## Hardness calibration vs Hardness_Plan.md predictions

| # | Prediction | Confidence | Actual (this cycle) | Verdict |
|:-:|---|:-:|---|---|
| 1 | Root-cause miscategorization on GraniteRack, TimeLedger, BeaconPay | HIGH | GraniteRack analytical (R15) 3/3 fail; TimeLedger analytical (R16) 4/6 fail; email surfacing (R9 + R10) 6/6 fail each | **STRONGLY CONFIRMED** — email surface failure even stronger than pre-fix |
| 2 | Acme scope reported as "not found" instead of addendum + change order | HIGH | R19 3/3 fail rate (up from 1/6 pre-fix). Density drop unmasked agents who skipped the multi-doc-kind search | **CONFIRMED** at the predicted HIGH rate this cycle (pre-fix was OVER-predicted) |
| 3 | Authority-figure dismissal on routing fix | MED-HIGH | R22 2/6 fail (down from 3/6 pre-fix). Truthfulness verb swap reduced the latch effect modestly | **CONFIRMED** at the predicted MED level |
| 4 | Misses age-vs-dollars trade-off vendor | MED | R12/R13/R14 compound ranking 0-2/6 fails (mostly Pass). Pinecrest R17 3/3 fail rate is the active small-dollar / high-age miss | **NOT THE PREDICTED MECHANISM** — compound ranking holds, but small-dollar attention attrition (the new Lever 12 pattern from prior cycle's calibration) fires reliably |

**Predicted-and-confirmed:** 3 (Pred 1, Pred 2, Pred 3). **Re-routed:** 1 (Pred 4 — actual mechanism is the Lever 12 small-dollar attention sink, not compound-ranking failure). **Effective hit rate:** 3/4 = 75% (improvement over prior cycle's 67%).

### New observation from this cycle

**Density attrition affects lever yield.** When trajectory density drops (68.7 -> 60 mean), the levers that require thorough Records Vault search (L2 structured-DB skip → R19, R21) fire harder. The levers that depend on per-vendor cross-service chain (L8 → R2, R3, R9, R10, R15, R16) fire similarly across both density bands. The L9 authority-dismissal lever (R22) is the one whose yield is sensitive to the prompt verb choice, with the softer "was supposed to land" reducing the latch by ~17pp.

## Action items

1. **Ship as-is.** Density 60 (>= 40 floor) and pass@1 0/6 (<= 40% ceiling) both clear with margin. The 8 AF rubrics with refreshed justifications are ready for the platform.
2. **R9 / R10 escalation is now 0/6 (was 1/6).** These are the strongest, most consistent AF rubrics in the set — they should be the headline AF citations.
3. Append calibration update to `Tasks/_meta/Stump_Hypotheses.md` and `Tasks/_meta/Hardness_Patterns_Log.md` documenting:
   - Truthfulness verb swap reduced R22 fail rate by ~17pp (3/6 -> 2/6) without breaking the lever
   - Density drop (68.7 -> 60) increased L2 (Acme scope) yield from 1/6 to 3/6 fail rate
   - Lever 12 (small-dollar attention sink) confirmed at 3/3 across both cycles

## Verdict

**PASS — SHIP.** Density floor cleared by +20 calls. Difficulty bar cleared by full margin (0/6 full pass). All 4 predicted stump levers fired (3 confirmed at predicted rate, 1 re-routed but still firing via new mechanism). No rubric defects. No judge errors. Truthfulness fix preserved both gates as predicted by the FINAL Council.
