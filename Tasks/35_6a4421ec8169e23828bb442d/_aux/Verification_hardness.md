# Verification — HARDNESS

## Sources consulted

### Per-task data
- `_aux/Universe_Split/email.emails.json` :: 7,287 emails scanned; 5 ransomware-related hits verified (email_email_8851e5637a6c, email_email_7aa25e7b6472, email_email_985ac55f2911, email_email_fc27f9914e8b, email_email_b2572b3105dc). Full body content read for lever grounding.
- `_aux/Universe_Split/slack.slack_messages.json` :: 573 messages scanned; 20 messages tagged on ransomware/restore/backup/2 BTC keyword set. Channel distribution verified (C001×4, C008×1, C002×1 decoy, additional adjacent hits).
- `_aux/Universe_Split/slack.slack_channels.json` :: 26 channels enumerated; Robert-relevant DMs confirmed (D_grace_robert, D_DENISE_ROBERT, D_grace_robert_denise, D_denise_grace).
- `_aux/Universe_Split/slack.slack_users.json` :: 30 users; Robert (keystone_e85bc913c756), Grace (keystone_e304643b171b), Denise (keystone_a989261d4d33), Raj (keystone_74dd8dde44e3), Marcus (keystone_a583f044387a), Priya Chakrabarti (keystone_9e2a42732bb6) resolved.
- `_aux/Universe_Split/mortgage_los.conditions.json` :: 32 rows; 8 outstanding across 4 loans (los_loan_8a34a3b1383b, los_loan_4c7c66c21c94, los_loan_58b56696d513, los_loan_ad53e691489a) confirmed as L10 structured-DB skip surrogate alternate surface.
- `_aux/Universe_Split/mortgage_los.loans.json` :: 644 loans; LN-2026-00601 confirmed as clear_to_close (ransomware-at-risk closing).
- `_aux/Universe_Split/crm.crm_engagements.json` :: 472 rows; 22 Robert-related engagements including load-bearing crm_engagement_f1cb06ea7b65 (2026-03-20 "Leadership weighing pay vs restore") and crm_engagement_b95df55fbf01 (2026-04-14 "Escalated to Robert. 3 borrower files in post-term access review; borrower notice may be needed") — both used as primary L10 structured-DB skip anchors and L25 existing-output supersession anchors.
- `_aux/Universe_Split/quickbooks.bills.json` :: 585 bills; zero cyber-counsel / Sloane / ransomware-related bill hits confirmed (verified absence — the ransomware cost surface is not seeded in bills, informing lever choice not to over-weight QuickBooks).
- `_aux/Universe_Split/contacts.contacts.json` :: 889 contacts; five Bennett-* legal contacts enumerated (lauren.bennett@icloud.com, lbennett@bennettfairlendinglaw.com, laura.bennett@bennettethicslaw.com, lbennett@bennettcyberlaw.com, laura.bennett@bennettstokeslaw.com) alongside Megan Sloane at wardbarrettlaw.com — near-miss entity opportunity verified.
- `_aux/Universe_Split/email.threads.json` :: 2,504 threads; no direct ransomware-keyword hits at thread level (threads may not carry subject text in this split — email-level scan sufficed).
- `_aux/Fact_Ledger.json` :: atom counts confirmed (emails 1923 / amounts 4446 / dates 808 / slack channels 8 / personas 1306). Non-zero surfaces confirm real grounding material.
- `_aux/Feasible_Surface.json` :: 21 tables + 29 enum columns skimmed. Loan status enum (application → closed pipeline) and condition status enum (outstanding/cleared) match runbook expectations.
- `_aux/Universe_Index/service_inventory.md` :: 34 sources across 8 services; densest sources identified (document_checklist_items 8841, emails 7287, fc_transactions 3228, threads 2504, charges 1730).
- `_aux/Universe_Index/graph_report.md` :: person density confirms Robert at rank ~15+ (Marcus at 146 sender mentions; Robert not in top 30 by raw density — matches PersonaBrief note that Robert's role is executive escalation, not day-to-day ops).
- `_aux/Universe_Index/key_facts.md` :: 7,287 emails / 573 slack messages / channel counts (C002=334, C001=55, C004=28, C008=24, C003=23, C006=21, D_grace_robert=21, D_denise_grace=10).
- `_aux/Universe_Index/today_horizon.json` :: universe_today 2026-04-28 America/New_York; last_event 2026-08-04T21:25:33+00:00; records_dated_after_today 8940 (legitimate future-dated status).
- `_aux/S0_Setup_Report.md` :: task anchors + 7 open scenarios + KeyStone landmine list (TRID, Marcus Webb, no account-number trap).
- `PersonaBrief.txt` :: Robert's 7 executive open threads + key relationships (Grace, Denise, Priya Chakrabarti, Megan Sloane, Laura Bennett).

### Eval spec
- `Evals_keystone/1_Prompt_Eval.md` — N/A at HARDNESS; consulted at S1. HARDNESS is lever selection only, not prompt evaluation.
- `Evals_keystone/2_Oracle_Events_Eval.md` — N/A at HARDNESS; consulted at S2.
- `Evals_keystone/3_Rubrics_Eval.md` — N/A at HARDNESS; consulted at S3.
- `Evals_keystone/4_Verifier_Fails_Eval.md` — Trajectory dim `Tool Call Count` (>= 15 floor per Eval spec; pipeline-internal design target 50+ midpoint) is the ONE eval sub-dim relevant to HARDNESS density projection. Consulted for the 15-floor comparison. Projected midpoint 52 clears both bars.

### QC spec
- `Docs_keystone/1_Prompt_V3_Guidelines.md` — N/A at HARDNESS; the 500-word cap / no-em-dash / no-tool-name rules bind at S1 not HARDNESS.
- `Docs_keystone/2_Rubrics_V3_Guidelines.md` — N/A at HARDNESS; rubric sub-dims bind at S3.
- `Docs_keystone/3_OE_V3_Guidelines.md` — N/A at HARDNESS; OE conventions bind at S2.
- `Docs_keystone/4_Prompt_Hard_Tips.md` — Consulted implicitly via Reference/Hardness_Playbook.md (Playbook 11-lever catalog is the Hard-Tips distillation). No additional pull needed.
- QC Trajectory T1 (Tool Call Count) is the ONE QC sub-dim relevant at HARDNESS. Projected midpoint 52 places task in the PASS band (>= 50 design target).

## Data sources consulted
- `_aux/Universe_Split/` :: email.emails (7287), slack.slack_messages (573), slack.slack_channels (26), slack.slack_users (30), mortgage_los.conditions (32), mortgage_los.loans (644), crm.crm_engagements (472), quickbooks.bills (585), contacts.contacts (889), email.threads (2504) — 10 tables sampled for lever scanning.
- `_aux/Fact_Ledger.json` :: atom counts (emails 1923, amounts 4446, dates 808, slack channels 8, personas 1306) confirmed via structural skim.
- `_aux/Universe_Index/graph_report.md` :: person-density top 30 consulted; ransomware scenario cross-referenced against email-sender density (Robert rank confirms escalation role).

## Reference docs consulted
- `Reference/Hardness_Playbook.md` :: All 11 Playbook levers evaluated; 5 selected via Learnings mapping (§L8→L8, §L9→L1, §L10→L2, §L25→L10, §L26→L4). 3 partial (L3/L5/L11). 0 no.
- `Tasks/_meta/Learnings.md` :: §L8 (three cross-service reductions), §L9 (authority-figure dismissal), §L10 (structured-DB skip), §L24 (soft-verb rule for §L9), §L25 (existing-output anchor), §L26 (decoy parent thread), §L28 (tool-variant filesystem trap — advisory for S2), §L6 (correct-answer-in-artifact prohibition — advisory for S1), §L15 (implicit-prompts rule — advisory for S1). §L4 (near-miss entity alone is insufficient) noted as supporting-density-only.

## Eval spec sub-dims relevant to this phase
- Trajectory dim `Tool Call Count` (>= 15 floor per spec; pipeline internal target 50+ midpoint) :: projected midpoint = 52.0, range 41-63. PASS band (>= 50). Even low-end 41 sits above spec floor and above pipeline THIN threshold of 40.

## QC spec sub-dims relevant to this phase
- Trajectory T1 `Tool Call Count` :: projected midpoint = 52.0, band = PASS (>= 50 design target). Also passes internal THIN threshold (40-49) and INSUFFICIENT threshold (< 40).

## Verification statements
- [x] At least 3 levers selected (target 4-5); each cites a Learnings.md entry. → 5 levers selected. Each cites a specific Learnings §L<n>: §L8, §L9 (with §L24), §L10, §L25, §L26.
- [x] Density midpoint projection is one of {PASS >= 50, THIN 40-49, INSUFFICIENT < 40}. → Midpoint 52.0 = PASS.
- [x] Service breadth table populated (v11 G1). → 8 distinct services, dominant email at 23% (<< 60% cap), all services >= 5%. PASS breadth gate.
- [x] Stump hypothesis has 2-4 predictions with confidence + mechanism. → 4 predictions delivered ([HIGH]×2, [MED]×2), each with confidence + Learnings mechanism + Playbook lever + specific rubric prediction + anchoring scenario tag.
- [x] Anchoring scenario named for S1. → `scenario_14b3ffde` (ransomware pay-vs-restore) named in Persona and Business Function section and re-stated in Hardness Brief.

## Discrepancies surfaced (if any)
- Ransomware evidence timestamps (2026-03-20 emails / 2026-03-20 to 2026-03-25 Slack) predate universe today (2026-04-28) by ~5 weeks. PersonaBrief describes the scenario as still-active pending Robert's decision. The gap is expected for a real-world escalation-review flow (outside counsel deliberation, backup viability testing, executive scheduling). No inconsistency with universe data; the 2026-04-14 CRM engagement `crm_engagement_b95df55fbf01` is the connecting artifact between the initial incident and the current pending-decision state. This is fine hardness-wise — actually reinforces Learnings §L4 (search-result-cap eviction risk on the older thread).
- KeyStone universe has NO `mortgage_los.disclosures` table in the split; TRID timing landmine (LE-3-day / CD-3-business-day) cannot be directly verified at HARDNESS. Disclosures may live inside `document_checklist_items` (8841 rows — not sampled at this phase). This is not a blocker for the ransomware anchor scenario but should be flagged to S1 if any TRID-adjacent lever surfaces.
- `email.threads.json` returned zero direct keyword hits on ransomware/privileged/Sloane at thread level — email-level scan was sufficient. Threads table likely holds thread_id / participant metadata rather than subject content. No blocker.
- Robert's primary email is `robert.calloway@keystonemortgage.com` but his Slack profile is `r.calloway@keystonemortgage.com` and Denise's 2026-03-20 email `email_email_fc27f9914e8b` addresses him at `r.calloway`. This addressing near-miss is captured in Playbook Lever 6 evidence but not made load-bearing (would fall to §L4 alone, insufficient per Learnings).

## Verdict
**PASS** — 5/5 levers selected with Learnings citations, density midpoint 52.0 (>= 50 design target), service breadth 8 distinct with dominant 23%, anchor scenario `scenario_14b3ffde` named. Proceed to S1.
