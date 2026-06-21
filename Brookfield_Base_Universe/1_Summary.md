# Brookfield CPAs & Advisors — Universe Summary

Welcome. This is the front door to the **Brookfield CPAs & Advisors universe** — a detailed synthetic environment we use to train and evaluate AI agents on multi-system, multi-step work that looks and feels like a real day at a real US accounting firm.

## What this universe is for

The Brookfield universe doesn't exist in the real world. It's a carefully-constructed simulation: a complete fictional accounting firm, with named employees who have personalities and reporting lines, three "client" companies whose books we keep, an external audit firm we coordinate with, regulators we file to, and a dense substrate of accounting records — over **22,000 artifacts across 12 business systems** — that an AI agent can read, write to, and act inside.

The point of all this scaffolding is to make agent tasks feel like **real work**, not benchmark puzzles. The work an agent does here isn't a toy problem with one right answer in one file. It's the kind of work a real accountant does on a Tuesday morning:

- Cross-reference an aged invoice against the original Statement of Work in a separate document repository.
- Post a journal entry through a five-step approval chain, respecting a five-minute minimum between state transitions.
- Draft an email to a partner that summarises a multi-system investigation in one paragraph.
- File a memo under the correct retention code so the firm passes its next AICPA quality-management audit.
- Dismiss a stale reminder that's re-firing on an already-closed case — without reopening the case.

We use this universe in two modes: **training** (where agents learn what good work looks like from worked examples) and **benchmark** (where we measure performance against a held-out task set). Together those target **300 training tasks + 100 benchmark tasks**, distributed across the 10 task categories defined in [`03_TASK_CATEGORIES`](03_TASK_CATEGORIES%20-%20BROOKFIELD%20UNIVERSE.html).

## How to use the doc set

This summary is the front door. Once you're oriented, here's where to go next:

| Doc | When you need to… |
|-----|---------------------|
| [`02_PERSONA_BRIEFS`](02_PERSONA_BRIEFS%20-%20BROOKFIELD%20UNIVERSE.html) | Pick the persona who will be the acting voice on a task. Each persona has a profile of their work, relationships, and scenario footprint. |
| [`03_TASK_CATEGORIES`](03_TASK_CATEGORIES%20-%20BROOKFIELD%20UNIVERSE.html) | Design a task. The 10 categories cover every workflow the firm produces, with subcategories, worked examples, and links to study scenarios. |
| [`04_SCENARIO_STORYLINES`](04_SCENARIO_STORYLINES%20-%20BROOKFIELD%20UNIVERSE.html) | Find a scripted scenario to model your task on. All 52 are catalogued with anchor IDs, role assignments, and primary category. |
| [`05_ARTIFACTS`](05_ARTIFACTS%20-%20BROOKFIELD%20UNIVERSE.html) | Get the dense reference — full personas + NPCs + system schemas + useful accounts + complete scenario index. |
| [`06_GLOSSARY`](06_GLOSSARY%20-%20BROOKFIELD%20UNIVERSE.html) | Look up any accounting term or universe convention. |

You can read in order (01 → 06) or jump to whichever doc fits your immediate need. The rest of *this* summary walks you through the firm, its clients, its people, and the systems and rhythms that shape the work.

---

## What's new in v47 *(universe published 2026-06-05)*

The latest universe drop addresses SME-flagged realism gaps from the May audit. Highlights:

- **+6 personas (28 → 34).** Audit Staff **Mia Hartwell** and Audit Manager **Devon Beale** flesh out the audit team into a proper four-person stack. AP Coordinator **Priya Khatri** and AP Clerk **Tariq Soto** give the AP function persona-level acting voices (the AP Specialist Owen Mercer remains an NPC). Procurement Officer **Lena Park** anchors a new `procurement` department, deliberately separated from AP per segregation-of-duties. Billing Coordinator **Marcus Knell** owns the internal billing function. *None of the six are yet anchored in scripted scenarios* — they're available authoring seats for new task design.
- **+1 account: `135000 Prepaid Marketing`** on all three entities ("& Advertising" on Acme). Pairs with the Cat 4.7 improper-request example, where mis-using the account to defer a *finished* campaign is the matching-principle violation.
- **+7 Records Vault documents.**
  - **4 `client_consent_letter`** files (Acme×2 + Northstar×2 — covering Audit↔Tax and Audit↔Accounting cross-team work on each engagement, all `restricted`). AICPA standards require these on file before the audit team can pull workpapers from the firm's tax or accounting-services teams.
  - **2 ERP-migration docs** flagging the **SAP→Oracle GL Oct 2026 cutover** (`internal_strategy` Migration Plan + `internal_status_update` Q2 2026 decommission tracker).
  - **1 `tax_determination_memo`** for Acme SaaS — the authoritative anchor for the new sales-tax position (uploaded by Hannah Grant, `IRS_TAX_7Y`).
- **Acme sales tax narrowed to the four states that genuinely tax SaaS — TX, NY, WA, AZ.** The Q1 2026 accrual posts as a single combined entry of $42,180.55 (account `525000` Sales Tax Expense), with TX (per-ZIP local rates) the largest jurisdiction after Acme crossed the $612K trailing-12 economic-nexus threshold. The older TX/GA/NC compound and TX-only framings are now design scaffolding to correct, not templates to copy.
- **5 AP escalation invoices re-dated** to a realistic recent band — early-March 2026 invoice dates, ~85–100 days aged (scen_029 TimeLedger, scen_031 GraniteRack, scen_033 CrownPeak, scen_036 CrownPeak, scen_030 LatticeHill); the Slack exception flags cite tighter counts (87 / 85 / 83 days). ⚠️ scen_030 is internally inconsistent — its SAP `invoice_date` was moved up to early March but its Slack message still cites 334d, flagged in the docs as an anomaly. The other three escalations (scen_032 / 034 / 035) stay genuinely aged at 300+ days.
- **Total entries: 22,950** across 12 services (live-file count). Total named cast: **63 people** (34 personas + 29 NPCs).

---

## The Firm

Brookfield CPAs & Advisors is a **partner-led US public accounting and business advisory firm** based in Chicago, IL. It positions itself as a top-20 firm offering public accounting, outsourced accounting, bookkeeping, corporate tax, **compliance and internal controls** (AML monitoring, preparer/certifier independence testing, document retention, state filings, improper-request refusal), audit, and advisory services. The firm has roughly **140 employees** across partner, manager, senior, associate, trainee, and bookkeeping levels, with formal merit-based career progression.

