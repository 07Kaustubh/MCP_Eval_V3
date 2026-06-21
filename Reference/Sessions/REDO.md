# PIPELINE REDO — Reviewer Redo as Full CB Build

**Trigger:** `PIPELINE REDO — Tasks/<TASK_DIR>`

**When to run:** REVIEW already ran, fixes were applied to `14_Updated_Oracle_Events.txt` and/or `15_Updated_Rubrics.json`, the corrected version was uploaded to the platform, 6 trajectories ran — and the task failed on **difficulty** (pass@1 > 40%) or **density** (average tool calls < 40). The candidate's structural design is unsalvageable. The reviewer has to rebuild from scratch like a CB.

This is also the trigger when a CB's own task came back failing density / difficulty and needs to be rewritten end-to-end.

## What it does

1. **Archives the candidate-original artifacts** so the rating evidence is preserved.
2. **Re-runs the full CB pipeline** (HARDNESS → S1 → S2 → S3 → FINAL) writing fresh 5/6/7.
3. **Locks in the candidate rating as FAIL** with the difficulty/density reason in `13_Feedback.txt`.

## Required inputs

| File | Source |
|---|---|
| `Tasks/<TASK_DIR>/5_Prompt.txt` | candidate's original prompt (was being reviewed) |
| `Tasks/<TASK_DIR>/6_Oracle_Events.txt` | candidate's original OEs |
| `Tasks/<TASK_DIR>/7_Rubrics.json` | candidate's original rubrics |
| `Tasks/<TASK_DIR>/14_Updated_Oracle_Events.txt` (if present) | reviewer's corrected OEs that still failed |
| `Tasks/<TASK_DIR>/15_Updated_Rubrics.json` (if present) | reviewer's corrected rubrics that still failed |
| `Tasks/<TASK_DIR>/Agent_Responses/Run*.json` | trajectories proving the difficulty / density failure |
| `Tasks/<TASK_DIR>/_aux/Universe_Split/`, `_aux/Universe_Index/`, `_aux/Fact_Ledger.json`, `_aux/Universe_Index/graph_report.md` | all present from REVIEW's S0 run |

If `_aux/` artifacts are missing (CB redo flow with no prior REVIEW): run `PIPELINE S0` first.

## Phase-readiness gate (run FIRST)

```
python Validators/phase_ready.py --phase redo --task Tasks/<TASK_DIR>
```

Refuses if upstream artifacts are missing. If it STOPs, run the upstream phase first.

## Procedure

1. **Confirm the failure reason** from the trajectories:
   - Compute `pass@1 = (runs that passed all rubrics) / 6`. If > 0.4 → difficulty fail.
   - Compute average tool calls across the 6 runs. If < 40 → density fail.
   - If neither failed but FINAL had a BLOCKER that couldn't be patched in 3 REVISE rounds → also redo territory.
   - Document which one(s) in `_aux/REDO_reason.md`: file paths, computed numbers, one-paragraph explanation.

2. **Archive the candidate-original + reviewer-corrected artifacts** to `Tasks/<TASK_DIR>/_aux/Candidate_Originals/`:
   ```
   cp 5_Prompt.txt _aux/Candidate_Originals/5_Prompt.txt
   cp 6_Oracle_Events.txt _aux/Candidate_Originals/6_Oracle_Events.txt
   cp 7_Rubrics.json _aux/Candidate_Originals/7_Rubrics.json
   cp 14_Updated_Oracle_Events.txt _aux/Candidate_Originals/14_Updated_Oracle_Events.txt   # if present
   cp 15_Updated_Rubrics.json _aux/Candidate_Originals/15_Updated_Rubrics.json              # if present
   cp changes.md _aux/Candidate_Originals/changes.md                                        # if present
   cp 13_Feedback.txt _aux/Candidate_Originals/13_Feedback.txt                              # if present
   ```
   These stay forever — they are the rating evidence.

