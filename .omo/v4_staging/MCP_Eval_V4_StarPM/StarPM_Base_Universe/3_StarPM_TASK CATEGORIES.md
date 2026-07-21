# Star Property Management — Task Categories

This document is the operating manual for task authoring at Star Property Management. It describes the **5 categories** of work the firm produces, the personas anchoring each, the subcategories inside them, and worked example prompts drawn from the universe's actual scenario set.

Star PM is a **residential property manager** in the Southwest Texas region handling a portfolio of ~10 properties on behalf of individual owners. The firm doesn't own the buildings — it runs them, covering operating budgets, leasing and applicant intake, make-ready turnovers, maintenance (HVAC, plumbing, carpet, exterior), rent collection and eviction, fair housing accommodations, and owner relations. A ~45-person onsite team is supervised centrally by a small portfolio-operations tier.

## How to use this guide

1. **Pick the acting persona** for your task from the persona → Business Function mapping below. Each persona lives in exactly one Business Function — that's their home lane.
2. **Open the matching category block**, read the scope, scan the subcategories, and read at least one worked example.
3. **Confirm anchors against the live universe.** Property IDs, unit numbers, vendor names, tenant names — everything in the examples is real, but always cross-check the live data before committing.
4. **Write the task prompt in the natural style** — as a real colleague handing off work. Make the task genuinely hard, not just long.

> **A note on the `*Prompt written by …*` lines below each worked example.** These are a documentation convention used *only inside this guide* to identify the protagonist persona behind the example. The persona never appears in the actual prompt — real prompts contain only the task itself, written in the protagonist's voice.

> **Star PM–specific note on NPCs.** A handful of NPCs (Alicia Vega, Tony Reyes, Wesley Tran, Isela Juarez) carry scripted actions inside some scenarios — most visibly, Alicia Vega leads the standard renewal-offer scenario. **Authoring seats are still persona-only** — tasks are voiced from the 13 personas — but authors should know some scripted flows thread through NPC-driven work that the persona's voice will oversee, coordinate, or hand off. Tenants (Tommy Reyes, Tanya Mitchell) and applicants (Priya Nambiar, Marcus Delgado, Angela Carter, Connor Beaumont, etc.) are NPCs — they are not authoring seats and never voice tasks.

## Universe constants

| | |
|---|---|
| Firm | Star Property Management — residential property manager, Southwest Texas region |
| "Today" (current date in agent prompts) | **2026-07-01**, America/Chicago |
| Time range (active workflow) | 2026-05-01 → 2026-07-01 (America/Chicago) |
| Email domain | `starpm.com` |
| Portfolio | ~10 properties (multifamily / apartments); Airtable + QuickBooks unit-level data anchors on **Las Palmas, Las Vistas, Mesa Vista, Rio Bend, Ridgeview** |
| Property owners | David Shea, Robert Finley, Linda Castillo, Harry Harris, Gary Hoffman, Dave Thomas |
| Systems of record | **QuickBooks** (accounting), **Airtable** (turnover + workflow tracking), **HubSpot** (leasing pipeline), **Linear** (maintenance tickets) |
| Coordination | Gmail · Slack · Google Calendar · Contacts |
| Universe totals | 27 scripted scenarios · 13 authoring personas + 47 NPCs · 8 services |

### Slack channels (8)

| Channel ID | Name | Primary category |
|------------|------|--------------------|
| C001 | #maintenance | Cat 4 Maintenance & Repairs |
| C002 | #leasing | Cat 5 Leasing & Applicant Intake |
| C003 | #general | Cross-cutting |
| C004 | #make-ready | Cat 1 (turnover coord) + Cat 3 (QC) |
| C005 | #vendors | Cat 2 (invoice approval) + Cat 4 (dispatch) |
| C006 | #owner-relations | Cat 2 Portfolio Coordination |
| C007 | #budget-review | Cat 2 Portfolio Coordination |
| C008 | #applications | Cat 5 Leasing |

### Vendors on file (QuickBooks)

| Vendor | Type |
|---|---|
| Alamo HVAC Services | HVAC service and repairs |
| Hill Country Plumbing | Plumbing service and repairs |
| Lone Star Electric | Electrical service |
| Big Bend Restoration | Structural / restoration |
| Permian Make-Ready Crew | Make-ready labor |
| Lone Star Maintenance Supply | Parts and supplies |
| A Plus Carpet Cleaning & Repairs | Carpet cleaning, repair, replacement |
| Sunshine Cleaning | Move-out and turnover cleaning |

---

## Persona → Business Function mapping

Each persona has exactly one Business Function. Personas may appear as participants inside scenarios owned by another Business Function (Brooke Phillips participates in almost every scenario, for example), but **tasks are always authored from a persona's home Business Function, not from participant appearances**.

| Persona | Title | Business Function |
|---|---|---|
| **Lisa Smith** | Onsite Property Manager | **1** Property Operations |
| **Carlos Mendez** | Onsite Property Manager | **1** Property Operations |
| **Patricia Nguyen** | Onsite Property Manager | **1** Property Operations |
| **Denise Morales** | Onsite Property Manager | **1** Property Operations |
| **Brooke Phillips** | Apartment Property Supervisor | **2** Portfolio Coordination & Owner Relations |
| **Teresa Wood** | Executive Secretary | **2** Portfolio Coordination & Owner Relations |
| **Jaime Salinas** | Quality Control Inspector | **3** Quality Control & Field Services |
| **Randy Jones** | Appliance & Bulk-Item Retrieval Specialist | **3** Quality Control & Field Services |
| **John Smith** | Lead Maintenance Technician | **4** Maintenance & Repairs |
| **Elias Navarro** | Lead Maintenance Technician | **4** Maintenance & Repairs |
| **James Bennett** | Assistant Maintenance Technician | **4** Maintenance & Repairs |
| **Sandra Allen** | Leasing Agent | **5** Leasing & Applicant Intake |
| **Kevin Okafor** | Leasing Agent | **5** Leasing & Applicant Intake |

**Note on scripted footprint.** Not every persona has an equal share of scripted actions.

- **Deeply rooted** (dozens of scripted actions across many scenarios): Brooke Phillips (69 actions), Carlos Mendez (33), Patricia Nguyen (26), Teresa Wood (24), Lisa Smith (20), Sandra Allen (20)
- **Rooted with a clear signature** (one or two lead scenarios): John Smith (13), Elias Navarro (10), Kevin Okafor (7), Jaime Salinas (7)
- **Design-surface** (thin scripted footprint — author from the shape of the role, not from a scripted anchor): Randy Jones (1), Denise Morales (1), James Bennett (0)

Author-from-spec is the norm for the design-surface personas. Their role in the universe is real, but the scripted anchor for their work is thin — task authors write from the shape of the role.

---

## Rubrics V3 conventions (must-follow)

