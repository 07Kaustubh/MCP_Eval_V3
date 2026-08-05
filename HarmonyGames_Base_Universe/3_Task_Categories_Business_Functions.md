# Harmony Games — Task Categories & Business Functions

> Universe date: **February 28, 2026**. Categories are **weighted** (target share of tasks), not credentialing tags — they route by *what the work is*. Weights are a starting proposal derived from the 10 storyline lenses; adjust as the task distribution fills in.

## The 6 Business Functions

| # | Business Function | Target % | Maps from lenses |
|---|-------------------|:---:|---|
| 1 | **Engineering & Live-Ops** | 25% | engineering-epics, live-ops-events-economy |
| 2 | **Product & Design** | 20% | designart, product-prototypes (design side) |
| 3 | **Growth / UA / Marketing** | 15% | marketing-growth-gtm, gmail (vendor UA threads) |
| 4 | **Founders / Exec / Strategy** | 15% | founders-exec, product-prototypes (bets/pitches) |
| 5 | **Finance / Legal / HR / Ops** | 15% | fundraising-finance-legal, hrfinance |
| 6 | **Analytics & Data** | 10% | analytics-data-stack |

Each of the six is described below with typical work, its **write-action surface**, and a worked example prompt (natural request → deep cross-service investigation, agent expected to fail on some rubric criteria).

---

