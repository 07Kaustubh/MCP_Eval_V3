# Brookfield CPAs & Advisors — Artifacts & Reference Sheet

Universe reference sheet for task authors. Cross-reference against the live universe before reusing any anchor.

## Universe constants

| | |
|---|---|
| Fiscal year end | **12-31** |
| Time range (active workflow) | 2026-03-01 → 2026-06-12 (last event 2026-06-11; snapshot date 2026-06-12) |
| **Agent "today"** | **2026-06-12 US/Eastern** |
| Timezone | **America/New_York** (Eastern). HQ is Chicago but all systems run on Eastern offsets. |
| Email domain | `brookfieldcpas.com` (shared by personas and NPCs) |
| Total entries | **22,950** across 12 enabled components |
| Scripted scenarios | 52 merged YAMLs (the usable anchors) + 9 partial + 10 stage-1 checkpoint files = 71 YAMLs in the scenarios dir |
| Snapshot verified against | `metadata.json updated_at = 2026-06-12` |

---

## Internal Personas (34) — *the acting seats*

All personas share the email domain `brookfieldcpas.com` and operate on the system timezone `America/New_York` (Eastern). **Only these 34 personas author tasks** — HR personas included, per the task-authoring conventions in [`03_TASK_CATEGORIES`](03_TASK_CATEGORIES%20-%20BROOKFIELD%20UNIVERSE.html). NPCs (next section) are never acting seats. **v47 added 6 personas:** persona_029 through persona_034 below. They cover Audit (Staff + Manager), AP (Coordinator + Clerk), Procurement (the new department), and Billing Coordinator; none are yet anchored in scripted scenarios.

| Persona ID | Name | Email | Title | Department | Reports to | Authors in | Scenarios |
|------------|------|-------|-------|------------|-----------|-----------|-----------|
| persona_001 | George McAdam *(primary)* | george.mcadam@brookfieldcpas.com | Accounts Senior | admin_operations | Daniel Jones | 1, 2, 5, 7, 8 | 20 |
| persona_002 | Daniel Jones | daniel.jones@brookfieldcpas.com | Accounts Manager | admin_operations | Andrea Phil | 1, 2, 5, 6, 7, 8 | 25 |
| persona_003 | Harry Marks | harry.marks@brookfieldcpas.com | Accounts Associate | admin_operations | George McAdam | 1, 2, 7 | 2 |
| persona_004 | Hannah Grant | hannah.grant@brookfieldcpas.com | Corporate Tax Senior | tax | Alex Cahoon | 3 | 14 |
| persona_005 | Marina Soko | marina.soko@brookfieldcpas.com | Compliance Officer | compliance | Peter Sanchez | 4 | 4 |
| persona_006 | Clint Peterson | clint.peterson@brookfieldcpas.com | HR Operations Manager | hr | Brent Noah | 10 | 0 |
| persona_007 | Edith Banda | edith.banda@brookfieldcpas.com | Accounts Senior | admin_operations | Daniel Jones | 1, 2, 5, 7, 8 | 11 |
| persona_008 | Andrea Phil | andrea.phil@brookfieldcpas.com | Partner, Accounting Services | partner | Matthew Li | 1, 5, 6, 8, 9 | 14 |
| persona_009 | Jones Harrison | jones.harrison@brookfieldcpas.com | Accounts Senior | admin_operations | Daniel Jones | 1, 2, 5, 7, 8 | 7 |
| persona_010 | Emily Adekole | emily.adekole@brookfieldcpas.com | Accounts Associate | admin_operations | Jones Harrison | 1, 2, 7 | 3 |
| persona_011 | Green Spatz | green.spatz@brookfieldcpas.com | Trainee Accountant | admin_operations | Jones Harrison | 1, 2, 7 | 2 |
| persona_012 | Anaya Wallace | anaya.wallace@brookfieldcpas.com | Trainee Accountant | admin_operations | Harry Marks | 1, 2, 7 | 10 |
| persona_013 | Blue Evans | blue.evans@brookfieldcpas.com | Accounts Associate | admin_operations | Edith Banda | 1, 2, 7 | 1 |
| persona_014 | Ben Arinzo | ben.arinzo@brookfieldcpas.com | Bookkeeper | bookkeeping | George McAdam | 2, 6, 7 | 8 |
| persona_015 | Sean Williams | sean.williams@brookfieldcpas.com | Bookkeeper | bookkeeping | George McAdam | 2, 6, 7 | 2 |
| persona_016 | Peter Sanchez | peter.sanchez@brookfieldcpas.com | Head of Compliance | compliance | Steven Perry | 4, 9 | 3 |
| persona_017 | Alex Cahoon | alex.cahoon@brookfieldcpas.com | Corporate Tax Manager | tax | Ming Chang | 3 | 4 |
| persona_018 | Rachel Green | rachel.green@brookfieldcpas.com | HR Business Partner | hr | Clint Peterson | 10 | 0 |
| persona_019 | Brent Noah | brent.noah@brookfieldcpas.com | Director of People and Culture | hr | Steven Perry | 10 | 0 |
| persona_020 | Ryan Delgado | ryan.delgado@brookfieldcpas.com | Audit Senior | audit | Julia Vance | 5, 7 | 10 |
| persona_021 | Julia Vance | julia.vance@brookfieldcpas.com | Audit Partner | partner | — | 5, 9 | 2 |
| persona_022 | Elita Moore | elita.moore@brookfieldcpas.com | Accounts Graduate Trainee | admin_operations | Edith Banda | 1, 2, 7 | 0 |
| persona_023 | Matthew Li | matthew.li@brookfieldcpas.com | Accounting Services Partner | partner | Steven Perry | 1, 5, 6, 8, 9 | 14 |
| persona_024 | Steven Perry | steven.perry@brookfieldcpas.com | Managing Partner | partner | — | 6, 9, 10 | 6 |
| persona_025 | Ming Chang | ming.chang@brookfieldcpas.com | Tax Partner | partner | Steven Perry | 3, 9 | 2 |
| persona_026 | William White | william.white@brookfieldcpas.com | Corporate Tax Associate | tax | Hannah Grant | 3 | 3 |
| persona_027 | Tom Chang | tom.chang@brookfieldcpas.com | Tax Associate | tax | Hannah Grant | 3 | 5 |
| persona_028 | Reshma Patel | reshma.patel@brookfieldcpas.com | HR Generalist | hr | Clint Peterson | 10 † | 2 |
| persona_029 ‡ | Mia Hartwell | mia.hartwell@brookfieldcpas.com | Audit Staff | audit | Ryan Delgado | 5, 7 | 0 |
| persona_030 ‡ | Devon Beale | devon.beale@brookfieldcpas.com | Audit Manager | audit | Julia Vance | 5 | 0 |
| persona_031 ‡ | Priya Khatri | priya.khatri@brookfieldcpas.com | AP Coordinator | admin_operations | Daniel Jones | 6 | 0 |
| persona_032 ‡ | Tariq Soto | tariq.soto@brookfieldcpas.com | AP Clerk | admin_operations | Priya Khatri | 6 | 0 |
| persona_033 ‡ | Lena Park | lena.park@brookfieldcpas.com | Procurement Officer | procurement | Daniel Jones | 6 | 0 |
| persona_034 ‡ | Marcus Knell | marcus.knell@brookfieldcpas.com | Billing Coordinator | admin_operations | Daniel Jones | 1, 8 | 0 |

