# Verification — S4 (Task 37)

## Data sources consulted
- `7_Rubrics.json` — rubric set being classified (30 rubrics, original)
- `8_Verifier_Fails.txt` — raw verifier output for 6 runs (226 lines)
- `trajectory-runs/trajectory-run-{1..6} (N).json` — per-run trajectories (6 files)
- `_aux/Universe_Split/` — ground-truth values re-confirmed for loans, LOs, dates, amounts
- `_aux/Fact_Ledger.json` — atom cross-reference
- `Mortgage_Base_Universe/6_Server_Tools_Details.json` — tool catalog (used to validate Bucket 2 finding: verifier grepped `activity_create`, real tool is `mortgage_los_add_activity`)
- `_aux/Trajectory_Stats.json` — parsed density stats (noted a per-run pass count miscount vs raw file; raw treated as authoritative)

## Eval spec verified
- `Evals/4_Verifier_Fails_Eval.md` — bucket taxonomy (Rubric Invalid / Judge Error / Legit Fail) applied per failing rubric
- 5-point pre-write checklist applied YES on all 5 items before each Bucket 3 justification
- Trajectory-walk gate (v10 mandate) — direct inspection of trajectory JSON confirmed the Bucket 2 finding on Rubric H Run 4 (26 successful `mortgage_los_add_activity` tool_use / tool_result pairs, not zero)

## QC spec sub-dims verified
- **T3 Error Rate:** 0 errors / 6 runs. PASS.
- **T2 Agent Failure Rate:** pass@1 = 1/6 = 16.7% (from raw 8_Verifier_Fails.txt run headers 23 / 29 / 28 / 29 / 28 / 30). PASS (≤ 40%).
- **T1 Tool-call Density:** avg 216.8 total tool calls / run (min 85, max 338). PASS (well above 50 design target).
- **All-Failing Rubrics sub-dim (v11):** Bucket 1 ratio = 0 / 8 = 0% (< 25%). Score 5/5 PASS.

## Verification statements
- [x] Trajectory walk recorded for EVERY failing rubric (13 fail instances across 8 unique rubrics).
- [x] T2 + T3 hard gates evaluated and recorded in `S4_verdict.md`.
- [x] Bucket 1 ratio computed; All-Failing Rubrics sub-dim scored (5/5).
- [x] 5-point checklist confirmed YES on all 5 for every Bucket 3 justification.
- [x] `check_justification.py` exit 0 on the AF batch (`S4_AF_justifications.md`).
- [x] Rubric H Bucket 2 finding cross-verified: Run 4 trajectory JSON parsed for `mortgage_los_add_activity` tool_use nodes (26 found) + matched tool_result payloads (26 found, each with unique activity id + created_at); other 5 runs' verifier justifications name the same tool correctly and mark Pass, confirming the verifier's Run 4 wording (`activity_create`) is a tool-name grep mismatch.

## Discrepancies surfaced

1. **`_aux/Trajectory_Stats.json` pass-count miscount.** Stats file records per-run passed counts of (28, 30, 28, 30, 28, 28) → `pass_at_1 = 0.333` (2/6 pass_all). Raw `8_Verifier_Fails.txt` header lines record (23, 29, 28, 29, 28, 30) → true pass@1 = 1/6 = 16.7%. Both readings PASS T2 (≤ 40%), so the discrepancy does not flip the verdict. Root cause is a probable off-by-two heuristic in the stats parser on the "Rubrics grading results N/M passed" line format. Not fixed in this S4 run (stats file is informational only for T1 density, which is correctly computed independently).

2. **Verifier judge tool-name mismatch on Rubric H Run 4.** Documented in `S4_judge_errors.md`. Recommend platform appeal.

No other discrepancies.
