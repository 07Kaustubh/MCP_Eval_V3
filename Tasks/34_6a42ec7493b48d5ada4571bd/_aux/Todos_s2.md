# Todos — S2 (Oracle Events drafting)

- [x] Read S2 runbook + format card + AGENTS.md (instruction priority, universe traps)
- [x] Fix upstream Verification_s1.md schema drift; re-run phase_ready --phase s2
- [x] Read inputs: 5_Prompt.txt, Hardness_Plan.md, PersonaBrief.txt, Universe_Index/* (service inventory, key facts, today_horizon)
- [x] Read MoveOps tool catalog (6_Server_Tools_Details.json) for exact tool + parameter names
- [x] Read one V3 reference Oracle_Events.txt for voice / structure / numbering
- [x] Decompose prompt sentence-by-sentence; map every explicit + implicit ask to discovery or write
- [x] Ground every discovery step against _aux/Universe_Split/ via python queries (atom-verify exact IDs + amounts + dates + email IDs)
- [x] Draft 6_Oracle_Events.txt: numbered prose, exact tool names, exact parameter names, concrete universe values, no em-dashes, no tool names in prompt-level prose (only in OE bodies)
- [x] Run validator: python3 Validators/validate.py --phase oe
- [x] Council A — Grounding sub-agent (verify every tool + parameter + ID + amount against Universe_Split/ and 6_Server_Tools_Details.json)
- [x] Council B — Adversarial QC sub-agent (OE Completeness, OE Accuracy; forward + reverse prompt-OE coverage; B3 density projection ≥50 design target; B4 lever preservation; B8 forward-map to rubrics; B9)
- [x] Loop fixes + revalidate if needed
- [x] AUDIT auto-fire decision (conditional triggers per Track F v21): density THIN, OE list revised, draft iterations → AUDIT MANDATORY
- [x] Write Verification_s2.md (validator schema: Sources consulted with Per-task data / Eval spec / QC spec / Reference docs; Verification statements; Discrepancies surfaced; Verdict)
- [x] Append _aux/Reasoning/OE_solvability.md final report (OE-to-prompt coverage map, OE-to-rubric preview, AUDIT verdict)
- [x] STOP gate: end response, do NOT proceed to S3
