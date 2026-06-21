# MCP Eval V3 — Operator Quick Reference

One task = one walk through this list.

---

## Setup once per task (one trigger does the folder + paths)

| Flow | Trigger | What it scaffolds |
|---|---|---|
| **CB** (you're authoring from scratch) | `PIPELINE NEW — <TASK_ID>` | empty `1/2/3` + `Agent_Responses/` + `trajectory-runs/` |
| **Review** (candidate-prefilled task) | `PIPELINE NEW REVIEW — <TASK_ID>` | empty `1/2/3/5/6/7/8` + the same folders |

`<TASK_ID>` is either the hex id alone (auto-picks next index) OR `<index>_<hex>` (uses given index). NEW prints exact paste paths + the next-trigger phrase (S0 for CB, REVIEW for review).

CB-mode files to paste:
- `1_Business_Function.txt` · `2_Persona.txt` · `3_UniverseDataForThisTask.json`

Review-mode files to paste (CB list + 4 more):
- `5_Prompt.txt` · `6_Oracle_Events.txt` · `7_Rubrics.json` · `8_Verifier_Fails.txt` (optional — only if candidate already ran trajectories)
- If candidate trajectories exist, drop the JSONs into `trajectory-runs/`. `parse_trajectories.py` will pick them up.

---

## The 7 mandatory commands (each in a NEW chat, in order)

```
PIPELINE S0       — Tasks/<TASK_DIR>
PIPELINE HARDNESS — Tasks/<TASK_DIR>
PIPELINE S1       — Tasks/<TASK_DIR>
```
↓ submit prompt to platform ↓
```
PIPELINE S2       — Tasks/<TASK_DIR>
PIPELINE S3       — Tasks/<TASK_DIR>
PIPELINE FINAL    — Tasks/<TASK_DIR>
```
↓ upload deliverables, run 6 trajectories on platform ↓
```
PIPELINE S4       — Tasks/<TASK_DIR>
```

Paste `8_Verifier_Fails.txt` into the task folder + 6 trajectories into `trajectory-runs/` (or `Agent_Responses/`) before S4.

---

## Closing the task

```
PIPELINE CLOSE — Tasks/<TASK_DIR>
```

Read-only audit. Refuses to greenlight unless required artifacts are present + FINAL verdict = PASS + (if trajectories) verdict = OK. Nudges to append any novel finding to `Tasks/_meta/Learnings.md` before exit.

---

## The 5 conditional commands

| When | Command |
|---|---|
| Platform linter blocked the prompt (CB-mode OR Review-mode where prompt is stuck) | `PIPELINE S1.5 — Tasks/<TASK_DIR>` + paste linter output. Review-mode routes the fix to scratch draft; CB-mode revises 5_Prompt.txt in place. S1.5 now runs `check_justification.py` on the pushback before allowing exit — pushbacks with internal terminology are blocked. |
| Platform paste-back rubrics suspected mutated | `PIPELINE COMPARE — Tasks/<TASK_DIR>` (after dropping `10_Rubrics_Platform.json`) |
| Task came prefilled (review-type, not CB) | See **Reviewer flow** below |
| Task came back failing difficulty (pass@1 > 40%) or density (< 40 tool calls) — REVIEW fix not enough, OR your own CB task came back too easy/thin | `PIPELINE REDO — Tasks/<TASK_DIR>` (archives candidate-original 5/6/7 + reviewer 14/15 to `_aux/Candidate_Originals/`, then runs full CB rebuild HARDNESS→S1→S2→S3→FINAL writing fresh 5/6/7) |
| Want an additional veteran second-opinion BEYOND the auto-fired per-phase AUDIT (pre-FINAL pre-upload sanity check, post-platform-rejection retro under maximum rigor, post-pipeline-change re-audit of a recently shipped task) | `PIPELINE AUDIT — Tasks/<TASK_DIR> --phase {prompt\|oe\|rubrics\|all}` — read-only re-verification in a fresh chat. Same strictest QC interpretation as the inline AUDIT (5/5 only, density bar 50+, every "should" read as "must"). Returns `PASS (STRICT)` / `REVISE` / `REBUILD`. Not a substitute for FINAL — complementary. **Note**: S1/S2/S3 already auto-fire AUDIT inline, so this on-demand trigger is for ADDITIONAL re-verification beyond the built-in per-phase gates. |

---

## Reviewer flow (task came prefilled with 5/6/7)

Paste the same 3 inputs (`1_Business_Function.txt`, `2_Persona.txt`, `3_UniverseDataForThisTask.json`) plus the candidate's prefilled `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json` into `Tasks/<TASK_DIR>/`. Then one new chat:

```
PIPELINE REVIEW — Tasks/<TASK_DIR>
```

What it does (single chat, runs the full review end-to-end):
- S0 setup (split, index, fact ledger, graph report)
- Validator on all 3 phases
- Council A grounding sweep on prompt + OE + rubrics
- Council B (5 perspectives × 5 lenses) on prompt + OE + rubrics
- **Final Council cross-artifact gate** (answer leakage, entity drift, lever regression — same gate the CB flow uses)
- **Hardness pre-assessment**: if `Agent_Responses/Run*.json` exist, compute measured `pass@1` + `avg_tool_calls`. Otherwise project from Council B-B3.
- Verifies every finding against the per-task universe before recording
- Writes `changes.md` (one row per confirmed finding, severity-tagged, status=Pending)
- Writes `13_Feedback.txt` (candidate-facing rating in plain narrative)
- Writes `_aux/Council_Reports/REVIEW_score.md` (per-phase QC scores)

**Binary triage outcome (the only if/else):**

| Verdict | Trigger | Action |
|---|---|---|
| **SALVAGEABLE** | prompt has no Major QC issues (or only minor cosmetic fixes) AND hardness OK (measured pass@1 ≤ 40% AND avg tool calls ≥ 40, OR projected density ≥ 40 + levers trigger + no answer leakage) | Fix OE + rubrics (+ minor prompt edits to scratch draft) via `changes.md`. Mark Applied → re-invoke REVIEW → emits 14/15. Originals stay pristine. |
| **REBUILD** | prompt fails Major QC dim OR hardness fails | Do NOT emit 14/15. `changes.md` + `13_Feedback.txt` still record everything for the rating. Invoke `PIPELINE REDO`. |

Originals stay pristine throughout. Same 4-layer defense (validator → Council A → Council B → FINAL) as the CB flow.

### Reviewer-specific: prompt stuck at platform linter (preferred over REDO)

If the candidate's prompt is blocked by the platform linter (any class: business function / data / similarity) so you can't get to the prefilled OE/rubrics, handle it FIRST before running REVIEW:

```
PIPELINE S1.5 — Tasks/<TASK_DIR>
<paste linter output>
```

S1.5 detects review-mode (presence of any REVIEW artifact in `_aux/`) and routes accordingly:
- **Push back (preferred)** — writes a 2-5 sentence justification to `_aux/Linter_Justifications.md` in your voice. You paste it back to the platform.
- **Minimal prompt fix** — writes the fix to `_aux/REVIEW_prompt_draft.txt` + Pending row in `changes.md`. Originals stay pristine. Validates the draft with same Fact_Ledger groundedness + Council A + B as a fresh S1 prompt.

Once the platform is unblocked, `PIPELINE REVIEW` proceeds normally with the scratch draft as the reference prompt.

---

## Mode flag

For critical deliverables (benchmark submission, redo of a rejected task): append `COUNCIL_MODE=multi` to S1 / S2 / S3 / FINAL triggers. Spawns 5 separate reviewer sub-agents + consensus instead of one 5-lens call. ~5× token spend, true model diversity.

---

## What each phase guarantees

- **S0** → universe split + fact ledger + graph report on disk
- **HARDNESS** → 3-5 levers picked, density projected ≥40 tool calls, stump hypothesis recorded. STOPs hard if insufficient.
- **S1 / S2 / S3** → drafts validated + Council A (grounding) + Council B (6 perspectives × 5 lenses, B6 catches upstream propagation issues) + **inline AUDIT (strict veteran second-opinion)**. All must GO. Each runbook starts with a `phase_ready.py` check that refuses to start if upstream artifacts are missing. **S1 additionally runs `calc_similarity.py` after Council B before AUDIT**: < 30 PASS, 30-39 WARN (logged), ≥ 40 STOP with Class B pivot mandatory (the 40% project ceiling — pivot using `Reference/Similarity_Pivot.md`).
- **FINAL** → cross-artifact check (answer leakage, entity drift, lever regression, integrated density). Mandatory before upload.
- **AUDIT** → auto-fires inline from S1/S2/S3 (and S1.5 on prompt revise, REVIEW on corrected materialization) as the per-phase strict-interpretation exit gate. Also invokable on-demand in a fresh chat via `PIPELINE AUDIT — Tasks/<TASK_DIR> --phase {prompt|oe|rubrics|all}` for high-stakes pre-upload sanity check, post-rejection retro, or post-pipeline-change re-audit. Strictest interpretation: 5/5 only (no NON-FAIL band), density bar 50+ (not 40), every "should" → "must". Read-only.
- **S4** → real `parse_trajectories.py` measurement of avg tool calls + pass@1 from the 6 platform runs you just pasted in. Each failing rubric classified Rubric-Invalid / Judge-Error / Legit-Fail. AF justifications written AND run through `check_justification.py` before ship.

## When trajectories appear

Trajectories are platform output. They don't exist until you upload + kick off the 6 runs.

| Phase | Are trajectories available? | What the pipeline uses |
|---|---|---|
| S0 / HARDNESS / S1 / S1.5 / S2 / S3 / FINAL | No (pre-upload) | Projected density + lever coverage + answer-leakage scan |
| S4 | Yes — you just pasted them in | Measured pass@1 + avg tool calls (`parse_trajectories.py`) |
| REDO | Yes (the failed trajectory is why REDO fired) | `_aux/REDO_reason.md` carries the failure numbers |
| REVIEW | Maybe — depends on whether the candidate already submitted to the platform | Measured if present, projected if not |

---

## Rules of the road

- **One phase = one fresh chat.** Never run two triggers in the same chat.
- **Paste nothing inside a phase chat** unless the trigger explicitly asks for it (S1.5 linter, S4 verifier fails).
- **If a phase STOPs with a stop reason** (insufficient levers, insufficient density, linter blocked, FINAL revise cap hit): you decide the next move. Do not ask the agent to "try anyway."
- **You never have to choose between universes, edit code, or write justifications.** The agent does all of it. Your job is paste-trigger-paste.

---

For the full mechanics: see [`AGENTS.md`](AGENTS.md) PIPELINE DISPATCH section + per-phase runbooks in `Reference/Sessions/`.
