# Validator report: prompt

**Status:** FAIL  
**Fails:** 1 · **Warns:** 2 · **Notes:** 7

## FAIL
- cross-service requirement — prompt references 1 distinct service(s) in its body. QC spec Tool-Use & Cross-Service requires investigation across 2+ services (single-service prompts can be trivially answered). Re-frame the ask to span multiple services.

## WARN
- bolt-on candidate: sentence `The Northstar planning workshop follow-up is later this month, and the partner d...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).
- bolt-on candidate: sentence `Hold off on Matthew or Ming until the ledger and the workpapers actually agree o...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).

## NOTE
- universe: brookfield
- word count: 365
- word count 365 is over 300 — within sweet spot but could still be tightened.
- relative date: `yesterday` — resolve against universe today `2026-06-12` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.
- relative date: `this morning` — resolve against universe today `2026-06-12` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.
- relative date: `this month` — resolve against universe today `2026-06-12` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.
- distinct services referenced: 1
