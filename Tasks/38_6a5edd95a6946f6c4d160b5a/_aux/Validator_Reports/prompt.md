# Validator report: prompt

**Status:** PASS  
**Fails:** 0 · **Warns:** 2 · **Notes:** 3

## WARN
- bolt-on candidate: sentence `Tony told me on Slack it's probably a clogged filter and he'd get someone in Thu...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).
- bolt-on candidate: sentence `I've been working off the "$8,400 approved scope" from the back-and-forth with R...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).

## NOTE
- universe: starpm
- word count: 217
- distinct services referenced: 2
