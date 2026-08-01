# Validator report: prompt

**Status:** FAIL  
**Fails:** 3 · **Warns:** 0 · **Notes:** 5

## FAIL
- em-dash / en-dash at offset 525: `oll-forward anchors — the retainer book,`
- em-dash / en-dash at offset 587: `k, and the AR aging — and use those cert`
- word count 514 exceeds 500 cap

## NOTE
- universe: brookfield
- word count: 514
- relative date: `today` — resolve against universe today `2026-06-12` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.
- relative date: `next week` — resolve against universe today `2026-06-12` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.
- distinct services referenced: 5
