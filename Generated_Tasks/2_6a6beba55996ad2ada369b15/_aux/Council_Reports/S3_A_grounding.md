# S3 Council A (Grounding) - Task 2_6a6beba55996ad2ada369b15

Universe: harmonygames. Persona: Robert (robert@harmonygames.co, EMPLOYEE_0016_SLACK_ID).
Scope: every concrete value in `7_Rubrics.json` (25 criteria) re-derived from `_aux/Universe_Split/`.
Nothing below rests on `6_Oracle_Events.txt`, `_aux/Verification_s2.md`, or any prior council report.

## Method / reproducibility

Snowflake tables file `snowflake.snowflake.tables.json` (159 MB) is an array of
`{"source","row_data":"<table-object-as-JSON-string>"}` wrappers. It was streamed with the
provided `_aux/stream_sf.py` (raw_decode + buffer trim), which `json.loads` each wrapper's
`row_data` into one table dict at a time and discards it. Only running scalars were kept.

Memory: the stream_sf-based derivation was measured at **235708 kbytes (230.2 MiB)** peak RSS by
external `/usr/bin/time -v`, corroborated by in-process `getrusage` at 230.18 MiB the same run.
This is under the rule 33 ceiling of 384 MiB. (Interim scripts printed a stale
`ru_maxrss` of 6329.62109375 MiB that was byte-identical across a do-nothing probe and real work,
i.e. an artifact, not a measurement; the external timer settles it.)

Command shape (per target table):
`for src, rd in stream_rows(PATH): if rd.get("name")==T: for r in rd["rows"]: <accumulate scalars>`

Slack shards `slack.2026-01.json` / `slack.2026-02.json` are arrays of
`{"source","row_data":"<message-as-JSON-string>"}`; parsed the same way, filtering by channel id.

## Snowflake derivations (raw results)

- DAILY_ACTIVE_USERS game_id=combo_fighter: 72 rows; date min 2026-01-05, max 2026-02-09;
  peak per-day DAU (sum across platform) = 801 on 2026-02-07 (peak single-row = 426);
  new_users sum = 845; total_sessions sum = 55101; d1_retention_pct simple arithmetic mean over
  the 72 rows = 44.0 (new_user-weighted mean would be 43.78, NOT used).
- REVENUE_DAILY game_id=combo_fighter (UNVERSIONED table): 72 rows; iap=0.0, ad=0.0, total=0.0.
  REVENUE_DAILY_V2 combo_fighter rows (title_id) = 0. Confirmed zero-revenue is on the live table
  and the V2 table carries no combo_fighter rows.
- AD_SPEND_DAILY spend_usd:
  - combo_fighter lifetime = 7483.42 (330 rows).
  - ALL game_ids, date strictly AFTER 2026-02-09 = 8452.64 (280 rows).
  - Competing readings (distinct): INCLUDING 2026-02-09 = 8922.12; combo_fighter-only strictly
    after = 2444.08. Post-decision spend by game: domino_delights 5569.66, combo_fighter 2444.08,
    zombie_match_3d 438.90 (sum 8452.64).
- CASH_BALANCE month_end_date=2026-02-28: cash_usd=2500, monthly_net_burn=22500, runway 0.1,
  headcount 6, notes "Company wind-down initiated".

## Slack derivations (verbatim, with ts)

- Net-proceeds source, #winddown C0ADGSZKR3R, ts 1770911000.728559, user Leonard (EMPLOYEE_0038):
  "Ok.  We got a a cash offer of $22500 for our data. They charge us $11700. We can pay up SVB debt
  and then cancel the card. We still need to settle with Unity and Singular. I'm more hopeful now
  that this can be done without cash out of pocket."
  => net = 22500 - 11700 = 10800.
- Managed wind-down cost, C07C2866011, ts 1770850852.708789, user Leonard:
  "the cost of Sunset is about ~$15K - the data will likely cover our costs without us liquifying
  the laptops/assets".
