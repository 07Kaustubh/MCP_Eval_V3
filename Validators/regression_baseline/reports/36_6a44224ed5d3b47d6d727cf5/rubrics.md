# Validator report: rubrics

**Status:** PASS  
**Fails:** 0 · **Warns:** 5 · **Notes:** 5

## WARN
- missing-Outcome candidate: prompt uses write-verb `fil` but no Outcome rubric title contains that verb. Verify an Outcome rubric checks the corresponding write action.
- rubric[24]: amount `$4,500` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[24]: amount `$750` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[24]: amount `$4,500` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[24]: amount `$1,100` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.

## NOTE
- universe: moveops
- Feasible_Surface loaded: 11 tables with enum maps
- using Fact_Ledger.json for groundedness (64 amounts, 216 emails indexed)
- counts: outcome=34, process=0
- Overall Rubric Quality: 0/34 (0%) with Major, 0/34 (0%) with Moderate+ , 0/34 (0%) with any issue
