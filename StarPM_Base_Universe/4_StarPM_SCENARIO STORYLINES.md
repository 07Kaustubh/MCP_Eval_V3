# Star Property Management — Scenario Storylines

Per-scenario detail for the 27 scripted scenarios in Star PM. Each block covers the storyline, the primary actor, the supporting cast, the scripted-action count, and the systems the scenario touches.

> **Reading these storylines.** The "primary actor" is who leads by scripted-action count. Supporting cast are named participants. Numbers in parentheses on the primary actor line show total scripted actions.
>
> **Grouping.** Scenarios are grouped by their **primary business function** — the category the leading actor belongs to. Some scenarios cross-cut multiple functions in execution; the grouping reflects home ownership.

---

# Cat 1 — Property Operations (10 primary scenarios)

## Make-ready turnovers

### `makeready_turn_carlos` — Mesa Vista 4C Make-Ready Turn
- **Primary actor:** Carlos Mendez (9)
- **Cast:** Carlos Mendez, Tony Reyes, Carmen Delgado (Sunshine Cleaning), Pete Donovan, Jaime Salinas, Brooke Phillips, Linda Castillo
- **Storyline.** Previous tenant vacates 4C. Carlos creates the Make-Ready Turn record, walks the unit and documents a punch list, dispatches Sunshine Cleaning (via Carmen Delgado) for the deep clean, emails Pete Donovan for the interior paint quote and schedule. Internal repairs are logged in Airtable. Cleaning and painting invoices come in and get processed. Jaime does the QC walk-through and signs off. An owner invoice gets issued to Linda Castillo. Carlos marks the unit market-ready and posts the completion update.
- **Systems.** Airtable · Slack · Gmail · Google Calendar · QuickBooks

### `makeready_laspalmas8d_turn` — Las Palmas 8D Make-Ready Turn
- **Primary actor:** Carlos Mendez (4)
- **Cast:** Carlos Mendez, Brooke Phillips, John Smith, James Bennett, Victor Rios, Isela Juarez, Jaime Salinas
- **Storyline.** Carlos walks the vacated 8D, creates the Make-Ready Turn record, posts to `#make-ready` announcing the turn. John and James handle internal repairs; Victor Rios (A Plus Carpet Cleaning & Repairs) handles carpet work; Isela handles cleaning. Jaime does the QC walk-through. Brooke updates the record to "Complete" and emails the leasing team the unit is available to show.
- **Systems.** Airtable · Slack · Linear · Gmail

## Maintenance response (property-facing)

### `maint_esc_carpet_repair_riobend` — Carpet Damage Escalation to A Plus Carpet
- **Primary actor:** Carlos Mendez (6)
- **Cast:** Carlos Mendez, Elias Navarro, Brooke Phillips, Victor Rios, Tommy Reyes, Teresa Wood, Linda Castillo
- **Storyline.** Tommy Reyes emails Carlos reporting heavy carpet staining and a torn seam in his unit. Carlos triages, escalates to A Plus Carpet Cleaning & Repairs (Victor Rios), coordinates the visit, and once the repair is complete emails Linda Castillo (the owner) a courtesy summary that the charge will appear on her next owner statement.
- **Systems.** Gmail · Slack · Linear · Airtable · QuickBooks

### `maintenance_escalation_waterheater_leak` — Water Heater Leak Escalation
- **Primary actor:** Carlos Mendez (6)
- **Cast:** Tommy Reyes, Carlos Mendez, John Smith, Victor Rios, Brooke Phillips, Linda Castillo
- **Storyline.** Tommy emails Carlos about standing water from a leaking heater that has warped the kitchen vinyl flooring. Carlos escalates for urgent attention. John assesses; Hill Country Plumbing replaces the heater; the flooring vendor repairs the floor. Brooke saves a work-completion report, posts in `#owner-relations`, and emails Linda Castillo with the completion note and pass-through charge.
- **Systems.** Gmail · Slack · Linear · QuickBooks · Airtable

## Fair housing

### `fair_housing_reasonable_accommodation` — Tanya Mitchell ESA Accommodation
- **Primary actor:** Lisa Smith (6)
- **Cast:** Tanya Mitchell, Lisa Smith, Sandra Allen, Brooke Phillips
- **Storyline.** Tanya Mitchell emails Sandra Allen requesting a reasonable accommodation under the Fair Housing Act — she has a disability-related need for an emotional support animal (a cat) in a no-pet unit. Sandra forwards to Lisa; Lisa runs the interactive process, verifies documentation, approves the accommodation. A HubSpot Ticket tracks the case; a lease addendum is executed. Lisa closes the ticket and creates a HubSpot Engagement note documenting the completed interactive process for compliance records.
- **Systems.** Gmail · HubSpot · Airtable · Slack

