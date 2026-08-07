# Hardness Plan — `2_6a6beba55996ad2ada369b15`

Universe **harmonygames** (framework `hg`, single-model) · Model under test **Claude Opus 4.7** · Universe today **2026-02-28** (America/Chicago, a **Saturday**, month-end, **mid-Q1**) · Injection posture: **none authored** (`4_Changelog.json` = `[]`, `9_Universe_inject.sql` = comment-only template)

## Persona and Business Function

- **Robert** — Co-Founder & Creative Director. `robert@harmonygames.co`, `persona_key: robert`, department **Executive** in `4_Persona_ACL_Roster.json`.
- Slack identity resolves across three schemes: `EMPLOYEE_0016_SLACK_ID` (message `user` / mention fields) = `U04TWDMDT0V` (channel `members[]` arrays) = `usr_robert`.
- **Business function: Executive.** This is the fixed scope anchor.

## Storyline decision

**Spine = the company wind-down.** Rejected as spine: Combo Fighter live tuning.

The wind-down is squarely Executive work (co-founder acting on board-level disposition of vendors, cash and IP) and Robert posts in `#winddown` from its creation. Combo Fighter **live tuning** is Product/Design work and, more decisively, it is **temporally superseded**: the shutdown decision lands 2026-02-09 and by 02-11 the team is cancelling subscriptions and sending termination letters, so a 02-28 prompt asking Robert to advance Combo Fighter monetization or ship an A/B test would be incoherent against its own universe.

### Open question for the operator — a prior S1 used a different spine

`Tasks/_meta/Hardness_Patterns_Log.md` carries an entry dated **2026-08-06** headed "Task 2 HG (**Combo Fighter post-mortem**, S1)", describing a Hardness Brief and a drafted prompt for this task index. No `5_Prompt.txt` and no prior `Hardness_Plan.md` survive in the task directory, and `Generated_Tasks/` is untracked by git, so nothing is recoverable.

This plan's rejection of Combo Fighter is a rejection of **live tuning / monetization**, and it does **not** extend to a post-mortem. A Combo Fighter post-mortem is in fact coherent and well-grounded: Leonard's 02-09 wind-down message opens "After reviewing the latest Combo Fighter data (see the attached screenshot from today below) and considering the iterations we've already run, we've decided to shut the company down" — the game's performance **is** the stated cause of the shutdown, and a post-mortem authored by the Creative Director is natural Executive work.

The two spines are therefore compatible rather than exclusive, and the levers in this plan are largely spine-portable: L2 (Snowflake `FINANCE.EXPENSES`, and equally the `GAME_EVENTS` tables that carry Combo Fighter from Jan 2026), L10 supersession, L7 multi-write and L8 chaining all survive a post-mortem framing. Only **L11 net-vs-gross is wind-down-specific**, because the $22,500 / $11,700 pair lives in the data-sale thread.

**Operator decision required before S1.** Options: (a) proceed on the wind-down spine as planned here; (b) re-target to the Combo Fighter post-mortem to match the prior S1, in which case L11 must be replaced with a `GAME_EVENTS`-derived figure and the density projection re-run; (c) a combined framing in which the post-mortem is the ask and the wind-down is the context. This plan is written for (a).

## Levers Available

