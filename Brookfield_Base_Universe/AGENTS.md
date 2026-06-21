# Brookfield_Base_Universe — STALE BY DEFAULT

> **HARD RULE.** This directory is stale-to-task. The only files that are reliably stable across tasks are:
>
> - `8_Server_Tools_Details.json` — the MCP tool definitions (versioned by tool surface, not by task)
> - `2_Persona_Briefs.md` — the 34 persona briefs (personas do not change per task)
>
> Everything else describes a snapshot from a particular universe version. The per-task universe in `Tasks/<TASK_DIR>/3_UniverseDataForThisTask.json` is the only source of truth for any concrete fact (JE counts, exception states, document IDs, AP invoice statuses, fiscal-period lock state, scenario presence, etc.).

## What's here

| File | Trust level | Use for |
|---|---|---|
| `1_Summary.md` | Stale-to-task | Persona / org-chart orientation only. Not for counts or status. |
| `2_Persona_Briefs.md` | **STABLE** | Source for `PersonaBrief.txt` in S0. |
| `3_Task_Categories_Business_Functions.md` | Stale-to-task | Reference for the 10 business functions and worked examples. |
| `4_Scenario_Storylines.md` | Stale-to-task | Reference for scripted scenarios. Do NOT assume any scenario is present in a given task. |
| `5_Artifacts_Universe_Ref_Sheet.md` | Stale-to-task | Reference for personas + NPCs + system schemas. |
| `6_Glossary.md` | Stable | Accounting term definitions. |
| `7_Brookfield_Universe_One_pager.md` | Stale-to-task | High-level orientation only. |
| `8_Server_Tools_Details.json` | **STABLE** | The only authoritative tool / parameter reference. Validators and OE writers consume this. |
| `9_Universe_Schema.json` | Stable | Database schema for all tables. |
| `Get_Universe_Data.sql` | Stable | SQL to extract a universe (used by the platform; not by this pipeline). |
| `Data/` | **STALE** | Pre-baked universe split. DO NOT use for per-task work. Use `Tasks/<TASK_DIR>/_aux/Universe_Split/` instead. |

## What changes per task

- All concrete record counts (JEs, exceptions, AP invoices, documents).
- All "open" / "investigating" / "awaiting_approval" / "closed" state distributions.
- Which fiscal periods are `open` vs `closed` vs `future`.
- Which scenarios are anchored in the data (the 52 scenario storylines are not all present in every task universe).
- Which document IDs / exception IDs / JE IDs / AP invoice IDs exist.

## When you need universe facts for a task

1. Read `Tasks/<TASK_DIR>/_aux/Universe_Split/` (built by `Validators/split_universe.py`).
2. Read `Tasks/<TASK_DIR>/_aux/Universe_Index/` (built by `Validators/build_universe_index.py`) for fast lookups.
3. Only consult `Brookfield_Base_Universe/8_Server_Tools_Details.json` for tool / parameter definitions.
4. Only consult `2_Persona_Briefs.md` for the persona brief (persona attributes are stable).

If you find yourself reading any other file in this directory to ground a fact in a deliverable, stop. Go to the per-task split.
