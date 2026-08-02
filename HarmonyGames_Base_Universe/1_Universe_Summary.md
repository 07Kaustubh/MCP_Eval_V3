# Harmony Games — Universe Summary

> **Harmony Games Universe — fixed today's date: February 28, 2026 (Saturday).** All instructions, examples, and relative-time references resolve against this date. The underlying data spans **January 2023 – February 28, 2026**, so no scripted storyline occurs after today; anything after February 28, 2026 is the future.

## The Company

**Harmony Games** (also styled "HarmonyGames") is a small, founder-led **mobile game studio** building casual puzzle games. Founded in early 2023, the founders rejected an initial NFT-based concept and pivoted to a domino-matching puzzle game — **Game of Dominoes (GoD)**, shipped to the iOS App Store beta as **Domino Delights** — as the flagship product. They raised a **$3M Series Seed at a $10M post-money valuation** in mid-2023, led by **Griffin Gaming Partners**, converting to a Delaware C-corp.

Facing a retention ceiling in the casual market, the studio began a second title, **Zombie Match 3D** (internally `match3d`), in early 2025 and shipped it to the App Store mid-2025. Through late 2025 into early 2026 the arc turns existential: **deteriorating runway**, a **failed $2.5M bridge round**, a string of experimental prototypes (Combo Fighter, Zombie Match Lite, a Barbie/Mattel pitch, a 4X crypto concept), and an eventual **company wind-down** underway by February 2026.

**Headquarters:** distributed / remote-first (US + international contractors)
**Founded:** 2023
**Size:** ~30 people (founders, engineers, artists, designers, UA/BD, contractors)
**Email domain:** `harmonygames.co`
**Timeline:** January 2023 – February 2026

### Products

| Product | Internal name | What it is |
|---|---|---|
| **Game of Dominoes / Domino Delights** | `GameOfDominoes` / GoD / DD | Casual domino-matching puzzle built in Unity. Dynamic/adaptive difficulty (Bayesian + bot-simulation tuning), a live-ops economy (leaderboards, win-streak, quests, season pass, daily login), ad monetization (AppLovin MAX), analytics Firebase→BigQuery→Metabase→Singular. |
| **Zombie Match 3D** | `match3d` / ZM3D | Match-3 puzzle with a zombie/horror theme, started 2025. Unity client + backend (leaderboards, live-ops). Season Pass, win-streak, Collect & Win ported from GoD. A lighter "Zombie Match Lite" variant was explored and stalled. |
| **Prototypes / R&D** | various | Combo Fighter (fighting-meets-match-3, live on the App Store), Tile Dozer, River Rush, Dominoes & Dragons RPG, 4X Crypto Conquerors, and a Barbie "Dream Life Glow" idle life-sim pitched to Mattel. |

---

## Org Chart

> **Note:** this org chart includes storyline identities, contractors, and
> external participants. Only the 17 exact entries in
> [`Persona_ACL_Roster.json`](Persona_ACL_Roster.json) are selectable task
> personas. Use the roster for identity fields and
> [`2_Persona_Briefs.md`](2_Persona_Briefs.md) for role context; storyline
> presence does not make another identity selectable. Several external
> contacts appear only as redacted `PERSON_XXXX` / `EMPLOYEE_XXXX` tokens.

### Executive / Founders
| Name | Title | ID |
|------|-------|----|
| **Leonard Hayes** | Co-founder & Creative Director (primary operator — product, fundraising, live-ops) | `leonard_hayes` |
| **Arthur Blake** | Co-founder & CTO (engineering, financial model, board/equity) | `arthur_blake` |
| **Robert** | Co-founder & Creative Director (game design, art direction, difficulty tuning) | `robert` |
| **Frederick Stone** | Co-founder / Head of BD & User Acquisition | `frederick_stone` |
| **Matthew Collins** | Co-Founder & CEO (advisor/board, legal response) | `matthew_collins` |
| **Michelle Carter** | General Counsel (seed financing legal close) | `michelle_carter` |

