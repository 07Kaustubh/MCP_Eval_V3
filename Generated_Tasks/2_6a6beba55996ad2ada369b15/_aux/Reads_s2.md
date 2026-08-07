# Reads — S2 (`2_6a6beba55996ad2ada369b15`, universe harmonygames)

Running log of every spec doc, reference card and data source opened in this phase, with what was confirmed from each. v11 E2 compliance gate.

## Runbooks and reference cards

- `Reference/Sessions/S2.md` :: phase contract, exit criteria, AUDIT auto-fire conditions. Note its "Required inputs" table names the HG tool catalog with prefix **6**, which is correct.
- `Reference/OE_Format.md` :: numbered prose, real tool names, real parameters, discovery before writes. HG deltas section confirms `slack_send_message` takes `text`, `slack_conversations_add_message` takes `payload`, `linear_create_issue` takes `team`, `gdocs_create_document` takes `bodyText`, and Gmail is read-only.
- `Reference/Council_Protocol.md` :: Council A 9 perspectives, Council B 8 perspectives, five role lenses. **B3's stated 50/40 bands are the V3-family scheme and do NOT apply to HarmonyGames**; the HG bands (>=40 PASS, 15-39 THIN, <15 INSUFFICIENT) were passed explicitly to Council B to prevent the same scheme drift S1 had to correct for.
- `AGENTS.md` :: hard rules 2, 3, 13, 23, 31, 32, 33 all bear on this phase. Rule 2's inverted payload boundary for HG is why the per-task `3_UniverseDataForThisTask.json` was never read as data.

## Spec docs

- `Docs_harmonygames/9_Common_Error.md` :: read BEFORE drafting, per the runbook. The "Oracle Event errors" section drove four concrete drafting decisions: (a) OEs are contributor-internal and sit at authority rank 6, so nothing in this OE list may bind the agent beyond what the prompt asks; (b) no OE may be a conclusion ("The Agent discovers X") rather than an observable lookup with an expected result; (c) no OE may be a prohibition; (d) every numeric claim must be checked for the precision the tool path actually exposes. Also drove the OE 6 wording, which states explicitly that an empty result is checked evidence rather than an unperformed lookup.
- `Docs_harmonygames/9_Common_Error.md`, Rubric section :: read forward for the S3 decompose directives. "Locking a goal to one method" is why OE 20 and OE 22 name an intended path and then name the equally valid alternates rather than pinning a single surface.
- `Evals_harmonygames/2_Oracle_Events_Eval.md` :: OE Completeness and OE Accuracy are both 3/4/5 NON-FAIL-only schemes, no FAIL band. Coverage is judged unordered; lifecycle preconditions are judged ordered.
- `Docs_harmonygames/7_QC_Spec_Doc1.json` :: the scored HG QC specification. The Oracle Event dimension is the one under review here; density thresholds re-read to keep the three distinct numbers separate (authoring target 40+ calls and 3+ services, prompt-eval gate >15 necessary calls, trajectory floor >=15 average).
- `Docs_harmonygames/14_Persona_ACL.md` :: seven scoped services, six unscoped. Confirms Snowflake, Confluence, Linear, Trello and Contacts are unscoped, so every structured read in this OE list carries zero ACL risk. Slack is scoped, so #winddown readability was established by authorship rather than by `members[]`.

## Per-task data (all figures below queried directly this phase, not inherited)

