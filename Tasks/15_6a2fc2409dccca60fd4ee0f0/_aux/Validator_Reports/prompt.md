# Validator report: prompt

**Status:** FAIL  
**Fails:** 1 · **Warns:** 2 · **Notes:** 5

## FAIL
- cross-service requirement — prompt references 1 distinct service(s) in its body. QC spec Tool-Use & Cross-Service requires investigation across 2+ services (single-service prompts can be trivially answered). Re-frame the ask to span multiple services.

## WARN
- word count 402 > 400 — prefer shorter. The 4 V3 reference prompts sit in the 300-400 sweet spot. Tighten if possible.
- Investigation + Action two-phase — prompt has action verbs but no clear investigation language. The richest tasks have BOTH phases. Add investigation cues (figure out / look into / find out / check / tell me where) if the task requires discovery.

## NOTE
- universe: brookfield
- word count: 402
- relative date: `this week` — resolve against universe today `2026-06-12` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.
- relative date: `next week` — resolve against universe today `2026-06-12` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.
- distinct services referenced: 1
