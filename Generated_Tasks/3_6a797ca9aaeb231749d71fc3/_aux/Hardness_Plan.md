# Hardness Plan — 3_6a797ca9aaeb231749d71fc3

Framework: `hg` (HarmonyGames V5). Model under test: **Claude Opus 4.7** (universe-scoped exception; NOT 4.8). Universe today: **2026-02-28 (Saturday, America/Chicago)**.

**REVISED 2026-08-12: post-ACL re-verification.** The initial plan anchored two levers on Slack channels. Verified against `slack.channels.json` membership: Victor Barnes (`EMPLOYEE_0030_SLACK_ID`) is a member of **zero** channels of any type (public / private / archived / DMs / mpim). Slack is dropped from lever anchoring entirely — reads AND writes. All 5 levers re-anchored on unscoped services (GitHub / Trello / Linear / Contacts) + Victor-owned Drive assets. All 5 levers preserved. Density re-projected: 56 midpoint across 7 services (up from 54 pre-ACL, driven by deeper Trello / GitHub / GDrive descent replacing Slack calls). See `## Lever changes from ACL re-verification` for the diff.

## Persona and Business Function

- **Victor Barnes** — nominal role Game Engineer; per PersonaBrief the actual scope is art/animation lead: character-ability VFX quality, character-profile UI, outsourced art-vendor management (Leapblock, Martin Walsh), Quests art, hero video, UA creative.
- persona_key: `victor_barnes`, email: `victor.barnes@harmonygames.co`, department: Engineering.
- Business function: `Engineering` (maps to HG's Engineering & Live-Ops 25% slice).
- Open threads named in the brief: zombie animation roster (Ozhan), marketing-asset production. Surfaces reachable to Victor (post-ACL): ART Linear tickets (unscoped), Combo-Fighters GitHub repo (unscoped), ZM ROADMAP Trello board (unscoped), Contacts (unscoped), his own Drive folder (own-user Drive reads).

## Levers Available

| # | Lever | Status | Evidence (file:row_id / stem) | Cost range | Learnings cite |
|---|---|---|---|---:|---|
| 1 | Latching | yes | `github.pull_requests` Combo-Fighters PR #1 (draft, `changed_files=0`, `additions=0`, updated 2026-01-21, label `["do not merge"]`) vs merged PR #36 "vfx updates" (2026-02-11) vs PR #16 "win screen coin vfx" (2025-12-21) | 5-8 | L1, L13 |
| 2 | Structured-DB skip | yes | (a) `github.review_comments` on PR #37 (10 line comments, Oliver Brooks CHANGES_REQUESTED) hidden under CodeRabbit summary in `pull_request_comments`; (b) `trello.check_items` on ZM ROADMAP card `6851a9942b47001e59c8e777` — item `Marcus to create VFX` still incomplete; siblings `6852f6014ef0266338b1728b`, `6851aafe8c9e95ec0abbd262` carry incomplete `Provide engineering estimate` items | 4-7 per variant | L2, L10, L28 |
| 3 | Missing reply | ACL-BLOCKED | Requires Slack `messages/` from base export — Victor has zero channel membership so any missing-reply lever on Slack is out of ACL reach. Not selected. | 3-5 | L3 |
| 4 | Search-result-cap eviction | ACL-BLOCKED | Same reason — depends on `slack_search_files` / `slack_search_messages` which are persona-scoped. Not selected. | 3-5 | L4 |
| 5 | Thread-reply blindness | ACL-BLOCKED | Contingent on L3. Not selected. | 2-4 | L5, L12 |
| 6 | Near-miss entity confusion | yes | Four distinct Marcuses: Marcus Bennett `marcus.bennett@harmonygames.co` (Artist persona, `usr_c77c50cc15c5342d`); Marcus Lee `marcus.lee@harmonygames.co` (`usr_b501f018a4c5319f`); `marcus@harmonygames.co` (`usr_d7ae9de750a5640a`); GitHub `PERSON_0396_GITHUB_USERNAME` = "Marcus" with no linked email (author of PRs #1, #16, #36). Also Martin Walsh (persona) vs Martin Lewis (NPC `PERSON_0394`). Triangulation via 3 unscoped services: `contacts.contacts` + `linear.users` + `github.users`. | 3-5 | L6, L4 |
| 7 | Multi-write diversification | yes | Feasible writes (post-ACL): Linear `save_issue` / `save_comment`; Trello `create_card` / `create_check_item` / `update_check_item_state_on_card` / `comment_card`; GitHub `add_pull_request_comment` / `create_pull_request_review` / `add_labels_to_issue`; GDocs `create_document` (creates a doc Victor owns); GSheets `create_spreadsheet` (creates a sheet Victor owns); GDrive `create_file`; Contacts `create_contact`. **Note: HG gmail is read-only; HG Slack write requires the persona to have a plausible destination channel, which Victor does not. Slack writes excluded.** | 9-12 | L7 |
| 8 | Multi-link chain | yes | Revised chain (post-ACL): `contacts.contacts` Leapblock vendor row + Ozhan freelance row -> Trello ZM ROADMAP card `6851a9942b47001e59c8e777` with incomplete `Marcus to create VFX` check_item -> Combo-Fighters PR history (#1 draft vs #16/#36 merged) -> Linear ART/ZOM ticket lineage. Same 4-service traversal, Contacts swapped in for Slack. | 6-9 | L8 |
| 9 | Authority-figure dismissal | yes | Leonard Hayes `leonard.hayes@harmonygames.co` (Co-founder & Creative Director) and Robert `robert@harmonygames.co` (Co-founder & Creative Director) both named as `direction` in the persona brief. Either can plausibly dismiss "the VFX import is still open" with domain-correct-sounding but wrong reasoning. Zero tool-call cost. | 3-5 | L9 |
| 10 | Reversal / supersession | yes | PR #1 (draft, no changes, `head_ref=Marcus/ImportingArtAssets`) has been de facto superseded by merged PR #36 and PR #16 shipping the same VFX. Trello `Marcus to create VFX` check_item (last toggled 2025-06-20, still incomplete) overtaken by merged VFX. ART Linear tickets all 2023-2024 archived Done — live vendor work has moved to Combo-Fighters git | 4-6 | L10, L25 |
| 11 | Net-vs-gross framing | ACL-partial-BLOCKED | Original analog required reading Leapblock invoice PDF from `#leapblock` Slack channel — Victor has no ACL to that channel. Leapblock invoice PDF may exist in Victor's Drive if shared with him; not verified. Held as fallback if S1 finds density thin. | 4-7 | L14, L20 |

### Lever 1 — Latching
PR #1 is a persuasive but stale anchor: title reads like the canonical VFX-import PR, Oliver Brooks named as reviewer, open since 2025-12-02. Reality: `additions=0`, `changed_files=0`, label `["do not merge"]`; Marcus's actual VFX imports shipped in PR #36 (2026-02-11) and PR #16 (2025-12-21). An agent asked "where does the ComboFighter art import stand" reads PR #1 as current status and reports it as in-flight. Anchors reporting frame on a placeholder branch. **Anchor: unscoped `github.pull_requests` — no ACL exposure.**

### Lever 2 — Structured-DB skip (two carriers, one lever)
Variant (a): PR #37 review_comments (Oliver Brooks `Please start enums with E`, the `ComboRarityDefinition` justification exchange, prefab naming pushback) never surface in the PR body or top-level comments (CodeRabbit auto-summary). Variant (b): only 9 of 79 ZM ROADMAP cards carry checklists; the incomplete `Marcus to create VFX` and multiple `Provide engineering estimate` items sit two tool-calls deep from the card list. Both variants require a niche descent (`github_list_review_comments`, `trello_get_check_items`) that agents skip. **Anchor: unscoped `github.review_comments` + unscoped `trello.check_items` — no ACL exposure.**

### Lever 6 — Near-miss entity confusion
Four Marcuses is unusually strong: GitHub author "Marcus" (`PERSON_0396`) has no linked email, so mapping him to Marcus Bennett vs marcus@ requires triangulating `contacts.contacts` + `linear.users` + `github.users`. Owner-attribution rubric fires here. **Anchor: 3 unscoped services (Contacts, Linear, GitHub) — original 4-way triangulation collapsed to 3-way after Slack drop. L6 remains valid because the three unscoped legs still uniquely resolve the four Marcuses; the Slack leg was corroborative not load-bearing.**

### Lever 8 — Multi-link chain (revised)
The revised traversal: `contacts.contacts` Leapblock vendor row (contact card with Martin Walsh's email as primary) + Ozhan freelance-animator contact -> ZM ROADMAP VFX-implementation cards with incomplete `Marcus to create VFX` -> Combo-Fighters merged-vs-draft PR history -> Linear ART/ZOM ticket lineage. Genuine four-service traversal (Contacts, Trello, GitHub, Linear) that fits a natural "before Monday I want to know what art vendor work is actually open" ask. Contacts swap for Slack keeps the chain length and cross-service breadth intact.

### Lever 9 — Authority-figure dismissal
Persona-relayed quote from Leonard or Robert time-anchored Friday 2026-02-27 evening (clear of the weekend-comms rule): plausible-but-wrong dismissal that "Marcus told me the import PR is already covered by the merged VFX branch, so treat that draft as parked." Collapses draft-status ownership with the incomplete check_items and unresolved PR #37 pushback. Uses L24 soft-verb convention ("Marcus told me" not "the import is covered"). **Anchor: prompt sentence — zero tool cost, zero ACL exposure.**

### Lever 10 — Reversal / supersession
PR #1 is a classic supersession decoy: same author, same asset scope, same repo, zero code, superseded by merged PRs #36 and #16. Trello check_items from 2025-06-20 never re-toggled after merge create a supersession discrepancy requiring reconciliation of Trello state against git state. **Anchor: unscoped `github.pull_requests` + unscoped `trello.check_items` — no ACL exposure.**

## Selected Levers (5) — revised anchors

- **L1 Latching** — one-line rationale: PR #1 anchors "art import in progress" reporting frame; merged reality lives in PRs #16, #36. Projected cost midpoint: **6**. Steering placement: **environment only** (in unscoped `github.pull_requests`). Naming PR #1 in the prompt would collapse the lever.
- **L2 Structured-DB skip** (two carriers: GitHub `review_comments` + Trello `check_items`) — rationale: load-bearing content sits two tool-calls deep on both surfaces; PR #37 line comments and ZM ROADMAP `Marcus to create VFX` incomplete items. Projected cost midpoint: **5 (review_comments) + 12 (Trello check_items + deeper actions descent for the Marcus toggle timeline) = 17 combined**. Steering placement: **environment** (both surfaces unscoped). Prompt gives Victor a reason to open recent Combo-Fighters PRs and the ZM ROADMAP board; whether the agent descends is the discrimination.
- **L6 Near-miss Marcus entity** — rationale: four Marcuses force cross-service identity resolution across three unscoped services (Contacts + Linear + GitHub). Projected cost midpoint: **5**. Steering placement: **environment** (identities distributed across the three unscoped services). Prompt refrains from disambiguating.
- **L9 Authority dismissal (Leonard or Robert, Friday 2026-02-27)** — rationale: single sentence in the prompt that dismisses the import PR as "already covered". Zero tool-call cost, high discrimination weight. Projected cost midpoint: **0**. Steering placement: **prompt**. L24 soft-verb convention.
- **L10 Reversal / supersession** — rationale: PR #1 draft-vs-merged supersession and stale Trello check_items add a rubric-visible discrimination beyond L1's frame-anchoring. Projected cost midpoint: **5** (includes commit / timeline_events verification). Steering placement: **environment** (unscoped GitHub + Trello).

**Prompt/environment split:** 1 lever in prompt (L9), 4 in environment. Every environment lever now sits on an unscoped surface (GitHub / Trello / Linear / Contacts), so Slack ACL removal costs zero lever count. Discovery chain remains reachable from surfaces the prompt gives the agent a natural reason to open (recent Combo-Fighters PRs, ZM ROADMAP, cross-service identity resolution via Contacts and Linear).

**L8 multi-link chain** is folded in structurally rather than counted as a separate lever — the Contacts -> Trello -> GitHub -> Linear traversal that the agent must run to satisfy L2 and L10 IS the multi-link chain.

**L11 net-vs-gross** dropped: original anchor was the Leapblock invoice PDF in the `#leapblock` Slack channel (Victor ACL-blocked). Held as fallback only if the Leapblock PDF turns out to be shared to Victor's Drive at S1 verification time.

## Tool-Call Density Projection

| Component | Range | Midpoint | Services touched |
|---|---|---:|---|
| Base discovery (contacts lookup, team resolution, today check) | 5-8 | 6 | contacts, linear |
| L1 latching traversal (list Combo-Fighters PRs, get PR #1, get PR #36, get PR #16, get commits) | 5-8 | 6 | github |
| L2a review_comments sweep on candidate merged PRs (#37 + 1-2 others) | 4-7 | 5 | github |
| L2b Trello check_items traversal (board -> lists -> cards -> checklists -> check_items -> actions) | 10-15 | 12 | trello |
| L6 Marcus disambiguation (linear.users, contacts.contacts, github.users) | 4-7 | 5 | linear, contacts, github |
| L10 supersession verification (PR merge state, commit dates, `updated_at`, timeline_events) | 4-6 | 5 | github |
| L9 authority reasoning (no tool call — logical rejection) | 0 | 0 | — |
| Write actions (Linear `save_comment` + Trello `update_check_item_state_on_card` + Trello `comment_card` + GDocs `create_document` for the status brief + GSheets `create_spreadsheet` for the vendor tracker) x ~2 supporting reads each including GDrive `list_files` in Victor's own folder | 9-15 | 12 | linear, trello, gdocs, gsheets, gdrive |
| Cross-service triangulation buffer | 4-6 | 5 | any |
| **TOTAL projected** | **41-72** | **56** | — |

**Gate verdict: PASS.** HG framework authoring target 40+ calls AND 3+ services — midpoint 56 (40% above the floor), distinct services 7 (well above 3+). Also clears the QC trajectory floor of 15 average by a factor of 3.7x.

**Two corrections applied since the oracle's initial density projection:**
1. **Gmail draft calls removed (pre-ACL correction, kept):** HarmonyGames gmail has NO send / reply / compose / draft tool (weaker than StarPM). Original 3 `create_draft` calls were reallocated to GDocs + GSheets writes.
2. **Slack calls removed (this revision, post-ACL):** Victor is not a member of any Slack channel of any type, so all `slack_*` reads and writes are ACL-blocked. Original 5 discovery reads + 2 write calls (7 total) were reallocated to: deeper Trello `actions` descent for the `Marcus to create VFX` toggle timeline (+2), GitHub commit/timeline_events verification (+1), GDrive `list_files` in Victor's own folder (+1), a second Trello `comment_card` write in place of the Slack post (+2), and the cross-service buffer (+1). Net midpoint moved from 54 to 56.

## Service Breadth (v11 G1) — revised

| Service | Calls | % of total |
|---|---:|---:|
| github | 15 | 27% |
| trello | 15 | 27% |
| linear | 10 | 18% |
| contacts | 5 | 9% |
| gdocs | 4 | 7% |
| gdrive | 4 | 7% |
| gsheets | 3 | 5% |
| **Distinct services** | **7** | — |

**Breadth gate: PASS.** 7 distinct services with 6 of them ≥ 5% share (the seventh is at the boundary at 5%). Well above the HG 3+ services requirement and above the V3-family "4 distinct services with each ≥ 5%" preferred bar. Universe = `harmonygames` per `_aux/Universe.txt`. Cross-correlation is genuinely multi-service, not a single-service deep trap. No single service dominates (highest is github at 27%, tied with trello). Slack removed entirely; Contacts and GDrive added.

## Lever changes from ACL re-verification

Applied 2026-08-12 following operator-directed `check_persona_acl.py` re-run and per-channel membership scan. The initial plan's Verification_hardness.md discrepancy #2 flagged Slack ACL as a S1 pre-check requirement. The check has been executed early and the result is decisive:

| Item | Before | After | Reason |
|---|---|---|---|
| L1 anchor | github.pull_requests | github.pull_requests | unchanged (unscoped) |
| L2a anchor | github.review_comments | github.review_comments | unchanged (unscoped) |
| L2b anchor | trello.check_items | trello.check_items + trello.actions | unchanged (unscoped); depth increased |
| L6 anchor | Contacts + Linear + Slack + GitHub (4-way) | Contacts + Linear + GitHub (3-way) | Slack leg dropped; three unscoped legs still uniquely resolve the 4 Marcuses |
| L8 chain | Slack Leapblock PDF -> Trello -> GitHub -> Linear | Contacts (Leapblock + Ozhan) -> Trello -> GitHub -> Linear | Slack swapped for Contacts; chain length + service count preserved |
| L9 anchor | prompt sentence | prompt sentence | unchanged |
| L10 anchor | github.pull_requests + trello.check_items | github.pull_requests + trello.check_items + timeline_events | unchanged; depth increased |
| Writes | Linear + Trello + Slack + GDocs + GSheets | Linear + Trello + Trello + GDocs + GSheets (Slack post replaced by second Trello comment) | Slack write dropped; second Trello `comment_card` added |
| Reads (Slack-only) | 5 discovery calls in slack.channels, slack.users, slack.files | 0 | Slack completely removed |
| Reads (Drive/Docs replacement) | 0 | GDrive `list_files` on Victor's owned folder + second GDocs read pass | +1 GDrive service to breadth table |
| Density midpoint | 54 | 56 | +2 net (deeper Trello + GitHub, plus new GDrive read leg) |
| Distinct services | 7 (github, trello, linear, slack, contacts, gdocs, gsheets) | 7 (github, trello, linear, contacts, gdocs, gdrive, gsheets) | Slack dropped, GDrive added |
| Levers preserved | 5 | 5 | All 5 retained; L6 marginally weakened (3-way vs 4-way triangulation) |

**Note on Slack lever family (L3 missing reply, L4 search-result-cap eviction, L5 thread-reply blindness):** all three were `partial` in the original plan due to `slack.messages` not being in the per-task split. They are now **ACL-BLOCKED** for Victor regardless of split availability. They cannot be resurrected without a persona swap.

**Note on gmail:** Victor's own mailbox has 4,370 messages / 4,286 threads (per `gmail.users`). Own-mailbox reads are always ACL-visible, but `gmail.messages` is not in the per-task split, and HG gmail has no send / reply / compose / draft tool. Gmail deliberately not chosen as a lever anchor — the read-only nature and split-absence together make it a weak carrier for the selected levers.

## Stump Hypothesis (4 predictions)

1. **[HIGH]** Agent reports `harmonygames-Games/Combo-Fighters#1` as active in-progress art-import work despite `changed_files=0`, `additions=0`, label `["do not merge"]`, unmerged since 2025-12-02 and de facto superseded by merged PR #36 "vfx updates" (2026-02-11) and PR #16 "Marcus/win screen coin vfx" (2025-12-21). Mechanism: L1 + L10. Reasoning: L13 (first-framing anchor) plus L25 (existing-artifact latching) — the PR title reads like the canonical import so the agent stops after finding it.

2. **[HIGH]** Agent misses substantive engineering pushback in PR #37 `review_comments` (Oliver Brooks: `Please start enums with E`, the `ComboRarityDefinition` justification exchange, locked-vs-special prefab naming question). Agent reads the PR body plus the top-level CodeRabbit auto-summary and treats the PR as clean. Mechanism: L2 structured-DB skip on GitHub review_comments. Reasoning: L2 + L10 — agents almost never descend to `github_list_review_comments` when the PR body already returns a summary.

3. **[MED-HIGH]** Agent will not surface the still-incomplete Trello check_item `Marcus to create VFX` on ZM ROADMAP card `6851a9942b47001e59c8e777` (Equipped Card Item Infusion VFX implementation), nor the incomplete `Provide engineering estimate` items on cards `6852f6014ef0266338b1728b` and `6851aafe8c9e95ec0abbd262` and siblings. Agent will list card names and treat state as "in progress" without descending to checklist items. Mechanism: L2 structured-DB skip on `trello.check_items`. Reasoning: L2 — 9 of 79 cards carry checklists and the item shape is a niche tool call (`trello_get_check_items`) agents rarely invoke.

4. **[MED]** Agent conflates the four Marcuses (Marcus Bennett `usr_c77c50cc15c5342d`, Marcus Lee `usr_b501f018a4c5319f`, marcus `usr_d7ae9de750a5640a`, GitHub `PERSON_0396_GITHUB_USERNAME` with no linked email) when attributing merged VFX ownership. Most likely path: agent assumes GitHub "Marcus" is Marcus Bennett the Artist persona without triangulating through `contacts.contacts` and `linear.users`. Mechanism: L6 near-miss entity confusion, amplified by L1 latching. Reasoning: L4 alone does not stump, but stacked with L1 the misattribution will corrupt the owner-of-merged-work rubric. Note: Slack identity mapping leg dropped after ACL revision — 3-way triangulation still uniquely resolves the ambiguity but requires slightly more Contacts descent than the original 4-way.

## Hardness Score

**5/5 — PASS.**

- Levers gate: 5 selected (L1, L2, L6, L9, L10) — clears the 3-lever minimum. L3/L4/L5/L11 reclassified as ACL-blocked (Slack lever family unavailable to Victor); L11 held as Drive-fallback only if S1 finds the projected density thin.
- Density gate: projected midpoint 56 tool calls across 7 distinct services — clears HG authoring target (40+ calls AND 3+ services) with 40% margin on calls and 133% margin on breadth. Applying rule L33 (design for margin, not for a number). Net +2 over the pre-ACL projection despite Slack drop, because the Trello / GitHub / GDrive depth compensates for the removed Slack calls.

No `INSUFFICIENT_LEVERS` or `INSUFFICIENT_DENSITY` flag.

## Hardness Brief for the Prompt Writer

Victor Barnes needs a status brief before Monday on the art-vendor and VFX-import position across the Combo-Fighters codebase and the Zombie Match 3D roadmap: what merged, what is still open, and who owns each piece. Anchor the framing on Leonard Hayes's or Robert's Friday-evening remark that "Marcus told me the import PR is already covered by the merged VFX branch, treat that draft as parked" — Victor believes it but is being asked to confirm. The real answer requires the agent to (1) not treat draft PR #1 as the canonical import work despite its title and reviewer, (2) descend to `github_list_review_comments` on merged Combo-Fighters PRs to catch the still-open Oliver Brooks pushbacks, (3) descend to `trello_get_check_items` on ZM ROADMAP VFX cards to catch the incomplete `Marcus to create VFX` items that were never re-toggled after the merged VFX shipped, and (4) attribute owner correctly across the four Marcuses using Contacts + Linear + GitHub triangulation. Ask for concrete writes: a Linear comment on the ART or ZOM tracking issue, a Trello check_item state update where appropriate, a Trello card comment on the affected card, a GDoc status brief for Leonard/Robert, and a GSheet vendor-tracker snapshot. Projected midpoint 56 tool calls across 7 services. **Do NOT anchor any lever on Slack — Victor is not a member of any channel of any kind, so all Slack reads are ACL-blocked and Slack writes have no plausible destination.** Do NOT hint that the dismissal is wrong (L15); do NOT put the correct answer in any body (L6-hard); do NOT reference Snowflake / Confluence / Airtable / QuickBooks / Firebase / BigQuery / a wiki / a knowledge base / an analytics warehouse (V5 retired); do NOT design any lever requiring gmail write (HG gmail is read-only, no draft); do NOT require a Slack post as a rubric-scored write.
