# Validator report: rubrics

**Status:** FAIL  
**Fails:** 2 · **Warns:** 13 · **Notes:** 4

## FAIL
- Overall Rubric Quality FAIL — 27% of rubrics have Moderate-or-Major issues (QC spec band: >15% = FAIL). Cap is 15%.
- Overall Rubric Quality FAIL — 27% of rubrics have any-severity issues (QC spec band: >20% = FAIL). Cap is 20%.

## WARN
- rubric[0] and rubric[2]: criterion text Jaccard similarity 71% — likely overlap/redundancy. Removing one may not change scoring outcomes.
- rubric[0] and rubric[10]: criterion text Jaccard similarity 71% — likely overlap/redundancy. Removing one may not change scoring outcomes.
- rubric[0] and rubric[14]: criterion text Jaccard similarity 71% — likely overlap/redundancy. Removing one may not change scoring outcomes.
- rubric[2] and rubric[10]: criterion text Jaccard similarity 71% — likely overlap/redundancy. Removing one may not change scoring outcomes.
- rubric[2] and rubric[14]: criterion text Jaccard similarity 71% — likely overlap/redundancy. Removing one may not change scoring outcomes.
- rubric[4] and rubric[6]: criterion text Jaccard similarity 71% — likely overlap/redundancy. Removing one may not change scoring outcomes.
- rubric[4] and rubric[8]: criterion text Jaccard similarity 71% — likely overlap/redundancy. Removing one may not change scoring outcomes.
- rubric[4] and rubric[12]: criterion text Jaccard similarity 71% — likely overlap/redundancy. Removing one may not change scoring outcomes.
- rubric[6] and rubric[8]: criterion text Jaccard similarity 71% — likely overlap/redundancy. Removing one may not change scoring outcomes.
- rubric[6] and rubric[12]: criterion text Jaccard similarity 71% — likely overlap/redundancy. Removing one may not change scoring outcomes.
- rubric[8] and rubric[12]: criterion text Jaccard similarity 71% — likely overlap/redundancy. Removing one may not change scoring outcomes.
- rubric[10] and rubric[14]: criterion text Jaccard similarity 71% — likely overlap/redundancy. Removing one may not change scoring outcomes.
- missing-Outcome candidate: prompt uses write-verb `email` but no Outcome rubric title contains that verb. Verify an Outcome rubric checks the corresponding write action.

## NOTE
- universe: keystone
- using Fact_Ledger.json for groundedness (4446 amounts, 1923 emails indexed)
- counts: outcome=30, process=0
- Overall Rubric Quality: 0/30 (0%) with Major, 8/30 (27%) with Moderate+ , 8/30 (27%) with any issue
