# Contacts (stale-to-task pre-baked split)

> Per-task data lives in `Tasks/<TASK_DIR>/_aux/Universe_Split/contacts.contacts.json`. Do not use these files for per-task work.

## Service role

Vendor / client / regulator / persona contact records. 63 contacts in the base universe.

## Tables (inner shapes, parsed from `row_data`)

| File | Key fields |
|---|---|
| `contacts.json` | `contact_id`, `email`, `first_name`, `last_name`, `job`, `is_user`, `phone`, `description` |

## Notes

- `is_user: true` marks the active acting persona for the current task (per-task flag). Do NOT rely on this to distinguish personas from NPCs universe-wide — it only flags the one persona authoring this task.
- The 34 internal personas + 29 NPCs all share the `@brookfieldcpas.com` email domain in this simulation.
- External vendors / regulators / client-side NPCs use their own domains in `email.emails.json` but have records here too.

## Discovery patterns

- For email-recipient resolution, always grep contacts first to confirm the address before writing the OE / rubric.
- The Universe_Index file `entities_personas.md` is the fast lookup view of this table.

## MCP tool notes

- `contacts_search_contacts`, `contacts_get_contact`, `contacts_list_contacts`
- Search by name + role to disambiguate when two people share a first name.
