# Validator report: prompt

**Status:** PASS  
**Fails:** 0 · **Warns:** 2 · **Notes:** 6

## WARN
- Investigation + Action two-phase — prompt has action verbs but no clear investigation language. The richest tasks have BOTH phases. Add investigation cues (figure out / look into / find out / check / tell me where) if the task requires discovery.
- bolt-on candidate: sentence `The May timing recon I sent Daniel for sign-off on June 1 went past its deadline...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).

## NOTE
- universe: brookfield
- word count: 398
- word count 398 is over 300 — within sweet spot but could still be tightened.
- relative date: `this morning` — resolve against universe today `2026-06-12` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.
- relative date: `this week` — resolve against universe today `2026-06-12` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.
- distinct services referenced: 4
