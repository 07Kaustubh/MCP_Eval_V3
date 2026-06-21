# Airtable (stale-to-task pre-baked split)

> Per-task data lives in `Tasks/<TASK_DIR>/_aux/Universe_Split/airtable.{bases,tables,records}.json`. Do not use these files for per-task work.

## Service role

Workflow management for portfolio coordination and ops tracking. 2 bases, 5 tables, 21 records in the base universe.

## Tables (inner shapes, parsed from `row_data`)

| File | Key fields |
|---|---|
| `bases.json` | `base_id`, `name`, `purpose` |
| `tables.json` | `table_id`, `base_id`, `name`, `purpose` |
| `records.json` | `record_id`, `base_id`, `table_id`, `fields` (nested map), `owner`, `status` |

## Common workflow tables (by name)

- Close Blocker Triage Log
- Weekly Tax and Review Cadence
- AP Workflow Exceptions
- Annual Report Filing Control
- Client Access and Onboarding Admin

## Status enum patterns (per table)

- Close Blocker: `open → investigating → awaiting_partner_review → resolved`
- AP Workflow: `open → pending_client_approval → remediating → closed`
- Tax Cadence: `scheduled → in_review → escalated → completed`
- Annual Report: `not_started → in_progress → awaiting_client_docs → ready_to_file → submitted`
- Onboarding Admin: `queued → in_progress → waiting_access → completed`

## MCP tool parameter notes

- `airtable_create_record` / `airtable_update_records` take `base_id`, `table_id`, `fields`.
- Always verify the per-task universe contains the base + table before referencing them in OEs.