‡ New in v47 — eligible authoring seats but not yet anchored in any of the 52 scripted scenarios. See [`02_PERSONA_BRIEFS`](02_PERSONA_BRIEFS%20-%20BROOKFIELD%20UNIVERSE.html) for full briefs.

† Reshma is named in 2 yamls (scen_012, 015) in non-HR "Accounts-side peer" roles — a scenario-generator quirk. In those two specific yamls treat her as a participant, not an HR acting voice. She remains a full Cat 10 acting seat for HR-anchored task authoring elsewhere.

**HR personas (Brent Noah, Clint Peterson, Rachel Green, Reshma Patel) are eligible acting seats** for Category 10 tasks (onboarding routing, appraisal scheduling, dispute coordination, EEOC liaison), per the framing in [`03_TASK_CATEGORIES`](03_TASK_CATEGORIES%20-%20BROOKFIELD%20UNIVERSE.html). Their scripted-scenario footprint is smaller than the accounting/tax/audit teams — reflect that in volume, not in eligibility. They also appear as participants/counterparties in cross-functional tasks authored from other categories.

---

## NPCs (29) — *never acting seats*

NPCs share the `brookfieldcpas.com` email domain in the simulation but their *role* in the world is external (regulator, vendor, client-side staff) or internal admin/bench staff. **NPCs never author tasks.** They are coordinated *with* (external) or appear as participants in cross-functional tasks (internal admin/bench).

### External / Regulator NPCs

| NPC ID | Name | Title | Real-world body | Brookfield counterpart |
|--------|------|-------|-----------------|------------------------|
| npc_005 | Maya Streamer | Compliance Technical Advisor | IRS / compliance | Daniel Jones |
| npc_009 | Robin Woods | Practice Standards Monitoring Officer | AICPA | Marina Soko |
| npc_010 | James O'Brien | Conciliation Officer | EEOC | Clint Peterson |
| npc_018 | Anita Knowles | AML Supervisory Officer | AML regulator | Peter Sanchez, Marina Soko |
| npc_019 | Priya Singh | Corporation Tax Officer | IRS | Alex Cahoon |

### Vendor / Banking / Legal NPCs

| NPC ID | Name | Title | Org type | Brookfield counterpart |
|--------|------|-------|----------|------------------------|
| npc_001 | Jane Founders | Business Support Officer | Oracle GL vendor | George McAdam, Jones Harrison |
| npc_016 | Brenda Abbas | Account Manager | Oracle GL vendor (+ Acme close reviewer + 6 AP escalation account-mgr roles) | Sean Williams; Daniel Jones (AP) |
| npc_006 | Linda Burns | Commercial Law Consultant | retained legal counsel | Daniel Jones, Peter Sanchez |
| npc_012 | Amira Siddiqui | Banking Relationship Manager | bank | Andrea Phil |
| npc_003 | James Randall | Audit Senior | E&P (external audit firm) | George McAdam; orphan-exception approver in 5 scenarios |

### Client-Side NPCs