### Engineering
Brian Foster (Game Engineer / Head of Product & Live-Ops), Vincent Parker (Game Systems Engineer), Victor Barnes (Art Director in narrative), Douglas (Senior Backend Engineer), Owen Baker (Game Engineer, Unity / Eng Lead), Oliver Brooks (Senior Game Engineer), Calvin Price (Unity/VFX Engineer), Simon Walker (Data Analyst, contractor), EMPLOYEE_0032 (Senior Unity Engineer), Felix Young (Feature/Backend Lead), Marcus (Backend Engineer), Lucas (contractor Game Developer), Person 6072 (Game Developer).

### Design / Art
Martin Walsh (Game Designer / UI artist), Marcus Bennett (Artist / VFX), Claire Morgan (Art Lead), Samuel Turner (Game Designer), Oscar Bennett (VFX / character-ability artist), Ozhan (freelance character animator).

### Product
Julia Lawson (Product Manager, game design / live-ops).

### Marketing / User Acquisition
Marcus Lee & George Miller (UA / AppLovin), Megan Wilson & Victoria Lane (UA — Adjoe), Christopher Allen (marketing-site contractor), plus several `Person_XXXX` UA/vendor-partnership managers (Node Media, PlayableX, Adjoe playable-ad vendors).

### Sales / BD
Tim Steudler (Mattel BD/licensing — external), patrick (Solsten partnerships), Person 5536 (web-distribution partnerships).

### Legal / Ops (external counsel & advisors)
Thomas Baker & Benjamin Clark (outside counsel — Rimon/Orrick seed close), plus redacted Business-Development/Operations contacts tied to the Superplay/TYZ Law patent matter.

---

## Communication & Work Systems

Harmony Games runs on a **game-studio tool stack** (not a business-ops stack). The state of record is spread across:

> **Tool authority and boundary:** `HarmonyGames_Base_Universe/Tool_Access/*.json` is authoritative. Directly available services are Gmail, GDrive, GitHub, Snowflake, Slack, GCal, GDocs, GSheets, GSlides, Trello, Linear, Contacts, and Confluence. There are no direct Firebase, BigQuery, Metabase, App Store Connect, Google Play, AppLovin, Singular, Figma, Carta, CRM, Airtable, QuickBooks, or Stripe tools. Those names below describe company systems, vendors, topics, or artifacts; retrieve evidence about them through Slack, Gmail, Drive/Docs/Sheets/Slides, Linear, GitHub, Confluence, or Snowflake as relevant.

> **Persona ACL boundary:** task identity comes only from the 17-entry
> [`Persona_ACL_Roster.json`](Persona_ACL_Roster.json), with read visibility
> governed by [`Docs/15_Persona_ACL.md`](../Docs/15_Persona_ACL.md). Gmail,
> Slack, GCal, and Contacts reads are persona-scoped; the other nine service
> reads are unscoped, and writes are outside Persona ACL.

> **Base export vs. live task state:** `Services_Data/` contains the full base service-level JSON. Large content is sharded or nested for Slack messages, Gmail threads, GDrive content, and GitHub repository content; `Services_Data/Base_Universe_Complete_Data.json` is the combined export. A live task can differ after its `9_Universe_inject.sql` and `4_Changelog.json` changes, and live tool responses determine what the Agent can observe.

