# S3 Council B — Adversarial Sweep (Re-run #3 after AUDIT fixes)

Task: `Tasks/27_6a39fd19048f9213281ec7b`
Phase: S3 Rubrics — re-run #3 (post-AUDIT)
Council role: B (adversarial)
Inputs reviewed: `7_Rubrics.json` (now **24** rubrics, nested V3 schema, 100% outcome), `5_Prompt.txt`, `6_Oracle_Events.txt`, `_aux/Hardness_Plan.md`, `Reference/Rubric_Format.md`, `Docs/2_Rubrics_V3_Guidelines.md`, `Docs/12_Always_Failing_Rubrics.md`, `QC_Tasks/V3_Tasks/Task14_*/Rubrics.json`, `QC_Tasks/V3_Tasks/Task11_*/Rubrics.json`.
Prior verdict (round 2): GO. AUDIT subsequently raised three findings (F1 vault-USD-cash missing, F2 vault-BL-8DCA-refutation missing, F3 `approximately` qualifier on static dollar values). Producer applied all three fixes.

## Verdict: GO

The producer added two new vault rubrics — **R2b** (FP-2025-11 BL-8DCA6908E272 / $3.42 refutation, mirrors email R8 + final-response R17) and **R3c** (USD Cash - Payroll grounding, mirrors email R10 + final-response R20). All five qualifying numeric values (R2/R7/R8/R14/R17) now drop the `approximately` qualifier on `$617.63` / `$3.42` / `$42`, consistent with Format Card § Rule 4 ("Never use `approximately` in front of … exact static values"). Both new vault rubrics score 5/5 on every sub-dim. The P8 (precedent dig) and P9 (USD-cash) hardness levers now trace through all three write surfaces (vault, email, final response). Outcome/Process distribution still 24/0. Density centroid pushed up to ~42–43 by the count change (24 vs 22) plus the reinforced reward gradient on the two universe-grounding calls.

One **Minor soft caveat** (F-AUDIT3 trade-off) logged per the operator's explicit instruction; per policy this does not block.

## Per-Rubric Scorecard — focus on new + changed rubrics

| # | Title slug | Atomicity | Self-Cont | Complete | Flex | Accuracy | Cat | Agent | overall |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **R2b (NEW)** | Vault: BL-8DCA6908E272 variance $3.42 / no expl / no attach | 4 | 5 | 5 | 4 | 5 | 5 | 5 | **4.7** |
| **R3c (NEW)** | Vault: 102000 USD Cash-Payroll → no FX | 5 | 5 | 5 | 5 | 5 | 5 | 5 | **5.0** |
| R2 (changed) | Vault: precedent — `approximately` stripped on $617.63 | 4 | 5 | 5 | 4* | 5 | 5 | 5 | 4.7 |
| R7 (changed) | Email: precedent — `approximately` stripped on $617.63 | 4 | 5 | 5 | 4* | 5 | 5 | 5 | 4.7 |
| R8 (changed) | Email: BL-8DCA variance — `approximately` stripped on $3.42 | 4 | 5 | 5 | 4* | 5 | 5 | 5 | 4.7 |
| R14 (changed) | Final: $617.63 — `approximately` stripped on both $617.63 + $42 | 5 | 5 | 5 | 4* | 5 | 5 | 5 | 4.9 |
| R17 (changed) | Final: BL-8DCA variance — `approximately` stripped on $3.42 | 4 | 5 | 5 | 4* | 5 | 5 | 5 | 4.7 |

`*` Flex 4 (was 5) reflects the soft caveat below. All other previously 5/5 rubrics unchanged. No rubric scores below 4 on any sub-dim. R3c is a clean 5/5/5/5/5/5/5.

**R2b atomicity = 4** mirrors R17's bundling (BL-8DCA + variance + missing explanations + missing attachments — same record, "same data point" rule applies). Acceptable per Format Card § Rule 2 bundling exception.

## Findings

### Major / Moderate

**None.** AUDIT findings F1, F2, F3 are all RESOLVED.

### Minor (soft caveat — non-gating, surfaced per operator instruction)

**F-AUDIT3-trade — `approximately` strip on $617.63 / $3.42 / $42 introduces some rounding rigidity.**