### ⚠️ Universe-specific tool note (read first)
- **Tool boundary:** use the full service summary in the
  [`One-Pager`](0_Universe_One-Pager.md#tool-access-boundary), the exact
  capabilities in the [`Reference Sheet`](5_Reference_Sheet.md#tool-capabilities-and-persona-acl),
  and `HarmonyGames_Base_Universe/6_Server_Tools_Details.json` as authority.
- **Business function is not identity:** select the required persona from the
  exact [`4_Persona_ACL_Roster.json`](4_Persona_ACL_Roster.json). There is no
  task-visible Finance persona or CFO; pair Finance work with an appropriate
  roster persona.
- **Persona ACL:** apply
  [`../Docs/14_Persona_ACL.md`](../Docs/14_Persona_ACL.md) for identity and read
  visibility. The write surfaces below describe catalog capability, not
  persona-based authorization or denial.

---

## 1) Engineering & Live-Ops (25%)
**Typical work:** triaging live bugs across Linear + GitHub + Slack; reconciling what actually shipped (PR merged? ticket Done? Trello card in the right list?); coordinating a live-ops event's client/backend/art handoff; auditing a feature's status across titles (GoD vs match3d); finding stalled/abandoned work.
**Write actions:** `linear_create_issue`/`linear_update_issue`/`linear_create_comment`, `github_create_issue`/`github_add_issue_comment`/`github_create_pull_request_review`, `trello_create_card`/`trello_update_card`/`trello_add_comment`, `slack_send_message`, `confluence_create_page`.
**Worked example:** *"The Season Pass on Zombie Match keeps throwing weird reward bugs after launch and I can't tell what's actually been fixed vs still open. Can you get to the bottom of it, make sure the right tickets reflect reality, and flag anything that's slipped through so the right engineer picks it up?"* → requires reading ZOM Linear tickets + match3d PRs + `#season-pass`/`#zombie-bugs` Slack + the reward spec sheet, noticing a fixed-but-still-open ticket and a minutes-vs-days unit bug, then updating Linear and pinging the owner.

## 2) Product & Design (20%)
**Typical work:** reconciling a GDD/spec (Drive) against what's implemented (Linear/GitHub); difficulty-curve and economy decisions backed by analytics; FTUE/tutorial redesign; roadmap hygiene (Trello); prototype go/no-go reconstruction.
**Write actions:** `gdocs_create_document`/`gdocs_batch_update`, `gsheets_values_update`/`gsheets_values_append`, `trello_create_card`/`trello_move_card`, `linear_create_issue`, `slack_send_message`, `confluence_create_page`.
**Worked example:** *"Robert wants the Combo Fighter progression to actually match what we wrote in the GDD before we push the next build. Check whether the combo rarity/leveling we shipped lines up with the design doc, write up what's off, and get it in front of the team."* → cross-reads the Combo Fighter GDD (Drive), `Combo-Fighters` PRs, `#prototype` Slack, direct Snowflake DPS data, and any Metabase dashboard evidence linked in Slack/Drive/Confluence; writes a discrepancy doc and a Slack summary.

## 3) Growth / UA / Marketing (15%)
**Typical work:** reconstructing a vendor/UA arc (AppLovin, Adjoe, Node Media, PlayableX, Google Ads) across Gmail threads + Slack vendor channels + Trello UA/BD board; ASO/store-listing readiness; attribution discrepancy hunts (Singular); spend/ROAS reconciliation.
**Write actions:** `trello_create_card`/`trello_update_card`, `slack_send_message`, `gdocs_create_document`, `gsheets_values_append`, `linear_create_issue` (creative/ASO tickets), plus Gmail label/archive/trash triage when the request calls for inbox organization. *(Gmail cannot send or reply.)*
**Worked example:** *"I need to know where the Adjoe test actually landed before the board call — what we spent, what the retention looked like, and why we paused. Pull the whole picture together and drop a clean summary in the UA channel."* → reads the Adjoe Gmail/Slack Connect thread, Singular reports or exports referenced in Gmail/Slack/Drive, direct Snowflake evidence where relevant, and `#executives`; computes ~$50–54.5K spend / ~21.5% ROAS / ~4% D30, then posts a Slack summary and/or a Trello card.

## 4) Founders / Exec / Strategy (15%)
**Typical work:** fundraise/board reconstruction; strategic-bet post-mortems (NFT/hypercasual, 4X crypto, Mattel Barbie); partnership status (CrazyGames/BoomBit/Mattel); runway/wind-down synthesis.
**Write actions:** `gslides_batch_update`/`gslides_create_presentation`, `gdocs_create_document`, `slack_send_message` (`#founders`/`#executives`), `gcal_create_event` (board syncs), `linear_create_project`.
**Worked example:** *"Where did the Mattel Barbie pitch actually end up, and what's outstanding if they come back in January? Put together a tight status brief for the founders."* → reads `#mattel_proposal` + the pitch decks (Slides/Drive) + the Gmail Mattel thread + the investor-update email; writes a brief doc + `#founders` summary, notes the deal is unresolved (Mattel shutdown).

## 5) Finance / Legal / HR / Ops (15%)
**Typical work:** cap-table/equity reconstruction (Carta exports, promissory notes, and board consents stored in Drive); patent-matter status (Superplay/TYZ); hiring/offboarding threads (Deel payroll, terminations, referrals); vendor-contract lifecycle (Helpshift, Deel, art vendors).
**Write actions:** `gdocs_create_document`/`gdocs_batch_update`, `gsheets_values_update`, `slack_send_message` (`#admin_foundersonly`), `contacts_add_new_contact`/`contacts_edit_contact`, `confluence_create_page`, `gcal_create_event`.
**Worked example:** *"Before we close the books on Helpshift, make sure we actually paid everything we owe and that both games are moved off it. Confirm the state and write up what's left."* → reads the Helpshift Gmail/Slack termination thread + invoices + the match3d/GoD integration PRs; writes a wind-down status doc and flags the ~$1.5K back-invoices / migration deadline.

## 6) Analytics & Data (10%)
**Typical work:** funnel/retention/DPS analysis (direct Snowflake queries plus Metabase references found in available services); pipeline-health reconstruction from Firebase→BigQuery and Singular evidence in Slack/Gmail/Drive/Linear/GitHub/Confluence; data-discrepancy hunts; instrumentation-gap audits.
**Write actions:** `gsheets_values_update`/`gsheets_create_spreadsheet`, `gdocs_create_document`, `linear_create_issue` (instrumentation gaps), `slack_send_message` (`#analytics`). *(Snowflake is read-only — query for evidence.)*
**Worked example:** *"Something's off between what Singular says and what our own dashboards show for installs — figure out where the gap is and write up what we think is real."* → reads the Singular reconciliation Slack/Gmail thread + Snowflake funnel tables; documents the ~15–38% user-level gap and pseudo-userid/region root cause; files an instrumentation ticket.

---

## Exact Write-Capability Matrix

This matrix is rebuilt from `HarmonyGames_Base_Universe/6_Server_Tools_Details.json`; omitted actions are unavailable. It describes service capabilities, not Persona ACL enforcement.

| Service | Exact available write/action surface |
|---|---|
| Gmail | Modify message/thread labels; batch-modify message labels; trash, untrash, or delete messages/threads; archive threads; create/delete labels. **No send/reply/compose; no single-message archive tool.** |
| GDrive | Create folders/files; update file metadata/content; move, trash, restore, delete, and share files. |
| GitHub | Create/update issues and add issue comments; create/update/merge PRs; create PR reviews and reply to PR comments; create branches; create/update/delete files and push file batches; create/update/delete labels. |
| Slack | Post/reply, edit, schedule, and draft messages; add/remove reactions; create conversations. |
| GCal | Create, update, patch, and delete events; respond to invitations. |
| GDocs | Create, batch-update, and delete documents. |
| GSheets | Create spreadsheets; update/append values; batch-update spreadsheets. |
| GSlides | Create presentations and batch-update presentations. |
| Trello | Create/update/archive/move/delete cards; add comments, members, and labels to cards; create/archive lists; create labels and checklists/check items; update check items. |
| Linear | Create users, teams, projects, issues, and issue comments; update projects and issues. |
| Contacts | Add, edit, and delete contacts. |
| Confluence | Create spaces; create/update/delete pages; restore page versions; add comments and page labels. |
| Snowflake | **None. Query/read-only.** |

---

## Outcome / Process Rubric Guidance

- Use **Outcome** rubrics for required action results, action content, and key final-response facts.
- Use **Process** rubrics only when the process itself is explicitly required and outcome evidence cannot capture it. Do not add tool-selection criteria merely because a service was historically labeled "default" or "non-default."
- Ground any required action in the exact capabilities above. A rubric must not require Gmail sending, Snowflake writes, or direct calls to a non-tool system.
- Validate required Gmail, Slack, GCal, and Drive-family (GDrive/GDocs/GSheets/GSlides) reads from the assigned persona's Agent/Verifier view. Universe Explorer is author god-mode; author-visible evidence may still be inaccessible to the selected persona.
- Do not write a rubric for acting-user setup or assume a persona-based write denial. Scoped list/search/get results, including by-ID denied/not-found behavior, are read-visibility constraints only.
