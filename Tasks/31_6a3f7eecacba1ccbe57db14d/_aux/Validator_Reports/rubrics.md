# Validator report: rubrics

**Status:** FAIL  
**Fails:** 1 · **Warns:** 18 · **Notes:** 3

## FAIL
- rubric[8]: forbidden vague connector `such as S` in title — QC spec explicitly forbids `such as` / `for example` / `e.g.` / `like` when defining what counts as correct. Use one of the canonical patterns instead: `must be one of: A, B, or C` (closed set) / `including but not limited to: A, B` (open set) / `at least one of: A, B, or C` (any one).

## WARN
- rubric[0]: evidence contains dates/IDs/amounts NOT in criterion: ['$10,382.73', '$139,441.10', '$166,816.16']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[0]: dollar amount `$131,135.84` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[0]: dollar amount `$156,433.43` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[0]: dollar amount `$4,820.30` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[0]: dollar amount `$24,150.54` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[0]: dollar amount `$115,290.56` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[1]: evidence contains dates/IDs/amounts NOT in criterion: ['$27,375.06', '2025-07-01', '2025-12-31']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[1]: dollar amount `$139,441.10` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[1]: dollar amount `$228,024.70` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[2]: evidence contains dates/IDs/amounts NOT in criterion: ['FP-2025-07', 'FP-2025-12']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[2]: dollar amount `$8,305.26` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[2]: dollar amount `$10,382.73` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[2]: dollar amount `$24,150.54` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[2]: dollar amount `$115,290.56` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[3]: evidence neither references an OE step (Per OE<n> / See OE<n> / OE<n>) nor uses trajectory-anchoring phrasing (Look for / Check the / Verify that / Inspect / Confirm / payload / final response). Add an explicit anchoring so the judge knows where to grade from.
- rubric[4]: dollar amount `$4,820.30` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[4]: dollar amount `$4,820.30` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[10]: evidence contains dates/IDs/amounts NOT in criterion: ['$131,135.84', '$156,433.43', '$4,820.30']. Evidence must not be stricter than criterion (judge grades criterion text first).

## NOTE
- using Fact_Ledger.json for groundedness (6461 amounts, 68 emails indexed)
- counts: outcome=13, process=0
- Overall Rubric Quality: 0/13 (0%) with Major, 1/13 (8%) with Moderate+ , 1/13 (8%) with any issue
