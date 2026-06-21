# PIPELINE REVIEW — Review-Type Task Intake

Triggered by: `PIPELINE REVIEW — Tasks/<TASK_DIR>`

## What this phase does

Review-type tasks arrive with `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json` already filled in by another candidate. The job is to score them against every QC dimension, identify every issue, propose fixes grounded in the per-task universe, and track each finding in `changes.md` so the user can rate the original candidate.

## Required inputs

| File | Source |
|---|---|
| `Tasks/<TASK_DIR>/1_Business_Function.txt` | user-pasted |
| `Tasks/<TASK_DIR>/2_Persona.txt` | user-pasted |
| `Tasks/<TASK_DIR>/3_UniverseDataForThisTask.json` | user-pasted |
| `Tasks/<TASK_DIR>/5_Prompt.txt` | candidate's prompt |
| `Tasks/<TASK_DIR>/6_Oracle_Events.txt` | candidate's OEs |
| `Tasks/<TASK_DIR>/7_Rubrics.json` | candidate's rubrics |
| `Reference/Prompt_Format.md`, `OE_Format.md`, `Rubric_Format.md` | format cards |
| `Reference/Council_Protocol.md` | council instructions |
| `Reference/Strict_Convention_Inventory.json` | allowed phrasings |
| `Reference/OE_Convention_Inventory.json` | OE conventions |
| `Tasks/_meta/Learnings.md` | empirical Opus 4.8 failure-mode catalog — used by triage to recognize known-bad patterns (L1 confirm-already-done, L6 stated-answer, L7 binary "is it posted?") faster than re-deriving them |
| `Docs/7_QC_Spec_Doc1.json`, `8_QC_Spec_Doc2.md` | QC scoring |

## Phase-readiness gate (run FIRST)

```
python Validators/phase_ready.py --phase review --task Tasks/<TASK_DIR>
```

Refuses if upstream artifacts are missing. If it STOPs, run the upstream phase first.

## Procedure

1. **Run S0 setup in full** — PersonaBrief, `split_universe.py`, `build_universe_index.py`, **`build_fact_ledger.py`**, **`build_graph_report.py`**. The review still needs the per-task universe split, index, ledger, and graph report — they were not produced when the candidate wrote the deliverables. The Fact Ledger is what backs the validator's groundedness sweep and Council A's atom verification; without it the review falls back to slow + less-rigorous substring scanning.

2. **Run the full assessment.** Always all three phases, regardless of any outcome — the candidate's rating depends on shortcomings across every artifact.
   ```
   python Validators/validate.py --phase all --task Tasks/<TASK_DIR>
   ```
   Then Council A grounding sweep on `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json`. Then Council B (5 perspectives × 5 lenses) on each. Then Final Council cross-artifact per `Reference/Sessions/FINAL.md` (Truthfulness lens, Cross-artifact Holism lens, Rubric Binding lens, Red-team lens). Every finding lands in `changes.md`.

3. **Pre-assess hardness (measured if possible).** Two paths:
   - **Trajectories present** (`Tasks/<TASK_DIR>/trajectory-runs/trajectory-run-*.json` OR `Tasks/<TASK_DIR>/Agent_Responses/Run*.json` non-empty): run the parser to compute real numbers:
     ```
     python Validators/parse_trajectories.py Tasks/<TASK_DIR>
     ```
     Output lands in `_aux/Trajectory_Stats.json`: per-run tool-call totals (with MCP-only subcount), `avg_tool_calls_total`, `pass_at_1`, `density_ok_at_40`, `difficulty_ok_at_40pct`, and an OK / REBUILD_CANDIDATE verdict. The script also parses `8_Verifier_Fails.txt` when present.
   - **No trajectories yet**: use Council B-B3's projected density + Council B-B4's lever-coverage report + FINAL Truthfulness lens's answer-leakage check. These are predictions — note them as predicted, not measured.

   Write the numbers + source (measured | predicted) to `_aux/Council_Reports/REVIEW_hardness.md`.