| | |
|---|---|
| **Headquarters** | Chicago, IL |
| **Email domain** | `brookfieldcpas.com` (shared by personas and NPCs) |
| **Fiscal year end** | **12-31** |
| **Time range (active workflow)** | 2026-03-01 → 2026-06-12 (last event 2026-06-11; snapshot date 2026-06-12) |
| **"Today" for agent prompts** | **2026-06-12 US/Eastern** |
| **Timezone** | America/New_York (all GL/BlackLine/SAP timestamps use Eastern; the HQ is in Chicago but the systems run on Eastern) |
| **Universe total** | **22,950 entries** across 12 enabled components |
| **Scripted scenarios** | **52 merged YAMLs** (the usable scripted anchors) + 9 partial + 10 stage-1 checkpoint files (mid-generation artifacts, not anchors) |
| **Universe snapshot verified against** | `metadata.json updated_at = 2026-06-12` |
| **Task categories** | 10 categories; full catalog in [`03_TASK_CATEGORIES`](03_TASK_CATEGORIES%20-%20BROOKFIELD%20UNIVERSE.html) |

### Reading this summary

This summary is written to be readable by a non-accountant. It does use a number of recurring abbreviations and accounting terms — every one of them is defined in [`06_GLOSSARY`](06_GLOSSARY%20-%20BROOKFIELD%20UNIVERSE.html). The most frequent ones, defined here for quick reference:

| Term | Plain-language meaning |
|------|------------------------|
| **GL** | General Ledger — the master record of all of an entity's accounting transactions. In this universe the GL system is **Oracle GL**. |
| **JE** | Journal Entry — one debit-and-credit accounting record posted to the GL. Every transaction creates a JE. |
| **CoA** | Chart of Accounts — the numbered list of all accounts an entity uses (Cash, AR, AP, Revenue, etc.). Each entity has its own CoA. |
| **AR** | Accounts Receivable — money clients owe the firm (account `110000`). |
| **AP** | Accounts Payable — money the firm owes to outside vendors (account `210000`). |
| **WIP** | Work in Process — hours worked for clients that haven't been billed yet (account `119000`). |
| **BD0–BD8** | Business Days 0 through 8 of the month-end close cycle. BD0 = partner kickoff. BD1 = close-period JEs posted. BD3 = period lock. BD5 = period close. BD6–7 = partner sign-off. BD8 = archival. |
| **MMA** | Monthly Management Accounts — the recurring monthly close deliverable for each client. |
| **MAP** | Management Accounts Package — the packaged version of the MMA that goes to the partner for sign-off. |
| **AML** | Anti-Money Laundering — the regulatory regime governing client onboarding and ongoing monitoring (BSA / FinCEN rules). |
| **BO** | Beneficial Owner — anyone with > 25 % ownership or significant control of a client entity. |
| **FX** | Foreign Exchange — non-USD balances that must be revalued at period-end exchange rates. |
| **PBC** | Prepared By Client — the list of items an external auditor requests from the client/firm during fieldwork. |
| **OOS** | Out Of Scope — work that exceeds the engagement-letter's agreed scope/budget; triggers a partner disposition (absorb vs. change-order). |
| **IOLTA** | Interest On Lawyers Trust Account — segregated client funds held by law-firm clients. The **IOLTA concept** is Northstar-Legal-only, sitting on account `105000` on that entity. ⚠️ Account number `105000` itself exists on all three entities but holds different things: `Cash – Client Trust` on Brookfield, the IOLTA trust on Northstar, and `Short-term Investments` on Acme. Don't read "105000" as "IOLTA" without checking the entity. |
| **CPE** | Continuing Professional Education — required ongoing training for CPAs. |
| **ASC 606 / 340-40 / 842 / 740** | Four US accounting standards used heavily by Acme Cloud: 606 = revenue recognition for SaaS; 340-40 = capitalized sales commissions; 842 = lease accounting; 740 = income tax. |
| **SLA** | Service Level Agreement — the time-based commitments (e.g., 24h client query response, BD3 lock target). |
| **NPC** | Non-Player Character — universe-internal term for any external counterpart (regulator, vendor, client-side staff) or internal background admin/bench staff who appears in scenarios but **never authors tasks**. The 29 NPCs are catalogued in [`05_ARTIFACTS`](05_ARTIFACTS%20-%20BROOKFIELD%20UNIVERSE.html). |

---

## Brookfield in plain English

Brookfield CPAs & Advisors is a Chicago-based, partner-led, roughly 140-person US public accounting and advisory firm. It positions itself as a top-20 firm in its market. In practice, that translates to a handful of things you'll see throughout the universe:

- **The firm closes books, files taxes, supports audits, and gives advice** for outside clients — the standard CPA-firm shape.
- **It also keeps its own books, files its own taxes, and runs its own compliance** — so the firm is both an accountant *and* an accounting client of itself.
- **Five partners** each own a book of business, but the firm coordinates centrally on quality, deadlines, and client satisfaction. Partner sign-off is the final step on almost every meaningful workflow.
- **Work flows on recurring rhythms.** The 15th-of-month deadline for monthly management accounts is non-negotiable. Quarterly reporting lands at the end of each quarter. Annual accounts and tax returns drive the year-end peak. AML monitoring runs continuously in the background. The close calendar (BD0 kickoff → BD1 entries → BD3 lock → BD5 close → BD8 archival) governs every period's heartbeat.

### The handful of people you'll see most often

Of the 34 employees you can write tasks for, four come up over and over again across scenarios. Knowing these four orients you fast:

- **George McAdam** — Accounts Senior. The primary persona. The "working file owner" who keeps client files moving day-to-day, bridging bookkeepers below him and managers above. Appears in 20 of the 52 scenarios.
- **Daniel Jones** — Accounts Manager. George's manager and the most-loaded persona in the scenario set (25 scenarios). He triages every AP escalation, reviews every complex close, and routes things to partners.
- **Andrea Phil** — Partner, Accounting Services. Signs off the firm's own and Acme Cloud's monthly close packages, and makes the partner-level call on the absorb-versus-change-order question when an engagement runs out of scope.
- **Marina Soko** — Compliance Officer. Runs the AML reviews, the quarterly partner sign-off control test, and the document retention sweeps.

