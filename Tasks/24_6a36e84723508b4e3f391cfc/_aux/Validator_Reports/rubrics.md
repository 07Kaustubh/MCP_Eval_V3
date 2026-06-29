# Validator report: rubrics

**Status:** FAIL  
**Fails:** 3 · **Warns:** 8 · **Notes:** 5

## FAIL
- rubric[6]: forbidden vague connector `for example V` in title — QC spec explicitly forbids `such as` / `for example` / `e.g.` / `like` when defining what counts as correct. Use one of the canonical patterns instead: `must be one of: A, B, or C` (closed set) / `including but not limited to: A, B` (open set) / `at least one of: A, B, or C` (any one).
- rubric[17]: forbidden vague connector `for example C` in title — QC spec explicitly forbids `such as` / `for example` / `e.g.` / `like` when defining what counts as correct. Use one of the canonical patterns instead: `must be one of: A, B, or C` (closed set) / `including but not limited to: A, B` (open set) / `at least one of: A, B, or C` (any one).
- rubric[21]: title bundles two independent actions via AND — split into atomic rubrics. (`The Agent reports that the departed-approver routing fix did not land, because i...`)

## WARN
- rubric[1]: evidence contains dates/IDs/amounts NOT in criterion: ['VEN-012-753165']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[15]: evidence contains dates/IDs/amounts NOT in criterion: ['VEN-010-693199']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[16]: account 193120 mentioned near entity `brookfield` but not present in Fact_Ledger.accounts_by_entity for brookfield. Account-number entity-trap: 105000 differs per entity (Cash-Trust on Brookfield, IOLTA on Northstar, Short-term Investments on Acme). Verify per-entity assignment.
- missing-Outcome candidate: prompt uses write-verb `draft` but no Outcome rubric title contains that verb. Verify an Outcome rubric checks the corresponding write action.
- rubric[12]: amount `$460,556.46` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[13]: amount `$289,217.86` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[15]: amount `$24,475.25` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[16]: amount `$1,040.63` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.

## NOTE
- universe: brookfield
- Feasible_Surface loaded: 19 tables with enum maps
- using Fact_Ledger.json for groundedness (6461 amounts, 68 emails indexed)
- counts: outcome=24, process=0
- Overall Rubric Quality: 1/24 (4%) with Major, 3/24 (12%) with Moderate+ , 3/24 (12%) with any issue
