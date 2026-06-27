# REVIEW hardness assessment — Task 30_6a3de5194c34125ef86fb36f

**Source:** measured (6 trajectory runs in `trajectory-runs/`).
**Parser output:** `_aux/Trajectory_Stats.json`.

## Measured numbers

| Metric | Value | Bar | Verdict |
|---|---:|---|---|
| Runs evaluated | 6 / 6 | — | — |
| Avg total tool calls | **43.2** | ≥50 design target / ≥40 floor | **THIN_DENSITY** (40-49 band) |
| Avg MCP tool calls | 36.8 | — | — |
| pass@1 | **0.167** | ≤ 0.40 | **OK** (1 / 6 runs passed all rubrics) |
| Density @ 40+ | OK | ≥40 floor | OK |
| Difficulty @ 40% | OK | pass@1 ≤ 0.40 | OK |
| Overall script verdict | OK | — | OK |

## Per-run breakdown

| Run | Total | MCP | Status |
|---|---:|---:|---|
| 1 | 50 | 45 | ok |
| 2 | 34 | 29 | ok |
| 3 | 33 | 31 | ok |
| 4 | 56 | 45 | ok |
| 5 | 36 | 35 | ok |
| 6 | 50 | 36 | ok |

3 of 6 runs (#2, #3, #5) sit BELOW the 40-call floor. The avg only crosses the floor because runs #1, #4 and #6 went to 50+. This is a fragility signal: a real-platform sample of differently-seeded runs could easily slip the avg below 40.

## Verifier-fail concentration

- Run #5 = 24/24 PASS. Other five runs all FAIL with 23/24.
- **All five failing runs fail the EXACT SAME rubric** — the Marina-Soko-as-CDD-coordinator memo-content rubric (item #13 in `7_Rubrics.json`).
- Single-lever hardness: the task's pass@1 = 16.7% is driven almost entirely by ONE rubric. Remove that rubric and pass@1 becomes 100%.

This is the most important hardness finding. Sharp single-rubric pass/fail is a fragile lever — if the platform's grader were more permissive on the "active clearance role" inference, the task would collapse to ~100% pass@1.

## Cross-check against Council B-B3 / B-B4

Projected density (predicted before trajectories arrived): scoping the work — pull 1 JE, search emails, search Slack, list reminders, delete 1 reminder, list vault docs, upload 1 memo, post 1 Slack threaded reply, send 1 email — yields ~15-20 atomic tool calls at minimum, ~30-40 with reasonable verification overhead. The actual avg of 43.2 (with 3 runs under 40) confirms the projection: this scenario has limited work surface. Most of the variance comes from how much exploratory listing the agent does before settling on the JE.

## Hardness verdict

NOT a hardness REBUILD by the numeric triggers — density floor and pass@1 cap both satisfied. But the task is **marginal on both axes**:

- Density 43.2 sits in the THIN band; half the runs underflow 40.
- pass@1 = 16.7% is monopolized by one rubric; lever diversity is thin.

Flag for SALVAGEABLE path with explicit hardness-fragility note.
