# Validator report: prompt

**Status:** PASS  
**Fails:** 0 · **Warns:** 3 · **Notes:** 3

## WARN
- Investigation + Action two-phase — prompt has action verbs but no clear investigation language. The richest tasks have BOTH phases. Add investigation cues (figure out / look into / find out / check / tell me where) if the task requires discovery.
- bolt-on candidate: sentence `Treat this as partner clearance only: do not rebook the entry, rebuild the liabi...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).
- bolt-on candidate: sentence `Tell me which jurisdictions belong in Q1, which expense and payable accounts car...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).

## NOTE
- universe: brookfield
- word count: 225
- distinct services referenced: 2
