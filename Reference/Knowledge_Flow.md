# Knowledge Flow + File Nomenclature

This is the canonical map of (a) what each phase reads and produces, (b) the file-naming conventions across `_aux/`, task root, and `Tasks/_meta/`, and (c) which downstream phases must re-run when a given artifact changes. A fresh-chat agent invoking any phase should be able to read this doc + the phase runbook and know every file path it will touch.

## Phase dependency chart

| Phase | Reads (primary) | Produces |
|---|---|---|
| **NEW** | `<TASK_ID>` argument | Folder skeleton at `Tasks/<TASK_DIR>/` with empty `1_Business_Function.txt`, `2_Persona.txt`, `3_UniverseDataForThisTask.json` (+ `5/6/7/8` in review mode), `Agent_Responses/`, `trajectory-runs/` |
| **S0** | `1_Business_Function.txt`, `2_Persona.txt`, `3_UniverseDataForThisTask.json`, `Brookfield_Base_Universe/2_Persona_Briefs.md` | `PersonaBrief.txt`, `_aux/Universe_Split/<service>.<table>.json` (many), `_aux/Universe_Index/<6 files>`, `_aux/Fact_Ledger.json`, `_aux/data_hash.txt`, `_aux/S0_Setup_Report.md` |
| **HARDNESS** | S0 outputs + `_meta/Learnings.md` (mandatory first read) + `Reference/Hardness_Playbook.md`; conditional: `_aux/REDO_reason.md`, `_aux/Candidate_Originals/` | `_aux/Hardness_Plan.md` |
| **S1** | S0 + HARDNESS outputs + `Reference/Prompt_Format.md` + `Docs/4_Prompt_Hard_Tips.md` + `Prompt_Guidelines.md` + `Brookfield_Base_Universe/8_Server_Tools_Details.json` + `QC_Tasks/V3_Tasks/Task11..14/Prompt.txt` | `5_Prompt.txt`, `_aux/Validator_Reports/prompt.md`, `_aux/Council_Reports/S1_A_grounding.md`, `_aux/Council_Reports/S1_B_adversarial.md`, `_aux/Similarity_Report.json`, `_aux/Council_Reports/AUDIT_prompt.md`, `_aux/Reasoning/prompt_design.md` |
| **S1.5** | `5_Prompt.txt` + pasted linter output + `_aux/Fact_Ledger.json` + `_aux/Universe_Index/` + `_aux/Hardness_Plan.md` + `Reference/Linter_Playbook.md` + `Reference/Similarity_Pivot.md` | Conditional: revised `5_Prompt.txt` (CB mode) OR `_aux/REVIEW_prompt_draft.txt` (Review mode); `_aux/Linter_Decision.md`; `_aux/Linter_Justifications.md` (if invalidate path); overwritten `_aux/Council_Reports/AUDIT_prompt.md` (if revised); appends to `_meta/Linter_Justifications.md`, `_meta/Similarity_Log.md` |
| **S2** | S0 + S1 outputs + `Reference/OE_Format.md` + `Reference/OE_Convention_Inventory.json` + `Brookfield_Base_Universe/8_Server_Tools_Details.json` + `QC_Tasks/V3_Tasks/Task11..14/Oracle_Events.txt` | `6_Oracle_Events.txt`, `_aux/Validator_Reports/oe.md`, `_aux/Council_Reports/S2_A_grounding.md`, `_aux/Council_Reports/S2_B_adversarial.md`, `_aux/Council_Reports/AUDIT_oe.md`, `_aux/Reasoning/OE_solvability.md` |
| **S3** | S0 + S1 + S2 outputs + `Reference/Rubric_Format.md` + `Reference/Strict_Convention_Inventory.json` + `Brookfield_Base_Universe/8_Server_Tools_Details.json` + `QC_Tasks/V3_Tasks/Task11..14/Rubrics.json` + `Docs/2_Rubrics_V3_Guidelines.md` + `Docs/12_Always_Failing_Rubrics.md` | `7_Rubrics.json`, `_aux/Validator_Reports/rubrics.md`, `_aux/Council_Reports/S3_A_grounding.md`, `_aux/Council_Reports/S3_B_adversarial.md`, `_aux/Council_Reports/AUDIT_rubrics.md`, `_aux/Reasoning/Rubric_Coverage_Matrix.md` |
| **FINAL** | S1 + S2 + S3 outputs + HARDNESS + `_aux/Fact_Ledger.json` + `_aux/Universe_Index/` + `_meta/Learnings.md` + `Docs/7_QC_Spec_Doc1.json` + `Docs/8_QC_Spec_Doc2.md` + `Reference/Council_Protocol.md` | `_aux/Council_Reports/FINAL_council.md`; appends to `_meta/Hardness_Patterns_Log.md` on PASS |
| **S4** | `5/6/7` + `Agent_Responses/Run{1..6}_Trajectory.json` (or `trajectory-runs/trajectory-run-*.json`) + `8_Verifier_Fails.txt` + `_aux/Universe_Split/` + `_aux/Hardness_Plan.md` + `Reference/Linter_Playbook.md` + `Docs/12_Always_Failing_Rubrics.md` + `Evals/4_Verifier_Fails_Eval.md` | `_aux/Trajectory_Stats.json` (via `parse_trajectories.py`), `_aux/Council_Reports/S4_fixes.md`, `_aux/Council_Reports/S4_judge_errors.md`, `_aux/Council_Reports/S4_AF_justifications.md`, `_aux/Council_Reports/S4_verdict.md`; updates to `_meta/Stump_Hypotheses.md`, `_meta/Hardness_Patterns_Log.md` |
| **REVIEW** | Candidate-prefilled `1/2/3/5/6/7/8` + `Reference/<Prompt|OE|Rubric>_Format.md` + `Reference/Council_Protocol.md` + `Reference/Strict_Convention_Inventory.json` + `Reference/OE_Convention_Inventory.json` + `_meta/Learnings.md` + QC spec docs | Step 0 may route to S1.5 if linter blocks; otherwise: full `_aux/*` (S0 outputs via re-run), `_aux/Validator_Reports/*`, `_aux/Council_Reports/REVIEW_triage.md`, `_aux/Council_Reports/REVIEW_score.md`, `_aux/Council_Reports/REVIEW_hardness.md`, `_aux/Council_Reports/REVIEW_dismissed.md` (optional), `_aux/Council_Reports/AUDIT_<phase>.md` per phase, `_aux/Council_Reports/FINAL_council.md`, `_aux/Trajectory_Stats.json` (if trajectories present), `changes.md`, `13_Feedback.txt`; conditional: `14_Updated_Oracle_Events.txt`, `15_Updated_Rubrics.json`, `_aux/REVIEW_prompt_draft.txt` (only when corresponding Applied rows exist) |
| **COMPARE** | `7_Rubrics.json` + `10_Rubrics_Platform.json` | `_aux/Compare_Report.md` |
| **AUDIT** (on-demand) | Per-phase deliverables + `_aux/Hardness_Plan.md` + `_aux/Fact_Ledger.json` + `_aux/Universe_Split/` + `_aux/Universe_Index/` + `_aux/Council_Reports/*` + `_meta/Learnings.md` + QC spec docs + Eval docs | `_aux/Council_Reports/AUDIT_<phase>.md` (overwrites prior auto-fire audit if present) |
| **REDO** | Existing `5/6/7` + `14/15` (if present) + `Agent_Responses/Run*.json` + `_aux/*` | `_aux/Candidate_Originals/<archived copies>`, `_aux/REDO_reason.md`, updated `13_Feedback.txt`, cleared `5/6/7` (then rebuilt via fresh-chat `HARDNESS → S1 → S2 → S3 → FINAL`); appends new finding to `_meta/Learnings.md` |
| **CLOSE** | All artifacts | None (read-only audit) |

