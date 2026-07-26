# Todos — S1 (Tasks/40_6a614767cd5b60ad96902fb4, universe=starpm/V4)

- [ ] Read inputs (Hardness_Plan, PersonaBrief, 1_Business_Function, 2_Persona, Prompt_Format, date SSOT Docs_starpm/6, Universe_Index, tool catalog, hard tips, V4 QC_Passed reference prompts)
- [ ] Draft 5_Prompt.txt (persona voice, <=500 words, no em-dash, no tool names, no MCP-server names, no internal IDs, no pre-solving; engineer the selected Hardness levers naturally)
- [ ] Run validator (validate.py --phase prompt) -> exit 0, fix all FAILs
- [ ] Run Council A (grounding) sub-agent -> zero ungrounded claims
- [ ] Run Council B (adversarial QC + B3 density projection + B4 lever preservation) sub-agent -> every applicable sub-dim >=5, density midpoint >=40 (StarPM), all levers triggered
- [ ] Loop on any council block (re-validate + re-run both councils)
- [ ] Run similarity gate (calc_similarity.py) -> composite < 40 (else PIVOT via Similarity_Pivot.md)
- [ ] Run AUDIT (oracle, --phase prompt) -> PASS (STRICT); REVISE cap 3 rounds
- [ ] Write Verification_s1.md (cross-source: data + eval spec + QC spec + reference cards)
- [ ] Write final report to _aux/Reasoning/prompt_design.md
- [ ] STOP at gate (end response; wait for linter paste -> S1.5, or linter-clean -> S2)


## Status: COMPLETE (2026-07-23)
All steps executed:
- [x] Inputs read (Hardness_Plan, PersonaBrief, 1/2, Prompt_Format, Prompt_Guidelines, Docs_starpm/4+6, Universe_Index, V4 QC_Passed reference prompts, Council_Protocol).
- [x] 5_Prompt.txt drafted (312 words, persona voice, 5 levers engineered, 0 dashes, 0 tool/MCP/ID leaks).
- [x] Validator --phase prompt PASS (0 fails / 0 warns / 7 notes; fixed initial cross-service FAIL + bolt-on WARN).
- [x] verify_universe_atoms PASS (0 atoms); regression anchors 62/62 PASS.
- [x] Council A (grounding, explore) -> GO, zero ungrounded claims.
- [x] Council B (adversarial QC, oracle) -> GO, 12/12 sub-dims = 5, density Opus~44/Gemini~46, all 5 levers preserved.
- [x] Similarity gate -> 26.6 composite < 40 (no pivot).
- [x] AUDIT (oracle, --phase prompt) -> PASS (STRICT), 0 REVISE rounds.
- [x] Verification_s1.md written (canonical format, check_verification.py OK).
- [x] Final report -> _aux/Reasoning/prompt_design.md.
- [x] Audit_Log.md appended; phase_ready --phase s2 green.
- [x] STOP gate reached.

4 binding carries recorded for S2/S3 (see prompt_design.md + S1_B_adversarial.md + AUDIT_prompt.md): (1) 'the ticket' cross-service referent -> pin eviction/turn tracker, goal-phrased rubric; (2) ESA 'approved on record' phrasing (not 'open ticket'); (3) preserve decoys incl fldMoveOut/selSched -> derive hold from NOTES; (4) universe date artifacts -> trace from newest notes.