- Issue: Format Card § Rule 4 ("Never use `approximately` for fixed, static values") supports the strip — $617.63 and $3.42 are exact retrieved values from `exc_d8fc13aa2cc742.financial_impact` and `BL-8DCA6908E272.variance` respectively. However, `Docs/12_Always_Failing_Rubrics.md` § Example 3 documents the inverse failure mode: an agent retrieving an exact dollars-and-cents value and reporting it as a round figure ("$347,000" instead of `$347,289.50`) caused 6/6 false-negative fails until the rubric was switched to `approximately`. The current strip prioritizes the Format Card rule; the trade-off is reduced tolerance for natural LLM number normalization.
- Why it's only a soft caveat: the discriminator's job here is to expose a roughly fifteen-times mismatch ($617.63 vs $42, $3.42 vs $42). An agent that reports "$618" or "$617" still carries the discriminative meaning; an agent that reports "$620" or "$600" still discriminates clearly from $42. The likelihood of a 6/6 false-negative on rounding alone is LOW because (a) the retrieval is a one-step `blackline_get_exception` / `blackline_get_reconciliation` call exposing the cents-precision value, and (b) the rubric titles end with "(or similar)" tails that give the judge marginal interpretive latitude (acknowledged that "(or similar)" near exact values is itself a Format-Card grey zone).
- Severity: Minor.
- Recommended (optional) actions: (a) leave as-is and gather real trajectory evidence — if 1–2 of 6 runs fail R2/R7/R8/R14/R17 only on rounding, restore `approximately` on those specific values; (b) document the choice in `_aux/Council_Reports/S3_B_adversarial.md` (this report) and in the eventual AF Justification packet if any of these rubrics show systematic rounding fails; (c) if pre-emptive insurance is desired, restore `approximately` on R8/R17 only (the $3.42 value is more rounding-prone because of its small magnitude — "$3" vs "$3.42" is a likely paraphrase).

### Minor (carried forward from prior rounds; non-gating)

These three Minor flags from rounds 1–2 still apply. None block GO.

- **F2 (prior) — R1 strict-pins `retention AICPA_SQMS_7Y, classification internal`.** Defensible against universe constants. Optional polish only.
- **F3 (prior) — R16 requires explicit reference to `BL-782A2EC69343` in the final response narrative.** Consistent with V3 reference precedent. Optional polish only.
- **F4 (prior) — R11's `(approximately mid-June 2026)` window is narrow.** Evidence clarifies "for example 2026-06-11". Note: R11 retains `approximately` on a date window (Format Card § Rule 4 says "Never use `approximately` for … Dates" — but here it qualifies a fuzzy date description ("mid-June 2026"), not a specific date, so this usage is defensible). Optional polish only.

### Stylistic nit (not a finding)

R2b's UUID (`b2c75e1a-3d8f-4c1b-9234-7e6f0a5d92c4`) is derived from R2's prefix (`…7e6f0a5d92b3`); R3c's UUID (`c3d84f2b-4e9a-4d2c-a345-8f7e1b6c03e6`) is derived from R3a/R3b's prefix (`…03c4` / `…03d5`). Same pattern noted in round 2 — all IDs are unique 36-char hex in canonical 8-4-4-4-12 form; validator does not enforce strict UUID-v4 bits. Not a defect. No action.

## Sweep Results (delta from round 2)

**Sweep 1 — Sub-dim scoring.** All 24 rubrics score ≥4 across every sub-dim. Flex scores on R2/R7/R8/R14/R17 marked at 4 (down from 5) to reflect the soft caveat; still passes the ≥4 floor. R2b and R3c are clean 5/5.

**Sweep 2 — Adversarial alt-path.** New alt-paths probed against the post-AUDIT set:
- Agent reports "$618" instead of "$617.63" — would now fail R2/R7/R14 strictly. Soft caveat logged above.
- Agent reports "$3" instead of "$3.42" — would now fail R8/R17 strictly. Soft caveat logged above (more rounding-prone given small magnitude).
- Agent reports magnitude without sign — still handled (all rubrics use the unsigned magnitude in titles).
- Agent describes USD-cash grounding only in final response but not in vault — would now fail R3c. This is the intended P9 lever-coverage tightening per AUDIT F1.
- Agent describes the FP-2025-11 BL-8DCA refutation only in email/final but not in vault — would now fail R2b. Intended tightening per AUDIT F2.

**Sweep 3 — Reverse coverage.** Both new rubrics map cleanly to prompt asks:
- R2b → "drop a write-up of what you saw on the prior-period record and the documents into the vault under the close-cycle file" (the "prior-period record" includes the actual FP-2025-11 102000 recon record).
- R3c → "drop a write-up of what you saw on the prior-period record and the documents into the vault" + the recon's own variance_explanation cites FX-revaluation, which the universe-grounding refutation belongs alongside.

No rubric goes beyond a prompt ask.

**Sweep 4 — Adversarial Process check.** 24/24 rubrics carry `rubric_category: "outcome"`. Zero process. Matches V3 reference distribution. PASS.

**Sweep 5 — Adversarial atomicity.** No new bundling regressions. R2b mirrors R17's same-record bundle (acceptable). R3c is a single-claim rubric. All previously-acceptable bundlings (R1 metadata, R2/R7 precedent facts, R8/R17/R2b BL-8DCA facts, R11 reminder action+date) remain acceptable.

**Sweeps 6 & 7 — see dedicated sections below.**

