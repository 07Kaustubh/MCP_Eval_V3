# MCP Eval V3 — Project Knowledge Base

**Updated:** 2026-06-21

> **Operator?** Read [`QUICK_START.md`](QUICK_START.md) — the 1-page how-to.

## What this project is

An evaluation pipeline for MCP-task deliverables (prompts, oracle events, rubrics) built on the **Brookfield CPAs & Advisors** synthetic universe. The pipeline produces 5-of-5 QC-grade deliverables that meaningfully stump **Opus 4.8** during the 6-run agent verification step.

## Hard rules (apply to every phase, every chat)

1. **Opus 4.8 is the model under test.** All hardness engineering targets known Opus 4.8 failure modes from `Docs/4_Prompt_Hard_Tips.md` and `Reference/Hardness_Playbook.md`.
2. **Per-task `3_UniverseDataForThisTask.json` is the ONLY universe source of truth.** Always work from the split written to `Tasks/<TASK_DIR>/_aux/Universe_Split/` for the current task.
3. **`Brookfield_Base_Universe/` is stale by default.** The one stable file is `8_Server_Tools_Details.json` (tool definitions). Persona briefs in `2_Persona_Briefs.md` are also stable (personas do not change per task). Everything else in that directory describes a snapshot that may not match the per-task universe.
4. **No universe edits in this pipeline.** Hardness comes from levers already present in the per-task data. If S0/HARDNESS finds fewer than 3 levers, stop and ask the user to decide.
5. **500-word cap on prompts. No em-dashes anywhere.** Validator blocks both.
6. **No "at least N" in rubric titles** unless the prompt explicitly mandates a minimum. Atomic rubrics for multi-item write actions.
7. **No tool names in prompts. No tool names in rubric titles.** Allowed only in OE bodies and in rubric evidence / justification fields.
8. **Outcome must outnumber Process in rubrics.** All 4 V3 reference tasks have zero process rubrics. Default to zero. Three-condition test before adding any.
9. **Platform similarity ≥ 40% is not allowed.** Pivot the prompt using `Reference/Similarity_Pivot.md`.
10. **5 of 5 on every QC sub-dim is the bar.** Both councils must return GO before any deliverable ships.
11. **50+ tool calls midpoint is the design target; 40 is the absolute floor.** Council B-B3 (tool-call density projection), HARDNESS, AUDIT, and FINAL all use this tiered scheme: midpoint ≥ 50 = PASS; midpoint 40-49 = THIN_DENSITY (operator can continue with explicit per-task justification, but the task is at risk of underflow on real platform runs); midpoint < 40 = INSUFFICIENT_DENSITY (BLOCKER, STOPs the pipeline). The 50+ design target was set after tasks shipped with 40+ projected density came back from the platform failing density on real runs — designing for 50+ produces ~40+ tool calls in reality.
12. **Strict veteran AUDIT runs after every per-phase deliverable.** S1/S2/S3 (and S1.5 on prompt revise, and REVIEW on corrected materialization) auto-fire an AUDIT sub-agent inline after Council A + Council B pass. `PASS (STRICT)` is a required exit criterion for those phases. `REVISE` iterates the producing phase (cap 3 rounds); `REBUILD` STOPs to `PIPELINE REDO`. Catching defects at the producing phase is the project policy — downstream re-iteration at FINAL or platform-reviewer time is more expensive than the ~3 additional sub-agent calls per task that auto-AUDIT costs.

## Pipeline Deviations from Eval Specs

Where the 4 evaluator specs (`Evals/1_Prompt_Eval.md` ... `Evals/4_Verifier_Fails_Eval.md`) contain internal contradictions, conditional scoring, or under-specified rules, the pipeline picks one interpretation and documents the choice here. All deviations are conservative — when the spec is ambiguous, the pipeline picks the STRICTER reading.