- **Agent-centric phrasing.** Rubrics read as behaviors of *the Agent* — *"The Agent updates the Make-Ready Turns record for Unit 9D…"* — never passive constructions.
- **No tool names in prompts or rubrics.** Tool names like `airtable_mock_update_record` or `send_email` belong in the "typical write actions" author guidance, not in prompt bodies or rubric criteria.
- **Outcome rubrics first**, three sub-types: 1.1 write-action results, 1.2 action content, 2.1 key facts in the final response. Process rubrics only when a necessary behavior can't be captured by a stronger Outcome.
- **Natural-language prompts.** No pre-solving, no checklist tone, no `"I'm X, my role is Y…"` opener. Prompts read like a real internal message from a colleague.

---

## Target task volume across the 5 categories (100 tasks total)

| Category | Personas in scope | Tasks | Subcategories |
|---|---:|---:|---:|
| **1 · Property Operations** | 4 | **32** | 4 |
| **2 · Portfolio Coord & Owner Relations** | 2 | **20** | 3 |
| **3 · QC & Field Services** | 2 | **10** | 3 |
| **4 · Maintenance & Repairs** | 3 | **18** | 3 |
| **5 · Leasing & Applicant Intake** | 2 | **20** | 3 |
| **Total** | 13 | **100** | 16 |

Per-subcategory targets are called out inline below.

---

# Category 1 — Property Operations (Onsite PM Lane) · 32 tasks

## What it is

The day-to-day work of running a single property. **Four Onsite Property Manager personas** each own a property in the portfolio: Lisa Smith, Carlos Mendez, Patricia Nguyen, and Denise Morales. Each is the connective tissue at their property between field maintenance, leasing, tenants, and portfolio-level oversight (Brooke Phillips). This category also holds the ground-level workflows for **rent collection, eviction, and fair housing accommodations** — property-manager-owned, not portfolio-owned.

## Why it matters

The property-level PM is where the rubber meets the road on every operational workflow. A make-ready that slips because the PM didn't scope the punch-list properly costs a month of rent. A tenant complaint about A/C in a Texas July that doesn't get escalated is a life-safety issue. A late-rent notice that misses the state-mandated window creates a court-filing problem later. Every task in this category tests whether the agent can operate at the property level with real accountability.

## Authoring checklist

| Field | Value |
|---|---|
| **Personas** | **Lisa Smith** · **Carlos Mendez** · **Patricia Nguyen** · **Denise Morales** (all Onsite Property Manager) |
| **Other personas touched** | Brooke Phillips (escalation up), John Smith / Elias Navarro / James Bennett (maintenance handoff), Jaime Salinas (QC handoff), Sandra Allen / Kevin Okafor (leasing handoff), Teresa Wood (portfolio-level admin support) |
| **NPC participants** | Property owners (David Shea, Robert Finley, Linda Castillo, Harry Harris, Gary Hoffman), tenants (Tommy Reyes, Tanya Mitchell), rental applicants, Court Clerk (Patricia Lowe), Code Compliance Inspector (Barry Sanderson), Fire Extinguisher Service Tech (Marcus Williams) |
| **Primary systems** | **Airtable** (Make-Ready Turns records, Maintenance Tickets, unit status) · **Slack** `#make-ready`, `#maintenance`, `#general`, `#leasing` · **Gmail** (tenant + owner comms) · **Google Calendar** (property-level scheduling) · **Linear** (maintenance tickets opened or triaged) · **QuickBooks** (rent invoicing, delinquency records) |
| **Primary artifacts** | Make-Ready Turns records (Airtable), tenant/owner emails, Slack coordination posts, maintenance ticket triage, rent invoices, delinquency notices |
| **Linked study scenarios** | `makeready_turn_carlos`, `makeready_laspalmas8d_turn`, `makeready_turn_lasvistas_9d`, `maint_esc_carpet_repair_riobend`, `maintenance_escalation_waterheater_leak`, `fair_housing_reasonable_accommodation`, `rent_late_first_notice`, `rent_delinquency_payment_plan`, `rent_3day_notice_pay_or_quit`, `eviction_filing_prep`, `eviction_court_coordination` |

## Subcategories

### 1.1 Unit Turnover Coordination · 10 tasks

The move-out to re-leased lifecycle at a single property. Move-out inspection → scope-set → punch-list creation → vendor scheduling → QC handoff → marketing-ready sign-off. The Onsite PM coordinates across Maintenance (John / Elias / James), Portfolio Ops QC (Jaime), and specialty field services (Randy).

**Read:** `airtable_mock_list_records` (Make-Ready Turns base), `slack_mock_conversations_history` on `#make-ready`, `gmail_mock_search_emails` (vendor threads), `linear_mock_list_issues` (any open maintenance tickets on the unit).

**Write:** `airtable_mock_create_record` (new turn) or `airtable_mock_update_records` (status updates), `slack_mock_send_message` (`#make-ready` coordination), `gmail_mock_send_email` (vendor confirmations, owner updates), `linear_mock_create_issue` (repair items surfaced during walk-through), `gcalendar_mock_create_event` (vendor visits, QC walk-throughs).

**Artifacts to inject:** A tenant move-out notice (with move-out date), any prior turn history for the property, a vendor list with capacity, potentially a scheduling conflict.

**Linked scenarios:** `makeready_turn_carlos` (Carlos Mendez primary — 9 actions), `makeready_laspalmas8d_turn` (Carlos Mendez primary — 4 actions).

**Example.**

> Tommy Reyes vacated Unit 8D at Las Palmas yesterday. I need to open the make-ready properly and get us on Brooke's two-week target. Pull the Make-Ready Turns record if one already exists — otherwise create one with move-out date 5/5, status "Vacant — Pending Inspection", and initial scope notes. Post in `#make-ready` tagging John for the walk-through and noting the target date. Once John and James do the walk-through and I have the full scope (paint touch-up, bathroom fixture replacement, appliance pull, carpet cleaning, deep clean), update the record to "Scope Set" and email A Plus Carpet Cleaning & Repairs and Sunshine Cleaning to schedule. Give Brooke a status ping when the scope is locked in.
>
> *Prompt written by Carlos Mendez, Onsite Property Manager.*

### 1.2 Property-Level Maintenance Response · 8 tasks

Tenant reports an issue → Onsite PM triages → routes to internal maintenance or vendor → follows up with tenant. This is the tenant-facing side of maintenance work; the PM owns the tenant relationship during the repair even when John / Elias / James or a vendor does the actual work.

**Read:** `linear_mock_list_issues` (open tickets), `linear_mock_get_issue` (specific ticket detail), `slack_mock_conversations_history` on `#maintenance`, `gmail_mock_search_emails` (tenant threads).

**Write:** `linear_mock_create_issue` (new ticket if not already opened), `linear_mock_create_comment` (routing note), `slack_mock_send_message` (`#maintenance` coordination), `gmail_mock_send_email` (tenant reply with status/ETA), `gcalendar_mock_create_event` (repair appointment).

**Artifacts to inject:** Tenant email or ticket reporting an issue, prior work-order history on the unit or appliance, vendor availability constraint.

**Linked scenarios:** `maint_esc_carpet_repair_riobend` (Carlos Mendez primary — 6 actions), `maintenance_escalation_waterheater_leak` (Carlos Mendez primary — 6 actions).

**Example.**

