# Validator report: rubrics

**Status:** PASS  
**Fails:** 0 · **Warns:** 17 · **Notes:** 5

## WARN
- rubric[0]: evidence contains dates/IDs/amounts NOT in criterion: ['rec98bdfeec73545e']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[1]: evidence contains dates/IDs/amounts NOT in criterion: ['rec987aae7d522057']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[2]: evidence contains dates/IDs/amounts NOT in criterion: ['rec8b679d92f30753']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[8]: dollar amount `$1,975.00` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[9]: evidence contains dates/IDs/amounts NOT in criterion: ['$1,622.00', '$7,325.00']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[9]: dollar amount `$10,980.00` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[10]: dollar amount `$3,655.00` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[23]: evidence contains dates/IDs/amounts NOT in criterion: ['$7,325.00']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[23]: dollar amount `$10,980.00` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[30]: evidence contains dates/IDs/amounts NOT in criterion: ['$1,622.00', '$7,325.00']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[30]: dollar amount `$10,980.00` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[7]: amount `$0.00` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[8]: amount `$1,975.00` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[9]: amount `$10,980.00` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[10]: amount `$3,655.00` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[23]: amount `$10,980.00` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[30]: amount `$10,980.00` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.

## NOTE
- universe: starpm
- Feasible_Surface loaded: 15 tables with enum maps
- using Fact_Ledger.json for groundedness (403 amounts, 206 emails indexed)
- counts: outcome=34, process=0
- Overall Rubric Quality: 0/34 (0%) with Major, 0/34 (0%) with Moderate+ , 0/34 (0%) with any issue
