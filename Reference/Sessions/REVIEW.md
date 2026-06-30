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

## Step 0: Create your TODO list (MANDATORY)

Before any other action, create `Tasks/<TASK_DIR>/_aux/Todos_review.md` listing every step in the Procedure below as a discrete atomic todo. Mark `in_progress` / `completed` as you progress. v11 E1 operator-discipline gate.

## Procedure

0. **Linter check FIRST.** If the operator could NOT access the candidate's prefilled OE / rubrics because the candidate's prompt is currently blocked by the platform linter, STOP the REVIEW flow here and route to `PIPELINE S1.5 — Tasks/<TASK_DIR>` in a fresh chat with the linter output. S1.5 will detect Review-mode (presence of candidate-prefilled `6_Oracle_Events.txt` + `7_Rubrics.json`) and handle the linter skeptical-first: invalidate with justification (preferred — preserves the candidate's original prompt for rating) or write a minimal-fix scratch draft to `_aux/REVIEW_prompt_draft.txt` if revision is unavoidable. Once linter is cleared (the platform accepts the prompt — either the candidate's original after pushback, or the scratch-draft fix), the operator returns and re-invokes `PIPELINE REVIEW` in a fresh chat. The original `5_Prompt.txt` stays pristine throughout — any fix lands in `_aux/REVIEW_prompt_draft.txt` for use during materialization (step 8).

   If the candidate's prompt already cleared linter at submission time (operator has full access to prefilled `6_Oracle_Events.txt` + `7_Rubrics.json`), skip step 0 and proceed to step 1.

1. **Run S0 setup in full** — PersonaBrief, `split_universe.py`, `build_universe_index.py`, **`build_fact_ledger.py`**, **`build_graph_report.py`**. The review still needs the per-task universe split, index, ledger, and graph report — they were not produced when the candidate wrote the deliverables. The Fact Ledger is what backs the validator's groundedness sweep and Council A's atom verification; without it the review falls back to slow + less-rigorous substring scanning.

