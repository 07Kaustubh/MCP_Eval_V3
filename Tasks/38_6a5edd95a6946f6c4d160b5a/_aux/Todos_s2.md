# Todos_s2.md -- Oracle Events Phase (S2)

## Task: 38_6a5edd95a6946f6c4d160b5a

- [x] Run phase_ready gate (python3 Validators/phase_ready.py --phase s2 --task Tasks/38_6a5edd95a6946f6c4d160b5a)
- [x] Read Reference/Sessions/S2.md (runbook)
- [x] Read Reference/OE_Format.md (format card)
- [x] Read Evals_starpm/2_OE_Eval.md (OE eval spec)
- [x] Read Docs_starpm/7_QC_Spec_Doc1.json (OE Completeness + OE Accuracy definitions)
- [x] Read StarPM_Base_Universe/7_Server_Tools_Details.json (exact tool names + parameters)
- [x] Read QC_Tasks/V4_Tasks/QC_Passed/Task1_6a26c29d5f5b7cf1ea90c0cc/6_Oracle_Events.txt (reference voice)
- [x] Verify all per-task universe data (airtable records, gmail threads, slack messages, QB entities, contacts)
- [x] Confirm Aurora Winona email (aurora.winona@starpm.com)
- [x] Confirm Tony Reyes email (tony.reyes@starpm.com)
- [x] Create _aux/Todos_s2.md (this file)
- [x] Create _aux/Reads_s2.md
- [x] Draft 6_Oracle_Events.txt (31 OEs, lower=34, strict midpoint=41.5, THIN_DENSITY)
- [x] Run validator: python3 Validators/validate.py --phase oe --task Tasks/38_6a5edd95a6946f6c4d160b5a
- [x] Fix any validator issues and re-run until clean exit 0
- [x] Spawn Council A (grounding sweep) sub-agent -> _aux/Council_Reports/S2_A_grounding.md (R1 BLOCK -> R2 GO)
- [x] Spawn Council B (adversarial QC) sub-agent -> _aux/Council_Reports/S2_B_adversarial.md (R1 GO THIN -> R2 GO THIN)
- [x] Iterate on OE per council feedback until both GO (2 rounds)
- [x] AUDIT auto-fire (oracle sub-agent, --phase oe) -> _aux/Council_Reports/AUDIT_oe.md (R1 REVISE -> R2 PASS STRICT)
- [x] Write _aux/Verification_s2.md (cross-source check)
- [x] Append to _aux/Reasoning/OE_solvability.md
- [ ] STOP -- wait for user to invoke PIPELINE S3
