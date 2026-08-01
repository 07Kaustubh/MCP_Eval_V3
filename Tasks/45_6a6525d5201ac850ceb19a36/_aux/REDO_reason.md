# REDO Reason - Task 45 (StarPM V4, CB-own) - DIFFICULTY FAIL

## Verdict
REBUILD_CANDIDATE_DIFFICULTY. Overall pass@1 = 0.75, far above the 0.40 ceiling.
Opus 4.8, the model under test (Hard rule 1), passed EVERY rubric on EVERY run.

## Computed numbers
Cross-checked: `_aux/Trajectory_Stats.json` vs a fresh `Validators/parse_trajectories.py` run. Both agree.

| Model | pass@1 | runs passing ALL 20 rubrics | avg tool calls (total) | avg MCP-only |
|---|---|---|---|---|
| Opus 4.8 (under test) | 1.00 | 6 / 6 | 37.0 | 27.5 |
| Gemini | 0.50 | 3 / 6 | 43.3 | 37.3 |
| Overall | 0.75 | 9 / 12 | 40.2 | 32.4 |

- Difficulty ceiling: pass@1 <= 0.40. Overall 0.75 and Opus 1.00 both FAIL. This is the decisive failure.
- Density: overall avg 40.2 total, above the StarPM QC-spec floor of 15. Opus averaged 37.0, below the 40 per-model design target (Hard rule 11). Secondary flag, not the trigger.
- Evidence files: `Agent_Responses/{Opus,Gemini}/*.json` (12 runs), `8a_Verifier_Fails_Opus.txt`, `8b_Verifier_Fails_Gemini.txt`, `_aux/Trajectory_Stats.json`.

## Why Opus aced it (root-cause for the rebuild's HARDNESS)

The design (`_aux/Hardness_Plan.md`) rested on a dual-model recipe:
- L2 structured-DB skip: SYMMETRIC primary.
- L1 latching + L10 supersession ("latest-row / trust-the-done-ticket"): OPUS-SELECTIVE stump.
- L31 explicit negative directive: GEMINI-SELECTIVE stump.

Gemini failed as predicted (3/6; the negative-directive omission bit on the failing runs).
Opus did NOT: the OPUS-SELECTIVE lever (L1/L10) failed to stump.

Opus 4.8 is now robust against exactly this trap class:
1. It did not latch on the two "done"-flavored maintenance tickets or the prior selReady turn.
2. It disambiguated the two make-ready rows by SEMANTIC content (move-out 6/15 > 6/1 identifies the current turn), not by the recency heuristic the trap baited (the selReady decoy row was created LATER, 5/29 > 5/22).
3. It read the structured single-select (fldTurnStatus=selProg) and the "still open" note, reconciled the past-due 6/30 target and the future 7/15 QC event, and correctly issued the hold / kick-back.

The discriminator was a SINGLE-HOP structured-DB read plus a recency-versus-meaning disambiguation. Both are 4.8-robust:
- Recency / latching / supersession traps ("pick the latest record", "trust the DONE ticket") no longer fool 4.8; it reads fields and disambiguates by meaning.
- There was no multi-hop reconciliation chain, no COMPUTED discriminator (net-vs-gross L11 was only a "partial" corroborator, never load-bearing), and no genuine ambiguity that survives careful field-reading.

## What the rebuild must change (feeds HARDNESS)

**PRIMARY fix (see Learnings L36): stop leaking the discriminators in the prompt.** The root cause was not a weak lever class on its own; it was that the candidate prompt named every trap, so inference load was near zero. Each lever mapped to a prompt sentence that pre-solved it: L2 from "finished with the bill still sitting unpaid, does not count as closed to me"; L10 from "moved out in the middle of June with a target-ready date at the end of the month" (which IS recbd087's distinguishing content, so no row disambiguation remains); L31 from "if it is not, say so plainly and hold it"; L9 from "a re-inspection on the calendar for the middle of this month". The rebuild's prompt MUST force discovery: do NOT define billed-but-unpaid, do NOT enumerate the scopes, do NOT pin the turn by its move-out / target dates, do NOT name the re-inspection as a gate. Ask for the QC determination and let the agent discover which make-ready row is live, reconcile QuickBooks itself, and surface the future event on its own. At S1, audit every rubric discriminator against the prompt: if a criterion can be satisfied from a prompt clause without discovering anything, the prompt leaks and must be tightened.

**SECONDARY (for margin): strengthen the Opus-selective lever so it survives careful reading even absent leakage.** Recency / latching / supersession (L1/L10) is 4.8-robust on its own; prefer a COMPUTED or MULTI-HOP discriminator:
- Net-vs-gross (L11) made load-bearing: "is the scope closed?" must require reconciling billed vs paid vs completed across QuickBooks + Airtable + the vendor thread, where no single field states the answer.
- A genuine multi-hop chain (L8): 3+ dependent lookups with a non-obvious precedence rule (which source wins when they disagree), not one structured-select read.
- Keep one SYMMETRIC structured-DB skip, but make the truth require reconciliation, not lookup.

**Density:** also lift Opus above 40 (design for margin, plan L33): hold 5-6 distinct writes and a discovery sweep a competent agent cannot short-circuit.

The universe atoms are all reusable (L36): the live selProg row, the decoy selReady row, the two "done" tickets, the unpaid QuickBooks bills, the past-due target, the 7/15 re-inspection. Only the prompt's information content must change. Before S1, consult `Tasks/_meta/Learnings.md` (especially L36) and `Tasks/_meta/Stump_Hypotheses.md` for 4.8-robust vs 4.8-fragile lever classes.

## Retained (unchanged)
- Per-task universe `3_UniverseDataForThisTask.json`: unchanged. No universe edits; injection artifacts intact.
- Persona (Jaime Salinas, p_007, QC Inspector) + Business Function 3 (QC & Field Services): unchanged.
- All `_aux/` S0 outputs (Universe_Split, Universe_Index, Fact_Ledger, Feasible_Surface): valid, same universe.
- Originals 5/6/7 and the failing trajectory evidence: archived under `_aux/Candidate_Originals/`.
