# Rubric Coverage Matrix

Task: `24_6a36e84723508b4e3f391cfc` (AP / Vendor Operations — Lena Park, Procurement Officer)
Deliverable: `7_Rubrics.json` — 25 rubrics, all `outcome`, zero `process`.
Maps every prompt ask -> Oracle Event(s) -> rubric index(es). Confirms no gaps (every ask has >=1 rubric) and no surplus (every rubric ties to an ask).

## Rubric index reference (0-based, as ordered in `7_Rubrics.json`)

| # | Sub-type | One-line |
|---|---|---|
| 0 | 1.1 | Slack standalone post to #vendor-bills-and-ap (C010) |
| 1 | 1.2 | Slack: GraniteRack stale/superseded SOW -> procurement |
| 2 | 1.2 | Slack: TimeLedger VEN-010-514242 missing credit memo -> AP |
| 3 | 1.2 | Slack: high-compound acme_cloud items = orphan chains, no owner on AP side |
| 4 | 1.1 | Linear comment on issue_378874ffeb8f4cb0b0417021f2d3d647 |
| 5 | 1.2 | Linear comment: 320/320 pending carry null approver |
| 6 | 1.2 | Linear comment: post-patch-dated items (VEN-028-492596, MetroShield) still orphaned |
| 7 | 1.1 | Email from lena.park@ to daniel.jones@ cc steven.perry@ |
| 8 | 1.2 | Email: GraniteRack VEN-012-753165 void-and-rebill = partner sign-off item |
| 9 | 1.2 | Email: TimeLedger VEN-010-514242 = partner sign-off item |
| 10 | 1.1 | Reminder due 2026-06-19 to re-check backlog |
| 11 | 2.1 | Ranks worst offenders by compound exposure (age x $) not top-dollar |
| 12 | 2.1 | VaultKey VEN-029-961721 ($460,556.46) largest dollar but not most severe by compound |
| 13 | 2.1 | BeaconPay VEN-033-26339 ($108,826.27, ~320d) high-age underweighted by top-dollar |
| 14 | 2.1 | CivicSquare VEN-024-891664 ($289,217.86, ~302d) leading compound offender |
| 15 | 2.1 | GraniteRack VEN-012-753165 stale/superseded SOW (rev3 vs rev1) -> procurement |
| 16 | 2.1 | TimeLedger VEN-010-514242 ($24,475.25) missing credit memo -> AP |
| 17 | 2.1 | Pinecrest VEN-006-193120 ($1,040.63, ~338d) active vendor dispute (owner unassigned) |
| 18 | 2.1 | High-compound acme_cloud items = orphan chains, no owner on AP side |
| 19 | 2.1 | Acme scope = addendum (doc_eb7cb30c59bd4f03) + change order (doc_2d85ac5a698745c5) |
| 20 | 2.1 | Northstar scope = engagement letter (doc_0036f5b991574808) |
| 21 | 2.1 | Scope docs restricted; cannot read without grant; not "missing" |
| 22 | 2.1 | Routing fix did not hold (post-patch null approver) -> signal for Priya |
| 23 | 2.1 | Scopes external-vendor account family 210000 vs employee-reimbursement 219000 |
| 24 | 2.1 | Defers approval/routing to Daniel, Steven, Priya; did not approve/route itself |

## Prompt ask -> OE -> Rubric

