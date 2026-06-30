# Validator report: rubrics

**Status:** FAIL  
**Fails:** 1 · **Warns:** 8 · **Notes:** 4

## FAIL
- rubric[10]: rubric locks in email channel but prompt uses open-ended goal verbs (notify/reach out/let know/loop in/update). Rubric would fail an agent posting in Slack or DM instead. Re-phrase as 'The Agent notifies <recipient> ...' to allow alternative channels.

## WARN
- rubric[1]: evidence contains dates/IDs/amounts NOT in criterion: ['BL-75810CD0FEE4']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[2]: multi-value phrasing — title lists multiple values via `A, B, or C` without a canonical pattern. QC spec requires `must be one of: ...` (closed set) / `including but not limited to: ...` (open set) / `at least one of: ...` (any one). Use the explicit pattern to clarify acceptance semantics.
- rubric[6]: evidence contains dates/IDs/amounts NOT in criterion: ['FP-2026-05']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[7]: evidence contains dates/IDs/amounts NOT in criterion: ['BL-75810CD0FEE4']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[18]: evidence contains dates/IDs/amounts NOT in criterion: ['$8,781.24']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[3] and rubric[5]: criterion text Jaccard similarity 85% — likely overlap/redundancy. Removing one may not change scoring outcomes.
- missing-Outcome candidate: prompt uses write-verb `fil` but no Outcome rubric title contains that verb. Verify an Outcome rubric checks the corresponding write action.
- missing-Outcome candidate: prompt uses write-verb `schedul` but no Outcome rubric title contains that verb. Verify an Outcome rubric checks the corresponding write action.

## NOTE
- universe: brookfield
- using Fact_Ledger.json for groundedness (6461 amounts, 68 emails indexed)
- counts: outcome=20, process=0
- Overall Rubric Quality: 1/20 (5%) with Major, 3/20 (15%) with Moderate+ , 4/20 (20%) with any issue