- **Slack** — primary internal comms. **985 channels** total (product, engineering, founders, investors, live-ops, per-feature and per-vendor channels, plus many multi-person DMs). Representative channels: `#founders`, `#admin_foundersonly`, `#investors`, `#pitch-deck`, `#product`, `#recruiting`, `#engineering-bots`, `#builds`, `#god-gameart`, `#god-ui-ux`, `#god-vfx`, `#game-design`, `#analytics`, `#leaderboards`, `#season-pass`, `#winandcollect`, `#river-rush`, `#prototype`, `#4xgame`, `#mattel_proposal`, `#aa_boardmeeting_room`, `#vendors`, `#node-external`, `#difficulty-optimization`. (~586K messages.)
- **Linear** — engineering/design PM. **5 teams** (ENG Engineering, ART Art, DES Design, EPI Epic, ZOM Zombie Match 3D) and per-title projects (`GoD - Beta`, `Zombie Match 3D`). ~3,852 issues (ENG-/ART-/DES-/ZOM- keys).
- **GitHub** — source & PRs. Org **`harmonygames-Games`**, **16 repos** including `GameOfDominoes`, `match3d`, `liveops`, `Combo-Fighters`, `rpg-prototype`, `MinigamePrototypes`, `website`, `game-analytics-pipeline`, plus backend repos (`match3d-backend`, `game-of-dominoes-backend`, `auth-game-backend`). ~2,629 PRs / ~12,687 commits. Heavy use of the CodeRabbit review bot.
- **Google Drive / Docs / Sheets / Slides** — GDDs, specs, financial models, pitch decks, legal docs. ~53K Drive files. Key docs: MVP requirements, Progression Philosophy GDD, Combo Fighter GDD, promissory notes, Certificate of Incorporation, Founders Stock Purchase Agreement, board decks, financial models, the Barbie "Dream Life Glow" pitch deck.
- **Gmail** — external correspondence: investors, outside counsel, vendors (AppLovin, Adjoe, Node Media, Singular, Solsten), and partners (Google Ads, Mattel, CrazyGames). ~24.7K messages across ~21K threads.
- **Trello** — product roadmap. **5 boards**: `Harmony Games`, `DD Product Roadmap`, `UA/BD`, `ZM ROADMAP`, `Welcome Board`.
- **Confluence** — wiki. **4 spaces**: `ENG` (Engineering), `PROD` (Product & Design), `COMPANY`, `OPS` (Operations & Live Ops).
- **Contacts** — address book for staff, contractors, investors, vendors, and legal contacts.
- **Google Calendar** — calendars, events, availability, invitations, and company scheduling.
- **Snowflake** — analytics warehouse for player funnel, retention, and DPS/economy tables.

---

## Scenarios (76 storylines across 10 lenses)

The universe is organized into **10 scenario lenses**. Storylines thread across services (a single arc typically spans Slack + Linear + GitHub + Drive/Gmail). Threading across storylines is a feature: e.g., the Superplay patent threat recurs across founders-exec, fundraising, and gmail lenses; the Season Pass and Collect & Win features appear in both GoD and match3d.

### founders-exec — Founders & Executive Track (5)
Vetting Arthur Blake & sizing founding bets · contractor pay cadence / equity philosophy / Delaware incorporation · recurring cash-conscious retreat planning (2023–24) · NFT/hypercasual pivot debate vs staying the course · the Mattel Barbie "Dream Life Glow" idle-sim pitch.

### fundraising-finance-legal — Fundraising, Finance & Legal (8)
Building the 2023 seed financial model · 2023 seed round (competing term sheets, Griffin wins) · closing the Series Seed with Griffin (SPA/IRA/voting agreement) · founder bridge loans before the seed closed · Superplay/TYZ Law patent threat over domino mechanics · advisor equity program via Carta · 2024 quarterly board cadence & investor reporting · 2025 fundraising: the Crownfall crypto pivot and the failed bridge round.

### marketing-growth-gtm — User Acquisition, Marketing & GTM (8)
Female-35+ TAM thesis via Solsten · naming "Domino Delights" (shortlist → IP lawyer → website) · building harmonygames.co with contractor Christopher Allen · inbound BD wave after the seed press release · Marcus Bennett's in-house UA video pipeline · Domino Delights AppLovin soft launch (AU/NZ/CA) · ASO readiness & Node-managed UA prep · Zombie Match 3D naming, App Store assets & alpha→beta launch.

### analytics-data-stack — Analytics & Data Infrastructure (8)
Firebase→BigQuery→dashboards pipeline · AWS S3→BigQuery pipeline · Singular attribution rollout & cross-platform discrepancy hunt · Firebase Remote Config A/B testing infra · funnel-data-driven early-tutorial redesign · stalled player-compensation tool · Bayesian pity/win-rate optimization for Domino Delights · rebuilding Zombie Match 3D analytics instrumentation from scratch.

