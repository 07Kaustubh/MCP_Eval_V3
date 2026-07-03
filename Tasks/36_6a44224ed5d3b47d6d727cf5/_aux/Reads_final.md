# Reads — FINAL (Task 36)

Log of QC spec / Reference cards / Eval specs consulted during the FINAL cross-artifact council phase.

## QC spec docs
- `Docs/7_QC_Spec_Doc1.json` :: full QC dimension list — Prompt (12 sub-dims), Universe (2), OE (2), Rubric (5), Trajectory (T1 at this phase). Re-applied via Final Council Lens 2 (rubric binding) + Lens 3 (cross-artifact holism).
- `Docs/8_QC_Spec_Doc2.md` :: sub-dim scoring narrative + failure examples. Consulted for FINAL's 6-lens binding.

## Eval specs (all 4)
- `Evals_moveops/1_Prompt_Eval.md` :: Prompt phase eval re-applied at integration layer (Lens 3, 4).
- `Evals_moveops/2_Oracle_Events_Eval.md` :: OE phase eval re-applied at integration layer (Lens 3, 5).
- `Evals_moveops/3_Rubrics_Eval.md` :: Rubrics phase eval re-applied at integration layer (Lens 2).
- `Evals_moveops/4_Verifier_Fails_Eval.md` :: Lens 6 simulates verifier-fails bucket classification pre-upload.

## Reference cards
- `Reference/Sessions/FINAL.md` :: runbook — 6 lenses, hard rules table, phase-readiness gate, STOP gate.
- `Reference/Council_Protocol.md` :: council instructions + B3 (density SSOT) tiered scheme.
- `Reference/Hardness_Playbook.md` :: lever preservation semantics for Lens 3 lever map.
- `Reference/Strict_Convention_Inventory.json` :: allowed verb patterns + qualifier rules for Lens 4 drift sweep.
- `Reference/OE_Convention_Inventory.json` :: OE step count + opening-verb coverage.

## Project root
- `AGENTS.md` :: universe constants (MoveOps V2.1), Airtable-vs-CRM SSOT landmine, PHMSA hazmat trap, Marcus Webb identity clash vs KeyStone universe (this task uses BrightLoop Marcus, NOT departed KeyStone Marcus).
- `Tasks/_meta/Learnings.md` :: empirical Opus 4.8 failure modes (L6 answer-leakage = 100% pass; L9 authority = ~100% fail; L25 anchor trap; L26 decoy parent).

## Per-task inputs read
- `Tasks/36_6a44224ed5d3b47d6d727cf5/5_Prompt.txt` :: full prompt.
- `Tasks/36_6a44224ed5d3b47d6d727cf5/6_Oracle_Events.txt` :: 27 OE steps.
- `Tasks/36_6a44224ed5d3b47d6d727cf5/7_Rubrics.json` :: 34 rubrics.
- `_aux/Hardness_Plan.md` :: 4 primary levers (L25/L9/L26/L2) + emergent L8; density midpoint 50 (PASS).
- `_aux/Fact_Ledger.json` :: 216 emails + 64 amounts + 155 dates + 132 personas + 9 Slack channels indexed.
- `_aux/Universe_Index/` :: service_inventory, entities_personas, key_facts, today_horizon, accounts_per_entity, graph_report.
- `_aux/Verification_s1.md`, `Verification_s2.md`, `Verification_s3.md` :: prior phase verifications.
- `_aux/Council_Reports/` :: prior council + AUDIT reports referenced.
- `_aux/Validator_Reports/prompt.md` + `oe.md` + `rubrics.md` :: current PASS status.
