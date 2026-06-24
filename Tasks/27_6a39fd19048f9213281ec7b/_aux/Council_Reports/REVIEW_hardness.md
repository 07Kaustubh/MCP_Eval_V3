# REVIEW — Hardness Assessment (Measured)

**Source:** `_aux/Trajectory_Stats.json` (6 real Opus 4.8 runs).

| Metric | Value | Bar | Pass |
|---|---|---|---|
| Avg tool calls (total) | 53.0 | >= 40 | YES |
| Avg tool calls (MCP only) | 43.7 | (info) | — |
| Per-run total range | 30 – 69 | — | — |
| pass@1 | 0.0 (0/6) | <= 0.40 | YES |
| Best-run rubric pass count | 11/13 | — | — |
| Worst-run rubric pass count | 10/13 | — | — |

**Verdict from parse_trajectories.py:** OK.

## What that hides

Every one of the 6 runs missed the same 2 or 3 rubrics. The rubrics the candidate runs uniformly fail include the two that demand the agent identify `brookfield_6000001115` and recommend journalizing it. The runs are "failing" because the task is asking them to name a record that does not exist in the per-task universe. This is not honest hardness — it is hardness from a target that cannot be hit.

Hardness gate would pass on the numbers, but the gate is a sufficient condition for ship, not a necessary one. Truthfulness failures on the rubric override hardness.

## Density check on the corrected scenario

Not run. The scenario cannot be salvaged in-place; the corrected scenario requires a rebuild that introduces a real discriminator.
