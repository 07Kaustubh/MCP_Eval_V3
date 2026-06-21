# Prompt Design Verdict — S1

Task: `24_6a36e84723508b4e3f391cfc` (REDO rebuild — prior FAIL on DENSITY at 32.5 avg).
Universe today: 2026-06-12 (US/Eastern).
Word count: 478 / 500.
Validator: PASS (0 fails, 0 warns, 1 note).

## Levers engineered into the prompt

| # | Lever | Engineered as |
|---|---|---|
| L1 | Latching (authority-figure dismissal + dollar-bias counter-anchor) | Persona references Daniel's earlier note that the routing rule was "patched last sprint" but flags that recent invoices still call into question whether the backlog cleared. Compound rank (age × outstanding $) explicitly displaces top-dollar framing. |
| L2 | Structured-DB skip (RV scope on 2 entities × 3 doc kinds) | "Check the vault for the executed engagement record. For Acme, the original engagement evolved through an addendum and at least one change order, so we have multiple documents to check, not a single letter. For Northstar the engagement letter itself should be cleaner." Plus the restricted/access-grant carve-out. |
| L7 | Multi-write diversification (4 writes / 4 services) | Vendor-by-vendor summary in the payables channel · comment on the open AP-routing orphan-approver ticket · email draft to Daniel cc Steven for partner sign-off · 7-day re-sweep reminder. |
| L8 | Multi-link chain (per-vendor SAP → Linear → email) | "I don't want the queue status alone... Cross-check what any open AP exception ticket says on the issues side, and look for an active partner sign-off thread or a void-and-rebill request sitting in email from Owen or Daniel." Three root-cause classes (orphan / disputed / missing-credit-memo) force the chain per vendor. |
| L9 | Universe-grounded gotcha (restricted class + access grants + 210000 vs 219000) | "If a record is marked restricted and you can't get to it without an access grant, say so plainly, don't report it as missing." · "Stay on the external-vendor side of the ledger, not the employee-reimbursement side, since those run through a different account family." |

## Expected stump targets

1. **Root-cause miscategorization on 2 of 3 top vendors** (HIGH). Agent reads SAP status and stops, never cross-references Linear (`issue_e5abbb9af74642eeb10a93426b0bbaa2` says GraniteRack needs void-and-rebill; `issue_e6fbc488077344c28cc7cd13640c54bc` says TimeLedger is awaiting partner sign-off; BeaconPay VEN-033 has no Linear issue, indicating a true orphan).
2. **Acme scope reported as "not found"** (HIGH). Agent searches for `kind = engagement_letter` on `entity_id = acme_cloud`, finds 0, fails to pivot to `engagement_letter_addendum` + `engagement_change_order` despite explicit prompt framing. Atom-grounded inversion of the prior R4 trap.
3. **Daniel-Jones authority dismissal** (MED-HIGH). Agent reads the planted "patched last sprint" Slack thread reply and defers, missing that invoices dated after the supposed fix still carry `approver = null`. Highest-yield Opus 4.8 stumping mechanism on Brookfield tasks.
4. **Age-vs-dollars trade-off vendor missed** (MED). BeaconPay VEN-033 ($109K / 320 days) is the dollar-bias latch escape. The new compound-rank framing reduces the gap but the latch is sticky.

## Council verdicts

- **Council A (Grounding + Convention):** GO. 15/16 substantive claims grounded to live atoms; 1 NOTE on the Daniel-Jones dismissal phrasing (precedent already exists in C010 from persona_002 on 2026-05-19; S2 plants the exact thread-reply formulation per the Hardness Plan). Convention sweep clean on all Major fields.
- **Council B (Adversarial QC + Density + Hardness):** GO. 11/12 QC sub-dims at 5; Strict-language at 4 with explicit justification ("at least two or three" is conversational vendor count, "at least one change order" is universe-grounded floor, neither violates the rubric-title linter rule). Zero adversarial divergence across 4 second-readings. Density midpoint 44 (+4 above 40 floor). All 5 Hardness levers naturally surfaced. Zero phrasing hits.

## Watch-outs flagged for downstream

- **S2 (OE):** must pressure per-vendor 3-link drill (SAP + Linear + email) and 4 distinct writes; this is what closes the low-end 35-call density gap.
- **S3 (Rubrics):** prefer exact-anchor formulations ("references the change order doc") over count-based ("at least 1 change order doc"), even though the prompt mandate would backstop the latter.
- **S3 (Rubrics):** for the Daniel-Jones dismissal lever, grade the reconciliation conclusion (post-fix-date invoices still carry null approver) rather than the act of reading the thread reply.

## Density delta vs prior candidate

| Metric | Prior | Rebuilt midpoint |
|---|---:|---:|
| Tool calls (avg of 6 runs) | 32.5 | 44 projected |
| Write surfaces | 1 (Slack only) | 4 (Slack + Linear + email + reminder) |
| Scope-verification entities × doc kinds | 1 × 1 (impossible atom) | 2 × 3 (live atoms) |
| Per-vendor root-cause chains | 0 explicit | 3 to 5 mandated |

Verdict: SHIP. Proceed to S2.