| NPC ID | Name | Title | Client | Brookfield counterpart |
|--------|------|-------|--------|------------------------|
| npc_002 | Ron Atkins | Operations Manager | XYZ Recruitment | George McAdam |
| npc_007 | Randall Peters | Payroll Officer | XYZ Recruitment | Harry Marks |
| npc_004 | Rakesh Ambani | Chief Executive Officer | mental wellbeing practice | Daniel Jones |
| npc_011 | John Bartlett | Chief Executive Officer | Southgate Interiors | Andrea Phil, Alex Cahoon |
| npc_008 | Remy Mas | Finance Officer | client | Hannah Grant |
| npc_013 | Mark Price | Finance Assistant | client | Emily Adekole |
| npc_014 | Olivia Steenkamp | Finance Officer | Marigold Property Services | Blue Evans |
| npc_015 | Liam Scotman | Business Owner | Marksman Hardware | Ben Arinzo |
| npc_017 | Taye Chestnut | Finance Officer | client | Sean Williams |
| npc_020 | Margaret Sullivan | Controller | client-side (close-review reviewer in 5 scenarios) | preparers across 5 close scenarios |

### Internal Background NPCs

| NPC ID | Name | Title | Department | Scenario footprint |
|--------|------|-------|------------|-------------------|
| npc_021 | Margot Reyes | Portfolio Coordinator | admin_operations | 0 |
| npc_022 | Anaya Patel | Workflow Administrator | admin_operations | 1 (scen_048 state catch-up) |
| npc_023 | Nia Okafor | Senior Bookkeeper | bookkeeping | 1 (scen_018 Acme orphan-exception assignee) |
| npc_024 | Mateo Kovac | Bookkeeper | bookkeeping | 3 (AP escalations) |
| npc_025 | Sofia Halabi | Tax Specialist | tax | 2 (scen_045 reviewer, scen_046 preparer) |
| npc_026 | Farah Dlamini | AML Analyst | compliance | 3 (control-test scenarios) |
| npc_027 | Yusuf Demir | Talent Operations Specialist | hr | 0 |
| npc_028 | Lucia Ferreira | Client Onboarding Specialist | admin_operations | 0 (participant in onboarding tasks) |
| npc_029 | Owen Mercer | Accounts Payable Specialist | admin_operations | 9 (all 8 AP escalations + 1 orphan-exception) |

---

## Client Entities

| Slug | Display name | Entity type | Engagement scope |
|------|--------------|-------------|------------------|
| `brookfield` | Brookfield CPAs & Advisors | CPA firm (the firm itself) | Internal books, sales tax, state annual reports, partner reporting, WIP recognition, bad-debt write-offs |
| `northstar_legal` | Northstar Legal LLP | US law firm | Annual partnership tax (Form 1065), bookkeeping cleanup, IOLTA trust (acct `105000`), annual audit, year-end partnership-distribution tax planning, FX revaluation |
| `acme_cloud` | Acme Cloud Inc | B2B SaaS | Outsourced bookkeeping, sales tax (TX/NY/WA/AZ — the four SaaS-taxable states per v47 determination memo), AML/BO review, ASC 606 deferred revenue, ASC 340-40 deferred commissions (acct `120000`), capitalized software (acct `155000`), R&D accruals, AP escalations on stalled SaaS vendor invoices |

Broader client base mentioned in surveys but without scenario data: **XYZ Recruitment, Southgate Interiors, Marigold Property Services, Marksman Hardware, and a private mental wellbeing practice.**

---

## Tools & Services — Overview

Twelve MCP services are enabled. Accounting state-of-record: **Oracle GL, SAP Subledger, BlackLine, Records Vault**. Workflow/coordination: **Airtable, Linear**. Communications: **Email, Slack, Messaging, Calendar, Reminder, Contacts**.

| Service | Role | Records | Backing file |
|---------|------|---------|--------------|
| **Oracle GL** | Main accounting platform | 245 accounts (v47 added 3 × `135000 Prepaid Marketing`), 36 fiscal periods, 22 subledger feeds, 242 feed runs, 2,388 journal entries — **2,933 total** | `services/oracle_gl/data.json` |
| **SAP Subledger** | Subledger detail supporting GL | 987 AP invoices, 240 fixed assets, 75 prepaid amortization schedules, 6 lease schedules, 2,752 subledger transactions — **4,060 total** | `services/sap_subledger/data.json` |
| **BlackLine** | Close & reconciliation workflow | 683 reconciliations, 218 review notes, 24 exceptions, 396 close tasks, 931 evidence items, 168 archived reconciliations, 4,414 audit-trail entries — **6,834 total** | `services/blackline/data.json` |
| **Records Vault** | Document repository | 2,007 documents (v47 added 7: 4 `client_consent_letter` + 2 ERP-migration docs + 1 `tax_determination_memo`), 2,356 versions, 184 access grants, 4 retention policies, 3 classifications, 0 legal holds — **4,554 total** | `services/records_vault/data.json` |
| **Airtable** | Portfolio & workflow management | 2 bases, 5 tables, 21 records — **28 total** | `services/airtable/data.json` |
| **Linear** | Work tracking | 6 teams, 8 projects, 30 issues, 25 comments, 44 users, 67 memberships — **180 total** | `services/linear/data.json` |
| **Email** | Formal comms + audit trail | **1,379 email messages — 1,379 entries** | `services/email/data.json` |
| **Slack** | Quick internal coordination | **2,545 messages across 11 channels + 57 users — 2,613 entries**. The 11 channels: `#general`, `#water-cooler`, `#announcements`, `#client-onboarding`, `#monthly-close-coordination`, `#tax-prep-and-filings`, `#audit-engagements`, `#compliance-and-registrations`, `#cash-management-and-banking`, `#vendor-bills-and-ap`, plus one unnamed `C012`. | `services/slack/data.json` |
| **Messaging** | DMs and small-group threads | **202 conversations** | `services/messaging/data.json` |
| **Calendar** | Meetings, kickoffs, lock targets | **51 events** | `services/calendar/data.json` |
| **Reminder** | SLA tracking, deadline triggers | **53 reminders** | `services/reminder/data.json` |
| **Contacts** | Vendor, client, regulator records | **63 contacts** (v47 added 6 for the new personas) | `services/contacts/data.json` |

