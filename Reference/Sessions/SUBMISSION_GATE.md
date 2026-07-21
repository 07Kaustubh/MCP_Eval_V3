# PIPELINE SUBMISSION_GATE — Session Runbook

**Trigger:** `PIPELINE SUBMISSION_GATE — Tasks/<TASK_DIR>`

**Universe:** StarPM (V4) only. This phase does not apply to Brookfield, Keystone, or MoveOps tasks.

**Position in pipeline:** Runs AFTER `PIPELINE FINAL` returns GO. It is the last check before platform upload. Zero tolerance — any single defect is a blocker.

---

## Purpose

Catch every defect pattern historically flagged by production auditors before the task reaches the platform. Where FINAL performs a holistic cross-artifact consistency review, SUBMISSION_GATE runs a targeted checklist of 6 canonical defect families across 32 documented failure patterns derived from the 158-task QC audit.

One failure in any family = task FAIL. The task does not upload until SUBMISSION_GATE returns PASS.

---

## Prerequisites

Before invoking, verify ALL of these are true:

- [ ] `5_Prompt.txt` is finalized (post-S1 + any S1.5 revisions)
- [ ] `6_Oracle_Events.txt` is finalized (post-S2)
- [ ] `7_Rubrics.json` is finalized (post-S3)
- [ ] `_aux/Council_Reports/FINAL_report.md` exists and contains `VERDICT: GO`
- [ ] `_aux/Universe.txt` contains `starpm`

If FINAL has not passed, STOP: `SUBMISSION_GATE BLOCKED: FINAL must return GO before SUBMISSION_GATE runs.`

---

## Required Inputs

| File | Role |
|---|---|
| `5_Prompt.txt` | Prompt — persona, scenario, all asks, entity references |
| `2_Persona.txt` | Role, authority, department |
| `1_Business_Function.txt` | Assigned business function |
| `6_Oracle_Events.txt` | Expected tool calls and parameters |
| `7_Rubrics.json` | All rubric items — primary target |
| `3_UniverseDataForThisTask.json` | Task-specific snapshot (use base + changelog as fallback) |
| `4_Changelog.json` | CB's change manifest |
| `StarPM_Base_Universe/Data/` | Base universe for entity verification |
| `StarPM_Base_Universe/7_Server_Tools_Details.json` | Tool inventory |
| `StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md` | Persona role boundaries |

---

## The 6 Defect Families

| # | Family | What it catches |
|---|---|---|
| F1 | Impossible-with-Tools | Rubrics demanding actions/data the toolset cannot provide |
| F2 | Persona & Date Mismatch | Persona attribution errors, date contradictions, phantom references |
| F3 | Process Rubric Violations | Rubrics crediting tool-calling motions instead of outcomes |
| F4 | Rubric Defects (Broken/Over-Strict) | Target data missing in universe, or valid paths wrongly penalized |
| F5 | Illegal Tool-Output Dependencies | Rubrics whose grading requires inspecting tool return values |
| F6 | QC-Pattern Compliance | Atomicity, coverage gaps, over-broad criteria, destination mismatch, blank fields |

---

## Execution

Invoke as a single `oracle` sub-agent with the full eval from `Evals_starpm/5_Submission_Gate_Eval.md`.

**Sub-agent prompt template:**

```
You are the SUBMISSION GATE EVALUATOR for a StarPM (V4) task.

TASK DIR: Tasks/<TASK_DIR>
EVAL SPEC: Evals_starpm/5_Submission_Gate_Eval.md
PROMPT: Tasks/<TASK_DIR>/5_Prompt.txt
PERSONA: Tasks/<TASK_DIR>/2_Persona.txt
BUSINESS FUNCTION: Tasks/<TASK_DIR>/1_Business_Function.txt
ORACLE EVENTS: Tasks/<TASK_DIR>/6_Oracle_Events.txt
RUBRICS: Tasks/<TASK_DIR>/7_Rubrics.json
UNIVERSE SNAPSHOT: Tasks/<TASK_DIR>/3_UniverseDataForThisTask.json
CHANGELOG: Tasks/<TASK_DIR>/4_Changelog.json
BASE UNIVERSE: StarPM_Base_Universe/Data/
TOOL CATALOG: StarPM_Base_Universe/7_Server_Tools_Details.json
PERSONA BRIEFS: StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md

TASK:
Execute every phase of the Submission Gate Eval (Phase 0 through Phase 7).
The mandatory TODO list in Phase 0 is a hard gate — create and track it.
Evaluate each rubric against all 6 defect families (F1-F6).
Save the full report to:
  Tasks/<TASK_DIR>/_aux/Council_Reports/SUBMISSION_GATE_report.md

Per-rubric findings table format:
  | Rubric # | Title (truncated) | F1 | F2 | F3 | F4 | F5 | F6 | Verdict |

Task-level checks table format:
  | Check | Family | Verdict | Note |

Final verdict:
  F1 Impossible-with-Tools: PASS / FAIL (<N> issues)
  F2 Persona & Date Mismatch: PASS / FAIL (<N> issues)
  F3 Process Rubric Violations: PASS / FAIL (<N> issues)
  F4 Rubric Defects: PASS / FAIL (<N> issues)
  F5 Illegal Tool-Output Dependencies: PASS / FAIL (<N> issues)
  F6 QC-Pattern Compliance: PASS / FAIL (<N> issues)
  OVERALL VERDICT: PASS / FAIL
  BLOCKER ISSUES: <numbered list, or "none">
```

---

## Exit Criteria

| Condition | Next step |
|---|---|
| Zero failures across F1-F6 | `SUBMISSION_GATE PASS. Task is cleared for platform upload.` |
| Any failure in any family | `SUBMISSION_GATE FAIL. Fix blocker(s) and re-run. Route: F1/F4/F5 → fix rubric at S3; F2 → fix prompt at S1 or persona at NEW; F3 → fix rubric at S3; F6 → fix at the phase owning the root cause.` |

**Re-run protocol after fixes:**
1. Apply fixes at the phase owning the root cause (not inline in SUBMISSION_GATE).
2. Re-run `PIPELINE FINAL` to confirm cross-artifact consistency holds.
3. Re-run `PIPELINE SUBMISSION_GATE` against the corrected artifacts.

---

## Output

`Tasks/<TASK_DIR>/_aux/Council_Reports/SUBMISSION_GATE_report.md`

Contains:
- Phase-by-phase findings (F1 through F6)
- Per-rubric findings table
- Task-level checks table
- Final family verdicts + overall PASS/FAIL
- Numbered blocker list with routing instruction per blocker

---

## How SUBMISSION_GATE fits in the full StarPM pipeline

```
PIPELINE INJECTION     — hard gate after universe injection
PIPELINE HARDNESS      — lever identification
PIPELINE S1            — prompt authoring
PIPELINE S2            — oracle events
PIPELINE S3            — rubrics
PIPELINE FINAL         — cross-artifact holistic review (must GO first)
PIPELINE SUBMISSION_GATE — this phase (zero-tolerance pre-upload check)
                        ← upload to platform if PASS
PIPELINE S4            — verifier fails (dual-model: Opus + Gemini)
PIPELINE CLOSE         — final sanity check
```
