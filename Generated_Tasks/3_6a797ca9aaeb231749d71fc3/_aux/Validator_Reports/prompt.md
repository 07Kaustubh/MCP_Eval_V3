# Validator report: prompt

**Status:** PASS  
**Fails:** 0 · **Warns:** 3 · **Notes:** 4

## WARN
- word count 430 > 400 — prefer shorter. The 4 V3 reference prompts sit in the 300-400 sweet spot. Tighten if possible.
- bolt-on candidate: sentence `Walk the pull-request history since December, both merged and unmerged, and figu...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).
- bolt-on candidate: sentence `Once the picture is straight, put a reconciliation comment on the ART tracking t...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).

## NOTE
- universe: harmonygames
- word count: 430
- distinct services referenced: 3
- persona ACL active: 7 scoped service(s) (gmail, gcal, gdrive, gdocs, gsheets, gslides, slack); validate every required read from the assigned persona's view, not Universe Explorer god-mode