**Universe total: 22,950 entries** across the 12 services.

---

## Oracle GL Structure

**Entities tracked:** `brookfield`, `northstar_legal`, `acme_cloud` — each with its own chart of accounts.

**Fiscal period format:** `<entity>_FP-YYYY-MM` (e.g. `brookfield_FP-2026-04`). Bare `FP-2026-04` will fail.

**JE ID format:** `JE-<entity>-FP-YYYY-MM-NNNN` (e.g. `JE-acme_cloud-FP-2026-05-0012`).

### JE lifecycle

`draft → submitted → approved → posted → (reversed)`. **Minimum 300 seconds between state transitions.** Closed-period posting requires `late_post_authorization_id`.

**Status counts:** `posted` 1,939 · `approved` 257 · `rejected` 113 · `draft` 41 · `submitted` 38. (No JE currently sits in the `reversed` state — reversals appear as posted entries carrying a `reverses_entry_id`.)

### Chart of Accounts (245 accounts)

Per-entity counts: `brookfield` 80 · `northstar_legal` 78 · `acme_cloud` 87.

**Account-number ranges:**

| Type | Range | Sample (Brookfield) |
|------|-------|--------------------|
| Asset | `1xxxxx` | `101000` Cash – Operating, `110000` AR, `131000` Prepaid Software Subscriptions, `132000` Prepaid Facilities Maintenance |
| Contra-asset | `117000` (allowance) / `158xxx` (accum-dep) / `175500` (accum-amort) | `117000` Allowance for Doubtful Accounts |
| Liability | `2xxxxx` | `210000` AP, `220000` Accrued Professional Services |
| Equity | `3xxxxx` | `300000` Partner Capital |
| Revenue | `4xxxxx` | `400000` Total Revenue |
| Expense | `5xxxxx` | `500000` Direct Engagement Costs – Subcontracted |

### Useful accounts for prompt design

> **⚠️ The account *number* is not a guarantee of meaning.** Many account numbers are reused across entities for completely different concepts. The role column below is **per-entity** — never assume an account number alone tells you what an account holds.

| Account | Brookfield | Northstar Legal | Acme Cloud | Notes |
|---------|-----------|-----------------|-----------|-------|
| `101000` | Cash – Operating | Cash – Operating | Cash – Operating | Consistent across all 3 |
| `105000` | **Cash – Client Trust** | **IOLTA – Client Trust Account** | **Short-term Investments** | ⚠️ Same number, three different concepts. IOLTA rules apply only on Northstar. |
| `110000` | AR – Client Billings | AR – Client Billings | AR – Subscription Billings | All entities have AR on 110000 |
| `117000` | Allowance for Doubtful Accounts | Allowance for Doubtful Accounts | Allowance for Doubtful Accounts | Contra-asset |
| `119000` | Work in Process – Unbilled Services / Time | Work in Process – Unbilled Services / Time | — | Brookfield + Northstar billable. Commonly abbreviated **WIP**; in this firm WIP always means unbilled revenue, not inventory. |
| `120000` | *(not in CoA)* | **Client Cost Advances** | **Deferred Commissions – Current** | ⚠️ Same number, two different concepts. ASC 340-40 only on Acme. |
| `130000` | Prepaid Professional Liability Insurance | Prepaid Malpractice Insurance | Prepaid Insurance | Each entity carries a prepaid-insurance account at 130000 with an entity-specific name. |
| `131000` | Prepaid Software Subscriptions | Prepaid Software Subscriptions | Prepaid Software & SaaS Subscriptions | All three entities. |
| `132000` | Prepaid Facilities Maintenance | Prepaid Facilities Maintenance | Prepaid Facilities Maintenance & Janitorial | All three entities. |
| `133000` | **Prepaid CPE & Training** | **Prepaid CLE & Bar Dues** | *(not in CoA)* | ⚠️ Same number, two different professional-ed concepts. |
| `134000` | Prepaid Other Operating Expenses | Prepaid Other Operating Expenses | Prepaid Other Operating Expenses | Catch-all prepaid, all three entities. |
| `135000` | Prepaid Marketing | Prepaid Marketing | Prepaid Marketing & Advertising | **v47 addition.** Prepaid asset for marketing campaigns that will deliver their benefit in future months. Cat 4.7 improper-request refusal anchors here. |
| `150200` | Fixed Assets – IT (≥ $5K) | Fixed Assets – IT (≥ $5K) | Fixed Assets – IT (≥ $5K) | Consistent |
| `153000` | ROU Asset | ROU Asset | ROU Asset | ASC 842 |
| `155000` | — | — | **Capitalized Software** | Acme-only |
| `158xxx` | Accumulated Depreciation | Accumulated Depreciation | Accumulated Depreciation | Contra-asset block |
| `175500` | Accum. Amortization | *(not in CoA)* | Accum. Amortization | Contra-asset. **⚠️ Brookfield + Acme only — Northstar has no `175500`.** |
| `210000` | AP – External Vendors | AP – External Vendors | AP – External Vendors | All entities |
| `219000` | AP – Employee Reimbursements | AP – Employee Reimbursements | AP – Employee Reimbursements | All entities |
| `220000` | Accrued Professional Services | Accrued Professional Services | Accrued Professional Services | All entities |
| `221000` / `222000` | Lease Liability | Lease Liability | Lease Liability | ASC 842 |
| `225000` | Accrued Salaries & Bonuses | Accrued Salaries & Bonuses | Accrued Salaries & Bonuses | All entities |
| `230000` | Income Tax Payable | Income Tax Payable | Income Tax Payable | All entities |
| `500000` | Direct Engagement Costs – Subcontracted | Direct Engagement Costs – Co-Counsel | Cost of Revenue – Cloud Infrastructure | ⚠️ Same number, three different concepts |
| `521000` | Tax Preparation Software | Document Management Software | Engineering Tools & Observability | ⚠️ Datadog reclass `500000`→`521000` (scen_028) is Acme-only |
| `525000` | *(not in CoA)* | *(not in CoA)* | **Sales Tax Expense** | **⚠️ Acme only.** Debit side of Acme's sales-tax accrual (scen_067). A *real* account — not the "non-existent 525000" of older guidance. No Brookfield/Northstar equivalent. |
| `530000` | Professional Services – Legal | Court Filing | Professional Services – Legal | ⚠️ Different roles per entity |
| `535000` | Continuing Professional Education (CPE) | Continuing Legal Education (CLE) | *(not in CoA)* | ⚠️ Brookfield + Northstar only. Paired with the prepaid at `133000`. Acme has neither. |
| `570000` | Depreciation | Depreciation | Depreciation | All entities |

