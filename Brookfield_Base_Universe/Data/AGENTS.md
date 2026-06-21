# Brookfield_Base_Universe/Data — STALE pre-baked split

> **HARD RULE.** Do NOT use any file in this directory for per-task work.
>
> These files are a pre-baked split of one historical universe snapshot. For the current task, the only valid universe split lives in `Tasks/<TASK_DIR>/_aux/Universe_Split/`, produced by `Validators/split_universe.py` from the per-task `3_UniverseDataForThisTask.json`.

## What's here

13 service subdirectories + `Base_Universe_Complete_Data.json` (the whole snapshot in one file).

| Service | What it covers | Key tables |
|---|---|---|
| [Airtable](Airtable/AGENTS.md) | Portfolio + workflow management | bases, tables, records |
| [Blackline](Blackline/AGENTS.md) | Close + reconciliation workflow | reconciliations, exceptions, close_tasks, review_notes, evidence, audit_trail, archived_reconciliations |
| [Calendar](Calendar/AGENTS.md) | Meetings + lock targets | events |
| [Contacts](Contacts/AGENTS.md) | Vendor / client / regulator records | contacts |
| [Email](Email/AGENTS.md) | Formal comms + audit trail | emails (threading via parent_id) |
| [Linear](Linear/AGENTS.md) | Systemic-issue tracking | issues, projects, teams, comments, users, team_memberships |
| [Messaging](Messaging/AGENTS.md) | DMs and small-group threads | conversations, messages |
| [Oracle_GL](Oracle_GL/AGENTS.md) | Main accounting platform | accounts, fiscal_periods, journal_entries, subledger_feeds, subledger_feed_runs |
| [Public](Public/AGENTS.md) | Universe changelog | _changelog |
| [Records_Vault](Records_Vault/AGENTS.md) | Document repository | documents, document_versions, access_grants, classifications, retention_policies |
| [Reminder](Reminder/AGENTS.md) | SLA tracking + deadline triggers | reminders |
| [SAP_Subledger](SAP_Subledger/AGENTS.md) | AP / fixed assets / leases / prepaid | ap_invoices, fixed_assets, depreciation_schedule, lease_schedules, prepaid_schedules, prepaid_periods, subledger_transactions |
| [Slack](Slack/AGENTS.md) | Internal coordination | slack_channels (C001..C010, C012), slack_messages, slack_users |

## Per-task naming convention

`Tasks/<TASK_DIR>/_aux/Universe_Split/` uses `<service>.<table>.json` (e.g., `oracle_gl.ogl_journal_entries.json`, `sap_subledger.ap_invoices.json`). Records are wrapped as `{"row_data": "<JSON-string>", "source": "<service>.<table>"}` — the actual row fields are in the JSON-encoded `row_data` string. Always parse `row_data` to access the inner fields.
