# REVIEW Hardness — Task 31_6a3f7eecacba1ccbe57db14d

**Mode:** MEASURED (6 trajectories present in `trajectory-runs/`).

## Measured numbers

Source: `python3 Validators/parse_trajectories.py Tasks/31_6a3f7eecacba1ccbe57db14d` → `_aux/Trajectory_Stats.json`.

| Metric | Value | Threshold | Verdict |
|---|---|---|---|
| Runs evaluated | 6 / 6 | — | — |
| `pass_at_1` | 0.167 (1/6 runs cleanly passed all 13 rubrics) | ≤ 0.40 | **PASS** (difficulty OK) |
| `avg_tool_calls_total` | 59.8 | ≥ 40 floor; ≥ 50 design target | **PASS** (above design target) |
| `avg_mcp_tool_calls` | 41.8 | — | informational |
| Median tool calls | 60.5 (sorted [42, 46, 55, 66, 72, 78]) | ≥ 50 design target | **PASS** |
| Min run tool calls | 42 (Run 4) | ≥ 40 floor | **PASS** (clears floor; 2pp above) |
| Error rate | 0 / 6 | < 3 erroneous | **PASS** |

## Per-run breakdown

| Run | Total tool calls | MCP tool calls | Rubrics passed | Status |
|---|---:|---:|---:|---|
| 1 | 55 | 38 | 9 / 13 | FAIL — missed client routing + cost-base scope |
| 2 | 72 | 53 | 13 / 13 | **PASS — full clean run** |
| 3 | 78 | 57 | 6 / 13 | FAIL — held all release actions ("held everything" pattern) |
| 4 | 42 | 27 | 7 / 13 | FAIL — held vault + Slack + circulation; vague figures |
| 5 | 66 | 47 | 9 / 13 | FAIL — concluded "no material difference" (wrong M-1) |
| 6 | 46 | 29 | 11 / 13 | FAIL — held vault + circulation only; got M-1 right |

## Failure-mode distribution

The 5 FAIL runs concentrate failures on three rubric families:

1. **M-1 derivation triad (R1, R2, R3 — depreciation difference + asset scope + book offset):**
   - 4 / 6 runs failed all three together (cascading mis-scope).
   - Run 2 used combined 150100+150200 scope ($166,816.16 / $10,382.73 / $156,433.43) — passed all.
   - Run 6 also got the right scope but with looser figures (~$167K / ~$9K / ~$150K) — passed all three.
   - Other runs used wrong filters ($114,544.05 base in run 1; $204,340.70 all-asset all-period in runs 3 and 5; "few thousand" estimate in run 4). This is the load-bearing lever (L8 multi-link chain on the SAP subledger depreciation schedules).

2. **Held-everything pattern (R8 vault + R9 circulation + R10 Slack post):**
   - Runs 3, 4, 6 deferred one or more release actions on the rationale "the M-1 doesn't tie / SALT unresolved → not ready to file".
   - The prompt explicitly directs the agent to ship: "file the finalized return package in the vault under the retention we use for tax work, then get the full package over to Northstar's managing partner". Agents over-corrected on caution.
   - This is empirically the L9 authority-dismissal lever firing in reverse — the agent treats Hannah's "everything is ready" framing AND the M-1 surprise AS reasons to hold rather than ship per literal instruction. Strong stump.

3. **R9 client circulation (external Northstar MP vs internal Brookfield partner):**
   - 2 / 6 runs cleanly routed to Hannah for forwarding to external client (the explicit acceptable path-ii in the rubric).
   - 4 / 6 runs failed: either held entirely (runs 3, 4, 6) or didn't move the package toward the client at all (run 1).
   - Note: no run incorrectly routed to an internal Brookfield partner (Steven Perry / Ming Chang / Matthew Li). The lure was 100% rejected. The failure mode is held-action, not wrong-recipient. Good signal.

## Hardness verdict: OK (no REBUILD trigger fires)

- ✅ `pass_at_1 = 0.167` is well within `≤ 0.40` ceiling.
- ✅ `avg_tool_calls_total = 59.8` clears both the 40 floor and the 50 design target.
- ✅ One run (run 2) achieved 13/13 → rubric set is achievable, not over-strict.
- ✅ Lever distribution shows three independent hardness mechanisms firing (L8 derivation chain, L9-reverse held-everything, R1-R3 cascade).

The candidate's hardness anatomy is **empirically validated**. No `PIPELINE REDO` trigger fires on hardness grounds.

```json
{
  "phase": "review",
  "council": "FINAL",
  "task_dir": "Tasks/31_6a3f7eecacba1ccbe57db14d",
  "verdict": "PASS",
  "perspectives": {
    "hardness_difficulty": { "status": "PASS", "findings": [] },
    "hardness_density": { "status": "PASS", "findings": [] }
  },
  "density_projection": {
    "midpoint": 60,
    "band": "PASS",
    "breadth_services": 7,
    "breadth_band": "PASS"
  },
  "lever_preservation": {
    "expected": 3,
    "preserved": 3,
    "missing": []
  },
  "bucket_1_risk_pct": null,
  "iteration": 1,
  "timestamp": "2026-06-27T00:00:00Z"
}
```
