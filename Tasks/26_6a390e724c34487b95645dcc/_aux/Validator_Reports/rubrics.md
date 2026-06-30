# Validator report: rubrics

**Status:** PASS  
**Fails:** 0 · **Warns:** 15 · **Notes:** 4

## WARN
- rubric[0]: dollar amount `$4,820.30` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[0]: dollar amount `$4,820.30` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[3]: dollar amount `$4,820.30` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[6]: dollar amount `$4,820.30` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[10]: wording mismatch — title uses `approval` but prompt uses `sign-off`. Align terminology to reduce judge ambiguity.
- rubric[10]: evidence contains dates/IDs/amounts NOT in criterion: ['$9.61']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[11]: wording mismatch — title uses `approval` but prompt uses `sign-off`. Align terminology to reduce judge ambiguity.
- rubric[16]: pins Slack channel_id `C006` without channel name (#name) — agent passing the name would wrongly fail this rubric. Accept either form.
- rubric[16]: evidence contains dates/IDs/amounts NOT in criterion: ['FP-2025-12']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[16]: dollar amount `$4,820.30` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[17]: pins Slack channel_id `C006` without channel name (#name) — agent passing the name would wrongly fail this rubric. Accept either form.
- rubric[18]: dollar amount `$4,820.30` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[21]: wording mismatch — title uses `approval` but prompt uses `sign-off`. Align terminology to reduce judge ambiguity.
- rubric[12]: amount `$647.97` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.
- rubric[19] (X2 rubric-OE consistency): typed value `2026-01-05` (date) in title differs from OE values of same type: ['2026-06-08']. CONSISTENCY_GAP candidate. WARN-only observation period.

## NOTE
- universe: brookfield
- using Fact_Ledger.json for groundedness (6461 amounts, 68 emails indexed)
- counts: outcome=23, process=0
- Overall Rubric Quality: 0/23 (0%) with Major, 0/23 (0%) with Moderate+ , 0/23 (0%) with any issue
