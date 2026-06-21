# PIPELINE COMPARE — Runbook

**Trigger:** `PIPELINE COMPARE — Tasks/<TASK_DIR>`

**When to use:** After uploading `7_Rubrics.json` to the platform and pasting the platform's copy back as `10_Rubrics_Platform.json`. Catches silent platform-side mutations (reformatting, field stripping, reordering).

## Inputs

- `Tasks/<TASK_DIR>/7_Rubrics.json` — local rubrics shipped to platform
- `Tasks/<TASK_DIR>/10_Rubrics_Platform.json` — paste-back from platform's rubric editor

If `10_Rubrics_Platform.json` is missing, ask the user to paste it.

## Phase-readiness gate (run FIRST)

```
python Validators/phase_ready.py --phase compare --task Tasks/<TASK_DIR>
```

Refuses if upstream artifacts are missing. If it STOPs, run the upstream phase first.

## Steps

1. Run the comparator:

```bash
python3 Validators/compare_rubrics.py \
  Tasks/<TASK_DIR>/7_Rubrics.json \
  Tasks/<TASK_DIR>/10_Rubrics_Platform.json
```

2. Read the output. Three outcomes:

| Output | Action |
|---|---|
| `Rubrics match.` | Done. Note in summary that platform did not mutate. |
| `COUNT MISMATCH: local=N platform=M` | Platform dropped or duplicated rubrics. Inspect which indices are missing. If platform stripped any, re-upload. If platform added any, investigate (rare). |
| `[N] <field> differs` (per index) | Platform mutated a field. For each diff, decide: (a) accept platform's version if it's a benign reformat (capitalization, trailing whitespace), or (b) re-upload from local if the mutation changed meaning. |

3. If any diff changed meaning, treat as a regression: update `_aux/Council_Reports/COMPARE_diff.md` with the diff list and re-run S3 Council A on the affected rubrics.

## Exit

- Match → done.
- Mismatch → user decides accept-platform vs re-upload-local, per diff.

## Outputs

- stdout: per-diff report
- `_aux/Council_Reports/COMPARE_diff.md` (only if diffs found): summary + per-rubric decision (accept | re-upload | re-author)

## STOP gate

This phase ends here. End your response.

Two next-trigger paths:
- Match → no further action; continue with the regular flow (`PIPELINE S4 — Tasks/<TASK_DIR>` once trajectories are back).
- Mismatch → user decides accept-platform vs re-upload-local per diff. If re-upload is chosen, the user resubmits to the platform, then re-invokes `PIPELINE COMPARE — Tasks/<TASK_DIR>` in a fresh chat to verify the paste-back is now clean.

Do NOT chain to S4 or other phases inside this chat.
