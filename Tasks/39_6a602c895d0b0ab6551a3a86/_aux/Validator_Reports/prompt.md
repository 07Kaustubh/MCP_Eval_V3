# Validator report: prompt

**Status:** PASS  
**Fails:** 0 · **Warns:** 3 · **Notes:** 7

## WARN
- bolt-on candidate: sentence `Got the QC pass posted for Las Vistas 3C back on the 18th but never wrapped the ...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).
- bolt-on candidate: sentence `Post in the #make-ready channel that the formal close is done and 3C is live for...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).
- bolt-on candidate: sentence `Check the calendar for any 3C showings booked between now and next Wednesday, an...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).

## NOTE
- universe: starpm
- word count: 356
- word count 356 is over 300 — within sweet spot but could still be tightened.
- relative date: `today` — resolve against universe today `2026-06-12` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.
- relative date: `today` — resolve against universe today `2026-06-12` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.
- relative date: `next Wednesday` — resolve against universe today `2026-06-12` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.
- distinct services referenced: 2
