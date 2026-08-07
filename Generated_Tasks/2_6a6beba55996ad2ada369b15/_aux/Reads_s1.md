# Reads — S1 (`2_6a6beba55996ad2ada369b15`)

Running log. One line per spec doc / reference card / eval read, with what it settled.

## Runbook + task state

- `Reference/Sessions/S1.md` :: phase contract. Exit criteria: validator PASS, Council A GO, Council B GO, B3 density, B4 lever preservation, similarity composite < 40, AUDIT PASS (STRICT). Note the density line in the runbook cites the V3-family 50/40 bands; HarmonyGames uses its own scheme (40 target / 15 floor) per the Hardness Plan and `Docs_harmonygames/4_Prompt_Hard_Tips.md:96`.
- `Reference/AGENTS.md` :: HG authors into `Generated_Tasks/`, framework `hg` = single-model verification + V4 injection/submission_gate phases.
- `Generated_Tasks/2_6a6beba55996ad2ada369b15/_aux/Hardness_Plan.md` :: 5 selected levers (L11 net-vs-gross, L2 Snowflake FINANCE skip, L8 multi-link chain, L10 supersession, L7 multi-write), density midpoint 47.0, 8 services, 9-item risk register, Hardness Brief. **Carries an explicit unresolved operator fork on the storyline spine (plan section "Open question for the operator").**
- `Generated_Tasks/.../1_Business_Function.txt` :: Executive. `2_Persona.txt` :: Robert, Co-Founder & Creative Director. `PersonaBrief.txt` :: `robert@harmonygames.co`, persona_key `robert`, design/art-direction lead, wind-down and Combo Fighter both in scope.
- `Generated_Tasks/.../3_UniverseDataForThisTask.json` :: the 940-byte contract descriptor, NOT data (hard rule 2). Source of truth is `HarmonyGames_Base_Universe/Services_Data/` + `4_Changelog.json` (which is `[]`, so no injection).
- `_aux/Universe.txt` :: `harmonygames`.

## Format cards

- `Reference/Prompt_Format.md` :: 500-word cap + em-dash ban are PROJECT POLICY for hg (not upstream spec), applied on operator ruling. today = 2026-02-28, a Saturday and month-end; weekend routine-comms trap and the "Q1 close is incoherent, Q1 has a month to run" trap. Never construct a persona email from a name; resolve via `4_Persona_ACL_Roster.json`. Density is three separate thresholds, not one.

## HarmonyGames spec docs

- `Docs_harmonygames/9_Common_Error.md` :: read BEFORE drafting per the S1 required-inputs table. Prompt-side misses ranked by frequency in the n=12 cohort: contrived/spec-sheet register 5/12 (state the goal and the deliverables, then stop, do not enumerate their contents), Unique Ground Truth 4/12 (two defensible readings producing different end states = FAIL), clarity/action-decision ambiguity 4/12, truthfulness 4/12 (check every stated premise against `Services_Data/`). Also: no giving away discoveries, no tool script, no MCP/function names, no pre-solving, no bolt-ons (remove-any-sentence test), **no requesting unavailable actions (Gmail cannot send/reply/compose/draft; Snowflake read-only; Singular/Firebase/Stripe etc. are topics not tools)**, no broken relative time, and do not substitute one complexity threshold for another.
- `Docs_harmonygames/4_Prompt_Hard_Tips.md` :: empirical, intuition not policy. Agents skip structured systems (the L2 lever's basis, Snowflake named explicitly at :15). Agents latch onto the first framing (the L11 lever's basis, :35). Agents stop at the first plausible status and miss follow-up evidence (:31). Go broad not specific (:76). Hint without giving away, e.g. "double-check my assumptions" (:78). Do NOT add writes to inflate call count; every write must be a realistic part of the outcome (:84). Design target 40+ necessary calls across 3+ services; prompt-eval gate >15 necessary + 2 services; trajectory floor >=15 average (:96). ACL-denied reads and `set_acting_user` count toward none of it (:98).
- `Docs_harmonygames/README.md` :: fixed environment block states "scoped reads on Gmail, Slack, GCal, and Contacts only". **This contradicts `14_Persona_ACL.md:52`** (scoped = Gmail/Slack/GCal/GDrive/GDocs/GSheets/GSlides; unscoped = Contacts/GitHub/Snowflake/Trello/Linear/Confluence) and `4_Prompt_Hard_Tips.md:19-24`, which agree with each other and with the project registry. Two of three sources plus the dedicated ACL doc win; `README.md` is treated as stale on this point. Not load-bearing for this task either way, since the planned reads are Slack (persona-authored channels, confirmed by authorship) and Snowflake (unscoped under every reading).

