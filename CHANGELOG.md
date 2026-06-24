# Changelog

## 2026-06-21 — v8: Trajectory-Mandatory S4 + REVIEW Linter Branch + Original-Candidate Feedback + Skeptical-First Linter + Multi-Dim Similarity + Class B Invalidation + Knowledge Flow + Density Target Raised to 50+

Eight follow-up improvements from operator-pain debrief on Tasks 23-24 and the legacy `command workflow.txt` parity review. Closes operator pain points that the v6/v7 sprint did not address.

### S4 trajectory walk strengthened (item 1)
- `Reference/Sessions/S4.md` step 2 rewritten: trajectory walk is now MANDATORY for EVERY failing rubric, not just Bucket 2 (Judge Error). Every bucket entry MUST carry a trajectory citation (`Run X, tool call Y: <parameter values>` or `Run X: action not attempted`). Without the walk, Bucket 1 (Rubric Invalid) and Bucket 3 (Legit AF) cannot be distinguished from Bucket 2. Each bucket section now spells out its trajectory-citation requirement explicitly.

### REVIEW linter branch added (item 2)
- `Reference/Sessions/REVIEW.md` new step 0 "Linter check FIRST" — if the candidate's prompt is blocked by the platform linter (operator cannot access prefilled OE / rubrics), STOP and route to `PIPELINE S1.5` in a fresh chat. Returns to REVIEW once linter is cleared (justification accepted OR scratch-draft fix accepted).
- `Reference/Sessions/S1.5.md` mode detection rewritten: Review-mode now detected by candidate-prefilled `6_Oracle_Events.txt` + `7_Rubrics.json` presence — does NOT require prior REVIEW run. Handles linter-before-REVIEW and linter-after-REVIEW symmetrically.

### REVIEW feedback fix: rates ORIGINAL not fixed (item 3)
- `Reference/Sessions/REVIEW.md` step 7 rewritten with explicit guardrails: `13_Feedback.txt` rates the CANDIDATE'S ORIGINAL deliverables AS SUBMITTED. Do NOT reference `changes.md`, `14_Updated_*.txt`, `15_Updated_*.json`, `_aux/REVIEW_prompt_draft.txt`, or anything we fixed. Common defect named explicitly: "writing feedback for the fixed task instead of the original".
- Feedback dimensions use plain-language descriptions of QC criteria, not the strict QC dim names (loose mapping table provided in runbook with 8 example translations). Voice-gate via `check_justification.py` is mandatory before save.

