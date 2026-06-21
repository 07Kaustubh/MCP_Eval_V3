# OE Solvability and Coverage — S2

Task: `24_6a36e84723508b4e3f391cfc` (REDO rebuild). Universe today 2026-06-12 (US/Eastern).
Deliverable: `6_Oracle_Events.txt` (22 OEs). Validator PASS. Council A GO. Council B GO (density ~46 to 48, all 5 levers preserved).

## Reconciliation note (Hardness_Plan vs real data)

The Hardness_Plan named BeaconPay / GraniteRack / TimeLedger as the "top 3 aged" per-vendor chains. The real per-task data is more nuanced, and the OE was grounded against it:

- The compound-rank (age x outstanding dollars) worst offenders on the external-vendor account family (210000), past 80 days, are large `acme_cloud` invoices: CivicSquare ($289,217.86 / 302d, compound #1), VaultKey ($460,556.46 / 137d, top dollar, compound #2), Clearpoint, PensionBridge, AssurePath, and high-age BeaconPay ($108,826.27 / 320d). All carry `approver = null` and have no documented dispute, so their per-vendor read is "approval chain with no owner on the AP side" (AP's problem).
- The differentiated-cause vendors are smaller dollar and surface via the prompt's mandated cross-check (the open Linear AP ticket + the Owen/Daniel void-and-rebill and partner-sign-off email threads + the C010 Slack history): GraniteRack = superseded SOW (procurement), TimeLedger VEN-010-514242 = missing credit memo (AP), Pinecrest = vendor dispute.
- GraniteRack's headline void-and-rebill invoice VEN-012-753165 is coded to account 219000 (set aside by the external-vendor lens) but is reached through the void-and-rebill thread; GraniteRack also has aged 210000 siblings. OE3 frames the 210000/219000 split as a scoping lens, not a strict vendor-versus-employee guarantee, so this is consistent and not a Completeness defect (Council B confirmed).

## Forward coverage: every prompt ask maps to an OE step

| Prompt ask (sentence) | OE step(s) |
|---|---|
| Vendors calling about outstanding payments; procurement owns relationship, AP owns the queue; triage before pushing to Priya/Daniel | OE 1 (persona + routing context), OE 22 (defer authority) |
| Snapshot of pending-approval AP queue across Brookfield, Northstar, Acme | OE 2 |
| Lens = age against outstanding dollars together, not top-dollar alone | OE 4, OE 5 |
| Past 80 days is the band | OE 4 |
| Stay on external-vendor activity; employee reimbursements are a different account family, not ours | OE 3 |
| Three to five worst offenders, per-vendor read from procurement angle | OE 5, OE 7, OE 11 to OE 14 |
| Classify holdup: stale/superseded SOW, missing change order, out-of-scope line, active vendor dispute, missing credit memo, or orphan approval chain | OE 11 (SOW), OE 12 (credit memo), OE 13 (dispute), OE 14 (orphan) |
| First three are procurement's; last two are AP's | OE 11 (procurement), OE 12 + OE 14 (AP), and the ownership split surfaced in OE 18 / OE 22 |
| Cross-check vault engagement records, the open AP exception ticket on the issues board, partner sign-off / void-and-rebill threads from Owen or Daniel | OE 8 (Linear), OE 9 (email), OE 10 (Slack), OE 16 (vault) |
| For any 80+ day Acme/Northstar item, scope confirmation before routing; Acme evolved via addendum + change order (multiple docs); Northstar engagement letter cleaner | OE 16 |
| If a record is restricted and unreachable without an access grant, say so plainly, do not call it missing | OE 17 |
| Daniel's payables-channel claim that departed-approver routing was patched last sprint; check whether invoices dated after the patch are still orphaned (signal for Priya) | OE 10 (find the claim), OE 15 (test whether it held) |
| Post a summary in the payables channel for Priya and AP with the per-vendor read and ownership | OE 18 |
| Drop a comment on the open AP-routing orphan-approver ticket with procurement-side evidence | OE 19 |
| Draft an email to Daniel with Steven on copy on vendors needing partner sign-off for release | OE 20 |
| Set a reminder to re-check in seven days | OE 21 |
| Not approving or routing; Priya, Daniel, Steven own that call | OE 22 |

No prompt ask is left without an OE step (Council B forward sweep clean).

## Reverse coverage: every OE step maps to a real prompt ask

OE 1 to OE 7 (discovery: contacts/channel, queue pull, account-family scope, age band, compound rank, null-approver signal, per-invoice drill) all serve the snapshot + worst-offender asks. OE 8 to OE 10 (Linear/email/Slack cross-check) and OE 16 to OE 17 (vault scope + access constraint) serve the explicit cross-check and scope-confirmation asks. OE 11 to OE 14 are the per-vendor classification. OE 15 is the routing-fix-held check. OE 18 to OE 21 are the four mandated writes. OE 22 is the defer-authority finale. No OE step goes beyond the prompt (no scope creep; Council B reverse sweep clean).

## OE-to-rubric mapping preview (for S3)

| OE | Rubric type | Note |
|---|---|---|
| OE 1 to OE 4 | none (discovery) | The downstream Outcome rubrics prove the queue pull, account-family scope, and 80-day band happened. |
| OE 5 | Outcome 2.1 | Worst offenders identified by compound exposure (age x dollars), not top-dollar; high-age mid-dollar BeaconPay surfaced. |
| OE 6 | Outcome 2.1 | Null-approver systemic signal reported (orphan-approver pattern, not vendor disputes). |
| OE 7 | none (discovery) | Per-invoice confirmation underpins the OE 11 to OE 14 classifications. |
| OE 8 to OE 10 | none (discovery) | Cross-check that feeds the per-vendor reads and the routing signal. |
| OE 11 | Outcome 2.1 | GraniteRack = stale/superseded SOW, procurement owns. |
| OE 12 | Outcome 2.1 | TimeLedger VEN-010-514242 = missing credit memo, AP owns; distinct from the VEN-010-693199 W-9 item. |
| OE 13 | Outcome 2.1 | Pinecrest = active vendor dispute. |
| OE 14 | Outcome 2.1 | High-compound acme_cloud items = orphan approval chain (AP owns); LatticeHill VEN-033-86573 not conflated with BeaconPay VEN-033-26339. |
| OE 15 | Outcome 2.1 | Routing fix did not hold (post-claim invoices still approver null); signal for Priya. |
| OE 16 | Outcome 2.1 | Acme scope from addendum + change order (not "missing"); Northstar engagement letter. |
| OE 17 | Outcome 2.1 | Restricted-access constraint stated plainly, not reported as missing. |
| OE 18 | Outcome 1.1 + 1.2 | Slack post to C010: existence (1.1) + content per-vendor read and ownership split (1.2). |
| OE 19 | Outcome 1.1 + 1.2 | Linear comment on issue_378874...: existence (1.1) + procurement-side evidence content (1.2). |
| OE 20 | Outcome 1.1 + 1.2 | Email to Daniel cc Steven: existence + recipients (1.1) + partner-sign-off vendor content (1.2). |
| OE 21 | Outcome 1.1 + 1.2 | Reminder: existence (1.1) + 7-day due date and scope content (1.2). |
| OE 22 | Outcome 2.1 | Defer approval/routing authority to Daniel, Steven, Priya; no approve/route action taken. |

Process rubrics: default zero. The ordering (discovery before writes) is provable through the Outcome rubrics, so no Process rubric is anticipated unless the three-condition test passes in S3.

Outcome count will exceed any Process count (Process expected = 0), consistent with the V3 reference tasks.
