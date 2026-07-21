# **Star Property Management — An In-Task Universe**

## **The short version**

Star Property Management is a residential property manager in the Southwest Texas region, running approximately 10 apartment properties on behalf of individual owners (David Shea, Robert Finley, Linda Castillo, Harry Harris, Gary Hoffman, and Dave Thomas among them). Star PM doesn't own the buildings — it manages them, covering operating budgets, leasing and applicant intake, make-ready turnovers, maintenance (HVAC, plumbing, carpet, exterior), rent collection and eviction, fair housing accommodations, and owner relations. A ~45-person onsite team is supervised centrally by a small portfolio-operations tier.

The universe leans into real property-management machinery — make-ready cycles at the operational heart of the business, HVAC compressor failures that are life-safety territory in the Texas summer, statutory rent-notice windows that ladder into court-filed evictions, and a monthly cadence of owner reporting. It's a **smaller, denser** universe than the accounting-heavy ones, but the cross-service threading is tight — a make-ready turn realistically touches Airtable + Slack + Linear + Gmail + QuickBooks all at once. Universe "today" is **2026-07-01** (America/Chicago).

## **By the numbers**

| Dimension | Star PM |
| :---- | :---- |
| Cast | **13 authoring personas + 47 NPCs** (owners, tenants, applicants, referral partners, specialty vendors, code compliance inspector, court clerk) |
| Portfolio | **~10 apartment properties**, populated at unit-level for Las Palmas, Las Vistas, Mesa Vista, Rio Bend, and Ridgeview |
| Pre-built scenarios | **27** — spanning make-ready, maintenance, rent collection, eviction, fair housing, leasing, renewals, owner reporting, and CapEx approval |
| Task categories | **5 flat business functions** — Property Operations · Portfolio Coordination & Owner Relations · Quality Control & Field Services · Maintenance & Repairs · Leasing & Applicant Intake |
| Time range (active workflow) | 2026-05-01 → 2026-07-01 (2-month window, America/Chicago) |
| Services | **8** — Airtable · Contacts · Google Calendar · Gmail · HubSpot · Linear · QuickBooks · Slack |
| Location | Southwest Texas · email domain `starpm.com` · timezone America/Chicago |

## **The systems Star PM runs on**

Four services do the heavy lifting:

- **QuickBooks** — the accounting layer, and the *heaviest single service* in the universe. Vendor bills, owner distributions, budget-vs-actual, tenant rent invoices, delinquency ledger. Distinctive vs the other universes: most treat accounting as a supporting layer; here it's a primary surface.
- **Airtable** — workflow tracking. The `Make-Ready Turns` table is the source of truth for every unit turnover (move-out date, scope-set status, vendor assignments, QC sign-off); the `Maintenance Tickets` table complements Linear on the property-visible ticket side.
- **Slack** — internal coordination, 8 channels: `#make-ready`, `#maintenance`, `#leasing`, `#applications`, `#vendors`, `#owner-relations`, `#budget-review`, `#general`.
- **Linear** — the maintenance ticket system across three projects (Property Ops, Summer Make-Ready Program, Preventive Maintenance Push). Repair queues, PM cycles, HVAC escalations.

Three more services round out the layer:

- **Gmail** — external correspondence (tenants, owners, vendors, applicants) and internal handoffs. Also carries application document attachments in leasing threads.
- **HubSpot** — leasing CRM. Applicants and tenants as contacts, deals for each leasing lifecycle stage, associations to owner LLCs.
- **Google Calendar** — tour scheduling, vendor visits, PM cycles, owner meetings, court dates, ops sync. Includes forward-scheduled events through mid-July.

And one light surface:

- **Contacts** — persona + external-contact directory (~60 entries covering owners, tenants, vendors, referral partners).

*(Note: this universe has no filesystem MCP service. Application documents, inspection reports, and screening notes flow through Gmail attachments, HubSpot notes, or Airtable record fields. The `Data/Files/` folder contains read-only reference PDFs — contracts, invoices, and reports — that the agent can read directly during task execution. CBs never edit these files.)*

## **What carries over**

This is the same project framework you've been working in, with the latest rubric conventions:

