# Validator report: prompt

**Status:** FAIL  
**Fails:** 1 · **Warns:** 3 · **Notes:** 4

## FAIL
- cross-service requirement — prompt references 1 distinct service(s) in its body. QC spec Tool-Use & Cross-Service requires investigation across 2+ services (single-service prompts can be trivially answered). Re-frame the ask to span multiple services.

## WARN
- Investigation + Action two-phase — prompt has action verbs but no clear investigation language. The richest tasks have BOTH phases. Add investigation cues (figure out / look into / find out / check / tell me where) if the task requires discovery.
- bolt-on candidate: sentence `What is sitting wrong with me is the May trust reconciliation....` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).
- bolt-on candidate: sentence `Once you actually understand what happened, write it up as a memo to the file so...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).

## NOTE
- universe: brookfield
- word count: 364
- word count 364 is over 300 — within sweet spot but could still be tightened.
- distinct services referenced: 1
