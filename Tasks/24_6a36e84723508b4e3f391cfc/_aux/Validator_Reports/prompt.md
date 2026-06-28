# Validator report: prompt

**Status:** PASS  
**Fails:** 0 · **Warns:** 2 · **Notes:** 3

## WARN
- word count 473 > 400 — prefer shorter. The 4 V3 reference prompts sit in the 300-400 sweet spot. Tighten if possible.
- bolt-on candidate: sentence `Vendors have been calling me since Monday about outstanding payments, at least t...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).

## NOTE
- universe: brookfield
- word count: 473
- distinct services referenced: 3
