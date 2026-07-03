# Validator report: rubrics

**Status:** PASS  
**Fails:** 0 · **Warns:** 3 · **Notes:** 5

## WARN
- missing-Outcome candidate: prompt uses write-verb `fil` but no Outcome rubric title contains that verb. Verify an Outcome rubric checks the corresponding write action.
- rubric[9] (X2 rubric-OE consistency): typed value `pam.kowalski@northwindtech.com` (email) in title differs from OE values of same type: ['blessing.okafor@moveops.com', 'catalina.dubois@moveops.com', 'chloe.vance@moveops.com']. CONSISTENCY_GAP candidate. WARN-only observation period.
- rubric[21] (X2 rubric-OE consistency): typed value `2026-04-27` (date) in title differs from OE values of same type: ['2026-04-11', '2026-04-13', '2026-04-14']. CONSISTENCY_GAP candidate. WARN-only observation period.

## NOTE
- universe: moveops
- Feasible_Surface loaded: 11 tables with enum maps
- using Fact_Ledger.json for groundedness (64 amounts, 216 emails indexed)
- counts: outcome=22, process=0
- Overall Rubric Quality: 0/22 (0%) with Major, 0/22 (0%) with Moderate+ , 0/22 (0%) with any issue
