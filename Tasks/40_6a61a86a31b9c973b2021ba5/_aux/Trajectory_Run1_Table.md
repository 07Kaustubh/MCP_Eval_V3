# Independent Run-1 Pass/Fail Table — Task 40

**Independence caveat:** The verifier fails files were already read before this table was built (see earlier density-blocker verdict draft). Where our independent read matches the verifier verbatim it is because trajectory evidence supports the same conclusion; where we DIVERGE we note it explicitly and re-walk the trajectory.

## Opus Run 1 (Agent_Responses/Opus/Run1_Trajectory.json) — 49 rubrics

| # | Rubric (short) | Our read | Verifier | Notes |
|---|---|---|---|---|
| 1 | Airtable update called (rec92f4a1c8e17bd3) | Pass | Pass | update_records_for_table item 79 |
| 2 | Airtable fldPriority = selHigh | Pass | Pass | Priority=High (maps to selHigh) |
| 3 | Airtable desc: overnight escalation | Pass | Pass | "follow-up call the evening of 06-30 reported the problem worsening" |
| 4 | Airtable desc: tenant without hot water | Fail | Fail | Desc says "intermittent hot water" — not "no hot water" |
| 5 | Airtable desc: active leak w/ occupants at home | Fail | Fail | Desc doesn't mention leak or occupants |
| 6 | Airtable desc: full unit replacement scope | Pass | Pass | "FULL UNIT REPLACEMENT (approx $1,850, equal-model swap)" |
| 7 | Airtable desc: ~$1,850 | Pass | Pass | "approx $1,850" |
| 8 | Airtable desc: Thursday install retained | Pass | Pass | "Install scheduled Thursday 07-02 AM with Hill Country" |
| 9 | Linear OPS-231 update called | Pass | Pass | save_issue item 81 |
| 10 | Linear desc: full unit replacement scope | Pass | Pass | Description covers full replacement |
| 11 | Linear desc: ~$1,850 | Pass | Pass | "approx $1,850" |
| 12 | Linear desc: Thursday install retained | Pass | Pass | "Install Thursday 07-02 AM (Hill Country)" |
| 13 | Linear comment added | Pass | Pass | save_comment item 83 |
| 14 | Comment: diagnostic write-up on Hill Country bill | Pass | Pass | Cites B2026-211 diagnostic write-up |
| 15 | Comment: full unit replacement | Pass | Pass | "recommends full unit replacement (~$1,850 equal-model swap)" |
| 16 | Comment: 12 year age | Pass | Pass | "On the 12-yr Ruud RS75" |
| 17 | Comment: Ruud RS75 | Pass | Pass | Model named |
| 18 | Comment: supersedes narrow exchanger swap | Pass | Pass | "That does not line up with the emailed/Slack summary (exchanger swap + new thermocouple, ~$310)" |
| 19 | Comment: overnight tenant escalation | Pass | Pass | "Tanya's follow-up call the evening of 06-30 confirmed the problem worsened" |
| 20 | Comment: tenant without hot water | Fail | Fail | Comment doesn't explicitly say "no hot water" |
| 21 | Comment: active water pooling w/ occupants at home | Fail | Fail | Comment doesn't mention pooling or occupants |
| 22 | Comment: Thursday install retained for fuller scope | Pass | Pass | "Hill Country confirmed for Thursday AM (07-02)" |
| 23 | Slack post send (C001, thread_ts 1782824160.000302) | Fail | Fail | **Agent explicitly said "One thing I did not do: post in #maintenance to Tony."** Only slack call was slack_search_public (item 7). |
| 24 | Slack: corrected scope | Fail | Fail | Cascade — no post attempted |
| 25 | Slack: escalation to High | Fail | Fail | Cascade |
| 26 | Slack: Thursday slot kept | Fail | Fail | Cascade |
| 27 | Gmail draft to ap@hillcountryplumbing.com | Pass | Pass | create_draft item 89 |
| 28 | Diane draft: full replacement | Pass | Pass | "full water heater replacement, equal-model Ruud RS75" |
| 29 | Diane draft: 12 year age | Pass | Pass | "the 12-year-old Ruud RS75" |
| 30 | Diane draft: Ruud RS75 | Pass | Pass | Named |
| 31 | Diane draft: ~$1,850 | Pass | Pass | "about $1,850 for an equal-model swap" |
| 32 | Diane draft: Thursday morning slot | Pass | Pass | "Please keep the Thursday morning (July 2) slot" |
| 33 | Gmail draft to tanya.mitchell@gmail.com | Pass | Pass | create_draft item 91 |
| 34 | Tanya draft: full replacement | Pass | Pass | "replace the whole water heater with a comparable new unit" |
| 35 | Tanya draft: Thursday morning timing | Pass | Pass | "Thursday morning (July 2)" |
| 36 | Tanya draft: realistic hot water expectation | Pass | Pass | "back to normal — and more reliable — by Thursday afternoon" |
| 37 | Tanya draft: no internal $ figures | Pass | Pass | No dollar amounts surfaced |
| 38 | Gmail draft to robert.finley@gmail.com | Pass | Pass | create_draft item 93 |
| 39 | Robert draft: initial ~$310 quote | Pass | Pass | "roughly $310 for the partial repair" |
| 40 | Robert draft: initial exchanger swap scope | Pass | Pass | "the partial repair that was first floated" (analog) |
| 41 | Robert draft: new full replacement | Pass | Pass | "recommends replacing the unit rather than repairing individual parts" |
| 42 | Robert draft: new ~$1,850 | Pass | Pass | "runs about $1,850" |
| 43 | Robert draft: corrosion at burner | Pass | Pass | "corrosion on the burner assembly" |
| 44 | Robert draft: corrosion at tank base | Pass | Pass | "and tank base" |
| 45 | Robert draft: cracked heat exchanger | Pass | Pass | "a cracked heat exchanger" |
| 46 | Robert draft: 12 year age | Pass | Pass | "It's a 12-year-old Ruud heater" |
| 47 | Robert draft: Ruud RS75 | Fail | Fail | Says "12-year-old Ruud heater" — model number RS75 dropped |
| 48 | Robert draft: Thursday morning install | Pass | Pass | "Hill Country scheduled for Thursday morning (July 2)" |
| 49 | Calendar event Thursday 2026-07-02 morning at Mesa Vista 7B | Pass | Pass | create_event item 84, startTime 2026-07-02T08:00:00 America/Chicago |