| Eval spec rule | Spec ambiguity | Pipeline interpretation |
|---|---|---|
| Prompt Eval 2.8 universe-level date alignment is FAIL only if "it caused an agent failure" | Tautology at prompt-writing time (pre-trajectory) | Pipeline scores Prompt 2.8 as NON-FAIL when relative-date phrases are present but resolved windows have universe data; defers the "still-solvable exception" to S4 trajectory evaluation. |
| Prompt Eval 1.3 anti-pattern checks are binary PASS/FAIL but Phase 4.1 scoring uses 1/3/5 | No documented mapping | Pipeline maps each anti-pattern FAIL to a hard 1/5 on its corresponding sub-dim (Command List → Coherence; Bolt-on → Coherence; Pre-Solving → Pre-Solving sub-dim; Tool Mention → Explicit Tool Mention). |
| OE Eval contradicts itself on OE ordering | "OEs are unordered" vs Phase 3.2 dependency-chain checks ordering | Pipeline treats OEs as **unordered for coverage purposes** (Council B-B2 forward/reverse map) but **ordered when lifecycle preconditions apply** (`validate.py` lifecycle precondition check, v10). Both can be true simultaneously — coverage doesn't require order; lifecycle does. |
| Rubrics Eval Severity Taxonomy lists channel-lock-in as Minor; Phase 2.7 escalates to Major-by-default | Two conflicting rules | Pipeline applies Phase 2.7 escalation rule: channel/method lock-in is **Major by default** when a valid alternative path exists; Minor only when no realistic alternative is rejected. The taxonomy table's Minor entry is the FALLBACK, not the primary rule. |
| Rubrics Eval All-Failing Rubrics sub-dim defers to verifier stage | Verifier Fails Eval doesn't explicitly score it | Pipeline scores it at S4: `All-Failing Rubrics sub-dim FAILs if >50% of failing rubrics across the 6 runs are classified as Bucket 1 (Rubric Invalid)`. See `Reference/Sessions/S4.md` for the scoring sub-step. |
| Verifier Fails Eval Phase 3.3 says "this eval does not have access to agent trajectories" | Phase 3.2 requires per-run consistency analysis | Pipeline has full trajectory access via `Agent_Responses/Run*.json`. v10 S4 makes trajectory walk MANDATORY for every bucket classification. Pipeline exceeds the spec here. |
| Rubrics Eval Phase 4.2 threshold math allows dilution | A 100-rubric set with 1 Major (1%) PASSes | Pipeline adds absolute-count gates (Major ≥ 3 = FAIL; documented in `Reference/Rubric_Format.md`). |
| Rubrics Eval Phase 1.1 "0 Outcome = FAIL" but no fail path for missing Process when one is needed | Missing-Process is Non-Fail per spec | Pipeline applies v10 B6 propagation: when a needed Process behavior is identified, it propagates back to S3 as a `PROPAGATE TO S3` flag. Forces rubric expansion or Outcome tightening at the producing phase. |
| Specs reference `[V2] QC_Tasks/` as samples but pipeline uses `QC_Tasks/V3_Tasks/Task11..14/` | V2 samples are on the old Keystone universe | Pipeline reads V3 references directly (Brookfield universe). This is a pipeline-EXCEEDS-spec choice, documented for future spec alignment. |
| Eval specs require "TODO list at Step 0 HARD GATE" + "Phase 0 deep universe exploration" | No mechanism to verify | Pipeline runbooks list required inputs per phase; v11 E1 + E2 add `phase_ready.py` checks for TODO and reference-read logs. Without those, operator discipline is the only enforcement. |
| Tool-name handling differs per artifact (Prompt = FAIL anywhere; OE = MANDATORY; Rubric = NOT in title, OK in evidence) | Specs don't cross-reference each other | Pipeline `validate.py` handles per-phase correctly: prompt phase FAILs any tool-name token; OE phase FAILs only on UNKNOWN tool names; rubric phase FAILs tool names in title only. Per-phase distinction is intentional and stable. |

When the spec gets a new version, re-check this table against the new spec. If a spec amendment resolves a contradiction differently than the pipeline's interpretation, update both the pipeline AND this table together.

## PIPELINE DISPATCH

> **Supersedes the legacy `command workflow.txt`.** The 16 PIPELINE triggers below are the only entry points the operator needs. `command workflow.txt` is preserved for reference but the runbook contracts it described are now codified in `Reference/Sessions/*.md`.

Each trigger phrase below runs in a **fresh chat with zero prior context**. The runbook bootstraps itself. Find-replace `<TASK_DIR>` per task; everything else is fixed.