## File nomenclature conventions

| Pattern | Examples | Used for |
|---|---|---|
| `<N>_<purpose>.<ext>` at task root | `1_Business_Function.txt`, `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json`, `8_Verifier_Fails.txt`, `9_Universe_inject.sql`, `10_Rubrics_Platform.json`, `13_Feedback.txt`, `14_Updated_Oracle_Events.txt`, `15_Updated_Rubrics.json` | User-pasted inputs (1-3, 8, 10) + pipeline-produced deliverables (5-7, 9, 13-15) at task root |
| `<phase>_<council>_<purpose>.md` | `S1_A_grounding.md`, `S1_B_adversarial.md`, `S2_A_grounding.md`, `S2_B_adversarial.md`, `S3_A_grounding.md`, `S3_B_adversarial.md` | Per-phase Council A / Council B reports |
| `AUDIT_<phase>.md` | `AUDIT_prompt.md`, `AUDIT_oe.md`, `AUDIT_rubrics.md` | AUDIT veteran reports per phase (overwritten on re-audit) |
| `S4_<purpose>.md` | `S4_fixes.md`, `S4_judge_errors.md`, `S4_AF_justifications.md`, `S4_verdict.md` | S4 verifier-fails outputs by bucket / verdict |
| `<PHASE>_<purpose>.md` (cross-phase / special) | `FINAL_council.md`, `REDO_reason.md`, `REVIEW_triage.md`, `REVIEW_score.md`, `REVIEW_hardness.md`, `REVIEW_dismissed.md`, `REVIEW_prompt_draft.txt` | Multi-purpose phase artifacts where a single report covers the whole phase OR is consumed by downstream phases |
| `<phase>.md` (validator reports) | `_aux/Validator_Reports/prompt.md`, `oe.md`, `rubrics.md` | Validator phase reports |
| `<descriptive>.md` (reasoning) | `_aux/Reasoning/prompt_design.md`, `OE_solvability.md`, `Rubric_Coverage_Matrix.md` | Phase-specific reasoning — semantic names, not phase-prefixed |
| `<descriptive>.json` (structured data) | `_aux/Fact_Ledger.json`, `_aux/Trajectory_Stats.json`, `_aux/Similarity_Report.json` | Structured per-task artifacts |
| `Tasks/_meta/<descriptive>.md` (cross-task logs) | `Learnings.md`, `Similarity_Log.md`, `Linter_Justifications.md`, `Hardness_Patterns_Log.md`, `Stump_Hypotheses.md`, `Audit_Log.md` | Append-only cross-task knowledge |
| `_aux/data_hash.txt` | (single file) | Source-of-truth hash for the per-task universe — regenerate-trigger for S0 outputs |