### live-ops-events-economy — Live-Ops, Events & Player Economy (8)
Quests (backend→shipped retention feature) · Collect & Win (design, match3d rebuild, live tuning) · Win Streak "Nathan's Treasure" · Leaderboards (Dec 2024 launch & scaling fixes) · offers/IAP store build-out · ad monetization (rewards, ad-removal IAP, LTV-based silent interstitials) · Season Pass (GoD → match3d port) · Zombie Match3D daily login/gift rewards.

### product-prototypes — Product Prototypes & R&D (7)
Tile Dozer (contractor prototype → GoD minigame) · Dominoes & Dragons RPG (stalled) · River Rush race event · 4X Crypto Conquerors (brainstorm → stalled Big Time proposal) · Barbie "Dream Life Glow" Mattel pitch · Zombie Match Lite (stalled) · Combo Fighter (live R&D experiment).

### gmail — Business Email Threads (9)
Solsten player-insights partnership · AppLovin UA partnership (deal → sunset) · TYZ Law patent engagement · Google Ads onboarding as UA partner · Node Media playable-ad vendor arc · PlayableX playable-ad vendor engagement · Mattel Barbie licensing pursuit · web-distribution partnership negotiation · Adjoe incentivized-UA test.

### designart — Design & Art Direction (7)
Designing Sophie (UX concept → 3D marketing art) · character selection/profile UI redesign · Sophie/Nathan ability VFX (custom-vs-generic debate) · scaling the puzzle layout pipeline to 1200 levels · onboarding freelancer Ozhan for ZM3D zombies · Bayesian-tuned dynamic/adaptive difficulty · Progression Philosophy GDD (card economy & wildcard debate).

### epics — Engineering Epics, Multi-source (8)
Arthur Blake's puzzle-editor & bot-tooling saga · standing up backend infra from scratch · Quests backend (Felix + Douglas) · Tutorial Editor backlog for Leonardo · VFX art→engineering handoff (match3d PR #408) · match3d vision bot for automated QA · Telegram Domino Delights MiniApp port · UI sprite-optimization sprint for the CrazyGames WebGL deal.

### hrfinance — HR, Finance & Business Ops (8)
Adopting & scaling Deel for contractor payroll · Elliot Mercer termination + two-person backfill · Leapblock outsourcing art vendor · hiring Douglas (equity-vs-cash) · build-vs-buy pay-per-prototype evaluation · Samuel Galdámez referral hire · hiring two Unity engineers (Aug 2024) · adopting/expanding/terminating Helpshift support SaaS.

---

## Operational tracking (the "source of truth" systems)

Unlike the accounting/CRM universes, Harmony Games' operational state lives in **engineering & product systems**:

- **Linear** is the closest thing to a work-of-record: issue status, assignees, projects, and cycles show what actually shipped vs. stalled. Keys: `ENG-`, `ART-`, `DES-`, `ZOM-`.
- **GitHub** is the code-of-record: PR state (merged/closed), reviews (often CodeRabbit-only), commit history, and per-repo branches show delivery. Repos map to titles (`GameOfDominoes`, `match3d`, `Combo-Fighters`).
- **Trello** is the roadmap-of-record: boards/lists/cards track planned vs. done features (roadmap sprints named after releases).
- **Google Drive/Docs/Sheets/Slides** hold the design-of-record (GDDs), the money-of-record (financial models, board decks, promissory notes, cap-table docs), and the pitch-of-record (investor and Mattel decks).
- **Gmail** holds the external-of-record: investor commitments, legal closings, and vendor contracts/invoices.
- **Confluence** holds durable wiki documentation (ENG/PROD/COMPANY/OPS spaces).
- **Snowflake** holds the analytics-of-record (player funnel, retention, DPS/economy tables).

Cross-service threading is tight: a feature's truth is rarely in one place — a Slack decision → a Linear ticket → a GitHub PR → a Drive spec → (sometimes) a Gmail vendor thread. Tasks that read only Slack + Gmail will miss half the story.