| Trigger phrase | Runbook | What it does |
|---|---|---|
| `PIPELINE NEW — <TASK_ID>` (or `PIPELINE NEW REVIEW — <TASK_ID>`) | [Reference/Sessions/NEW.md](Reference/Sessions/NEW.md) | Create fresh task folder + scaffold the input files. CB mode scaffolds 1/2/3 + nudges to S0. Review mode scaffolds 1/2/3/5/6/7/8 + nudges to REVIEW. Accepts `<hex>` (auto-index) or `<index>_<hex>` (explicit). |
| `PIPELINE S0 — Tasks/<TASK_DIR>` | [Reference/Sessions/S0.md](Reference/Sessions/S0.md) | Extract PersonaBrief, split universe, build Universe_Index |
| `PIPELINE HARDNESS — Tasks/<TASK_DIR>` | [Reference/Sessions/HARDNESS.md](Reference/Sessions/HARDNESS.md) | Scan for Opus-4.8 stumping levers, produce Hardness_Plan and Stump Hypothesis |
| `PIPELINE S1 — Tasks/<TASK_DIR>` | [Reference/Sessions/S1.md](Reference/Sessions/S1.md) | Draft `5_Prompt.txt`, validate, two councils |
| `PIPELINE S1.5 — Tasks/<TASK_DIR>` + linter paste | [Reference/Sessions/S1.5.md](Reference/Sessions/S1.5.md) | Handle linter blocker: revise / justify / pivot |
| `PIPELINE S2 — Tasks/<TASK_DIR>` | [Reference/Sessions/S2.md](Reference/Sessions/S2.md) | Draft `6_Oracle_Events.txt`, validate, two councils |
| `PIPELINE S3 — Tasks/<TASK_DIR>` | [Reference/Sessions/S3.md](Reference/Sessions/S3.md) | Draft `7_Rubrics.json`, validate, two councils (heaviest pass) |
| `PIPELINE FINAL — Tasks/<TASK_DIR>` | [Reference/Sessions/FINAL.md](Reference/Sessions/FINAL.md) | Cross-artifact holistic council — answer-leakage scan, entity-drift check, lever-preservation end-to-end. **Required before platform upload.** |
| `PIPELINE S4 — Tasks/<TASK_DIR>` + verifier-fails paste | [Reference/Sessions/S4.md](Reference/Sessions/S4.md) | Classify verifier fails, draft AF justifications |
| `PIPELINE REVIEW — Tasks/<TASK_DIR>` | [Reference/Sessions/REVIEW.md](Reference/Sessions/REVIEW.md) | Review-type task intake: full assessment (validator + Council A + Council B + AUDIT on original + FINAL) + deep trajectory analysis (S4-style bucket classification on original trajectories if present) + initialize `changes.md` with all rows auto-marked Applied. Does NOT materialize 14/15 (v16 split — MATERIALIZE does that). |
| `PIPELINE MATERIALIZE — Tasks/<TASK_DIR>` | [Reference/Sessions/MATERIALIZE.md](Reference/Sessions/MATERIALIZE.md) | Apply Applied rows from `changes.md` to produce `14_Updated_Oracle_Events.txt` / `15_Updated_Rubrics.json` / `_aux/REVIEW_prompt_draft.txt`, then re-run full gate set (validator + Council A + Council B + AUDIT + FINAL) on the corrected materialization. Runs AFTER REVIEW, BEFORE FEEDBACK. |
| `PIPELINE REDO — Tasks/<TASK_DIR>` | [Reference/Sessions/REDO.md](Reference/Sessions/REDO.md) | Reviewer redo: REVIEW done + fixes applied but trajectory failed on difficulty (pass@1 > 40%) or density (avg tool calls < 40). Archives candidate originals + rebuilds 5/6/7 from scratch as a full CB build. Also used when a CB's own task came back failing density / difficulty. |
| `PIPELINE COMPARE — Tasks/<TASK_DIR>` | [Reference/Sessions/COMPARE.md](Reference/Sessions/COMPARE.md) | Diff local `7_Rubrics.json` vs platform paste-back `10_Rubrics_Platform.json` to catch silent platform-side mutations |
| `PIPELINE AUDIT — Tasks/<TASK_DIR> --phase {prompt\|oe\|rubrics\|all}` | [Reference/Sessions/AUDIT.md](Reference/Sessions/AUDIT.md) | Veteran QC second-opinion under the STRICTEST possible interpretation (5/5 only, density bar 50+, every "should" read as "must"). **Auto-fires inline from S1/S2/S3 (and S1.5 on prompt revise, REVIEW on corrected materialization)** as the per-phase exit gate. Also available **on-demand** in a fresh chat via this trigger for high-stakes pre-upload sanity checks, post-platform-rejection retros, or post-pipeline-change re-audits. Read-only. Not a substitute for FINAL — complementary. |
| `PIPELINE FEEDBACK — Tasks/<TASK_DIR>` | [Reference/Sessions/FEEDBACK.md](Reference/Sessions/FEEDBACK.md) | **(REVIEW flow only.)** Write `13_Feedback.txt` rating the candidate's ORIGINAL submission against the QC SPEC baseline. Strict input allowlist — reads ONLY originals 5/6/7 + 3 (universe) + QC spec docs; explicitly DENIES `changes.md`, `14_*`, `15_*`, `_aux/Council_Reports/*`, REVIEW draft. Evaluates against spec baseline ONLY (NOT our internal exceeds-spec bar like 50+ density / strictest AUDIT — those are project policy, not spec requirements). Runs AFTER REVIEW, BEFORE CLOSE. Lifted into a separate phase because inline-with-REVIEW feedback consistently drifted to rating the fixed task instead of the original. |
| `PIPELINE CLOSE — Tasks/<TASK_DIR>` | [Reference/Sessions/CLOSE.md](Reference/Sessions/CLOSE.md) | Final read-only sanity check. Audits required artifacts + FINAL verdict + trajectory verdict; refuses to greenlight if anything is missing. Nudges to append cross-task learnings before exit. |

