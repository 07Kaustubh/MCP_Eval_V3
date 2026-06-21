# Linear (stale-to-task pre-baked split)

> Per-task data lives in `Tasks/<TASK_DIR>/_aux/Universe_Split/linear.*.json`. Do not use these files for per-task work.

## Service role

Systemic-issue tracking. Not routine close work. 30 issues across 8 projects and 6 teams in the base universe (Linear tables are largely empty as write-targets in some tasks).

## Tables (inner shapes, parsed from `row_data`)

| File | Key fields |
|---|---|
| `linear_issues.json` | `id` (`issue_<hex>`), `title`, `description`, `state` / `status`, `assignee`, `due_date`, `priority`, `project_id`, `team_id` |
| `linear_projects.json` | `project_id` (`proj_*` or `linear_*`), `name`, `team_id` |
| `linear_teams.json` | `team_id`, `name` |
| `linear_comments.json` | `comment_id`, `issue_id`, `author`, `body`, `created_at` |
| `linear_users.json` | `user_id`, `email`, `name` |
| `linear_team_memberships.json` | `user_id`, `team_id`, `role` |

## Key project

`linear_63697b7dff5c` — "AP workflow standardization for managed clients". Primary destination for systemic issues surfaced by AP escalations.

## Parameter traps

- `linear_create_issue` takes `title`, `description`, `assignee_email`, `team_id`, `project_id`, `due_date`, `priority`.
- `linear_create_comment` takes `issueId` (camelCase!) + `body`. Watch the casing.
- `linear_update_issue` takes `id` + the fields to update.

## Discovery patterns

- Issues that are `state=todo` past their `due_date` = overdue tracking items (recurring hardness lever).
- Pair Linear issue updates with status comments to track "bring AP standardization tracking issues current" asks.

## MCP tool notes

- Read: `linear_list_issues`, `linear_get_issue`, `linear_list_projects`, `linear_list_comments`
- Write: `linear_create_issue`, `linear_update_issue`, `linear_create_comment`