### ⚠️ Known CoA gap

**There is no dedicated Sales Tax *Payable* account in the CoA.** The expense side exists — `525000` Sales Tax Expense is a real account on Acme (scen_067 debits it $42,180.55); the payable lands on `225000` (otherwise Accrued Salaries & Bonuses). Confirm the correct accrual (liability) + expense accounts per entity before authoring Category 3 sales-tax tasks rather than assuming a purpose-built payable.

### Subledger Feeds (22, each entity-specific)

Feeds run nightly via cron.
- **Brookfield (7):** client billing, time & WIP, cash receipts, accounts payable, payroll, tax engagement trust, treasury & bank activity.
- **Northstar Legal (7):** client billing, cash receipts, vendor payables, payroll & partner draw, corporate card expense, trust & retainer activity, tax workflow accrual.
- **Acme Cloud (8):** client billing, cash receipts, vendor payables, payroll & partner draw, treasury & bank activity, intercompany allocation, time capture accrual, expense report.

### JE schema fields

`id`, `entry_number`, `period_id`, `posting_date`, `status`, `description`, `business_justification`, `source_module`, `entry_type`, `is_standard_entry`, `lines`, `total_debit`, `total_credit`, `prepared_by`, `approved_by`, `rejected_by`, `rejection_reason`, `posted_by`, `review_threshold_triggered`, `late_post_authorization_id`, `attachments`, `reversed_by_entry_id`, `reverses_entry_id`, `created_at`, `submitted_at`, `approved_at`, `rejected_at`, `posted_at`, `reversed_at`, `entity_id`.

---

## SAP Subledger Structure

| Collection | Count | Notes |
|------------|------:|-------|
| AP Invoices | 987 | brookfield 375 / northstar_legal 264 / acme_cloud 348 |
| Fixed Assets | 240 | 80 per entity, all `in_service` |
| Prepaid Amortization Schedules | 75 | Drives prepaid setup / amortization adjusting JEs |
| Lease Schedules | 6 | ASC 842 leases |
| Subledger Transactions | 2,752 | Transaction-level detail supporting GL balances |

### AP Invoice statuses

| Status | Count |
|--------|------:|
| `pending_approval` | 320 |
| `approved` | 301 |
| `paid` | 274 |
| `voided` | 92 |

**Vendors:** 117 unique vendor names in the AP invoice set. Notable scenario-tied vendors: **TimeLedger Nexus** (scen_029, 032), **LatticeHill Learning Center** (scen_030), **GraniteRack Compute Services** (scen_031), **CrownPeak Cyber Defense** (scen_033, 034, 036), **Pinecrest Workflow Works** (scen_035).

### AP Approval Threshold Ladder

| Tier | Authority |
|------|-----------|
| All amounts | AP clerk codes |
| ≤ $10,000 | AP manager |
| ≤ $50,000 | Controller |
| > $50,000 | **Managing Partner — by entity:** Steven Perry (Brookfield/Acme), Matthew Li (Northstar), Andrea Phil (de-minimis) |

---

## BlackLine Structure

> **Excel is the primary reconciliation surface in this firm; BlackLine is the workflow + evidence store around the spreadsheet.** The Excel workbook holds the GL balance, supporting items, computed variance, and the explanation; BlackLine records the recon metadata (`gl_balance`, `supporting_balance`, `variance`, `state`), routes preparer / reviewer / certifier signatures, and runs SLA reminders. Tasks in Cat 7 are designed around that division.

| Collection | Count | Notes |
|------------|------:|-------|
| Reconciliations | 683 | brookfield 221 / northstar_legal 220 / acme_cloud 242 |
| Review Notes | 218 | Reviewer ↔ preparer threads during close |
| Exceptions | 24 | Six exception types |
| Close Tasks | 396 | Per-period close checklists |
| Evidence | 931 | Supporting attachments on reconciliations |
| Archived Reconciliations | 168 | Period-over-period roll-forward |
| Audit Trail | 4,414 | Every reconciliation touch |