## Knowledge flow + file nomenclature

For the cross-cutting dependency chart (which phase reads / produces what), file-naming conventions (`<phase>_<council>_<purpose>.md`, `AUDIT_<phase>.md`, `S4_<bucket>.md`, etc.), single-source ownership map (Fact_Ledger SSOT, Universe_Split SSOT, etc.), and the cross-phase re-run map (when an artifact changes, what downstream phases must re-run), see [`Reference/Knowledge_Flow.md`](Reference/Knowledge_Flow.md). A fresh-chat agent invoking any phase should read that doc + the phase runbook to know every file path it will touch.

## Project layout

```
MCP_Eval_V3/
├── AGENTS.md                       # this file — entry point
├── Reference/                      # format cards + lever catalog + session runbooks
│   ├── Hardness_Playbook.md
│   ├── Prompt_Format.md
│   ├── OE_Format.md
│   ├── Rubric_Format.md
│   ├── Similarity_Pivot.md
│   ├── Linter_Playbook.md
│   ├── Council_Protocol.md
│   ├── Strict_Convention_Inventory.json
│   ├── OE_Convention_Inventory.json
│   └── Sessions/
│       ├── S0.md  HARDNESS.md  S1.md  S1.5.md  S2.md  S3.md  S4.md  REVIEW.md  COMPARE.md
├── Validators/
│   ├── split_universe.py           # per-task data.py wrapper
│   ├── build_universe_index.py     # per-task summaries
│   ├── build_fact_ledger.py        # per-task atom surface (emails, amounts, dates, ids, accounts, personas)
│   ├── build_graph_report.py       # per-task compact density map (people, periods, exceptions, AP, docs)
│   ├── compare_rubrics.py          # local vs platform-paste-back rubric diff
│   └── validate.py                 # phase-aware validator (prompt | oe | rubrics | all)
├── Brookfield_Base_Universe/       # STALE except 8_Server_Tools_Details.json + 2_Persona_Briefs.md
│   ├── 1_Summary.md ... 7_*.md     # stale reference, do not trust over per-task data
│   ├── 2_Persona_Briefs.md         # stable per-version (personas don't change per task)
│   ├── 8_Server_Tools_Details.json # STABLE — the tool / parameter reference
│   ├── 9_Universe_Schema.json
│   └── Data/                       # stale pre-baked universe split — do NOT use for per-task work
├── Docs/                           # V3 framework specs and guidelines (stable)
├── Evals/                          # phase eval specs (Prompt / OE / Rubrics / Verifier-Fails)
├── Guide/                          # how-to docs and verifier-fails template
├── QC_Tasks/
│   ├── V3_Tasks/                   # on-framework reference tasks (Task11..Task14)
│   └── V2_Tasks/                   # legacy V2/Keystone — study craft, not framework
├── Tasks_Template/                 # platform-paste-target template
├── Tasks/                          # live tasks
│   ├── <TASK_DIR>/                 # per-task work
│   │   ├── 1_Business_Function.txt … 9_Universe_inject.sql  # user-pasted + pipeline-produced (1-9 as before)
│   │   ├── 10_Rubrics_Platform.json   # optional, user pastes for COMPARE
│   │   ├── 13_Feedback.txt            # REVIEW flow only — candidate-facing rating
│   │   ├── 14_Updated_Oracle_Events.txt  # REVIEW flow only, IFF OE fixes Applied
│   │   ├── 15_Updated_Rubrics.json       # REVIEW flow only, IFF rubric fixes Applied
│   │   ├── PersonaBrief.txt
│   │   ├── changes.md              # review-tasks only
│   │   ├── Agent_Responses/        # 6 trajectory JSONs (user-pasted)
│   │   └── _aux/                   # pipeline working directory
│   │       ├── Universe_Split/     # per-task universe split
│   │       ├── Universe_Index/     # service_inventory, entities_personas, key_facts, today_horizon, accounts_per_entity, graph_report
│   │       ├── Fact_Ledger.json    # per-task verifiable atom surface (emails, $, dates, IDs, accounts, personas)
│   │       ├── Hardness_Plan.md
│   │       ├── S0_Setup_Report.md
│   │       ├── Linter_Decision.md
│   │       ├── Linter_Justifications.md
│   │       ├── Council_Reports/
│   │       ├── Validator_Reports/
│   │       └── Reasoning/
│   └── _meta/                      # cross-task learning logs
│       ├── Similarity_Log.md
│       ├── Linter_Justifications.md
│       ├── Hardness_Patterns_Log.md
│       └── Stump_Hypotheses.md
├── data.py                         # smart forwarder — routes per-task input to Validators/split_universe.py
└── data.legacy.py                  # original script (writes to shared Data/, can corrupt parallel work)
```

