# Verification — HARDNESS phase (Task 33)

## Data sources consulted

- `_aux/Universe_Split/mortgage_los.loans.json` :: LN-2026-00211 status=withdrawn (2026-03-28); LN-2026-00622 assigned to todd.jennings (los_staff_0375f7c91014); LN-2026-00009 + LN-2026-00184 status check
- `_aux/Universe_Split/mortgage_los.conditions.json` :: 32 rows total; LN-2026-00009 has 3 outstanding (los_cond_74d7f24385f5, los_cond_739ecac87a02, los_cond_d7fdad61f9fa) issued 2026-02-27 to 2026-03-03, cleared_date=None; LN-2026-00184 has 0 conditions
- `_aux/Universe_Split/mortgage_los.staff.json` :: Grace Yamamoto present (Director of Operations); Robert NOT present (fabrication-risk — do not use); Marcus Webb present but DEPARTED
- `_aux/Universe_Split/slack.slack_messages.json` :: 573 total; C002=334 (58%); D_grace_robert=21 msgs; 10 msgs on LN-2026-00211 across C002+C005+D_denise_grace
- `_aux/Universe_Split/email.emails.json` :: 7287 total; 6 emails on LN-2026-00211
- `_aux/Universe_Split/crm.crm_engagements.json` :: 472 rows; engagement_type=NOTE pattern at crm_engagement_fc92d4a91195
- `_aux/Universe_Split/crm.crm_deals.json` :: 80 rows (deal anchor for L25 stale CRM engagement)
- `_aux/Universe_Split/stripe.charges.json` :: 1730 rows with amount_refunded field (L11 partial feasibility)
- `_aux/Fact_Ledger.json` :: atom-level cross-check (emails, IDs, dates)
- `_aux/Universe_Index/key_facts.md` :: Slack channel breakdown + email totals
- `_aux/Universe_Index/graph_report.md` :: person-by-mention density (Carlos 193 mentions; Grace + Sofia as top authority candidates)

## Reference docs consulted

- `Reference/Hardness_Playbook.md` :: 11-lever catalog with per-lever cost ranges; design target 50+ midpoint
- `Tasks/_meta/Learnings.md` :: L9 authority dismissal (~100% effective), L10 SAP-skip translated to `mortgage_los.conditions`, L13 first-framing trap, L25 existing-output anchor (highest-yield novel stump), L26 decoy parent thread
- `Reference/Sessions/HARDNESS.md` :: phase runbook (this run)
- `AGENTS.md` :: PIPELINE HARD RULES + keystone universe constants (TRID timing, status enums, Marcus Webb departed, NO Records Vault / Linear / Airtable / SAP / BlackLine)

## Eval spec sub-dims relevant to this phase

- Trajectory dim Tool Call Count (≥ 15 floor; pipeline targets 50+ midpoint) :: projected midpoint **50.5** → PASS
- Trajectory Service Breadth :: 7 distinct services, dominant 32% → PASS

## QC spec sub-dims relevant to this phase

- Trajectory T1 Tool Call Count :: projected midpoint **50.5**, band PASS

## Verification statements

- [x] At least 3 levers selected; each cites a Learnings.md entry. (L10 + L2 + L9 + L8 + L25 — five selected; each cites L<n>.)
- [x] Density midpoint projection is one of {PASS ≥ 50, THIN 40-49, INSUFFICIENT < 40}. **PASS at 50.5.**
- [x] Service breadth table populated (v11 G1). **7 distinct services, breadth PASS.**

## Discrepancies surfaced (if any)

- **Robert is named in PersonaBrief (scenario_d8b2b048) as reviewing Carlos's pipeline alongside Grace, but Robert is NOT present in `mortgage_los.staff.json`.** This is a fabrication risk for S1. Hardness_Plan.md explicitly forbids using Robert as the sender of any authority message; Grace is the sole authority voice. The PersonaBrief mention of Robert is treated as background flavor only — not a citeable artifact.
- **LN-2026-00622 is assigned to todd.jennings (los_staff_0375f7c91014), not Carlos**, even though PersonaBrief frames it as Carlos's pipeline. This becomes Stump Hypothesis #4 (L6 first-framing trap on assignment).
- **LN-2026-00184 has 0 conditions / 0 doc-checklist rows** despite 9 Slack mentions and notes citing build delays. The absence itself is a hardness signal for L2 — but the lever load-bearing on LN-2026-00009's overdue conditions, not LN-2026-00184.
