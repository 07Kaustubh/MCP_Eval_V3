# Tasks/_meta — Cross-Task Learning Logs

Append-only logs that capture cross-task patterns. Each entry references one task; later phases mine these logs to avoid repeating mistakes and to calibrate hardness predictions.

## Files

| File | Written by | Captures |
|---|---|---|
| [Similarity_Log.md](Similarity_Log.md) | S1.5 (Class B) | Every 40%+ similarity hit: linter excerpt, matched-task reference, pivot levers used, outcome after resubmit |
| [Linter_Justifications.md](Linter_Justifications.md) | S1.5 (Class A) | Every justification sent back to the platform: full text, reviewer's decision (placeholder until known), reason if rejected |
| [Hardness_Patterns_Log.md](Hardness_Patterns_Log.md) | HARDNESS (predicted) + S4 (actual) | Per task: which 3-5 levers were selected, which rubrics Opus 4.8 actually failed |
| [Stump_Hypotheses.md](Stump_Hypotheses.md) | HARDNESS (predicted) + S4 (actual) | Per task: stump hypothesis predictions + actual AF rubrics + calibration delta |

## Append protocol

Each log uses a `## Entry — Tasks/<TASK_DIR> — <YYYY-MM-DD>` heading then a tight body. Do not edit prior entries in place — append a follow-up entry if a previous outcome changes.

## Why these matter

- **Similarity_Log** prevents re-pivoting against the same matched task with the same lever combination.
- **Linter_Justifications** builds a library of phrasings that the human reviewer accepted vs rejected.
- **Hardness_Patterns_Log** + **Stump_Hypotheses** calibrate the lever catalog. If a lever predicts well, lean on it; if it misses, downweight it for future tasks.

## When NOT to log

- Routine outcomes (linter passes first try, no similarity hit). Only log when there is a learning signal.
- Sensitive specifics beyond what is needed to teach future tasks (no full email contents, no PII).
