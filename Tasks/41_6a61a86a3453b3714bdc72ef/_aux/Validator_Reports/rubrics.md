# Validator report: rubrics

**Status:** PASS  
**Fails:** 0 · **Warns:** 18 · **Notes:** 5

## WARN
- rubric[0]: evidence contains dates/IDs/amounts NOT in criterion: ['$0', '$1,832', '$13,208.75']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[0]: dollar amount `$1,832` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[1]: evidence contains dates/IDs/amounts NOT in criterion: ['$1,125', '$187.50', '$975']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[1]: dollar amount `$1,982` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[2]: evidence contains dates/IDs/amounts NOT in criterion: ['OPS-32']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[4]: evidence contains dates/IDs/amounts NOT in criterion: ['rec94e86a3007dd5e']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[5]: evidence contains dates/IDs/amounts NOT in criterion: ['rec94e86a3007dd5e', 'reca8230a8fd9ff51', 'recc83c05d889b354']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[15]: evidence contains dates/IDs/amounts NOT in criterion: ['$150', '$185', '$2,132,']. Evidence must not be stricter than criterion (judge grades criterion text first).
- rubric[15]: dollar amount `$1,832` not in Fact_Ledger amounts (verify against universe by hand)
- rubric[10] and rubric[17]: criterion text Jaccard similarity 73% — likely overlap/redundancy. Removing one may not change scoring outcomes.
- rubric[0] (X2 rubric-OE consistency): typed value `150.00` (amount) in title has no OE step referencing any `amount` value. CONSISTENCY_GAP candidate. WARN-only observation period.
- rubric[0] (X2 rubric-OE consistency): typed value `1832.00` (amount) in title has no OE step referencing any `amount` value. CONSISTENCY_GAP candidate. WARN-only observation period.
- rubric[1] (X2 rubric-OE consistency): typed value `210.00` (amount) in title has no OE step referencing any `amount` value. CONSISTENCY_GAP candidate. WARN-only observation period.
- rubric[1] (X2 rubric-OE consistency): typed value `925.00` (amount) in title has no OE step referencing any `amount` value. CONSISTENCY_GAP candidate. WARN-only observation period.
- rubric[1] (X2 rubric-OE consistency): typed value `847.00` (amount) in title has no OE step referencing any `amount` value. CONSISTENCY_GAP candidate. WARN-only observation period.
- rubric[1] (X2 rubric-OE consistency): typed value `1982.00` (amount) in title has no OE step referencing any `amount` value. CONSISTENCY_GAP candidate. WARN-only observation period.
- rubric[15] (X2 rubric-OE consistency): typed value `0.00` (amount) in title has no OE step referencing any `amount` value. CONSISTENCY_GAP candidate. WARN-only observation period.
- rubric[15] (X2 rubric-OE consistency): typed value `1832.00` (amount) in title has no OE step referencing any `amount` value. CONSISTENCY_GAP candidate. WARN-only observation period.

## NOTE
- universe: starpm
- Feasible_Surface loaded: 15 tables with enum maps
- using Fact_Ledger.json for groundedness (403 amounts, 206 emails indexed)
- counts: outcome=20, process=0
- Overall Rubric Quality: 0/20 (0%) with Major, 2/20 (10%) with Moderate+ , 2/20 (10%) with any issue