- `_aux/Universe_Split/snowflake.snowflake.tables.json` (159 MB) :: streamed with an incremental JSON decoder, never fully loaded, per hard rule 33. 33 table records across 3 databases.
  - `ANALYTICS.GAME_EVENTS.DAILY_ACTIVE_USERS` :: combo_fighter = 72 rows / 36 distinct dates / 2026-01-05 to 2026-02-09. Combined DAU 45 on day one, peak 801 on 2026-02-07. 845 new users, 55,101 sessions. D1 mean 44.00 (range 37.34 to 50.73), D7 mean 22.10, D30 mean 10.99.
  - `ANALYTICS.MONETIZATION.REVENUE_DAILY` :: combo_fighter = 72 rows over the same window, iap + ad + total all summing to **0.00**, paying_users 0, zero revenue-bearing days.
  - `ANALYTICS.MONETIZATION.IAP_TRANSACTIONS` :: combo_fighter = **0 rows**. Corroborates the zero independently.
  - `ANALYTICS.MARKETING.AD_SPEND_DAILY` :: combo_fighter = 330 rows / 2026-01-05 to **2026-02-28** / spend **7,483.42** / 1,341 installs / 110,531 impressions / 3,904 clicks. Six channels: meta_facebook 2,265.43, meta_instagram 1,355.97, unity_ads 1,318.85, google_uac 1,070.33, ironsource 742.91, applovin 729.93.
  - Post-2026-02-09 spend, all titles :: **8,452.64** over 280 rows and 19 consecutive days. domino_delights 5,569.66, combo_fighter 2,444.08, zombie_match_3d 438.90. Spend dated 2026-02-28 is 346.00 over 17 rows across all three titles, combo_fighter 160.88. Max date is 2026-02-28 for every title.
  - `ANALYTICS.MONETIZATION.REVENUE_DAILY_V2` :: 1,636 rows, **zero** combo_fighter, `calc_metadata.excludes_prototype = true`. `ANALYTICS.MARKETING.UA_SPEND_UNIFIED_V2` :: 4,313 rows, **zero** combo_fighter. Both confirmed as the live decoy S1 flagged.
  - `FINANCE.EXPENSES.CASH_BALANCE` 2026-02-28 :: cash_usd 2,500, monthly_net_burn 22,500, runway_months 0.1, headcount 6, notes "Company wind-down initiated".
  - `FINANCE.EXPENSES.MONTHLY_BURN` 2026-02 :: six category rows summing to 20,000 against CASH_BALANCE's 22,500. Known risk-register item 2; deliberately kept off the OE critical path.
  - Zero combo_fighter rows in `USER_COHORT_RETENTION`, `LEVEL_PERFORMANCE`, `LIVE_EVENT_PERFORMANCE` and `APP_STORE_REVIEWS`. No OE step asks for cohort or level data for this title.
- `_aux/Universe_Split/slack.2026-02.json` :: all 212 #winddown (C0ADGSZKR3R) messages reconstructed in timestamp order. Authorship 166 Leonard Hayes / 22 Arthur Blake / 21 Robert, which is the membership proof for Robert's scoped read. Range 2026-02-09 18:53 to 2026-02-13 19:40 UTC. Grounded every money-chain timestamp cited in OE 14 through OE 16, the supersession pair, and the consolidated action list.
- `_aux/Universe_Split/slack.2026-01.json` :: campaign-ownership evidence for OE 12. Leonard Hayes shuts down a campaign 2026-01-03, asks to pause and then confirms "ok, campaigns are paused" 2026-01-11, and sets up Unity and ironsource 2026-01-13. Arthur Blake appears asking to be added as an AppLovin user, which is the opposite of account ownership.
- `_aux/Universe_Split/slack.slack.channels.json` :: C0ADGSZKR3R = #winddown, private, created 1770663237.
- `_aux/Universe_Split/confluence.confluence.spaces.json` :: four spaces, ENG / PROD / COMPANY / OPS. COMPANY chosen as the intended destination in OE 20.
- `_aux/Universe_Split/linear.linear.teams.json` :: five teams, ART / DES / ENG / EPI / ZOM. No wind-down team exists, which is why OE 22 accepts any existing team rather than pinning one.
- `_aux/Universe_Split/trello.trello.lists.json` :: UA/BD board `66da196af476ab78deaa0cef`, list "BD Follow Up" = `670015c2ecd45b634d5eec81`. Named as the alternate tracker destination.
- `_aux/Universe_Split/contacts.contacts.contacts.json` and `linear.linear.users.json` and `confluence.confluence.users.json` :: Leonard Hayes and Arthur Blake resolvable by email in all three, so OE 19 is satisfiable on more than one surface.
- `HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json` :: 17 personas. Robert = `robert@harmonygames.co`, persona_key `robert`, Executive. Leonard Hayes and Arthur Blake confirmed roster-exact.

