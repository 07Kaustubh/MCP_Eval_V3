# Validator report: rubrics

**Status:** PASS  
**Fails:** 0 · **Warns:** 7 · **Notes:** 4

## WARN
- rubric[0]: evidence contains dates/IDs/amounts NOT in criterion: ['$340']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[2]: wording mismatch — title uses `approval` but prompt uses `sign-off`. Align terminology to reduce judge ambiguity.
- rubric[6]: evidence neither references an OE step (Per OE<n> / See OE<n> / OE<n>) nor uses trajectory-anchoring phrasing (Look for / Check the / Verify that / Inspect / Confirm / payload / final response). Add an explicit anchoring so the judge knows where to grade from.
- rubric[7]: multi-value phrasing — title lists multiple values via `A, B, or C` without a canonical pattern. QC spec requires `must be one of: ...` (closed set) / `including but not limited to: ...` (open set) / `at least one of: ...` (any one). Use the explicit pattern to clarify acceptance semantics.
- rubric[8]: evidence neither references an OE step (Per OE<n> / See OE<n> / OE<n>) nor uses trajectory-anchoring phrasing (Look for / Check the / Verify that / Inspect / Confirm / payload / final response). Add an explicit anchoring so the judge knows where to grade from.
- rubric[9]: evidence contains dates/IDs/amounts NOT in criterion: ['$340']. Evidence must not be stricter than criterion (judge grades criterion text first).
- missing-Outcome candidate: prompt uses write-verb `fil` but no Outcome rubric title contains that verb. Verify an Outcome rubric checks the corresponding write action.

## NOTE
- universe: brookfield
- using Fact_Ledger.json for groundedness (6461 amounts, 68 emails indexed)
- counts: outcome=10, process=1
- Overall Rubric Quality: 0/11 (0%) with Major, 0/11 (0%) with Moderate+ , 1/11 (9%) with any issue
