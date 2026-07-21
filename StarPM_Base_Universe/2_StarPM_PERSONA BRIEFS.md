# Star Property Management — Persona Briefs

Per-persona detail for the 13 authoring personas in Star PM. Each brief covers role, home Business Function, systems they touch most, communication style, scripted footprint, and the scenarios they lead.

> **Reading these briefs.** The "signature scenarios" are where the persona is the primary actor (leads by scripted-action count). "Also present" scenarios are where they participate but aren't the lead. Personas with 0 or 1 scripted actions are called out as **design-surface** — author tasks from the shape of the role, not from a scripted anchor.

---

# Cat 1 — Property Operations Personas

Four Onsite Property Manager personas. Each is responsible for their own property; their work overlaps in the make-ready surge and cross-property coordination.

## Lisa Smith · Onsite Property Manager

| | |
|---|---|
| Business Function | 1 · Property Operations |
| Persona id | `p_002` · email `lisa.smith@starpm.com` |
| Seniority | Mid · Department: Property Operations |
| Communication | Formality 0.60 · verbosity 0.55 · response time fast · active hours 7 AM–5 PM |
| Personality | Responsible · thorough · calm |
| Scripted footprint | **20 actions across 11 scenarios** — deeply rooted |

**What she owns.** Lisa is the Onsite PM anchoring turnovers, tenant coordination, and property-level operations at her property. She leads the anchored **fair housing accommodation** scenario and drives one make-ready end-to-end. She's the connective tissue between maintenance (John / Elias), leasing (Sandra / Kevin), and the portfolio-level supervisor (Brooke).

**Systems she touches most.** Airtable (Make-Ready Turns), Slack `#make-ready`, `#maintenance`, Gmail (tenant threads), Google Calendar, Linear (tickets she opens or triages).

**Signature scenarios.**
- `fair_housing_reasonable_accommodation` — 6 actions (leads)
- `makeready_turn_lasvistas_9d` — participates heavily on the property side (2 actions)
- `owner_capex_approval_roof` — 2 actions (submits the originating maintenance ticket)
- `owner_monthly_report_review` — submits property-level data to Brooke

**Voice.** Warm-professional, thorough, calm. She keeps tenants informed and always confirms before escalating.

---

## Carlos Mendez · Onsite Property Manager

| | |
|---|---|
| Business Function | 1 · Property Operations |
| Persona id | `p_009` · email `carlos.mendez@starpm.com` |
| Seniority | Mid · Department: Property Operations |
| Communication | Formality 0.55 · verbosity 0.50 · response time fast · active hours 7 AM–5 PM |
| Personality | Organized · steady · communicative |
| Scripted footprint | **33 actions across 11 scenarios** — most-rooted Onsite PM after Brooke |

**What he owns.** Carlos anchors Mesa Vista and Las Palmas activity. He drives the two Cat 1 make-ready scenarios and the two Cat 1 maintenance-response scenarios (carpet, water-heater) that thread through onsite operations.

**Systems he touches most.** Airtable, Slack `#make-ready` and `#maintenance`, Gmail (tenants + vendors), Linear.

**Signature scenarios.**
- `makeready_turn_carlos` (Mesa Vista 4C) — 9 actions (leads)
- `maint_esc_carpet_repair_riobend` — 6 actions (leads, threads through A Plus Carpet Cleaning & Repairs)
- `maintenance_escalation_waterheater_leak` — 6 actions (leads, threads through Hill Country Plumbing)
- `makeready_laspalmas8d_turn` — 4 actions (leads)
- `vendor_invoice_aplus_carpet_repair` — 2 actions (participates in the field-repair side)

**Voice.** Steady, professional. Communicates in structured updates. Coordinates well across vendor threads.

---

## Patricia Nguyen · Onsite Property Manager

| | |
|---|---|
| Business Function | 1 · Property Operations |
| Persona id | `p_010` · email `patricia.nguyen@starpm.com` |
| Seniority | Mid · Department: Property Operations |
| Communication | Formality 0.60 · verbosity 0.50 · response time medium · active hours 8 AM–5 PM |
| Personality | Detail-oriented · firm · approachable |
| Scripted footprint | **26 actions across 7 scenarios** — the rent/eviction anchor |

