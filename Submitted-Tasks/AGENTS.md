# Submitted-Tasks

Archive of shipped tasks. One subdirectory per task. The **active** task lives in a folder at the repo root (e.g. `Task99-6a33cbf80d154de5ec83ab5a`); move its folder here after it ships. Naming convention: `<index>_<platform-task-id>` (e.g., `23_6a347770af5b452cf30b0fa0`) or `Task<n>_<id>_<suffix>` for legacy entries.

## Per-task folder schema

```
<TASK_DIR>/
├── 1_Business_Function.txt        # user-pasted
├── 2_Persona.txt                  # user-pasted
├── 3_UniverseDataForThisTask.json # user-pasted (per-task pgweb export, single source of truth)
├── PersonaBrief.txt               # S0 produces from 2_Persona_Briefs.md
├── 4_Changelog.json               # optional, user-pasted if exists
├── 5_Prompt.txt                   # S1 produces
├── 6_Oracle_Events.txt            # S2 produces
├── 7_Rubrics.json                 # S3 produces
├── 8_Verifier_Fails.txt           # user-pasted after agent runs (S4 input)
├── 9_Universe_inject.sql          # optional, user-pasted if exists
├── changes.md                     # REVIEW-only — tracks findings on existing deliverables
├── Agent_Responses/               # user-pasted per-run trajectories (S4 input)
│   └── Run{1..6}_Trajectory.json
└── _aux/                          # pipeline working dir (gitignore-friendly)
    ├── data_hash.txt              # sha256 of 3_UniverseDataForThisTask.json
    ├── Universe_Split/            # split_universe.py output (per-task; no cross-task collisions)
    ├── Universe_Index/            # build_universe_index.py output (fast lookups)
    ├── S0_Setup_Report.md         # S0 summary
    ├── Hardness_Plan.md           # HARDNESS output (levers + stump hypothesis)
    ├── Linter_Decision.md         # S1.5 output (one per linter round)
    ├── Linter_Justifications.md   # S1.5 output (only for Class A pushbacks)
    ├── Council_Reports/           # one report per phase per council
    │   ├── S1_A_grounding.md ... S4_verdict.md
    ├── Validator_Reports/         # validate.py output per phase
    │   ├── prompt.md  oe.md  rubrics.md
    └── Reasoning/                 # internal narrative
        ├── prompt_design.md
        ├── OE_solvability.md
        └── Rubric_Coverage_Matrix.md
```

## Workflow entry points

| Scenario | Trigger phrase |
|---|---|
| New task (creation mode) | `PIPELINE S0 — <TASK_DIR>` then S0 → HARDNESS → S1 → (S1.5 as needed) → S2 → S3 → S4 |
| Review-type task | `PIPELINE REVIEW — <TASK_DIR>` |
| Linter blocked the prompt | `PIPELINE S1.5 — <TASK_DIR>` + paste the linter output |
| Verifier results came back | `PIPELINE S4 — <TASK_DIR>` + paste verifier fails |

See root `AGENTS.md` for the full dispatch table.

## Cross-task learning

`Submitted-Tasks/_meta/` holds cross-task logs that feed back into hardness calibration, linter justification reuse, similarity-pivot decisions. See [Submitted-Tasks/_meta/AGENTS.md](_meta/AGENTS.md).

## Conventions

- `_aux/` is per-task working state. Safe to delete and rebuild from inputs.
- The 4 user-pasted inputs (`1_*`, `2_*`, `3_*`, plus the verifier-fails and trajectories after agent runs) are the only files the user supplies. Everything else the pipeline produces.
- Never commit `_aux/Universe_Split/` to git in a large team — it can be GBs across many tasks. Per-task gitignore recommended.
