# Rubric Coverage Matrix — Task 35 (S3)

**AUDIT verdict:** PASS (STRICT) — all 7 active lenses cleared. Validator PASS (0/0/5). Council A GO. Council B GO (5/5 all QC dims).

Rubric numbering below uses 0-indexed `rubric[N]` as the validator reports. 35 rubrics total (35 outcome, 0 process). Below maps every prompt sentence + every OE step to the rubric(s) that verify it, and back-maps every rubric to its prompt anchor + OE.

## Prompt → OE → Rubric forward map

| Prompt sentence / paragraph | OE step(s) | Rubric idx | Notes |
|---|---|---|---|
| "walk Raj's picture back to what the emails and records actually say" | OE 2, 3, 8, 16 | rubric[4] (email covers 72-hour + rebuild + validation), rubric[5] (email covers LOS integrity caveat), rubric[20] (memo pay-vs-restore section: 72-hour + rebuild + validation), rubric[21] (memo LOS integrity caveat), rubric[27] (restore is a lift not foreclosed), rubric[28] (approximately 72 hours), rubric[29] (Raj LOS integrity caveat) | Walking Raj's picture back = L9 authority-dismissal lever, must present as tradeoff enumeration not foregone conclusion |
| "If restore is still a lift, I want the specific gaps and rebuild items as tradeoffs, not a foregone conclusion" | OE 16, 23 | rubric[4], rubric[20], rubric[27], rubric[28], rubric[29] | Tradeoff enumeration is the required frame |
| "confirm nothing has shifted on the legal side since we asked outside cyber counsel for the sanctions and privilege read" | OE 5, 16 | rubric[7] (email requests view on sanctions/privilege), rubric[22] (memo covers sanctions/privilege posture still open), rubric[30] (no counsel reply since 3/20) | Truthful-gap check: no Sloane reply exists post-3/20 |
| "plain read of where that plan stands. Has scope narrowed. Are there specific files anyone has identified since. Anything queued I have not been looped on" | OE 11, 12, 13, 14, 15 | rubric[8]/[9]/[10] (email covers 4 portal + Raj audit + 3 post-term files), rubric[13] (Slack post covers 3 workstreams), rubric[14] (Slack post: 7 files), rubric[18] (CRM lists 7 files), rubric[23] (memo enumerates 4 + 3 files), rubric[31] (3/20 plan superseded/expanded), rubric[32] (final response: 7 files aggregate), rubric[33] (Raj-audit stream), rubric[34] (ransomware-attributable scope preliminary) | L25 supersession + L10 structured-DB skip on CRM engagements |
| "Do not take the March framing at face value. Anything feeding the same borrower notice counts, even from a separate workstream" | OE 12, 13, 14, 15, 23 | rubric[8]/[9]/[10] (email content), rubric[13] (Slack workstream posture), rubric[17] (CRM reconciled 4 workstreams), rubric[18] (CRM 7 files), rubric[23] (memo 4+3 files), rubric[31] (3/20 plan expanded), rubric[33] (Raj-audit as third feeder) | L26 decoy trap on Slack channel choice + L10 structured-DB skip |
| "write me a decision brief with the tradeoffs on the payment call, the current borrower-notice posture with any specific files, and anything counsel still needs before I decide" | OE 21, 22, 23 | rubric[3] (memo write action), rubric[19] (memo covers 2 BTC + 72h + rebuild + validation as tradeoffs), rubric[20] (LOS integrity caveat), rubric[21] (sanctions/privilege posture), rubric[22] (memo counsel-still-needs section), rubric[23] (memo borrower-notice section: 4+3 files), rubric[24] (memo: ransomware-attributable scope preliminary), rubric[25] (memo: what counsel still needs — sanctions, notice-threshold, evidence preservation) | Memo is the decision-brief deliverable |
| "Email outside cyber counsel with the reconciled picture and a request for their view on whatever is still open" | OE 1, 18 | rubric[0] (write action — Sloane at Ward Barrett), rubric[4] (restore tradeoffs), rubric[5] (LOS integrity caveat), rubric[6] (payment not authorized), rubric[7] (request sanctions/privilege view), rubric[8]/[9]/[10] (4 portal + Raj audit + 3 post-term files), rubric[11] (request what counsel still needs) | L4 near-miss trap: Sloane at wardbarrettlaw.com, NOT any Bennett-* variant |
| "Post a short status in the leadership channel so we are all reading the same room without pushing it wider than needed" | OE 6, 19 | rubric[1] (write action — Grace/Robert/Denise mpim, NOT wider), rubric[12] (Slack payment posture), rubric[13] (Slack borrower-notice posture), rubric[14] (Slack: 7 files), rubric[15] (Slack: decision brief on incident record) | L26 decoy trap on C001/C002/C008 |
| "Put a formal note on the incident record in our engagement log so the paper trail is clean" | OE 20 | rubric[2] (write action — CRM engagement NOTE), rubric[16] (CRM: payment held pending), rubric[17] (CRM: 4 workstreams reconciled), rubric[18] (CRM lists 7 files), rubric[19] (CRM: counsel re-engaged) | Engagement log = CRM engagements |
| "drop the memo itself in the incident folder alongside the counsel correspondence" | OE 21 | rubric[3] (write action — filesystem incident-folder), rubric[19]-[25] (memo content coverage) | Filesystem write; incident-folder semantics per prompt |
| "If your read differs from the picture I have been operating on, say so plainly" | OE 23 | rubric[27] (restore is a lift not foreclosed → March framing "restore is expensive as foregone conclusion" is superseded), rubric[31] (3/20 preliminary plan superseded → March framing "borrower notice is only ransomware-LOS" is superseded) | Two decisive read-differences per OE 23 |
| "Better I hear it from you now than get blindsided" | OE 23 | rubric[26] (Sloane identification, since routing to Bennett-cyber would be the blindside), rubric[27]/[31] (read-differences) | Anti-blindside surface |

