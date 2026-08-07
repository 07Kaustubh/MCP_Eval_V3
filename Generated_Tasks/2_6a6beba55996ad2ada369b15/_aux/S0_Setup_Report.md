# S0 Setup Report - `2_6a6beba55996ad2ada369b15`

**Universe:** harmonygames (HarmonyGames, `hg` framework); detected + pinned in `_aux/Universe.txt`.
**Persona:** Robert, Co-Founder & Creative Director (Executive); `robert@harmonygames.co`; roster key `robert`.
**Business function:** Executive.
**Per-task data hash (sha256):** `3490592453b404019cf971c7aaf8b4e73c1140e8fcb6b13a635db99b57b64016` (hash of the restored `3_UniverseDataForThisTask.json` pointer).

## Data contract
HarmonyGames uses `base_export_plus_changelog`. `3_UniverseDataForThisTask.json` is a pointer (not data) and `4_Changelog.json` is empty (`[]`), so the task runs on the base HarmonyGames universe. Source of truth: `HarmonyGames_Base_Universe/Services_Data/` (hydrated v2, manifest-matched via check_hydration, exit 0).

## v2 payload hydration (this phase)
S0 opened against a stale v1 payload (blob `30751b...`, 233,946,251 B, 5.1 GB). Per operator ruling the canonical payload is the v2 / 8.1 GB drop, hydrated this phase from the repo's public GitHub Release `harmonygames-payload-v2`:
- 7 assets (6 x 734,003,200 B + 876,294 B), reassembled to a 4,404,895,494 B archive, archive sha256 `53be756d...` (matches MANIFEST + `hydrate_harmonygames.sh` pin).
- Extracted blob sha256 `31cb9ee54367c5b11c9896409ef3b8c021884710858636db28d4ba7fd1fc146b`, 359,094,851 B (canonical v2).
- 296,543 payload files across 13 service dirs, after stripping 308,048 macOS AppleDouble `._*` sidecars the tarball carried (296,543 = the manifest count exactly).
- `check_hydration.py` exits 0: "[OK] harmonygames: payload hydrated and matches its manifest".
- `README_HYDRATE.md` preserved (tracked + gitignore-allowlisted); payload correctly gitignored; temp download cache (`_dist/`) removed after verification.

## Universe scale (full per-service split)
- Split: **852,325 records** across **47,607 sources**, 3.0 GB in `_aux/Universe_Split/` (plus `Universe_complete_data.json`, 1.54 GB). Split peak RSS 2.57 GB, 90s.
- Services present (13): confluence, contacts, gcal, gdocs, gdrive, github, gmail, gsheets, gslides, linear, slack, snowflake, trello.
- Key volumes: contacts 178; confluence 31 pages; slack 985 channels; trello 803 cards.

## Today / horizon
- Universe today: **2026-02-28** (America/Chicago).
- Last event timestamp seen: 2026-02-22T02:03:50Z.
- Records dated after today: **0** (no future-dated anomalies to flag).

## Fact Ledger atom surface (`_aux/Fact_Ledger.json`)
emails 23,928; amounts 5,750; dates 1,171; personas 177; linear ids 3,909; slack channels 1,109; slack users 254; trello cards 9,482; gdrive file ids 53,702. `entities` 0 / `fiscal_periods` 0 (no GL/Airtable in HG; see gaps below).

## Known HG builder gaps (Brookfield/StarPM-shaped builders vs HG tables; non-blocking)
- `entities_personas.md` empty (0 emails): it reads the exact filenames `contacts.contacts.json` / `slack.slack_users.json`, but HG split names carry a doubled service prefix (`contacts.contacts.contacts.json`). The persona/contact surface is instead in `Fact_Ledger.json` (personas 177 + aliases); the 17 ACL personas come from `4_Persona_ACL_Roster.json`.
- `key_facts.md` empty: it only summarizes Brookfield/StarPM tables (Oracle GL, BlackLine, SAP AP, Records Vault, Airtable). HG structured facts live in Linear/GitHub/Trello (see `service_inventory.md` + `Fact_Ledger.ids`).
- `accounts_per_entity.md`: N/A (HG has no GL).
- `graph_report.md`: only "People by artifact density" is populated (slack-id tokens; bot/service ids dominate; `usr_robert`=969). JE/BlackLine/AP/period-pair sections are Brookfield-specific and empty for HG.
`phase_ready --phase hardness` = OK, so these gaps do not block HARDNESS.

## Exit
All S0 exit criteria met against the canonical, manifest-matched v2 payload. Next: `PIPELINE HARDNESS - Generated_Tasks/2_6a6beba55996ad2ada369b15` (fresh chat).