> Tanya Mitchell in Unit 4B just emailed saying her water heater is leaking into the closet floor and she's been placing towels down since this morning. Check the Linear ticket queue — if there's already an open ticket for 4B, pull it and see where we are. If not, open one, mark it urgent, and get Hill Country Plumbing dispatched today. Reply to Tanya with a same-day appointment window and let her know we're on it — water damage compounds fast. If the diagnosis comes back as a full replacement rather than a repair, escalate to Brooke via `#maintenance` because that crosses the vendor-spend threshold and she'll need to loop the owner.
>
> *Prompt written by Carlos Mendez, Onsite Property Manager.*

### 1.3 Onsite Coordination & Tenant Support · 7 tasks

The cross-cutting property-level coordination work that isn't turnover, maintenance response, or rent collection — new-tenant orientation, small tenant requests (parking, package handling, noise complaints), staff coordination, and **fair-housing reasonable-accommodation requests** (mobility, service-animal, medical unit modifications, transfer requests). Lisa Smith leads the anchored fair-housing scenario; the rest is design-surface work.

**Read:** `airtable_mock_list_records` (tenant list at the property), `gmail_mock_search_emails` (tenant threads including accommodation requests), `contacts_search` (tenant contact records), `slack_mock_conversations_history` on `#general` and `#leasing` (if a transfer or unit swap is on the table).

**Write:** `gmail_mock_send_email` (tenant communications, formal accommodation-decision letters), `airtable_mock_update_records` (tenant status / notes, accommodation status), `slack_mock_send_message`, `gcalendar_mock_create_event` (tenant meetings, staff coordination, move-over walk-throughs), `linear_mock_create_issue` (any physical modifications required for an accommodation — ramp, grab bars).

**Artifacts to inject:** A tenant email raising a non-maintenance concern; a reasonable-accommodation request with medical or mobility context (10-day response expectation is standard); a lease-renewal window approaching; a staff scheduling gap.

**Linked scenarios:** `fair_housing_reasonable_accommodation` (Lisa Smith primary — 6 actions).

**Example.**

> Tanya Mitchell submitted a reasonable-accommodation request last week — she needs a ground-floor unit due to a new mobility limitation, and she'd like to move from her current second-floor unit to something available. Pull her tenant record and current lease details from Airtable, then check ground-floor availability across the property in the current Make-Ready Turns. Draft a warm and professional decision letter approving the accommodation, offering a ground-floor option from the current turn cycle with a matched rent bridge from her current lease. Coordinate with Sandra Allen in `#leasing` to draft the new lease and with John's team to open a Linear ticket for the grab-bar installation Tanya specifically asked about. Set a calendar event for the move-over walk-through.
>
> *Prompt written by Lisa Smith, Onsite Property Manager.*

### 1.4 Rent Collection & Eviction Lifecycle · 7 tasks

The full delinquency workflow — first late notice → payment-plan negotiation → 3-day pay-or-quit → eviction filing → court coordination with the Court Clerk (Patricia Lowe). Runs on state-mandated timing windows: miss a required notice window and the downstream eviction filing gets challenged. Patricia Nguyen leads all five anchored rent/eviction scenarios.

**Read:** `quickbooks_mock_list_invoices` (open rent invoices, delinquency ledger), `gmail_mock_search_emails` (prior notice correspondence — full trail becomes part of any filing packet), `airtable_mock_get_record` (tenant record with notice history), `contacts_search` (Patricia Lowe, Court Clerk).

**Write:** `gmail_mock_send_email` (late-notice letter, payment-plan offer, filing packet transmittal, court communications), `quickbooks_mock_update_invoice` (payment-plan terms, partial payment recording), `airtable_mock_update_records` (delinquency and eviction status, hearing date), `gcalendar_mock_create_event` (statutory notice deadlines, payment-plan check-ins, court date), `slack_mock_send_message` (`#general` or `#owner-relations`), `linear_mock_create_issue` (post-eviction unit turnover if court rules for the property).

**Artifacts to inject:** An overdue rent invoice past the statutory notice window; a tenant hardship email; a partial payment needing a payment-plan structure; a completed 3-day pay-or-quit notice with no response; a specific court date window from Patricia Lowe.

**Linked scenarios:** `rent_late_first_notice` (Patricia Nguyen primary — 5 actions), `rent_delinquency_payment_plan` (Patricia Nguyen primary — 5 actions), `rent_3day_notice_pay_or_quit` (Patricia Nguyen primary — 7 actions), `eviction_filing_prep` (Patricia Nguyen primary — 4 actions), `eviction_court_coordination` (Patricia Nguyen primary — 3 actions).

**Example.**

> The 3-day pay-or-quit window on Tanya Mitchell's unit expired yesterday with no payment or contact. I need to prep the eviction packet for filing. Pull the full notice trail from Gmail — first late notice, payment-plan offer, 3-day pay-or-quit — and the QuickBooks invoice showing the delinquency ledger. Confirm with Teresa Wood that the packet formatting matches what Patricia Lowe's office needs. Once assembled, email the packet to Patricia Lowe requesting a hearing date, and update the Airtable tenant record with status "Eviction Filed — awaiting hearing date." Post a brief internal note in `#general` so Carlos and Brooke know the property has an active eviction on it.
>
> *Prompt written by Patricia Nguyen, Onsite Property Manager.*

---

# Category 2 — Portfolio Coordination & Owner Relations · 20 tasks

## What it is

The cross-portfolio oversight layer. **Brooke Phillips**, as Apartment Property Supervisor over Portfolio Operations, coordinates across all ~10 properties — she runs the routine ops sync, approves vendor invoices, reviews budget variances, handles owner-facing communications, and is the escalation point when an onsite PM needs air cover. **Teresa Wood**, as Executive Secretary, supports Brooke on scheduled admin work — calendaring, correspondence formatting, vendor-invoice packet assembly, and executive-office communications with owners.

## Why it matters

Star PM is small enough that Brooke is present in nearly every meaningful workflow — 26 of 27 scenarios list her in the cast, and she's the primary actor in more than half. Teresa's admin support extends her reach into calendaring, filing prep, and owner-facing correspondence. This category holds the tasks where the portfolio-level voice is genuinely the correct one — because the work either spans multiple properties, requires signing authority above the onsite PM tier, or needs to be presented to an owner.

## Authoring checklist

| Field | Value |
|---|---|
| **Personas** | **Brooke Phillips** (Apartment Property Supervisor, Portfolio Operations) · **Teresa Wood** (Executive Secretary) |
| **Other personas touched** | All the onsite PMs (Lisa Smith, Carlos Mendez, Patricia Nguyen, Denise Morales), John Smith / Elias Navarro on maintenance escalations, Jaime Salinas on QC |
| **NPC participants** | Property owners (David Shea, Robert Finley, Linda Castillo, Harry Harris, Gary Hoffman, Dave Thomas), executive tier (Aurora Winona), major vendors (A Plus Carpet Cleaning & Repairs, Alamo HVAC Services, Hill Country Plumbing, Permian Make-Ready Crew) |
| **Primary systems** | **QuickBooks** (invoice approval, budget vs actual — the heaviest service in the universe) · **Gmail** (owner comms, vendor threads) · **Slack** (`#vendors`, `#owner-relations`, `#budget-review`, `#general`) · **Google Calendar** (owner meetings, ops sync) · **Airtable** (portfolio-level rollups) |
| **Primary artifacts** | Approved vendor invoices, budget-variance memos, owner reports and briefings, portfolio-level Slack coordination |
| **Linked study scenarios** | `property_ops_weekly_cycle`, `summer_makeready_weekly_cycle`, `portfolio_ops_preventive_maintenance_push`, `preventive_maintenance_push_routine`, `vendor_invoice_aplus_carpet_repair`, `vendor_invoice_landscape_may2026`, `budget_review_makeready_q2`, `owner_monthly_report_review`, `owner_portfolio_review_midyear`, `owner_capex_approval_roof` |