## Rent lifecycle

### `rent_late_first_notice` — Tanya Mitchell First Late-Rent Notice
- **Primary actor:** Patricia Nguyen (5)
- **Cast:** Patricia Nguyen, Tanya Mitchell, Teresa Wood, Brooke Phillips
- **Storyline.** Patricia reviews the June rent roll and identifies Tanya's rent unpaid past the 5-day grace period. She creates a Maintenance Tickets Airtable record logging the delinquency. Teresa generates a first late-rent notice letter; Patricia emails it. Teresa creates a Google Calendar follow-up for June 20 to check whether payment has been received.
- **Systems.** QuickBooks · Airtable · Gmail · Google Calendar · Slack

### `rent_delinquency_payment_plan` — Second-Month Delinquency + Payment Plan
- **Primary actor:** Patricia Nguyen (5)
- **Cast:** Tanya Mitchell, Patricia Nguyen, Brooke Phillips, Teresa Wood
- **Storyline.** Tanya emails Patricia explaining she has fallen behind for a second consecutive month (May was late; June is past the grace period) and describes ongoing financial hardship. Patricia proposes a three-installment payment plan; Tanya agrees. Patricia emails a final confirmation summarizing the three installment dates, amounts, and total balance, with a note the team will confirm each payment.
- **Systems.** Gmail · QuickBooks · Airtable · Google Calendar

### `rent_3day_notice_pay_or_quit` — 3-Day Notice to Pay or Quit
- **Primary actor:** Patricia Nguyen (7)
- **Cast:** Patricia Nguyen, Tanya Mitchell, Brooke Phillips, Teresa Wood, Linda Castillo
- **Storyline.** Payment plan installment is missed on June 23. Patricia sends a follow-up email; no response. She escalates to the statutory 3-day pay-or-quit notice, coordinated with Teresa on packet formatting. Brooke posts a closing message in `#general` acknowledging the notice is served and deadline tracking is in place. If Tanya doesn't pay or vacate by June 29, Star PM proceeds with eviction filing.
- **Systems.** Gmail · Airtable · Google Calendar · Slack

## Eviction lifecycle

### `eviction_filing_prep` — Eviction Filing Package + Owner Authorization
- **Primary actor:** Patricia Nguyen (4)
- **Cast:** Patricia Nguyen, Brooke Phillips, Linda Castillo, Teresa Wood, Tanya Mitchell, Patricia Lowe (Court Clerk)
- **Storyline.** Morning after the June 29 3-day notice deadline, no payment and no tenant communication. Patricia updates the Airtable tracking record to "Eviction Filing — Prepared." Brooke approves the escalation in `#general`. Teresa generates a consolidated rent ledger from QuickBooks. Patricia assembles the complete eviction filing packet (rent ledger, first late notice, 3-day notice, payment-plan agreement). Owner (Linda Castillo) authorization is obtained. Brooke posts a closing message confirming the packet is complete and the court filing is being coordinated with the Justice of the Peace.
- **Systems.** Airtable · QuickBooks · Gmail · Slack · Google Calendar

### `eviction_court_coordination` — Mitchell Eviction Advances to Court
- **Primary actor:** Patricia Nguyen (3) — tied with Brooke Phillips (3)
- **Cast:** Patricia Nguyen, Brooke Phillips, Teresa Wood, Harry Harris, Patricia Lowe (Court Clerk)
- **Storyline.** Patricia learns from JP Court Clerk Patricia Lowe that a hearing date has been set for the Tanya Mitchell eviction at one of Harry Harris's units. She creates a Linear issue "Eviction Hearing — Mitchell, Harris Property" to track case prep. The case file gets assembled (all prior notices + payment-plan trail + owner authorization). Brooke posts a wrap-up confirming the team is ready for the hearing.
- **Systems.** Linear · Airtable · Gmail · Slack · Google Calendar

---

# Cat 2 — Portfolio Coordination & Owner Relations (10 primary scenarios)

## Cross-portfolio operations sync

### `property_ops_weekly_cycle` — Property Ops Weekly Sync + Board Update
- **Primary actor:** Brooke Phillips (5)
- **Cast:** Brooke Phillips, Lisa Smith, Carlos Mendez, Patricia Nguyen, Teresa Wood
- **Storyline.** Brooke reminds the onsite managers about the mid-week Property Ops sync and asks everyone to update their Linear board issues beforehand. The sync happens; decisions are made (brand-compliant signage vendor, pool-gate standardization). Brooke posts a short recap in `#general` summarizing completions, decisions, and next action items.
- **Systems.** Slack · Linear · Google Calendar

