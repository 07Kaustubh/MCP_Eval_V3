# Validator report: prompt

**Status:** PASS  
**Fails:** 0 · **Warns:** 1 · **Notes:** 6

## WARN
- bolt-on candidate: sentence `End of June was the target to have the Preventive Maintenance Push closed out....` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).

## NOTE
- universe: starpm
- word count: 313
- word count 313 is over 300 — within sweet spot but could still be tightened.
- relative date: `yesterday` — resolve against universe today `2026-07-01` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.
- relative date: `today` — resolve against universe today `2026-07-01` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.
- distinct services referenced: 2
