# Validator report: prompt

**Status:** PASS  
**Fails:** 0 · **Warns:** 2 · **Notes:** 6

## WARN
- bolt-on candidate: sentence `His 2019 Honda Civic hit that transfer hub in Indianapolis on the eleventh and h...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).
- bolt-on candidate: sentence `Update the BrightLoop engagement on our CRM so it stops reading like the April c...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).

## NOTE
- universe: moveops
- word count: 385
- word count 385 is over 300 — within sweet spot but could still be tightened.
- relative date: `tomorrow` — resolve against universe today `2026-06-12` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.
- relative date: `today` — resolve against universe today `2026-06-12` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.
- distinct services referenced: 4