## OE → Rubric back-map (every OE step verified)

| OE | Coverage | Rubric idx / Notes |
|---|---|---|
| OE 1 Sloane resolution | ✓ | rubric[0] (Sloane routing), rubric[26] (Sloane identification in final response) |
| OE 2 Raj ransomware escalation | ✓ | rubric[4]/[5] (email content) + rubric[27]/[28]/[29] (final response) |
| OE 3 Robert's 3/20 counsel request | ✓ | rubric[6] (payment not authorized), rubric[22] (memo sanctions posture), rubric[30] (no reply since 3/20) |
| OE 4 Denise's 3/20 privileged trio | ✓ | rubric[31] (3/20 plan superseded) |
| OE 5 no Sloane reply | ✓ | rubric[7] (email request), rubric[30] (final response) |
| OE 6 Slack channels_list | ✓ (density) | rubric[1] (D_grace_robert_denise pin) — infra step |
| OE 7 Slack ransomware exchange | ✓ (density) | infra — no direct rubric, feeds rubric[27]/[29] |
| OE 8 Raj's later restore-quality Slack | ✓ | rubric[5]/[21]/[29] (LOS integrity caveat) |
| OE 9 leadership triad ambient | ✓ (density) | infra — feeds rubric[1] channel choice |
| OE 10 at-risk-closings ambient | ✓ SOFT-OUTCOME | No rubric enforces (per Verification_s2.md D#4) |
| OE 11 3/20 ransomware CRM stream | ✓ | rubric[17] (CRM 4 workstreams), rubric[31] (supersession) |
| OE 12 4/07 wholesale lender portal breach CRM | ✓ | rubric[8] (email), rubric[13] (Slack), rubric[17]/[18] (CRM), rubric[23] (memo) |
| OE 13 4/07 Raj-access-audit CRM | ✓ | rubric[9] (email), rubric[13] (Slack), rubric[17] (CRM), rubric[33] (final response) |
| OE 14 4/14 Marcus Webb post-term CRM | ✓ | rubric[10] (email), rubric[13] (Slack), rubric[17]/[18] (CRM), rubric[23] (memo) |
| OE 15 borrower-notice reconciliation | ✓ | rubric[13] (Slack), rubric[14] (Slack 7 files), rubric[17]/[18] (CRM), rubric[23] (memo), rubric[31] (supersession), rubric[32] (final response 7 aggregate), rubric[34] (ransomware-attributable preliminary) |
| OE 16 pay-vs-restore reconciliation | ✓ | rubric[4]/[5]/[6]/[7] (email), rubric[19]/[20]/[21]/[22] (memo), rubric[27]/[28]/[29]/[30] (final response) |
| OE 17 at-risk-closings ops | ✓ SOFT-OUTCOME | No rubric enforces (per Verification_s2.md D#4) |
| OE 18 send email to Sloane | ✓ | rubric[0] + rubric[4]-[11] |
| OE 19 Slack leadership DM | ✓ | rubric[1] + rubric[12]-[15] |
| OE 20 CRM engagement NOTE | ✓ | rubric[2] + rubric[16]-[19] |
| OE 21 filesystem memo | ✓ | rubric[3] + rubric[19]-[25] |
| OE 22 memo three sections | ✓ | rubric[19]-[25] (pay-vs-restore, borrower-notice, counsel-still-needs) |
| OE 23 two read-differences | ✓ | rubric[27] (restore tradeoff), rubric[31] (borrower-notice expanded) |
| OE 24 no ledger writes | ✓ | Absence-check: no rubric requires mortgage_los / stripe / quickbooks writes |
| OE 25 tight-distribution posture | ✓ | rubric[1] (D_grace_robert_denise), rubric[0] (Sloane only) |
| OE 26 reconciliation across 4 writes | ✓ | rubric[8]/[9]/[10] (email files), rubric[13] (Slack workstreams), rubric[14] (Slack 7 files), rubric[18] (CRM 7 files), rubric[23] (memo 4+3 files) — reconciliation emerges from same values across 4 artifacts |
| OE 27 tool-call surface breadth | ✓ | infra — Council B B3 confirms 8 KeyStone services × midpoint 52 |

## Rubric → prompt/OE back-map (every rubric anchored)

| Rubric idx | Category | Prompt anchor | OE anchor | Universe atom |
|---|---|---|---|---|
| 0 | 1.1 | "Email outside cyber counsel" | OE 1, OE 18 | contacts_contact_f5367b22340d |
| 1 | 1.1 | "Post a short status in the leadership channel...not wider than needed" | OE 6, OE 19 | D_grace_robert_denise mpim |
| 2 | 1.1 | "Put a formal note on the incident record in our engagement log" | OE 20 | CRM engagement NOTE type |
| 3 | 1.1 | "drop the memo itself in the incident folder" | OE 21 | filesystem path semantic |
| 4 | 1.2 | "walk Raj's picture back...tradeoffs, not a foregone conclusion" | OE 8, OE 16 | email_email_7aa25e7b6472 (~72h), email_email_b2572b3105dc (rebuild + validation) |
| 5 | 1.2 | "walk Raj's picture back" | OE 8 | slack C001 ts 1774447787 (LOS integrity) |
| 6 | 1.2 | Robert's 3/20 anchor | OE 3, OE 16 | email_email_b2572b3105dc ("I am not authorizing payment at this moment") |
| 7 | 1.2 | "confirm nothing has shifted on the legal side" | OE 5, OE 16 | truthful gap (no Sloane reply post-3/20) |
| 8 | 1.2 | "specific files anyone has identified since" | OE 12 | crm_engagement_d27cd1da0d5a (4 portal files) |
| 9 | 1.2 | "Anything queued I have not been looped on" | OE 13 | crm_engagement_266683ef80a3 (Raj-access-audit) |
| 10 | 1.2 | "specific files anyone has identified since" | OE 14 | crm_engagement_985a3efbbee8, a33cc635ceed, 1b81acccf98e (3 post-term files) |
| 11 | 1.2 | "a request for their view on whatever is still open" | OE 18 | (derived request) |
| 12 | 1.2 | leadership status posture | OE 19 | (aggregated derivation) |
| 13 | 1.2 | leadership status growth | OE 19 | (aggregated derivation) |
| 14 | 1.2 | leadership status 7 files | OE 19 | (aggregated count 4+3) |
| 15 | 1.2 | leadership status → decision brief | OE 19 | (paper trail reference) |
| 16 | 1.2 | "clean paper trail" | OE 20 | (aggregated derivation) |
| 17 | 1.2 | "reconciled picture" | OE 20 | 4 workstream CRM streams |
| 18 | 1.2 | "specific files" enumeration for durable record | OE 20 | 7 loan IDs verified in mortgage_los.loans.json |
| 19 | 1.2 | counsel re-engagement | OE 20 | (aggregated derivation) |
| 20 | 1.2 | memo pay-vs-restore section | OE 22 | 2 BTC + 72h + rebuild + validation |
| 21 | 1.2 | memo LOS integrity caveat | OE 22 | slack C001 ts 1774447787 |
| 22 | 1.2 | memo sanctions posture | OE 22 | truthful gap |
| 23 | 1.2 | memo borrower-notice with specific files | OE 22 | 7 loan IDs (4+3) |
| 24 | 1.2 | memo: ransomware-attributable scope | OE 22 | (truthful qualifier) |
| 25 | 1.2 | memo: counsel-still-needs | OE 22 | sanctions + notice-threshold + evidence-preservation |
| 26 | 2.1 | Sloane routing | OE 1 | contacts_contact_f5367b22340d |
| 27 | 2.1 | "If your read differs...say so plainly" (restore) | OE 23 | Robert's 3/20 email + Raj's later Slack |
| 28 | 2.1 | quantitative tradeoff | OE 16 | email_email_7aa25e7b6472 (~72h) |
| 29 | 2.1 | Raj's later view | OE 8, OE 16 | slack C001 ts 1774447787 |
| 30 | 2.1 | "confirm nothing has shifted" | OE 5 | truthful gap |
| 31 | 2.1 | "If your read differs...say so plainly" (borrower notice) | OE 15, OE 23 | 3/20 privileged emails vs 4/07 + 4/14 CRM streams |
| 32 | 2.1 | "any specific files" aggregate count | OE 15 | 4+3=7 across workstreams |
| 33 | 2.1 | Raj-audit as third feeder | OE 13, OE 15 | crm_engagement_266683ef80a3 |
| 34 | 2.1 | "Do not take the March framing at face value" | OE 15 | (truthful qualifier) |

## Coverage summary

- **35/35 rubrics** map to a prompt sentence + OE step + universe atom (or truthful qualifier).
- **27/27 OE steps** map to at least one rubric (OE 10 + OE 17 at-risk-closings are SOFT-OUTCOME per Verification_s2.md and correctly have no rubric enforcement; OE 6/OE 7/OE 9 are infra-density steps that feed channel-selection rubrics).
- **Zero gaps**: every prompt ask has a rubric.
- **Zero surplus**: every rubric ties back to a prompt ask.
- **All 5 hardness levers** covered (§L8 chain across email/Slack/CRM/memo/final response; §L9 authority-dismissal via rubric[27]; §L10 structured-DB skip via rubric[8]/[9]/[10]/[17]/[18]/[23]/[33]; §L25 supersession via rubric[31]; §L26 decoy parent via rubric[1] channel pin).
- **Density projection**: Council B midpoint 52; AUDIT LENS 4 confirms 52 ≥ 50 target.
- **Distribution**: 4 outcome-1.1 (write actions) + 22 outcome-1.2 (content) + 9 outcome-2.1 (key facts) = 35 outcome, 0 process.
