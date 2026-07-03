# OE Solvability + Coverage — S2

## OE-to-prompt coverage map

| Prompt ask | OE(s) |
|---|---|
| Denise pinged again this morning about the ransomware piece; put a stake in the ground this week | overall trajectory context (drives OE 15 + OE 16 reconciliation) |
| Close the pay-vs-restore call | OE 2, OE 3, OE 8, OE 16 |
| Walk Raj's picture back to what emails / records actually say | OE 2, OE 8, OE 16 |
| Specific gaps and rebuild items as tradeoffs, not foregone conclusion | OE 16, OE 22 (a), OE 23 (i) |
| Confirm nothing has shifted on legal side since 3/20 counsel ask (sanctions + privilege) | OE 3, OE 5, OE 22 (c) |
| Plain read of Denise's preliminary borrower-notice plan | OE 4, OE 11 |
| Has scope narrowed | OE 15 |
| Specific files identified since | OE 12, OE 13, OE 14, OE 15 |
| Anything queued not looped on | OE 13, OE 14 |
| Do NOT take March framing at face value | OE 15, OE 16, OE 23 (i) + (ii) |
| Anything feeding same borrower notice counts, even from separate workstream | OE 12, OE 13, OE 14, OE 15 |
| Find freshest signals and reconcile them, wherever they live | OE 15 |
| Decision brief: tradeoffs on payment call | OE 21 + OE 22 (a) |
| Decision brief: current borrower-notice posture with any specific files | OE 21 + OE 22 (b) |
| Decision brief: anything counsel still needs before decide | OE 21 + OE 22 (c) |
| Email outside cyber counsel with reconciled picture + request their view | OE 1, OE 18 |
| Post short status in leadership channel, not wider than needed | OE 6, OE 19, OE 25 |
| Formal note on incident record in engagement log | OE 20, OE 25 |
| Drop memo itself in incident folder alongside counsel correspondence | OE 21, OE 25 |
| If your read differs from the picture, say so plainly | OE 23 (i) + (ii) |

Every substantive prompt sentence has ≥1 OE covering it. No orphan asks (Council B-B8 forward-map: clean; AUDIT check 1: PASS).

## OE-to-rubric mapping preview (for S3)

**Outcome 1.1 write-action rubrics (4):**
| Rubric slot | OE source | Write tool |
|---|---|---|
| Send reconciled outreach to outside cyber counsel | OE 18 | send_email (or reply_to_email on email_email_b2572b3105dc) |
| Post leadership status | OE 19 | conversations_add_message on D_grace_robert_denise |
| Formal incident-record note | OE 20 | crm_create_engagement engagement_type=NOTE |
| Decision memo in incident folder | OE 21 | filesystem_write_file (+ filesystem_create_directory optional) |

**Outcome 1.2 content rubrics (candidates):**
| Rubric slot | OE source |
|---|---|
| Counsel email body: reconciled 3-workstream borrower-notice posture + restore tradeoffs + sanctions/privilege request | OE 18 + OE 22 |
| Slack status body: not-wider-than-needed distribution + reconciled position | OE 19 + OE 25 |
| CRM note body: paper-trail reconciliation across all 4 streams | OE 20 + OE 26 |
| Filesystem memo body: 3-section decision brief matching counsel email | OE 21 + OE 22 + OE 26 |

**Outcome 2.1 fact rubrics (candidates):**
- Payment call is NOT authorized at this moment; restore path is a lift but not foreclosed (OE 16 + OE 22 (a))
- 7 specific files identified across feeding streams: LN-2026-00522, LN-2026-00008, LN-2026-00010, LN-2026-00009, LN-2025-00002, LN-2025-00007, LN-2025-00229 (OE 12 + OE 14 + OE 15)
- Ransomware-attributable file exposure remains preliminary / unconfirmed (OE 15 + OE 23 (ii))

**Pure discovery OEs (no rubric target):**
- OE 1, OE 2, OE 3, OE 4, OE 5, OE 6, OE 7, OE 8, OE 9, OE 11, OE 12, OE 13, OE 14, OE 17

**Verification / cross-cutting OEs (become Process only if 3-condition test passes; default zero process):**
- OE 15, OE 16, OE 22, OE 23, OE 24, OE 25, OE 26, OE 27 (verification steps, likely folded into 1.1 / 1.2 / 2.1 rubrics rather than getting their own process rubric)

Council B-B9 flagged OE 10 + OE 17 as WEAK scope-creep (ambient at-risk-closings reads). These are propagated as SOFT-OUTCOME guidance for S3 — do NOT create separate rubrics for the at-risk-closings ambient layer.

## AUDIT verdict

**PASS (STRICT)** — all 11 checks pass under strictest read. Written to `_aux/Council_Reports/AUDIT_oe.md`. No REVISE. No REBUILD. No PROPAGATE TO S1.

## 7 propagate flags to S3

1. OE 10 + OE 17 SOFT-OUTCOME (ambient at-risk-closings, do NOT rubric-require)
2. Supersession anchor = 4/07 wholesale lender portal breach stream (not 4/14 Marcus Webb post-term stream)
3. Tight-distribution write posture is a HARD requirement (channel_id=D_grace_robert_denise, counsel email to Sloane only, memo in incident folder, CRM engagement NOTE)
4. Sloane no-reply is a truthful universe gap — do NOT rubric-require finding a Sloane response
5. 7 specific files across 3 feeding workstreams is the load-bearing content requirement
6. Ransomware-attributable file exposure REMAINS preliminary — must NOT be conflated with the 4/07 portal-breach identifiers
7. Bennett-cyber near-miss (`lbennett@bennettcyberlaw.com`) is a live L4 trap — counsel-routing rubric MUST anchor on `megan.sloane@wardbarrettlaw.com`