- Ad-account/campaign control (Leonard is the campaign operator), all C07C2866011 / C09UHHN6PFZ:
  ts 1770404487.065799 "I created the VO campaign"; ts 1767475598.015409 "Shutting down the
  campaign today btw to keep our cpi low"; ts 1768166121.923249 "Can I pause the campaigns";
  ts 1770844112.235939 "I set up the campaign except the playable". Arthur only advises Singular/meta
  configuration (ts 1768500781.313729); Robert only voices concern (ts 1769107371.348799 "I am
  worried about marketing... turning campaigns on/off can't be good") without operating them.

## Literal checks

- Token "10800"/"10,800" as a DOLLAR figure does NOT appear anywhere in the universe; the only
  substring hits are inside unix timestamps (e.g. 1768510800 in a date-formatted Slack blob).
  10,800 is a genuine derivation (22500 - 11700), correctly not stated as a universe literal.
- 22,500 collision honored: it is both CASH_BALANCE.monthly_net_burn and the gross data offer.
  The rubric grades the derived net 10,800, never 22,500. No conflation in the rubric.

## Persona reachability (Robert authorship, text-bearing message counts)

- #winddown C0ADGSZKR3R: Robert authored 19 messages -> reachable. (Leonard 150, Arthur 22.)
  members[] shows opaque U04* ids, but authorship confirms Robert is in-channel.
- Founder channel C07C2866011 (carries the ~15K cost message): Robert authored 691 -> reachable.
No Slack-sourced value lives outside Robert's scope. No reachability BLOCK.

## Identity checks

- Leonard Hayes = EMPLOYEE_0038_SLACK_ID (slack.users / user_profile "leonard hayes"), founder.
- Arthur Blake = EMPLOYEE_0025_SLACK_ID, founder (author of Unity termination note signed "Arthur Blake").
- Robert = EMPLOYEE_0016_SLACK_ID, gmail robert@harmonygames.co (19192 msgs). Assigned persona.
- #winddown channel: id C0ADGSZKR3R, name "winddown", is_private=true, num_members=3. Exists.

## Per-value verification table

| # | value | claims | source + locator | found | verdict |
|---|---|---|---|---|---|
| 1 | (standalone written page) | write action, no universe atom | trajectory | n/a | GROUNDED (no value) |
| 2 | 2026-01-05 to 2026-02-09 | measured life window | DAILY_ACTIVE_USERS WHERE game_id=combo_fighter, min/max(date) | 2026-01-05 / 2026-02-09 | MATCH |
| 3 | 0.00 | lifetime revenue | REVENUE_DAILY combo_fighter sum(iap+ad+total)=0; V2 combo rows=0 | 0.0 | MATCH |
| 4 | 7,483.42 | lifetime acquisition spend | AD_SPEND_DAILY combo_fighter sum(spend_usd) | 7483.42 | MATCH |
| 5 | 801 peak DAU | peak daily active users | DAILY_ACTIVE_USERS combo, max of per-day platform-sum | 801 (2026-02-07) | MATCH |
| 5 | 845 lifetime new users | sum new_users | DAILY_ACTIVE_USERS combo sum(new_users) | 845 | MATCH |
| 5 | 55,101 lifetime sessions | sum total_sessions | DAILY_ACTIVE_USERS combo sum(total_sessions) | 55101 | MATCH |
| 5 | 44.0 % avg D1 retention | mean d1_retention_pct | DAILY_ACTIVE_USERS combo simple mean over 72 rows | 44.0 | MATCH |
| 6 | 8,452.64 | spend after 2026-02-09 (all titles) | AD_SPEND_DAILY all game_ids, date > 2026-02-09, sum(spend_usd) | 8452.64 | MATCH |
| 7 | Leonard Hayes controls ad accounts | owner of continuing spend / sole campaign operator | slack ts 1770404487, 1767475598, 1768166121, 1770844112 | Leonard starts/stops/pauses; Arthur/Robert do not | MATCH |
| 8 | 10,800 | net proceeds of data agreement | derived 22500 - 11700, slack C0ADGSZKR3R ts 1770911000.728559 | 10800 | MATCH (derivation) |
| 9 | 2,500 | cash on hand | CASH_BALANCE month_end_date=2026-02-28, cash_usd | 2500 | MATCH |
| 10 | approximately 15,000 | managed wind-down cost | slack C07C2866011 ts 1770850852.708789 "~$15K" (Sunset) | ~15000 | MATCH |
| 11 | 15,000 > net proceeds | cost exceeds net | 15000 > 10800 | true | MATCH |
| 12 | funds fall short (conclusion) | 10800+2500=13300 < ~15000 + vendor obligations | derived from grounded components | shortfall | MATCH (direction) |
| 13 | posts in #winddown | write action; channel exists | slack.channels C0ADGSZKR3R private | exists | GROUNDED |
| 14 | Leonard Hayes + Arthur Blake | both founders addressed | slack.users EMPLOYEE_0038 / EMPLOYEE_0025 | both confirmed | MATCH |
| 15 | (link/title to account) | write action | trajectory | n/a | GROUNDED (no value) |
| 16 | coverage conclusion in msg | same shortfall as #12 | grounded components | shortfall | MATCH (direction) |
| 17 | 8,452.64 in msg | continuing spend figure | AD_SPEND_DAILY all > 2026-02-09 | 8452.64 | MATCH |
| 18 | files tracking item | write action | trajectory | n/a | GROUNDED (no value) |
| 19 | paid acquisition spend as subject | continuing cost identity | AD_SPEND_DAILY post-decision spend is UA | grounded | MATCH |
| 20 | 8,452.64 on tracking item | continuing spend figure | AD_SPEND_DAILY all > 2026-02-09 | 8452.64 | MATCH |
| 21 | Leonard Hayes owner on item | owner of continuing spend | same as #7 | Leonard | MATCH |
| 22 | two or three lead figures | count in final response | trajectory | n/a | GROUNDED (no value) |
| 23 | accepted set {0.00; 7,483.42; 8,452.64; 10,800; 2,500; ~15,000} | each a grounded headline figure | rows 3,4,6,8,9,10 above | all six re-derived | MATCH (each member) |
| 24 | funds fall short (final response) | same shortfall as #12 | grounded components | shortfall | MATCH (direction) |
| 25 | account written before post | ordering | trajectory | n/a | GROUNDED (no value) |

## Result

Every concrete value in all 25 criteria was re-derived from `_aux/Universe_Split/` and matches.
Derived values (10,800 net proceeds; the shortfall conclusion) rest only on grounded components and
verbatim Slack sources. Every Slack-sourced value sits in a channel Robert authors in. No mismatch,
no ungrounded value, no out-of-scope reachability.

VERDICT: GO
