# Linter Decision — Task 36

**Date:** 2026-07-02
**Universe:** moveops (auto-detected, cached at `_aux/Universe.txt`)
**Class:** A (misalignment on business function / systems / write actions / scope)
**Action:** INVALIDATE (justification only, no prompt edit)
**Final state of `5_Prompt.txt`:** unchanged

## What the linter blocked

Platform linter ran the "Keystone Business alignment check for v2.2 tasks" against the prompt and returned FALSE. It flagged:
- Function Match Weak (Customer Engagement vs perceived relocation logistics)
- Systems Check flagged Airtable, Road Runner, Linear as not existing in Keystone tool matrix
- Write Actions Check flagged Linear comment, Airtable update, Calendar hold as outside Customer Engagement
- Scope & Authority Check flagged coordination across housing partners / carriers / finance as Operations-scope not Customer Engagement
- Naturalness Check: Pass
- Verdict: FALSE, no suggested revision offered

## Skeptical-first reasoning

The linter's entire premise is universe-misclassified. This task is a MoveOps universe task (auto-detected at S0, cached at `_aux/Universe.txt`), NOT a Keystone Mortgage task. The linter check name explicitly says "Keystone Business alignment" — it applied the wrong universe's tool matrix.

Universe grep against `3_UniverseDataForThisTask.json` confirms every entity and system the linter claims doesn't exist:

| Entity / system | Hits in per-task data | Linter claim |
|---|---:|---|
| BrightLoop | 313 | "not in Keystone business model" |
| Simone Richter | 54 | "corporate relocation not mortgage" |
| Marcus Webb | 91 | "corporate relocation not mortgage" |
| 2019 Honda Civic | present | "no vehicle transport in Keystone" |
| Road Runner | 36 | "not a recognized tool" |
| UrbanNest | 101 | (implicit — housing partner) |
| Julian Brooks | 13 | (Lead Customer Support Specialist per persona brief) |
| Airtable | 273 hits, 167 records, 2 bases, 3 tables | "not in any function tool matrix" |
| Linear | 527 hits, 69 issues, 8 projects, 79 comments | "Engineering-adjacent not Customer Engagement" |
| Mina Hashimoto | 146 | (audit thread owner) |
| Carmen | 48 | (housing partner rep prompt names) |
| April cohort | 1 explicit | "categorically different CRM use case" |

Per `AGENTS.md` MoveOps registry: services include airtable, calendar, contacts, crm, email, linear, public, quickbooks, slack. Business functions include Customer Engagement / Support at 30%. Airtable is source-of-truth for relocation state per hardcoded landmine. Every write action the prompt names is available to the Customer Engagement function in this universe.

The linter is clearly wrong (not ambiguous, not clearly right). Cost asymmetry favors invalidation. INVALIDATE.

## Voice gate

`python3 Validators/check_justification.py Tasks/36_6a44224ed5d3b47d6d727cf5/_aux/Linter_Justifications.md` → 0 hits, exit 0.

## AUDIT skip

Per S1.5 runbook step 8: "Skip this step ONLY if the resolution was justification-only (no prompt edit)." The prompt was not modified; no re-audit required.