**What she owns.** Patricia is the anchor for the entire **rent collection and eviction lifecycle**. She leads all five anchored scenarios in that workflow — from first late notice through 3-day pay-or-quit through eviction filing and court coordination with Patricia Lowe (Court Clerk). She's methodical about documentation because every prior notice becomes part of the filing packet.

**Systems she touches most.** QuickBooks (rent invoices, delinquency ledger), Gmail (notices), Airtable (tenant records), Google Calendar (statutory deadlines, court dates), Slack `#general` and `#owner-relations` for escalations.

**Signature scenarios.**
- `rent_late_first_notice` — 5 actions (leads)
- `rent_delinquency_payment_plan` — 5 actions (leads)
- `rent_3day_notice_pay_or_quit` — 7 actions (leads)
- `eviction_filing_prep` — 4 actions (leads)
- `eviction_court_coordination` — 3 actions (leads, coordinates with Court Clerk Patricia Lowe)

**Voice.** Firm and factual on late-rent correspondence. Approachable in the payment-plan conversation. Always references the specific invoice and prior notice in her emails.

---

## Denise Morales · Onsite Property Manager

| | |
|---|---|
| Business Function | 1 · Property Operations |
| Persona id | `p_013` · email `denise.morales@starpm.com` |
| Seniority | Mid · Department: Property Operations |
| Communication | Formality 0.55 · verbosity 0.50 · response time fast · active hours 7 AM–4 PM |
| Personality | Warm · efficient · thorough |
| Scripted footprint | **1 action in 1 scenario** — **design-surface** |

**What she owns.** Denise is an Onsite PM at another property in the portfolio. She has thin scripted footprint but the role is real — her workflows mirror Lisa's, Carlos's, and Patricia's. Tasks written for Denise are author-from-spec, anchored on the shape of Onsite PM work rather than a scripted arc.

**Systems she touches most.** Airtable, Slack, Gmail, Google Calendar, Linear — same as the other Onsite PMs.

**Where she appears.** `lease_renewal_declined_to_moveout` (participates in the move-out coordination for Connor Beaumont — 1 action).

**Voice.** Warm and efficient. Same tone as Lisa but a touch more casual.

**Authoring guidance.** Because Denise has only one scripted action, most tasks written for her are author-from-spec property-level operations. Model her prompts after Lisa's or Carlos's rooted patterns but shift the property and unit numbers.

---

# Cat 2 — Portfolio Coord & Owner Relations Personas

Two personas: the portfolio Supervisor and her admin support.

## Brooke Phillips · Apartment Property Supervisor

| | |
|---|---|
| Business Function | 2 · Portfolio Coord & Owner Relations |
| Persona id | `p_000` · email `brooke.phillips@starpm.com` |
| Seniority | Senior · Department: Portfolio Operations |
| Communication | Formality 0.65 · verbosity 0.60 · response time fast · active hours 7 AM–5 PM |
| Personality | Organized · direct · coaching |
| Scripted footprint | **69 actions across 23 scenarios** — deepest in the universe |

**What she owns.** Brooke is the portfolio-level supervisor. She's present in 26 of 27 scenarios — often as the coordinator, approver, or escalation target. She owns cross-portfolio operations sync, vendor invoice approval, budget oversight, owner reporting, and the CapEx approval flow with owners.

**Systems she touches most.** QuickBooks (invoice approval, budget), Gmail (owner and vendor threads), Slack `#vendors`, `#owner-relations`, `#budget-review`, `#general`, Google Calendar (owner meetings, ops sync), Airtable (portfolio rollups).

**Signature scenarios.**
- `owner_capex_approval_roof` — 8 actions (leads)
- `owner_monthly_report_review` — 7 actions (leads)
- `property_ops_weekly_cycle`, `summer_makeready_weekly_cycle`, `portfolio_ops_preventive_maintenance_push` — 4-5 actions each (leads cross-portfolio sync)
- `budget_review_makeready_q2` — 4 actions (leads, reconciles Q2 make-ready spend variance)
- `owner_portfolio_review_midyear` — 4 actions (leads, coordinates with Aurora Winona)

**Voice.** Direct, organized, coaching. She writes concise Slack posts, structured owner memos, and short but pointed vendor emails. She's the escalation point when a workflow crosses spend or judgment thresholds.

---

## Teresa Wood · Executive Secretary

