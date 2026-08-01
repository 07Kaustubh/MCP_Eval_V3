# S2 — Oracle Events TODOs (Task 45)

Runbook: Reference/Sessions/S2.md. One in_progress at a time. Mark completed immediately.

- [x] T1  Read required inputs: 5_Prompt.txt, Universe_Split, Universe_Index, Hardness_Plan, OE_Format card, Docs_starpm/9_Common_Error.md, tool catalog (7_Server_Tools_Details.json), OE_Convention_Inventory, Council_Protocol
- [x] T2  Decompose prompt sentence-by-sentence: every explicit ask + every implicit ask -> discovery steps + write actions
- [x] T3  Verify each step against per-task universe (records exist in Universe_Split) + tool catalog (tool names + param names, StarPM traps) + verify_universe_atoms.py (0 fails, 1 benign warn = intentional 7/15 future event)
- [x] T4  Draft 6_Oracle_Events.txt (15 OEs, sequential, no em-dashes, concrete expected values)
- [x] T5  Validator PASS (0 fails, 0 warns, 3 notes) -> _aux/Validator_Reports/oe.md
- [x] T6  Council A (grounding) GO (round 0 + REVISE round 1 re-verify GO) -> S2_A_grounding.md
- [x] T7  Council B (adversarial QC) GO (round 0 bg_4ef2f366 + REVISE round 1 fresh bg_8a5579aa) -> S2_B_adversarial.md; OE Completeness 5/5, OE Accuracy 5/5
- [x] T8  REVISE round 1: OE6 vendor-sweep fix applied in place; re-ran validator (PASS) + Council A (GO) + Council B (GO) + AUDIT (PASS STRICT) clean
- [x] T9  AUDIT --phase oe: round 0 REVISE (PROPAGATE-TO-S1) -> adjudicated S2-locus (rule 19) -> OE6 fix -> round 1 PASS (STRICT) -> AUDIT_oe.md
- [x] T10 Wrote _aux/Verification_s2.md (cross-source check, all statements checked) + _aux/Reads_s2.md (reads log)
- [x] T11 _aux/Reasoning/OE_solvability.md: OE-to-prompt coverage map + OE-to-rubric preview + council/AUDIT verdicts + consolidated S3 carry-forwards
- [x] T12 STOP gate: end response, print next trigger (PIPELINE S3)