The full org chart, including the other 30 personas (and the 29 NPCs they work alongside), is just below.

---

## Three clients, three personalities

Brookfield works on three sets of books. Each has its own chart of accounts, its own fiscal-period prefixes, and its own engagement rhythms. Getting comfortable with all three is the fastest way to build intuition for the universe.

### 🏢 Brookfield CPAs & Advisors itself

Yes — the firm is its own client. Its own books, its own monthly close, its own state annual reports across **NY, NJ, DE**, its own AP, its own internal-control tests. Think of Brookfield's own engagement as the **control case**: the work the firm does *on itself* that proves it practises what it preaches. When you see a "firm-internal" scenario in the catalogue (the quarterly partner sign-off control test, the document retention sweep, the state annual report catch-up), the books being worked on are Brookfield's.

- **Entity slug:** `brookfield`
- **Fiscal period format:** `brookfield_FP-YYYY-MM`
- **Lead partner on the firm's own close:** Andrea Phil
- **Headline scenarios:** scen_023, 024 (monthly close), scen_048 (state annual report catch-up), scen_042 (quarterly control test).

### ⚖️ Northstar Legal LLP

A mid-sized US law firm client. Brookfield handles their **annual partnership tax return (Form 1065)**, their bookkeeping cleanup, supports their annual external audit (E&P is the audit firm, with **James Randall** as their named senior on Brookfield's side), and reconciles their **IOLTA trust account** (account `105000`). IOLTA — *Interest On Lawyers Trust Account* — is the segregated client-funds account that lawyer-trust rules require every law firm to maintain; reconciling it cleanly is a major piece of Northstar's audit support.

Northstar work involves law-firm specifics: court-filing expense codes, partner-distribution planning (the year-end tax-planning workshop is a Northstar fixture), lease accounting under **ASC 842**. **Matthew Li** is the engagement partner.

- **Entity slug:** `northstar_legal`
- **Fiscal period format:** `northstar_legal_FP-YYYY-MM`
- **Headline scenarios:** scen_025 (April close), scen_043 (FY2026 audit kickoff), scen_063 (FY2025 annual accounts), scen_068 (FY2025 federal partnership tax).

### ☁️ Acme Cloud Inc

A private B2B SaaS company. Acme is Brookfield's **outsourced-bookkeeping** client, which means Brookfield does Acme's *entire* monthly close end-to-end. That makes Acme the **most accounting-heavy** client in the universe. Every month, Acme requires:

- **ASC 606 deferred revenue release** — when a SaaS customer pays for an annual subscription, the revenue is recognised monthly as service is delivered.
- **ASC 340-40 capitalized commissions amortisation** — sales commissions paid upfront for multi-year contracts get amortised over the contract life (account `120000`).
- **R&D accruals**, **capitalized software entries** (account `155000`), **FX revaluation** on non-USD balances.
- **Sales tax filings** — **TX, NY, WA, AZ** for Acme's SaaS product, per the SaaS-taxability determination memo added in v47 (Records Vault, `kind: tax_determination_memo`, uploaded by Hannah Grant). TX uses destination-based per-ZIP local rates after Acme crossed the $612K trailing-12 economic-nexus threshold. CA and other older nexus references are exempt or services-not-taxed; treat them as cleanup items rather than current accruals. The Q1 2026 Acme sales-tax accrual posts as a single combined entry of $42,180.55 (`JE-acme_cloud-acme_cloud_FP-2026-03-0076`, account `525000`).
- An **annual beneficial-owner refresh** under AML rules.

Andrea Phil certifies Acme's monthly close package. **Steven Perry**, the Managing Partner, signs off on Acme AP invoices over $50K.

- **Entity slug:** `acme_cloud`
- **Fiscal period format:** `acme_cloud_FP-YYYY-MM`
- **Headline scenarios:** scen_027, 028 (monthly close), scen_046 (Q1 estimated tax), scen_055 (month-end FX), scen_061 (annual BO refresh), scen_064 → scen_065 (OOS review → change order).

### What this lets you do

The three entities cover meaningfully different territory: a CPA firm, a law firm, and a SaaS company. So tasks can be **entity-specific** (Acme's ASC 606 revenue recognition, Northstar's IOLTA reconciliation, Brookfield's state filings) or **cross-entity** (firm-wide risk pulls that aggregate across all three, quarterly control tests that sample reconciliations from any entity, OOS conversations that affect engagement economics). The cross-entity scenarios are where the universe gets most interesting because they require an agent to read across all three sets of books at once.

---

## How an engagement works

1. **Preparative vetting** — assess client transaction volume, financial position, suitability, AML status, and service scope. Marina Soko (Compliance) blocks onboarding if AML evidence is incomplete.
2. **Engagement setup** — contracts signed by partner/admin. Client file opened in Airtable, client assigned to a portfolio, access provisioned in Oracle GL and Records Vault.
3. **In-progress (recurring)** — bookkeeping, monthly management accounts (due by the 15th of each month), sales tax submissions, dashboard/quarterly reporting, BlackLine reconciliations, reviews, client queries.
4. **Review chain** — file owner (Senior) → Manager review (≥ 5 business days before delivery) → Partner sign-off for deliverable approval and legal contracts.
5. **Statutory delivery** — annual financial statements, annual corporate tax returns, quarterly sales tax returns, audit support to external auditors.
6. **Post-completion** — renewal, scope change orders (e.g. Acme out-of-scope review → change-order package), and recycle.

**Pricing:** recurring subscription / retainer arrangements. Minimum engagement value ~$7,500, typical ~$15,000, maximum ~$25,000. More than 200 active work items in flight at a time; 51-200 new items per month.

**Work effort:** simple item ~2 hours, typical ~2 days, complex ~2 weeks. Seasonal peaks in **December, January, and March**. 21-50% of work is repeat with the same clients.

---

## What a CPA / Advisory firm actually does

Brookfield is the **outsourced finance back office** for its clients plus the regulator-facing layer when statutory filings, audits, or AML supervision come due. The firm does not just compile numbers — it owns the controls, documentation, and review trail that lets a client file with the IRS, satisfy AML supervisors, pass an audit, and get the financing it needs.

**The firm's value proposition:** access to a multi-disciplinary partner-led team — bookkeeping, monthly management accounts, corporate tax, sales tax, audit support, AML/BO review and the broader internal-controls program (independence testing, retention sweeps, improper-request refusal), advisory — all on a single retainer. Each partner owns a book of business with meaningful autonomy, but central coordination, quality, and client satisfaction are firm-wide concerns. A SaaS client like Acme Cloud gets outsourced bookkeeping + multi-state sales tax + AML/BO review + ASC 606/340-40/842 specialty; a law-firm client like Northstar Legal gets bookkeeping cleanup + annual partnership tax + IOLTA-trust care + annual audit support.

**How Brookfield gets paid:** recurring retainer/subscription invoices billed by seniors/managers. Out-of-scope work triggers a formal change-order process — a draft package, partner review, CFO negotiation, signed engagement-letter addendum filed in Records Vault.

**The cast of characters Brookfield deals with** (external; coordinated *with*, never authored *as*):

| Party | Real-world body / org | Brookfield counterpart |
|-------|----------------------|------------------------|
| Client Finance Officer / Controller / CFO | client-side | seniors/managers; Margaret Sullivan (Controller NPC) appears in 5 close-side scenarios |
| External Auditor (E&P) | independent audit firm | Brookfield audit team (Mia Hartwell, Ryan Delgado, Devon Beale, Julia Vance — four-person stack as of v47); James Randall (E&P NPC) is the counterpart |
| IRS | federal tax authority | Alex Cahoon, Hannah Grant via Priya Singh (Corporation Tax Officer NPC) |
| AICPA | professional body | Marina Soko via Robin Woods (Practice Standards Monitoring Officer NPC) |
| AML Supervisor | money-laundering regulator | Peter Sanchez, Marina Soko via Anita Knowles (AML Supervisory Officer NPC) |
| EEOC | workplace-rights regulator | Steven Perry via James O'Brien (Conciliation Officer NPC) |
| Oracle GL vendor support | platform vendor | George McAdam, Sean Williams via Jane Founders / Brenda Abbas (NPCs) |
| Outside legal counsel | retained law | Daniel Jones, Peter Sanchez via Linda Burns (Commercial Law Consultant NPC) |
| Banks | client banking partners | Andrea Phil via Amira Siddiqui (Banking Relationship Manager NPC) |

---

## Org chart

**34 generated personas across 8 departments** (the v47 universe added 6 new personas: Audit Staff + Audit Manager, AP Coordinator + AP Clerk, Procurement Officer — a brand-new `procurement` department — and Billing Coordinator). Every persona — HR personas included — is an eligible acting seat. HR has a smaller scenario footprint than the accounting/tax/audit teams; that's a volume difference, not an eligibility rule. See the HR note below. **The 6 new v47 personas don't yet appear in any of the 52 scripted scenarios** — they're available for new task design but won't show up if you grep an existing scenario's role list.

### Partners (5)

| Name | Title | Notes |
|------|-------|-------|
| **Steven Perry** | Managing Partner | Top of the firm. Approves AP items > $50K for Brookfield/Acme. Final partner clearance authority on AML wire-flag (scen_041), quarterly partner sign-off control test (scen_042), document retention sweep (scen_044). 6 scenarios. |
| **Matthew Li** | Accounting Services Partner | Northstar engagement partner. AP partner for Northstar (> $50K tier). 14 scenarios — orphan exceptions, CrownPeak AP escalations, change order, BO refresh, Q1 partner package, tax planning. |
| **Ming Chang** | Tax Partner | Approver on Brookfield multi-state sales tax + Acme Q1 estimated tax. 2 scenarios. |
| **Andrea Phil** | Partner, Accounting Services | Reports to Matthew Li. Brookfield + Acme close certifier; OOS/change-order disposition; de-minimis AP partner. 14 scenarios. |
| **Julia Vance** | Audit Partner | Engagement partner on Northstar FY2026 audit + quarterly partner sign-off control test. Sits above the now-four-person audit-support team (Mia + Ryan + Devon + her, as of v47). 2 scenarios. |

### Admin & Operations (13)

| Name | Title | Notes |
|------|-------|-------|
| **Daniel Jones** | Accounts Manager | **Most-loaded persona — 25 scenarios.** Manager-layer triage across MMA, all 8 AP escalations, orphan exceptions, AML, audit, OOS. |
| **George McAdam** *(primary)* | Accounts Senior | **20 scenarios.** Anchor persona; preparer/identifier/peer across all major workflows. |
| **Edith Banda** | Accounts Senior | Northstar preparer + FX second-eye + Acme historical comparator. 11 scenarios. |
| **Jones Harrison** | Accounts Senior | Acme close preparer + recurring identifier on orphan exceptions. 7 scenarios. |
| **Harry Marks** | Accounts Associate | Working papers + control-account recs + fixed-asset schedules. 2 scenarios. |
| **Emily Adekole** | Accounts Associate | AR aging signal owner on Ridgepoint + orphan-exception peer/assignee. 3 scenarios. |
| **Blue Evans** | Accounts Associate | Accounts prep, payroll vetting, schedule prep. 1 scenario. |
| **Green Spatz** | Trainee Accountant | Trainee recon preparer (scen_039, 053). 2 scenarios. |
| **Anaya Wallace** | Trainee Accountant | Trainee anchor across AP escalations, FX JE prep, AR aging, orphan-exception live triage. 10 scenarios. |
| **Elita Moore** | Accounts Graduate Trainee | Anchored in deferred scen_049. 0 scripted scenarios. |
| **Priya Khatri** | AP Coordinator | *New in v47.* Owns AP intake routing, vendor-master accuracy, and weekly AP-exceptions triage. Natural canonical acting voice for new Cat 6.1 escalation tasks. 0 scripted scenarios. |
| **Tariq Soto** | AP Clerk | *New in v47.* Invoice data entry, three-way-match verification, routes exceptions up to Priya. 0 scripted scenarios. |
| **Marcus Knell** | Billing Coordinator | *New in v47.* Converts approved time and WIP into client invoices; coordinates revenue-recognition timing with Accounting Services. 0 scripted scenarios. |

### Bookkeeping (2)

| Name | Title | Notes |
|------|-------|-------|
| **Ben Arinzo** | Bookkeeper | AML transaction-context, AP escalations, orphan-exception assignments. 8 scenarios. |
| **Sean Williams** | Bookkeeper | Cash-operating orphan-exception assignee. 2 scenarios. |

### Tax (4)

| Name | Title | Notes |
|------|-------|-------|
| **Alex Cahoon** | Corporate Tax Manager | Identifier on closed-exception verifications. 4 scenarios. |
| **Hannah Grant** | Corporate Tax Senior | Tax-side reviewer overlay on orphan exceptions + tax cycles + recon-residual review. 14 scenarios. |
| **William White** | Corporate Tax Associate | Northstar tax partner of record + orphan-exception assignee. 3 scenarios. |
| **Tom Chang** | Tax Associate | Stale-reminder triage + multi-state sales tax + annual partnership tax + tax planning. 5 scenarios. |

### Compliance (2)

| Name | Title | Notes |
|------|-------|-------|
| **Peter Sanchez** | Head of Compliance | Sign-off on quarterly control + state catch-up. 3 scenarios. |
| **Marina Soko** | Compliance Officer | AML + quarterly compliance control tests. 4 scenarios. |

### Audit (3)

| Name | Title | Notes |
|------|-------|-------|
| **Mia Hartwell** | Audit Staff | *New in v47.* Tick-and-tie + detail testing on Northstar and Acme fieldwork; day-to-day fieldwork partner to the audit senior. 0 scripted scenarios. |
| **Ryan Delgado** | Audit Senior | Identifier + audit-side approver + FX rate snapshot + BO-refresh approver. 10 scenarios. |
| **Devon Beale** | Audit Manager | *New in v47.* Engagement planning, in-charge review, partner-level memo prep. Bridge between staff fieldwork and partner sign-off. 0 scripted scenarios. |

### Procurement (1) — *new department in v47*

| Name | Title | Notes |
|------|-------|-------|
| **Lena Park** | Procurement Officer | *New in v47.* Owns PO issuance, vendor onboarding diligence, and SOW lifecycle. Deliberately separated from AP per segregation-of-duties controls. 0 scripted scenarios (the scen_031 SOW-supersession question is the natural fit, but Lena isn't anchored in that yaml yet). |

### HR (4) — *low scenario footprint, full acting eligibility*

| Name | Title | Notes |
|------|-------|-------|
| **Brent Noah** | Director of People and Culture | 0 scripted scenarios. Eligible Cat 10 author; appears as participant/counterparty in cross-functional tasks. |
| **Clint Peterson** | HR Operations Manager | 0 scripted scenarios. Eligible Cat 10 author; appears as participant/counterparty. |
| **Rachel Green** | HR Business Partner | 0 scripted scenarios. Eligible Cat 10 author; appears as participant/counterparty. |
| **Reshma Patel** | HR Generalist | Named in 2 scenarios as an Accounts-side peer. Eligible Cat 10 author; also appears as participant/counterparty. |

**HR personas are eligible acting seats, like every other persona** — see the task-authoring conventions in [`03_TASK_CATEGORIES`](03_TASK_CATEGORIES%20-%20BROOKFIELD%20UNIVERSE.html). They author Category 10 tasks (onboarding routing, appraisal scheduling, dispute coordination, EEOC liaison) and appear as participants/counterparties in cross-functional tasks authored from other categories. Their scripted-scenario footprint is smaller than the accounting/tax/audit teams — reflect that in volume, not in eligibility.

---

## Background staff (NPCs) — *never acting seats*

29 generated NPCs share the same `brookfieldcpas.com` email domain. **NPCs are external in role** — regulators, vendors, client-side staff — or internal admin/bench staff. **NPCs never author tasks**; they are coordinated *with* (vendors, regulators) or appear as participants in cross-functional tasks (internal admin/bench staff).

### External / Regulator NPCs

| NPC | Title | Real-world body | Brookfield counterpart |
|-----|-------|-----------------|------------------------|
| Maya Streamer | Compliance Technical Advisor | IRS | Daniel Jones |
| Robin Woods | Practice Standards Monitoring Officer | AICPA | Marina Soko |
| James O'Brien | Conciliation Officer | EEOC | Clint Peterson |
| Anita Knowles | AML Supervisory Officer | AML regulator | Peter Sanchez, Marina Soko |
| Priya Singh | Corporation Tax Officer | IRS | Alex Cahoon |

### Vendor / Banking / Legal NPCs

| NPC | Title | Org type | Brookfield counterpart |
|-----|-------|----------|------------------------|
| Jane Founders | Business Support Officer | Oracle GL vendor | George McAdam, Jones Harrison |
| Brenda Abbas | Account Manager | Oracle GL vendor (+ Acme close reviewer + 6 AP escalations) | Sean Williams; Daniel Jones (AP) |
| Linda Burns | Commercial Law Consultant | retained legal counsel | Daniel Jones, Peter Sanchez |
| Amira Siddiqui | Banking Relationship Manager | bank | Andrea Phil |
| James Randall | Audit Senior | E&P (external audit firm) | George McAdam; orphan-exception approver in 5 scenarios |

### Client-Side NPCs

| NPC | Title | Client |
|-----|-------|--------|
| Ron Atkins | Operations Manager | XYZ Recruitment |
| Randall Peters | Payroll Officer | XYZ Recruitment |
| Rakesh Ambani | Chief Executive Officer | mental wellbeing practice |
| John Bartlett | Chief Executive Officer | Southgate Interiors |
| Remy Mas | Finance Officer | client |
| Mark Price | Finance Assistant | client |
| Olivia Steenkamp | Finance Officer | Marigold Property Services |
| Liam Scotman | Business Owner | Marksman Hardware |
| Taye Chestnut | Finance Officer | client |
| Margaret Sullivan | Controller | client-side (close-review reviewer in 5 scenarios) |

### Internal Background NPCs

| NPC | Title | Department | Scenario footprint |
|-----|-------|------------|-------------------|
| Margot Reyes | Portfolio Coordinator | admin_operations | 0 |
| Anaya Patel | Workflow Administrator | admin_operations | 1 (scen_048 state catch-up) |
| Nia Okafor | Senior Bookkeeper | bookkeeping | 1 (scen_018 Acme orphan-exception assignee) |
| Mateo Kovac | Bookkeeper | bookkeeping | 3 (AP escalations) |
| Sofia Halabi | Tax Specialist | tax | 2 (scen_045 reviewer, scen_046 preparer) |
| Farah Dlamini | AML Analyst | compliance | 3 (control-test scenarios) |
| Yusuf Demir | Talent Operations Specialist | hr | 0 |
| Lucia Ferreira | Client Onboarding Specialist | admin_operations | 0 (participant in onboarding tasks) |
| Owen Mercer | Accounts Payable Specialist | admin_operations | 9 (all 8 AP escalations + 1 orphan-exception) |

---

## Task design — the 10 categories

The full task catalog with subcategories, build blocks, and worked examples lives in [`03_TASK_CATEGORIES`](03_TASK_CATEGORIES%20-%20BROOKFIELD%20UNIVERSE.html). Brief overview:

| # | Category | Tag | Train | Bench |
|---|----------|---|------:|------:|
| 1 | Accounting Operations | 🎓 CPA-heavy | 90 | 30 |
| 2 | Bookkeeping | 🛠 No-CPA-required | 24 | 8 |
| 3 | Tax | 🎓 CPA-heavy | 30 | 10 |
| 4 | Compliance & Internal Controls | 🎓 CPA-heavy | 30 | 10 |
| 5 | Audit | 🎓 CPA-heavy | 18 | 6 |
| 6 | AP / Vendor Operations | 🛠 No-CPA-required | 36 | 12 |
| 7 | BlackLine Close-Discipline & Variance | 🎓 CPA-heavy | 30 | 10 |
| 8 | Engagement Mgmt & Client Operations | 🛠 No-CPA-required | 21 | 7 |
| 9 | Executive / Partner Oversight | 🎓 CPA-heavy | 12 | 4 |
| 10 | HR & People Operations | 🛠 No-CPA-required | 9 | 3 |
| | **Total** | | **300** | **100** |

Each category has 3–7 subcategories with their own worked examples (42 subcategories total). The persona → category mapping is in [`03_TASK_CATEGORIES`](03_TASK_CATEGORIES%20-%20BROOKFIELD%20UNIVERSE.html) §"Persona → Category mapping". The tag column is informational — 🎓 CPA-heavy categories lean on accounting concepts (adjusting entries, ASC standards, GAAP review, tax-code judgement); 🛠 No-CPA-required categories are operational / coordination work that doesn't require CPA-grade credentialing. The narrative in 03 explains every concept inline so any reader can follow.

---

## Communication channels (Slack)

| Channel ID | Name | Purpose |
|------------|------|---------|
| C001 | #general | Firm-wide updates |
| C002 | #water-cooler | Non-work chatter — coffee, weekend plans, client-safe humor |
| C003 | #announcements | One-way broadcast: hires, departures, holidays, firm wins |
| C004 | #client-onboarding | Kickoff, document collection, scope setup, new-client handoff |
| C005 | #monthly-close-coordination | Close timelines, reconciliations, review items (most active) |
| C006 | #tax-prep-and-filings | Return prep, extension tracking, filing deadlines |
| C007 | #audit-engagements | Audit support, PBC tracking, workpaper coordination |
| C008 | #compliance-and-registrations | Compliance calendars, registrations, annual reports, AML |
| C009 | #cash-management-and-banking | Bank feeds, treasury, signatory changes, payment workflows |
| C010 | #vendor-bills-and-ap | Vendor onboarding, invoice handling, AP exceptions |
| C012 | *(auto-created placeholder)* | Empty system-generated channel — not used for real coordination. It exists in the data and brings the Slack channel count to **11**. |

---

## Core systems

### Oracle GL (Accounting Platform) — 2,933 artifacts

The main accounting platform for bookkeeping, ledger review, transactions, reports, onboarding. Multi-entity ledger across `brookfield`, `northstar_legal`, `acme_cloud`. **v47 note:** the SAP Subledger is being consolidated into Oracle GL by an **Oct 2026 cutover** per the SAP→Oracle migration plan in Records Vault (`internal_strategy` doc + `internal_status_update` Q2 2026 decommission tracker).

- **245 accounts** (asset 70 / liability 44 / expense 75 / revenue 26 / equity 9 / contra-asset 20 / contra-equity 1). *v47 added 3 asset accounts:* `135000 Prepaid Marketing` on each entity (`Prepaid Marketing & Advertising` on Acme).
- **36 fiscal periods**, entity-prefixed (`<entity>_FP-YYYY-MM`)
- **22 subledger feeds** running nightly crons
- **2,388 journal entries** (statuses: `draft`, `submitted`, `approved`, `rejected`, `posted`, `reversed`)

**JE lifecycle:** `draft → submitted → approved → posted → (reversed)`. **Minimum 300 seconds between state transitions.** **Closed-period posting requires `late_post_authorization_id`.** Entity-prefixed JE IDs: `JE-acme_cloud-FP-2026-05-0012`.

**Adjusting JEs:** `is_standard_entry: false`. **Standard recurring:** `is_standard_entry: true`.

### SAP Subledger — 4,060 artifacts

Transaction-level detail supporting GL. **987 AP invoices** (`pending_approval` 320 / `approved` 301 / `paid` 274 / `voided` 92) across 117 unique vendor names. **240 fixed assets** (80 per entity), **75 prepaid amortization schedules**, **6 ASC 842 lease schedules**, **2,752 subledger transactions**.

### BlackLine (Close & Reconciliation) — 6,834 artifacts

- **683 reconciliations** flowing `open → in_progress → submitted → approved → certified → archived` (+ `overdue` side state)
- **24 exceptions** across 6 types: `duplicate_entry_detected` (6), `unrecorded_invoice` (5), `timing_difference_over_sla` (4), `fx_revaluation_drift` (4), `subledger_feed_drop` (3), `missing_accrual_variance` (2)
- Exception states: `logged → investigating → awaiting_approval → closed`
- **218 review notes**, **396 close tasks**, **931 evidence items**, **168 archived reconciliations**, **4,414 audit-trail entries**

The **scen_001 polling-bug pattern** — stale tickler re-firing on closed exception `exc_151b0bee7e374e` — has expanded into a 15-scenario family.

### Records Vault (Document Repository) — 4,554 artifacts

**2,007 documents** (brookfield 711 / northstar_legal 731 / acme_cloud 565), **2,356 versions**, **184 access grants**, **0 legal holds**. *v47 added 7 documents:* 4 `client_consent_letter` files (Acme×2 and Northstar×2, each covering Audit↔Tax and Audit↔Accounting, all `restricted`), 2 ERP-migration docs (`internal_strategy` Migration Plan + `internal_status_update` Decommission Status), and 1 `tax_determination_memo` (Acme SaaS multi-state, uploaded by Hannah Grant under `IRS_TAX_7Y`).

**Retention policies (4):** `AICPA_SQMS_7Y` (default, 7y), `IRS_TAX_7Y` (tax, 7y), `FIRM_INTERNAL` (engagement letters, 5y), `INDEFINITE`. **Do not use** `SOX_7Y` or `SEC_PERMANENT` — they don't exist.

**Classifications (3 defined, 2 in use):** `internal` (default, ~98% of documents — 1,975 of 2,007), `restricted` (AML files, executive comp, audit folders, partner-only memos, client-consent letters — 32 documents). The `public` classification is defined in the schema but **no document in the universe currently uses it** — don't author prompts that produce `public` artifacts unless deliberately introducing the first one.

### Airtable — 28 artifacts

**2 bases, 5 tables, 21 records.** Tables: Close Blocker Triage Log, Weekly Tax and Review Cadence, AP Workflow Exceptions, Annual Report Filing Control, Client Access and Onboarding Admin.

### Linear — 180 artifacts

**6 teams, 8 projects, 30 issues, 25 comments, 44 users, 67 memberships.** Used for systemic-issue tracking, not routine close work. The **AP workflow standardization project** (`linear_63697b7dff5c`) is the primary destination for issues surfaced by AP escalations.

### Supporting components

| Component | Count | Purpose |
|-----------|------:|---------|
| Email | 1,379 | 1,379 email messages. Formal comms + audit trail |
| Slack | 2,613 | 2,545 messages + 57 users + 11 channels. Quick internal coordination |
| Messaging | 202 | DMs and small-group threads |
| Calendar | 51 | Close kickoffs, partner reviews, audit kickoffs |
| Reminder | 53 | SLA tracking, deadline triggers |
| Contacts | 63 | Vendor, client, regulator records. *v47 added 6 internal contacts matching the 6 new personas.* |

**Universe total:** **22,950 entries** across the 12 enabled components.

---

## A quick word on account numbers

Every transaction in the universe posts to a numbered general-ledger account. The numbering follows a standard US convention: `1xxxxx` for assets, `2xxxxx` for liabilities, `3xxxxx` for equity, `4xxxxx` for revenue, `5xxxxx` for expenses. A handful you'll see a lot:

- `101000` Cash – Operating (all entities) · `110000` AR (all entities) · `119000` WIP (Brookfield + Northstar)
- `105000` — **three different concepts**: *Cash – Client Trust* (Brookfield), *IOLTA Trust* (Northstar), *Short-term Investments* (Acme)
- `120000` — **two different concepts**: *Deferred Commissions* (Acme, ASC 340-40), *Client Cost Advances* (Northstar); not present on Brookfield
- `133000` — **two different concepts**: *Prepaid CPE & Training* (Brookfield), *Prepaid CLE & Bar Dues* (Northstar); not present on Acme
- `135000` Prepaid Marketing — *v47 addition*, all three entities (`Prepaid Marketing & Advertising` on Acme)
- `153000` ROU Asset (all entities, ASC 842) · `155000` Capitalized Software (Acme only)
- `210000` AP · `220000` Accrued Professional Services · `225000` Accrued Salaries & Bonuses · `230000` Income Tax Payable (all entities)
- `500000` / `521000` / `530000` / `535000` — **same numbers, different roles per entity**. The Datadog reclass `500000 → 521000` in scen_028 is meaningful only on Acme.
- `570000` Depreciation (all entities)

**⚠️ Account numbers are not a guarantee of meaning.** A surprising number of account numbers in this universe are reused across entities for entirely different concepts — IOLTA on `105000` is Northstar-only, deferred commissions on `120000` is Acme-only, prepaid CPE on `133000` is Brookfield-only, and so on. Never reuse an account number across entities without confirming its role on each one's CoA. The full per-entity grid is in [`03_TASK_CATEGORIES`](03_TASK_CATEGORIES%20-%20BROOKFIELD%20UNIVERSE.html) under "Quick reference — useful accounts for prompt design."

**⚠️ Known CoA gap.** There is no dedicated **Sales Tax *Payable*** account in the CoA. The expense account `525000` Sales Tax Expense *does* exist on Acme (scen_067 debits it); the payable side lands on `225000` (otherwise Accrued Salaries & Bonuses). Before authoring any sales-tax task, confirm the correct accrual (liability) + expense accounts against the entity's CoA rather than assuming a purpose-built payable.

For the full account table, see [`05_ARTIFACTS`](05_ARTIFACTS%20-%20BROOKFIELD%20UNIVERSE.html).

---

## Compliance & approval rules

### Access controls
- Staff see only **portfolios they're assigned to**.
- HR files visible only to **HR staff + directors**.
- Internal firm accounts visible only to **internal accounting staff**.

### Action authority

| Action | Authorized roles |
|---|---|
| Basic client data + record editing | partners/admin, juniors, seniors/managers |
| Deliverable approval | partners/admin, seniors/managers |
| Official invoice sending | seniors/managers |
| Financial expense approval | partners/admin, seniors/managers |
| Legal contract signing | partners/admin only |
| AP coding (any amount) | AP clerks |
| AP approval ≤ $10,000 | AP managers |
| AP approval ≤ $50,000 | Controllers |
| AP approval > $50,000 | Managing Partner — by entity: Steven Perry (Brookfield/Acme), Matthew Li (Northstar), Andrea Phil (de-minimis) |

### Regulatory exposure

| Regime | Exposure |
|--------|----------|
| Data Protection Act 2018 / GDPR-style privacy | Up to 4% of worldwide turnover for serious violations |
| AICPA professional practice (SQMS 1; Code of Professional Conduct §1.700) | Fines up to $10,000/member; possible loss of practice rights |
| AML supervision (BSA / FinCEN CDD + BOI) | Fines, business restriction, criminal exposure |

### Named policies

IT Usage Policy, Employee Code of Conduct, Anti-Money Laundering Policy.

### Hard SLAs

- **24h** client query response
- **≥ 5 business days** between work submitted to review and the delivery deadline
- IRS quarterly sales tax / annual corporate tax — non-negotiable statutory deadlines
- Management accounts due by the **15th of the month**

---

## Close calendar (BD0–BD8)

The firm-wide close cadence per period:

| Day | What happens |
|-----|--------------|
| **BD0** (last day of period) | Partner kickoff. AP cuts off end of day. Final bank feed runs. FX rate snapshot taken. New fixed assets added. AR closed for the period. |
| **BD1** | Close-period **journal entries** posted: standard accruals, prepaid amortization, depreciation, ASC 606 deferred-revenue release (Acme), ASC 340-40 commission amortization (Acme), R&D accruals (Acme), credit-card accruals, reclasses. The 6 "June 1 BD1" JEs in this universe (`je_855f1b9deccb4502` and siblings) are FP-2026-05 BD1 postings. |
| **BD2** | Reviewer feedback. Operating expense report. Credit card recon. Revenue and cash entries finalized. |
| **BD3** | **Period lock target.** `bd3_lock_at` is the *scheduled* lock timestamp on the fiscal period — a target, not a realized state. Once a partner actually locks (period flips to `status=locked`), any further posting requires `late_post_authorization_id`. The FP-2026-05 lock target was 2026-06-03; periods remain `status=open` as of today (see "Why today = 2026-06-12" below). |
| **BD4** | All expense/revenue entries complete. |
| **BD5** | **Period close.** Non-revenue/expense entries finalized. Final reconciliations. Financial analysis begins. |
| **BD6–BD7** | Management Accounts Package (MAP) partner sign-off. |
| **BD8** | Archival — BlackLine reconciliations move to `archived` state. |

Quarter-end closes extend a few days past BD8. Some clients have shorter or longer close windows by engagement.

---

## Broader client base

Beyond the three entities that have full books in the universe, surveys reference a wider client roster Brookfield serves at a lighter touch: **XYZ Recruitment, Southgate Interiors, Marigold Property Services, Marksman Hardware, and a private mental wellbeing practice.** These appear as named clients in noise themes and persona relationships but don't have their own scenario yamls.

For the full engagement-scope breakdown by entity, see the [three-clients tour above](#three-clients-three-personalities). For schema-level entity reference, see [`05_ARTIFACTS`](05_ARTIFACTS%20-%20BROOKFIELD%20UNIVERSE.html).

---

## Scenarios — 52 merged YAMLs (the scripted anchors)

The full storyline catalog is in [`04_SCENARIO_STORYLINES`](04_SCENARIO_STORYLINES%20-%20BROOKFIELD%20UNIVERSE.html). Each scenario is a beat-by-beat artifact chain laid down across Oracle GL, BlackLine, SAP, Records Vault, Airtable, email, slack, messaging, calendar, reminder, and Linear.

### Family summary

| # | Family | Count | Primary category |
|---|--------|------:|-----------------|
| 1 | Monthly Management Accounts / Close | 5 | 1 |
| 2 | Orphan Exception / Stale SLA / Live Triage | 15 | 7 |
| 3 | AP Escalation | 8 | 6 |
| 4 | Recon Currency Refresh | 2 | 7 |
| 5 | Audit & Compliance | 5 | 4 / 5 |
| 6 | Tax & Regulatory | 3 | 3 |
| 7 | Adjusting / Recon / FX / Bad Debt / WIP / Fixed Asset | 6 | 1 / 7 |
| 8 | AML, Engagement Mgmt, Quarterly AR, Sales Tax, Annual Tax | 8 | 3 / 4 / 8 |
| | **Total** | **52** | |

---

## Universe layers

| Layer | What it provides | Volume |
|-------|------------------|--------|
| **L1 — Noise themes** | Background slack/email/messaging chatter | 28 themes / ~3,704 communication artifacts |
| **L2 — Baseline accounting state** | Routine recurring artifacts: CoA, fiscal periods, recurring close JEs, baseline AP invoices, baseline reconciliations | ~22,250 artifacts across Oracle GL, BlackLine, SAP, Records Vault |
| **L3 — Scripted scenarios** | Specific named, traceable workflow instances | 52 merged + 9 partial + 10 stage-1 checkpoint (71 YAMLs total; only the 52 merged are usable as scripted anchors) |

A workflow is **fully realistic only when all three layers contribute**. The agent investigating the universe sees chatter (L1), finds the records (L2), and can trace a named example (L3).

---

## Operating context

- HQ in Chicago, IL — but **system timezone is America/New_York** (Eastern); every Oracle GL / BlackLine / SAP timestamp uses Eastern offsets
- Universe time range: **2026-03-01 → 2026-06-12** (latest event timestamps run through 2026-06-11; metadata snapshot date is 2026-06-12)
- Agent "today": **2026-06-12 US/Eastern** (Friday, after FP-2026-05 BD3/BD5 calendar targets but before FP-2026-06 BD0)
- Sales tax obligations for Acme: **TX, NY, WA, AZ** (the four SaaS-taxable states per the v47 determination memo; older GA/NC scaffolding is exempt and treated as cleanup)
- Multi-state annual reports for Brookfield itself: NY, NJ, DE
- Peak demand months: **December, January, March**

### Why "today" = 2026-06-12

At 2026-06-12 the FP-2026-05 close has moved through most of its calendar — the BD3 lock target (June 3) and BD5 close target (June 5) have passed, BlackLine archives ran June 3–5, the June 1 BD1 JE postings are in, and all nightly subledger feed runs through June 11 are complete. **However: the three FP-2026-05 fiscal periods are still `status=open` (`locked_by=null`, `locked_at=null`)** — the lock-target deadlines passed without anyone actually locking, which is itself a plausible task setup (a partner still owes the lock, or there's a legitimate hold-open reason). FP-2026-06 hasn't started (`status=future`; BD3 lock target July 3 is future). The agent picks up an unusual between-state: BD-calendar past lock target but ledger still open, with AP invoices in mid-month payment cycle.

**The universe is clean past June 12.** A re-scan against the live `services/*/data.json` files at the 2026-06-12 cutoff finds only **12 records dated after today**, all legitimately forward-looking:

| Cluster | Count | Reason |
|---------|------:|--------|
| Oracle GL `fiscal_periods` FP-2026-06 (3 entities) | 3 | `status=future` — empty period shells for next-period posting (standard) |
| SAP AP invoices with `due_date` June 13–22 | 9 | Upcoming payment queue (standard 30–60 day vendor terms) |