# Validator report: prompt

**Status:** FAIL  
**Fails:** 1 · **Warns:** 2 · **Notes:** 4

## FAIL
- cross-service requirement — prompt references 1 distinct service(s) in its body. QC spec Tool-Use & Cross-Service requires investigation across 2+ services (single-service prompts can be trivially answered). Re-frame the ask to span multiple services.

## WARN
- bolt-on candidate: sentence `Heading into the Q2 retention sweep kickoff I want to widen the scope from what ...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).
- bolt-on candidate: sentence `Anything Northstar side that affects audit's workpaper access, Julia needs to kn...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).

## NOTE
- universe: brookfield
- word count: 356
- word count 356 is over 300 — within sweet spot but could still be tightened.
- distinct services referenced: 1
