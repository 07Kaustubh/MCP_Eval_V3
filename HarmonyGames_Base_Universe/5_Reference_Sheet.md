# Harmony Games — Universe Reference Sheet

Use this when writing prompts, Oracle Events, and rubrics to stay consistent with existing universe data. **Universe date: February 28, 2026.** Email domain: `harmonygames.co`. GitHub org: `harmonygames-Games`.

> `Services_Data/` contains the full base export: full service-level JSON plus sharded or nested Slack messages, Gmail threads, GDrive content, and GitHub repository content. `Services_Data/Base_Universe_Complete_Data.json` is the combined export. A live task can differ after its `9_Universe_inject.sql` and `4_Changelog.json` changes; live tool responses control what the Agent can observe. The Agent has no direct Postgres tool.

## Tool capabilities and Persona ACL

`HarmonyGames_Base_Universe/6_Server_Tools_Details.json` is the sole authority for capabilities, exact tool names,
and parameters. [`../Docs/14_Persona_ACL.md`](../Docs/14_Persona_ACL.md) is the
authority for task-visible identity and read visibility.

- **Available services:** Gmail, GDrive, GitHub, Snowflake, Slack, GCal, GDocs, GSheets, GSlides, Trello, Linear, Contacts, and Confluence.
- **Persona-scoped reads:** Gmail, Slack, GCal, GDrive, GDocs, GSheets, and GSlides (the Drive-family inherits Drive's file ACL). List/search results are filtered to the acting user, and direct by-ID retrieval does not bypass visibility; inaccessible records are denied or returned as not found.
- **Unscoped reads:** Contacts, GitHub, Snowflake, Trello, Linear, and Confluence.
- **Context:** Universe Explorer is author god-mode. Agent Runner and Run Verifiers use the same taxonomy-selected required persona. The environment automatically applies `set_acting_user` with the exact roster email after universe load and reapplies it each run and turn. Do not use the persistent, overriding AMV persona dropdown. Acting-user setup is environment configuration, not Agent work or a task-call contribution.
- **Writes:** Persona ACL does not govern writes. Use the catalogs alone to determine write capability; do not assume persona-based write permission or denial.
- **Gmail:** read/search, thread/message/label/profile lookup, and attachment reads; triage writes include message/thread label modifications, batch message-label changes, thread archive, message/thread trash/untrash/delete, and label creation/deletion. There is no send/reply/compose and no single-message archive tool.
- **Snowflake:** database/schema/table discovery, table descriptions, query execution/submission, and query history only; it is query/read-only.
- **Other write-capable services:** Slack (post/reply/edit/schedule/draft messages, add/remove reactions, create conversations); Linear (create users/teams/projects/issues/comments; update projects/issues); GitHub (create/update issues, add comments, create/update/merge PRs, create reviews/replies/branches, create/update/delete or batch-push files, create/update/delete labels); Trello (create/update/archive/move/delete cards, add comments/members/labels to cards, create/archive lists, create labels/checklists/items, update check items); GDrive (create folders/files, update metadata/content, move/trash/restore/delete/share); GDocs (create/batch-update/delete); GSheets (create, value update/append, batch-update); GSlides (create/batch-update); GCal (create/update/patch/delete events and RSVP); Confluence (create spaces/pages/comments, update/delete pages, restore page versions, add page labels); Contacts (add/edit/delete).
- **No direct tools:** Firebase, BigQuery, Metabase, App Store Connect, Google Play, AppLovin, Singular, Figma, Carta, CRM, Airtable, QuickBooks, or Stripe. These may appear below as company systems, vendors, topics, or artifacts. Retrieve evidence about them through available Slack, Gmail, Drive/Docs/Sheets/Slides, Linear, GitHub, Confluence, or Snowflake sources as relevant.

---

## Task-visible personas (exact ACL roster)

The machine-readable source is
[`4_Persona_ACL_Roster.json`](4_Persona_ACL_Roster.json), and it is authoritative
over the human-readable table below. Use each email exactly; never derive it
from the name. There are exactly 17 task-visible personas and no task-visible
Finance persona or CFO.

| Persona key | Name | Email | Role | Department |
|----|------|-------|-------|------|
| claire_morgan | Claire Morgan | claire.morgan@harmonygames.co | Art Lead | Design |
| marcus_bennett | Marcus Bennett | marcus.bennett@harmonygames.co | Artist | Design |
| samuel_turner | Samuel Turner | samuel.turner@harmonygames.co | Game Designer | Design |
| martin_walsh | Martin Walsh | martin.walsh@harmonygames.co | Game Designer | Design |
| simon_walker | Simon Walker | simon.walker@harmonygames.co | Data Analyst (Contractor) | Engineering |
| victor_barnes | Victor Barnes | victor.barnes@harmonygames.co | Game Engineer | Engineering |
| brian_foster | Brian Foster | brian.foster@harmonygames.co | Game Engineer | Engineering |
| calvin_price | Calvin Price | calvin.price@harmonygames.co | Game Engineer (Unity VFX) | Engineering |
| owen_baker | Owen Baker | owen.baker@harmonygames.co | Game Engineer (Unity) | Engineering |
| vincent_parker | Vincent Parker | vincent.parker@harmonygames.co | Game Systems Engineer | Engineering |
| oliver_brooks | Oliver Brooks | oliver.brooks@harmonygames.co | Senior Game Engineer | Engineering |
| douglas | Douglas | douglas@harmonygames.co | Software Engineer | Engineering |
| frederick_stone | Frederick Stone | frederick.stone@harmonygames.co | Co-founder | Executive |
| robert | Robert | robert@harmonygames.co | Co-Founder & Creative Director | Executive |
| leonard_hayes | Leonard Hayes | leonard.hayes@harmonygames.co | Co-founder & Creative Director | Executive |
| arthur_blake | Arthur Blake | arthur.blake@harmonygames.co | Co-founder & CTO | Executive |
| julia_lawson | Julia Lawson | julia.lawson@harmonygames.co | Product Manager | Product |

## Additional storyline identities (not selectable personas)

These people and tokens can appear in service data but are not identities in
the Persona ACL roster.

| ID | Name | Email | Title | Dept |
|----|------|-------|-------|------|
| matthew_collins | Matthew Collins | matthew@harmonygames.co | Co-Founder & CEO | Executive |
| michelle_carter | Michelle Carter | michelle.carter@harmonygames.co | General Counsel | Executive |
| benjamin_clark | Benjamin Clark | benjamin.clark@harmonygames.co | Co-Founder & CEO (outside counsel in narrative) | Executive |
| felix_young | Felix Young | felixyoung@harmonygames.co | Feature Lead | Engineering |
| person_0001 | EMPLOYEE_0032 | employee_0032@harmonygames.co | Senior Unity Engineer | Engineering |
| marcus | Marcus | marcus.lee@harmonygames.co | Backend Engineer | Engineering |
| lucas | Lucas | lucas@harmonygames.co | Game Developer (contractor) | Engineering |
| person_0015 | Person 6072 | person_6072_slack_id@example.com | Game Developer | Engineering |
| oscar_bennett | Oscar Bennett | oscar@harmonygames.co | VFX/Character Ability Artist | Design |
| ozhan | Ozhan | ozhan@example.com | Freelance Character Animator | Design |
| marcus_lee | Marcus Lee | marcus.lee@harmonygames.co | User Acquisition Manager | Marketing |
| george_miller | George Miller | george.miller@harmonygames.co | User Acquisition Manager | Marketing |
| megan_wilson | Megan Wilson | megan.wilson@harmonygames.co | User Acquisition Manager | Marketing |
| victoria_lane | Victoria Lane | victoria.lane@harmonygames.co | User Acquisition Manager | Marketing |
| christopher_allen | Christopher Allen | christopherallen@harmonygames.co | Marketing Site Contractor | Marketing |
| tim_steudler | Tim Steudler | tim.steudler@example.com | BD Manager, Licensing (Mattel) | Sales |
| patrick | patrick | patrick@harmonygames.co | BD / Partnerships Manager (Solsten) | Sales |
| josh_dempsey | Josh Dempsey | josh.dempsey@example.com | BD Manager (Solsten) | Product |
| person_0008 | Person 5536 | person_5536@example.com | BD / Partnerships (web distribution) | Sales |
| thomas_baker | Thomas Baker | thomas.baker@harmonygames.co | General Counsel (Orrick) | General |
| person_0002–0005 | Person 3011 / 2568 / 5402 / 3123 | person_*@example.com | BD / Operations / Legal-Ops (Superplay/TYZ) | Operations |
| person_0006–0007 | Person 3086 / 3299 | person_*@example.com | UA Managers (Adjoe) | Marketing |
| person_0009–0011 | Person 3937 / 6073 / 6078 | person_*@example.com | BD Playable-Ads (PlayableX) | Marketing |
| person_0012–0014 | Olivia (6062) / Person 0498 / Person 3009 | person_*@example.com | UA / Vendor (Node Media) | Marketing |

*(Service data contains roughly 52 named or tokenized identities; contacts
holds 178 rows and Slack users 218, including external contacts and redacted
tokens. These counts do not expand the 17-person task-visible ACL roster.)*

---

## External Companies & Contacts

**Investors / board:** Griffin Gaming Partners (Series Seed lead, $3M @ $10M post), Sisu Capital & Play Ventures (2023 competing term sheets), 1AM Gaming, a16z Games Speedrun, GFR Fund, General Catalyst, Turkish fund (2025 bridge rejections), TOR Capital + Carta (angels / cap table).
**Legal:** Rimon PC (Benjamin Clark / James Ballard), Orrick (Thomas Baker), TYZ Law (Superplay patent), Michelle Carter (GC).
**UA / ad & data vendors:** AppLovin (Marcus Lee, George Miller), Adjoe, Node Media, PlayableX, Google Ads, Singular (attribution), Solsten (player insights — Josh Dempsey, patrick), Helpshift (support), Deel (payroll).
**Partners:** Mattel Game Studios (Tim Steudler — Barbie "Dream Life Glow"), CrazyGames + BoomBit (web/mobile distribution), Big Time / Open Loot (4X crypto).
**Competitors referenced:** Superplay ("Domino Dreams"), Royal Match, Match Factory, Solitaire Grand Harvest, Candy Crush, Tile Busters.

---

## Slack (985 channels; sample of names)

`#founders`, `#admin_foundersonly`, `#investors`, `#pitch-deck`, `#financial-model-1881`, `#product`, `#recruiting`, `#industry`, `#company-building`, `#engineering-bots`, `#builds`, `#god-gameart`, `#god-ui-ux`, `#god-vfx`, `#game-design`, `#analytics`, `#leaderboards`, `#season-pass`, `#winandcollect`, `#zm-collect-win`, `#river-rush`, `#difficulty-optimization`, `#prototype`, `#4xgame` / `#4xgameproposal`, `#mattel_proposal`, `#zombie-design`, `#zombie-bugs`, `#zombie-match3d`, `#zombie-match-lite`, `#telegram-dd`, `#aa_boardmeeting_room`, `#vendors`, `#node-external`, `#ad_monetization`, `#recruiting_senior_unity_engineer`, `#company-internal`, plus many `mpdm-*` multi-person DMs and per-vendor Slack Connect channels. Channel fields: `id, name, is_channel, is_private, is_im, is_mpim, is_archived, is_general, num_members, created_ts`.

---

## Linear

**Teams:** `team_ENG` Engineering (ENG), `team_ART` Art (ART), `team_DES` Design (DES), `team_EPI` Epic (EPI), `team_ZOM` Zombie Match 3D (ZOM).
**Projects:** `GoD - Beta` (team_ENG), `Zombie Match 3D` (team_ZOM).
**Issue keys:** `ENG-`, `ART-`, `DES-`, `ZOM-` (~3,852 issues; e.g. ENG-636 Quests Backend, ENG-1871 Win Streak, ENG-2065 River Rush, ENG-2377 Telegram DD, ENG-2403/2404 UI/Live-Ops optimization, ZOM-299 Daily Login, ZOM-387 Giant Analytics Ticket, ZOM-521 VFX Master).

---

## GitHub (org `harmonygames-Games`, 16 repos)

| Repo | Role |
|------|------|
| `GameOfDominoes` | GoD / Domino Delights Unity client (primary) |
| `match3d` | Zombie Match 3D Unity client |
| `Combo-Fighters` | Combo Fighter prototype (live experiment) |
| `MinigamePrototypes` | prototype minigames |
| `rpg-prototype` | Dominoes & Dragons RPG (stalled) |
| `liveops` / `liveops-dashboard-buddy` | live-ops backend + dashboard |
| `game-analytics-pipeline` | analytics pipeline |
| `game-of-dominoes-backend` / `match3d-backend` / `match3d-backend-auth` / `auth-game-backend` | backend services (Python/FastAPI, Elixir/Nakama) |
| `match3d-quests` | ZM3D quests |
| `ZM-Liveops-Docs` | ZM live-ops docs |
| `harmony-gpt` | internal AI tooling |
| `website` | harmonygames.co marketing site |

~2,629 PRs / ~12,687 commits. Reviews are frequently **CodeRabbit bot only** (no human reviewer) — relevant when writing rubrics about "review/approval."

---

## Trello (5 boards)

| Board | Purpose / notable lists |
|-------|--------------------------|
| `Harmony Games` | company board — To Do / Doing / Done / Backlog / Recruiting |
| `DD Product Roadmap` | GoD release trains named after codenames: Rebirth, Baklava, Desire (Beta), Elon (Dec 2025), Avengers (Jan), cappadocia (Feb), plus "What we said to the board" |
| `UA/BD` | ZM3D Technical Launch/Alpha, DD Technical Launch, Beta Launch, BD Follow Up, Distribution |
| `ZM ROADMAP` | dated sprint lists (Jun 18 → Nov 5) |
| `Welcome Board` | onboarding |

---

## Confluence (4 spaces, ~31 pages)

- **ENG** — Engineering Home, Architecture Overview, AWS Infrastructure Guide, Backend Services (Elixir/Phoenix), CI/CD & Branching, Nakama Server Setup, Data Model & Event Schema, API Reference, Observability & Alerting, Local Dev Setup, Analytics Integration (Unity→Snowflake).
- **PROD** — Product & Design Home, Domino Delights GDD, Zombie Match 3D GDD, Combo Fighter GDD, Economy Design, Live-Ops Event Engine, Product OKRs 2025 H1, Competitive Analysis (Match Factory), DD 2024 Roadmap (archived).
- **COMPANY** — Company Home, Company Story & Mission, Team & Onboarding.
- **OPS** — Operations & Live Ops Home, Live-Ops Event Calendar & Planning, Analytics & Metrics Dashboards (Metabase), QA Regression Runbook, Release Checklist & Store Submission, Quest System Design & Incident Postmortem, ZM3D Season Pass Spec, Customer Support Playbook.

---

## Google Drive / Docs / Sheets / Slides (key artifacts)

- **GDDs / specs:** Combo Fighter GDD, Progression Philosophy, Zombie Match 3D Level/Item/Monster Design docs, GDD Template, Funnel Completion & Dynamic Difficulty.
- **Finance / legal:** Certificate of Incorporation, Statement of Incorporator, Organizational Consent, Founders Stock Purchase Agreement, Confidentiality/IP Assignment, promissory notes (Blake + others), board decks, financial models.
- **Pitch decks (Slides):** Barbie "Dream Life Glow", fundraising/bridge decks, Crownfall/4X proposal.
- **Sheets:** Player Funnel Summary, Card Packs Simulation, Combo Fighter Design Details, Zombie Match Crashed Users Funnel, Rewarded Ads, VFX Requirements, Art Recruiting, Parameter/Bot optimization sheets.

---

## Snowflake (analytics warehouse — read-only)

Player-behavior tables (funnel, retention, DPS/economy; e.g. `LEVEL_PERFORMANCE` with `game_id` values like `pioneer_delights`, `zombie_match_3d`). Reachable via `snowflake_list_databases`, `snowflake_list_schemas`, `snowflake_list_tables`, `snowflake_describe_table`, and `snowflake_execute_query` (SELECT/WITH/SHOW/DESCRIBE only).

---

## Environment / Universe IDs

- **Environment ID:** `hg4-2026-07-02-env`
- **Base Universe ID:** `hg4-2026-07-02`

These are existing provisioning identifiers. Their embedded date is a legacy label and does not define the universe's simulation date.