- `Docs_harmonygames/6_Prompt_Relative_Time_Updates.md` :: date SSOT. today = 2026-02-28, a Saturday, last day of February, second month of Q1; Q1 does not end until March 31, so "Q1 close" or "Q1 results are final" is incoherent. Relative phrases resolve against this baseline ("next Friday" = 2026-03-06). Author checklist item 3, verify the resolved window actually contains records, drove the Combo Fighter date-range check below.

## Reference corpus (voice / structure)

- `QC_Tasks/V5_HG_Buckets/QC_Passed/Task2_6a62909d918832d268962da6_HG/5_Prompt.txt` :: ~330 words, four paragraphs, register-building ask, ends with a reply ask ("Send me the usable spreadsheet link, the verified row count, and the recommendation you shared").
- `QC_Tasks/V5_HG_Buckets/QC_Passed/Task4_6a629f9fde3bc1f8e747e72b_HG/5_Prompt.txt` :: ~470 words, five paragraphs, investigative brief ending in three writes plus a reply ask. Together these confirm HG tolerates a longer and more deliverable-explicit register than the Brookfield reference prompts. But `9_Common_Error.md`'s 5/12 spec-sheet miss means that length is the CEILING, not the target. Draft settled at 398 words.

## Council Protocol

- `Reference/Council_Protocol.md` :: Council A 9 active perspectives, Council B 8. B3's stated bands (50 design target / 40 floor) are the V3-family scheme, so the HG bands (40 target / 15-39 THIN / <15 INSUFFICIENT) were passed to Council B explicitly in its brief to prevent scheme drift.

## Verified directly against `_aux/Universe_Split/` (first-hand, not carried from any prior phase)

- `slack.2026-02.json` :: reconstructed all 212 February messages in #winddown (C0ADGSZKR3R) in timestamp order. Confirmed the 02-09 shutdown decision and its stated cause, the $22,500 offer against the $11,700 charge (ts `1770911000.728559`), the sale-to-licence restructure with cash consideration unchanged (ts `1770924424.711879`, `1770924465.624129`), the consolidated vendor disposition (ts `1770933601.686309`), board-level personal liability (ts `1770674426.735229`), and Leonard's outstanding angel outreach (ts `1770934638.035469`).
- `snowflake.snowflake.tables.json` :: streamed line by line, never fully loaded (159 MB; hard rule 33). Confirmed `FINANCE.EXPENSES.CASH_BALANCE` at month_end_date 2026-02-28 = cash_usd 2500, runway_months 0.1, monthly_net_burn 22500, notes "Company wind-down initiated".

## Corrections this reading forced on inherited premises

1. **The licensed data is the company corpus, not game telemetry.** Leonard at ts `1770858442.063329` states the Figma export is for "giving us quote on much much our company data is worth for ai labs"; the inventory discussed is Slack messages, Figma files, Google, GitHub and Analytics. Any framing asserting the data deal and the Combo Fighter post-mortem concern the same asset would be untruthful. The draft therefore does NOT make that claim.
2. **`LEVEL_PERFORMANCE` and `USER_COHORT_RETENTION` carry ZERO Combo Fighter rows** (1500 rows = Domino Delights 1000 + ZM3D 500; 214 cohort rows, none Combo Fighter). No ask or downstream criterion may assume level-difficulty or cohort-retention data exists for that title, which matters because those are exactly the surfaces Robert's role would reach for first.
3. **The `_V2` tables are a live decoy.** `REVENUE_DAILY_V2` (0 CF rows) and `UA_SPEND_UNIFIED_V2` (0 CF rows) against `REVENUE_DAILY` (72) and `AD_SPEND_DAILY` (330). A run that reaches for the newer-looking table concludes no Combo Fighter data exists at all.
4. **Combo Fighter's own numbers**, for grounding the ask rather than for the prompt body: DAU 2026-01-05 through 2026-02-09 growing from ~22 to ~420 per platform with D1 retention ~37-46%, against total_revenue_usd of exactly 0.00 on all 72 revenue rows. Acquisition spend $7,483.42 total, and `AD_SPEND_DAILY` runs through 2026-02-28 while revenue stops at 02-09, i.e. spend continued for 19 days past the shutdown decision ($2,444.08 on Combo Fighter, $8,452.64 across all three titles, $160.88 dated today). No February message pauses campaigns, and the 02-12 wind-down action list never mentions the ad networks, so the premise is uncontradicted.
5. **The January pause is deliberately NOT load-bearing.** ts `1768166394.438899` (2026-01-11 21:19 UTC, channel C07C2866011, Leonard) records "ok, campaigns are paused", but Combo Fighter daily spend does not dip on 01-12; it rises from $96.72 to $198.67. That single inconsistency is confined to January and is superseded by explicit restart discussion on 01-22, 01-24 and 02-06. Nothing in the draft or the intended solution path depends on it.
