# Validator report: prompt

**Status:** PASS  
**Fails:** 0 · **Warns:** 3 · **Notes:** 6

## WARN
- bolt-on candidate: sentence `Check what's been going on with each of these loans, look at any recent email th...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).
- bolt-on candidate: sentence `Reach out to Carlos, Derek, Keisha, and any other LO with active files in my que...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).
- bolt-on candidate: sentence `If anything you find looks like it could be a compliance concern, flag it separa...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).

## NOTE
- universe: keystone
- word count: 343
- word count 343 is over 300 — within sweet spot but could still be tightened.
- relative date: `today` — resolve against universe today `2026-06-12` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.
- relative date: `this morning` — resolve against universe today `2026-06-12` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.
- distinct services referenced: 2
