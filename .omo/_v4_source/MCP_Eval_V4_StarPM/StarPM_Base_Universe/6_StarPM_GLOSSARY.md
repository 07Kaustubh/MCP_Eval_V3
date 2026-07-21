# Star Property Management — Glossary

Terms specific to Star PM and to the task-authoring framework. Grouped by topic. When in doubt about a word in the doc set, look here first.

---

## Roles

**Onsite Property Manager (Onsite PM).** The persona who runs a single property day-to-day. Owns turnovers, tenant coordination, maintenance triage, and property-level operations at their assigned property. Four Onsite PM personas in Star PM: Lisa Smith, Carlos Mendez, Patricia Nguyen, Denise Morales.

**Apartment Property Supervisor.** Portfolio-tier supervisor over all Onsite PMs. Coordinates cross-portfolio operations, approves vendor invoices, oversees budgets, handles owner reporting, drives CapEx approval flows. Brooke Phillips is the Supervisor.

**Executive Secretary.** Admin-support persona sitting inside the executive office (Aurora Winona's tier). Handles owner-side calendaring, packet assembly, vendor-invoice packet formatting, and executive correspondence. Teresa Wood.

**Lead Maintenance Technician (Lead Tech).** Senior-tier maintenance persona. Owns ticket triage, dispatch, diagnosis, and hands-on repair. Two Leads: John Smith (general) and Elias Navarro (HVAC-heavy).

**Assistant Maintenance Technician.** Junior-tier maintenance persona. Executes tickets under a Lead's direction — routine repairs, tenant-facing appointments, second-hand support during turns. James Bennett.

**Quality Control Inspector (QC Inspector).** Cross-portfolio specialty role. Walks units after the maintenance team declares work complete, validates the punch-list, signs off on marketing-ready status or kicks work back. Jaime Salinas.

**Appliance & Bulk-Item Retrieval Specialist.** Cross-portfolio field role. Pulls old appliances during move-out, delivers replacements during scope-set, hauls bulk waste and abandoned items. Randy Jones.

**Leasing Agent.** Handles the leasing lifecycle — inbound inquiry through tour, application, screening, lease signing, move-in coordination, and renewals. Sandra Allen (intake anchor) and Kevin Okafor (renewal anchor).

**Referral partner / apartment locator.** External NPCs who refer prospective tenants to Star PM in exchange for a commission on signed leases. Represented by NPCs like Tasha Wentworth, Jerome Okafor, Craig Pemberton, etc. — most work through Apartment Locator Central.

**Property Owner.** External NPC who owns one or more of the ~10 properties Star PM manages. Six owners on file (David Shea, Robert Finley, Linda Castillo, Harry Harris, Gary Hoffman, Dave Thomas). Star PM invoices them for management fees and passes through repair costs; owners approve CapEx requests.

**Court Clerk.** External NPC at the Justice of the Peace court where Star PM files evictions. Patricia Lowe is the Court Clerk contact.

**Code Compliance Inspector.** External NPC representing the local code enforcement office. Sends violation notices; Star PM tracks and remediates. Barry Sanderson.

---

## Workflow terms

**Make-Ready Turn.** The full lifecycle of turning a vacated unit into a re-leasable unit. Move-out inspection → scope-set → punch-list creation → vendor scheduling → maintenance execution → QC handoff → marketing-ready sign-off. Tracked in the Airtable `Make-Ready Turns` table.

**Punch list.** The itemized scope of work required to turn a specific unit — paint touch-ups, appliance swaps, carpet cleaning, deep clean, fixture replacements. Documented after the move-out walk-through.

**Scope-set.** Milestone in the make-ready workflow — the point at which the full scope of work is defined, vendors are booked, and the turn moves from "Vacant — Pending Inspection" into active execution.

**QC walk-through.** The Quality Control inspection that happens after the maintenance team declares work complete. Jaime walks the unit against the punch-list and either signs off ("QC Approved — Marketing Ready") or kicks work back ("Needs Rework") with specific observations.

**Marketing-ready.** The final make-ready state — unit has passed QC and is available for leasing to show and lease.

**Preventive Maintenance (PM) cycle.** The scheduled maintenance cadence, distinct from reactive tickets — HVAC coil cleaning, filter changes, water-heater flushes, exterior touch-ups. Runs on a cadence set by Brooke; executed by the maintenance team; tracked as Linear issues under `proj_003` (Preventive Maintenance Push).

**Ticket triage.** The Lead Tech's routing decision on an incoming maintenance ticket — assess urgency, dispatch to internal tech (James) or external vendor (Alamo HVAC, Hill Country Plumbing, etc.), escalate to Brooke if it crosses a spend or judgment threshold.

**Escalation.** A ticket or workflow that moves up the chain — from tenant to Onsite PM, from Onsite PM to Lead Tech, from Lead Tech to Brooke, from Brooke to Owner or Executive. HVAC compressor failures and water-heater full replacements typically escalate.

**CapEx (Capital Expenditure).** Owner-approved spend that crosses the routine-maintenance threshold — roof repairs, HVAC system replacements, exterior renovations, structural work. Requires an owner-facing memo with vendor quotes before commit. Brooke drives the CapEx approval flow.

**Owner statement / owner report.** Monthly performance summary sent to each property owner — occupancy, rent collection, expenses, vendor-invoice pass-throughs. Brooke leads the monthly reporting cycle; Teresa Wood assembles the packet.

**Mid-year portfolio review.** Semi-annual owner meeting covering strategic and operational review of the full portfolio. Anchored in `owner_portfolio_review_midyear`.

---

## Leasing terms

**Inquiry.** Inbound lead from a prospective tenant (via web form, email, referral partner, or apartment-locator introduction). The top-of-funnel stage in HubSpot.

**Tour.** Scheduled unit showing on Google Calendar. Leasing Agent walks the applicant through the unit.

**Application.** Applicant submits their rental application with documents (ID, income verification, prior-residence letter). Documents arrive as Gmail attachments (no filesystem in this universe).

**Screening.** Third-party background and credit check on the applicant. Result determines approval or denial.

**Deal stage progression.** HubSpot pipeline: `appointmentscheduled` → `presentationscheduled` → `qualifiedtobuy` → `decisionmakerboughtin` → `contractsent` → `closedwon` (or `closedlost` on decline).

**Renewal window.** The 60-day period before a lease expires when Star PM sends the renewal offer. Kevin Okafor anchors the renewal outreach.

**Non-renewal / decline-to-move-out.** When a tenant declines the renewal offer and moves out. Triggers move-out inspection and returns the unit to make-ready.

**Referral commission.** Payment Star PM sends to a referral partner when a referred lead signs a lease. Referral partners are QuickBooks vendors (Star PM pays them), not customers.

---

## Rent & eviction terms

**Rent roll.** The list of tenants and their monthly rent obligations. Patricia Nguyen reviews the rent roll monthly to identify delinquencies.

**Grace period.** The number of days after the rent due date before a late-payment notice is required. Star PM uses a 5-day grace period.

**First late-rent notice.** The initial formal notice sent to a tenant after their rent is past the grace period. Anchored in `rent_late_first_notice`.

**Payment plan.** Structured repayment arrangement negotiated with a delinquent tenant, typically 2–3 installments over a defined window. Documented in Gmail and updated in QuickBooks. Anchored in `rent_delinquency_payment_plan`.

**3-day pay-or-quit notice.** The statutory notice sent when a payment-plan installment is missed or a delinquency crosses a specific threshold. The tenant has 3 days to pay in full or vacate before eviction filing. Anchored in `rent_3day_notice_pay_or_quit`.

**Eviction filing packet.** The compiled document set required to file an eviction with the Justice of the Peace court — rent ledger, first late notice, payment-plan agreement (if any), 3-day pay-or-quit notice, owner authorization. Teresa Wood assembles the packet; Patricia Nguyen files. Anchored in `eviction_filing_prep`.

**Court coordination.** Communication with the Justice of the Peace Court Clerk (Patricia Lowe) to schedule the eviction hearing and confirm the case file. Anchored in `eviction_court_coordination`.

**Owner authorization.** Written approval from the property owner to proceed with eviction filing. Required before filing.

**Pass-through charge.** A repair or make-ready cost that Star PM pays to a vendor and then invoices to the property owner. Common in maintenance escalations; documented in QuickBooks as a bill (Star PM pays vendor) + invoice (Star PM bills owner).

---

## Fair housing terms

**Reasonable accommodation.** A modification to a policy, unit, or process to accommodate a tenant's disability under the Fair Housing Act — e.g., emotional support animal in a no-pet unit, ground-floor transfer for a mobility limitation, grab-bar installation. Anchored in `fair_housing_reasonable_accommodation`.

**Interactive process.** The dialogue between the tenant, the property manager, and (when needed) medical/legal parties to determine what accommodation is appropriate. Legally required — must be documented.

**Documentation-of-need.** The tenant's supporting documentation for the accommodation request — typically a letter from a medical provider or licensed professional. Reviewed by the Onsite PM (Lisa in the anchored scenario).

**Lease addendum.** An amendment to the existing lease documenting the accommodation (e.g., ESA addendum). Filed with the executed lease documents.

---

## Framework terms

**Business Function.** One of the 5 categories in this universe (Property Operations, Portfolio Coord & Owner Relations, QC & Field Services, Maintenance & Repairs, Leasing & Applicant Intake). Every persona has exactly one home Business Function.

**Persona.** An authoring seat — a named individual whose voice tasks are written from. Star PM has 13 personas. Contrast with **NPC**.

**NPC.** A named individual in the universe who is *never* an authoring seat — tenants, applicants, owners, external vendors, referral partners, and select Star PM staff figures who exist as cast but not as task voices.

**Design-surface persona.** A persona whose scripted footprint is thin (0 or 1 scripted actions). Tasks written for them are author-from-spec — anchored on the shape of the role, not on a specific scripted arc. Randy Jones, Denise Morales, and James Bennett are design-surface in the current universe.

**Scripted action.** A single step performed by a named actor inside a scenario. In the scenario yaml, each beat has an `actor` field; the actor's total scripted-action count across all scenarios is their rooting depth. (This term replaces "beat" in user-facing writing.)

**Scenario anchor.** A scripted scenario that grounds a specific workflow — e.g., `maintenance_hvac_elias` is the anchor for HVAC-escalation task authoring. Tasks are often anchored to the shape of a specific scenario.

**Author-from-spec.** Writing a task from the shape of a persona's role rather than from a specific scripted scenario. Used for design-surface personas and for subcategories that lack a scripted anchor.

**Signature scenario.** A scenario where a persona leads by scripted-action count — their strongest home ground.

**Cast.** The named participants in a scenario. Personas and NPCs both appear in cast lists; only personas can be the primary actor for authoring purposes.

**Primary actor.** The persona (or occasionally NPC) with the most scripted actions in a scenario — the "lead" of the storyline.

---

## Rubrics V3 terms

**Rubric.** A single criterion an agent's task response is graded on. Each rubric has three fields: criterion + justification + evidence.

**Outcome rubric.** The mandatory rubric category — what the agent should have *done*. Three sub-types: 1.1 write-action results, 1.2 action content, 2.1 key facts in the final response.

**Process rubric.** Optional rubric category — how the agent should have gone about the task. Only used when a necessary behavior can't be captured by a stronger Outcome rubric.

**Agent-centric phrasing.** The Rubrics V3 convention that every rubric reads as a behavior of *the Agent* — *"The Agent updates the Make-Ready Turns record for Unit 9D…"* — never as passive voice.

**Ground truth.** The unambiguous, verifiable correct answer for a rubric criterion. Every Outcome 2.1 rubric requires a specific ground-truth fact that can be checked against the universe data.

**Persona match.** The spec-quality dimension that a task's voice, tone, and workflow shape match its authoring persona's home Business Function and communication traits.

**Universe feasibility.** The spec-quality dimension that a task's ground-truth answer is actually derivable from the universe data — every artifact referenced exists, every date is inside the window, every persona/NPC referenced is in the cast.

---

## Terms this doc set explicitly does *not* use

**"Beat" / "beats."** Internal yaml field name — the underlying data structure calls these "beats." User-facing docs use "scripted action" instead because "beat" reads opaque to CBs.

**"Mock" (as part of a service name).** Service display names in this doc set are "Airtable," "QuickBooks," "Slack," etc. — the "Mock" suffix is dropped from display but retained in tool identifiers (`airtable_mock_list_records`, `quickbooks_mock_get_bill`, etc.).

**"Filesystem."** There is no filesystem MCP service in this universe. Documents that would live on disk in other universes travel as Gmail attachments, HubSpot notes, or Airtable record fields here. The `Data/Files/` folder contains read-only reference PDFs (contracts, invoices, reports) the agent reads directly — these are universe data, not an editable filesystem.
