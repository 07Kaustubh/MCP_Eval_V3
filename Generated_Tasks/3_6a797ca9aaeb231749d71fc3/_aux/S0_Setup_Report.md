# S0 Setup Report — 3_6a797ca9aaeb231749d71fc3

## Universe
- Universe: `harmonygames` (from `_aux/Universe.txt`)
- Framework: `hg` (hybrid — single-model verification like V3 family + V4 injection/submission_gate phases)
- Model under test: Claude Opus 4.7 (universe-scoped exception to hard rule 1)
- Working directory: `Generated_Tasks/` (HG convention, not `Tasks/`)
- Universe today: 2026-02-28 (America/Chicago)
- Last event timestamp seen: 2026-02-22T02:03:50Z
- Records dated after today: 0

## Persona
- Name: Victor Barnes
- persona_key: `victor_barnes`
- Email: `victor.barnes@harmonygames.co`
- Role: Game Engineer
- Department: Engineering
- Roster source: `HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json`
- Brief source: `HarmonyGames_Base_Universe/2_Persona_Briefs.md` lines 66-70
- Persona-ACL note: Victor is subject to the seven-service scoped-read filter (gmail, gcal, gdrive, gdocs, gsheets, gslides, slack). Contacts, github, trello, linear are unscoped. Writes are outside ACL scope.

## Business function
- `Engineering` (from `1_Business_Function.txt`)
- Maps to HG business-function slice `Engineering & Live-Ops` (25%, largest slice)

## Data contract & source of truth
- Contract: `base_export_plus_changelog` (per `Validators/universe_data_source.py`)
- Per-task descriptor `3_UniverseDataForThisTask.json` was 0 bytes on entry; replaced with the upstream 940-byte pointer from `Tasks_Template_harmonygames/`, which is the shape the accessor expects for HG (a pointer, not the data)
- Base data path: `HarmonyGames_Base_Universe/Services_Data/` (symlink to `HarmonyGames_Base_Universe/Data/`); hydration verified via `check_hydration.py`
- Changelog: `4_Changelog.json` = `[]` (empty — no injection performed yet)
- Per-task data sha256 (of the pointer descriptor): `3490592453b404019cf971c7aaf8b4e73c1140e8fcb6b13a635db99b57b64016`

## Record totals (38 sources, 185,618 rows)
Top-density services drawn from `_aux/Universe_Index/service_inventory.md`:
- gdrive.drive_files 53,702
- slack.files 47,968
- github.commit_map 21,208
- github.pull_request_commits 15,938
- github.commits 12,687
- github.timeline_events 12,437
- trello.actions 5,294
- linear.issues 3,852
- gitub.pull_requests 2,629
- linear.attachments 2,027

Full inventory: `_aux/Universe_Index/service_inventory.md`.

## Fact ledger surface (`_aux/Fact_Ledger.json`)
- emails 47 · amounts 41 · dates 1,078
- id_linear_issue 3,859 · id_slack_channel 987 · id_slack_user 218
- id_trello_card 8,783 · id_gdrive_file 53,702
- personas seen in data: 41 · personas declared in roster: 17

## Feasible surface
- 13 tables with enum columns, 16 enum columns total — `_aux/Feasible_Surface.json`

## Injection status
- `9_Universe_inject.sql`: 56 lines, 3,416 bytes, ALL comment lines (0 executable statements). Comment-only template header — no injection yet.
- `validate.py --phase injection` -> PASS (0 fails, 0 warns, 4 notes). Report at `_aux/Validator_Reports/injection.md`. If HARDNESS proposes injecting scenario data, re-run this gate whenever the SQL changes.

## Flags for downstream phases
- Model is Opus 4.7, not 4.8. Every hardness lever must target 4.7 failure modes.
- HG uses `Generated_Tasks/`; every command below routes through this path.
- Gmail is READ-ONLY here (no send/reply/compose/draft tool). Any prompt requiring the agent to "email" someone via gmail is ungradeable.
- Two Slack send tools with different text params exist: `slack_send_message(channel, message)` and `slack_conversations_add_message(channel_id, payload)`.
- Today (2026-02-28) is a Saturday and the last day of February; the weekend-comms rule applies to any routine business message dated today.
- Persona ACL is a hard gate — every required read must be validated from Victor Barnes' Agent/Verifier view, never Universe Explorer god-mode.
- Snowflake and Confluence are RETIRED in V5. `check_retired_servers.py` will fail any prompt / OE that names them or reaches for a verb-scoped stand-in (wiki, knowledge base, analytics warehouse).