| # | Lever | Status | Evidence (verified against `_aux/Universe_Split/`) | Cost |
|---|---|---|---|---|
| 1 | Latching / first-framing | **yes** | `slack.2026-02` ts `1770911000.728559` (#winddown C0ADGSZKR3R, Leonard): "We got a a cash offer of **$22500** for our data. They charge us **$11700**." Belief anchor at ts `1770859981.856189`: "I'm hoping the data will cover our cost of shutting down orderly at least" | 5-8 |
| 2 | Structured-source skip (HG analogue) | **yes** | `snowflake.snowflake.tables` : `FINANCE.EXPENSES.CASH_BALANCE`, `FINANCE.EXPENSES.MONTHLY_BURN`, `FINANCE.EXPENSES.HEADCOUNT`. Rows are embedded in the table record | 4-7 |
| 3 | Missing reply | partial | vendor outcomes land as later confirmations, e.g. ts `1770789534.434749` (Helpshift "gonna cancel without a big hassle"), ts `1770839322.836779` (Robert: "Soundly canceled") | 3-5 |
| 4 | Search-result-cap eviction | partial | #winddown carries 212 Feb messages in one shard; the load-bearing offer line sits mid-thread, not at top | 3-5 |
| 5 | Thread-reply blindness | partial | present but weak — the decisive lines here are top-level posts, not thread replies | 2-4 |
| 6 | Near-miss entity / near-miss figure | **yes** | see the two numeric collisions in the Risk register below. Also first-name collisions in `Fact_Ledger.json`: **marcus** -> 2, **claire** -> 2, **thomas** -> 2, **brian** -> 2, **victor** -> 2 | 3-5 |
| 7 | Multi-write diversification | **yes** | write surfaces confirmed in the catalog: `slack_send_message` / `slack_conversations_add_message`, `confluence_create_page` / `confluence_add_comment`, `gsheets_create_spreadsheet` / `gsheets_values_append`, `linear_create_issue` / `linear_create_comment`, `gdocs_create_document`, `trello_create_card`, `gdrive_create_file`, `contacts_add_new_contact` | 9-12 |
| 8 | Multi-link chain | **yes (revised up)** | gross offer (Slack) -> net after their charge (derived) -> cash on hand (Snowflake `CASH_BALANCE` 2026-02-28) -> obligations (Helpshift, Unity, Singular, SVB). See "Correction to the sub-agent's read" | 6-9 |
| 9 | Universe-grounded gotcha | partial | Gmail read-only, weekend/month-end/mid-Q1 coherence. These constrain authoring more than they stump the model | 3-5 |
| 10 | Reversal / supersession | **yes** | deal structure flips sale -> licence at ts `1770924424.711879` ("instead of just selling the data we'll do data licensing agreeement so that we can ... own the entire IP"), with ts `1770924465.624129` confirming "the quote is gonna go slightly higher but cash offer is gonna stay the same". Vendor state flips: ts `1770839688.408909` ("I'll keep Intuit for now") superseded by ts `1770933601.686309` ("keep Deel, gusto, Intuit ... linear we keep during transition") | 4-6 |
| 11 | Net-vs-gross framing | **yes** | $22,500 gross vs $11,700 charge. **$10,800 net appears nowhere in the universe** (verified: a regex sweep of the whole Feb shard for `10[,.]?800` returns zero hits) — L6-clean | 4-7 |

## Selected Levers (5)

| Lever | Rationale | Cost mid | Learnings cite | What the prompt MUST withhold (L36) |
|---|---|---|---|---|
| **L11 net-vs-gross** | The derived figure is the highest-discrimination rubric target and is verifiably absent from the universe | 5.5 | L11, L18, L16 | The net figure; any hint that $22,500 is gross or incomplete. Robert asks for execution, not audit |
| **L2 structured-source skip (Snowflake FINANCE)** | The symmetric stump. Agents read Snowflake as game analytics and never enumerate `FINANCE.EXPENSES` | 5.5 | L2, L10, L11 (Learnings) | The words Snowflake, cash balance, runway, burn; any pointer that a finance schema exists |
| **L8 multi-link chain** (promoted from the scan's `partial`) | Converts a single subtraction into a three-service chain — see the correction below | 7.5 | L8, L2 (Learnings), L19 | That cash on hand must be added; that obligations must be netted |
| **L10 supersession (sale -> licence, and vendor state)** | Two independent supersession hops on the same spine | 5 | L10, L13, L12 | That the deal structure changed; the final vendor keep/cancel list |
| **L7 multi-write (4 writes across 4 services)** | Density and breadth driver; internal-only because Gmail cannot send | 10.5 | L5, L33 Rule 4 | Tool names, channel names, artifact types. State goals only |

**Symmetric structured-source stump: present** (L2 on Snowflake `FINANCE.EXPENSES`). The set does not rest on L4 or L5 alone. **L31 is deliberately not used**: it is a cross-model differentiator and HarmonyGames is single-model, so there is no second model to carry the asymmetry.

### Correction to the sub-agent's read (load-bearing)

The scan proposed L11 as the primary stump at [HIGH] confidence on the strength of a single subtraction, $22,500 − $11,700 = $10,800. **Learnings L2 rates a single-hop reduction at roughly 80% pass**, so as specified that lever would likely have produced a task the model beats. The fix is already in the universe and costs no injection: the executive question is not "what is the net" but "does this actually cover an orderly shutdown", which forces a chain across three services:

1. **Slack** — gross offer $22,500 and their $11,700 charge (ts `1770911000.728559`).
2. **Derived** — net proceeds $10,800.
3. **Snowflake** — `FINANCE.EXPENSES.CASH_BALANCE` row `month_end_date = 2026-02-28`: `cash_usd = 2500`, `runway_months = 0.1`, notes "Company wind-down initiated". The agent must add cash on hand, not treat proceeds as the whole picture.
4. **Slack again** — obligations still open at ts `1770911000.728559` ("We still need to settle with Unity and Singular"), Helpshift's outstanding balance ("$150*10 = $1500", 02-09), and SVB (ts `1770860000.975869` "we need to pay up SVB for sure"; ts `1770927223.969899` "as soon as the money hits the account we pay SVB fully and close the credit card").

This is L8 proper, and it is why L8 is promoted to a selected lever and the density projection rises.

## Tool-Call Density Projection

| Component | Range | Midpoint |
|---|---|---|
| Base discovery (identity, channel resolution, winddown page-in, horizon) | 5-8 | 6.5 |
| L11 net-vs-gross | 4-7 | 5.5 |
| L2 Snowflake FINANCE skip | 4-7 | 5.5 |
| L8 multi-link chain (cash + obligations reconciliation) | 6-9 | 7.5 |
| L10 supersession (deal structure + vendor state) | 4-6 | 5.0 |
| Write actions (4 writes across 4 services, ~3 supporting reads each) | 9-12 | 10.5 |
| Cross-service triangulation buffer | 5-8 | 6.5 |
| **TOTAL projected** | **37-57** | **47.0** |

**Gate (HarmonyGames scheme — NOT the V3-family 50/40 bands):** midpoint >= 40 = PASS · 15-39 = THIN_DENSITY · < 15 = INSUFFICIENT_DENSITY.

**Verdict: 47.0 -> PASS** against the 40+ authoring design target.

**Necessary-call subtotal (the prompt-eval hard gate scores necessary calls only, not total):** base ~4 + L11 ~4 + L2 ~4 + L8 ~5 + L10 ~3 + writes ~8 = **~28 necessary calls** across >= 2 services, with multiple meaningful writes and real information friction. Gate is >15 -> **PASS**. Trajectory QC floor (>= 15 average) -> **PASS** with margin.

Per L33 Rule 1, margin is the point: the projection clears the 40 target by 7 and the 15 floor by 13, so grader non-determinism cannot move the gate. `set_acting_user`, ACL-denied reads and retries against inaccessible records are excluded from every count above.

## Service Breadth (v11 G1)

| Service | Calls | % of total (mid 47) |
|---|---|---|
| slack | 12-16 | ~30% |
| snowflake | 4-7 | ~12% |
| confluence | 3-5 | ~9% |
| gdocs | 3-5 | ~9% |
| gsheets | 3-4 | ~8% |
| linear | 2-3 | ~5% |
| gdrive | 1-3 | ~5% |
| contacts | 1-2 | ~4% |
| github / trello | 0-2 | ~2% |
| gcal / gslides | 0 | 0% (no data — see below) |
| **Distinct services** | **8** | — |

**Breadth gate: PASS.** Seven services sit at or above 5% and the dominant service (slack) is ~30%, well under the 60% ceiling. S1 must preserve this by forcing the Snowflake read and at least two non-Slack writes; if the prompt collapses to a Slack-only investigation the breadth degrades to THIN_BREADTH even though density holds.

**`gcal` and `gslides` carry zero records.** `Services_Data/gcal/gcal.events.json`, `gcal.calendars.json` and `gslides/gslides.slides_presentations.json` are each 3 bytes (`[]`). The write tools (`gcal_create_event`, `gslides_create_presentation`) do exist, so a write is technically feasible, but no discovery lever can rest on either. **Consequence for hard rule 13:** the every-service Calendar sweep is **vacuously satisfied** — with zero calendar events universe-wide, no future confirmed event can contradict a completeness claim. This is a cleared check, not a skipped one, which matters because deviation HG-U11 leaves the `v4_gates.py` F9 gate unavailable for HarmonyGames.

## Stump Hypothesis

1. **[HIGH] Net-vs-gross on the data deal.** The agent reports the wind-down as funded by **$22,500** rather than the **$10,800** net after the counterparty's $11,700 charge. Mechanism: first-framing latch on the only figure the persona states (ts `1770911000.728559`), reinforced because the persona's own belief line ("I'm hoping the data will cover our cost of shutting down orderly", ts `1770859981.856189`) presents the gross as sufficient. Cites L11 / L13 / L18. Confidence rests on the chain, not the subtraction alone — see stump 2.
2. **[HIGH] Snowflake FINANCE never queried.** The agent reasons about coverage entirely from Slack and never enumerates `FINANCE.EXPENSES.CASH_BALANCE`, so it misses that cash on hand at 2026-02-28 is **$2,500** with 0.1 months runway. Mechanism: structured-source invisibility — Snowflake reads as a game-analytics warehouse and nothing in the conversation points at a finance schema. Cites Learnings L2 / L10 / L11. This is the symmetric stump and the reason the task should not collapse to an arithmetic exercise.
3. **[MED] Deal-structure supersession missed.** The agent describes an outright data **sale** and misses the restructure into an IP-retaining **licensing agreement** (ts `1770924424.711879`), and/or misreports the cash consideration as having risen because the quote did (ts `1770924465.624129` is explicit that the quote rises but "cash offer is gonna stay the same"). Mechanism: supersession plus a same-minute pair of messages that pull in opposite directions. Cites L10 / L13.
4. **[MED] Vendor disposition reported at an intermediate state.** The agent reports "keeping Intuit" alone (ts `1770839688.408909`) or an otherwise stale keep/cancel mix, missing the consolidated final state at ts `1770933601.686309` ("keep Deel, gusto, Intuit ... linear we keep during transition"). Mechanism: supersession across a 2-hour window inside a high-traffic channel. Cites L12 / L10.

## Hardness Score

**5/5 — PASS.** Five independent levers, density midpoint 47.0 (PASS band), ~28 necessary calls against a >15 gate, 8 distinct services with the dominant at ~30%, zero injection required.

## Risk register (carry into S1 and S2)

These are the items S1/S2 must resolve. Two are numeric collisions the sub-agent did not surface.

1. **`$22,500` collides with Snowflake's February net burn.** `CASH_BALANCE` for `2026-02-28` records `monthly_net_burn = 22500` — numerically identical to the data offer. An agent that queries Snowflake (which the task *wants*) meets `22500` in a second, unrelated role. This is usable as an L6 near-miss, but a rubric that grades "$22,500" as a token rather than as the gross offer will mis-grade. **S3 must bind the figure to its role, not just its value.**
2. **`MONTHLY_BURN` and `CASH_BALANCE` disagree for February 2026.** The `MONTHLY_BURN` category rows for `2026-02-01` sum to **$20,000** (salaries 4,000 + contractor 500 + aws 500 + legal 13,000 + tools 500 + other 1,500), while `CASH_BALANCE` records `monthly_net_burn = 22500` for the same month — a $2,500 gap. Do **not** make a burn-reconciliation load-bearing until this is explained; an unexplained cross-table contradiction is exactly what the binary QC sub-dim *Universe / Cross-service Coherence* penalises when it causes an agent failure.
3. **A `$12K` variant of the `$11,700` charge exists but Robert cannot read it.** ts `1770927719.631589` says "they cover all the third party fiduciary stuff for $12K", in DM `D04UC0UEN2V` — a conversation Robert is **not** party to (his DMs are D07H86MV4DN, D04UP2L3E3S, D077ALC9VK3, D05GU6L0XFH, D05SJRKTUMS, D05UDNCCFEW, D05PJG45YA2, D04V95AAAHW, D04UP2KUFCY). Under persona-scoped Slack reads this is invisible to the agent, so it cannot poison the derivation — but S2 must not cite it as reachable evidence, and S3 must not accept `$10,500` as an alternate net.
4. **The `$11,700` charge is never revised.** Verified by regex sweep of the full February shard: five hits on `11700|22500|SVB|10800`, none revising it. `$10,800` is therefore safe to pin as the single correct net. **Zero universe hits on `10,800`** confirms L6 cleanliness.
5. **SVB debt has no stated figure.** Referenced three times (ts `1770860000.975869`, `1770911000.728559`, `1770927223.969899`) but never quantified. A rubric demanding a full obligation reconciliation would be ungradeable. **S2 must anchor the chain on net proceeds plus cash on hand versus the *named* open obligations, not on a closed arithmetic of total liabilities.**
6. **Fifteen-day staleness gap.** The universe's last Slack message is **2026-02-13 19:58 UTC**; universe today is **2026-02-28**. (`today_horizon.json` reports a last-event timestamp of 2026-02-22 from a non-Slack service.) A prompt dated 02-28 must read as "where did we land on this", never as "this just came in".
7. **Date coherence.** 2026-02-28 is a **Saturday**, month-end, and mid-Q1. The wind-down channel is demonstrably active across weekends, so internal founder coordination on a Saturday is in character and does not trip the weekend-comms rule. S1 must still avoid a weekday deadline, avoid implying any external vendor communication dated Saturday, and never use "Q1 close" or "Q1 final" framing.
8. **Single-target uniqueness (hard rule 13).** The data buyer and the accounting firm are referred to by redacted or inconsistent tokens across messages. **Grade on the figure and the disposition, never on the buyer or firm entity**, unless S1 names one unambiguously.
9. **Gmail cannot send.** Verified at the catalog level: all 27 `gmail_*` tools enumerated, zero match `send|compose|draft|reply|forward`. The wind-down's most natural artifacts (termination letters, vendor and investor emails) are therefore **not writable**. Every deliverable must be phrased as internal coordination. A prompt that says "email the vendor" is a `[Fail - Prompt Feasibility with Tools]` defect, not a hard task.

## Feasibility confirmations

- **Persona ACL, evidenced by authorship rather than by `members[]`.** `Tasks/_meta/Hardness_Patterns_Log.md` (2026-08-06) records that HarmonyGames Slack `members[]` arrays are unusable as membership evidence — the export tokenised 100 of 218 users and never re-tokenised those arrays, so `#executives` reports `num_members: 3` while carrying tens of thousands of messages from tokenised employees. Membership is therefore established by **authorship**, which proves it because a non-member cannot post: Robert authored **21 messages in `#winddown`, 132 in `#executives`, 136 in `#prototype`** in the February shard (and 583 / 720 in `#executives` / `#prototype` in January). Every channel this task reads is confirmed by that method. **Snowflake, Confluence, Linear, Trello, GitHub and Contacts are ACL-unscoped**, so the structured-source lever carries zero read-feasibility risk. All **26 GSheets are owned by `robert@harmonygames.co`**, so the Drive-derived ACL that governs GSheets/GDocs/GSlides is satisfied for the sheets surface.
- **Lever-carrier buildability (banked check).** A prior HG pass lost its top-ranked lever because the brief forbade naming the workbook that the planned `gsheets_values_update` write targeted, leaving no phrasing that bought the write without either killing the lever or breaking single-target uniqueness. Checked here and clear: the four planned writes are all **creations** (a Slack post, a new Confluence page, a **new** GSheet tracker, a new Linear issue), none requires naming a pre-existing artifact, and the withheld terms (Snowflake, cash balance, runway, burn) constrain a **read** path rather than a write carrier. No conflict between the withhold list and the write set.
- **Weekend-comms constraint propagates to S3, not just to injection.** The rule reads as an injection gate but is also enforced by `validate.py --phase submission_gate` against **rubric text** (anchor `v22 HG-7` fixtures a Slack post dated 2026-02-28 and requires it to flag; `HG-8` pins 2026-02-27 as the weekday control). Since this task injects nothing, the live constraint lands at S3: **no criterion may date a communications write to 2026-02-28.** Carry this into S2 and S3.
- **No lever requires** a Gmail send or draft, a calendar event, or a slides deck.
- **Zero injection required.** Every selected lever is grounded in data already present. Keep `4_Changelog.json` as `[]` and leave `9_Universe_inject.sql` comment-only.

## Hardness Brief for the Prompt Writer

Write an **Executive** task for **Robert**, dated **2026-02-28** (Saturday, month-end, mid-Q1), framed as internal founder coordination during the company wind-down — never as sending external mail, because Gmail in this universe cannot send, reply, compose or draft. The spine is whether the data deal actually funds an orderly shutdown. Robert believes it does: the only figure anyone has stated is the **$22,500 cash offer** (`slack.2026-02` ts `1770911000.728559`, #winddown), and the persona's own words are "I'm hoping the data will cover our cost of shutting down orderly at least" (ts `1770859981.856189`). The agent must derive the **$10,800 net** after the counterparty's $11,700 charge, then set that against the **actual cash position in Snowflake `FINANCE.EXPENSES.CASH_BALANCE` for month-end 2026-02-28 ($2,500, 0.1 months runway)** and the obligations still named as open (Unity, Singular, Helpshift's outstanding balance, SVB). It must also register that the deal was restructured from an outright **sale into an IP-retaining licensing agreement** (ts `1770924424.711879`, with ts `1770924465.624129` confirming the cash consideration is unchanged even though the quote rises), and report the **final** vendor disposition (ts `1770933601.686309`) rather than the superseded "keep Intuit for now" (ts `1770839688.408909`). Force **four internal writes across four services** — a Slack summary into #winddown or #executives, a Confluence wind-down status page, a GSheet disposition tracker, and a Linear tracking issue — targeting ~47 tool calls across 8 services with slack held under 60%. **Withhold**: the net figure; any suggestion that $22,500 is gross or insufficient; the words Snowflake, cash balance, runway and burn; the sale-to-licence change; and the final vendor keep/cancel list. Grade on figures and dispositions, never on the buyer or accounting-firm entity, and treat the 15-day gap between the last message (02-13) and today (02-28) by asking where things landed rather than implying fresh news.
