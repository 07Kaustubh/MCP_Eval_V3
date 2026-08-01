# Validator report: rubrics

**Status:** PASS  
**Fails:** 0 · **Warns:** 8 · **Notes:** 5

## WARN
- rubric[4]: amount `$387` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[5]: amount `$1,340` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[16]: amount `$387` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[17]: amount `$1,340` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[4] (X2 rubric-OE consistency): typed value `387.00` (amount) in title has no OE step referencing any `amount` value. CONSISTENCY_GAP candidate. WARN-only observation period.
- rubric[5] (X2 rubric-OE consistency): typed value `1340.00` (amount) in title has no OE step referencing any `amount` value. CONSISTENCY_GAP candidate. WARN-only observation period.
- rubric[16] (X2 rubric-OE consistency): typed value `387.00` (amount) in title has no OE step referencing any `amount` value. CONSISTENCY_GAP candidate. WARN-only observation period.
- rubric[17] (X2 rubric-OE consistency): typed value `1340.00` (amount) in title has no OE step referencing any `amount` value. CONSISTENCY_GAP candidate. WARN-only observation period.

## NOTE
- universe: starpm
- Feasible_Surface loaded: 15 tables with enum maps
- using Fact_Ledger.json for groundedness (403 amounts, 206 emails indexed)
- counts: outcome=20, process=0
- Overall Rubric Quality: 0/20 (0%) with Major, 0/20 (0%) with Moderate+ , 0/20 (0%) with any issue
