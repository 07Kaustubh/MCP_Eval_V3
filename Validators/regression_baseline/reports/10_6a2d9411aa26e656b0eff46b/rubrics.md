# Validator report: rubrics

**Status:** FAIL  
**Fails:** 1 · **Warns:** 3 · **Notes:** 4

## FAIL
- rubric[14]: forbidden vague connector `e.g., F` in title — QC spec explicitly forbids `such as` / `for example` / `e.g.` / `like` when defining what counts as correct. Use one of the canonical patterns instead: `must be one of: A, B, or C` (closed set) / `including but not limited to: A, B` (open set) / `at least one of: A, B, or C` (any one).

## WARN
- rubric[8]: evidence contains dates/IDs/amounts NOT in criterion: ['2026-08-04']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[9]: evidence contains dates/IDs/amounts NOT in criterion: ['2026-08-04']. Evidence must not be stricter than criterion (judge grades criterion text first).
- missing-Outcome candidate: prompt uses write-verb `fil` but no Outcome rubric title contains that verb. Verify an Outcome rubric checks the corresponding write action.

## NOTE
- universe: brookfield
- Fact_Ledger.json not present — falling back to raw blob substring match
- counts: outcome=15, process=0
- Overall Rubric Quality: 0/15 (0%) with Major, 1/15 (7%) with Moderate+ , 1/15 (7%) with any issue
