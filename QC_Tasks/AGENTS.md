# QC_Tasks

Reference tasks that have already passed QC. Two cohorts with very different treatment.

## V3_Tasks — primary reference (on-framework)

`V3_Tasks/Task11..Task14` are on-framework tasks built against the **Brookfield universe**, using the **V3 rubric framework** (Outcome / Process only). They are the canonical reference for:

- prompt voice and structure
- OE numbered-prose format
- rubric phrasing patterns and the use of `(or similar)` / `approximately`
- write-action diversity

**Read every V3 task's `Rubrics.json` before writing rubrics in S3.** The convention inventory in `Reference/Strict_Convention_Inventory.json` is auto-extractable from these 4 files — if new V3 tasks are added, regenerate the inventory.

Each task folder has 5 files:

| File | Purpose |
|---|---|
| `Prompt.txt` | Reference prompt |
| `Oracle_Events.txt` | Reference OE |
| `Rubrics.json` | Reference rubrics (all 4 tasks combined have 59 rubrics, 100% outcome, 0 process) |
| `Quality_Scores.json` | Per-dim QC scores the task earned |
| `Task_Info.json` | Metadata |

## V2_Tasks — craft reference only (off-framework universe + framework)

`V2_Tasks/Task1..Task10` are pre-V3 tasks built against the **Keystone Mortgage universe** using the V2 rubric framework (TS / QC / Outcome). They are useful for studying:

- prompt craft (voice, structure, naturalness)
- OE composition

They are NOT useful for:

- the V3 rubric framework (TS / QC do not exist in V3)
- the Brookfield universe (Keystone is a different universe with different personas / systems)
- any concrete value (the data is from a different universe)

**Apply V3 framework rules when learning from V2 tasks. Do not import V2 rubric structures.**

## Labeled QC verdict corpora (bucket ground truth)

Four labeled corpora are the acceptance ground truth for `Validators/qc_verdict.py` (the deterministic QC verdict engine). Each holds tasks split into 4 buckets - `QC_Passed`, `QC_True_Fails`, `QC_Non_Fails`, `QC_False_Fails_PT_Dispute_Accepted` - with a `QC_Feedback_Verdict.txt` per task (plus the `9_QC_Feedback` / `10_PT_Dispute_To_QC_Feedback` / `11_Final_QC_Validation_On_PT_Dispute` trio on disputed tasks).

| Corpus | Universe | Tasks |
|---|---|---|
| `V3_Buckets/` | Brookfield (V3) | 16 |
| `V3.1_Buckets/` | KeyStone (V3.1) | 16 |
| `V2.1_Buckets/` | MoveOps (V2.1) | 80 |
| `V4_Tasks/` | StarPM (V4) | 16 |

`python3 Validators/qc_verdict.py selftest QC_Tasks/<corpus>` classifies every task from parsed CONTENT (scores + dispute resolution), never the directory name, and must stay bucket-correct 128/128 across all four. These are the QC-verdict SSOT; the `V3_Tasks/` + `V2_Tasks/` cohorts above are craft references only, not verdict ground truth.

## When to consult

- **S3 (Rubrics):** read every V3 `Rubrics.json` in full. Study V2 only for variety in prompt-to-OE mapping styles.
- **S1 (Prompt):** read at least 2 V3 `Prompt.txt` for the persona-voice register against Brookfield-style situations.
- **S2 (OE):** read at least 2 V3 `Oracle_Events.txt` for the numbered-prose format and tool-name discipline.
- **REVIEW:** consult V3 reference scores in `Quality_Scores.json` for what a 5/5 deliverable looks like dimensionally.

## Adding a new reference task

If a future task scores 5/5 across all dimensions, copy it here as `V3_Tasks/Task<n>_<id>/` and regenerate `Reference/Strict_Convention_Inventory.json` so the convention inventory captures any new phrasings.
