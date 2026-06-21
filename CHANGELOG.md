# Changelog

## 2026-06-21 — v6: Justification Voice Gate + Similarity Gate + AUDIT Runbook + Upstream-Propagation Council Perspective + OE Meta-Tag Ban + Word-Count Tiers + Hardened STOP Gates

Nine improvements driven by operator-pain debrief on Tasks 23-24. Closes the justification-voice gap (reviewers were seeing internal terminology in pushbacks), the silent-similarity-leak gap (similarity score wasn't enforced as a phase gate), the missing-veteran-audit gap (no on-demand strictest-interpretation re-verification), the upstream-propagation gap (S3 caught OE issues the operator had to manually trace back to S2), the OE meta-tag gap (validator missed `→ Write action` / `→ Read action` arrows operator had to manually strip), the lenient-word-count gap (single 500-word hard fail with no sweet-spot signal), and the STOP-gate leakage gap (operators were chaining phases inside one chat against the contract).

### New scripts

- **`Validators/calc_similarity.py`** — Jaccard on word bigrams (stdlib only). Scores `5_Prompt.txt` against every prior `5_Prompt.txt` in `Tasks/` + V3 reference prompts. Writes `_aux/Similarity_Report.json` with top matches per source. Project ceiling enforced at 40 (Class B pivot mandatory above that). Smoke-tested against Task 24: max score 4.2/100 (well clear of ceiling).
- **`Validators/check_justification.py`** — 8 forbidden-term categories (rubric numbers, council references, pipeline phase names, internal artifact names, script names, guide / spec references, V3 framework refs, Brookfield meta refs). Scans any reviewer-facing file (linter pushbacks, AF justifications, candidate feedback). Per-hit report with line + matched term + 60-char context. Smoke-tested against Task 24 `13_Feedback.txt`: caught 3 real hits (`Candidate_Originals`, `Trajectory_Stats`, `per-task universe`).

### New runbook

- **`Reference/Sessions/AUDIT.md`** — `PIPELINE AUDIT — Tasks/<TASK_DIR> --phase {prompt|oe|rubrics|all}` trigger. Veteran QC second-opinion under STRICTEST possible interpretation: 5/5 is the only acceptable score, density bar is 50+ midpoint (not 40 floor), every "should" reads as "must", every soft convention is binding. Returns `PASS (STRICT)` / `REVISE` / `REBUILD`. Read-only. Not a substitute for FINAL — complementary on-demand tool for high-stakes re-verification (pre-upload sanity check, post-rejection retro, post-pipeline-change re-audit).

### Validator changes

- **`Validators/validate.py`** — word-count tiers replace the single 500-word hard fail. HARD FAIL > 500, WARN > 400, NOTE > 300 (sweet spot 300-400 matches the V3 reference distribution).
- **`Validators/validate.py`** — OE meta-tag ban catches three forbidden patterns operators had to manually strip: `→ Write action` arrows, `→ Read action` arrows, `→ Outcome N.M` inline annotations, process-rubric inline annotations. The reviewer-facing OE file is meant to read as numbered prose, not as a process-aware annotated document.

### Council changes

- **`Reference/Council_Protocol.md`** — Council B adds B6 perspective: **Upstream Propagation**. When a council finds an issue whose root cause lives in an upstream artifact (S3 rubric review surfaces an OE accuracy gap; S2 OE review surfaces a prompt truthfulness gap; FINAL surfaces a lever the prompt's framing actively prevents), flag `PROPAGATE TO <PHASE>: ...` instead of patching downstream. Patching downstream silently embeds the bug forever. B6 finding is BLOCKING — the operator must re-run the named upstream phase, then re-run the current phase against the fresh upstream output. Closes the operator-pain pattern of OE errors caught at S3 (rubrics) stage and prompt truthfulness issues caught late at FINAL.
- **Role-Lens Anchoring** — Integration lens now also maps to B6 (root-cause-upstream attribution is a cross-phase property).

### Pipeline changes

- **`Reference/Sessions/S1.md`** — new step 7 between councils and Final Report: similarity gate via `calc_similarity.py`. < 30 PASS, 30-39 WARN (logged in `_aux/Reasoning/prompt_design.md`), ≥ 40 STOP with Class B pivot mandatory. Exit criteria updated.
- **`Reference/Sessions/S1.5.md`** — new step 6: `check_justification.py` gate on `_aux/Linter_Justifications.md` before STOP. Pushbacks with internal terminology now blocked at the runbook layer (operator was previously catching these manually).
- **`Reference/Sessions/S4.md`** — new step 5: `check_justification.py` gate on `_aux/Council_Reports/S4_AF_justifications.md` before producing the verdict report. AF batches with internal terminology now blocked at the runbook layer.
- **`Reference/Sessions/S0.md`, `S1.md`, `S1.5.md`, `S2.md`, `S3.md`, `FINAL.md`, `REVIEW.md`, `REDO.md`** — STOP gates hardened with explicit "if user pastes follow-up content in this chat, do NOT process it" canonical block. Closes the operator-pain pattern of agents auto-processing pasted content that should have been a fresh chat per the fresh-chat-per-phase contract.

### Linter Playbook changes

- **`Reference/Linter_Playbook.md`** — new "Forbidden terms (enforced by `Validators/check_justification.py`)" section listing all 8 categories with rationale. Two new BEFORE/AFTER worked examples (feasibility pushback + AF reasoning gap) showing the most common authoring mistake (writing in process-aware voice) and how to strip it. Pre-ship check sections added to both Class A pushback and AF justification flows. `changes.md` (operator-internal change log) explicitly excluded from the check — it uses internal terms legitimately.

### Dispatch + docs updates

- Root **`AGENTS.md`** — PIPELINE DISPATCH adds AUDIT row between COMPARE and CLOSE. Trigger count updated from 13 to 14.
- **`QUICK_START.md`** — conditional commands table expanded from 4 to 5 with the AUDIT row. S1 phase description notes the similarity gate. S4 description notes the AF justification check. AUDIT added to the "What each phase guarantees" list.

### What this closes

| Operator-pain gap from Tasks 23-24 debrief | Status |
|---|---|
| Reviewer-facing pushbacks / AF justifications had internal terminology slipping through | Closed — `check_justification.py` wired at S1.5 + S4 STOP gates |
| Similarity score wasn't a phase gate — only caught downstream at platform linter | Closed — `calc_similarity.py` wired at S1 between Council B and STOP |
| No on-demand strictest-interpretation re-verification for high-stakes uploads | Closed — `PIPELINE AUDIT` runbook + dispatch row |
| OE errors caught late at S3 had to be manually traced back to S2 with no protocol | Closed — Council B-B6 PROPAGATE perspective with mandatory upstream re-run |
| OE meta-tags (write/read action arrows) had to be manually stripped | Closed — validator catches all 3 patterns |
| Word count had no sweet-spot signal — operator couldn't tell 480 from 320 | Closed — HARD FAIL > 500 / WARN > 400 / NOTE > 300 tiers |
| Operators chained phases inside one chat, polluting the decision-clean contract | Closed — STOP gates hardened in 8 runbooks with explicit reject-follow-up block |

Smoke-tested end-to-end against Task 24 (reference task, 473 words, full lifecycle):
- `calc_similarity.py`: max 4.2/100 vs prior corpus (clear of 40 ceiling).
- `check_justification.py`: caught 3 real hits in `13_Feedback.txt`.
- `validate.py` word-count tiers: prompt = PASS with warn/note flags.
- `validate.py` OE meta-tag ban: synthetic test → 1 fail recorded.

---

## 2026-06-21 — v4: Learnings Log + Final Council + Multi-Model Opt-In + STOP Gates

Adopted the remaining 4 gaps from the sibling reviewer pipeline (excluding the SQL-inject layer the user explicitly skipped). Closes the empirical-calibration gap and the cross-artifact gate gap. Pipeline is now decisively ahead overall.

### New files
- `Tasks/_meta/Learnings.md` — append-only empirical Opus 4.8 failure-mode log. 22 numbered findings (L1-L22) distilled from the Archive's two-task iteration evidence: which patterns reliably fail Opus 4.8 (L8 three reductions across services, L9 authority-figure dismissal, L10 SAP subledger invisibility) and which do not (L1 confirm-already-done, L6 stated-answer correction emails, L7 binary "is it posted?" traps). HARDNESS phase reads this BEFORE drafting; every lever pick must cite an entry that justifies it.
- `Reference/Sessions/FINAL.md` — new `PIPELINE FINAL — Tasks/<TASK_DIR>` runbook. Cross-artifact holistic council reading prompt + OE + rubrics together, plus Hardness_Plan and Fact_Ledger. 4 lenses (Truthfulness / Rubric binding / Cross-artifact holism / Red-team adversarial) catch what per-phase councils cannot: answer leakage (correct figure appearing verbatim in artifact text), entity drift across artifacts, hardness-lever regression after S2/S3 edits, integrated tool-call density. Required before platform upload — STOP gate at end of S3 points here.

### Council changes
- `Reference/Council_Protocol.md` adds opt-in `COUNCIL_MODE=multi` mode: 5 separate sub-agent calls (one per role lens) + 6th consensus synthesizer. Default Council B stays as 1-call with 5 lenses overlaid. Multi-mode is for critical deliverables where the 5x token spend is justified.

### Runbook changes
- `Reference/Sessions/S1.md` / `S2.md` / `S3.md` — explicit `STOP gate` sections at end. Each phase ends, the chat closes, user invokes the next phase in a fresh chat. S3 STOP now points to `PIPELINE FINAL` (mandatory) before any platform upload.
- `Reference/Sessions/HARDNESS.md` — step 1 is now "Read `Tasks/_meta/Learnings.md` end to end" before any sub-agent spawn. Every lever pick cites a Learnings entry. Step 4 (lever selection) defaults to the L8 + L9 + L10 anatomy. Step 6 (stump hypothesis) cites Learnings entries in the reasoning.

### Dispatch + index updates
- Root `AGENTS.md` PIPELINE DISPATCH adds `PIPELINE FINAL` between S3 and S4, marked "Required before platform upload".
- `Reference/AGENTS.md` runbook table adds `FINAL.md`.
- `Tasks/_meta/AGENTS.md` table adds `Learnings.md` with note "Read this BEFORE every PIPELINE HARDNESS run".

### What this closes

| Gap from prior comparison | Status |
|---|---|
| Their `Learnings.md` empirical calibration | Closed — mine is seeded from theirs + designed for ongoing append after every S4 |
| Their Final Council cross-artifact gate | Closed — `PIPELINE FINAL` is a binding gate before platform upload |
| Their true multi-model reviewer diversity | Closed — opt-in mode for critical deliverables |
| Their explicit pause-between-phases discipline | Closed — STOP gates in S1/S2/S3 |
| Their universe-inject SQL workflow | Intentionally skipped per user spec |

The only remaining advantages on their side are universe-edit Phase 1.5 (out of scope) and one-task-at-a-time `clear_task_folder.sh` discipline (incompatible with parallel batch QC).



Adopted 6 improvements from a sibling reviewer pipeline. Closes the grounding-rigor gap (their strongest dimension) and adds compounding cross-task value.

### New scripts
- `Validators/build_fact_ledger.py` — emits `_aux/Fact_Ledger.json`: a flat surface of every verifiable atom per task (emails, money amounts canonicalized to 2dp, ISO dates with day-of-week, typed ID buckets, accounts-by-entity, fiscal periods with lock state, personas with aliases). Replaces grep-based grounding with O(1) set lookups. Source hash tracks regenerate trigger.
- `Validators/build_graph_report.py` — emits `_aux/Universe_Index/graph_report.md`: compact discovery map for HARDNESS (people-by-density top 30, periods-by-JE-count top 20, exceptions/recons by entity×state, pending-AP by vendor top 20, docs by kind/classification, densest person×period pairs top 15). Summary tables only, no edge-list bloat.
- `Validators/compare_rubrics.py` — per-index diff between `7_Rubrics.json` and `10_Rubrics_Platform.json`. Catches silent platform-side mutations.

### Validator changes
- `validate.py --phase rubrics` now uses `_aux/Fact_Ledger.json` for groundedness when available (falls back to raw blob substring match). O(1) set lookups instead of substring scanning. The dollar-amount false-positive class on formatted floats is permanently eliminated.
- New naturalness heuristics adopted from rubric_naturalness.py: subjective terms (`thorough`, `professional`, `helpful`, `properly`, `appropriately`, `sufficiently`, `enough`) are FAIL; non-agent eval-voice (`the email mentions`, `(via `, `tool call`, `trajectory shows`, `the model must use`, `as expected`, `should obviously`) is WARN; awkward negation (`does not fail`, `never fails`, `must not be wrong`) is WARN.

### Council changes
- Council B gets a Role-Lens Anchoring layer overlaying the existing B1-B5 perspectives. Five lenses (Architect / Implementer / Red-team / Ground-truth / Integration) read the deliverable five times each, with each lens mapped to the strongest perspective. Single sub-agent call, multi-perspective coverage. BLOCK from any lens propagates to its mapped perspective.

### Pipeline changes
- S0 runbook now produces `_aux/Fact_Ledger.json` and `_aux/Universe_Index/graph_report.md` automatically.
- New `PIPELINE COMPARE — Tasks/<TASK_DIR>` trigger + `Reference/Sessions/COMPARE.md` runbook for platform paste-back verification.
- REVIEW runbook now emits `13_Feedback.txt` (candidate-facing rating, concise human voice, no em-dashes, no guide references) and conditionally emits `14_Updated_Oracle_Events.txt` / `15_Updated_Rubrics.json` ONLY when corresponding `changes.md` rows are Applied. Originals `5/6/7` stay pristine for rating.

### Docs updated
- Root `AGENTS.md` — dispatch table adds COMPARE, project layout adds 5 new files in `_aux/` and 13/14/15 in per-task root, validator inventory adds 3 new scripts.
- `Validators/AGENTS.md` — full documentation for the 3 new scripts + ledger / naturalness mentions on `validate.py --phase rubrics`.
- `Reference/Sessions/S0.md` — steps 4-5 added for fact ledger + graph report.
- `Reference/Sessions/REVIEW.md` — steps 7-8 added for `13_Feedback.txt` + conditional 14/15, plus updated exit criteria.
- `Reference/Council_Protocol.md` — Role-Lens Anchoring section + lens instructions woven into the Council B prompt template.



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
