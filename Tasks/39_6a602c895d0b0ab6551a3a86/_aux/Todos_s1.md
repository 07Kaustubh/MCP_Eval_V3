# Todos — S1 (REDO build — 2026-07-23)

Note: Pre-REDO S1 (5 levers, no L6) was completed and archived. This tracks the REDO S1 rebuild with 6 levers (L1+L6+L8+L9+L25+L26).

- [x] Read inputs (Hardness_Plan REDO, Candidate_Originals/5_Prompt.txt, Fact_Ledger, Prompt_Format, PersonaBrief)
- [x] Draft 5_Prompt.txt (Jaime voice, ≤500 words, no em-dashes, no tool names, no IDs, all 6 levers including L6 HubSpot deal paragraph)
- [x] Run validator (python3 Validators/validate.py --phase prompt) — PASS 0 fails 3 warns
- [x] Spawn Council A (grounding) — R1→R2 REVISE (count "twice"), R3 GO; R4 BLOCK (A3 pre-existing 6/18 Slack posts); R5 GO after Fix A (opener + Slack ask reframed)
- [x] Spawn Council B (adversarial QC) — R1 GO, R2 GO (uniform 5/5)
- [x] Run similarity gate (python3 Validators/calc_similarity.py) — max composite 24.8 PASS
- [x] Spawn AUDIT (oracle) — PASS (STRICT): 0 blockers, 0 revise, 7 minor downstream flags, 15/15 injection, 48/48 regression, density mid 60.5, 6/6 levers intact
- [x] Write Verification_s1.md
- [x] Write final report entry in _aux/Reasoning/prompt_design.md
