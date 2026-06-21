# Changelog

All notable changes to the MCP Eval V3 automated pipeline. Newest first.

## 2026-06-21 — v2: Tool-Call Density Gate + OE Inventory + Multi-Perspective Councils

Improvements driven by the parity-review pass against the original requirements. Focus: harden the 40+ tool-call baseline, codify OE conventions, and make council coverage explicit per perspective.

### Added

- **`Reference/OE_Convention_Inventory.json`** — auto-extracted from V3 reference OE files. Captures 36 tool-usage frequencies, 9 parameter patterns, opening-phrase shapes, parameter traps, and anti-patterns. Council A's convention sweep on OE phase reads this.
- **Hard rule #11 in root AGENTS.md** — 40+ tool-call average is the maximalism floor. Enforced by two independent gates (HARDNESS phase projection + Council B-B3 adversarial).
- **`Hardness_Plan.md` density projection section** — every HARDNESS run emits a tool-call density estimate. `< 40` returns `INSUFFICIENT_DENSITY` and stops the pipeline.
- **Per-lever tool-call cost column in `Reference/Hardness_Playbook.md`** — each of the 11 levers carries a cost range so the projection is mechanical.
- **Council B-B3 (tool-call density adversarial)** — Council B now sketches the trajectory a competent Opus 4.8 agent would take, counts tool calls, and blocks the deliverable if the sketch produces < 40.
- **Council B-B4 (hardness preservation)** — Council B verifies every lever selected in HARDNESS still triggers in the deliverable. Lost lever = `HARDNESS_REGRESSION` block.
- **`Prompt_Guidelines.md` programmatic cross-check** — validator warns on QC-sample clichés, over-signaling investigation phrasing, generic urgency framing.
- **OE step-count + opening-verb checks** — validator warns when OE list has < 8 steps or < 60% of lines start with an action verb (V3 references run 11-28 OEs with consistent action-first openings).
- **`data.py` smart forwarder** — routes per-task input to `Validators/split_universe.py`. Original behavior preserved in `data.legacy.py`. Refuses non-per-task paths with a clear pointer.
- **`CHANGELOG.md`** (this file) — append-only history.

### Changed

- **`Reference/Council_Protocol.md`** — fully rewritten. Council A enumerated as A1 (Grounding) + A2 (Convention). Council B enumerated as B1 (QC sub-dim scoring) + B2 (Adversarial alt-path) + B3 (Tool-call density) + B4 (Hardness preservation) + B5 (Tool-leak / phrasing scan). Same two sub-agent calls per phase, full perspective coverage.
- **`Reference/Sessions/HARDNESS.md`** — added 6-section Hardness_Plan template with explicit Tool-Call Density Projection section + `INSUFFICIENT_LEVERS` / `INSUFFICIENT_DENSITY` gates.
- **`Reference/Sessions/S1.md`, `S2.md`, `S3.md`** — exit criteria now name B3 (≥40 projected tool calls) and B4 (hardness preservation) explicitly.
- **`Reference/AGENTS.md`** — references OE_Convention_Inventory.json.
- **`Validators/validate.py`** — dollar-amount groundedness sweep now tries `34495.06`, `34495`, `34495.0`, and `34,495.06` variants. Removes formatted-amount false-positives. New prompt anti-pattern checks. New OE step-count + opening-verb checks.
- **`Validators/AGENTS.md`** — refreshed check list per phase.
- **Root `AGENTS.md`** — added hard rule #11 (40+ floor), added "supersedes `command workflow.txt`" note under PIPELINE DISPATCH, updated `data.py` guidance (smart forwarder, not forbidden).

### Renamed

- **`data.py` → `data.legacy.py`** (the original script that writes to the shared `Brookfield_Base_Universe/Data/`). A new `data.py` replaces it as a smart forwarder.

### Validator smoke-test on task 23 (after this round)

```
[PASS] prompt:  0 fails, 0 warns, 2 notes
[PASS] oe:      0 fails, 0 warns, 1 notes
[PASS] rubrics: 0 fails, 0 warns, 1 notes
```

Down from 3 warns (dollar-amount false-positives) in v1.

---

## 2026-06-21 — v1: Initial Pipeline Build

First-pass automated pipeline supplanting the manual `command workflow.txt` workflow. Built end-to-end from the user's verbal spec.