## Single-source ownership (the SSOT map)

| Source | What it owns | Who consumes it |
|---|---|---|
| `_aux/Fact_Ledger.json` | Per-task verifiable atom surface (emails, money, dates, IDs, accounts, personas, periods) | Validator (groundedness sweep), Council A (atom verification), AUDIT (Lens 2), FINAL (Truthfulness lens), REVIEW (step 5 verification) |
| `_aux/Universe_Split/<service>.<table>.json` | Per-task universe raw data (overrides stale `Brookfield_Base_Universe/Data/`) | Validator (records lookups), Council A (grounding), HARDNESS (lever scan), AUDIT (Lens 3) |
| `_aux/Universe_Index/` | Compact lookups (service inventory, entities, accounts per entity, today/horizon, graph report) | HARDNESS (density-rich pivots), Council A (quick scoping), AUDIT (Lens 5 adversarial veteran) |
| `_aux/Hardness_Plan.md` | Selected levers + density projection + stump hypothesis | S1 (prompt drafting), Council B-B4 (preservation), AUDIT (Lens 3 end-to-end), FINAL (lever map), S4 (calibration) |
| `_meta/Learnings.md` | Empirical Opus 4.8 failure-mode catalog | HARDNESS (mandatory first read), Council B (calibration), AUDIT (Lens 5), REVIEW (triage faster-than-rederive) |
| `Brookfield_Base_Universe/8_Server_Tools_Details.json` | Tool definitions + parameter names (only stable file in base universe) | Validator (param checks), S2 (OE drafting), Council A-A1 (tool/param verification), AUDIT |
| `Brookfield_Base_Universe/2_Persona_Briefs.md` | Persona descriptions (stable per version) | S0 (PersonaBrief extract), S1 (voice), Council A-A2 (convention) |
| `Docs/7_QC_Spec_Doc1.json` + `Docs/8_QC_Spec_Doc2.md` | QC dimension scoring rubric | Council B-B1 (sub-dim scoring), AUDIT (Lens 1 strict scoring), FINAL (lens 2), REVIEW (step 10 scoring) |
| `_aux/Trajectory_Stats.json` | Measured pass@1 + avg_tool_calls + per-rubric run matrix | S4 (verdict), REVIEW step 3 (hardness pre-assessment when present), REDO (REDO trigger numbers) |
| `Reference/Strict_Convention_Inventory.json` | Allowed rubric phrasings extracted from V3 references | Validator (rubric phase), Council A-A2 (convention) |
| `Reference/OE_Convention_Inventory.json` | Allowed OE shapes extracted from V3 references | Validator (oe phase), Council A-A2 (convention) |

