# Validator report: rubrics

**Status:** PASS  
**Fails:** 0 · **Warns:** 3 · **Notes:** 5

## WARN
- rubric[17]: dollar amount `$16,800` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[19]: evidence contains dates/IDs/amounts NOT in criterion: ['$7,760']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[8] and rubric[19]: criterion text Jaccard similarity 75% — likely overlap/redundancy. Removing one may not change scoring outcomes.

## NOTE
- universe: starpm
- Feasible_Surface loaded: 15 tables with enum maps
- using Fact_Ledger.json for groundedness (403 amounts, 208 emails indexed)
- counts: outcome=24, process=0
- Overall Rubric Quality: 0/24 (0%) with Major, 2/24 (8%) with Moderate+ , 2/24 (8%) with any issue