### `summer_makeready_weekly_cycle` — Summer Make-Ready Program Weekly Cycle
- **Primary actor:** Brooke Phillips (5)
- **Cast:** Brooke Phillips, John Smith, Elias Navarro, Jaime Salinas, Carlos Mendez, Lisa Smith
- **Storyline.** Brooke kicks off the week with a status check in `#make-ready`, setting the cadence and prompting maintenance leads to update the Summer Make-Ready Program board. The week runs; QC-passed units get moved to Done. Brooke closes the cycle with a weekly summary — units turned, units in progress, upcoming intake from Lisa's vacancy reports.
- **Systems.** Linear · Slack · Airtable

### `portfolio_ops_preventive_maintenance_push` — Cross-Property Summer Readiness
- **Primary actor:** Brooke Phillips (4)
- **Cast:** Brooke Phillips, Lisa Smith, Carlos Mendez, Patricia Nguyen, John Smith, Jaime Salinas, Teresa Wood
- **Storyline.** Brooke posts in `#maintenance` announcing that the Preventive Maintenance Push (proj_003) is moving into active execution — a portfolio-wide HVAC, plumbing, and electrical audit before peak summer heat. Onsite PMs coordinate access; Patricia reports her cluster's electrical panel inspections are complete. Brooke posts a portfolio-wide status update in `#general` at the mid-initiative check-in.
- **Systems.** Slack · Linear · Google Calendar

## Vendor invoice approval & budget oversight

### `vendor_invoice_aplus_carpet_repair` — A Plus Carpet Invoice → Payment
- **Primary actor:** Carlos Mendez (2), Brooke Phillips (2), Victor Rios (2) — tied; collaborative scenario
- **Cast:** Victor Rios, Carlos Mendez, Brooke Phillips, Teresa Wood, John Smith
- **Storyline.** Carlos creates a Maintenance Ticket for carpet damage too extensive for in-house patching. A Plus Carpet Cleaning & Repairs (Victor Rios) is engaged. The repair completes; Victor sends the invoice. Brooke reviews and approves in QuickBooks; Teresa Wood processes payment; Victor emails Teresa a receipt acknowledgement.
- **Systems.** Airtable · Gmail · QuickBooks · Slack

### `vendor_invoice_landscape_may2026` — Gary Hoffman Landscape Invoice
- **Primary actor:** Teresa Wood (5)
- **Cast:** Gary Hoffman, Lisa Smith, Brooke Phillips, Teresa Wood
- **Storyline.** Gary Hoffman emails his May landscaping service invoice (common-area mowing, edging, tree trimming across Las Palmas and Mesa Vista) to Brooke. Teresa Wood assembles the packet, verifies against the service schedule, gets Brooke's approval, and processes payment. Brooke posts a wrap-up in `#general` noting the vendor has been paid and common areas are ready for summer.
- **Systems.** Gmail · QuickBooks · Slack

### `budget_review_makeready_q2` — Q2 Make-Ready Budget Reconciliation
- **Primary actor:** Brooke Phillips (4)
- **Cast:** Brooke Phillips, Dave Thomas, Lisa Smith, Aurora Winona, Teresa Wood, Carlos Mendez, Patricia Nguyen
- **Storyline.** Brooke flags in `#budget-review` that Summer Make-Ready Program spending is tracking ~18% over Q2 allocation. She asks Lisa, Carlos, and Patricia to compile their property-level cost breakdowns. A Linear issue tracks the reconciliation. Reallocation is decided (June and July turn budgets shift). Brooke moves the Linear issue to Done; Teresa posts a wrap-up confirming the revised allocations.
- **Systems.** Slack · Linear · QuickBooks · Airtable

## Owner reporting & CapEx

### `owner_monthly_report_review` — May Monthly Owner Report (Finley)
- **Primary actor:** Brooke Phillips (7)
- **Cast:** Brooke Phillips, Robert Finley, Lisa Smith, Teresa Wood
- **Storyline.** Brooke announces in `#owner-relations` that month-end owner reports are due; she begins compiling Robert Finley's May Mesa Vista report. Lisa submits property-level occupancy numbers and rent collection. Teresa assembles the packet. Brooke reviews and sends. Robert responds with a follow-up question about a vacant Mesa Vista unit; Brooke relays that the make-ready is on track and leasing is scheduling showings.
- **Systems.** Slack · Gmail · QuickBooks · Airtable · Google Calendar

