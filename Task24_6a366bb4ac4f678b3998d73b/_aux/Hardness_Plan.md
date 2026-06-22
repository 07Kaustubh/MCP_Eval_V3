# Hardness_Plan (synthesized from REVIEW phase artifacts)

This file is a synthesized Hardness_Plan-equivalent for a REVIEW-flow task that has measured trajectory data instead of a pre-build HARDNESS scan. Source: `_aux/Council_Reports/REVIEW_hardness.md` + `_aux/Trajectory_Stats.json` + `changes.md` density/difficulty rows.

## Measured hardness verdict

- Density: avg 89.5 tool calls / run across 6 runs. PASS at 40+.
- Difficulty: pass@1 = 0.167 (1/6 runs passed all 12 rubrics). PASS at <= 0.40.
- Trajectory parser verdict: OK.
- Both axes empirically validate that the task is properly hard for Opus 4.8.

## Levers (validated against actual trajectory fail patterns)

### Lever A: FX-vs-duplicate ambiguity (primary attractor)

Two contradictory narratives at the same dollar amount ($6,328.86) on the same recon (BL-516B536953DA). Anaya Wallace's recon `variance_explanation` is generic ("Adjusting entry pending Manager approval; will clear in resubmit."). The exception's `root_cause` field literally says "FX rate table refresh ran 4 hours late on BD2" even though the exception type is `duplicate_entry_detected`. The GL-overstated direction on 210000 also rules out an FX-revaluation miss (revaluation miss would understate the liability).

- Trigger in prompt: "Two different stories landed on the same recon over the last two and a half weeks, both around six thousand three hundred dollars, both on AP external vendors, and they may or may not be the same underlying line."
- Trigger in OE: OE 2 (exception's contradictory root_cause text), OE 3 (GL-direction check rules out FX), OE 4 (Hannah's slack post pins it on a duplicate vendor invoice).
- Trigger in rubric: rubric 2 (attribute the JE to duplicate, not FX) + rubric 7 (review note rejects FX hypothesis explicitly).
- Empirical bite: Run #2 committed to the FX narrative and never named VEN-441207. Runs #3-#6 partially missed the cause.

### Lever B: Vendor-name-only-in-slack

Vendor VEN-441207 is mentioned exactly once in the universe: Hannah Grant's slack post on 2026-05-27 in #monthly-close-coordination. There is no SAP AP invoice for VEN-441207 in the universe and no AP invoice anywhere in the universe carries the amount $6,328.86. The agent has to commit to a vendor surfaced only from a Slack message with no corroborating invoice record.

- Trigger in prompt: "I need to walk through everyone's notes and the exception record" (forces the agent to read slack).
- Trigger in OE: OE 4 (slack search).
- Trigger in rubric: rubric 6 (review note names VEN-441207) + rubric 11 (final response names VEN-441207).
- Empirical bite: trajectories that never reached Hannah's slack post hedged on the vendor or named the wrong one.

### Lever C: SLA-overdue root_cause lock

The exception exc_a0f77f2a19104e has `sla_due_at` already breached (2026-05-26T12:54:31-04:00). The `blackline_update_exception` tool returns `EX.SLA_OVERDUE` because of the breach, even though the update is the only path that overwrites the misleading FX-rate-refresh text in `root_cause`. The agent has to know the update call is the right intent even though the tool returns a platform-side error.

- Trigger in prompt: "update the exception so it stops looking orphaned".
- Trigger in OE: OE 6 (call update_exception with overwriting root_cause).
- Trigger in rubric: rubric 4 (graded on call intent, not platform acceptance; evidence acknowledges EX.SLA_OVERDUE will return).
- Empirical bite: even passing runs noted EX.SLA_OVERDUE; non-passing runs either skipped update_exception or read the error as a signal to abandon.

### Lever D: SOX adjusting-entry approval gate

The corrected OE 5 sets `is_standard_entry=true` so the JE classifies as standard correcting. The original CB had it `false` (adjusting), which triggers a SOX manager-only approval gate that no reachable role in this universe can clear; Run #2 stalled there. The lever still bites on the JE classification choice, because an agent that defaults to "adjusting" without checking will stall the lifecycle.

- Trigger in prompt: "I'll need to put the corrective accounting through the full lifecycle".
- Trigger in OE: OE 5 (full lifecycle to state=posted with is_standard_entry=true).
- Trigger in rubric: rubric 1 (state=posted) + rubric 2 (cause attribution).
- Empirical bite: Run #2 stalled at submitted on the adjusting-entry SOX gate.

## Stump Hypothesis (synthesized)

Opus 4.8 fails by reading the exception's `root_cause` text first, locking the FX narrative in mind, then either filing an FX-framed JE that doesn't reverse the duplicate posting, or stalling on the adjusting-entry SOX gate, or hedging the vendor name because no AP invoice mentions $6,328.86 or VEN-441207. The duplicate-posting cause is only recoverable through Hannah's slack post — every other artifact (recon variance, exception root_cause, GL/subledger tie) requires inference, not lookup.

## Notes for Force-FINAL council

- Hardness_Plan is synthesized from measured trajectory data; original CB build did not produce a pre-build Hardness_Plan because this is a REVIEW-flow task. Council should treat the lever list above as the authoritative lever set for the Force-FINAL lever-preservation check on `5_Prompt.txt` + `14_Updated_Oracle_Events.txt` + `15_Updated_Rubrics.json`.
- Two `changes.md` rows are Pending (row 5 persona is_user flag, row 8 OE 4/11 thread misattribution) and one row is user-skipped (row 6 Anaya FX framing in prompt). Council should flag these as already-known findings if surfaced, not as new issues.