### Reconciliation states

`open → in_progress → submitted → approved → certified → archived` (plus `overdue` as a side state).

| State | Count |
|-------|------:|
| `certified` | 363 |
| `archived` | 168 |
| `approved` | 69 |
| `in_progress` | 32 |
| `open` | 21 |
| `overdue` | 20 |
| `submitted` | 10 |

**Variance materiality thresholds:** under $10 immaterial; $10–$1,000 should be addressed (may be rolled to subsequent month JE); over $1,000 urgent.

### Exception types

| Type | Count |
|------|------:|
| `duplicate_entry_detected` | 6 |
| `unrecorded_invoice` | 5 |
| `timing_difference_over_sla` | 4 |
| `fx_revaluation_drift` | 4 |
| `subledger_feed_drop` | 3 |
| `missing_accrual_variance` | 2 |

### Exception states

`logged → investigating → awaiting_approval → closed`.

**Polling-bug pattern:** scen_001 stale-tickler family — canonical exception `exc_151b0bee7e374e` on account `110000`, $647.97 variance, recon `BL-2E691B2E18FA`, period `brookfield_FP-2025-07`. The polling bug causes stale SLA reminders to re-fire on already-closed exceptions; the correct response is dismissal with documented audit trail (Category 7.1), not reopening.

---

## Records Vault Structure

| Collection | Count | Notes |
|------------|------:|-------|
| Documents | 2,007 | brookfield 711 / northstar_legal 731 / acme_cloud 565 (v47 added 7) |
| Document Versions | 2,356 | Multiple versions per doc |
| Access Grants | 184 | Portfolio-scoped |
| Retention Policies | 4 | See below |
| Classifications | 3 defined, **2 in use** | `internal` (1,975) · `restricted` (32, including the 4 v47 client-consent letters) · `public` (0 — defined but unused) |
| Legal Holds | 0 | None active |

### Retention Policies

| Code | Years | Regulatory basis | Description |
|------|-------|------------------|-------------|
| `AICPA_SQMS_7Y` | 7 | AICPA SQMS 1 | 7-year retention for tax workpapers, audit support, reconciliation evidence. **Default — use this for almost every scenario doc.** |
| `IRS_TAX_7Y` | 7 | IRS §6107 | 7-year retention for tax-preparer records and supporting work files |
| `FIRM_INTERNAL` | 5 | Firm internal policy | Engagement letters, client master files, operational records |
| `INDEFINITE` | — | Firm internal policy | Partnership agreements, statutory records, legal-hold-only documentation |

**Do not use** `SOX_7Y`, `SEC_PERMANENT`, or any other code outside this list — they don't exist. Retention usage in current data: `AICPA_SQMS_7Y` 1,989 · `FIRM_INTERNAL` 9 · `IRS_TAX_7Y` 8 · `INDEFINITE` 1 (= 2,007).

### Classifications

| Code | Elevated role required | Description |
|------|:---------------------:|-------------|
| `public` | no | Publicly available. **⚠️ Defined in schema but currently unused — 0 documents carry this classification.** Don't author prompts that produce `public` artifacts unless deliberately introducing the first one. |
| `internal` | no | Internal company use only (default — 1,975 docs, ~98% of the corpus) |
| `restricted` | **yes** | VP-level or above; AML disposition memos, executive comp, audit folders, partner-only memos, client-consent letters (32 docs) |

### Document kinds (18 kinds — full breakdown, sums to 2,007)

| Kind | Count |
|------|------:|
| `journal_entry_support` | 1,569 |
| `reconciliation_support` | 332 |
| `audit_evidence` | 73 |
| `memo` | 10 |
| `client_consent_letter` | 4 |
| `management_accounts_package` | 4 |
| `tax_return` | 4 |
| `annual_accounts_package` | 1 |
| `engagement_change_order` | 1 |
| `engagement_letter` | 1 |
| `engagement_letter_addendum` | 1 |
| `internal_status_update` | 1 |
| `internal_strategy` | 1 |
| `quarterly_reporting_package` | 1 |
| `receipt` | 1 |
| `state_filing_receipts` | 1 |
| `tax_determination_memo` | 1 |
| `workpaper` | 1 |

### Records Vault past-cutoff scan (clean)

At today = 2026-06-12, **0 Records Vault documents and 0 document_versions are dated after today**. The latest `uploaded_at` across all 2,356 versions is now 2026-06-12T05:55-04:00, earlier in the same day as the universe "now". No action required for authors.

---

## Airtable Structure

Two bases hold the firm's portfolio and workflow management state.

### Bases

| Base ID | Name |
|---------|------|
| `airtable_e86eaf439d1d` | Daily outsourced accounting close blocker triage — bank feed exceptions and cash posting follow-up |
| `airtable_6ac18f5d342c` | Multi-state annual report catch-up and filing readiness control center |

### Tables