**Opus Run 1 result: 40/49 pass — matches verifier exactly.**

## Gemini Run 1 (Agent_Responses/Gemini/Run1_Trajectory.json) — 49 rubrics

Independent read matches verifier at 47/49 pass. Fails:

| # | Rubric (short) | Our read | Verifier | Notes |
|---|---|---|---|---|
| 5 | Airtable desc: active leak w/ occupants at home | Fail | Fail | Desc says "active kitchen floor leak reported 06/30" — mentions leak but NOT occupants at home |
| 21 | Linear comment: active water pooling w/ occupants at home | Fail | Fail | Same pattern in Linear comment — mentions leak/pooling, misses occupants atom |

**Gemini Run 1 result: 47/49 pass — matches verifier exactly.**

## Divergence log
No divergences. Our independent trajectory read agrees with the verifier for every failing rubric in both models' Run 1.

## Signal interpretation
- All Run-1 fails are Bucket 3 candidates (legitimate model failures) — trajectory evidence confirms the agent either did not attempt the action, attempted with wrong parameters, or omitted a required atom from generated content.
- No Bucket 2 (judge error) candidates in Run 1 for either model.
- No Bucket 1 (rubric invalid) hard candidates — the failing atoms are all real, prompt-derived, and achievable (proven by other runs / cross-model passes).
- The Gemini R5 bundle ("active leak with occupants at home") is technically two-atom; noted as a soft refinement suggestion but not a rebuild blocker. See Bucket 1 fixes for the atomicity refinement note.
