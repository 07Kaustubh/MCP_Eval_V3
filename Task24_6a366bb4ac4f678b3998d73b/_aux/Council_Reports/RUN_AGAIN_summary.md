# Re-run summary (Task24, REVIEW-flow, 2026-06-22)

Operator invoked "run again" on the corrected deliverables (5_Prompt.txt + 14_Updated_Oracle_Events.txt + 15_Updated_Rubrics.json). Three layers re-executed in parallel.

## Layer 1: Mechanical validators (on staged 5/14/15)

| Phase | Status | Fails | Warns | Notes |
|---|---|---|---|---|
| prompt | PASS | 0 | 0 | 4 (relative dates — operator-resolved) |
| oe | PASS | 0 | 0 | 1 (12 steps) |
| rubrics | PASS | 0 | 12 ("id is not a uuid" — integers, non-blocking; platform accepts) | 2 (Fact_Ledger groundedness OK, 12 outcome / 0 process) |

Source: `_aux/scratch_corrected/_aux/Validator_Reports/`.

## Layer 2: REVIEW re-score on 5/14/15 (oracle council)

Verdict: **NOT-YET-SHIP-READY** (by strict 5/5-per-sub-dim QC bar)

- Per-phase: 0 FAIL band · 2 NON-FAIL · 1 PASS
- 7 sub-dims lifted from <5 to 5 (Prompt UGT + Feasibility; OE Tool-Name Accuracy + Outcome Accuracy; Rubrics Valid JSON + Self-containment + Ship-readiness)
- 3 sub-dims still at 4 — all KNOWN changes.md rows:
  - Row 5 Pending: Persona Alignment (Edith vs George is_user flag)
  - Row 8 Pending: OE Truthfulness (OE 4 / OE 11 thread misattribution)
  - Row 6 user-skipped: Prompt Truthfulness (Anaya FX framing)
- 0 NEW issues found
- Hardness carried PASS on both axes (density 89.5 avg, pass@1 = 0.167)

Source: `_aux/Council_Reports/REVIEW_rescore.md`.

## Layer 3: Force-FINAL cross-artifact council on 5/14/15 (oracle)

Verdict: **PASS** (by FINAL's BLOCKER / NEW-MAJOR bar)

- 0 BLOCKER · 0 NEW MAJOR · 3 KNOWN (the same rows 5 / 6 / 8 from REVIEW)
- All tight identifiers verify against Fact_Ledger / Universe_Split
- No answer leakage to agent-readable surfaces (Hannah's slack post naming VEN-441207 is the by-design Lever B source, not leakage)
- All 4 Hardness levers triangulate prompt sentence → OE step → rubric end-to-end
- Density projection 45–65 (measured 89.5)
- BF alignment to "BlackLine Close-Discipline & Variance" confirmed
- Every change in 14/15 traces to an Applied changes.md row

Source: `_aux/Council_Reports/FINAL_council.md`.

## Why the two councils give different verdicts

Different bars by design.

- REVIEW uses strict 5/5 per sub-dim — anything <5 = NOT-YET-SHIP-READY, including operator-accepted known issues.
- FINAL uses BLOCKER / NEW-MAJOR — known and accepted issues don't gate upload.

Both verdicts are correct under their own standard. The operator is the tiebreaker on the 3 KNOWN rows:

1. **Row 5 (Persona Alignment)** — lifts to 5 by either flipping `is_user` to Edith in the per-task universe OR rewriting the prompt in George's voice. Light-touch fix, but blocks a 5/5 prompt score until decided.
2. **Row 6 (Anaya FX framing in prompt)** — operator already opted to skip. Caps Prompt/Truthfulness at 4 unless reversed.
3. **Row 8 (OE 4/11 thread misattribution)** — narrative-only; mechanical OE call still lands in a real on-topic thread. Caps OE/Truthfulness at 4 until clarified.

## Recommendation

- If the operator is comfortable shipping with the 3 KNOWN deviations (rows 5/6/8) as accepted trade-offs, the FINAL PASS clears upload. The corrected `14_Updated_Oracle_Events.txt` + `15_Updated_Rubrics.json` are the operative deliverables.
- If a clean 5/5 across every sub-dim is required, decide on rows 5 and 8 (low-cost edits), then re-run mechanical validators + REVIEW re-score to confirm sub-dims lifted. Row 6 stays NON-FAIL unless the prompt edit is unblocked.