| Table ID | Name | Purpose |
|----------|------|---------|
| `airtable_1a80ff5c1ed3` | **Close Blocker Triage Log** | Daily close blockers tied to bank-feed exceptions, cash-posting delays, recon follow-up |
| `airtable_11c1e4c6585d` | **Weekly Tax and Review Cadence** | Wednesday tax pipeline review, trainee work-review loops, return-review threads ahead of filings |
| `airtable_8ee8b6013413` | **AP Workflow Exceptions** | Managed-client AP workflow standardization, vendor-approval delays, invoice-related payment misses |
| `airtable_d2d6dfe7c4b3` | **Annual Report Filing Control** | Multi-state annual report catch-up, overdue entity filings, readiness checks |
| `airtable_f9ea4c4c150d` | **Client Access and Onboarding Admin** | Client onboarding kickoff, document-request review, new-starter access scheduling, confidential records-vault restrictions |

### Status enums

| Table | Status flow |
|-------|-------------|
| Close Blocker | `open` → `investigating` → `awaiting_partner_review` → `resolved` |
| Annual Report | `not_started` → `in_progress` → `awaiting_client_docs` → `ready_to_file` → `submitted` |
| AP Workflow | `open` → `pending_client_approval` → `remediating` → `closed` |
| Tax Cadence | `scheduled` → `in_review` → `escalated` → `completed` |
| Onboarding Admin | `queued` → `in_progress` → `waiting_access` → `completed` |

**Common engagement annotation queue ID:** `ENG-BUDGET-acme_cloud-FY2026-Q1` (referenced in scen_065 change-order workflow).

---

## Linear Structure

**6 teams · 8 projects · 30 issues · 25 comments · 44 users · 67 memberships.** Used for systemic-issue tracking, not routine close work.

### Teams

| Team ID | Name |
|---------|------|
| `team_acctops` | Accounting Operations |
| `team_tax` | Tax |
| `team_comp` | Compliance |
| `team_audit` | Audit |
| `linear_5477c0808ac2` | Client Accounting Operations |
| `linear_7d4b3f1127cd` | Tax & Compliance Delivery |

### Projects

| Project ID | Name | Team |
|------------|------|------|
| `proj_monthly_portfolios` | Monthly Portfolio Delivery | Accounting Operations |
| `proj_qtr_tax_deadlines` | Quarterly Tax Deadline Readiness | Tax |
| `proj_aml_onboarding` | AML and Onboarding Control Improvements | Compliance |
| `proj_audit_docs` | Audit Support and Documentation Pack | Audit |
| `linear_63697b7dff5c` | AP workflow standardization for managed clients | Client Accounting Operations |
| `linear_feeee7292b66` | Multi-state annual report catch-up for overdue client entities | Tax & Compliance Delivery |
| `linear_de68751be591` | Audit PBC backlog burn-down for retail client group | Tax & Compliance Delivery |
| `linear_ecebc0cac4bf` | Legacy bookkeeping cleanup and opening balance remediation | Client Accounting Operations |

The **AP workflow standardization project** (`linear_63697b7dff5c`) is the primary destination for systemic-issue tickets surfaced by the 8 AP escalation scenarios.

---

## Slack Channels (11)

10 working channels (C001–C010) plus one auto-created placeholder (`C012`), which brings the channel count to 11.

| Channel ID | Name | Purpose |
|------------|------|---------|
| C001 | #general | Firm-wide updates |
| C002 | #water-cooler | Non-work chatter |
| C003 | #announcements | One-way broadcast |
| C004 | #client-onboarding | Kickoff, document collection, scope setup, new-client handoff |
| C005 | #monthly-close-coordination | Close timelines, reconciliations, review items (most active) |
| C006 | #tax-prep-and-filings | Return prep, extension tracking, filing deadlines |
| C007 | #audit-engagements | Audit support, PBC tracking, workpaper coordination |
| C008 | #compliance-and-registrations | Compliance calendars, registrations, annual reports, AML |
| C009 | #cash-management-and-banking | Bank feeds, treasury, signatory changes, payment workflows |
| C010 | #vendor-bills-and-ap | Vendor onboarding, invoice handling, AP exceptions |
| C012 | *(auto-created placeholder)* | Empty system-generated channel — not used for real coordination |

---

## Communication & Coordination Components

| Component | Count | Purpose |
|-----------|------:|---------|
| Email | 1,379 entries | 1,379 email messages. Formal internal/external comms; audit trail |
| Slack | 2,613 entries | 2,545 messages + 11 channels + 57 users. Quick internal coordination |
| Messaging | 202 conversations | DMs and small-group threads (compliance signal-checks, partner-routed reviews) |
| Calendar | 51 events | Close kickoffs, partner reviews, lock targets, audit kickoffs |
| Reminder | 53 reminders | SLA tracking, filing deadlines, recurring milestones |
| Contacts | 63 contacts | Vendor, client, regulator records (v47 added 6 for the new personas) |

---

## Compliance & Approval Rules

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
| AP approval > $50,000 | Managing Partner (Steven Perry — Brookfield/Acme · Matthew Li — Northstar · Andrea Phil — de-minimis) |

### Regulatory exposure

| Regime | Exposure |
|--------|----------|
| Data Protection Act 2018 / GDPR-style privacy | Up to 4% of worldwide turnover for serious violations |
| AICPA SQMS 1 + Code of Professional Conduct §1.700 | Fines up to $10,000/member; possible loss of practice rights |
| AML supervision (BSA / FinCEN CDD + BOI) | Fines, business restriction, criminal exposure |

### Named policies

IT Usage Policy, Employee Code of Conduct, Anti-Money Laundering Policy.

### Hard SLAs

