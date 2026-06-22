# REVIEW hardness assessment (measured, fresh re-run)

Source: `_aux/Trajectory_Stats.json` (6 platform-exported runs in `trajectory-runs/` + `8_Verifier_Fails.txt`).

## Density (measured)

| Run | Tool calls (total) | MCP-only |
|---|---|---|
| 1 | 100 | 74 |
| 2 | 70 | 50 |
| 3 | 93 | 72 |
| 4 | 86 | 68 |
| 5 | 111 | 88 |
| 6 | 77 | 54 |

- avg_tool_calls_total = **89.5**
- density_ok_at_40 = **TRUE** (more than 2x the floor)

## Difficulty (measured, fresh parser re-run)

Per-run rubric pass rates from `8_Verifier_Fails.txt`:

| Run | Result |
|---|---|
| #1 | 12/12 PASS |
| #2 | 3/12 FAIL |
| #3 | 11/12 FAIL |
| #4 | 7/12 FAIL |
| #5 | 9/12 FAIL |
| #6 | 5/12 FAIL |

- **pass@1 = 1/6 = 0.167** = 16.7%
- difficulty_ok_at_40pct = **TRUE** (well under the 0.40 ceiling)

Note: fresh parser run produced slightly different per-run pass counts vs the prior review (12, 4, 11, 6, 9, 6 then; 12, 3, 11, 7, 9, 5 now). Pass@1 and the OK verdict are identical.

## Combined verdict
- Density: **PASS** (89.5 avg, floor 40)
- Difficulty: **PASS** (pass@1 = 0.167, ceiling 0.40)
- Trajectory parser verdict: **OK**

Both hardness metrics clear. The task IS properly hard for Opus 4.8 - the FX-revaluation narrative is a strong attractor that 5 of 6 runs partially or fully fell for. The "two contradictory narratives on the same dollar amount" lever, the SLA-overdue exception's `root_cause` text trap, the SOX adjusting-entry approval gate, and the vendor-name-only-in-slack lever all bite empirically.

## Lever coverage check (validated against actual fail patterns)
- **FX-vs-duplicate ambiguity lever** - validated. Run #2 committed to the FX narrative because the exception's `root_cause` field literally says "FX rate table refresh ran 4 hours late on BD2" and Anaya's recon `variance_explanation` is generic ("Adjusting entry pending Manager approval; will clear in resubmit.").
- **Vendor-only-in-slack lever** - validated. VEN-441207 is mentioned exactly once in the universe (Hannah's slack post on 2026-05-27). There is no SAP AP invoice for VEN-441207, and there is no AP invoice anywhere in the universe with amount $6,328.86. The agent has to commit to a vendor surfaced only from a Slack message, with no corroborating invoice record.
- **SLA-overdue root_cause lock** - validated. Even passing runs note `EX.SLA_OVERDUE` on the `update_exception` call. Rubric 4 explicitly acknowledges this in its evidence text in the corrected `15_Updated_Rubrics.json`.
- **SOX adjusting-entry gate** - validated. The `is_standard_entry=false` trap forces a re-classification or stalls the JE at submitted (Run #2 stalled there). The corrected OE 5 in `14_Updated_Oracle_Events.txt` switches the flag to `true` so the prescribed `state=posted` lifecycle is reachable.
