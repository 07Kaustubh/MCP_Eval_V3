# Harmony Games — An In-Task Universe

## The short version

**Harmony Games** is a small, founder-led **mobile game studio** building casual puzzle games. Founded in 2023, the founders rejected an NFT concept and pivoted to a domino-matcher — **Game of Dominoes**, shipped as **Domino Delights** — then raised a **$3M Series Seed at $10M post** led by **Griffin Gaming Partners**. A second title, **Zombie Match 3D** (`match3d`), followed in 2025. The late-2025→early-2026 arc is existential: burn-rate collapse, a **failed $2.5M bridge round**, a run of prototypes (Combo Fighter, Zombie Match Lite, a Barbie/Mattel pitch, a 4X crypto concept), and a **company wind-down** underway by February 2026.

The depth of this universe comes from **cross-system threading across a real game-studio tool stack** — a Slack decision becomes a Linear ticket becomes a GitHub PR becomes a Drive spec, with vendor/investor context living in Gmail — not from invented complexity. An agent reading only Slack + Gmail will miss half the story; the actual state of work lives in Linear, GitHub, Trello, Drive/Sheets, Confluence, and Snowflake.

Today inside the universe is **2026-02-28**. The scripted data runs Jan 2023 – Feb 2026, so no storyline occurs after today.

## By the numbers

| Dimension | Harmony Games |
| :---- | :---- |
| Narrative people | **~30 storyline identities** (founders, engineering, design/art, product, UA/BD, contractors) |
| Selectable task personas | **17 exact roster entries**; storyline presence does not make another identity selectable |
| Available tool services | **13** (Gmail, GDrive, GitHub, Snowflake, Slack, GCal, GDocs, GSheets, GSlides, Trello, Linear, Contacts, Confluence) |
| Pre-built storylines | **76 across 10 lenses** |
| Task categories | **6 business functions** (Engineering/Live-Ops 25%, Product/Design 20%, Growth/UA 15%, Founders/Exec 15%, Finance/Legal/HR/Ops 15%, Analytics/Data 10%) |
| Slack | **~586K messages** across **985 channels**, 218 users |
| Gmail | **~24.7K messages** / **~21.2K threads** |
| GitHub | **16 repos**, **~2.6K PRs**, **~12.7K commits**, 884 PR comments (org `harmonygames-Games`) |
| Linear | **~3.85K issues**, 5 teams, 2 projects |
| Google Drive | **~53.7K files** (Docs 67, Sheets 26 / 101 tabs, Slides decks) |
| Trello | **5 boards**, 803 cards, 48 lists, 5.3K actions |
| Confluence | **4 spaces**, ~31 pages |
| HQ | Remote-first · email domain `harmonygames.co` |

## The systems Harmony Games runs on

Four systems hold the operational state of record:

- **Slack** (~586K msgs / 985 channels) — primary internal coordination; per-feature, per-vendor, and founder channels plus many multi-person DMs. Where decisions get made.
- **Linear** (~3.85K issues) — the work-of-record. Teams ENG/ART/DES/EPI/ZOM; projects `GoD - Beta` and `Zombie Match 3D`. Ticket status is how you tell shipped from stalled.
- **GitHub** (16 repos / ~2.6K PRs) — the code-of-record. PR merged? branch alive? review actually human (vs CodeRabbit bot)? Repos map to titles.
- **Google Drive/Docs/Sheets/Slides** (~53.7K files) — design-of-record (GDDs), money-of-record (financial models, board decks, promissory notes, cap-table docs), pitch-of-record (Mattel/investor decks).

Rounding out the stack:

- **Gmail** (~24.7K msgs) — external-of-record: investors, counsel, UA/data vendors, partners. Supports read/search plus triage writes (message/thread labels, thread archive, trash/untrash/delete, and label creation/deletion), but **no send/reply/compose**.
- **Trello** (5 boards) — roadmap-of-record (release-train lists).
- **Confluence** (4 spaces) — durable wiki (architecture, GDDs, runbooks, OKRs).
- **Contacts** — address book (178 rows).
- **Google Calendar** — calendars, events, availability, invitations, and RSVP actions.
- **Snowflake** — analytics-of-record (funnel/retention/DPS), read-only.

### Tool-access boundary

`HarmonyGames_Base_Universe/6_Server_Tools_Details.json` is the authoritative tool catalog. The agent has direct tools only for **Gmail, GDrive, GitHub, Snowflake, Slack, GCal, GDocs, GSheets, GSlides, Trello, Linear, Contacts, and Confluence**.

Firebase, BigQuery, Metabase, App Store Connect, Google Play, AppLovin, Singular, Figma, Carta, CRM systems, Airtable, QuickBooks, and Stripe may appear as company systems, topics, or artifacts, but there are **no direct tools** for them. Evidence about those systems must be retrieved through available sources such as Slack, Gmail, Drive/Docs/Sheets/Slides, Linear, GitHub, Confluence, or Snowflake, as relevant.

