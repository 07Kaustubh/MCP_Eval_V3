# MCP Eval V3 — Project Knowledge Base

**Updated:** 2026-06-21

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
11. **40+ tool calls average across 6 runs is the maximalism floor.** Council B-B3 (tool-call density projection) blocks any deliverable that projects below 40. HARDNESS phase also gates at 40 before allowing S1.

## PIPELINE DISPATCH

> **Supersedes the legacy `command workflow.txt`.** The 10 PIPELINE triggers below are the only entry points the operator needs. `command workflow.txt` is preserved for reference but the runbook contracts it described are now codified in `Reference/Sessions/*.md`.

Each trigger phrase below runs in a **fresh chat with zero prior context**. The runbook bootstraps itself. Find-replace `<TASK_DIR>` per task; everything else is fixed.

| Trigger phrase | Runbook | What it does |
|---|---|---|
| `PIPELINE S0 — Tasks/<TASK_DIR>` | [Reference/Sessions/S0.md](Reference/Sessions/S0.md) | Extract PersonaBrief, split universe, build Universe_Index |
| `PIPELINE HARDNESS — Tasks/<TASK_DIR>` | [Reference/Sessions/HARDNESS.md](Reference/Sessions/HARDNESS.md) | Scan for Opus-4.8 stumping levers, produce Hardness_Plan and Stump Hypothesis |
| `PIPELINE S1 — Tasks/<TASK_DIR>` | [Reference/Sessions/S1.md](Reference/Sessions/S1.md) | Draft `5_Prompt.txt`, validate, two councils |
| `PIPELINE S1.5 — Tasks/<TASK_DIR>` + linter paste | [Reference/Sessions/S1.5.md](Reference/Sessions/S1.5.md) | Handle linter blocker: revise / justify / pivot |
| `PIPELINE S2 — Tasks/<TASK_DIR>` | [Reference/Sessions/S2.md](Reference/Sessions/S2.md) | Draft `6_Oracle_Events.txt`, validate, two councils |
| `PIPELINE S3 — Tasks/<TASK_DIR>` | [Reference/Sessions/S3.md](Reference/Sessions/S3.md) | Draft `7_Rubrics.json`, validate, two councils (heaviest pass) |
| `PIPELINE FINAL — Tasks/<TASK_DIR>` | [Reference/Sessions/FINAL.md](Reference/Sessions/FINAL.md) | Cross-artifact holistic council — answer-leakage scan, entity-drift check, lever-preservation end-to-end. **Required before platform upload.** |
| `PIPELINE S4 — Tasks/<TASK_DIR>` + verifier-fails paste | [Reference/Sessions/S4.md](Reference/Sessions/S4.md) | Classify verifier fails, draft AF justifications |
| `PIPELINE REVIEW — Tasks/<TASK_DIR>` | [Reference/Sessions/REVIEW.md](Reference/Sessions/REVIEW.md) | Review-type task intake: score existing deliverables, initialize `changes.md`, generate `13_Feedback.txt` + optional `14_Updated_Oracle_Events.txt` / `15_Updated_Rubrics.json` |
| `PIPELINE COMPARE — Tasks/<TASK_DIR>` | [Reference/Sessions/COMPARE.md](Reference/Sessions/COMPARE.md) | Diff local `7_Rubrics.json` vs platform paste-back `10_Rubrics_Platform.json` to catch silent platform-side mutations |

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

- **New task (creation mode):** `PIPELINE S0 — Tasks/<TASK_DIR>`
- **Review-type task (deliverables prefilled):** `PIPELINE REVIEW — Tasks/<TASK_DIR>`
- **Stuck on a linter block:** `PIPELINE S1.5 — Tasks/<TASK_DIR>` + paste the linter output
- **Verifier results came back:** `PIPELINE S4 — Tasks/<TASK_DIR>` + paste verifier fails

## Anti-patterns (this project)

- Reading anything in `Brookfield_Base_Universe/` other than `8_Server_Tools_Details.json` or `2_Persona_Briefs.md` and treating it as current per-task truth.
- Calling `data.legacy.py` directly (overwrites shared `Brookfield_Base_Universe/Data/` and can corrupt parallel work). Use `data.py` (smart forwarder) or `Validators/split_universe.py` instead.
- Adding process rubrics without applying the three-condition test.
- Using em-dashes or "at least N" without prompt mandate.
- Mentioning guides / specs / frameworks in linter justifications or AF justifications.
- Editing the per-task universe to "make room" for a hardness lever.
- Shipping a deliverable that hasn't cleared both councils.
