# S0 Setup Report — Tasks/38_6a5edd95a6946f6c4d160b5a

## Persona
- **Name:** Denise Morales
- **Role:** Onsite Property Manager
- **Persona ID:** p_013
- **Email:** denise.morales@starpm.com
- **Seniority:** Mid · Department: Property Operations
- **Active hours:** 7 AM–4 PM
- **Scripted footprint:** 1 action in 1 scenario (design-surface)
- **Systems:** Airtable, Slack, Gmail, Google Calendar, Linear

## Business Function
- **Name:** Property Operations (Business Function 1)

## Universe
- **Universe:** starpm (Star Property Management)
- **Detected by:** Validators/universes.py (auto-detection)

## Data Hash
- **SHA-256:** a9272951bdd3a4e3f7bddbd4472f5e4c5b938afbbabba97c8671787b980c9149

## Record Count Totals
- **Total records:** 3,914 across 34 sources

| Source | Records |
|---|---:|
| airtable (all tables) | 249 |
| contacts.contacts | 62 |
| gcalendar (calendars + events) | 585 |
| gmail (messages + threads) | 645 |
| hubspot (all tables) | 673 |
| linear (all tables) | 410 |
| public._changelog | 11 |
| quickbooks (all tables) | 628 |
| slack (channels + messages + users) | 650 |

## Today Date and Horizon
- **Universe today:** 2026-07-01 (America/Chicago)
- **Last event timestamp seen:** 2026-12-30T12:40:00-05:00
- **Records dated after today:** 70

> FLAG: 70 records are dated after universe today (2026-07-01). Per build_universe_index note, these are legitimate — they are future-status records (upcoming calendar events, future due dates). No universe integrity issue.

## Fact Ledger Atom Counts
| Atom type | Count |
|---|---:|
| emails | 208 |
| amounts | 403 |
| dates | 192 |
| id_airtable_record | 171 |
| id_linear_issue | 231 |
| id_linear_comment | 48 |
| id_hubspot_object | 183 |
| id_slack_channel | 8 |
| id_slack_user | 61 |
| id_invoice | 506 |
| personas | 62 |

## Feasible Surface
- 15 tables with enum columns, 19 enum columns total — written to _aux/Feasible_Surface.json
