# Slack (stale-to-task pre-baked split)

> Per-task data lives in `Tasks/<TASK_DIR>/_aux/Universe_Split/slack.*.json`. Do not use these files for per-task work.

## Service role

Quick internal coordination. 2,545 messages across 11 channels + 57 users in the base universe.

## Tables (inner shapes, parsed from `row_data`)

| File | Key fields |
|---|---|
| `slack_messages.json` | `message_id`, `channel_id`, `user_id`, `payload` (NOT `text`), `timestamp`, `thread_ts` (parent for thread replies), `mentions` |
| `slack_channels.json` | `channel_id` (`C001`..`C012`), `name`, `topic`, `purpose`, `is_private` |
| `slack_users.json` | `user_id`, `name`, `email`, `profile` (nested with `real_name`, `title`) |

## Parameter trap (critical)

- `slack_conversations_add_message` uses `payload` (NOT `text`). The OE validator blocks `text` for this tool.
- Channel can be specified by `channel_id` (`C010`) or `channel` (`vendor-bills-and-ap`). The platform accepts both.

## Channels

| ID | Name | Purpose |
|---|---|---|
| C001 | #general | firm-wide updates |
| C002 | #water-cooler | non-work chatter |
| C003 | #announcements | one-way broadcast |
| C004 | #client-onboarding | kickoff, document collection |
| C005 | #monthly-close-coordination | close timelines, reconciliations |
| C006 | #tax-prep-and-filings | return prep, deadlines |
| C007 | #audit-engagements | audit support, PBC tracking |
| C008 | #compliance-and-registrations | AML, registrations, annual reports |
| C009 | #cash-management-and-banking | bank feeds, treasury |
| C010 | #vendor-bills-and-ap | vendor onboarding, AP exceptions |
| C012 | (auto-created placeholder) | unused |

## Discovery patterns

- **Thread-reply blindness** is a major Opus 4.8 failure mode. The resolution often sits in a thread reply (`thread_ts != null`), not the top-level message. When designing OEs, explicitly call out thread reply IDs to force the agent to read into the thread.
- **Search-result-cap eviction**: a buried message under high-traffic keywords may not appear in the top results. Pair the keyword with the entity name to narrow.

## MCP tool notes

- Read: `slack_conversations_history` (filter by `channel`), `slack_conversations_search_messages` (filter by `search_query` + optional `filter_in_channel`), `slack_users_list`, `slack_channels_list`
- Write: `slack_conversations_add_message` (`channel_id`, `payload`, optional `thread_ts` for thread reply)
