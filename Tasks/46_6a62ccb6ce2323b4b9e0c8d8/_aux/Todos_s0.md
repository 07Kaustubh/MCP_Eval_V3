# S0 Todos — Tasks/46_6a62ccb6ce2323b4b9e0c8d8

Runbook: `Reference/Sessions/S0.md`. Step 0 gate (v11 E1). Status legend: `pending` / `in_progress` / `completed`.

| # | Step | Command / artifact | Status |
|---|---|---|---|
| 0 | Create this TODO list | `_aux/Todos_s0.md` | completed |
| 1 | Detect universe | `python3 Validators/universes.py Tasks/46_6a62ccb6ce2323b4b9e0c8d8` -> `_aux/Universe.txt` | completed (`starpm`) |
| 2 | Extract Persona Brief verbatim | `StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md` L13-34 -> `PersonaBrief.txt` | completed (1,451 bytes) |
| 3 | Split per-task universe | `python3 Validators/split_universe.py ...` -> `_aux/Universe_Split/`, `_aux/data_hash.txt` | completed (3,892 records / 33 sources) |
| 4 | Build Universe Index (5 files) | `python3 Validators/build_universe_index.py ...` -> `_aux/Universe_Index/` | completed |
| 5 | Build Fact Ledger | `python3 Validators/build_fact_ledger.py ...` -> `_aux/Fact_Ledger.json` | completed |
| 6 | Build Graph Report | `python3 Validators/build_graph_report.py ...` -> `_aux/Universe_Index/graph_report.md` | completed |
| 7 | Build Feasible Surface | `python3 Validators/build_feasible_surface.py ...` -> `_aux/Feasible_Surface.json` | completed (15 tables / 19 enum cols) |
| 8 | V4 injection gate (starpm + non-empty `9_Universe_inject.sql`) | `python3 Validators/validate.py --phase injection --task ...` | completed, non-blocking (PASS 0/0/4; inject file is a comment-only header, 0 executable statements -> SKIP per hard rule 4) |
| 9 | Write setup report | `_aux/S0_Setup_Report.md` | completed |
| 10 | Write cross-source verification (Step 0.5) | `_aux/Verification_s0.md` | completed |
| 11 | Exit-criteria audit + STOP gate | `check_verification.py --phase s0` OK; `phase_ready.py --phase hardness` OK (both are FORMAT gates, see note below) | completed |
| 12 | Adversarial second-opinion review | independent skeptical review of the S0 output against the runbook | completed (verdict: exit criteria MET, all 8 steps ran, STOP correct; 4 reporting defects found) |
| 13 | Apply review findings | 3 discrepancies appended to `_aux/Verification_s0.md` (4 -> 7), mirrored as notes 5-7 in `_aux/S0_Setup_Report.md`, gate-citation language corrected, discrepancies numbered so cross-references resolve | completed |

## Notes

- Inputs present at start: `1_Business_Function.txt` (Property Operations), `2_Persona.txt` (Lisa Smith, Onsite Property Manager), `3_UniverseDataForThisTask.json` (4,431,335 bytes).
- `9_Universe_inject.sql` is present at 4,065 bytes but has **0 non-comment lines** (still the `PIPELINE NEW` scaffold header), and `4_Changelog.json` is `[]`. Step 8 therefore SKIPs. The validator was run anyway to record a result rather than assert one, and returned PASS with 4 council-deferred notes, but that PASS is **vacuous**: with no statements to evaluate it certifies nothing about injection quality.
- Dual-model `Agent_Responses/{Opus,Gemini}/Run1-6_Trajectory.json` present (V4 shape) — not consumed at S0.
- **On the gates in step 11.** `check_verification.py` validates format only: substring checks for the four section headers and three source-category labels, a checklist rule that fails only when `unchecked > 0 and checked == 0`, and a bare regex for the PASS / REVISE / BLOCK token. It never reads the justification behind a checked box. Its `[OK]` is formatting compliance, not validation, and the PASS verdict in `Verification_s0.md` is therefore self-graded.
- **Review findings applied in step 13** (all forward-looking, none blocked HARDNESS): Fact_Ledger carries no Calendar / Gmail / QuickBooks id classes though rule 13 names Calendar specifically; `Feasible_Surface.json` omits `airtable.airtable_records`, StarPM's source of record, because the builder reads only top-level `row_data` keys while the enums nest under `fields.fld*`; and `Fact_Ledger.lifecycle.today` is `null` from a `today` vs `universe_today` key mismatch between two builders. All three are pipeline-builder limitations rather than run errors, so they were surfaced rather than patched mid-phase.
