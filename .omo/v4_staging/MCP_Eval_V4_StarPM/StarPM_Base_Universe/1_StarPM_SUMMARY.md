# Star Property Management — Universe Summary

The 30,000-foot view of the Star PM universe. Read this first before any of the other docs.

---

## What Star PM is

Star Property Management is a **residential property manager** in the Southwest Texas region. It runs approximately 10 multifamily / apartment properties on behalf of individual owners — Star PM doesn't own the buildings, it operates them. The firm covers operating budgets, leasing and applicant intake, make-ready turnovers, maintenance across HVAC / plumbing / carpet / exterior work, rent collection and eviction, fair housing accommodations, and owner reporting. A ~45-person onsite team is supervised centrally by a small portfolio-operations tier.

### The company, at a glance

| | |
|---|---|
| Business | Residential property management (multifamily apartments) |
| Region | Southwest Texas, timezone America/Chicago |
| Email domain | `starpm.com` |
| Portfolio | ~10 properties, ~45 onsite staff |
| Structure | Property-tier PMs → Portfolio-tier Supervisor (Brooke Phillips) → Executive tier (Aurora Winona, President) |

### The universe, at a glance

| | |
|---|---|
| "Today" (agent-prompt anchor) | **2026-07-01**, America/Chicago |
| Active workflow window | 2026-05-01 → 2026-07-01 (2-month operational window) |
| Personas (authoring seats) | **13** |
| NPCs | **47** |
| Scripted scenarios | **27** |
| Services | **8** — Airtable · Contacts · Google Calendar · Gmail · HubSpot · Linear · QuickBooks · Slack |
| Business Functions (task categories) | **5** |

---

## The systems Star PM runs on

### Heavy-lift systems (primary system of record for their domain)

| Service | Primary role | Notes |
|---|---|---|
| **QuickBooks** | Accounting system of record | Vendor bills, tenant rent invoices, owner distributions, budget vs actual. The heaviest single service in the universe. |
| **Airtable** | Workflow tracking | Two tables — `Make-Ready Turns` (unit turnover state) and `Maintenance Tickets` (property-visible ticket tracking) |
| **HubSpot** | Leasing CRM | Applicants and tenants as contacts, deals for each leasing lifecycle stage, associations to owner-LLC companies |
| **Linear** | Maintenance ticket system | Three projects: Property Ops, Summer Make-Ready Program, Preventive Maintenance Push |

### Coordination layer

| Service | Primary role |
|---|---|
| **Slack** | Internal team coordination — 8 channels aligned to workflows |
| **Gmail** | External correspondence (tenants, owners, vendors, applicants) and internal handoffs |
| **Google Calendar** | Tour scheduling, PM cycles, owner meetings, court dates, ops sync |
| **Contacts** | Directory (personas + NPCs, ~60 entries) |

**No filesystem MCP service.** Documents that would live on a filesystem (application docs, inspection reports, screening reports) flow through Gmail attachments, HubSpot notes, or Airtable record fields instead. The `Data/Files/` folder contains read-only reference PDFs (contracts, invoices, reports) the agent can read directly — these are universe data, not an editable filesystem.

### Slack channel map

| ID | Name | Home business function |
|---|---|---|
| C001 | #maintenance | Cat 4 Maintenance & Repairs |
| C002 | #leasing | Cat 5 Leasing & Applicant Intake |
| C003 | #general | Cross-cutting |
| C004 | #make-ready | Cat 1 (turnover coordination) + Cat 3 (QC) |
| C005 | #vendors | Cat 2 (invoice approval) + Cat 4 (dispatch) |
| C006 | #owner-relations | Cat 2 Portfolio Coordination |
| C007 | #budget-review | Cat 2 Portfolio Coordination |
| C008 | #applications | Cat 5 Leasing |

---

## The portfolio

Five properties are meaningfully populated at the unit level in Airtable and QuickBooks. All are multifamily apartments in Southwest Texas.

| Property | Airtable references | Notes |
|---|---:|---|
| Las Palmas | 87 | Highest-density property in the data; Unit 8D anchors `makeready_laspalmas8d_turn` |
| Las Vistas | 40 | Unit 9D anchors `makeready_turn_lasvistas_9d` |
| Mesa Vista | 16 | Unit 4C anchors `makeready_turn_carlos` |
| Rio Bend | 14 | Anchors the carpet and water-heater escalation scenarios |
| Ridgeview | 2 | Only appears in the CapEx roof scenario (`owner_capex_approval_roof`) |

---

## The owners

Six property-owner NPCs are on file. Each owns one or more properties in the portfolio.

