# **MoveOps Inc. — An In-Task Universe**

## **The short version**

MoveOps Inc. is a B2B remote-work relocation startup based in San Francisco. Founded in 2019 as a boutique luxury travel agency, the company nearly went bankrupt during the pandemic and pivoted into helping tech companies relocate employees — sourcing long-term apartments, booking flights, coordinating moving vendors, and managing home-office equipment stipends through a proprietary platform. Today the firm runs at about 21 employees across six departments (Executive, Finance, Customer Engagement, Operations, Engineering, Customer Support), serving a portfolio of six core client companies plus one onboarding, two at-risk accounts, and a wider prospect pipeline.

The universe is built around real operational and relationship machinery — a six-vendor logistics ecosystem (UrbanNest, Heartland Movers, Swift Relocations, Atlas Corporate Travel, KeyMove Specialty Transport, Road Runner Auto Transport), recurring monthly invoicing rhythms, an in-flight DOT/PHMSA hazmat compliance audit, a misfiring auto-categorization tool, a wave of complex April relocations (visa cases, ADA, ESA, lab equipment, vehicle shipping), and a real client churn crisis. The depth comes from cross-system threading, not from invented complexity.

Today inside the universe is **2026-04-26**.

## **By the numbers**

| Dimension | MoveOps |
| :---- | :---- |
| Employees | **21 across 6 departments** (Executive, Finance, CE, Ops, Engineering, CS) |
| Active client portfolio | **6 core + 2 at-risk + 1 onboarding** + a wider prospect pipeline |
| Pre-built scenarios | **27** (bulk client relocations, service-recovery & crisis cases, strategic/operational threads) |
| Task categories | **5 business functions** (Operations 25%, CE/Support 30%, Engineering 20%, Finance 15%, Executive 10%) |
| Total artifact volume | **1,705 entries across 8 services** |
| Headquarters | San Francisco, CA · email domain `moveops.com` |

## **The systems MoveOps runs on**

Four services do the heavy lifting — they hold the operational state of record:

- **CRM** (242 entries) — front-of-funnel pipeline and ongoing relationship management. 88 contacts, 71 companies, 44 deals (including the at-risk Vectral renewal, the dropped Ridgeline Robotics referral, and the Terraform Digital onboarding), 23 leads, 16 engagements. Deal stage transitions and engagement notes are where client health and decisions get recorded.

- **Email** (494 messages) — primary external comms. Every client request, vendor confirmation, escalation thread, and partner sign-off lives here. Threads cross-link to CRM engagements and Linear tickets.

- **Slack** (354 messages across 9 channels) — internal coordination. Channels: `#general`, `#customer-engagement`, `#engineering`, `#executive`, `#finance`, `#operations`, `#customer-support`, `#announcements`, plus `#root-cause-aws-spike` (spun up during the AWS cost spike investigation).

- **Airtable** (167 records across 3 tables) — operational tracking. **Relocations** (63 records) is the source of truth for every employee move; **Stipend Transactions** (33 records) holds home-office expense submissions with approval status and receipt hashes; **Client Accounts** (69 records) maps clients to their assigned account managers with relationship details.

Three more services round out the workflow + financial layer:

- **Linear** (182 entries — 69 issues across 8 projects, 3 teams) — systemic-issue tracking. Projects include the Expense Auto-Categorizer Engine, the DOT Compliance Audit (Q1/Q2 2026 hazmat shipments), and per-client relocation projects (`proj_brightloop`, `proj_canopy`, `proj_mosaic`, `proj_vectral`, etc.). Key clusters: ExpenseBot pilot remediation, stipend duplicate detection (ENG-220), DOT documentation gaps, vendor reconciliation.

- **QuickBooks** (112 entries) — bookkeeping ledger. 15 customers, 16 vendors, 35 invoices, 17 bills, 7 accounts. Holds the big liability accruals — the **$90K Mosaic prototype damage liability**, the **$50K DOT penalty contingent liability**, and the **$12,800 Heartland Movers payment hold**.

- **Contacts** (119 entries) — address book for the 21 personas plus all external client/vendor contacts.

And one lighter service:

- **Calendar** — service exists but the snapshot is empty (0 events). Calendar-anchored tasks (kickoff scheduling, executive briefings) seed their own events rather than querying existing ones.

## **What carries over**

This is the same project framework you've been working in, with the latest rubric conventions:

