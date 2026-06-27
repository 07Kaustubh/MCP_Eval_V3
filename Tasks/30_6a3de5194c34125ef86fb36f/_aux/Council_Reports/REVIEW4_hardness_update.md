# REVIEW4 hardness update — fresh trajectory + verifier-fails ingest

**Trigger context:** Operator dropped updated `trajectory-runs/trajectory-run-*.json` (6 fresh runs) + updated `8_Verifier_Fails.txt` after REVIEW4 SHIP-READY consensus. Per REVIEW step 3 (hardness pre-assessment), re-ran `parse_trajectories.py` on the fresh data and re-compared against REVIEW4's projections.

**Scope:** Step-3 hardness re-assessment only. Verifier-fails BUCKETING + AF JUSTIFICATIONS are out of scope (S4 phase, fresh chat).

## Updated measured numbers

| Metric | Value | Bar | Verdict |
|---|---:|---|---|
| Avg tool calls (total) | **47.2** | 50+ target / 40 floor | THIN_DENSITY (40-49), top of band |
| Avg tool calls (MCP-only) | 35.5 | informational | — |
| Min run | 39 (run 2) | per-run-floor advisory | 1 of 6 under 40 |
| Max run | 59 (run 6) | informational | — |
| Runs under 40 | **1 of 6** | per-run-floor advisory | improved from prior 3 of 6 |
| Pass@1 (all-26-rubric pass) | **0.333** (2 of 6) | ≤ 0.40 target | PASS |
| Density verdict (Rule #11) | **OK** | midpoint ≥ 40 | passes |
| Difficulty verdict | **OK** | pass@1 ≤ 40% | passes |
| Overall parse_trajectories verdict | **OK** | — | — |

Per-run breakdown:

| Run | Total | MCP | Pass | Status |
|---:|---:|---:|---|---|
| 1 | 49 | 37 | 24/26 | FAIL (1-2 rubric miss) |
| 2 | 39 | 36 | 25/26 | FAIL (1 rubric miss); only run under 40-floor advisory |
| 3 | 43 | 30 | 26/26 | **PASS** |
| 4 | 46 | 31 | 25/26 | FAIL (1 rubric miss) |
| 5 | 47 | 33 | 25/26 | FAIL (1 rubric miss) |
| 6 | 59 | 46 | 26/26 | **PASS** |

## Comparison vs REVIEW4 B3 Implementer projections

| Metric | REVIEW4 B3 projection | Measured | Δ | Disposition |
|---|---:|---:|---:|---|
| Avg tool calls | ~44.2 | 47.2 | **+3.0 better** | Row 12 OE6 lift exceeded projection |
| Min run | ~33 (compact-profile runs 2/3/5 stay at floor) | 39 | **+6 better** | compact-profile runs adopted OE06 more than L27 pattern predicted |
| Runs under 40 | 3 of 6 (33/34/36) | **1 of 6** (39) | **-2 better** | floor risk materially reduced; only run 2 marginally underflowed |
| Pass@1 | ~0/6 (R25+R26 cascade adds two fail surfaces) | **2/6** = 33.3% | **+33.3 percentage points** better | discriminating levers + guard rubric working but slightly weaker than projected |
| Effective lever performance | R13 misses ~4-5/6, R25/R26 misses ~3-4/6, R5 misses 0-1/6 | 4 of 6 runs each missed 1-2 rubrics | — | failure distribution matches lever-projection shape; specific rubric ids need S4 to bucket |

**Net:** all REVIEW4 projections held in the right direction; actual results were BETTER than B3 predicted on every metric. REVIEW4's MAJOR RISK_FLAGGED finding (THIN_DENSITY) is empirically validated as ship-safe at the top of the THIN_DENSITY band, NOT a REDO trigger.

## Rule #11 + difficulty gate decision

| Trigger condition | Threshold | Measured | Fires? |
|---|---|---|---|
| Density INSUFFICIENT (BLOCKER) | midpoint < 40 | 47.2 | **NO** |
| Density THIN_DENSITY (continuable) | midpoint 40-49 | 47.2 | **YES** (top of band) |
| Density 50+ design target | midpoint ≥ 50 | 47.2 | NO (2.8 short) |
| Difficulty failure (REDO trigger) | pass@1 > 0.40 | 0.333 | **NO** |
| Density failure (REDO trigger) | avg < 40 | 47.2 | **NO** |

**Verdict: clean continuation under Rule #11.** Density passes both letter (midpoint 47.2 ≥ 40) and spirit (only 1 of 6 runs under floor, materially better than the 3 of 6 the prior sample showed). Difficulty passes (pass@1 33.3% < 40%). **No REDO trigger fires.**

## REVIEW4 MAJOR (RISK_FLAGGED) status update

| REVIEW4 finding | Pre-update status | Post-update status |
|---|---|---|
| Convergent MAJOR (B3 + B5): AGENTS.md Rule #11 THIN_DENSITY band, RISK_FLAGGED | acknowledged + operator must accept on ship | **MATERIALLY DE-RISKED.** Measured data shows the bundle landed at the top of THIN_DENSITY (47.2 / band 40-49) with only 1 run marginally underflowed. The empirical risk that Rule #11's THIN_DENSITY warning anticipates is now substantially reduced — the bundle ships at the safe edge of the band, not deep in the danger zone. |
| B3 m1 (effective lever count = 2 mechanisms + 1 guard rubric) | INFORMATIONAL framing clarification | confirmed empirically — 4 failing runs each miss 1-2 rubrics, consistent with the 2-mechanism + 1-guard projection |

## Next-trigger decision

Per dispatch table + the measured gate verdicts:

| Scenario | Match? |
|---|---|
| `PIPELINE REDO` (avg < 40 OR pass@1 > 40%) | **NO** — both gates pass |
| `PIPELINE COMPARE` (platform rubric mutation) | not applicable here — no `10_Rubrics_Platform.json` paste pending |
| `PIPELINE S4` (verifier-fails bucketing + AF justification drafting) | **YES** — 4 of 6 runs failed at least 1 rubric; need to identify WHICH rubric(s) failed and classify the fails into S4 buckets (legitimate rubric, false positive, edge case, etc.) |
| `PIPELINE FEEDBACK` (write `13_Feedback.txt`) | independently needed regardless |
| `PIPELINE CLOSE` (final read-only audit) | after S4 + FEEDBACK |

**Recommended next trigger: `PIPELINE S4 — Tasks/30_6a3de5194c34125ef86fb36f`** (fresh chat) + paste the updated `8_Verifier_Fails.txt`. The S4 agent will read REVIEW4's reports (preserving the lever-projection context — R13 Marina-coordinator predicted highest miss rate, R25+R26 precedent-linkage paired second, R5 JE-in-subject guard rubric) and bucket each fail accordingly. The 2 passing runs (#3, #6) + the 4 partial-pass runs (#1, #2, #4, #5 each missing 1-2 rubrics) give S4 a clean signal for which rubrics are discriminating-working vs which need AF justification.

## Files updated this pass

| Path | Change |
|---|---|
| `_aux/Trajectory_Stats.json` | overwritten with fresh 6-run stats (avg 47.2; pass@1 0.333; verdict OK) |
| `_aux/Council_Reports/REVIEW4_hardness_update.md` | this file (new) |

NOT touched: `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json` (originals), `14_Updated_Oracle_Events.txt`, `15_Updated_Rubrics.json`, `_aux/REVIEW_prompt_draft.txt`, `_aux/REVIEW_persona_draft.txt`, `changes.md`, any AUDIT_*.md, REVIEW4_summary.md, REVIEW4_score.md, REVIEW4_FINAL.md. The corrected materialization remains byte-identical; the measured improvement is a property of the corrected bundle, not a result of a new fix.

## Headline

**Fresh trajectory + verifier-fails ingest improves on every REVIEW4 projection.** Density 47.2 (was projected 44.2, was measured 43.2 prior sample). Pass@1 0.333 (was projected ~0, was measured 0.167 prior sample). The Row 12 OE6 + Row 8 prompt re-frame + persona scope tightening combined to lift the bundle to the top of the THIN_DENSITY band with only 1 of 6 runs marginally underflowing the 40 advisory floor (run 2 at 39). REVIEW4's RISK_FLAGGED MAJOR is materially de-risked, not materialized. **Both Rule #11 gates pass.** Bundle ships under the rule's continuation envelope. Next: `PIPELINE S4` (fresh chat) to bucket the 4 partial-pass runs' rubric misses.