4. **Binary triage decision, mapped strictly to QC scoring.** The bar is clean 5/5 on every applicable QC sub-dimension. No score below 5 ships — either fix it to 5 in-place, or REBUILD. No issue is overlooked.

   First, produce a per-sub-dim QC scoresheet for the prompt (12 sub-dims from `Docs/7_QC_Spec_Doc1.json` Prompt + Universe sections). Then apply this decision table:

   | Trigger (apply in order) | Verdict | Action |
   |---|---|---|
   | ANY QC sub-dim on prompt or universe scores **1-2 (FAIL band)** — feasibility, unique-ground-truth end-state divergence, persona / business-function major mismatch, coherence bolt-on, contrived, investigation pre-solved, single-service tool use, ≥2 Major truthfulness errors, universe data missing | **REBUILD** | Cannot be fixed in-place — the scenario itself is the problem. Do NOT emit 14/15. Recommend `PIPELINE REDO`. |
   | Hardness fails: `pass_at_1 > 0.40` OR `avg_tool_calls_total < 40` (measured) OR Council B-B3 projected density < 40 OR Council B-B4 says levers don't trigger OR FINAL caught answer leakage | **REBUILD** | Hardness can't be patched by OE/rubric edits — needs new lever combination. Recommend `PIPELINE REDO`. |
   | Otherwise (every sub-dim scores 3-5, no hardness failure) | **SALVAGEABLE** | Fix every sub-dim < 5 in-place via `changes.md`. The fix MUST raise the score to 5 — a 3-4 (NON-FAIL band) score is still unacceptable for ship. Minor prompt edits land in `_aux/REVIEW_prompt_draft.txt`; OE + rubric edits land in 14/15. Re-score after Applied rows to confirm 5/5 before ship. |

   Document the verdict in `_aux/Council_Reports/REVIEW_triage.md`. Include:
   - The full per-sub-dim scoresheet (sub-dim name → score → one-line reason citing per-task universe).
   - The measured or predicted hardness numbers from `_aux/Trajectory_Stats.json` or Council B-B3/B-B4.
   - The verdict + which trigger row fired.
   - For SALVAGEABLE: a list of every sub-dim currently below 5 with the targeted fix (this becomes the `changes.md` rows).

5. **Verify every finding against the per-task universe BEFORE writing it to `changes.md`.** The candidate may be right and the council's first instinct may be wrong. Re-grep `_aux/Universe_Split/`. If the council was wrong, do not add the finding — note it in `_aux/Council_Reports/REVIEW_dismissed.md` instead.

6. **Initialize `Tasks/<TASK_DIR>/changes.md`** (or update if it exists) with one row per confirmed finding:

   ```markdown
   # changes.md

   | # | Phase | Dimension | Severity | Before | After (proposed) | Why | Verified | Status |
   |---|---|---|---|---|---|---|---|---|
   | 1 | Prompt | Truthfulness | Major | "<exact quote from candidate>" | "<proposed text>" | <one-line why, citing the per-task record> | yes — checked <file>:<row_id> | Pending |
   | 2 | OE | Accuracy | Major | "OE5: ... entry_number JE-acme_cloud-FP-2026-03-0099" | "OE5: ... entry_number JE-acme_cloud-FP-2026-03-0075" | the JE-0099 entry does not exist in this task's universe; the actual ID is JE-0075 | yes — confirmed in oracle_gl.ogl_journal_entries.json | Pending |
   | 3 | Rubrics | Atomicity | Moderate | rubric[12] bundles 'sends email AND creates Linear issue' | split into two rubrics | bundling violates atomicity (two failure modes for one rubric) | yes — flagged by validator and Council B | Pending |
   ```

   Severity from QC spec: Major / Moderate / Minor.
   Status starts as Pending. The user later marks Applied / Dismissed-with-proof / Pending.

7. **Write the candidate-facing feedback** to `Tasks/<TASK_DIR>/13_Feedback.txt`. This is the human-readable rating + what was strong + what was weak + the top 5 issues by severity. Write it in the persona of a senior reviewer giving direct, professional feedback. Concise. No em-dashes. No reference to the eval docs, the QC spec by file name, or the council process. Plain narrative.

   Structure:
   ```
   Overall: <FAIL | NON-FAIL | PASS> on QC (worst dimension: <X>).

   Strengths
   - <one sentence per strength, max 3>

   Issues
   - <issue 1, named with severity>: <one sentence explaining what was wrong and what it should have been>
   - <issue 2>: ...

   Recommended next steps for the candidate
   - <action 1>
   - <action 2>
   ```