| Prompt ask (paraphrase) | OE(s) | Rubric(s) |
|---|---|---|
| Pull pending-approval AP queue across Brookfield, Northstar, Acme; see who is stuck and how long | OE2, OE4 | 11, 12, 13, 14, 23 (worst-offender ranking + scoping are the observable outputs of the pull) |
| Lens = age x outstanding dollars (compound), not top-dollar alone; long-aged mid-dollar can drift | OE5 | 11, 12, 13 |
| 80+ days is the band of concern | OE4 | 11-18 (every named offender is 80+; band embedded in selection) |
| Stay on external-vendor activity; employee reimbursements are a different account family | OE3 | 23 |
| For 3-5 worst offenders, per-vendor read from procurement angle | OE5, OE7, OE11-14 | 1-3 (Slack), 14, 15, 16, 17, 18 |
| Classify each: stale/superseded SOW \| missing change order \| out-of-scope line \| active vendor dispute \| missing credit memo \| orphan approval chain | OE11-14 | 15 (SOW), 16 (credit memo), 17 (dispute), 18 (orphan). See "Deliberately uncovered" below for the two unused categories |
| First three categories = procurement's; last two = AP's | OE11-14 | 1+15 (procurement); 2+16, 3+18 (AP). Pinecrest dispute left unassigned (17) |
| Cross-check vault engagement records, open AP exception ticket, partner sign-off / void-and-rebill emails from Owen or Daniel | OE8, OE9, OE16 | Proven by 15, 16, 17, 19, 20, 21 (each diagnosis/scope value requires the cross-check; no standalone Process rubric needed) |
| 80+ item touching Acme or Northstar -> scope confirmation before routing | OE16 | 19, 20 |
| Acme: addendum + at least one change order (multiple docs, not a single letter) | OE16 | 19 |
| Northstar: engagement letter (cleaner) | OE16 | 20 |
| If restricted and unreachable without a grant, say so plainly; don't call it missing | OE17 | 21 |
| Daniel claimed routing rule patched last sprint; if post-patch invoices still sitting, issue is alive on AP side; Priya needs the signal | OE10, OE15 | 22 (final response); 6 (Linear comment evidence) |
| Post summary in payables channel for Priya + AP with per-vendor read and owning side | OE18 | 0, 1, 2, 3 |
| Drop comment on open AP-routing orphan-approver ticket with procurement-side evidence | OE19 | 4, 5, 6 |
| Email Daniel with Steven cc on vendors needing partner sign-off for release | OE20 | 7, 8, 9 |
| Reminder to re-check in seven days | OE21 | 10 |
| Not approving or routing; Priya, Daniel, Steven own that call | OE22 | 24 |
| (Systemic data signal) approver null on 320/320 pending | OE6 | 5; reinforced in 22 |
| Final synthesis to Lena (worst offenders, per-vendor cause + owner, scope result + access constraint, routing signal, deferral) | OE22 | 11-24 |

## No gaps

Every explicit prompt ask maps to >=1 rubric. The four write actions (Slack/Linear/email/reminder) each have a 1.1 plus content 1.2 rubrics. Every final-response fact the prompt asks Lena to be told has a 2.1.

## No surplus

Every rubric traces to a prompt ask in the table above. No rubric tests a fact the prompt did not request.

## Deliberately uncovered (correct, not gaps)

- **"missing change order" and "out-of-scope line" root-cause categories:** the prompt lists six possible classifications, but no ground-truth worst-offender exhibits these two. They are options in a diagnostic menu, not mandated findings. Writing rubrics for them would test facts that do not exist in the universe. (Confirmed by Council B reverse-coverage.)
- **Owning side for the vendor-dispute category (Pinecrest, rubric 17):** the prompt assigns owners to only five of the six categories; "active vendor dispute" is unassigned. Rubric 17 deliberately does not pin Pinecrest to procurement or AP. (S2 adversarial guard.)
- **External-vendor backlog count:** no rubric hard-fails on an exact count. Rubric 23 tests recognition of the 210000-vs-219000 account split (the scoping lens); an agent that surfaces 219000 miscoding or reports a broader count still passes. (S2 adversarial guard — ~30 vendors appear on both accounts; GraniteRack VEN-012-753165 is itself on 219000.)

## Hardness lever -> rubric coverage (B4 cross-check)

| Lever | Rubric(s) that depend on traversing it |
|---|---|
| L1 Latching (compound vs top-dollar + Daniel "already fixed" dismissal) | 11, 12, 13, 14 (compound lens); 22 + 6 (authority dismissal reconciliation) |
| L2 Structured-DB scope skip (2 entities x mixed doc kinds) | 19, 20 |
| L7 Multi-write diversification (4 writes across 4 services) | 0, 4, 7, 10 (+ content rubrics 1-3, 5-6, 8-9) |
| L8 Multi-link chain (SAP -> Linear -> email per vendor) | 15, 16, 17 (root-cause classification requires the chain) |
| L9 Universe-grounded gotcha (restricted docs, 210000/219000, null approver) | 21 (restricted), 23 (account split), 5 + 22 (null-approver signal) |

## Status

- Validator: PASS (0 fails, 0 warns; outcome=25, process=0).
- Council A (Grounding + Convention): GO.
- Council B (Adversarial QC + Density + Hardness, ultrabrain): GO — every QC sub-dim 5, projected density ~46-48 (>= 40), all five levers tied to outcome rubrics, both S2 guards honored.
- Next: `PIPELINE FINAL — Tasks/24_6a36e84723508b4e3f391cfc` (mandatory cross-artifact holistic council before platform upload).
