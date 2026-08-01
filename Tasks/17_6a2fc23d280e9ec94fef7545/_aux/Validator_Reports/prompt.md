# Validator report: prompt

**Status:** FAIL  
**Fails:** 1 · **Warns:** 1 · **Notes:** 3

## FAIL
- cross-service requirement — prompt references 1 distinct service(s) in its body. QC spec Tool-Use & Cross-Service requires investigation across 2+ services (single-service prompts can be trivially answered). Re-frame the ask to span multiple services.

## WARN
- word count 401 > 400 — prefer shorter. The 4 V3 reference prompts sit in the 300-400 sweet spot. Tighten if possible.

## NOTE
- universe: brookfield
- word count: 401
- distinct services referenced: 1
