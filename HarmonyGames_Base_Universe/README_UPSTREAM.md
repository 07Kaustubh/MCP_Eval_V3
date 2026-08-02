# HarmonyGames MCP Evaluation Corpus

This repository contains the HarmonyGames universe, task templates, evaluation
playbooks, and QC calibration examples used by Original Conference. It is a
documentation-and-artifact corpus, not a runnable application: evaluation is
performed manually in Cursor against a populated task folder.

## Start here

- **Author or revise a task:** read
  [`Docs/1_Project_Instructions_Overall.md`](Docs/1_Project_Instructions_Overall.md).
- **Run the evaluation workflow:** follow
  [`Guide/How_To_Use_This_Eval.md`](Guide/How_To_Use_This_Eval.md).
- **Understand the documentation set:** use
  [`Docs/README.md`](Docs/README.md).
- **Apply persona read visibility:** use
  [`Docs/15_Persona_ACL.md`](Docs/15_Persona_ACL.md) and the exact
  [`Persona_ACL_Roster.json`](HarmonyGames_Base_Universe/Persona_ACL_Roster.json).
- **Create a working task:** copy [`Tasks_Template/`](Tasks_Template/) into
  `Generated_Tasks/<task-name>/`.
- **Calibrate against completed examples:** browse [`QC_Tasks/`](QC_Tasks/).
  Do not use that directory for in-progress tasks.

## Repository map

- [`Docs/`](Docs/) — authoring rules, QC specifications, and specialist guidance.
- [`Guide/`](Guide/) — the operational, copy-paste evaluator runbook.
- [`Evals/`](Evals/) — six ordered evaluator playbooks (`0` through `5`).
- [`HarmonyGames_Base_Universe/Tool_Access/`](HarmonyGames_Base_Universe/Tool_Access/) — authoritative MCP capabilities, tool names,
  and parameters.
- [`HarmonyGames_Base_Universe/`](HarmonyGames_Base_Universe/) — universe
  narrative, persona ACL roster, schema, exports, and service data.
- [`Tasks_Template/`](Tasks_Template/) — canonical task artifact scaffold.
- [`Generated_Tasks/`](Generated_Tasks/) — local workspace for tasks under
  development or evaluation.
- [`QC_Tasks/`](QC_Tasks/) — completed QC calibration examples.
- [`QC_Tasks_Archive/`](QC_Tasks_Archive/) — legacy examples from other
  universes; not HarmonyGames ground truth.

## Authority order

When sources disagree, use this order:

1. `HarmonyGames_Base_Universe/Tool_Access/*.json` for service capabilities, available tools, and
   parameters.
2. `Docs/15_Persona_ACL.md` and
   `HarmonyGames_Base_Universe/Persona_ACL_Roster.json` for task-visible
   identity and persona-scoped read visibility.
3. `HarmonyGames_Base_Universe/Services_Data/`, the task's
   `4_Changelog.json`, `9_Universe_inject.sql`, and
   `HarmonyGames_Base_Universe/6_Universe_Schema.json` for live task/universe
   facts and database structure.
4. The prompt and any live, uniquely discoverable source it validly
   incorporates for the requested work.
5. `Evals/*.md` for current procedures and repository-level policy overrides,
   plus `Docs/7_QC_Spec_Doc1.json` and `Docs/8_QC_Spec_Doc2.md` for scored QC
   dimensions and their interpretation.
6. The remaining authoring guides and QC examples for explanation and
   calibration.

The fixed universe date is **February 28, 2026 (America/Chicago)**. The active
injection window is **January 1 through February 28, 2026**.