## Universe constants (per-task may differ)

- **Universe today:** 2026-06-12 (US/Eastern). Always confirm from `_aux/Universe_Index/today_horizon.json` per task.
- **Three client entities:** `brookfield` (the firm itself), `northstar_legal` (law firm), `acme_cloud` (SaaS).
- **Account-number trap:** `105000` is Cash-Trust on Brookfield, IOLTA on Northstar, Short-term Investments on Acme. `120000` is Client Cost Advances on Northstar, Deferred Commissions on Acme, absent on Brookfield. Always verify the per-entity role.
- **Valid Records Vault retention codes:** `AICPA_SQMS_7Y`, `IRS_TAX_7Y`, `FIRM_INTERNAL`, `INDEFINITE`. Never `SOX_7Y` or `SEC_PERMANENT`.
- **Classifications:** `internal` (default), `restricted` (elevated role required), `public` (defined but unused).
- **Slack channels:** C001 #general · C002 #water-cooler · C003 #announcements · C004 #client-onboarding · C005 #monthly-close-coordination · C006 #tax-prep-and-filings · C007 #audit-engagements · C008 #compliance-and-registrations · C009 #cash-management-and-banking · C010 #vendor-bills-and-ap · C012 (auto-created placeholder, not used).
- **Parameter traps:** email + messaging use `content` (not `body`). Slack uses `payload` (not `text`). Linear comments use `issueId` + `body`.
- **JE lifecycle:** `draft → submitted → approved → posted → reversed`. Minimum 300 seconds between transitions. Closed-period posting requires `late_post_authorization_id`.

## Where to start

- **Brand-new task (CB creation):** `PIPELINE NEW — <TASK_ID>` → paste 3 inputs → `PIPELINE S0 — Tasks/<TASK_DIR>`
- **Brand-new task (review-type, deliverables prefilled):** `PIPELINE NEW REVIEW — <TASK_ID>` → paste 7 inputs → `PIPELINE REVIEW — Tasks/<TASK_DIR>`
- **Already-scaffolded task, continuing mid-pipeline:** invoke the next-trigger phrase the previous phase's STOP gate printed
- **Stuck on a linter block:** `PIPELINE S1.5 — Tasks/<TASK_DIR>` + paste the linter output
- **Verifier results came back:** `PIPELINE S4 — Tasks/<TASK_DIR>` + paste verifier fails
- **Wrapping up:** `PIPELINE CLOSE — Tasks/<TASK_DIR>` (read-only final audit)

## Anti-patterns (this project)

- Reading anything in `Brookfield_Base_Universe/` other than `8_Server_Tools_Details.json` or `2_Persona_Briefs.md` and treating it as current per-task truth.
- Calling `data.legacy.py` directly (overwrites shared `Brookfield_Base_Universe/Data/` and can corrupt parallel work). Use `data.py` (smart forwarder) or `Validators/split_universe.py` instead.
- Adding process rubrics without applying the three-condition test.
- Using em-dashes or "at least N" without prompt mandate.
- Mentioning guides / specs / frameworks in linter justifications or AF justifications.
- Editing the per-task universe to "make room" for a hardness lever.
- Shipping a deliverable that hasn't cleared both councils.