- **Rubrics (V3).** Two categories only: **Outcome** (mandatory — the default training signal) and **Process** (optional — only when a necessary behavior can't be captured by a stronger Outcome rubric). Outcome has three sub-types — **1.1** write-action results, **1.2** action content, **2.1** key facts in the final response. Default to making Outcomes stricter rather than reaching for Process.
- **Phrasing convention.** Every rubric reads as a behavior of *the Agent* — *"The Agent sends an email to chloe.vance@…"* rather than *"An email was sent to Chloe."* No tool names in rubrics or prompts.
- **Same prompt rules.** No pre-solving, no command lists, no bolting, natural language throughout, agent must fail on some rubrics.
- **Same spec-quality dimensions we evaluate against:** unique ground truth, feasibility, cross-service requirement, coherence, persona match, business function, universe feasibility, OE completeness/accuracy, rubric quality thresholds, category balance, failure rate.
- **Same three fields per rubric:** criterion + justification + evidence.

## **What's new for task design**

A few things make MoveOps distinctive in ways worth knowing up front:

- **Smaller, denser universe.** 1,705 entries across 8 services — far lighter than the accounting-heavy universes. Every artifact tends to matter, and the cross-service threading is tight. An agent reading just email + Slack will miss half the story; the actual state of work lives in CRM, Airtable, Linear, and QuickBooks.

- **No NPCs.** MoveOps has no enumerated NPC roster. Every named character is either one of the 21 personas, or a *named external contact* who appears inside scenarios — client HR leads (Patricia Langford at Canopy, Rachel Whitfield at Vectral, Tessa Moreno at BrightLoop, Pam Kowalski at NorthWind), client employees being relocated (Dr. Mehta, Noah Fitzpatrick, Raj Patel, Keiko Tanaka), vendor reps (Greg Pallone at Swift, Jake Loomis at Heartland, Carmen Reyes at UrbanNest), and a few regulators (Linda Castellano at DOT/PHMSA). They exist inside scenarios but never author tasks.

- **Categories are weighted, not credentialing-tagged.** Each of the 5 business functions has a target percentage of total tasks — Operations 25%, Customer Engagement/Support 30%, Engineering 20%, Finance 15%, Executive 10%. None require special credentials; categories route by *what the work is*.

- **27 scenarios, deeply cross-referenced.** Many scenarios sit on top of each other — the Mosaic damage claim (`damage_claim`) ties back to the original `bulk_mosaic` move; the Vectral renegotiation (`contract_renegotiation`) cites the ExpenseBot fiasco; the StormCloud failure cascade (`stormcloud_expansion_gone_wrong`) implicates the Sunbelt/Palmetto invoice swap as a parallel pattern; the vendor consolidation crisis (`vendor_consolidation`) sits on top of the unresolved Heartland dispute. Threading across scenarios is a feature, not noise.

- **The write-action surface is mid-rich.** Not as deep as the accounting-heavy universes — but the agent can update Airtable records, advance CRM deal stages, create CRM engagements, create/update Linear issues and projects, create QuickBooks invoices/bills/customers, send and reply to email, post to Slack, and (when seeded) add calendar events. The Write Tool Coverage Matrix in [03_TASK_CATEGORIES](03_MoveOps_TASK%20CATEGORIES.html) shows which write actions belong to which function.

- **Real client portfolio risk.** Vectral is in active renegotiation (10% counter-offer pending against a 15% demand). NorthWind issued a final warning naming PathFinder Logistics as a competitor. StormCloud is mid-multi-failure escalation (unsigned lease, dropped referral, misapplied credit). Sunbelt VP and Palmetto Foundation are at risk after a real invoice-swap mishap. Mosaic Robotics is open on a $90K damage claim. Several scripted scenarios sit directly on those tensions.

- **Regulatory exposure is live.** A formal DOT/PHMSA hazmat documentation inquiry (Case No. PHMSA-2026-04-1187) is mid-audit with a June 5, 2026 deadline and potential penalties up to **$59,017/day**. Elena issued a company-wide hazmat documentation policy in response.

- **Compounded engineering incidents.** The Expense Auto-Categorizer pilot launched, broke both ways (false rejections at Vectral, false approvals at Mosaic, $885 total exposure across 8 mis-decisions), was paused under Elena's direct order, and is now mid-remediation. Independently, a March AWS cost spike (~3x baseline, $42,870 vs $14,300) traced back to the Terraform Digital onboarding traffic — `#root-cause-aws-spike` is still the active investigation channel.

## **The personas you'll see most often**

These six anchor the largest share of scenarios. If you're stuck for a starting point, pick one of their open threads in [02_PERSONAS](02_MoveOps_PERSONAS.html):

| Name | Title | Best for |
| :---- | :---- | :---- |
| **Marcus Thorne** | Head of Finance | Vendor disputes, accrual reviews, DOT compliance financials, stipend fraud, vendor consolidation strategy |
| **David Chen** | Customer Engagement Lead | Account health, NorthWind retention, Vectral renewal, cross-functional reckoning, Sunbelt/Palmetto fallout |
| **Chloe Vance** | Operations Manager | Coordinator capacity, vendor consolidation, hazmat audit, ops timeline reconstruction, NorthWind chain-of-custody |
| **Mina Hashimoto** | Account Manager | Vectral renewal, BrightLoop expansion, Terraform onboarding, Dr. Mehta exec relocation, StormCloud recovery |
| **Emeka Diallo** | Account Manager | GreenStack/Mosaic accounts, $90K damage claim, Sunbelt/Palmetto invoice mishap, vendor exposure mapping |
| **Elena Rostova** | CEO | Strategic directives, DOT compliance policy, refusal/escalation handling, vendor strategy memo, expense-tool pause |

## **Where to dig deeper**

The full doc set lives next to this one-pager. They're written to be read in any order, but the Summary is the friendliest place to land first:

- [**Summary**](01_MoveOps_SUMMARY.html) — Company background, org chart, all 27 scenarios summarized as short stories, Slack channels, Airtable schema. Start here.
- [**Personas**](02_MoveOps_PERSONAS.html) — All 21 personas with active work, key relationships, open threads, and recent activity.
- [**Task Categories**](03_MoveOps_TASK%20CATEGORIES.html) — The 5 business functions with category patterns, typical write actions, worked example prompts, and the write-tool coverage matrix.
- [**Reference Sheet**](04_MoveOps_REFERENCESHEET.html) — The dense reference: internal personas, clients (active / at-risk / onboarding / prospects), vendors, Slack, Airtable, Linear, QuickBooks, and active CRM deals.
