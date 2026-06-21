# Email (stale-to-task pre-baked split)

> Per-task data lives in `Tasks/<TASK_DIR>/_aux/Universe_Split/email.emails.json`. Do not use these files for per-task work.

## Service role

Formal communications and audit trail. 1,379 messages in the base universe.

## Tables (inner shapes, parsed from `row_data`)

| File | Key fields |
|---|---|
| `emails.json` | `email_id`, `sender`, `to_json` (list), `cc_json` (list), `subject`, `content`, `folder`, `parent_id` (threading), `timestamp`, `is_read`, `keywords_json` |
| `threads.json` | Empty in base universe — threading is implicit via `parent_id` in `emails.json` |
| `mailboxes.json` | Empty in base universe |
| `jmap_emails.json` | Empty in base universe |

## Parameter trap (critical)

- `email_send_email` and `email_reply_to_email` use `content` (NOT `body`) for the message text. The OE-format validator blocks `body` for these tools.
- `sender` field is required; this is where the acting persona's email must appear.
- `cc` is a list of email addresses, not a single string.

## Discovery patterns

- Reply chains follow `parent_id`. To find a reply, search for messages whose `parent_id` equals an earlier `email_id`.
- Buried replies are a major Opus 4.8 failure mode. When designing OEs, explicitly call out the reply that flips the conclusion.
- Search by `keywords_json` field for thematic clusters.

## MCP tool notes

- Read: `email_search_emails`, `email_list_emails`, `email_get_email`
- Write: `email_send_email`, `email_reply_to_email`
- Both write tools require `sender`, `to` (list), `subject`, `content` (and optionally `cc`).