2. **Run the full assessment with parity to CB's per-phase gates.** Always all three phases, regardless of any outcome — the candidate's rating depends on shortcomings across every artifact.

   **Programmatic floor FIRST (v18):** every assessment starts with a deterministic universe-atom check that walks the original 5/6/7 and runs precise universe queries per atom (account-on-entity, no-response-claims, ID presence, etc.):

   ```
   python Validators/verify_universe_atoms.py --task Tasks/<TASK_DIR>
   ```

   Exit non-zero on any atom FAIL with the specific atom + universe row. This is the load-bearing floor the LLM councils trust — if it doesn't run clean, FIX THE ATOMS BEFORE the council assessment (otherwise the councils will narrate "atoms verified" on broken atoms).

   **Per-universe landmines:** the full landmine catalog is codified in `Validators/universes.py` (per-universe `landmines` block) and enforced programmatically by `verify_universe_atoms.py`. Full per-landmine descriptions live in `AGENTS.md` under "Universe constants (multi-universe — v20)" — read the section matching `_aux/Universe.txt` to know which apply to this task. The script runs each landmine check; the LLM REVIEW pass then sanity-checks any flagged atom against the corresponding universe row. **Recurring landmines by universe** (see AGENTS.md for full descriptions): Brookfield → account-number trap (105000/120000 differ per entity) + email-chain truthfulness; KeyStone → TRID timing + LOS-vs-CRM source-of-truth + departed-employee Marcus Webb; MoveOps → PHMSA hazmat + Airtable-vs-CRM source-of-truth + Marcus Webb identity (BrightLoop analyst, distinct from KeyStone Marcus) + Heartland Q1 invoice cross-reference + ExpenseBot pilot bugs.

   Then the validator + council sequence:

   ```
   python Validators/validate.py --phase all --task Tasks/<TASK_DIR>
   ```

   Then in sequence:
   1. **Council A** grounding sweep on `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json` (all 13 perspectives A1-A13).
   2. **Council B** adversarial QC on each artifact (all 11 perspectives B1-B11).
   3. **AUDIT on each ORIGINAL artifact (v17 — parity with CB's per-phase auto-fire)**: invoke `PIPELINE AUDIT --phase prompt`, `--phase oe`, `--phase rubrics` on the candidate's originals. Reports → `_aux/Council_Reports/AUDIT_prompt_original.md`, `AUDIT_oe_original.md`, `AUDIT_rubrics_original.md`. This applies the strictest-interpretation lens that CB gets per-phase via the v7 inline-AUDIT mandate; REVIEW previously skipped this on the originals and only ran AUDIT on the corrected 14/15.
   4. **Final Council** cross-artifact per `Reference/Sessions/FINAL.md` (all 6 lenses).

   Every finding from Council A + Council B + AUDIT + FINAL lands in `changes.md` (Step 6).

3. **Pre-assess hardness (measured if possible).** Two paths:
   - **Trajectories present** (`Tasks/<TASK_DIR>/trajectory-runs/trajectory-run-*.json` OR `Tasks/<TASK_DIR>/Agent_Responses/Run*.json` non-empty): run the parser to compute real numbers:
     ```
     python Validators/parse_trajectories.py Tasks/<TASK_DIR>
     ```
     Output lands in `_aux/Trajectory_Stats.json`: per-run tool-call totals (with MCP-only subcount), `avg_tool_calls_total`, `pass_at_1`, `density_ok_at_40`, `difficulty_ok_at_40pct`, and an OK / REBUILD_CANDIDATE verdict. The script also parses `8_Verifier_Fails.txt` when present.
   - **No trajectories yet**: use Council B-B3's projected density + Council B-B4's lever-coverage report + FINAL Truthfulness lens's answer-leakage check. These are predictions — note them as predicted, not measured.

   Write the numbers + source (measured | predicted) to `_aux/Council_Reports/REVIEW_hardness.md`.

3.5. **Deep trajectory analysis with S4-style bucket classification (v17).** If `Agent_Responses/Run*.json` exists, walk every failing rubric trajectory across all runs and classify each into a bucket — same procedure as PIPELINE S4, but applied to the candidate's ORIGINAL rubric set, not the corrected one.

   For every rubric that failed in any run, build a trajectory walk record covering ALL completed runs:
   - **Bucket 1 — Rubric Invalid**: the rubric is the problem (e.g., locked-in channel when prompt said "notify", fabricated value, fake tool name, evidence stricter than criterion, overly broad accepting invalid options). Action: each Bucket 1 finding AUTO-POPULATES a `changes.md` row tagged `[trajectory-bucket-1]` with the concrete failure evidence (Run X, trajectory citation showing why the rubric fails the candidate's correct action). The materialization step will fix or remove the rubric.
   - **Bucket 2 — Judge Error**: the rubric is correct but the judge misread the trajectory. Trajectory citation proves the agent satisfied it. Action: log to `_aux/Council_Reports/REVIEW_bucket_classification.md` as POSITIVE evidence of rubric soundness.
   - **Bucket 3 — Legitimate Model Failure**: the rubric is correct and the agent really failed. This is desired difficulty. Action: log as POSITIVE evidence of rubric quality + hardness.

   Then run the same T2 + T3 hard gates from S4 on the ORIGINAL trajectories:
   - **T2 (pass@1 ≤ 40%)**: across completed runs, count how many passed all valid rubrics. > 40% = task is too easy on the original; this strengthens the case for REBUILD.
   - **T3 (error_runs ≤ 2)**: count runs that errored out. ≥ 3 = trajectory set unreliable; flag for re-run before final scoring.

   **All-Failing Rubrics sub-dim scoring (same threshold as S4 D2)**: compute `Bucket 1 ratio = Bucket 1 count / total failing rubrics count`. > 50% = 1/5 FAIL on All-Failing Rubrics sub-dim; 25-50% = 3/5 NON-FAIL; < 25% = 5/5 PASS. Record in `_aux/Council_Reports/REVIEW_bucket_classification.md` AND feed into the triage decision in Step 4 (high Bucket 1 ratio = rubric set is fragile, weighs toward REBUILD).

   This closes the gap where REVIEW used trajectory data only for hardness numbers (pass@1, tool calls) and never walked the trajectories to distinguish rubric defects from genuine model failures.

4. **Binary triage decision, mapped strictly to QC scoring.** The bar is clean 5/5 on every applicable QC sub-dimension. No score below 5 ships — either fix it to 5 in-place, or REBUILD. No issue is overlooked.

   First, produce a per-sub-dim QC scoresheet for the prompt (12 sub-dims from `Docs/7_QC_Spec_Doc1.json` Prompt + Universe sections). Then apply this decision table:

   | Trigger (apply in order) | Verdict | Action |
   |---|---|---|
   | **Business function mismatch** — the prompt's primary scenario does not match the assigned business function (one of the 10 Brookfield categories) | **REBUILD** | Business function is the FIXED scope anchor and cannot be reassigned in either CB or REVIEW flow. Do NOT emit 14/15. Recommend `PIPELINE REDO`. |
   | **Persona mismatch (business function still valid)** — the assigned persona's role does not credibly fit the prompt, but a different persona within the SAME business function would | **SALVAGEABLE (persona-swap)** | Both CB and REVIEW authors may swap persona for a better-fitting one within the same business function. Add a `## Persona swap` row in `changes.md` naming the new persona + role + reason. Update 2_Persona.txt + minor prompt edits in `_aux/REVIEW_prompt_draft.txt` if persona name appears in prompt body. Re-score after the swap. |
   | ANY OTHER QC sub-dim on prompt or universe scores **1-2 (FAIL band)** — feasibility, unique-ground-truth end-state divergence, coherence bolt-on, contrived, investigation pre-solved, single-service tool use, ≥2 Major truthfulness errors, universe data missing | **REBUILD** | Cannot be fixed in-place — the scenario itself is the problem. Do NOT emit 14/15. Recommend `PIPELINE REDO`. |
   | Hardness fails: `pass_at_1 > 0.40` OR `avg_tool_calls_total < 40` (measured) OR Council B-B3 projected density < 40 OR Council B-B4 says levers don't trigger OR FINAL caught answer leakage | **REBUILD (or persona-swap retry)** | First check: would a persona-swap within the SAME business function unlock more hardness levers (e.g., a Compliance Officer persona surfaces more cross-service AML levers than the assigned Accounts Manager)? If yes, swap persona and re-run HARDNESS before declaring REBUILD. If no, hardness can't be patched — recommend `PIPELINE REDO`. |
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
   | 1 | Prompt | Truthfulness | Major | "<exact quote from candidate>" | "<proposed text>" | <one-line why, citing the per-task record> | yes — checked <file>:<row_id> | `oracle_gl.ogl_accounts WHERE account_number=N AND entity_id=E -> 'Actual Role Label'` | Applied |
   | 2 | OE | Accuracy | Major | "OE5: ... entry_number JE-acme_cloud-FP-2026-03-0099" | "OE5: ... entry_number JE-acme_cloud-FP-2026-03-0075" | the JE-0099 entry does not exist in this task's universe; the actual ID is JE-0075 | yes — confirmed in oracle_gl.ogl_journal_entries.json | `verify_universe_atoms.py: JE-...-0099 NOT FOUND; JE-...-0075 verified` | Applied |
   | 3 | Rubrics | Atomicity | Moderate | rubric[12] bundles 'sends email AND creates Linear issue' | split into two rubrics | bundling violates atomicity (two failure modes for one rubric) | yes — flagged by validator and Council B | `validate.py rubric[12]: AND-bundling FAIL` | Applied |

   **Verification-Evidence column (v18, MANDATORY).** Every "verified" cell must link to the universe query that proved it (e.g., `oracle_gl.ogl_accounts WHERE account_number=120000 AND entity_id=northstar_legal -> 'Client Cost Advances'` or `verify_universe_atoms.py: <atom> -> <result>`). Empty Verification-Evidence cell = the finding is operator-trusted, not data-verified. Reject any row that ships without verification evidence; force the operator to re-query the universe + populate the cell.
   ```

   Severity from QC spec: Major / Moderate / Minor.
   **Status defaults to `Applied` (v17 auto-apply)** so the operator can invoke `PIPELINE MATERIALIZE` in a fresh chat directly without manual marking. If the operator wants to reject a specific row, they can manually edit `changes.md` and change `Applied` → `Dismissed` (with one-line proof) before invoking MATERIALIZE. Trajectory-bucket-1 findings auto-populated in Step 3.5 are tagged `[trajectory-bucket-1]` in the issue column for traceability.

7. **Defer the candidate-facing feedback to PIPELINE FEEDBACK.** Do NOT write `13_Feedback.txt` inside REVIEW. The feedback step has been lifted into a dedicated fresh-chat phase (`PIPELINE FEEDBACK — Tasks/<TASK_DIR>`) that runs AFTER REVIEW and BEFORE CLOSE.

   **Why this is a separate phase.** By the time REVIEW reaches feedback-time, the chat context is saturated with fix-related work (changes.md rows, council reports, fix proposals, the materialized 14/15). The feedback then consistently drifts to rating what we fixed instead of what the candidate submitted — even with explicit guardrails in the runbook. The new phase has a clean fresh-chat context AND a strict input allowlist (originals 5/6/7 only — no `changes.md`, no `14_*`, no `15_*`, no `_aux/Council_Reports/*`, no draft). It also evaluates the candidate against the QC SPEC BASELINE only, NOT against our internal exceeds-spec bar (50+ density, strictest AUDIT, B6 propagation, etc.). See `Reference/Sessions/FEEDBACK.md` for full procedure.

   REVIEW step 7 is therefore a NO-OP. Skip to step 8 (materialization). `13_Feedback.txt` gets written when the operator invokes `PIPELINE FEEDBACK` in a fresh chat after REVIEW completes.

8. **Score each phase against QC.** Write a final score summary in `_aux/Council_Reports/REVIEW_score.md`:

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

   Include the All-Failing Rubrics sub-dim score from Step 3.5 if trajectories were available.

9. **STOP — materialization handed off to PIPELINE MATERIALIZE (v17).** REVIEW no longer materializes the corrected 14/15 inline. It produces the analysis + change-list + auto-marked changes.md, then the operator invokes `PIPELINE MATERIALIZE — Tasks/<TASK_DIR>` in a fresh chat to apply Applied rows and re-run the gates on the corrected set. This split keeps the REVIEW chat context clean (analysis only) and the MATERIALIZE chat focused (apply + verify only).

## Exit criteria

- `_aux/Universe_Split/` and `_aux/Universe_Index/` exist.
- `_aux/Fact_Ledger.json` exists.
- `_aux/Validator_Reports/` populated.
- `_aux/Council_Reports/REVIEW_*.md` populated (one per phase + AUDIT_*_original.md per artifact + REVIEW_bucket_classification.md if trajectories were present).
- `changes.md` exists with every confirmed finding as a row, all rows auto-marked `Applied` (operator may manually flip individual rows to `Dismissed` before invoking MATERIALIZE).
- `_aux/Council_Reports/REVIEW_score.md` exists with per-phase QC scores.
- `13_Feedback.txt` is NOT written by this phase (deferred to `PIPELINE FEEDBACK` in a fresh chat — see step 7).
- `14_Updated_Oracle_Events.txt` / `15_Updated_Rubrics.json` are NOT written by this phase (deferred to `PIPELINE MATERIALIZE`).
- Originals `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json` are UNTOUCHED.

## STOP gate

This phase ends here. End your response. The operator can optionally edit `changes.md` to flip specific Applied rows to Dismissed before next step. Then invoke `PIPELINE MATERIALIZE — Tasks/<TASK_DIR>` in a fresh chat to apply the Applied rows + re-run gates on the corrected 14/15 + prompt draft. After MATERIALIZE, invoke `PIPELINE FEEDBACK` then `PIPELINE CLOSE`.

Next-trigger paths (per triage verdict + platform outcome):

| Scenario | Next trigger |
|---|---|
| **Standard REVIEW intake done (any triage path)** | `PIPELINE FEEDBACK — Tasks/<TASK_DIR>` in a fresh chat to write `13_Feedback.txt`. Then `PIPELINE CLOSE — Tasks/<TASK_DIR>`. |
| **SALVAGEABLE + rows Applied** | Re-invoke `PIPELINE REVIEW — Tasks/<TASK_DIR>` in a fresh chat — the runbook materializes `14_Updated_Oracle_Events.txt` / `15_Updated_Rubrics.json` (and a corrected prompt draft if any prompt-phase row was Applied) and re-runs all gates on the corrected set. |
| **REBUILD** | `PIPELINE REDO — Tasks/<TASK_DIR>` in a fresh chat. The corrected deliverables were intentionally not emitted because the scenario itself needs a rebuild. The candidate rating is captured in `changes.md`; invoke `PIPELINE FEEDBACK` to write the FAIL-verdict `13_Feedback.txt`. |
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
