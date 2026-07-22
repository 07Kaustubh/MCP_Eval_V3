# HARDNESS reference-doc reads — Tasks/38_6a5edd954557325b498168d1

- Reference/Sessions/HARDNESS.md :: HARDNESS runbook - phase-readiness gate, 6-section Hardness_Plan template, tiered density gate (>=50 PASS / 40-49 THIN / <40 STOP), INSUFFICIENT_LEVERS (<3) gate, service-breadth gate (v11 G1)
- Validators/phase_ready.py :: phase gate - hardness requires Universe_Split + Universe_Index + Fact_Ledger; validates upstream Verification_s0.md via check_verification.py
- Validators/check_verification.py :: Verification_<phase>.md schema - Sources consulted (Per-task data/Eval spec/QC spec) + Verification statements + Discrepancies surfaced + Verdict (PASS/REVISE/BLOCK)
- Tasks/_meta/Learnings.md :: (reading) empirical Opus 4.8 failure-mode evidence - L1-L7 do-not-reliably-fail block, L8-L14 reliably-fails block; every selected lever must cite an L-entry
- Reference/Hardness_Playbook.md :: (reading) 11-lever catalog with per-lever tool-call cost ranges
- _aux/Universe_Index/graph_report.md :: (reading) per-task density map for lever selection
- _aux/Universe_Index/key_facts.md :: (reading) counts + state distributions
- _aux/Universe_Index/service_inventory.md :: (reading) record counts per service
- _aux/Universe_Index/entities_personas.md :: (reading) personas + NPCs + contacts
- _aux/Universe_Index/today_horizon.json :: (reading) universe today + records_dated_after_today
- _aux/Feasible_Surface.json :: (reading) StarPM S0-computed feasible action surface