Only the 17 entries in
[`4_Persona_ACL_Roster.json`](4_Persona_ACL_Roster.json) are selectable task
personas. [`Docs/14_Persona_ACL.md`](../Docs/14_Persona_ACL.md) defines the
active boundary: Gmail, Slack, GCal, GDrive, GDocs, GSheets, and GSlides reads are
persona-scoped; the other six service reads are unscoped, and writes are outside
Persona ACL.

## What carries over (same project framework)

- **Rubrics (V3).** Two categories: **Outcome** (mandatory) and **Process** (optional/rare). Outcome sub-types 1.1 (write-action results), 1.2 (action content), 2.1 (key facts in the final response). Default to stricter Outcomes over reaching for Process.
- **Agent-centric phrasing**, no tool names in rubrics or prompts.
- **Same prompt rules:** no pre-solving, no command lists, no bolting, natural language, agent must fail on some rubrics.
- **Same spec-quality dimensions** and **four stored fields per rubric**:
  `title` (criterion text), `category`, `justification`, and `evidence`.

## What's new for task design (Harmony Games specifics)

- **Engineering/product tool stack, not business-ops.** Write-actions live in Slack, Gmail triage, Linear, GitHub, Trello, Drive/Docs/Sheets/Slides, Calendar, Confluence, and Contacts. There are no direct CRM, Airtable, QuickBooks, or Stripe tools.
- **Gmail supports read/search + triage, not sending.** It can modify message/thread labels; archive threads; trash, untrash, or delete messages/threads; create/delete labels; and read attachments. "Email the vendor" is *not* an available action.
- **Snowflake is read-only** — analytics is evidence, not a write surface.
- **CodeRabbit-only reviews.** Many PRs were "reviewed" only by the CodeRabbit bot — be careful writing rubrics about human review/approval.
- **Full local base export.** The universe contains ~700K+ artifacts. `Services_Data/` contains the full service-level JSON, with large content sharded or nested for Slack messages, Gmail threads, GDrive content, and GitHub repository content. `Services_Data/Base_Universe_Complete_Data.json` is the combined export. These files describe base state; a live task can differ after its `9_Universe_inject.sql` and `4_Changelog.json` changes, and live tool responses control what the Agent can observe. The Agent has no direct Postgres tool.
- **Redacted personas.** Some real actors survive only as `PERSON_XXXX` / `EMPLOYEE_XXXX` tokens (external vendors, a few engineers) — don't build a task's unique ground truth on an unresolvable token.
- **Everything trends toward wind-down.** By the February 28, 2026 "today," the company is post-bridge-failure and winding down; many arcs (Mattel, Telegram DD, Zombie Match Lite, 4X) end unresolved/stalled — good material for "reconstruct what actually happened / what's still open" tasks.

## The personas you'll see most often

This narrative shortlist includes prominent storyline people; task selection is
limited to the exact 17-entry roster linked above.

| Name | Title | Best for |
| :---- | :---- | :---- |
| **Leonard Hayes** | Co-founder & Creative Director | Fundraising, live-ops strategy, vendor/partner arcs, runway/wind-down, Mattel pitch |
| **Arthur Blake** | Co-founder & CTO | Engineering tooling, difficulty-sim, WebGL/build-size, backend, board/equity |
| **Robert** | Co-founder & Creative Director | Game design, difficulty/economy, character VFX, Combo Fighter |
| **Frederick Stone** | Co-founder / Head of BD & UA | UA vendor arcs (AppLovin/Adjoe/Node/PlayableX), ASO, attribution |
| **Brian Foster** | Head of Product & Live-Ops | Live-ops features (Season Pass, Collect & Win, Win Streak, Daily Login), UI optimization |
| **Julia Lawson** | Product Manager | GDD-vs-implementation, puzzle pipeline, Mattel deck, prototype scoping |
| **Douglas** | Senior Backend Engineer | Backend/analytics pipelines, Quests/Leaderboards backend, live-incident compensation |

## Where to dig deeper

- [**Summary**](1_Universe_Summary.md) — company, org chart, all 76 storylines by lens, systems. Start here.
- [**Persona Briefs**](2_Persona_Briefs.md) — per-persona active work, relationships, open threads.
- [**Task Categories**](3_Task_Categories_Business_Functions.md) — 6 business functions, exact write-capability matrix, Outcome/Process guidance, worked prompts.
- [**Reference Sheet**](5_Reference_Sheet.md) — dense reference: personas, externals, Slack/Linear/GitHub/Trello/Confluence/Drive/Snowflake structures, env/universe IDs.
- **Authoritative tool catalog:** [`HarmonyGames_Base_Universe/6_Server_Tools_Details.json`](../HarmonyGames_Base_Universe/6_Server_Tools_Details.json) — per-service JSON inventories with the exact available tool names and parameters.
- **Repository navigation:** [root README](../README.md) · [Docs index](../Docs/README.md).
- [**Get Universe Data**](8_Get_Universe_Data.sql) — SQL to extract the full universe from Postgres.