## Tool catalog

- `HarmonyGames_Base_Universe/6_Server_Tools_Details.json` :: 276 tools across 13 services. Every tool named in `6_Oracle_Events.txt` was resolved against this file with its full parameter list before being written. Signatures confirmed in place: `slack_search_channels(query*, limit, include_private)`, `slack_conversations_history(channel_id*, cursor, include_activity_messages, limit)`, `slack_read_channel(channel*, ...)`, `slack_conversations_search_messages(search_query, ..., filter_in_channel, ...)`, `slack_send_message(channel*, text*, ...)`, `slack_conversations_add_message(channel_id*, payload*, ...)`, `slack_search_users(query*, limit)`, `snowflake_list_databases`, `snowflake_list_schemas(database)`, `snowflake_list_tables(database, schema)`, `snowflake_describe_table(table*)`, `snowflake_execute_query(sql*, limit, offset)`, `confluence_list_spaces(...)`, `confluence_create_page(space*, title*, body, parentId, bodyFormat, authorId)`, `gdocs_create_document(title*, bodyText, driveFileId)`, `gdrive_create_file(name*, content*, mimeType, ...)`, `linear_create_issue(team*, title*, description, assignee, ...)`, `trello_create_card(idList*, name*, desc, ...)`, `contacts_search_contacts(query*, limit, cursor)`.
- Gmail re-verified send-less: all 27 `gmail_*` tools read, label or trash. No OE step emails anyone.

## Correction forced by AUDIT (round 1)

- `_aux/Universe_Split/slack.2026-02.json` ts `1770765511.243329`, channel `C07C2866011` (**#executives**), Leonard Hayes :: "We have to pay to Singular ($18750), Unity (~2.348*9 months), and Helpshift ($150*8 months)". **Singular 18,750 and Unity at roughly 21,000 across nine months are stated outright.** My first draft of OE 16 and OE 18 claimed the records never state them. Robert authored **130** February messages in #executives, so the channel is squarely in his read scope, and OE 12 already reads it.
- Helpshift resolves to **1,200** here (150 x 8), superseding the **1,500** (150 x 10) at ts `1770673467.186629` in #winddown the previous day.
- **SVB alone** is genuinely unquantified across every Robert-reachable channel: ts `1770860000.975869`, `1770911000.728559`, `1770927223.969899`, no amount attached to any.
- Two further figures verified as OUT of scope and excluded from the OE: the Helpshift **300** at ts `1770765910.100299` in `#admin_foundersonly` (C04UEQVDVB7), where the only February author is Leonard Hayes, and the **12K** third-party fiduciary line at ts `1770927719.631589` in DM `D04UC0UEN2V`, which is not among Robert's DMs.
- Robert's February authorship by channel, the persona-reachability map used above: D07H86MV4DN 230, **executives 130**, prototype 130, D04UP2L3E3S 100, D05SJRKTUMS 24, **winddown 19**, company-internal 8, D05PJG45YA2 7, D04V95AAAHW 4, mpdm 3, D05UDNCCFEW 2.
- **Method lesson, recorded because it is the reusable part.** Both councils swept only `#winddown` and both returned GO on a false-absence claim. An "X is stated nowhere" assertion is only as good as the channel set it was tested against, and the persona-authorship map is the correct denominator for that sweep, not the channel the topic lives in.

## Deterministic gates run this phase

- `Validators/phase_ready.py --phase s2` :: initially FAILED on a malformed upstream `Verification_s1.md`. Repaired (see Discrepancies in `Verification_s2.md`), then clean.
- `Validators/validate.py --phase oe` :: PASS, 0 fails, 0 warns, 3 notes, 23 OE steps. One action-verb warn on the first draft, fixed by rewording 14 OE openings to catalogued action verbs.
- `Validators/check_persona_acl.py` :: 0 findings.
- `Validators/verify_universe_atoms.py` :: PASS, 0 fails, 0 warns, 3 atoms checked.