- **24h** client query response
- **≥ 5 business days** between work submitted to review and the delivery deadline
- IRS quarterly sales tax / annual corporate tax — non-negotiable statutory deadlines
- Management accounts due by the **15th of the month**
- BD-day calendar: BD0 kickoff → BD1 close entries → BD3 period lock → BD5 close → BD6–7 MAP sign-off → BD8 archival

---

## Task Categories — Quick Reference

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

The full catalog with subcategories, build blocks, and worked examples is in [`03_TASK_CATEGORIES`](03_TASK_CATEGORIES%20-%20BROOKFIELD%20UNIVERSE.html).

---

## Scenario Index (52 merged YAMLs; 9 partial + 10 stage-1 checkpoint files exist but are not scripted anchors)

Full descriptions in [`04_SCENARIO_STORYLINES`](04_SCENARIO_STORYLINES%20-%20BROOKFIELD%20UNIVERSE.html). Compact mapping:

| Family | Primary cat | Scenarios |
|--------|:-----------:|-----------|
| Monthly Management Accounts / Close (5) | 1 | scen_023, 024, 025, 027, 028 |
| Orphan Exception / Stale SLA / Live Triage (15) | 7 | scen_001, 005, 006, 009, 010, 011, 012, 013, 014, 015, 018, 019, 020, 021, 022 |
| AP Escalation (8) | 6 | scen_029, 030, 031, 032, 033, 034, 035, 036 |
| Recon Currency Refresh (2) | 7 | scen_039, 040 |
| Audit & Compliance (5) | 4 / 5 | scen_041, 042, 043, 044, 048 |
| Tax & Regulatory (3) | 3 | scen_045, 046, 047 |
| Adjusting / Recon / FX / Bad Debt / WIP / Fixed Asset (6) | 1 / 7 | scen_051, 053, 055, 056, 058, 059 |
| AML, Engagement Mgmt, Quarterly AR, Sales Tax, Annual Tax (8) | 3 / 4 / 8 | scen_061, 062, 063, 064, 065, 066, 067, 068 |
| **Total present** | | **52** |

### Checkpoint / partial (not merged)

| Scenario | Family | Status |
|----------|--------|--------|
| scen_002, 004, 007, 008, 016, 017 | orphan_exception | Stage-2 LLM pathology |
| scen_037, 038 | recon_currency_refresh | Stage-2 pathology |
| scen_043_diag | audit_compliance diagnostic | Diagnostic build of scen_043 |
| scen_026, 049, 052, 054, 057, 060 | earlier v2-loop deferrals | Documented in `SCENARIO_LOG.md` |

---

## Entity coverage

| Entity | Scenarios touching it | Notes |
|--------|----------------------:|-------|
| **Brookfield CPAs & Advisors** | 27 | Internal close, AR write-off, WIP, orphan exceptions, AP escalations, state catch-up, quarterly control tests |
| **Northstar Legal LLP** | 14 | Annual accounts, audit kickoff, annual tax, AML triage, partnership-distribution planning, orphan exceptions, CrownPeak AP escalations |
| **Acme Cloud Inc** | 15 | Outsourced bookkeeping, multi-state sales tax, AML wire-flag, BO refresh, OOS review, change order, quarterly AR, FX revaluation, prepaid setup, AP escalations |
| **Mixed / firm-internal** | ~5 | Quarterly control tests, Pinecrest AP escalation, recon-currency-refresh scen_040 |

---

## Universe past-cutoff scan (today = 2026-06-12)

The universe is **clean past June 12**. Only 12 records dated after today, all legitimately forward-looking:

| Cluster | Count past today | Reason |
|---------|----------------:|--------|
| Oracle GL `fiscal_periods` FP-2026-06 (3 entities) | 3 | `status=future` — empty period shells for next-period posting (standard) |
| SAP AP invoices with `due_date` June 13–22 | 9 | Upcoming payment queue (standard 30–60 day vendor terms) |
| **Total** | **12** | All legitimate forward-looking |

The previously-flagged 17 Records Vault `document_versions` outliers (uploaded_at extending to July 16) have been re-timestamped backward into the May 6 → June 12 window — no longer outliers.

---

## Document map

| Doc | Purpose |
|-----|---------|
| [`01_SUMMARY`](01_SUMMARY%20-%20BROOKFIELD%20UNIVERSE.html) | Universe summary — firm, org chart, NPCs, systems, scenarios, today date. |
| [`02_PERSONA_BRIEFS`](02_PERSONA_BRIEFS%20-%20BROOKFIELD%20UNIVERSE.html) | The 34 personas, each with author-in mapping, open threads, scenario footprint. NPCs are not in this doc — see this file for the NPC roster. |
| [`03_TASK_CATEGORIES`](03_TASK_CATEGORIES%20-%20BROOKFIELD%20UNIVERSE.html) | The 10 task categories with subcategories, build blocks, worked examples, and the canonical persona → category mapping. |
| [`04_SCENARIO_STORYLINES`](04_SCENARIO_STORYLINES%20-%20BROOKFIELD%20UNIVERSE.html) | All 52 merged scenarios documented with entity, anchor IDs, role assignments, components, primary category. |
| [`05_ARTIFACTS`](05_ARTIFACTS%20-%20BROOKFIELD%20UNIVERSE.html) | This file — universe reference sheet: personas, NPCs, systems, schemas, useful accounts, scenario index, persona ↔ scenario matrix. |
| [`06_GLOSSARY`](06_GLOSSARY%20-%20BROOKFIELD%20UNIVERSE.html) | Term-by-term glossary of accounting jargon, abbreviations, and universe-specific conventions. |