### Added — Validators (3 scripts)

- **`Validators/split_universe.py`** — patched `data.py` wrapper. Writes the per-task universe split into `Tasks/<TASK_DIR>/_aux/Universe_Split/` instead of the shared `Brookfield_Base_Universe/Data/`. Prevents cross-task collisions.
- **`Validators/build_universe_index.py`** — builds quick lookup summaries from `_aux/Universe_Split/` (service_inventory.md, entities_personas.md, key_facts.md, today_horizon.json, accounts_per_entity.md). Parses `row_data` JSON-encoded strings correctly.
- **`Validators/validate.py`** — phase-aware validator. Supports both nested (`{annotations: {...}}`) and flat (`{evidence, justification, category}`) rubric schemas. Exits non-zero on any FAIL.

### Added — Reference (7 cards + 1 inventory)

- **`Reference/Hardness_Playbook.md`** — 11-lever Opus-4.8-specific catalog with hard-tip provenance.
- **`Reference/Prompt_Format.md`** — voice, anti-patterns, 500-word cap.
- **`Reference/OE_Format.md`** — numbered-prose template + parameter traps.
- **`Reference/Rubric_Format.md`** — V3 schema (nested + flat) + verbatim patterns extracted from V3 references.
- **`Reference/Similarity_Pivot.md`** — 6-lever menu for ≥40% similarity blocker.
- **`Reference/Linter_Playbook.md`** — strict justification style (concise, human, no em-dashes, no references to guides) + AF justification template with 2 examples.
- **`Reference/Council_Protocol.md`** — verbatim sub-agent prompt templates for Council A (Grounding) + Council B (Adversarial-QC).
- **`Reference/Strict_Convention_Inventory.json`** — extracted from `QC_Tasks/V3_Tasks/Task11..Task14/Rubrics.json`. Allowed phrasings, evidence-field shapes, "(or similar)" usage rules.

### Added — Session Runbooks (8 files)

- **`Reference/Sessions/S0.md`** — PersonaBrief extract + universe split + index build.
- **`Reference/Sessions/HARDNESS.md`** — lever scan + stump hypothesis.
- **`Reference/Sessions/S1.md`** — prompt drafting + validator + 2 councils.
- **`Reference/Sessions/S1.5.md`** — linter blocker handler (Class A misalignment + Class B similarity ≥40%).
- **`Reference/Sessions/S2.md`** — Oracle Events drafting + validator + 2 councils.
- **`Reference/Sessions/S3.md`** — Rubrics drafting + validator + 2 councils (heaviest pass).
- **`Reference/Sessions/S4.md`** — verifier-fails classification (Rubric-Invalid / Judge-Error / Legit-Fail) + AF justifications.
- **`Reference/Sessions/REVIEW.md`** — review-type task intake + `changes.md` initialization.

### Added — Cross-task learning (`Tasks/_meta/`)

- **`Similarity_Log.md`** — per-task pivot history.
- **`Linter_Justifications.md`** — justification history with reviewer outcomes.
- **`Hardness_Patterns_Log.md`** — lever selection vs actual failure calibration.
- **`Stump_Hypotheses.md`** — predicted vs actual AF rubrics with calibration delta.

### Added — AGENTS.md hierarchy (25 files)

- Root + Brookfield_Base_Universe + Brookfield_Base_Universe/Data + 13 per-service + 9 infrastructure (Docs, Evals, Guide, QC_Tasks, Reference, Tasks, Tasks/_meta, Tasks_Template, Validators).
- All carry the staleness warning where applicable: per-task `3_UniverseDataForThisTask.json` is the only source of truth; base universe is stale except `8_Server_Tools_Details.json` and persona briefs.

### Pipeline contract

8 trigger phrases (`PIPELINE S0`, `HARDNESS`, `S1`, `S1.5`, `S2`, `S3`, `S4`, `REVIEW`). Each runs in a fresh chat with zero prior context. Find-replace `<TASK_DIR>` per task.

Hard rules: 5/5 QC on every dimension; per-task universe is SSoT; 500-word prompt cap; no em-dashes; no "at least N" without prompt mandate; no tool names in prompts or rubric titles; outcome > process in rubrics; 40% similarity ceiling.