## Subcategories

### 2.1 Cross-Portfolio Operations Sync · 7 tasks

Routine sync meetings across the onsite PMs, seasonal pushes (the summer make-ready surge is the canonical shape), cross-property scheduling, and coordination when a workflow spans multiple properties or requires more than one property's capacity.

**Read:** `slack_mock_conversations_history` on `#general` and `#make-ready`, `airtable_mock_list_records` (portfolio rollups), `gcalendar_mock_list_events` (upcoming sync meetings), `gmail_mock_search_emails` (onsite PM threads).

**Write:** `slack_mock_send_message` (`#general`, `#make-ready`), `gcalendar_mock_create_event` (sync meetings), `gmail_mock_send_email` (batch outreach to onsite PMs), `airtable_mock_update_records` (portfolio-level status tracking).

**Artifacts to inject:** A calendar trigger for the routine sync; a seasonal capacity strain (summer heat + turn volume); an onsite PM raising a cross-property issue.

**Linked scenarios:** `property_ops_weekly_cycle` (Brooke Phillips primary — 5 actions), `summer_makeready_weekly_cycle` (Brooke Phillips primary — 5 actions), `portfolio_ops_preventive_maintenance_push` (Brooke Phillips primary — 4 actions).

**Example.**

> It's the last Friday of June and I want to lock down the July make-ready schedule before we get another week into the heat. Pull the current Airtable Make-Ready Turns records across all properties and give me a count of vacants and in-flight turns per property. Cross-reference against our vendor capacity — I know A Plus Carpet Cleaning & Repairs and Permian Make-Ready Crew are already tight. Post in `#make-ready` with the summary tagging Lisa, Carlos, Patricia, and Denise, and set up a 30-minute sync on the calendar for next Wednesday so we can walk through how we're staffing the surge. If any property looks like it's headed for a scope-set backlog, flag it in the post.
>
> *Prompt written by Brooke Phillips, Apartment Property Supervisor.*

### 2.2 Vendor Invoice Approval & Budget Oversight · 7 tasks

Invoice review and approval, budget variance analysis, spend-vs-plan reporting, contract renewal decisions. Star PM runs on a make-ready-heavy budget cycle — variance overruns get real scrutiny. Teresa Wood assembles the invoice-approval packets Brooke reviews.

**Read:** `quickbooks_mock_list_bills` (open payables), `quickbooks_mock_get_bill` (invoice detail), `airtable_mock_list_records` (Make-Ready Turns for work verification), `gmail_mock_search_emails` (vendor threads).

**Write:** `quickbooks_mock_update_bill` (approve / hold / dispute), `slack_mock_send_message` (`#vendors`, `#budget-review`), `gmail_mock_send_email` (vendor confirmation, dispute letter, internal briefing), `linear_mock_create_issue` (if a systemic vendor issue surfaces).

**Artifacts to inject:** A vendor invoice with a line-item discrepancy; a make-ready spend that overshoots budget; a vendor rate-change notice.

**Linked scenarios:** `vendor_invoice_aplus_carpet_repair` (Carlos Mendez, Brooke Phillips, Victor Rios each 2 actions — collaborative), `vendor_invoice_landscape_may2026` (Teresa Wood primary — 5 actions), `budget_review_makeready_q2` (Brooke Phillips primary — 4 actions).

**Example.**

> A Plus Carpet Cleaning & Repairs' May carpet-repair invoice came in — verify each line item against the Airtable Make-Ready Turns records for the units on the bill, confirm each turn was actually completed in May, and check the price against our contracted rate. If the totals reconcile, approve the invoice in QuickBooks and post confirmation in `#vendors`. If any line looks off — wrong unit, wrong price, cancelled turn — put a hold on the bill and email Victor Rios (their lead technician) with the specific discrepancies. Copy Carlos and Lisa if any of their units are on the invoice so they can weigh in on scope.
>
> *Prompt written by Brooke Phillips, Apartment Property Supervisor.*

### 2.3 Owner Reporting, Communications & CapEx Approvals · 6 tasks

Monthly performance reports, mid-year portfolio reviews, distribution tracking, owner-facing communications, and the **CapEx approval flow** — capital-expenditure requests that cross the routine-maintenance spend threshold and require owner approval before commit (roof repairs, HVAC replacements, exterior renovations). Owners on file: David Shea, Robert Finley, Linda Castillo, Harry Harris. Teresa Wood assembles the report packets and manages the owner-side calendar.

**Read:** `quickbooks_mock_list_bills` / `quickbooks_mock_list_invoices` (P&L support, prior spend history), `linear_mock_get_issue` (originating maintenance ticket for a CapEx), `airtable_mock_list_records` (occupancy, turn status, common-area records), `gmail_mock_search_emails` (recent owner threads, vendor quote threads), `contacts_search` (owner contact records), `gcalendar_mock_list_events` (upcoming owner meetings).

**Write:** `gmail_mock_send_email` (owner report, meeting brief, CapEx memo, vendor quote transmittal, approval confirmation), `gcalendar_mock_create_event` (owner sync, CapEx approval call, project kickoff), `airtable_mock_update_records` (mark reports sent, CapEx status tracking), `quickbooks_mock_create_bill` (once CapEx is approved), `slack_mock_send_message` (`#owner-relations`, `#budget-review` for internal awareness).

**Artifacts to inject:** An owner requesting a status update; a month-end performance moment; a mid-year cadence trigger; a maintenance ticket escalated into a common-area or structural issue; two or more vendor quotes with different scopes.

**Linked scenarios:** `owner_monthly_report_review` (Brooke Phillips primary — 7 actions), `owner_portfolio_review_midyear` (Brooke Phillips primary — 4 actions), `owner_capex_approval_roof` (Brooke Phillips primary — 8 actions).

**Example.**

> John flagged the Ridgeview roof section on the top-floor common structural — missing shingles and interior ceiling stains after last week's storm. I need to bring this to Robert Finley for CapEx approval. Pull the maintenance ticket and John's inspection notes, then package the two vendor quotes we have from Alamo HVAC Services and Big Bend Restoration (Big Bend's scope is broader and includes debris removal; Alamo's is repair-only). Draft the CapEx memo to Robert with both options, recommended path, and a clear timeline. Put a 30-minute call on his calendar for Wednesday. Post in `#owner-relations` and `#budget-review` internally so Teresa Wood and I are aligned before the call. Once Robert approves, create the vendor bill in QuickBooks and open the Airtable common-area CapEx record.
>
> *Prompt written by Brooke Phillips, Apartment Property Supervisor.*