3. **Clear the in-place artifacts.** Delete the top-level `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json`, `14_Updated_Oracle_Events.txt`, `15_Updated_Rubrics.json`, `changes.md`. The CB flow about to run will write fresh 5/6/7.

   Do NOT delete `_aux/` (the S0 outputs are still good — same per-task universe).

4. **Update `13_Feedback.txt`** to the candidate-facing FAIL rating. Use this template, plain narrative, no em-dashes, no guide references:

   ```
   Overall: FAIL on difficulty/density (worst dimension: <pass@1=X.XX | avg_tool_calls=YY>).

   What this means
   The task as submitted (with the reviewer's corrections applied) ran 6 trajectories on the
   platform. <pass@1 was X.XX, above the 40% ceiling | average tool calls were YY, below the
   40 floor>. The corrections fixed surface-level QC issues but the underlying scenario
   <was not hard enough for Opus 4.8 | did not exercise enough services to hit the call-count
   target>. The task has been rebuilt from scratch.

   What was retained
   - The per-task universe (3_UniverseDataForThisTask.json) is unchanged.
   - The persona and business function assignment are unchanged.
   - The originals (5/6/7), reviewer fixes (14/15), and changes.md are archived under
     _aux/Candidate_Originals/ for the rating record.
   ```

5. **Run the CB build sequence** in fresh chats:
   ```
   PIPELINE HARDNESS — Tasks/<TASK_DIR>
   PIPELINE S1       — Tasks/<TASK_DIR>
   PIPELINE S2       — Tasks/<TASK_DIR>
   PIPELINE S3       — Tasks/<TASK_DIR>
   PIPELINE FINAL    — Tasks/<TASK_DIR>
   ```
   HARDNESS will read the new Learnings.md entry (you should append one — see step 7) plus the candidate's failure mode from `_aux/REDO_reason.md` so the new build addresses the specific gap.

6. **Re-upload to the platform.** Run 6 trajectories. Verify pass@1 ≤ 0.4 AND average tool calls ≥ 40. If either fails again, repeat REDO with a different lever combination.

7. **Append a new finding to `Tasks/_meta/Learnings.md`.** Document why the candidate's design failed difficulty / density and what the new lever combination did to fix it. This is the highest-value cross-task learning — capturing the redo prevents repeating it.

## Exit criteria

- `_aux/Candidate_Originals/` populated with every artifact the candidate produced + reviewer corrected.
- `_aux/REDO_reason.md` documents the failure (pass@1 or tool-call count) with trajectory references.
- New `5/6/7` exist as fresh CB output (validator + Council A + B + FINAL all GO).
- `13_Feedback.txt` is the FAIL rating with the specific reason.
- Optional but encouraged: new `Tasks/_meta/Learnings.md` entry numbered L<n>.

## STOP gate

This phase ends here after the archive + clear + feedback-update steps. End your response. The user opens fresh chats for each step of the CB rebuild:

```
PIPELINE HARDNESS — Tasks/<TASK_DIR>
PIPELINE S1       — Tasks/<TASK_DIR>
PIPELINE S2       — Tasks/<TASK_DIR>
PIPELINE S3       — Tasks/<TASK_DIR>
PIPELINE FINAL    — Tasks/<TASK_DIR>
```

Do NOT chain those phases inside the REDO chat. Each must be a fresh chat — the fresh-chat-per-phase contract is what keeps each phase decision-clean.

**If the user pastes follow-up content in this chat** (HARDNESS inputs, S1 / S2 / S3 inputs, a new task, fix attempts on a different deliverable, or an unrelated question), do NOT process it. Reply: "This chat is single-shot for the REDO archive + clear + feedback pass. Please open a fresh chat and invoke the appropriate next trigger from the dispatch table." Chaining inside one chat defeats the entire pipeline.

## Bootstrap

Read root `AGENTS.md` first. REDO is destructive of the in-place 5/6/7 — always archive before clearing. The candidate-rating evidence is the originals, not the rebuilt deliverable.
