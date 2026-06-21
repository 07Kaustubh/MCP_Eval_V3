# Reference

Format cards + lever catalog + session runbooks. The single source of "how things are done" in this pipeline. Every runbook bootstraps from here.

## Cards (read when drafting / reviewing a deliverable)

| File | When |
|---|---|
| [Hardness_Playbook.md](Hardness_Playbook.md) | S0/HARDNESS lever selection; before S1 prompt drafting |
| [Prompt_Format.md](Prompt_Format.md) | S1 (drafting), S1.5 (linter response), REVIEW (scoring) |
| [OE_Format.md](OE_Format.md) | S2 (drafting), REVIEW (scoring) |
| [Rubric_Format.md](Rubric_Format.md) | S3 (drafting), REVIEW (scoring) |
| [Similarity_Pivot.md](Similarity_Pivot.md) | S1.5 Class B (similarity ≥ 40%) |
| [Linter_Playbook.md](Linter_Playbook.md) | S1.5 Class A (misalignment); S4 (AF justifications). **Both linter justifications and AF justifications use the same strict style: concise, human, no em-dashes, no references to guides / specs / frameworks.** |
| [Council_Protocol.md](Council_Protocol.md) | Every phase that runs councils (S1, S2, S3, REVIEW) |
| [Strict_Convention_Inventory.json](Strict_Convention_Inventory.json) | Council A grounding sweeps; S3 rubric review. Allowed phrasings extracted from V3 reference rubrics. |
| [OE_Convention_Inventory.json](OE_Convention_Inventory.json) | Council A convention sweep on OEs; S2 OE review. Tool-usage frequencies + opening-phrase patterns + parameter traps extracted from V3 reference OEs. |

## Session runbooks (one per trigger phrase)

Each runbook is self-bootstrapping — a fresh chat reads it and executes without further context. See root `AGENTS.md` for the PIPELINE DISPATCH table mapping triggers to runbooks.

| File | Trigger phrase |
|---|---|
| [Sessions/S0.md](Sessions/S0.md) | `PIPELINE S0 — Tasks/<TASK_DIR>` |
| [Sessions/HARDNESS.md](Sessions/HARDNESS.md) | `PIPELINE HARDNESS — Tasks/<TASK_DIR>` |
| [Sessions/S1.md](Sessions/S1.md) | `PIPELINE S1 — Tasks/<TASK_DIR>` |
| [Sessions/S1.5.md](Sessions/S1.5.md) | `PIPELINE S1.5 — Tasks/<TASK_DIR>` + linter paste |
| [Sessions/S2.md](Sessions/S2.md) | `PIPELINE S2 — Tasks/<TASK_DIR>` |
| [Sessions/S3.md](Sessions/S3.md) | `PIPELINE S3 — Tasks/<TASK_DIR>` |
| [Sessions/S4.md](Sessions/S4.md) | `PIPELINE S4 — Tasks/<TASK_DIR>` + verifier-fails paste |
| [Sessions/FINAL.md](Sessions/FINAL.md) | `PIPELINE FINAL — Tasks/<TASK_DIR>` (cross-artifact holistic council, required before platform upload) |
| [Sessions/REVIEW.md](Sessions/REVIEW.md) | `PIPELINE REVIEW — Tasks/<TASK_DIR>` |
| [Sessions/REDO.md](Sessions/REDO.md) | `PIPELINE REDO — Tasks/<TASK_DIR>` (reviewer redo: trajectory failed on difficulty / density, rebuild from scratch as CB) |
| [Sessions/COMPARE.md](Sessions/COMPARE.md) | `PIPELINE COMPARE — Tasks/<TASK_DIR>` (diff local rubrics vs platform paste-back) |

## Update protocol

- `Strict_Convention_Inventory.json` is extracted from `QC_Tasks/V3_Tasks/Task11..Task14/Rubrics.json`. Regenerate when new V3 reference tasks are added.
- `OE_Convention_Inventory.json` is extracted from `QC_Tasks/V3_Tasks/Task11..Task14/Oracle_Events.txt`. Regenerate when new V3 reference tasks are added.
- Cards change only when the QC spec changes. Cite the QC spec sub-dim in any update.
- Runbooks should remain copy-paste-stable across tasks. If a runbook needs per-task customization, add a `<TASK_DIR>` placeholder.
