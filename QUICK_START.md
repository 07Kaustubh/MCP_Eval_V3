# MCP Eval V3 — Operator Quick Reference

One task = one walk through this list.

---

## Setup once per task

Paste these 3 files into `Tasks/<TASK_DIR>/`:
- `1_Business_Function.txt`
- `2_Persona.txt`
- `3_UniverseDataForThisTask.json`

---

## The 6 mandatory commands (each in a NEW chat, in order)

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

Paste `8_Verifier_Fails.txt` + 6 trajectory JSONs into `Agent_Responses/` before S4.

---

## The 3 conditional commands

| When | Command |
|---|---|
| Platform linter blocked the prompt | `PIPELINE S1.5 — Tasks/<TASK_DIR>` + paste linter output |
| Platform paste-back rubrics suspected mutated | `PIPELINE COMPARE — Tasks/<TASK_DIR>` (after dropping `10_Rubrics_Platform.json`) |
| Task came prefilled (review-type, not CB) | `PIPELINE REVIEW — Tasks/<TASK_DIR>` instead of S0→S3 |

---

## Mode flag

For critical deliverables (benchmark submission, redo of a rejected task): append `COUNCIL_MODE=multi` to S1 / S2 / S3 / FINAL triggers. Spawns 5 separate reviewer sub-agents + consensus instead of one 5-lens call. ~5× token spend, true model diversity.

---

## What each phase guarantees

- **S0** → universe split + fact ledger + graph report on disk
- **HARDNESS** → 3-5 levers picked, density projected ≥40 tool calls, stump hypothesis recorded. STOPs hard if insufficient.
- **S1 / S2 / S3** → drafts validated + Council A (grounding) + Council B (5 perspectives × 5 lenses). Both must GO.
- **FINAL** → cross-artifact check (answer leakage, entity drift, lever regression, integrated density). Mandatory before upload.
- **S4** → each failing rubric classified Rubric-Invalid / Judge-Error / Legit-Fail. AF justifications written.

---

## Rules of the road

- **One phase = one fresh chat.** Never run two triggers in the same chat.
- **Paste nothing inside a phase chat** unless the trigger explicitly asks for it (S1.5 linter, S4 verifier fails).
- **If a phase STOPs with a stop reason** (insufficient levers, insufficient density, linter blocked, FINAL revise cap hit): you decide the next move. Do not ask the agent to "try anyway."
- **You never have to choose between universes, edit code, or write justifications.** The agent does all of it. Your job is paste-trigger-paste.

---

For the full mechanics: see [`AGENTS.md`](AGENTS.md) PIPELINE DISPATCH section + per-phase runbooks in `Reference/Sessions/`.