| Owner | NPC role | Owns / touches |
|---|---|---|
| David Shea | Property Owner | Named in mid-year portfolio reviews |
| Robert Finley | Property Owner | Ridgeview (CapEx roof), Mesa Vista (monthly reports) |
| Linda Castillo | Property Owner | Rio Bend (carpet, water-heater escalations) |
| Harry Harris | Property Owner | Tanya Mitchell's unit (eviction workflow) |
| Gary Hoffman | Owner & Lead Landscaper | Unusual: also the landscape vendor billing common-area service |
| Dave Thomas | Owner | External owner reference |

---

## The vendor bench (QuickBooks)

| Vendor | Type |
|---|---|
| Alamo HVAC Services | HVAC service and repairs |
| Hill Country Plumbing | Plumbing service and repairs |
| Lone Star Electric | Electrical service |
| Big Bend Restoration | Structural / restoration |
| Permian Make-Ready Crew | Make-ready labor |
| Lone Star Maintenance Supply | Parts and supplies |
| A Plus Carpet Cleaning & Repairs | Carpet cleaning, repair, replacement (Victor Rios is their lead technician) |
| Sunshine Cleaning | Move-out and turnover cleaning |

---

## The cast

### 13 authoring personas

Every task is voiced from one of these 13 personas. Their home Business Function is their authoring lane.

| Business Function | Personas |
|---|---|
| **1 · Property Operations** | Lisa Smith · Carlos Mendez · Patricia Nguyen · Denise Morales (all Onsite Property Manager) |
| **2 · Portfolio Coord & Owner Relations** | Brooke Phillips (Apartment Property Supervisor) · Teresa Wood (Executive Secretary) |
| **3 · QC & Field Services** | Jaime Salinas (QC Inspector) · Randy Jones (Appliance & Bulk-Item Retrieval Specialist) |
| **4 · Maintenance & Repairs** | John Smith · Elias Navarro (Lead Maintenance Technicians) · James Bennett (Assistant Maintenance Technician) |
| **5 · Leasing & Applicant Intake** | Sandra Allen · Kevin Okafor (Leasing Agents) |

### 47 NPCs

NPCs are never authoring seats — they only appear inside scenarios as tenants, applicants, owners, vendors, or specialty roles. Some NPCs carry scripted actions inside scenarios (most notably Alicia Vega leads the standard renewal-offer scenario; Tony Reyes and Wesley Tran carry maintenance-tier work; Isela Juarez appears across many make-ready scenarios).

Notable NPCs by category:

- **Executive tier**: Aurora Winona (President)
- **Property owners**: David Shea, Robert Finley, Linda Castillo, Harry Harris, Gary Hoffman, Dave Thomas
- **Tenants**: Tommy Reyes, Tanya Mitchell, Connor Beaumont
- **Rental applicants** (~12): Priya Nambiar, Marcus Delgado, Angela Carter, Tobias Wren, Yuki Tanaka, Simone Okafor, Derek Hutchinson, and others
- **Referral partners / apartment locators** (~10): Necia Perales (Apartment Locator Central), Tasha Wentworth, Jerome Okafor, Craig Pemberton, Lindsey Carmichael, and others
- **Star PM staff NPCs**: Alicia Vega (Leasing Agent), Maria Lopez (Weekend Leasing Agent), Tony Reyes (Lead Maintenance NPC), Wesley Tran (Assistant Maintenance NPC), Isela Juarez / Rosa Cantu (Part-Time Housekeepers)
- **External specialty**: Barry Sanderson (Code Compliance Inspector), Marcus Williams (Fire Extinguisher Service Tech), Ruben Barr (Pest Control), Pete Donovan (Exterior Painter), Victor Rios (A Plus Carpet lead technician), Diane Flores (Account Rep at Lone Star Maintenance Supply), Carmen Delgado (Sunshine Cleaning Operations Coordinator), Patricia Lowe (Justice-of-the-Peace Court Clerk)

Full per-persona detail: **02 · Persona Briefs**. Full per-scenario detail: **04 · Scenario Storylines**.

---

## The scripted scenarios

27 scenarios cover the full breadth of Star PM's operational surface. See **04 · Scenario Storylines** for per-scenario detail.

### Scenarios by primary business function

Each scenario is grouped under the Business Function of its **primary actor** (the persona or NPC with the most scripted actions in that scenario).

**Cat 1 · Property Operations** (10 primary scenarios):
- Make-ready turnovers: `makeready_turn_carlos`, `makeready_laspalmas8d_turn` (Carlos leads both)
- Maintenance response: `maint_esc_carpet_repair_riobend`, `maintenance_escalation_waterheater_leak` (Carlos leads both)
- Fair housing: `fair_housing_reasonable_accommodation` (Lisa leads)
- Rent lifecycle: `rent_late_first_notice`, `rent_delinquency_payment_plan`, `rent_3day_notice_pay_or_quit` (Patricia leads all)
- Eviction lifecycle: `eviction_filing_prep`, `eviction_court_coordination` (Patricia leads both)

