# Verifier Fails — S4 verdict (Task 37 — Sofia Reyes pipeline review, Keystone Mortgage)

## Trajectory hard gates

### T3 — Error Rate
Erroneous runs: 0/6. Verdict: **PASS** (< 3).

### T2 — Agent Failure Rate (pass@1 ≤ 40%)
Raw per-run counts from `8_Verifier_Fails.txt`:
| Run | Passed | Total | passes_all |
|---|---|---|---|
| 1 | 23 | 30 | false |
| 2 | 29 | 30 | false |
| 3 | 28 | 30 | false |
| 4 | 29 | 30 | false |
| 5 | 28 | 30 | false |
| 6 | 30 | 30 | true |

Runs passing all rubrics: 1/6. pass@1: **16.7%**. Verdict: **PASS** (≤ 40%).

**Note on parsed-stats discrepancy.** `_aux/Trajectory_Stats.json` records `pass_at_1 = 0.333` (2 runs of 6). Ground truth from `8_Verifier_Fails.txt` header lines is 1/6. The stats file appears to have used a lenient count that over-credited Runs 2 + 4 + 6 and under-credited Runs 1 + 5. The raw file is authoritative; the discrepancy does not flip the T2 verdict (both readings PASS ≤ 40%).

### T1 — Tool-call density
Average total tool calls per run: **216.8** (min 85, max 338). Well above the 50+ design target and the 40 floor. Verdict: **PASS**.

## Run × rubric fail matrix

13 total fail instances across 8 unique rubrics. No fully all-failing rubrics.

| Fail line | Run | Rubric (short) | Bucket |
|---|---|---|---|
| L14 | 1 | A. Final response names LN-2026-00623 as CTC + 5 outstanding docs | 3 (Legit) |
| L17 | 1 | B. Amy Chen update includes LN-2024-00123 lock date 2024-10-07 | 3 (Legit) |
| L19 | 1 | C. Keisha Williams update includes 4-loan lock dates (3 stale) | 3 (Legit) |
| L23 | 1 | D. Marcus Webb update includes LN-2024-00125 lock date 2024-10-17 | 3 (Legit) |
| L30 | 1 | E. Final response names LN-2026-00010 with 7 outstanding docs | 3 (Legit) |
| L32 | 1 | F. Natasha Okafor update includes LN-2025-00286 lock date 2025-05-12 | 3 (Legit) |
| L37 | 1 | G. James Thornton update includes 3-loan lock dates (2 stale) | 3 (Legit) |
| L70 | 2 | F. Natasha Okafor update omits LN-2025-00286 entirely | 3 (Legit) |
| L90 | 3 | A. Final response omits LN-2026-00623 | 3 (Legit) |
| L106 | 3 | E. Final response omits LN-2026-00010 | 3 (Legit) |
| L143 | 4 | H. LOS activity note on at least one loan | **2 (Judge Error)** |
| L166 | 5 | A. Final response misclassifies LN-2026-00623 as dormant | 3 (Legit) |
| L182 | 5 | E. Final response names LN-2026-00010 without doc count | 3 (Legit) |

## Classifications

- **Bucket 1 (rubric invalid): 0 rubrics.** No rubric is the problem. See empty `S4_fixes.md`.
- **Bucket 2 (judge error): 1 rubric × 1 run (Rubric H, Run 4).** See `S4_judge_errors.md`. Verifier justification claims "No LOS activity_create tool calls were found in the trajectory"; direct inspection of `trajectory-runs/trajectory-run-4 (23).json` finds 26 `mortgage_los_add_activity` tool_use nodes paired with 26 tool_result payloads that return legitimate activity IDs + created_at timestamps. Runs 1, 2, 3, 5, 6 evaluated the same tool call set as Pass on this rubric. Root cause: judge grepped for a non-existent tool name (`activity_create`) instead of the real Keystone tool name (`mortgage_los_add_activity`).
- **Bucket 3 (legitimate model failure): 7 unique rubrics × 12 fail instances.** See `S4_AF_justifications.md`.

## All-Failing Rubrics sub-dim (v11)

Bucket 1 ratio = 0 / 8 = **0% (< 25%)**. Score: **5/5 (PASS)**. No failing rubric is caused by invalid rubric design; failures decompose to one systemic Run-1 aged-file compression pattern (6 rubrics), a shared final-response depth-vs-breadth trap on the two anomaly loans (2 rubrics × 3 runs each), a single Run-2 email omission (1 rubric), and a single judge error (1 rubric).

## Hardness calibration vs `_aux/Hardness_Plan.md`

Stump hypothesis at S1: "premature CTC on LN-2026-00623 + max-outstanding-docs on LN-2026-00010 are anomalies that a broad-summary agent misses in the final response; aged-file lock dates require per-loan atom fidelity that a compressing agent will collapse."

Empirical validation:
- Predicted final-response miss on LN-2026-00623 → 3 of 6 runs fail (Rubric A). **Hit.**
- Predicted final-response miss on LN-2026-00010 → 3 of 6 runs fail (Rubric E). **Hit.**
- Predicted aged-file lock-date compression → 5 of 6 per-LO cohort rubrics fail on Run 1 (B, C, D, F, G). **Hit — concentrated in one run.**
- Predicted terminated-LO surfacing (Veronica Hayes / Brian Mitchell) → 0 fails (Rubrics 8 + 9 + 12 in original). **Over-predicted — this lever was too soft; the LO cohort routinely names both departed employees.**
- Predicted CRM engagement creation gap → 0 fails. **Over-predicted — universal Pass.**
- Not predicted, did surface: Run 2 completely omitted LN-2025-00286 from the Natasha email (single-loan drop). **Under-predicted — a Bucket 3 miss that's a proper legit fail but was not in the S1 hypothesis.**

Hit rate on stump levers: 3 of 5 predicted (60%). Two over-predictions (terminated-LO + CRM engagement) and one under-prediction (single-loan drop within a per-LO update).

Calibration deltas appended to `Tasks/_meta/Hardness_Patterns_Log.md` and `Tasks/_meta/Stump_Hypotheses.md`.

## Action items

- Nothing to change in `7_Rubrics.json`. Zero Bucket 1 rubrics.
- Ship `S4_AF_justifications.md` per rubric per run to platform (7 unique justifications; per-run citations included).
- Optional platform appeal for the Run 4 Rubric H judge error (see `S4_judge_errors.md`) — verifier used the wrong tool name.
- Persist the calibration deltas: aged-file compression is a real Opus-4.8 failure mode on Sofia-style breadth-vs-depth tasks; premature-CTC anomaly + max-outstanding-docs anomaly are load-bearing stumping levers; terminated-LO + CRM engagement are soft levers that no longer stump.

## Verdict

**S4 verdict: PASS.** Task 37 is properly calibrated. pass@1 = 16.7% (well below the 40% ceiling), density 216.8 avg (well above 50 design target), 0 error runs, 0 invalid rubrics, 1 optional judge-error appeal. The corrected materialization (`15_Updated_Rubrics.json`) does not need re-verification — the two Applied rows tightened rubrics [3] + [24].justification, and neither of those rubrics appears in the 8 failing rubrics identified above (rubric [3] passed all 6 runs on the ORIGINAL narrower title; rubric [24] passed all 6 runs).

No REDO. No re-run. Task is shippable.
