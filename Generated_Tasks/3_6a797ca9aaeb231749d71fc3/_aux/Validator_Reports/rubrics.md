# Validator report: rubrics

**Status:** PASS  
**Fails:** 0 · **Warns:** 12 · **Notes:** 6

## WARN
- rubric[1]: evidence contains dates/IDs/amounts NOT in criterion: ['ART-252', 'ART-770']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[2]: evidence contains dates/IDs/amounts NOT in criterion: ['ART-252', 'ART-770']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[3]: evidence contains dates/IDs/amounts NOT in criterion: ['ART-252', 'ART-770']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[4]: evidence contains dates/IDs/amounts NOT in criterion: ['ART-252', 'ART-770']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[5]: evidence contains dates/IDs/amounts NOT in criterion: ['ART-252', 'ART-770']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[16]: evidence contains dates/IDs/amounts NOT in criterion: ['2025-12-21', '2026-02-11']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[4] and rubric[25]: criterion text Jaccard similarity 70% — likely overlap/redundancy. Removing one may not change scoring outcomes.
- rubric[5] and rubric[27]: criterion text Jaccard similarity 75% — likely overlap/redundancy. Removing one may not change scoring outcomes.
- missing-Outcome candidate: prompt uses write-verb `draft` but no Outcome rubric title contains that verb. Verify an Outcome rubric checks the corresponding write action.
- missing-Outcome candidate: prompt uses write-verb `email` but no Outcome rubric title contains that verb. Verify an Outcome rubric checks the corresponding write action.
- missing-Outcome candidate: prompt uses write-verb `reply` but no Outcome rubric title contains that verb. Verify an Outcome rubric checks the corresponding write action.
- missing-Outcome candidate: prompt uses write-verb `updat` but no Outcome rubric title contains that verb. Verify an Outcome rubric checks the corresponding write action.

## NOTE
- universe: harmonygames
- Feasible_Surface loaded: 13 tables with enum maps
- using Fact_Ledger.json for groundedness (41 amounts, 47 emails indexed)
- counts: outcome=28, process=0
- sub-categories: Outcome 1.1=6, Outcome 1.2=17, Outcome 2.1=5
- Overall Rubric Quality: 0/28 (0%) with Major, 4/28 (14%) with Moderate+ , 4/28 (14%) with any issue