**Cat 2 · Portfolio Coord & Owner Relations** (10 primary scenarios):
- Cross-portfolio sync: `property_ops_weekly_cycle`, `summer_makeready_weekly_cycle`, `portfolio_ops_preventive_maintenance_push`, `preventive_maintenance_push_routine`
- Vendor invoice & budget: `vendor_invoice_aplus_carpet_repair` (collaborative), `vendor_invoice_landscape_may2026` (Teresa leads), `budget_review_makeready_q2`
- Owner reporting & CapEx: `owner_monthly_report_review`, `owner_portfolio_review_midyear`, `owner_capex_approval_roof`

**Cat 3 · QC & Field Services** (0 primary — Jaime participates broadly across Cat 1/2/4 make-ready and PM scenarios as the QC anchor)

**Cat 4 · Maintenance & Repairs** (2 primary scenarios):
- `maintenance_hvac_elias` (Elias Navarro leads the summer HVAC preventive push)
- `makeready_turn_lasvistas_9d` (John Smith leads the maintenance side of this turn)

**Cat 5 · Leasing & Applicant Intake** (5 primary scenarios):
- Intake: `lease_inquiry_delgado_referral`, `rental_app_priya_nambiar`, `leasing_application_to_movein` (Sandra leads all three)
- Renewals: `lease_renewal_offer_standard` (Alicia Vega NPC-led), `lease_renewal_declined_to_moveout` (Kevin Okafor)

Total: 10 + 10 + 0 + 2 + 5 = 27

---

## What carries over from prior universes

The Star PM universe uses the same project framework as Brookfield, Keystone, and MoveOps:

- **Rubrics V3 conventions**: Two categories only — Outcome (mandatory, three sub-types: 1.1 write-action results, 1.2 action content, 2.1 key facts) and Process (optional, only when a necessary behavior can't be captured by a stronger Outcome).
- **Phrasing**: Every rubric reads as a behavior of *the Agent* — no passive constructions.
- **No tool names in prompts or rubrics.** Tool identifiers like `airtable_mock_update_record` belong in author guidance, not in prompt bodies.
- **Prompt style**: Natural language, no pre-solving, no checklist tone, no `"I'm X, my role is Y…"` opener. Prompts read like a real internal message from a colleague.
- **Same spec-quality dimensions**: unique ground truth, feasibility, cross-service requirement, coherence, persona match, business function, universe feasibility, OE completeness/accuracy, rubric quality thresholds, category balance, failure rate.
- **Same three fields per rubric**: criterion + justification + evidence.

---

## What's distinctive about Star PM

- **A broader lifecycle than pure ops.** Beyond make-ready and maintenance, the universe carries a full rent-to-eviction lifecycle, a leasing lifecycle from inquiry through renewal-or-move-out, and CapEx approval flows with owners.
- **Persona footprint varies widely.** Brooke Phillips is in 26 of 27 scenarios (deeply rooted); Randy Jones, Denise Morales, and James Bennett are design-surface (thin scripted footprint — author from the shape of the role, not a scripted anchor).
- **Some NPCs carry scripted actions.** Alicia Vega, Tony Reyes, Wesley Tran, and Isela Juarez execute inside scenarios. Authoring stays persona-only, but tasks can hand off to or reconcile with NPC-driven work.
- **QuickBooks is unusually heavy.** The biggest single service surface — cash cycles, vendor bills, owner distributions, and tenant rent invoices dominate the operational data.
- **Texas-specific operational context.** HVAC failures in Southwest Texas summer are life-safety events; rent-notice timing runs on state-mandated windows; code compliance is enforced by external inspectors.
- **Tight cross-service threading.** Every artifact tends to matter — a make-ready task will realistically touch Airtable + Slack + Linear + Gmail + QuickBooks in one flow; a rent-collection task threads QuickBooks + Gmail + Airtable + Calendar.

---

## Doc set index

- **[00 · One-Pager](00_StarPM_One-Pager.html)** — Landing-page teaser
- **01 · Summary** — This document
- **[02 · Persona Briefs](02_StarPM_PERSONA%20BRIEFS.html)** — Per-persona detail for all 13
- **[03 · Task Categories](03_StarPM_TASK%20CATEGORIES.html)** — 5 business functions, 16 subcategories, 100-task distribution, worked example prompts
- **[04 · Scenario Storylines](04_StarPM_SCENARIO%20STORYLINES.html)** — Per-scenario detail for all 27
- **[05 · Artifacts](05_StarPM_ARTIFACTS.html)** — Systems catalog: tables, objects, artifact shapes
- **[06 · Glossary](06_StarPM_GLOSSARY.html)** — Terms specific to Star PM and the framework
