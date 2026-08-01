# Validator report: prompt

**Status:** FAIL  
**Fails:** 1 · **Warns:** 2 · **Notes:** 4

## FAIL
- cross-service requirement — prompt references 1 distinct service(s) in its body. QC spec Tool-Use & Cross-Service requires investigation across 2+ services (single-service prompts can be trivially answered). Re-frame the ask to span multiple services.

## WARN
- Investigation + Action two-phase — prompt has action verbs but no clear investigation language. The richest tasks have BOTH phases. Add investigation cues (figure out / look into / find out / check / tell me where) if the task requires discovery.
- bolt-on candidate: sentence `Once the real state is confirmed, file the close-out record in the vault, send t...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).

## NOTE
- universe: brookfield
- word count: 379
- word count 379 is over 300 — within sweet spot but could still be tightened.
- distinct services referenced: 1
