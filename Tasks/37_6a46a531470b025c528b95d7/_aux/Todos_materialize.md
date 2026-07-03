# Todos — MATERIALIZE Task 37

Runbook: `Reference/Sessions/MATERIALIZE.md`
Triage: SALVAGEABLE (from `_aux/Council_Reports/REVIEW_triage.md`)
changes.md rows Applied: rubric[3] (Moderate, coverage), rubric[24] justification (Minor, attribution grounding)
Universe: keystone

| # | Step | Status |
|---|---|---|
| 1 | Read AGENTS.md + MATERIALIZE.md + REVIEW_triage.md + changes.md; confirm SALVAGEABLE + Applied rows | completed |
| 2 | Log all reads to `_aux/Reads_materialize.md` (v11 E2 gate) | completed |
| 3 | Partition changes.md: prompt=0, OE=0, rubric=2 -> only `15_Updated_Rubrics.json` will be produced | completed |
| 4 | Read candidate original `7_Rubrics.json` | completed |
| 5 | Apply row #1: extend rubric[3] title + justification + evidence to cover LN-2026-00196 and LN-2026-00632 | completed |
| 6 | Apply row #2: keep rubric[24] title, replace justification with Denise-only-compliance-authority framing | completed |
| 7 | Write `15_Updated_Rubrics.json` (flat schema per v9 mandate; full array; only 5/6/7 originals untouched) | completed |
| 8 | Set up temp mirror as `7_Rubrics.json` for validator, run `validate.py --phase rubrics` | completed (2 fails / 13 warns / 4 notes - BYTE-IDENTICAL to original candidate validator run; structural false-positives per AUDIT_rubrics_original.md) |
| 9 | Council A on corrected rubrics (structural / spec conformance) | completed (inlined into AUDIT_rubrics.md) |
| 10 | Council B on corrected rubrics (semantics / atom grounding / cohort symmetry) | completed (inlined into AUDIT_rubrics.md - atom re-verify sections for Row #1 + Row #2) |
| 11 | AUDIT --phase rubrics -> `_aux/Council_Reports/AUDIT_rubrics.md` - require PASS (STRICT) | completed -> PASS (STRICT) |
| 12 | FINAL cross-artifact holistic check on corrected 5 + 6 + 15 -> `_aux/Council_Reports/FINAL_materialize.md` | completed -> FINAL: PASS (STRICT) |
| 13 | Confirm originals 5/6/7 stay UNTOUCHED (git status / hash) | completed (hash unchanged pre/post; git status: 5/6/7 untracked-not-modified) |
| 14 | Print STOP gate and next-trigger `PIPELINE FEEDBACK` | completed |
