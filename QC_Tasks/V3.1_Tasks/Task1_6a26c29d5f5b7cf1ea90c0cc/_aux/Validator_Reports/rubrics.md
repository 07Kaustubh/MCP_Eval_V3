# Validator report: rubrics

**Status:** PASS  
**Fails:** 0 · **Warns:** 5 · **Notes:** 3

## WARN
- rubric[4]: wording mismatch — title uses `approval` but prompt uses `sign-off`. Align terminology to reduce judge ambiguity.
- rubric[6]: evidence contains dates/IDs/amounts NOT in criterion: ['2026-06-15', '2026-06-16']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[19]: evidence contains dates/IDs/amounts NOT in criterion: ['BL-A49384E5FAF8']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[23]: evidence contains dates/IDs/amounts NOT in criterion: ['$220,855.43']. Evidence must not be stricter than criterion (judge grades criterion text first).
- missing-Outcome candidate: prompt uses write-verb `reject` but no Outcome rubric title contains that verb. Verify an Outcome rubric checks the corresponding write action.

## NOTE
- Fact_Ledger.json not present — falling back to raw blob substring match
- counts: outcome=32, process=0
- Overall Rubric Quality: 0/32 (0%) with Major, 0/32 (0%) with Moderate+ , 0/32 (0%) with any issue
