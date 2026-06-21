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
| `Docs/7_QC_Spec_Doc1.json`, `8_QC_Spec_Doc2.md` | QC scoring |

## Procedure

1. **Run S0 setup** (PersonaBrief, split_universe, build_universe_index). The review still needs the per-task universe split and index — they were not produced when the candidate wrote the deliverables.

2. **Run the full validator suite.**
   ```
   python Validators/validate.py --phase all --task Tasks/<TASK_DIR>
   ```
   Read all three reports. These are findings #1 onwards in `changes.md`.

3. **Run Council A — Grounding** against `5_Prompt.txt`, `6_Oracle_Events.txt`, and `7_Rubrics.json` in sequence. Every ungrounded concrete claim is a finding.

4. **Run Council B — Adversarial QC + Density + Hardness Preservation** against all three deliverables in sequence. Every QC sub-dim that scores < 5 is a finding (B1). Every adversarial alt-path hit (second valid reading, over-specific outcome) is a finding (B2). Projected tool-call count < 40 is a finding (B3). Any Hardness lever from the candidate's design that the deliverable fails to trigger is a finding (B4). Tool-name leak / phrasing violation is a finding (B5). See `Reference/Council_Protocol.md` for the full perspective definitions.

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

7. **Apply only fixes the user has marked Applied** in `changes.md`. Do NOT apply fixes unilaterally — the user is rating the original candidate; pre-applying fixes erases the evidence.

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

## Exit criteria

- `_aux/Universe_Split/` and `_aux/Universe_Index/` exist.
- `_aux/Validator_Reports/` populated.
- `_aux/Council_Reports/REVIEW_*.md` populated (one per phase).
- `changes.md` exists with every confirmed finding as a row.
- `_aux/Council_Reports/REVIEW_score.md` exists with per-phase QC scores.

## Next step

User reviews `changes.md`, marks each row Applied / Dismissed / Pending, and rates the original candidate. If the user asks to fix the deliverables, apply each Applied row in turn and re-run validators / councils to confirm clean.

## Bootstrap

Read root `AGENTS.md` first. Findings must be grounded in the per-task universe — base universe assumptions are stale. Severity follows the QC spec. Be conservative about flagging Minor issues that don't actually affect the score.