8. **Materialize the corrected deliverables (triage-aware)**:
   - **If triage = REBUILD**: do NOT emit 14/15 even if rows are Applied. The scenario is the problem — patching OE / rubric on top would ship a half-fixed task. `13_Feedback.txt` carries the FAIL verdict + full shortcoming list, and the user invokes `PIPELINE REDO — Tasks/<TASK_DIR>` to rebuild from scratch.
   - **If triage = SALVAGEABLE**:
     - `Tasks/<TASK_DIR>/14_Updated_Oracle_Events.txt` — written ONLY if any OE-phase row in `changes.md` is Applied. Contains the full corrected OE list.
     - `Tasks/<TASK_DIR>/15_Updated_Rubrics.json` — written ONLY if any rubric-phase row in `changes.md` is Applied. Contains the full corrected rubric JSON.
     - If any prompt-phase row in `changes.md` is Applied (minor fixes that don't change the scenario shape): write the corrected prompt to `_aux/REVIEW_prompt_draft.txt`. The user pastes it back to the platform if they want to ship the corrected prompt alongside 14/15.

   Do NOT touch `5_Prompt.txt`, `6_Oracle_Events.txt`, or `7_Rubrics.json`. The originals are the rated artifact. 14/15 (and the draft) are the candidate-correct version that the user can ship to the platform.

   If no rows are Applied at REVIEW time, skip 14/15. They are generated on a subsequent pass once the user marks rows Applied in `changes.md`.

9. **Apply only fixes the user has marked Applied** in `changes.md`. Do NOT apply fixes unilaterally — the user is rating the original candidate; pre-applying fixes erases the evidence.

10. **Score each phase against QC.** Write a final score summary in `_aux/Council_Reports/REVIEW_score.md`:

   ```markdown
   # REVIEW score summary

   ## Prompt
   - Unique Ground Truth: 5
   - Feasibility: 3
   - ...
   - Worst dim: <X>
   - Overall: <FAIL | NON-FAIL | PASS>

   ## Oracle Events
   - Completeness: 5
   - Accuracy: 3
   - Worst dim: <X>
   - Overall: ...

   ## Rubrics
   - Atomicity: 5
   - Self-Containment: 5
   - ...
   - Worst dim: <X>
   - Overall: ...
   ```

11. **Re-run gates on the corrected `14_Updated_Oracle_Events.txt` and `15_Updated_Rubrics.json` if emitted.** Treat the corrected versions as a fresh shipment: run `python Validators/validate.py --phase oe` and `--phase rubrics` against them (point the validator at temp copies named `6_Oracle_Events.txt` / `7_Rubrics.json` in a scratch dir if needed), then re-run Council A + Council B + FINAL against the corrected set. Any BLOCKER on the corrected version means the fix introduced a new issue — iterate until clean. Originals 5/6/7 stay untouched throughout.

## Exit criteria

- `_aux/Universe_Split/` and `_aux/Universe_Index/` exist.
- `_aux/Fact_Ledger.json` exists.
- `_aux/Validator_Reports/` populated.
- `_aux/Council_Reports/REVIEW_*.md` populated (one per phase).
- `changes.md` exists with every confirmed finding as a row.
- `_aux/Council_Reports/REVIEW_score.md` exists with per-phase QC scores.
- `13_Feedback.txt` exists with the candidate-facing rating.
- `14_Updated_Oracle_Events.txt` exists IFF any OE-phase row is Applied.
- `15_Updated_Rubrics.json` exists IFF any rubric-phase row is Applied.
- Originals `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json` are UNTOUCHED.

## STOP gate

This phase ends here. End your response. The user reviews `changes.md`, marks each row Applied / Dismissed / Pending, and rates the original candidate.

Next-trigger paths (per triage verdict + platform outcome):

| Scenario | Next trigger |
|---|---|
| **SALVAGEABLE + rows Applied** | Re-invoke `PIPELINE REVIEW — Tasks/<TASK_DIR>` in a fresh chat — the runbook materializes `14_Updated_Oracle_Events.txt` / `15_Updated_Rubrics.json` (and a corrected prompt draft if any prompt-phase row was Applied) and re-runs all gates on the corrected set. |
| **REBUILD** | `PIPELINE REDO — Tasks/<TASK_DIR>` in a fresh chat. The corrected deliverables were intentionally not emitted because the scenario itself needs a rebuild. The candidate rating + feedback are already complete in `changes.md` + `13_Feedback.txt`. |
| **Shipped corrected version → platform linter blocks** | `PIPELINE S1.5 — Tasks/<TASK_DIR>` + paste linter output. |
| **Shipped corrected version → trajectories ran → verifier-fails** | `PIPELINE S4 — Tasks/<TASK_DIR>` + paste verifier fails. |
| **Shipped corrected version → platform paste-back may have mutated `7_Rubrics.json`** | `PIPELINE COMPARE — Tasks/<TASK_DIR>` after dropping `10_Rubrics_Platform.json` into the task folder. |
| **Shipped corrected version → trajectory failed difficulty (pass@1 > 40%) or density (avg < 40 tool calls)** | `PIPELINE REDO — Tasks/<TASK_DIR>` in a fresh chat. |
| **Review closed, candidate rated, task shipped clean** | EXIT. Append any novel finding to `Tasks/_meta/Learnings.md` if the review surfaced a new Opus 4.8 failure pattern. |

For maximum rigor on the review (review of a critical candidate's task): append `COUNCIL_MODE=multi` to the trigger — `PIPELINE REVIEW — Tasks/<TASK_DIR> COUNCIL_MODE=multi`. Spawns 5 separate reviewer sub-agents + consensus instead of single 5-lens call.

Do NOT pre-apply fixes in this chat.

**If the user pastes follow-up content in this chat** (Applied-row updates for materialization, a new task, fix attempts on a different deliverable, or an unrelated question), do NOT process it. Reply: "This chat is single-shot for the REVIEW intake and scoring pass. Please open a fresh chat and invoke the appropriate next trigger from the dispatch table." Chaining inside one chat defeats the entire pipeline.

## Bootstrap

Read root `AGENTS.md` first. Findings must be grounded in the per-task universe — base universe assumptions are stale. Severity follows the QC spec. Be conservative about flagging Minor issues that don't actually affect the score.