---

# Category 3 — Quality Control & Field Services · 10 tasks

## What it is

The specialty field-operator lane inside Portfolio Operations. Two personas share this category with very different day-to-day work: **Jaime Salinas** moves through properties with an impartial QC eye, feeding observations back into the make-ready workflow; **Randy Jones** handles appliance swaps and bulk-item retrieval across the portfolio.

Both are cross-property (they don't belong to a single property like the Onsite PMs) and both operate largely in the field with minimal desk work. Their scripted footprint is thin — Jaime participates as a QC anchor across 7 make-ready and portfolio scenarios but rarely drives the majority of actions; Randy has one scripted action. Tasks in this category are largely design-surface work anchored on their real-world roles.

## Why it matters

Star PM's make-ready cycle depends on both roles. A turn that doesn't get Jaime's QC sign-off isn't ready to re-lease. An appliance swap that Randy hasn't executed leaves the unit incomplete. These are essential handoffs — the fact that they don't drive the majority of actions in the current scenario set is a scripted-footprint gap, not a role gap.

## Authoring checklist

| Field | Value |
|---|---|
| **Personas** | **Jaime Salinas** (Quality Control Inspector) · **Randy Jones** (Appliance & Bulk-Item Retrieval Specialist) |
| **Other personas touched** | Lisa / Carlos / Patricia / Denise (property-level handoffs), John Smith / Elias Navarro (post-repair QC), Brooke Phillips (escalation and reporting) |
| **NPC participants** | Onsite housekeeping (Isela Juarez, Rosa Cantu), Code Compliance Inspector (Barry Sanderson), Fire Extinguisher Service Tech (Marcus Williams), Pest Control (Ruben Barr), vendor teams during turns |
| **Primary systems** | **Airtable** (Make-Ready Turns QC status, inspection tracking) · **Slack** (`#make-ready`, `#general`) · **Google Calendar** (walk-through scheduling) · **Linear** (issues surfaced during inspection) · **Gmail** (inspector correspondence) |
| **Primary artifacts** | QC walk-through notes, punch-list updates, inspection notes stored in Airtable record fields, appliance-swap logs |
| **Linked study scenarios** | Design-surface — Jaime participates across `makeready_turn_carlos`, `makeready_laspalmas8d_turn`, `makeready_turn_lasvistas_9d`, `summer_makeready_weekly_cycle`, `portfolio_ops_preventive_maintenance_push`; Randy is a light participant |

## Subcategories

### 3.1 Make-Ready QC Walk-Throughs · 5 tasks

The post-scope-set QC pass. Jaime walks the unit after the maintenance team declares work complete, validates the punch-list, and either signs off on marketing-ready status or kicks work back for corrections.

**Read:** `airtable_mock_get_record` (Make-Ready Turns record for the unit), `slack_mock_conversations_history` on `#make-ready`, `linear_mock_list_issues` (open items on the unit).

**Write:** `airtable_mock_update_records` (QC status: Approved / Needs Rework, with observation notes), `slack_mock_send_message` (`#make-ready` sign-off or kickback), `linear_mock_create_issue` (any surprise issues found during QC), `gmail_mock_send_email` (Onsite PM notification).

**Artifacts to inject:** A unit in "Ready for QC" status with a completed punch-list; occasional discrepancy between the scope set and the actual finished work.

**Example.**

> Carlos flagged Unit 8D at Las Palmas as ready for QC — the paint, bathroom fixtures, and deep clean are done. Walk the unit against the punch-list on the Airtable Make-Ready Turns record. If everything checks out, flip the status to "QC Approved — Marketing Ready" and post the sign-off in `#make-ready` tagging Carlos. If anything's off — paint touch-ups missed, bathroom caulk sloppy, cleaning didn't include the appliance interiors — put the status back to "Needs Rework" with specific observation notes and open a Linear ticket per item so John's team can close them out. Copy Brooke on the `#make-ready` post either way, since 8D is on her radar this week.
>
> *Prompt written by Jaime Salinas, Quality Control Inspector.*

### 3.2 Property Inspections & Compliance · 3 tasks

Routine standing-property inspections (not tied to a turn), code compliance follow-through when Barry Sanderson or another inspector flags an issue, fire-extinguisher and life-safety inspections coordinated with Marcus Williams. Cross-property scope. Design-surface subcategory — no anchor scenario yet, but a real Jaime workflow.

**Read:** `gmail_mock_search_emails` (inspector correspondence), `airtable_mock_list_records` (properties with open compliance items), `gcalendar_mock_list_events` (upcoming inspection windows).

**Write:** `airtable_mock_update_records` (compliance status, inspection notes stored on the record), `linear_mock_create_issue` (items requiring remediation), `gmail_mock_send_email` (inspector reply, Onsite PM notification), `slack_mock_send_message` (`#general` if a life-safety item is urgent), `gcalendar_mock_create_event` (inspection appointment).

**Artifacts to inject:** A code compliance notice from Barry Sanderson; a life-safety window (fire extinguisher inspection due); an annual property walk-through cadence.

**Example.**

> Barry Sanderson emailed about the fire extinguisher tags at Mesa Vista — three are past their annual inspection date. Check the Airtable compliance record for Mesa Vista and confirm which units are affected. Coordinate with Marcus Williams to get the tags refreshed within the 10-day window Barry gave us, and put the appointment on the calendar. Update the Airtable compliance record to show the item as "In Remediation" with the vendor and expected close date. Once Marcus completes the tags, log the completion note on the Airtable record and reply to Barry confirming closure. Ping Brooke in `#general` if anything's going to slip the deadline.
>
> *Prompt written by Jaime Salinas, Quality Control Inspector.*

### 3.3 Appliance & Bulk-Item Retrieval · 2 tasks

The field-level appliance and bulk-item work during turns. Randy pulls old appliances during move-out, delivers replacements during scope-set, hauls bulk waste and abandoned items. Cross-portfolio, coordinated with the Onsite PMs and the make-ready timeline. Design-surface subcategory — Randy has one scripted action in the current scenario set.

**Read:** `airtable_mock_get_record` (Make-Ready Turns record — pulls current scope), `slack_mock_conversations_history` on `#make-ready`, `gcalendar_mock_list_events` (his own scheduled pickups/deliveries).

**Write:** `airtable_mock_update_records` (log appliance pull/deliver, bulk pickup complete), `slack_mock_send_message` (`#make-ready` status ping), `gcalendar_mock_create_event` (next scheduled pickup), `gmail_mock_send_email` (rare — occasional coordination with disposal vendors).

**Artifacts to inject:** A turn scope calling out appliance replacement; a bulk-item pickup request from an Onsite PM; a scheduling conflict across two properties on the same day.

**Example.**

> Carlos needs the old refrigerator out of Unit 8D at Las Palmas before the new one arrives Thursday. Check the Airtable Make-Ready record to confirm the scope calls for a full appliance swap and note whether the new fridge is already on-site or being delivered. If pickup is Thursday, schedule my own truck run for Wednesday afternoon to pull the old unit — put it on my calendar. Update the Make-Ready record to log the appliance pull with date and disposition (haul to yard vs. donate). Post a quick "8D old fridge out" note in `#make-ready` so Carlos and Jaime know we're clear for the delivery window. If I hit a scheduling conflict with a Mesa Vista pickup request, flag it to Brooke.
>
> *Prompt written by Randy Jones, Appliance & Bulk-Item Retrieval Specialist.*

---

# Category 4 — Maintenance & Repairs · 18 tasks

## What it is

The ticket-to-close lane on all maintenance work — both routine and escalated. Three maintenance-tech personas share this category: **John Smith** and **Elias Navarro** as Lead Maintenance Technicians (John general lead, Elias rooted in the HVAC-heavy scenario), and **James Bennett** as Assistant Maintenance Technician. HVAC is a first-class concern in Southwest Texas, particularly through the summer, and compressor-scale failures are life-safety territory that get escalated to Brooke.

## Why it matters

Maintenance is the workflow tenants feel directly. Every A/C outage in July is a retention risk. Every preventive maintenance round that gets skipped is a compounding cost that shows up at turnover. Star PM runs a ticket-driven maintenance model (Linear is the primary maintenance system of record) with the Lead's judgment as the routing layer.

## Authoring checklist

| Field | Value |
|---|---|
| **Personas** | **John Smith** · **Elias Navarro** (Lead Maintenance Technicians) · **James Bennett** (Assistant Maintenance Technician) |
| **Other personas touched** | Lisa / Carlos / Patricia / Denise on tenant-facing coordination, Brooke Phillips on HVAC escalations, Randy Jones on appliance-adjacent work, Jaime Salinas on post-repair QC |
| **NPC participants** | Assistant maintenance NPCs (Wesley Tran, Tony Reyes), tenants (Tommy Reyes, Tanya Mitchell), vendors — Alamo HVAC Services (Victor Rios is A Plus Carpet's lead tech, not HVAC), Hill Country Plumbing, A Plus Carpet Cleaning & Repairs, Big Bend Restoration, Lone Star Electric, Pest Control (Ruben Barr), Exterior Painter (Pete Donovan) |
| **Primary systems** | **Linear** (ticket system — the primary maintenance system of record) · **Slack** (`#maintenance`, `#vendors`) · **Gmail** (vendor threads, tenant coordination) · **Google Calendar** (dispatch scheduling, vendor visits) · **QuickBooks** (work-order costing) |
| **Primary artifacts** | Linear tickets (open → in progress → done → closed), Slack coordination in `#maintenance`, vendor emails, work-order records |
| **Linked study scenarios** | `maintenance_hvac_elias`, `maintenance_escalation_waterheater_leak`, `maint_esc_carpet_repair_riobend`, `preventive_maintenance_push_routine`, participation in `makeready_turn_lasvistas_9d` and `makeready_laspalmas8d_turn` |

## Subcategories

### 4.1 Ticket Triage & Dispatch · 6 tasks

Incoming ticket intake, urgency assessment, dispatch to internal tech or vendor. The Lead's core lane — routing between tenant reports (via the Onsite PM or direct) and the maintenance execution. Simple repairs go to James; escalations go up to Brooke.

**Read:** `linear_mock_list_issues` (open queue), `linear_mock_get_issue` (specific detail), `slack_mock_conversations_history` on `#maintenance`, `gmail_mock_search_emails` (tenant/vendor threads).

**Write:** `linear_mock_update_issue` (status, assignee, priority), `linear_mock_create_comment` (routing note, diagnosis), `slack_mock_send_message` (`#maintenance` dispatch note), `gcalendar_mock_create_event` (repair appointment).

**Artifacts to inject:** A tenant report of a specific issue; a queue of routine tickets needing prioritization; a scheduling conflict between competing repairs.

**Example.**

> Carlos just moved a garbage-disposal ticket into my queue from a tenant at Unit 8D at Las Palmas. Pull the ticket in Linear — read the description and any prior comments. If this looks like a jammed unit, assign it to James for a same-day visit and schedule the appointment on the calendar. Post a `#maintenance` note tagging James so he knows to grab the disposal wrench and the reset key before he heads out. Once James is on-site, follow the ticket — if it turns out the disposal needs replacement instead of repair, I'll handle the parts order and let Brooke know we're touching a small capex line.
>
> *Prompt written by John Smith, Lead Maintenance Technician.*

### 4.2 Escalated Repairs & Vendor Coordination · 7 tasks

The compressor-scale, life-safety-adjacent maintenance work — HVAC compressor failures, water-heater leaks, carpet-damage escalations — along with the vendor lifecycle that sits alongside them (dispatch, work-order sign-off, invoice-ready close-out). Southwest Texas summers make A/C an operational priority; escalations loop in Brooke because they involve vendor sign-off (Alamo HVAC Services, Hill Country Plumbing, A Plus Carpet Cleaning & Repairs) and often cross a spend threshold. Elias Navarro leads the anchored HVAC scenario in the current universe.

**Read:** `linear_mock_get_issue` (ticket detail), `slack_mock_conversations_history` on `#maintenance` and `#vendors`, `gmail_mock_search_emails` (vendor threads), `quickbooks_mock_list_bills` (prior spend on the unit, property, or vendor), `contacts_search` (vendor contact records).

**Write:** `linear_mock_update_issue` (escalate priority, add vendor as watcher, "Complete — awaiting invoice" sign-off), `linear_mock_create_comment` (diagnosis note, sign-off referencing model / serial), `slack_mock_send_message` (`#maintenance`, `#vendors`), `gmail_mock_send_email` (vendor dispatch, tenant status update, invoice-ready confirmation), `gcalendar_mock_create_event` (vendor visit), `airtable_mock_update_records` (vendor performance / notes).

**Artifacts to inject:** A tenant HVAC or water-heater report during a heat window; a diagnosis pointing at compressor / tank replacement rather than a filter or valve; a prior ticket on the same unit within 90 days (systemic issue); a work-order needing sign-off before invoice.

**Linked scenarios:** `maintenance_hvac_elias` (Elias Navarro primary — 8 actions), `maintenance_escalation_waterheater_leak` (Carlos Mendez primary but rooted in Maintenance workflow), `maint_esc_carpet_repair_riobend` (Carlos Mendez primary but rooted in Maintenance workflow — Victor Rios at A Plus Carpet Cleaning & Repairs on the vendor side).

**Example.**

> Carlos escalated the A/C ticket on a Rio Bend unit — I did the diagnostic this morning and it's the compressor, not the thermostat. This is a vendor call, not something James and I can handle. Update the Linear ticket to reflect the compressor diagnosis, add Alamo HVAC Services as a watcher, and bump priority to urgent — the tenant is in the unit and it's going to hit 102 tomorrow. Email Alamo with the ticket ID asking for a same-day visit, and copy Brooke — we're looking at a $2K+ vendor invoice which she'll need to approve. Post in `#maintenance` and `#vendors` so everyone's on the same page. Once Alamo completes the swap, drop a sign-off comment on the ticket referencing the new compressor's model and serial, and email Alamo confirming we're clear to bill.
>
> *Prompt written by Elias Navarro, Lead Maintenance Technician.*

### 4.3 Preventive Maintenance · 5 tasks

The scheduled PM rounds — HVAC coil cleaning, filter changes, water-heater flushes, exterior touch-ups. Runs on a routine cadence, distinct from reactive tickets. Star PM tries to hit PM cycles ahead of the summer heat surge.

**Read:** `linear_mock_list_issues` (open PM tickets), `airtable_mock_list_records` (units due for PM per schedule), `gcalendar_mock_list_events` (existing PM windows), `slack_mock_conversations_history` on `#maintenance`.

**Write:** `linear_mock_create_issue` (new PM ticket per unit/system), `linear_mock_update_issue` (close on completion), `gcalendar_mock_create_event` (PM appointment blocks), `slack_mock_send_message` (`#maintenance` planning update), `airtable_mock_update_records` (PM tracker: last date, next due).

**Artifacts to inject:** A seasonal PM cadence (pre-summer HVAC push); a specific unit's last PM date; a vendor availability window.

**Linked scenarios:** `preventive_maintenance_push_routine` (Brooke Phillips primary but rooted in Maintenance workflow — John Smith and Elias Navarro on execution).

**Example.**

> Brooke wants the annual HVAC coil cleaning done across the portfolio before we get any deeper into July. Pull the Airtable PM tracker to see which units are past due — I think Las Palmas and Mesa Vista are most of them. For each unit that's due, open a Linear ticket, assign it to me, Elias, or James depending on load, and put the appointment on the calendar. If any unit is more than 90 days past due, flag it separately — those go to the top of the list because they're the ones likely to fail this summer. Post a `#maintenance` schedule summary tagging Lisa and Carlos so the Onsite PMs know when their units are being touched, and let Brooke know once the plan is locked in.
>
> *Prompt written by John Smith, Lead Maintenance Technician.*

---

# Category 5 — Leasing & Applicant Intake · 20 tasks

## What it is

The full leasing lifecycle: inbound inquiry → tour scheduling → application processing → screening → lease execution → move-in coordination, plus **the retention loop** on the back end: renewal outreach → renewal offer → renewal accepted or declined-to-move-out. **Two leasing personas** share the category: **Sandra Allen** (intake anchor) and **Kevin Okafor** (renewal anchor). Lisa / Carlos / Patricia / Denise back them up on the onsite side.

## Why it matters

Vacancy days are the single biggest lever in property-management economics. A unit that takes seven days to lease vs. two costs the owner real money. And renewals matter as much as new leases — turning over a well-behaved tenant costs a month of vacancy plus a full make-ready. Category 5 tests whether an agent can drive the leasing lifecycle end-to-end (new lease AND renewal) without cutting corners on screening or letting inquiries go cold.

## Authoring checklist

| Field | Value |
|---|---|
| **Personas** | **Sandra Allen** (Leasing Agent, intake anchor) · **Kevin Okafor** (Leasing Agent, renewal-heavy) |
| **Other personas touched** | Lisa / Carlos / Patricia / Denise (Onsite PM backup, application approval sign-off), Brooke Phillips (portfolio-level pipeline visibility) |
| **NPC participants** | Alicia Vega (NPC Leasing Agent — leads `lease_renewal_offer_standard`), Maria Lopez (NPC Weekend Leasing Agent), Necia Perales (Apartment Locator), Tasha Wentworth / Craig Pemberton / Jerome Okafor / Lindsey Carmichael / Darnell Hutchins / Svetlana Borisova (referral partners), applicants (Priya Nambiar, Marcus Delgado, Angela Carter, Tobias Wren, Yuki Tanaka, Simone Okafor, Derek Hutchinson, and others), existing tenants for renewal (Tommy Reyes, Connor Beaumont) |
| **Primary systems** | **HubSpot** (leasing pipeline — the CRM system of record: contacts, deals, notes, associations) · **Gmail** (applicant communication) · **Google Calendar** (tour scheduling) · **Airtable** (unit availability rollup) · **Slack** (`#leasing`, `#applications`) · **QuickBooks** (first-month rent + deposit on move-in) |
| **Primary artifacts** | HubSpot contact + deal records per applicant, tour calendar events, application document attachments on HubSpot notes or Gmail, lease agreements, renewal offers |
| **Linked study scenarios** | `lease_inquiry_delgado_referral`, `rental_app_priya_nambiar`, `leasing_application_to_movein`, `lease_renewal_offer_standard`, `lease_renewal_declined_to_moveout` |

## Subcategories

### 5.1 Inquiry, Tour & Application Intake · 8 tasks

The top-of-funnel and screening lane — inbound lead → tour scheduled → application submitted → document verification → background / credit screening → approval or denial decision. Runs continuously from an inbound email or referral through the "ready to draft a lease" milestone. Sandra Allen leads the anchored intake scenarios; referral-source applications (like Priya Nambiar's, referred through Apartment Locator Central) come with existing context.

**Read:** `hubspot_search_contacts` / `hubspot_get_contact` (existing lead / applicant record), `hubspot_get_deal` (deal stage and prior notes), `airtable_mock_list_records` (current vacants and pricing), `gmail_mock_search_emails` (prior threads with the lead, referral threads, uploaded application docs), `gcalendar_mock_list_events` (agent availability for tours).

**Write:** `hubspot_create_contact` / `hubspot_update_contact` (new lead), `hubspot_create_deal` (open leasing deal, associated to the contact), `hubspot_update_deal` (stage progression: Inquiry → Tour Scheduled → Application → Screening → Approved / Denied), `hubspot_create_note` (screening report, verification notes on the deal), `gmail_mock_send_email` (inquiry response with unit options + tour times, screening request to background vendor, applicant status update), `gcalendar_mock_create_event` (tour appointment), `slack_mock_send_message` (`#leasing`, `#applications` handoff).

**Artifacts to inject:** An inbound inquiry with preference signals (bedrooms, budget, timing); a referral source thread (Necia Perales, Tasha Wentworth, Jerome Okafor); a partial application missing income verification; a credit-score edge case; a prior-residence red flag.

**Linked scenarios:** `lease_inquiry_delgado_referral` (Sandra Allen primary — 7 actions), `rental_app_priya_nambiar` (Sandra Allen primary — 7 actions).

**Example.**

> Priya Nambiar's application came in — she's referred by Jerome Okafor from Apartment Locator Central. Pull her HubSpot contact and the deal she was tagged on. Verify income from the pay stubs she attached to her Gmail thread — I want to see three months for a full picture — and check that her ID and prior-residence letter are in the thread. If any doc is missing, email Priya asking for it politely, giving her 48 hours before we pause the app. Once the packet is complete, kick off the background/credit screening — email our vendor with her info, drop a "Screening Started" note on the HubSpot deal, and post `#applications` so Lisa knows we've got a referred applicant moving through. If anything comes back marginal on the screening, loop Lisa before we send Priya a decision.
>
> *Prompt written by Sandra Allen, Leasing Agent.*

### 5.2 Lease Execution & Move-In Coordination · 6 tasks

The closing lane of the new-lease side: approved applicant → lease drafted → signed → deposit collected → keys handed over → new tenant onboarded.

**Read:** `hubspot_get_deal` (approved deal, stage: Ready for Lease Execution), `hubspot_get_contact` (applicant record), `airtable_mock_get_record` (unit availability and turn status).

**Write:** `hubspot_update_deal` (stage: Lease Signed → Move-In Scheduled), `hubspot_create_note` (executed lease terms on the deal record), `gmail_mock_send_email` (lease-to-sign to applicant, welcome email post-signing), `gcalendar_mock_create_event` (move-in walk-through), `quickbooks_mock_create_invoice` (first-month rent + deposit), `airtable_mock_update_records` (unit status: Leased, tenant name, move-in date), `slack_mock_send_message` (`#leasing` + `#make-ready` for readiness handoff).

**Artifacts to inject:** An approved applicant with a target move-in date; a unit still finishing its turn on a tight timeline; a deposit that hasn't cleared the day before move-in.

**Linked scenarios:** `leasing_application_to_movein` (Sandra Allen primary — 4 actions).

**Example.**

> Marcus Delgado is approved for a 2BR at Las Palmas — Carlos signed off yesterday and Marcus wants to move in July 15. Pull the deal in HubSpot and confirm the associated contact and screening notes are attached. Draft the lease using our standard 12-month template — Unit 8D, standard rent, standard deposit, July 15 start — and attach it as a HubSpot note on the deal. Send the lease PDF to Marcus via Gmail for signature with a 5-day return window, and drop the calendar event for the July 15 move-in walk-through (Carlos will handle the actual hand-off). Once he signs, update the HubSpot deal stage to "Move-In Scheduled", create the QuickBooks invoice for first month + deposit, and update the Airtable unit record to "Leased — Move-In 7/15". Post in `#leasing` and give Jaime a heads-up in `#make-ready` — 8D needs to be fully turn-complete by July 13 to give us buffer.
>
> *Prompt written by Sandra Allen, Leasing Agent.*

### 5.3 Lease Renewals & Retention · 6 tasks

The back-end of the leasing lifecycle: renewal outreach → renewal offer → renewal signed OR declined-to-move-out. Kevin Okafor leads the anchored renewal-decline scenario; Alicia Vega (NPC) drives the anchored standard-renewal scenario. Retention is treated as leasing-owned work because the CRM (HubSpot) is where the renewal lifecycle lives, not the property-side tenant record.

**Read:** `hubspot_get_contact` (tenant contact), `hubspot_get_deal` (renewal deal or original lease deal), `airtable_mock_get_record` (tenant record and lease-end date), `gmail_mock_search_emails` (tenant thread).

**Write:** `hubspot_update_deal` (renewal stage), `hubspot_create_deal` (new renewal deal opened off the existing contact), `hubspot_create_note` (renewal terms, tenant response), `gmail_mock_send_email` (renewal offer, decision confirmation), `gcalendar_mock_create_event` (renewal-window follow-up, move-out walk-through if declined), `airtable_mock_update_records` (tenant status update).

**Artifacts to inject:** A lease approaching its 60-day renewal window; a tenant with a mixed maintenance / rent history; a rent-bump within market range that may be declined.

**Linked scenarios:** `lease_renewal_declined_to_moveout` (Kevin Okafor primary — 6 actions), `lease_renewal_offer_standard` (Alicia Vega NPC primary — Kevin Okafor should be the persona voice for the same shape).

**Example.**

> Connor Beaumont's lease at Mesa Vista is up September 30 and we need to send the renewal offer this week to stay in the 60-day window. Pull his HubSpot contact and the original lease deal to confirm his current rent and lease terms. Check his Airtable tenant record for any maintenance flags or late-rent history in the last 12 months. Open a new HubSpot deal on his contact at the "Renewal Offer Sent" stage. Draft the renewal offer email — standard 12-month renewal at a modest bump within our range, keeping his other terms the same. Set a 10-day response window and put a follow-up on my calendar. If he doesn't respond in the first five days, escalate to a call rather than another email. Post a brief `#leasing` note tagging Lisa so she knows we're in the renewal window on his unit.
>
> *Prompt written by Kevin Okafor, Leasing Agent.*

---

# How to write a strong Star PM task prompt

A good Star PM task prompt has these properties:

- **Written in the natural style** of a real colleague handing off work — not a template, not a checklist preamble. Drop straight into the request. The attribution line (`*Prompt written by …*`) goes **outside** the prompt body.
- **Anchored to specific universe artifacts** — unit numbers (8D, 9D, 4B), property names (Las Palmas, Las Vistas, Mesa Vista, Rio Bend, Ridgeview), vendor names (A Plus Carpet Cleaning & Repairs, Alamo HVAC Services, Hill Country Plumbing, Permian Make-Ready Crew), tenant names, ticket IDs. Confirm anchors against the live data before committing.
- **Multi-system.** A genuine Star PM task touches at least 3 services — commonly HubSpot + Gmail + Calendar for leasing; Airtable + Slack + Linear for turnovers; QuickBooks + Gmail + Airtable for financial oversight; Linear + Slack + Calendar for maintenance.
- **Respectful of persona Business Functions.** Author from the persona's assigned Business Function, even when the workflow crosses other categories in execution. An Onsite PM authoring a maintenance task is a Category 1 prompt (property-level maintenance response); a Lead Maintenance persona authoring the same shape is a Category 4 prompt (ticket triage & dispatch).
- **Followed by an attribution line** identifying the authoring persona and their role.

## Difficulty levers

- **More systems to read across.** Force the agent to pull from Airtable + Linear + QuickBooks + Slack + Gmail rather than one or two.
- **Verification of every cited number.** If the prompt references a unit, expect the agent to confirm its turn status in Airtable. If it references a ticket, expect a Linear pull. If it references a vendor invoice, expect QuickBooks + the Make-Ready Turns cross-check.
- **Multi-step chained dependencies.** Step 2 depends on Step 1's correct output; Step 5 depends on Step 4. A missed step breaks the chain.
- **Reconciling persona vs NPC scripted work.** A handful of NPCs (Alicia Vega, Tony Reyes, Wesley Tran, Isela Juarez) carry scripted actions inside some scenarios — tasks can require the agent to reconcile "who did what" across persona and NPC actors, surfacing what an NPC actually posted vs what the persona's voice should now do next.
- **Filter at volume.** Make the agent surface the relevant 3 tickets from a queue of 30, or the 5 leases due to renew in the next 45 days from a portfolio of 100.
- **Timeline-driven sequencing.** Turnover deadlines, move-in dates, PM cycles, statutory rent-notice windows, court dates, owner report cadence — all constrain sequencing and force the agent to prioritize.
- **Cross-property context.** Mixing work across multiple properties surfaces coordination challenges (vendor capacity, cross-portfolio scheduling, portfolio-level rollup reporting).
- **Red herrings in the data.** Unrelated anomalies the agent should ignore — the right answer requires identifying which signals matter and which don't.