### `owner_portfolio_review_midyear` — Mid-Year Owner Portfolio Review
- **Primary actor:** Brooke Phillips (4)
- **Cast:** Brooke Phillips, Teresa Wood, Aurora Winona, Lisa Smith, Patricia Nguyen
- **Storyline.** Brooke posts in `#owner-relations` announcing mid-year portfolio reviews for all four owners (Harry Harris, David Shea, Linda Castillo, Robert Finley) and creates a parent Linear tracking issue. Teresa assembles the packets. Meetings get scheduled. Brooke moves the parent issue to In Review and posts wrap-up confirming all four reviews are scheduled and materials are ready for Aurora Winona's sign-off before the first meeting.
- **Systems.** Slack · Linear · Google Calendar · Gmail

### `owner_capex_approval_roof` — Roof Repair Escalation + Owner Approval
- **Primary actor:** Brooke Phillips (8)
- **Cast:** Brooke Phillips, Robert Finley, Lisa Smith, John Smith, Pete Donovan, Teresa Wood
- **Storyline.** Lisa notices missing shingles and water staining on ceilings in a top-floor unit at one of Robert Finley's Ridgeview properties. She creates a Maintenance Ticket flagging the roof as needing professional evaluation. Brooke coordinates the CapEx approval: gets two vendor quotes, packages the memo to Robert with recommended path and timeline, holds the approval call. Robert approves. The vendor bill is created in QuickBooks; the repair cost is passed through as an owner charge invoice.
- **Systems.** Airtable · Linear · QuickBooks · Gmail · Google Calendar · Slack

### `preventive_maintenance_push_routine` — Preventive Maintenance Weekly Cycle
- **Primary actor:** Brooke Phillips (3)
- **Cast:** Brooke Phillips, John Smith, Elias Navarro, Tony Reyes, Carlos Mendez, Jaime Salinas
- **Storyline.** Brooke creates several Linear issues under proj_003 assigning HVAC filter replacements and smoke detector battery checks across the portfolio to John, Elias, and Tony Reyes. Execution runs. Jaime does a QC spot-check on finished HVAC filter replacements and moves the completed-work Linear issue to In Review, commenting that all units passed with no rework needed. The scenario is coordinated from the portfolio-supervisor level; execution threads through the Cat 4 maintenance team.
- **Systems.** Linear · Slack

---

# Cat 4 — Maintenance & Repairs (2 primary scenarios)

### `maintenance_hvac_elias` — Preventive HVAC Summer Service Push
- **Primary actor:** Elias Navarro (8)
- **Cast:** Elias Navarro, Brooke Phillips, Tony Reyes, Carlos Mendez, Jaime Salinas, Wesley Tran
- **Storyline.** Brooke posts in `#maintenance` announcing the summer preventive HVAC service push (coil cleaning, refrigerant checks, filter swaps portfolio-wide before peak heat), designating Elias as lead coordinator. Elias creates Linear issues under proj_003 for each property cluster (South, East, North) and posts the two-week rolling schedule. Carlos confirms tenant access notices for the first batch. Execution runs; Elias posts a wrap-up summary — units serviced, recurring issues noted (two condensate drain clogs, one compressor flagged for monitoring). Brooke replies acknowledging completion.
- **Systems.** Linear · Slack · Google Calendar

### `makeready_turn_lasvistas_9d` — Las Vistas 9D Make-Ready Turn
- **Primary actor:** John Smith (5)
- **Cast:** Lisa Smith, Brooke Phillips, John Smith, Jaime Salinas, Randy Jones, Isela Juarez, Victor Rios, Sandra Allen
- **Storyline.** Lisa confirms tenant move-out on May 5 and creates a Make-Ready Turn record with status "Vacant — Needs Assessment" and a preliminary scope (paint touch-ups, carpet cleaning, minor repairs). John and the team execute the scope; Randy pulls the old appliance during the turn; Jaime does the QC pass; Brooke updates the record to "Rent Ready" on May 21 and posts completion. Lisa hands off to Sandra for showing. John leads the maintenance execution side, which is why this make-ready sits in Cat 4 rather than Cat 1.
- **Systems.** Airtable · Slack · Linear · Gmail

---

# Cat 5 — Leasing & Applicant Intake (5 primary scenarios)

