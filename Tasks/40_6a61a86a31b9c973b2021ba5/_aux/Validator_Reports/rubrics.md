# Validator report: rubrics

**Status:** PASS  
**Fails:** 0 · **Warns:** 15 · **Notes:** 5

## WARN
- rubric[36]: evidence contains dates/IDs/amounts NOT in criterion: ['$1,850', '$310']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[42] and rubric[43]: criterion text Jaccard similarity 77% — likely overlap/redundancy. Removing one may not change scoring outcomes.
- rubric[6]: amount `$1,850` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[6]: amount `$1,850` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[10]: amount `$1,850` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[10]: amount `$1,850` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[30]: amount `$1,850` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[30]: amount `$1,850` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[41]: amount `$1,850` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[41]: amount `$1,850` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[6] (X2 rubric-OE consistency): typed value `1850.00` (amount) in title has no OE step referencing any `amount` value. CONSISTENCY_GAP candidate. WARN-only observation period.
- rubric[10] (X2 rubric-OE consistency): typed value `1850.00` (amount) in title has no OE step referencing any `amount` value. CONSISTENCY_GAP candidate. WARN-only observation period.
- rubric[30] (X2 rubric-OE consistency): typed value `1850.00` (amount) in title has no OE step referencing any `amount` value. CONSISTENCY_GAP candidate. WARN-only observation period.
- rubric[38] (X2 rubric-OE consistency): typed value `310.00` (amount) in title has no OE step referencing any `amount` value. CONSISTENCY_GAP candidate. WARN-only observation period.
- rubric[41] (X2 rubric-OE consistency): typed value `1850.00` (amount) in title has no OE step referencing any `amount` value. CONSISTENCY_GAP candidate. WARN-only observation period.

## NOTE
- universe: starpm
- Feasible_Surface loaded: 15 tables with enum maps
- using Fact_Ledger.json for groundedness (403 amounts, 206 emails indexed)
- counts: outcome=49, process=0
- Overall Rubric Quality: 0/49 (0%) with Major, 2/49 (4%) with Moderate+ , 2/49 (4%) with any issue
