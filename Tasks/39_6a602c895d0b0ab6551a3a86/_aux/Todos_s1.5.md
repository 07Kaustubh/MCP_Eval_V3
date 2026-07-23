# Todos — S1.5 Round (post platform linter block on HubSpot cross-persona write)

- [x] Read S1.5 runbook + Linter_Playbook + current 5_Prompt + Hardness_Plan + Council reports + REDO_reason
- [x] Verify linter claim skeptically — spawn `explore` on QC-persona HubSpot scope (bg_52c174f8)
- [x] Verify density recovery options — spawn `explore` on QC-scope density levers (bg_90468e4b)
- [x] Classify linter block: Class A (persona / business-function scope violation), verdict CLEARLY RIGHT → REVISE
- [x] Draft revised prompt: remove HubSpot ask, elevate Bennett-note verification (+3 calls) and Sandra-tag lookup (+1 call) to recover density
- [x] Overwrite `5_Prompt.txt` in place (CB-mode revise per runbook step 3.2)
- [x] Run `python3 Validators/validate.py --phase prompt --task Tasks/39_6a602c895d0b0ab6551a3a86`
- [x] Spawn Council A (grounding + convention re-sweep on revised prompt) in background
- [x] Spawn Council B (adversarial + density + hardness-preservation on revised prompt) in background
- [x] Wait for both council reports; verify GO on both — Council A R6 GO / Council B R3 GO
- [x] Update Hardness_Plan.md with S1.5 REVISION UPDATE section (Council B B6 propagation)
- [x] Run regression-anchor suite (LENS 8 prerequisite) — 48/48 PASS
- [x] Spawn AUDIT (`oracle` — strict veteran, per S1.5 runbook step 8, MANDATORY on revise path)
- [x] Wait for AUDIT verdict; require PASS (STRICT) — verdict PASS (STRICT), zero BLOCKER, zero MAJOR, 4 MINOR informational
- [x] Write `_aux/Linter_Decision.md` summarizing block, reasoning, resolution, density-recovery moves, downstream impact on Hardness_Plan L6
- [x] STOP with next-trigger instructions (re-submit revised 5_Prompt.txt to platform; on clear → PIPELINE S2 fresh chat)