### `lease_inquiry_delgado_referral` — Tasha Wentworth Refers Marcus Delgado
- **Primary actor:** Sandra Allen (7)
- **Cast:** Marcus Delgado, Tasha Wentworth, Sandra Allen, Lisa Smith, Brooke Phillips
- **Storyline.** Tasha Wentworth (referral partner) emails Sandra referring Marcus Delgado for a 2BR near Las Palmas or Rio Bend, early-June move-in. Sandra opens a HubSpot deal, schedules a tour, processes the application, and drives it through screening and lease signing. The signed lease is filed and the deal closes as won.
- **Systems.** Gmail · HubSpot · Google Calendar · Airtable · Slack

### `leasing_application_to_movein` — Angela Carter Approval-to-Move-In
- **Primary actor:** Sandra Allen (4)
- **Cast:** Angela Carter, Sandra Allen, Lisa Smith, Alicia Vega
- **Storyline.** Sandra advances Angela's application to `decisionmakerboughtin` and emails move-in logistics. Lease is executed. On move-in day, Lisa conducts the unit walkthrough with Angela, documents the condition on a move-in inspection form. Keys are handed over; HubSpot deal advances to `closedwon`; move-in coordination Ticket is closed.
- **Systems.** HubSpot · Gmail · Airtable · Google Calendar

### `rental_app_priya_nambiar` — Priya Nambiar Referral Application via Jerome Okafor
- **Primary actor:** Sandra Allen (7)
- **Cast:** Priya Nambiar, Jerome Okafor, Sandra Allen, Kevin Okafor, Lisa Smith, Brooke Phillips
- **Storyline.** Jerome Okafor (Apartment Locator Central) emails Sandra referring Priya for a 2BR unit. Sandra creates a HubSpot contact, logs the referral source linked to Apartment Locator Central, and opens a deal. Kevin confirms unit availability. Sandra runs the application through document verification and screening. On approval, Sandra posts the move-in confirmation in `#applications` with the move-in date, unit number, and key-pickup instructions. The deal closes as won; Sandra emails Jerome a referral-closed confirmation.
- **Systems.** HubSpot · Gmail · Slack · Airtable · Google Calendar

### `lease_renewal_offer_standard` — Tommy Reyes Renewal Offer + Signing
- **Primary actor:** Alicia Vega (6) — **NPC-led scenario**; the persona voice for a task of this shape would be Kevin Okafor
- **Cast:** Alicia Vega, Tommy Reyes, Carlos Mendez, Brooke Phillips
- **Storyline.** Alicia (NPC Leasing Agent) identifies Tommy Reyes's lease ending June 30 and posts in `#leasing` alerting the team, tagging Carlos to confirm unit condition and reliability. Carlos confirms; Alicia drafts the standard renewal offer at a modest bump and sends. Tommy signs. The executed renewal lease is filed as of July 1; the HubSpot deal closes as won; Airtable tenant record is updated.
- **Systems.** HubSpot · Gmail · Slack · Airtable

### `lease_renewal_declined_to_moveout` — Connor Beaumont Non-Renewal + Move-Out
- **Primary actor:** Kevin Okafor (6)
- **Cast:** Kevin Okafor, Connor Beaumont, Denise Morales, Brooke Phillips, Tony Reyes, Robert Finley
- **Storyline.** Kevin identifies Connor Beaumont's lease at a Mesa Vista property expiring June 30. He creates a HubSpot contact, opens a deal at `appointmentscheduled` to track renewal outreach, logs a note documenting the lease-end context. Connor declines the renewal (moving out of the region). Denise coordinates the move-out inspection walkthrough on June 27 — unit in fair condition with normal wear (carpet needs professional cleaning, minor wall scuffs, appliance dust). Denise posts confirmation in `#leasing`; the HubSpot deal closes as lost.
- **Systems.** HubSpot · Gmail · Airtable · Slack · Google Calendar

---

## Scripted-footprint summary

| Category | Scenarios owned | Primary personas |
|---|---:|---|
| Cat 1 · Property Operations | 10 | Carlos Mendez (4) · Patricia Nguyen (5) · Lisa Smith (1) |
| Cat 2 · Portfolio Coord & Owner Relations | 10 | Brooke Phillips (8) · Teresa Wood (1) · collaborative (1) |
| Cat 3 · QC & Field Services | 0 | Jaime Salinas participates broadly but never leads; Randy Jones is design-surface |
| Cat 4 · Maintenance & Repairs | 2 | Elias Navarro (1) · John Smith (1) |
| Cat 5 · Leasing & Applicant Intake | 5 | Sandra Allen (3) · Kevin Okafor (1) · Alicia Vega NPC (1) |

Total: 27 scripted scenarios covering every business function except Cat 3 (Jaime participates broadly across make-ready and PM scenarios as the QC anchor but never leads).
