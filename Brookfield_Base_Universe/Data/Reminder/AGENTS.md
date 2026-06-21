# Reminder (stale-to-task pre-baked split)

> Per-task data lives in `Tasks/<TASK_DIR>/_aux/Universe_Split/reminder.reminders.json`. Do not use these files for per-task work.

## Service role

SLA tracking, filing deadlines, recurring milestones. 53 reminders in the base universe.

## Tables (inner shapes, parsed from `row_data`)

| File | Key fields |
|---|---|
| `reminders.json` | `reminder_id`, `title`, `description`, `due_datetime`, `owner`, `related_exception_id`, `related_recon_id`, `status` |

## Discovery patterns

- The **stale-tickler / polling-bug pattern** (Task family scen_001..scen_022): a reminder fires repeatedly against an already-closed exception. The correct response is dismissal with audit trail, NOT reopening.
- Reminders past their `due_datetime` against still-open work items signal which approvals / chases are overdue.

## MCP tool notes

- Read: `reminder_get_all_reminders`, `reminder_get_due_reminders`, `reminder_get_reminder`
- Write: `reminder_add_reminder`, `reminder_update_reminder`, `reminder_dismiss_reminder`
- `reminder_add_reminder` takes `title`, `description`, `due_datetime` (ISO 8601 with timezone offset).
