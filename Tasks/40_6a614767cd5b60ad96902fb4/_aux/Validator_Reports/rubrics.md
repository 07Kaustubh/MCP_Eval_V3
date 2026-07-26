# Validator report: rubrics

**Status:** PASS  
**Fails:** 0 · **Warns:** 4 · **Notes:** 5

## WARN
- missing-Outcome candidate: prompt uses write-verb `escalat` but no Outcome rubric title contains that verb. Verify an Outcome rubric checks the corresponding write action.
- missing-Outcome candidate: prompt uses write-verb `forwar` but no Outcome rubric title contains that verb. Verify an Outcome rubric checks the corresponding write action.
- rubric[9]: amount `$2,132.00` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[9] (X2 rubric-OE consistency): typed value `2132.00` (amount) in title has no OE step referencing any `amount` value. CONSISTENCY_GAP candidate. WARN-only observation period.

## NOTE
- universe: starpm
- Feasible_Surface loaded: 15 tables with enum maps
- using Fact_Ledger.json for groundedness (403 amounts, 206 emails indexed)
- counts: outcome=17, process=0
- Overall Rubric Quality: 0/17 (0%) with Major, 0/17 (0%) with Moderate+ , 0/17 (0%) with any issue
