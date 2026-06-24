# AUDIT — Rubrics (strictest possible interpretation)

**Phase:** rubrics
**Mode:** auto-fired on the corrected materialization (`15_Updated_Rubrics.json` = current `7_Rubrics.json` post prior-iteration apply).
**Interpretation rule:** every "should" read as "must". 5/5 only. Zero Major / zero Moderate / zero Minor wording. Any "at least N", "appropriate", "enough", "professional", "thorough" in criterion text = REVISE.

## Strict checks

| # | Check | Result |
|---|---|---|
| 1 | Total rubric count | 11 — PASS |
| 2 | Category balance: Outcome >= Process | 10 Outcome + 1 Process — PASS |
| 3 | Every criterion begins `The Agent` | All 11 — PASS |
| 4 | Zero tool names in criterion `title` field | 0 — PASS |
| 5 | Zero "at least N", "or more", "at minimum", "at a minimum" in criterion text | 0 — PASS |
| 6 | Zero V3-banned subjective words in criterion `title` (`enough`, `sufficient`, `appropriate`, `professional`, `thorough`, `helpful`, `comprehensive`, `reasonable`, `adequate`, `properly`, `correctly`, `accurately`) | 0 in titles. ("appropriate classification" appears in R7 evidence — universe-truth phrasing for the Records Vault classification field, not a grading qualifier — acceptable.) PASS |
| 7 | Zero em-dashes (U+2014, U+2013) in titles, evidence, or justification | 0 — PASS |
| 8 | Zero typos / verb-form errors | 0 — PASS |
| 9 | Every rubric is self-contained (no out-of-rubric context required to grade) | YES — every JE id, doc id, account number, period id, and stakeholder email embedded inline. PASS |
| 10 | Every rubric is atomic (no independent-action bundling) | YES — R1 / R7 / R9 / R10 bundle attributes of one artifact / action; V3-permitted. PASS |
| 11 | Process rubric R11 passes three-condition test | YES — see REVIEW_rubrics.md Perspective 3. PASS |
| 12 | Every Outcome rubric is uniquely verifiable in the per-task universe | YES — verified in REVIEW_final.md Lens 3. PASS |
| 13 | Process rubric count <= 30% of total | 1 / 11 = 9.1% — PASS |
| 14 | Evidence field describes how a grader verifies (specific tool calls or response checks) | YES on all 11 — PASS |
| 15 | Justification field explains why the criterion matters | YES on all 11 — PASS |

## Verdict: PASS (STRICT)

No edits required.
