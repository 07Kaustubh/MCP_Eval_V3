# AUDIT — Prompt (strictest possible interpretation)

**Phase:** prompt
**Mode:** auto-fired on the corrected materialization (`_aux/REVIEW_prompt_draft.txt` = current `5_Prompt.txt` post prior-iteration apply).
**Interpretation rule:** every "should" read as "must". Density bar 50+. 5/5 only.

## Strict checks

| # | Check | Result |
|---|---|---|
| 1 | Prompt under 500 words | 251 — PASS |
| 2 | Zero em-dashes (U+2014, U+2013) | 0 — PASS |
| 3 | Zero "at least N" without explicit prompt minimum | 0 — PASS |
| 4 | Zero tool names | 0 — PASS |
| 5 | Persona-voice continuity from `2_Persona_Briefs.md` Matthew Li entry | "highly formal, calm, commercially aware" — matches | PASS |
| 6 | Premise truth-checked against universe | "Andrea is wrapping up her certification" matches `2_Persona_Briefs.md` Andrea Phil (certifies Acme monthly close incl. scen_028 May) | PASS |
| 7 | No leakage of JE id, doc id, account number, dollar amount, or stakeholder email | 0 — PASS |
| 8 | Single-assumption cap | One assumption (which item is contested) resolved by investigation | PASS |
| 9 | Investigation drives action (not advisory-only) | "If you believe something needs to change before sign-off, explain why and identify what still requires attention" + "make sure the rationale is documented clearly" + "the relevant stakeholders have a consistent understanding" — three mandate verbs | PASS |
| 10 | Coherence — investigation feeds recommendation feeds documentation feeds communication | Each prompt clause drives toward the next | PASS |
| 11 | Anti-pattern: pre-solving the answer | None | PASS |
| 12 | Anti-pattern: contrived setup | None — partner peer-review pre-finalization is a real CPA workflow | PASS |
| 13 | Persona / business-function tight fit | Matthew Li (AS Partner) + Accounting Operations (Cat 1) — clean fit | PASS |
| 14 | Today-alignment (universe today = 2026-06-12; Acme FP-2026-05 open) | Aligned | PASS |
| 15 | Universe data exists for the implied investigation path | Verified across Oracle GL, SAP Subledger, BlackLine, Records Vault, Email, Slack, Messaging | PASS |

## Verdict: PASS (STRICT)

No edits required.