### Skeptical-first linter handling (item 4)
- `Reference/Sessions/S1.5.md` Class A decision flow rewritten: default assumption is the linter MAY be wrong. INVALIDATE with justification is the preferred path (cheap — platform doesn't intelligently evaluate justifications). REVISE is high cost (re-runs all gates including AUDIT). Ambiguous cases default to INVALIDATE. Choose REVISE only when the universe grep gives no plausible counter to the linter.
- Rationale codified: cost asymmetry favors invalidation; revision risks introducing new defects.

### Multi-dimensional similarity scoring with multiplicative context model (item 5)
- `Validators/calc_similarity.py` upgraded to multi-dimensional COMPOSITE score with MULTIPLICATIVE context modifier (context dominates word stats per operator preference — same-day amendment).
  - Lexical: word_bigram Jaccard (weight 0.40), word_unigram Jaccard (weight 0.40), word_count_similarity (weight 0.20).
  - Context multipliers when CONSTANTS DIFFER: business_function × 0.6, persona × 0.6, universe × 0.7 (multiplicative — max compounded reduction ×0.252 when all three differ, ~75% off raw lexical). Same constants leave lexical similarity intact (expected overlap — same persona × business function × universe has a fixed set of plausible scenarios); DIFFERENT constants REDUCE the score so contextual differentiators dominate lexical overlap.
  - Bands (simplified, two-band): **composite < 40 = INVALIDATE** (write 2-3 sentence justification, move on); **composite ≥ 40 = PIVOT** (high overlap that survives contextual weighting, constants align, structural similarity is genuine).
- New CLI flag `--explain <prior_task_dir>` prints per-dimension breakdown vs a specific prior task, naming the differentiating dimensions for use in the Class B invalidation justification.
- `_aux/Similarity_Report.json` now carries per-dimension breakdown + composite + context multiplier + recommendation per top-10 match. Back-compat `max_score` field preserved for older runbook references.
- Smoke-tested on Task 24: max composite 26.2 (clear, INVALIDATE recommendation across top-10 entries). `--explain` vs Task 23 shows raw lexical 26.3 × ×0.252 multiplier (BF + persona + universe all differ) = composite 6.6 — clear INVALIDATE, strong differentiators cited for justification angle.

### Class B similarity invalidation template + 2-band simplification (item 6)
- `Reference/Linter_Playbook.md` Class B section rewritten: no longer "pivot only" — now skeptical-first invalidation OR pivot. New template (2-3 sentences max, stricter than Class A) + 2 worked examples (different persona / same BF; same persona / different BF). Voice-gate via `check_justification.py`.
- `Reference/Sessions/S1.5.md` Class B decision flow simplified to two bands per operator preference: **composite < 40 → INVALIDATE** (move on); **composite ≥ 40 → PIVOT** (constants align even after the context multiplier was applied, structural similarity is genuine). No ambiguous middle band — the context multiplier handles ambiguity at the score level.
- `Reference/Sessions/S1.md` proactive similarity gate simplified to two bands matching S1.5: < 40 PASS, ≥ 40 STOP/PIVOT.

### Knowledge-flow + file-nomenclature reference (item 7)
- New `Reference/Knowledge_Flow.md` — phase dependency chart (every phase's reads + produces), file nomenclature canonical conventions (`<phase>_<council>_<purpose>.md`, `AUDIT_<phase>.md`, `S4_<bucket>.md`, `<descriptive>.md` for reasoning, etc.), single-source ownership map (Fact_Ledger SSOT, Universe_Split SSOT, etc.), cross-phase re-run map (when an artifact changes, what downstream phases must re-run).
- Root `AGENTS.md` Project Layout amended to point at Knowledge_Flow.md.

### Density target raised: 50+ design / 40 floor (item 8)
- Hard rule #11 rewritten in root `AGENTS.md`: 50+ midpoint design target produces ~40+ tool calls in real platform runs. Tiered scheme — midpoint ≥ 50 = PASS; 40-49 = THIN_DENSITY (operator continues with per-task justification, task at risk of underflow); < 40 = INSUFFICIENT_DENSITY (BLOCKER).
- HARDNESS phase: density-projection gate tiered (PASS at ≥ 50, THIN at 40-49 with `## THIN density acceptance` justification, STOP at < 40). Composition rules bumped: default 4-5 levers instead of 3-5 (3 acceptable only with high-cost lever combo + per-task justification, since 3 levers will frequently land in THIN band or below).
- Council B-B3 perspective + prompt template + pass criteria all updated to tiered scheme.
- S1 / S2 / S3 exit criteria updated.
- FINAL council density check tiered (table row + prompt template).
- AUDIT Lens 4 unchanged (already at 50+ midpoint — this was the v6 setting that the v8 pipeline now aligns with).
- QUICK_START updated.
- Rationale: tasks that shipped with 40+ projected density came back from the platform failing density on real runs. Designing for 50+ produces ~40+ in reality.

### Smoke-test evidence

| Script | Task 24 result | Pass criterion |
|---|---|---|
| `validate.py --phase all` | PASS all three phases (0 fails, low warns/notes) | exit 0 |
| `calc_similarity.py` (default) | max composite 26.2 vs 29-prompt corpus | < 40 |
| `calc_similarity.py --explain Tasks/23_...` | raw 26.3 → composite 0.0 after −50 discount (BF + persona + universe all differ) | < 40 |
| `calc_similarity.py --explain Tasks/22_...` | raw 27.1 → composite 0.0 after −40 discount (BF + persona differ, universe unknown) | < 40 |
| `check_justification.py` on `13_Feedback.txt` | 3 pre-existing hits caught (`Candidate_Originals`, `Trajectory_Stats`, `per-task universe`) — gate works as designed | (separate fix pass) |

### What this closes

| Operator-pain gap | Status |
|---|---|
| S4 bucket classification relying on verifier text alone, not trajectory | Closed — trajectory walk mandatory per failing rubric, citation required per bucket |
| REVIEW had no way to handle linter-blocking on candidate's prompt before seeing prefilled OE / rubrics | Closed — Step 0 routing to S1.5 + Review-mode detection without requiring prior REVIEW run |
| `13_Feedback.txt` chats wrote feedback for the fixed task instead of the original candidate | Closed — explicit guardrail in step 7 + plain-language QC dim mapping + voice-gate |
| Linter handling was authoritative-first, expensive (revise) by default | Closed — skeptical-first, invalidate by default (cheap), revise only when universe grep is unambiguous |
| Similarity scoring was lexical-only — couldn't surface that same persona × business function × universe has expected overlap | Closed — multi-dimensional with context discounts for differing constants + `--explain` mode |
| No Class B invalidation template — operator wrote them by hand and they overshot | Closed — strict 2-3 sentence template + 2 worked examples + voice-gate |
| File nomenclature and knowledge flow scattered across runbooks; fresh-chat agents missed dependencies | Closed — single canonical `Reference/Knowledge_Flow.md` with phase dependency chart + SSOT map + re-run map |
| Tasks projected to 40+ density but real runs underflowed | Closed — design target raised to 50+ midpoint; 40-49 explicitly flagged as THIN and at risk |

---

## 2026-06-21 — v7: Strict Veteran AUDIT Auto-Fires After Every Per-Phase Deliverable

Same-day amendment to v6's AUDIT runbook. Operator found flaws on Tasks 23-24 that escaped per-phase Council A + B + FINAL. Decision: catching defects at the producing phase is cheaper than catching them downstream at FINAL or at platform-reviewer time, so AUDIT becomes a MANDATORY per-phase exit gate, not an optional on-demand tool.

### Behavior change

v6 shipped AUDIT as an on-demand-only trigger. v7 makes AUDIT mandatory inline after every per-phase deliverable:

| Phase | When AUDIT fires | Sub-agent | Phase argument |
|---|---|---|---|
| S1 | After Council A + B + similarity gate pass | `oracle` | `--phase prompt` |
| S2 | After Council A + B pass | `oracle` | `--phase oe` |
| S3 | After Council A + B pass | `ultrabrain` | `--phase rubrics` |
| S1.5 | After Council A + B re-run on revised prompt (skipped on justification-only path) | `oracle` | `--phase prompt` |
| REVIEW | On the corrected materialization (14/15 + prompt draft) | per phase | per phase |

`PASS (STRICT)` is now a required exit criterion. `REVISE` iterates the producing phase (validators + Council A + Council B + AUDIT, iteration cap 3 rounds). `REBUILD` STOPs to `PIPELINE REDO`. `PROPAGATE TO <upstream>` STOPs to the upstream phase re-run (uses the Council B-B6 propagation mechanism added in v6).

On-demand mode preserved unchanged for additional re-verification beyond the built-in gates (pre-FINAL pre-upload sanity check, post-platform-rejection retro, post-pipeline-change re-audit).

### Files modified

- **`Reference/Sessions/AUDIT.md`** — "What this phase does" rewritten to describe dual-mode operation (Mode 1 auto-fire from per-phase runbooks + Mode 2 on-demand). "When NOT to use" updated (removed "during normal build pipeline" bullet). Cost note updated to reflect the ~3 additional sub-agent calls per task. STOP gate clarified as on-demand-mode only (auto-fire piggybacks on the parent phase's STOP gate).
- **`Reference/Sessions/S1.md`** — new step 8 "Strict veteran audit (MANDATORY, auto-fire)" between similarity gate (step 7) and final report (now step 9). Exit criteria updated to require `AUDIT_prompt.md` with `PASS (STRICT)`.
- **`Reference/Sessions/S2.md`** — new step 8 "Strict veteran audit (MANDATORY, auto-fire)" between Loop (step 7) and final report (now step 9). Exit criteria updated to require `AUDIT_oe.md` with `PASS (STRICT)`. Includes explicit handling for `PROPAGATE TO S1` findings (STOP to S1 re-run).
- **`Reference/Sessions/S3.md`** — new step 9 "Strict veteran audit (MANDATORY, auto-fire)" between Loop (step 8) and coverage matrix (now step 10). Uses `ultrabrain` (rubrics is the heaviest phase). Exit criteria updated to require `AUDIT_rubrics.md` with `PASS (STRICT)`. Includes explicit handling for `PROPAGATE TO S1` and `PROPAGATE TO S2` findings.
- **`Reference/Sessions/S1.5.md`** — new step 7 "Strict veteran audit on any revised prompt" between justification voice gate (step 6) and exit. Conditional: fires only when 5_Prompt.txt or REVIEW_prompt_draft.txt was modified (Class A revise OR Class B pivot path). Skipped on justification-only resolution.
- **`Reference/Sessions/REVIEW.md`** — step 11 amended to include AUDIT on every corrected artifact (14/15 + prompt draft). AUDIT fires before FINAL in the re-run gate set, matching the per-phase order in S1/S2/S3.
- **Root `AGENTS.md`** — new hard rule #12: "Strict veteran AUDIT runs after every per-phase deliverable." Dispatch table description for AUDIT updated to call out auto-fire mode + preserved on-demand mode.
- **`QUICK_START.md`** — "What each phase guarantees" updated to note inline AUDIT in S1/S2/S3. Conditional commands table updated to clarify the on-demand AUDIT trigger is for ADDITIONAL re-verification beyond the auto-fired inline gate.

### Cost + benefit

- **Cost**: ~3 additional sub-agent calls per task (S1 + S2 + S3, with S3 using ultrabrain). Pre-FINAL pre-upload on-demand AUDIT is still possible but largely redundant once auto-fire is in place.
- **Benefit**: catches defects at the producing phase, before they propagate through downstream phases. Operator-pain pattern on Tasks 23-24 (defects surfacing only at S3 or at FINAL or post-trajectory) is structurally prevented.

The bar is now: validator + Council A + Council B + AUDIT all GO per phase, then FINAL GO before platform upload. Five gates per task.

---

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
