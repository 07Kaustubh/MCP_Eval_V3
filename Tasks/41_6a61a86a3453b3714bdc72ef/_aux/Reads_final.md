# Reads — PIPELINE FINAL — Tasks/41_6a61a86a3453b3714bdc72ef

QC spec docs / Eval specs / Reference cards consulted this phase (v11 E2 compliance log).

- Reference/Sessions/FINAL.md :: FINAL runbook — 6-lens cross-artifact council + StarPM V4 injection + submission_gate extra gates + answer-leakage hard rule.
- AGENTS.md (PIPELINE DISPATCH + density-framework §11 + auto-AUDIT §12 + Universe routing §248) :: FINAL is required pre-upload; StarPM density = 40+ avg per-model (NOT the Brookfield 50/40 scheme).
- Docs_starpm/7_QC_Spec_Doc1.json :: StarPM QC dimension/sub-dimension scoring surface (Prompt/Universe/OE/Rubric) — routed to Final Council.
- Docs_starpm/8_QC_Spec_Doc2.md :: StarPM QC narrative spec — routed to Final Council.
- Evals_starpm/0 (injection) :: 7 hard gates (schema, ID format, date window 2026-05-01..2026-07-01, cross-service integrity, naturalness, reachability, pre-solve). Gate PASS; P4/P5/P6/P8 are COUNCIL semantic judgments.
- Evals_starpm/5 (submission_gate) :: defect families F1-F6; single deterministic defect = FAIL. Gate PASS (0 fails); rubric#2 atomicity WARN + 6.3/6.6/6.8/6.9/6.10/6.11 = COUNCIL review.
- Tasks/_meta/Learnings.md :: Opus 4.8 / Gemini empirical failure modes (L6 stated-answer=100%-pass; L13/L10/L26 latching+supersession; L22 net-vs-gross sign; L31 Gemini negative-directive omission).
- _aux/Hardness_Plan.md :: 5 selected levers (L2 flagship / L10 / L1 / L11 / L31) + 5 stump predictions + per-model density (~50 Opus / ~43 Gemini).
- _aux/Verification_s1.md / s2.md / s3.md :: prior-phase cross-source checks cross-referenced at integration layer.
- _aux/Fact_Ledger.json :: atom surface for tight-identifier grounding + derived-figure recomputation.