## Cross-phase re-run map

When an artifact changes, downstream phases that DEPEND on it MUST re-run.

| Artifact changed | Phases that must re-run |
|---|---|
| `3_UniverseDataForThisTask.json` (universe re-sourced) | S0 (regenerates ALL `_aux/*`); HARDNESS (re-picks levers); S1 (prompt may need re-engineering); S2 (OE re-grounding); S3 (rubric re-grounding); FINAL (cross-artifact re-check) |
| `_aux/Fact_Ledger.json` | Same as universe — propagates everywhere |
| `_aux/Hardness_Plan.md` | S1 (re-engineer prompt to match new lever set); B4 hardness preservation re-checks downstream |
| `5_Prompt.txt` | S1.5 (re-run validator + A + B + AUDIT + similarity); S2 (re-grounding — OE may need adjustment); S3 (re-coverage — rubrics may need adjustment); FINAL (cross-artifact re-check) |
| `6_Oracle_Events.txt` | S2 (re-run validator + A + B + AUDIT); S3 (re-grounding — rubric evidence cites OE steps); FINAL (cross-artifact re-check) |
| `7_Rubrics.json` | S3 (re-run validator + A + B + AUDIT); FINAL (cross-artifact re-check); if already shipped → COMPARE on next paste-back |
| `_aux/Council_Reports/AUDIT_<phase>.md` showing REVISE | Iterate the producing phase up to 3 rounds; if AUDIT still REVISE → escalate to user; if REBUILD → REDO |
| `_aux/Council_Reports/<phase>_B_adversarial.md` showing `PROPAGATE TO <upstream>` (Council B-B6) | STOP the current phase; re-run the named upstream phase; then re-run the current phase against the fresh upstream output |

## Why this matters

Two failure modes this prevents:

1. **Phase invokes the wrong file path.** A fresh-chat agent reading the phase runbook + this doc will know the exact path of every input and output. No guessing, no creating duplicate-purpose files under different names.
2. **Downstream phases run against stale upstream artifacts.** The cross-phase re-run map tells the operator (and the agent) which downstream phases need re-runs when an artifact changes. Skipping this is the most common pipeline failure mode.

For runbook-level details of each phase, see `Reference/Sessions/*.md`. This doc is the cross-cutting reference that ties them together.
