# Guide

How-to docs and templates that operators reference. Stable per project version.

## Files

| File | Purpose |
|---|---|
| `How_To_Use_This_Eval.md` | Original CB-facing eval workflow doc. Useful background. The pipeline in this repo automates most of what this doc describes manually. |
| `Verifier_Fails_Template.txt` | Template for `8_Verifier_Fails.txt` in each task. Copy into `Tasks/<TASK_DIR>/` and paste raw "Run Detail" blocks for failing rubrics before running PIPELINE S4. |

## When to consult Guide

- First-time setup: read `How_To_Use_This_Eval.md` for the manual workflow background. Then use the pipeline triggers in root `AGENTS.md`.
- Verifier-fails handoff: open `Verifier_Fails_Template.txt`, copy into the task folder, paste the failures, then run `PIPELINE S4`.

## What changes here

Templates and how-tos change with the platform's verifier-fails output format. If the platform changes the "Run Detail" block shape, update `Verifier_Fails_Template.txt` and the related parsing in `Reference/Sessions/S4.md`.