- **Rubrics (V3).** Two categories only: **Outcome** (mandatory — the default training signal) and **Process** (optional — only when a necessary behavior can't be captured by a stronger Outcome rubric). Outcome has three sub-types — **1.1** write-action results, **1.2** action content, **2.1** key facts in the final response. Default to making Outcomes stricter rather than reaching for Process.
- **Phrasing convention.** Every rubric reads as a behavior of *the Agent* — *"The Agent updates the Make-Ready Turns record for Unit 9D…"* rather than *"The Make-Ready Turns record was updated."* No tool names in rubrics or prompts.
- **Same prompt rules.** No pre-solving, no command lists, no bolting, natural language throughout, agent must fail on some rubrics.
- **Same spec-quality dimensions we evaluate against:** unique ground truth, feasibility, cross-service requirement, coherence, persona match, business function, universe feasibility, OE completeness/accuracy, rubric quality thresholds, category balance, failure rate.
- **Same three fields per rubric:** criterion + justification + evidence.

## **What's distinctive about Star PM**

- **A broad lifecycle beyond pure ops.** Beyond make-ready and maintenance, the universe carries a full rent-to-eviction ladder (first late notice → payment plan → 3-day pay-or-quit → filing → court coordination with Court Clerk Patricia Lowe), a leasing lifecycle from inquiry through renewal-or-move-out, and CapEx approval flows with owners.
- **Persona footprint varies widely.** Brooke Phillips is in 26 of 27 scenarios (deeply rooted); Carlos Mendez, Patricia Nguyen, Teresa Wood, and Lisa Smith each anchor 7-13 scenarios; Randy Jones, Denise Morales, and James Bennett are design-surface (thin scripted footprint — author from the shape of the role).
- **Some NPCs carry scripted actions.** Alicia Vega, Tony Reyes, Wesley Tran, and Isela Juarez execute inside scenarios. Authoring stays persona-only, but tasks can hand off to or reconcile with NPC-driven work.
- **QuickBooks is unusually heavy.** The biggest single service surface — cash cycles, vendor bills, owner distributions, and tenant rent invoices dominate the operational data.
- **Texas-specific operational context.** HVAC failures in Southwest Texas summer are life-safety events. Rent-notice timing runs on state-mandated windows. Code compliance is enforced by external inspectors (Barry Sanderson NPC).
- **Tight cross-service threading.** Every artifact tends to matter — a make-ready task will realistically touch Airtable + Slack + Linear + Gmail + QuickBooks in one flow; a rent-collection task threads QuickBooks + Gmail + Airtable + Calendar.

## **The personas you'll see most often**

Six personas anchor most of the scripted work:

| Name | Title | Scenarios | Best for |
| :---- | :---- | ----: | :---- |
| **Brooke Phillips** | Apartment Property Supervisor | 26 | Cross-portfolio coordination, vendor invoice approval, budget oversight, owner reporting, CapEx memos, escalation authority |
| **Teresa Wood** | Executive Secretary | 14 | Owner-side calendaring, packet assembly, vendor-invoice packet formatting, executive correspondence |
| **Lisa Smith** | Onsite Property Manager | 13 | Property-level make-ready coordination, fair housing accommodations, tenant support |
| **Carlos Mendez** | Onsite Property Manager | 12 | Make-ready turnovers, tenant-facing maintenance response, day-to-day onsite operations |
| **Patricia Nguyen** | Onsite Property Manager | 9 | Rent collection lifecycle, eviction filing and court coordination |
| **John Smith** | Lead Maintenance Technician | 8 | Ticket triage, preventive maintenance rounds, vendor dispatch |

Three more with a signature scenario block:

| Name | Title | Scenarios | Best for |
| :---- | :---- | ----: | :---- |
| **Jaime Salinas** | Quality Control Inspector | 7 | Post-scope QC walk-throughs, punch-list validation, sign-off before re-leasing |
| **Sandra Allen** | Leasing Agent | 5 | Inquiry response, tour scheduling, application processing, screening |
| **Elias Navarro** | Lead Maintenance Technician | 4 | HVAC escalations, compressor-scale repairs, vendor sign-off |
| **Kevin Okafor** | Leasing Agent | 2 | Lease renewals, retention outreach |

Three personas — **James Bennett** (Assistant Maintenance), **Randy Jones** (Appliance & Bulk-Item Retrieval), and **Denise Morales** (Onsite Property Manager) — are eligible authoring seats with thin scripted footprint. Tasks written for them are author-from-spec, anchored on the shape of their real-world roles.

## **Where to dig deeper**

The full Star PM doc set:

- [**01 · Summary**](01_StarPM_SUMMARY.html) — Universe overview, cast, systems, scenario inventory
- [**02 · Persona Briefs**](02_StarPM_PERSONA%20BRIEFS.html) — Per-persona detail for all 13 (voice, systems, signature scenarios)
- [**03 · Task Categories**](03_StarPM_TASK%20CATEGORIES.html) — 5 business functions, 16 subcategories, 100-task distribution, worked example prompts
- [**04 · Scenario Storylines**](04_StarPM_SCENARIO%20STORYLINES.html) — Per-scenario detail for all 27
- [**05 · Artifacts**](05_StarPM_ARTIFACTS.html) — Systems catalog with table schemas and cross-service threading
- [**06 · Glossary**](06_StarPM_GLOSSARY.html) — Terms specific to Star PM and the task-authoring framework
