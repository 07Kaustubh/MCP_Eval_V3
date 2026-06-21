# Messaging (stale-to-task pre-baked split)

> Per-task data lives in `Tasks/<TASK_DIR>/_aux/Universe_Split/messaging.*.json`. Do not use these files for per-task work.

## Service role

DMs and small-group threads. 202 conversations in the base universe. Used for second-eye reviews, partner-routed approvals, compliance signal-checks.

## Tables (inner shapes, parsed from `row_data`)

| File | Key fields |
|---|---|
| `conversations.json` | `conversation_id`, `participants` (list of emails), `subject`, `created_at` |
| `messages.json` | `message_id` (`msg_*`), `conversation_id`, `sender`, `content`, `timestamp`, `parent_message_id` |

## Parameter trap

- `messaging_send_message` uses `content` (NOT `body`).

## Discovery patterns

- Late-superseding messages are a recurring hardness lever: an earlier reply says one thing, a later reply in the same thread overrides it (the Task 14 account-132000 FX-drift "treat as acceptable noise" → "corrective JE is the right call" pattern). The agent must read past the first response.

## MCP tool notes

- Read: `messaging_list_conversations`, `messaging_get_conversation`, `messaging_search_conversations`
- Write: `messaging_send_message`