## Density Projection (B3) — re-run

The two new rubrics add no NEW tool calls (R2b and R3c both check vault upload content, satisfied by the same upload call as R1). However, they sharpen the reward gradient on calls that are already required for R8/R17 (the `blackline_get_reconciliation BL-8DCA6908E272` call) and for R10/R20 (the `oracle_gl_get_account 102000` call), now triple-incentivized across vault + email + final response.

Re-walking the call budget:

| Block | Calls | Notes |
|---|---:|---|
| Base discovery | 6 | Unchanged. |
| P1 latching reads | 6 | Unchanged. |
| P2 evidence chase | 5–6 | Unchanged from round 2 (still reward-amplified by R3a/R3b/R9a/R9b/R18/R19 split). |
| **P8 precedent dig (now reward-amplified by R2b across vault surface)** | **7–8** | The FP-2025-11 BL-8DCA refutation is now triple-anchored (R2b vault + R8 email + R17 final); the `blackline_get_reconciliation BL-8DCA6908E272` call gradient is steeper, +0 to +1 budget centroid. |
| **P9 universe grounding (now reward-amplified by R3c across vault surface)** | **3–4** | The USD-cash grounding is triple-anchored (R3c vault + R10 email + R20 final); the `oracle_gl_get_account 102000` call gradient is steeper, +0 to +1 budget centroid. |
| P7 multi-write + `reminder_get_all_reminders` | 5 | Unchanged. |
| Cross-service buffer | 6 | Unchanged. |
| **Projected midpoint** | **≈ 40–46** | Centroid 42–44 (slight upward shift from ~42 in round 2). |

Density floor: 40. Projected midpoint comfortably above; centroid moved up from ~42 (round 2) to ~42–44 (round 3) as the count change reinforced the P8 and P9 budgets. Hardness_Plan baseline (44) sits inside the projected range. Candidate trajectory baseline (avg 53 / min 30 / max 69) is well above floor.

**Density verdict: PASS.**

## Hardness Lever Coverage (B4) — re-run

| Lever | Coverage rubric(s) | Verdict |
|---|---|:---:|
| **P1 latching** | R4 (thread_ts 1780147500) + R5 (exc + BL refs) + R8 (FP-2025-11 framing baseline) | **PASS** (unchanged) |
| **P2 blackline_evidence → RV doc chase** | R3a + R3b + R9a + R9b + R18 + R19 — six per-row rubrics across three surfaces | **PASS** (unchanged) |
| **P7 multi-write diversification** | R1 (vault) + R4 (Slack) + R6 (email) + R11 (reminder) — 4 surfaces | **PASS** (unchanged) |
| **P8 precedent dig** | R2 + R2b + R7 + R8 + R13 + R14 + R15 + R16 + R17 — **NINE** rubrics on the precedent dig (was 7 in round 2). Four-pillar refutation now traces through all three surfaces with the FP-2025-11 BL-8DCA refutation present on vault (R2b) + email (R8) + final (R17). | **PASS** (strengthened) |
| **P9 USD-cash → no FX** | R3c (vault) + R10 (email) + R20 (final response) — **THREE** rubrics across all three surfaces (was 2 in round 2). | **PASS** (strengthened) |
| **L9 authority-dismissal overlay** | R13–R17 — four-pillar refutation of George's claim against records | **PASS** (unchanged) |

**Lever coverage verdict: 6/6 PASS, with P8 and P9 measurably strengthened by the per-surface mirror across vault, email, and final response.**

Cross-check: each of the five "hardness-load-bearing" content items (precedent record, $617.63 financial impact, unrecorded_invoice cause, corrective-JE close-out, USD-cash grounding) now appears in at least two distinct write surfaces among {vault, email, final response}, and the FP-2025-11 BL-8DCA refutation appears in all three.

---

## Summary

| Dimension | Round 1 | Round 2 | Round 3 (this report) |
|---|---|---|---|
| Total rubrics | 20 | 22 | **24** |
| Outcome / Process | 20 / 0 | 22 / 0 | **24 / 0** |
| Sub-dim cells < 4 | 2 | 0 | 0 |
| Major findings | 0 | 0 | 0 |
| Moderate findings | 1 (R3/R9 atomicity) | 0 | 0 |
| Minor flags | 3 | 3 | **4** (3 carried + 1 new soft caveat on `approximately` strip) |
| Density projection centroid | ~41 | ~42 | **~43** |
| Density verdict | PASS | PASS | PASS |
| Lever coverage | 6/6 PASS | 6/6 PASS (P2↑) | **6/6 PASS (P8↑, P9↑)** |
| Overall verdict | BLOCK | GO | **GO** |

All three AUDIT findings (F1, F2, F3) resolved. P8 and P9 lever coverage now traces through all three write surfaces. Proceed to coverage matrix.
