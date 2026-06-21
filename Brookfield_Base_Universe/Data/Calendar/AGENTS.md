# Calendar (stale-to-task pre-baked split)

> Per-task data lives in `Tasks/<TASK_DIR>/_aux/Universe_Split/calendar.events.json`. Do not use these files for per-task work.

## Service role

Close kickoffs, partner reviews, audit kickoffs, lock targets, CPE sessions. 51 events in the base universe.

## Tables (inner shapes, parsed from `row_data`)

| File | Key fields |
|---|---|
| `events.json` | `event_id`, `title`, `organizer`, `attendees` (list of emails), `start`, `end`, `location`, `description` |

## Common event kinds

- Period close kickoff (BD0)
- Partner sign-off review
- Audit kickoff / PBC walkthrough
- Compliance review
- CPE training session (LatticeHill etc.)
- Onboarding kickoff

## Discovery patterns

- Attendee mismatches between calendar and a vendor invoice are a recurring hardness lever (the LatticeHill CPE overbilling pattern in Task 13).
- Cross-check `events.json` attendees against `email.emails.json` cancellation notices and `slack.slack_messages.json` last-minute drop-out messages.

## MCP tool notes

- `calendar_add_calendar_event` / `calendar_update_calendar_event` / `calendar_delete_calendar_event`
- `calendar_search_events`, `calendar_list_events`
- Always confirm timestamps land in the right timezone (America/New_York / `-04:00` Eastern).