| | |
|---|---|
| Business Function | 2 · Portfolio Coord & Owner Relations |
| Persona id | `p_014` · email `teresa.wood@starpm.com` |
| Seniority | Mid · Department: Executive |
| Communication | Formality 0.75 · verbosity 0.45 · response time fast · active hours 8 AM–5 PM |
| Personality | Detail-oriented · reliable · professional |
| Scripted footprint | **24 actions across 14 scenarios** — deeply rooted admin support |

**What she owns.** Teresa is the Executive Secretary supporting Brooke and Aurora Winona. She leads the anchored **landscape-vendor-invoice** scenario end-to-end (Gary Hoffman's May service). Across most other Cat 2 scenarios she handles owner-side calendaring, packet assembly, and formatting — the admin infrastructure that scales Brooke's throughput.

**Systems she touches most.** Gmail (owner correspondence, vendor confirmations), Google Calendar (owner meetings, executive scheduling), QuickBooks (invoice packet assembly), Slack `#general`, `#owner-relations`, `#budget-review`.

**Signature scenarios.**
- `vendor_invoice_landscape_may2026` — 5 actions (leads, from vendor email through payment)
- `eviction_filing_prep`, `eviction_court_coordination`, `rent_late_first_notice`, `rent_3day_notice_pay_or_quit` — 1-2 actions each (packet assembly, calendaring)
- `owner_monthly_report_review`, `owner_portfolio_review_midyear` — packet formatting, calendar invites
- `budget_review_makeready_q2`, `portfolio_ops_preventive_maintenance_push` — admin infrastructure

**Voice.** Most formal in the universe (formality 0.75). Uses complete sentences, avoids emoji, keeps communications professional and precise. She sounds like the executive-office voice she is.

---

# Cat 3 — QC & Field Services Personas

Two cross-portfolio specialty roles. Both are thin on scripted footprint but essential to the operational reality.

## Jaime Salinas · Quality Control Inspector

| | |
|---|---|
| Business Function | 3 · Quality Control & Field Services |
| Persona id | `p_007` · email `jaime.salinas@starpm.com` |
| Seniority | Mid · Department: Portfolio Operations |
| Communication | Formality 0.55 · verbosity 0.30 · response time medium · active hours 8 AM–4 PM |
| Personality | Observant · unbothered · methodical |
| Scripted footprint | **7 actions across 7 scenarios** — participates broadly, leads none |

**What she owns.** Jaime is the impartial QC eye. She walks units after the maintenance team declares work complete, validates the punch-list, and either signs off on marketing-ready status or kicks work back. Her scripted footprint spans across make-ready scenarios but she's never the primary actor — she's the sign-off anchor.

**Systems she touches most.** Airtable (Make-Ready Turns QC status), Slack `#make-ready`, Linear (issues she opens on QC finds), Gmail (Onsite PM notifications).

**Where she appears.** `makeready_turn_carlos`, `makeready_laspalmas8d_turn`, `makeready_turn_lasvistas_9d`, `summer_makeready_weekly_cycle`, `portfolio_ops_preventive_maintenance_push`, `preventive_maintenance_push_routine`, `maintenance_hvac_elias` — always as the QC anchor.

**Voice.** Short, factual, observation-first. Verbosity 0.30 — she doesn't over-explain. Her Slack posts are one-liners with a status flip and a couple of specific observations. Zero emoji.

---

## Randy Jones · Appliance & Bulk-Item Retrieval Specialist

| | |
|---|---|
| Business Function | 3 · Quality Control & Field Services |
| Persona id | `p_008` · email `randy.jones@starpm.com` |
| Seniority | Junior · Department: Portfolio Operations |
| Communication | Formality 0.30 · verbosity 0.25 · response time medium · active hours 7 AM–3 PM |
| Personality | Practical · self-sufficient · mobile |
| Scripted footprint | **1 action in 1 scenario** — **design-surface** |

**What he owns.** Randy handles the field-level appliance and bulk-item work — pulls old appliances during move-out, delivers replacements during scope-set, hauls bulk waste and abandoned items. Cross-portfolio scope. Coordinates with Onsite PMs and the make-ready timeline.

**Systems he touches most.** Airtable (Make-Ready Turns record — pulls current scope), Slack `#make-ready` (status pings), Google Calendar (his own pickup schedule), Gmail (rare, disposal vendor coordination).

**Where he appears.** `makeready_turn_lasvistas_9d` (1 scripted action).

**Voice.** Short and practical. Least formal persona in the universe (formality 0.30). Uses short-form language, tells you where he's headed and when he'll be clear. Not much elaboration.

**Authoring guidance.** Because Randy has only one scripted action, tasks written for him are author-from-spec, anchored on the appliance-swap and bulk-pickup shape of his real-world role.

---

# Cat 4 — Maintenance & Repairs Personas

Three maintenance-tech personas. John and Elias are Lead Techs; James is the Assistant.

## John Smith · Lead Maintenance Technician

| | |
|---|---|
| Business Function | 4 · Maintenance & Repairs |
| Persona id | `p_004` · email `john.smith@starpm.com` |
| Seniority | Mid · Department: Maintenance |
| Communication | Formality 0.40 · verbosity 0.35 · response time fast · active hours 6 AM–4 PM |
| Personality | Proactive · skilled · proud |
| Scripted footprint | **13 actions across 7 scenarios** — the general-lead anchor |

**What he owns.** John is the general Lead Maintenance Technician — ticket triage, dispatch, diagnosis, and hands-on repair work across the portfolio. He leads the maintenance side of `makeready_turn_lasvistas_9d` and threads through most of the maintenance and preventive maintenance work.

**Systems he touches most.** Linear (primary ticket system), Slack `#maintenance`, Gmail (vendor threads), Google Calendar (dispatch scheduling), QuickBooks (work-order costing on escalations).

**Signature scenarios.**
- `makeready_turn_lasvistas_9d` — 5 actions (leads the maintenance side)
- `preventive_maintenance_push_routine`, `summer_makeready_weekly_cycle`, `portfolio_ops_preventive_maintenance_push` — participates on execution
- `maintenance_escalation_waterheater_leak` — 2 actions (participates as second-lead)
- `owner_capex_approval_roof` — provides the originating diagnostic

**Voice.** Direct, terse, hands-on. Least formal after Randy (formality 0.40). His Slack posts are dispatch decisions and diagnostic conclusions. He starts early — active from 6 AM.

---

## Elias Navarro · Lead Maintenance Technician

| | |
|---|---|
| Business Function | 4 · Maintenance & Repairs |
| Persona id | `p_012` · email `elias.navarro@starpm.com` |
| Seniority | Mid · Department: Maintenance |
| Communication | Formality 0.35 · verbosity 0.30 · response time fast · active hours 6 AM–3 PM |
| Personality | Hands-on · reliable · proactive |
| Scripted footprint | **10 actions across 3 scenarios** — HVAC anchor |

**What he owns.** Elias is the HVAC-heavy Lead — he leads the anchored summer HVAC preventive push scenario end-to-end (creates Linear issues under proj_003, coordinates the two-week rolling schedule, dispatches vendors, closes the tickets). He also participates in the preventive maintenance routine cycle and the makeready of Las Palmas 8D.

**Systems he touches most.** Linear (issue creation and comment threading — heavy user), Slack `#maintenance` and `#vendors`, Google Calendar (vendor visits).

**Signature scenarios.**
- `maintenance_hvac_elias` — 8 actions (leads the summer HVAC push)
- `preventive_maintenance_push_routine` — 1 action (participates)
- `summer_makeready_weekly_cycle` — 1 action (participates)

**Voice.** Similar to John's — terse, hands-on, proactive. Even less formal (0.35). His Linear comments carry the diagnostic detail; his Slack messages are short handoffs.

---

## James Bennett · Assistant Maintenance Technician

| | |
|---|---|
| Business Function | 4 · Maintenance & Repairs |
| Persona id | `p_006` · email `james.bennett@starpm.com` |
| Seniority | Junior · Department: Maintenance |
| Communication | Formality 0.35 · verbosity 0.30 · response time fast · active hours 6 AM–3 PM |
| Personality | Diligent · punctual · eager to learn |
| Scripted footprint | **0 scripted actions** (participant in `makeready_laspalmas8d_turn`) — **design-surface** |

**What he owns.** James is the Assistant Maintenance Technician. He executes tickets under John's or Elias's direction — routine repairs (garbage disposals, minor plumbing, small drywall), tenant-facing appointments, and second-hand support during turns. He has zero scripted actions in the current universe but participates as cast in `makeready_laspalmas8d_turn`.

**Systems he touches most.** Linear (ticket execution), Slack `#maintenance`, Google Calendar (dispatch appointments), occasional Gmail.

**Voice.** Diligent, punctual, junior-tier. Least formal (0.35). Short confirmations, quick status updates. Tone is closer to a technician on the ground than a Lead.

**Authoring guidance.** Because James is completely design-surface, tasks written for him are author-from-spec — model his prompts after the shape of Assistant Maintenance Tech work (executes assigned tickets, follows Lead's routing, reports back on completion) rather than any specific scripted arc.

---

# Cat 5 — Leasing & Applicant Intake Personas

Two Leasing Agent personas. Sandra anchors intake; Kevin anchors renewals.

## Sandra Allen · Leasing Agent

| | |
|---|---|
| Business Function | 5 · Leasing & Applicant Intake |
| Persona id | `p_003` · email `sandra.allen@starpm.com` |
| Seniority | Junior · Department: Property Operations |
| Communication | Formality 0.50 · verbosity 0.60 · response time fast · active hours 8 AM–5 PM |
| Personality | Cheerful · eager · professional |
| Scripted footprint | **20 actions across 4 scenarios** — intake anchor |

**What she owns.** Sandra is the intake Leasing Agent. She anchors the full applicant lifecycle from inbound inquiry through application processing, screening, and approval-to-lease-signing.

**Systems she touches most.** HubSpot (contacts, deals, notes — the CRM system of record for her workflow), Gmail (applicant threads, referral partner threads), Google Calendar (tour scheduling), Airtable (unit availability), Slack `#leasing` and `#applications`.

**Signature scenarios.**
- `lease_inquiry_delgado_referral` — 7 actions (leads, Marcus Delgado referred by Tasha Wentworth)
- `rental_app_priya_nambiar` — 7 actions (leads, Priya referred by Jerome Okafor via Apartment Locator Central)
- `leasing_application_to_movein` — 4 actions (leads, Angela Carter approval-to-move-in)
- `fair_housing_reasonable_accommodation` — 2 actions (participates on the leasing side of the unit swap)

**Voice.** Cheerful and eager (junior seniority, but professional). Formality 0.50 — friendly but polished. Uses light emoji (0.05 rate).

---

## Kevin Okafor · Leasing Agent

| | |
|---|---|
| Business Function | 5 · Leasing & Applicant Intake |
| Persona id | `p_011` · email `kevin.okafor@starpm.com` |
| Seniority | Junior · Department: Property Operations |
| Communication | Formality 0.45 · verbosity 0.55 · response time fast · active hours 8 AM–5 PM |
| Personality | Personable · motivated · energetic |
| Scripted footprint | **7 actions across 2 scenarios** — renewal anchor |

**What he owns.** Kevin is the renewal-heavy Leasing Agent. He leads the anchored non-renewal scenario (Connor Beaumont declines and moves out). He also supports intake — he's in the cast for Priya Nambiar's application.

**Systems he touches most.** HubSpot (renewal deal management), Gmail (tenant renewal correspondence), Airtable (tenant records, lease-end dates), Google Calendar, Slack `#leasing`.

**Signature scenarios.**
- `lease_renewal_declined_to_moveout` — 6 actions (leads, Connor Beaumont non-renewal at Mesa Vista)
- `rental_app_priya_nambiar` — 1 action (checks unit availability during Sandra's intake flow)

**Voice.** Personable and energetic. Formality 0.45 — slightly less formal than Sandra. Higher emoji rate (0.04) — reads younger and more casual than the senior tier.

---

## A note on scripted footprint

| Persona | Actions | Scenarios | Rooting tier |
|---|---:|---:|---|
| Brooke Phillips | 69 | 23 | Deep |
| Carlos Mendez | 33 | 11 | Deep |
| Patricia Nguyen | 26 | 7 | Deep |
| Teresa Wood | 24 | 14 | Deep |
| Lisa Smith | 20 | 11 | Deep |
| Sandra Allen | 20 | 4 | Deep |
| John Smith | 13 | 7 | Signature |
| Elias Navarro | 10 | 3 | Signature |
| Kevin Okafor | 7 | 2 | Signature |
| Jaime Salinas | 7 | 7 | Signature (broad, no lead) |
| Randy Jones | 1 | 1 | Design-surface |
| Denise Morales | 1 | 1 | Design-surface |
| James Bennett | 0 | 1 (cast only) | Design-surface |

**Design-surface personas** (Randy Jones, Denise Morales, James Bennett) don't have a scripted arc to author against. Tasks for them are written from the shape of their role — the workflows are real, the scripted anchor is thin.
