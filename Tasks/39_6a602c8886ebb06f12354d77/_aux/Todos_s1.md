# Todos — S1 (Tasks/39_6a602c8886ebb06f12354d77, StarPM V4) — COMPLETE

- [x] Phase-readiness gate green. Repaired malformed Verification_hardness.md (validator false-positive: self-referential prose quoting `## Sources consulted`/`## Verdict` + `## Data sources consulted` header mismatch). Substance untouched.
- [x] Reads_s1.md reading log (v11 E2 gate)
- [x] Read inputs: Hardness_Plan.md, PersonaBrief.txt, business function, persona, universe index/split grounding rows
- [x] Read Prompt_Format.md, Docs_starpm hard tips + date SSOT, Prompt_Guidelines.md, tool catalog (feasibility, closes HARDNESS disc. #3), V4 QC_Passed refs, Council_Protocol.md
- [x] Draft 5_Prompt.txt (233 words, no em-dash, no tool/MCP/ID names, levers L10/L2/L1/L4/L3 environmental, 4 writes; Airtable/Linear/disposal unnamed to preserve traps)
- [x] validate.py --phase prompt -> PASS (revised once past cross-service + investigation/action keyword gates by naming email + make-ready channel write targets while keeping trap services unnamed)
- [x] Council A (grounding) -> GO
- [x] Council B (adversarial QC) -> GO (5/5 all sub-dims, unique end-state, density ~47/model, 5 levers preserved)
- [x] Similarity gate -> PASS (max_composite 26.7 < 40)
- [x] AUDIT (oracle, StarPM V4 40+ density bar) -> PASS (STRICT). 14/14 sub-dims 5/5, density ~46/model, 62/62 regression anchors, no telegraphing
- [x] Verification_s1.md (v16 cross-source; authored in validator-conforming shape so S2 phase-gate passes)
- [x] Final report -> Reasoning/prompt_design.md
- [x] STOP gate reached: awaiting platform linter paste (S1.5) or linter-clean confirmation (S2)

## Carry-forward for operator (surface before S2)
- BLOCKER-BEFORE-S2: Fact_Ledger.lifecycle.today is null (should be 2026-07-01). Rebuild via build_fact_ledger.py (registry today) or patch, before S2/S3 (Council A A3 narrative-state checks consume it).
- S0 report injection claim inaccurate (comment-only inject stub); correct to "no separately-documented injection".
- S2/S3 rubric-design constraint (AUDIT advisory): full credit must require cross-source synthesis + the 4-write workflow, since James's own 6/22 #maintenance messages corroborate "8D still open" (universe-resident, not in the prompt-directed #make-ready channel, does not defeat the stump). Optional authority-injection re-hardens.
- Pipeline bugs worth a fix: (a) check_verification.py false-positives on docs quoting their own header-strings in prose; (b) runbook verification templates name the first section "Data sources consulted" while the validator requires "Sources consulted".
