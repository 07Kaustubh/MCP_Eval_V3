# Task Categories — Brookfield CPAs & Advisors

This document is the operating manual for task authoring at Brookfield. It describes the **10 categories** of work the firm produces, what each one means in plain accounting terms, the rules and tools the work runs against, the sub-tasks inside it, and worked examples drawn from the universe's actual scenario set.

It is written for a generalist audience — you do **not** need an accounting background to read it. Every accounting concept is explained in the text where it first appears. If you want even more background, see [`06_GLOSSARY`](06_GLOSSARY%20-%20BROOKFIELD%20UNIVERSE.html) for term-by-term definitions.

## How to use this guide

1. **Pick the acting persona** for your task from [`02_PERSONA_BRIEFS`](02_PERSONA_BRIEFS%20-%20BROOKFIELD%20UNIVERSE.html). The persona briefs each say which categories the person can author tasks in.
2. **Open the matching category block below**, read the *What it is* and *Why it matters* sections to ground the work, scan the subcategories, and read at least one worked example.
3. **Confirm anchors against the live universe.** Account numbers, scenario IDs, persona names, vendor names — everything in the examples is real, but always cross-check the live data before committing.
4. **Write the task prompt in the natural style** — as a real colleague handing off work. Make the task genuinely hard, not just long.

> **A note on the `*Prompt written by …*` lines below each worked example.** These are a documentation convention used *only inside this guide* to identify the protagonist persona behind the example. The persona never appears in the actual prompt — real prompts contain only the task itself, written in the protagonist's voice. Read the attribution lines as reader-facing labels, not as something to copy.

## Universe constants

| | |
|---|---|
| Firm | Brookfield CPAs & Advisors — US public accounting & advisory firm, partner-led, private |
| Fiscal year end (all entities) | **12-31** |
| "Today" (current date in agent prompts) | **2026-06-12**, US/Eastern |
| Email domain | `brookfieldcpas.com` |
| Entities | `brookfield` (firm's own books) · `northstar_legal` (law-firm client, IOLTA trust `105000` — *IOLTA = Interest On Lawyers Trust Account, the segregated client-funds account US lawyer-trust rules require law firms to maintain*) · `acme_cloud` (B2B SaaS client) |
| Systems of record | **Oracle GL** (ledger) · **SAP Subledger** (AP, fixed assets, prepaid, lease detail — *being consolidated into Oracle GL by an Oct 2026 cutover per the SAP→Oracle migration plan in Records Vault*) · **BlackLine** (reconciliations) · **Records Vault** (documents) |
| Coordination | Airtable (workflows) · Linear (issues) · Email · Slack · Messaging · Calendar · Reminder · Contacts |
| Retention codes for filed documents | `AICPA_SQMS_7Y` (default, 7y) · `IRS_TAX_7Y` (tax records, 7y) · `FIRM_INTERNAL` (engagement letters, 5y) · `INDEFINITE`. **Never use `SOX_7Y` or `SEC_PERMANENT` — they do not exist.** *Why these matter:* the retention tag is what determines (a) how long the firm is required to preserve a document under AICPA/IRS rules, (b) what the audit trail must show if the document is ever requested by a regulator, and (c) when the firm is permitted to delete the document without exposure. Mis-tagging a workpaper as `FIRM_INTERNAL` instead of `AICPA_SQMS_7Y` could mean the firm deletes audit-relevant evidence two years too early. Tasks that touch retention are testing whether the agent picks the correct code for the document's actual content, not the easiest one. |
| Classifications | `internal` (default, ~99% of artifacts) · `restricted` (AML files, executive comp, audit folders, partner-only memos). The `public` classification value exists in the schema but **no document in the universe currently uses it** — do not author prompts that produce `public` artifacts unless you are deliberately introducing the first one. |
| Universe total | 22,950 entries across 12 services; 52 merged scenarios + 9 partial + 10 stage-1 checkpoint = 71 scenario YAMLs. **34 authoring personas** (covering 8 departments including the new `procurement` function) + **29 NPCs** = 63-person named cast inside the firm. |

### Universal conventions for journal entries (JEs)

These rules apply across every category that touches Oracle GL:

- **JE lifecycle:** `draft → submitted → approved → posted → (reversed)`. Rejected JEs go back to the preparer.
- **Minimum 300 seconds between state transitions.** If you submit at 09:56:00, the earliest you can approve is 10:01:00.
- **Closed-period posting needs `late_post_authorization_id`.** Without it, the post is rejected.
- **Entity-prefixed IDs.** Period IDs look like `brookfield_FP-2026-04`; JE IDs look like `JE-acme_cloud-FP-2026-05-0012`. Bare `FP-2026-04` will fail.
- **`is_standard_entry: true`** = recurring monthly entry (accruals, depreciation, prepaid amortization). **`is_standard_entry: false`** = adjusting entry (variance correction, reclass, one-off).
- **Every adjusting JE needs a supporting attachment** filed to Records Vault, and a reviewer separate from the preparer.

### Universal conventions for reconciliations (BlackLine)

- **Reconciliation (recon) lifecycle:** `open → in_progress → submitted → approved → certified → archived` (plus `overdue` as a side state). A *reconciliation* compares the GL balance for an account against supporting detail (subledger, bank statement, vendor confirmation) and explains any variance.
- **Variance materiality thresholds:** under $10 is immaterial and acceptable; under $1K should be addressed but is not critical and may be fixed via a JE in a subsequent month; over $1K is urgent and demands investigation and a documented explanation.
- **Exception types (6):** `duplicate_entry_detected`, `unrecorded_invoice`, `timing_difference_over_sla`, `fx_revaluation_drift`, `subledger_feed_drop`, `missing_accrual_variance`.
- **Exception states:** `logged → investigating → awaiting_approval → closed`.

---

# Distribution

| # | Category | Training | Benchmark |
|---|---|--------:|---------:|
| 1 | Accounting Operations | 90 | 30 |
| 2 | Bookkeeping | 24 | 8 |
| 3 | Tax | 30 | 10 |
| 4 | Compliance & Internal Controls | 30 | 10 |
| 5 | Audit | 18 | 6 |
| 6 | AP / Vendor Operations | 36 | 12 |
| 7 | BlackLine Close-Discipline & Variance | 30 | 10 |
| 8 | Engagement Mgmt & Client Operations | 21 | 7 |
| 9 | Executive / Partner Oversight | 12 | 4 |
| 10 | HR & People Operations | 9 | 3 |
| | **Total** | **300** | **100** |

---

# Persona → Category mapping

Use this when authoring as a given persona. Seniority sets whether they prepare, review, or approve within a category — a trainee drafts, an associate prepares, a senior owns, a manager reviews, a partner signs off.

| Persona(s) | Role | Authors tasks in |
|---|---|---|
| **George McAdam** *(primary)*, Edith Banda, Jones Harrison | Accounts Senior | 1, 2, 5, 7, 8 |
| Daniel Jones | Accounts Manager | 1, 2, 5, 6, 7, 8 |
| Harry Marks, Emily Adekole, Blue Evans | Accounts Associate | 1, 2, 7 |
| Green Spatz, Anaya Wallace | Trainee Accountant | 1, 2, 7 |
| Elita Moore | Accounts Graduate Trainee | 1, 2, 7 |
| Ben Arinzo, Sean Williams | Bookkeeper | 2, 6, 7 |
| **Priya Khatri** | AP Coordinator | 6 |
| **Tariq Soto** | AP Clerk | 6 |
| **Lena Park** | Procurement Officer | 6 |
| **Marcus Knell** | Billing Coordinator | 1, 8 |
| Tom Chang | Tax Associate | 3 |
| William White | Corporate Tax Associate | 3 |
| Hannah Grant | Corporate Tax Senior | 3 |
| Alex Cahoon | Corporate Tax Manager | 3 |
| Ming Chang | Tax Partner | 3, 9 |
| Marina Soko | Compliance Officer | 4 |
| Peter Sanchez | Head of Compliance | 4, 9 |
| **Mia Hartwell** | Audit Staff | 5, 7 |
| Ryan Delgado | Audit Senior | 5, 7 |
| **Devon Beale** | Audit Manager | 5 |
| Julia Vance | Audit Partner | 5, 9 |
| Andrea Phil | Partner, Accounting Services | 1, 5, 6, 8, 9 |
| Matthew Li | Accounting Services Partner | 1, 5, 6, 8, 9 |
| Steven Perry | Managing Partner | 6, 9, 10 |
| Brent Noah | Director of People and Culture | 10 |
| Clint Peterson | HR Operations Manager | 10 |
| Rachel Green | HR Business Partner | 10 |
| Reshma Patel | HR Generalist | 10 |

**Rules.**
- **Only personas author tasks.** This table lists the 34 generated personas eligible to be the acting voice on a task. NPCs (Owen Mercer, Brenda Abbas, Sofia Halabi, Farah Dlamini, James Randall, Lucia Ferreira, Margot Reyes, Anaya Patel, Mateo Kovac, Nia Okafor, Yusuf Demir, etc.) are **never** acting seats — they appear as participants, counterparties, or subjects inside other personas' tasks.
- **The six new v47 personas** (Mia Hartwell, Devon Beale, Priya Khatri, Tariq Soto, Lena Park, Marcus Knell) are full eligible authoring seats but **don't yet appear in any of the 52 scripted scenarios**. They're available for new task design — pair them with the existing scenarios where their role fits, or build tasks from spec.
- **HR personas are eligible acting seats**, like every other persona. They author Category 10 tasks (onboarding routing, appraisal scheduling, EEOC liaison, dispute coordination), and they appear as participants/counterparties in cross-functional tasks authored from other categories. Their scenario footprint is smaller than the accounting/tax/audit personas — reflect that in volume, not in eligibility.
- **Partners and managers** also appear as reviewer/approver *inside* other personas' tasks. Only author a task *as* a partner when the work is genuinely theirs (sign-off, partner risk pull, refusal decision).
- **External people** (regulators, vendors, client-side staff — e.g., Brenda Abbas, Priya Singh, Anita Knowles, Margaret Sullivan, James Randall) are coordinated *with*, never authored *as*.

---

# Category 1 — Accounting Operations

## What it is

Every month and every quarter, accounting firms must **close the books** — both for themselves and for each of their clients. Closing the books means locking the period so no more transactions can be added or changed, after which the firm produces the period's financial statements, dashboards, and partner sign-off package. This category covers everything from posting the standard recurring entries on the first business day after period-end through to the final partner sign-off on the Management Accounts Package (MAP).

Closing happens on a recurring cadence:

- **Month-end close** is the routine cycle. It runs for roughly five business days after the last day of the month.
- **Quarter-end close** runs every three months on top of the monthly cycle and produces additional partner reporting (Category 8.4 / Category J in some legacy references). It typically takes longer and includes more journal entries than a month-end.
- **Year-end close** is the heaviest. It feeds into the annual financial statements deliverable in Category 5 and the partnership/corporate tax returns in Category 3.

The single most important rule running through every close is the **matching principle**: revenue and expenses must be recorded in the period when they occur, **not when cash is received or paid**. A monthly software subscription paid in April but covering May/June service must be recorded as April-prepaid and then expensed across May and June. A consulting fee earned in June but invoiced in July must be recognized as June revenue. Half of all close work is enforcing this principle.

## Why it matters

A clean close drives every downstream deliverable:

- **Client trust.** A late or sloppy MAP undermines the engagement.
- **Statutory deadlines.** The 15th-of-month management-accounts deadline is non-negotiable per the engagement letter.
- **Audit and tax.** Year-end annual accounts (Category 5) and federal/state tax returns (Category 3) draw directly from the closed periods. A reopened period is expensive — late-post authorization is required, the audit trail expands, and reviewers re-scope.

## Authoring checklist

> **🎓 CPA-heavy category.** The close cycle is built on three accounting concepts that show up in every Category 1 task: **adjusting journal entries** (entries that correct, accrue, or defer items so they land in the right accounting period), the **matching principle** (revenue and expenses are recorded when they occur, not when cash moves), and the **ASC standards** that apply most heavily to Acme — ASC 606 (deferred revenue release on prepaid subscriptions), ASC 340-40 (capitalized sales commissions amortized over the contract life), and ASC 842 (right-of-use lease assets). You'll see these in close JEs, MAP review, WIP-to-revenue recognition, and working-paper sign-off. The narrative sections below explain each concept inline as it first appears, so anyone working through this guide can follow the workflow end-to-end and write a task that holds up under review.

| Field | Value |
|---|---|
| **Eligible acting personas** | **Andrea Phil**, **Matthew Li** (partners — sign-off + period lock); **Daniel Jones** (manager — review + close coordination); **George McAdam** *(primary)*, **Edith Banda**, **Jones Harrison** (seniors — own the working file); **Harry Marks**, **Emily Adekole**, **Blue Evans** (associates — prepare entries); **Green Spatz**, **Anaya Wallace**, **Elita Moore** (trainees — draft entries under senior review); **Marcus Knell** (Billing Coordinator — owns the WIP-to-invoice conversion and coordinates revenue-recognition timing with Accounting Services; natural author for tasks that bridge billing into Cat 1.4 WIP recognition). |
| **Other entities touched** | All three: `brookfield`, `northstar_legal`, `acme_cloud`. Each entity runs its own close on the same BD0–BD8 cadence. Acme is the most ASC-heavy. |
| **External / NPC participants** | **Lucia Ferreira** (admin participant on access provisioning if the close needs it); **Margaret Sullivan** (client-side reviewer at the Q1 partner-package level for some engagements). NPCs do not author Cat 1 tasks. |
| **Primary systems** | **Oracle GL** (close JEs, `fiscal_periods` state, `bd3_lock_at` / `bd5_close_at`, late-post authorization); **BlackLine** (close-task checklist, period reconciliations); **Records Vault** (MAP, support memos, working files — `AICPA_SQMS_7Y`); **SAP Subledger** (fixed-asset depreciation, prepaid amortization schedules, AR feed — *AR = Accounts Receivable, money owed to the firm by clients*); **Email + Slack `#monthly-close-coordination`** (review coordination); **Calendar** (close kickoff + sign-off windows). |
| **Primary artifacts** | Standard and adjusting JEs (`is_standard_entry: true` for recurring, `false` for reclass); BlackLine reconciliations and close tasks; **Management Accounts Package (MAP)** under `kind: management_accounts_package`; working file + reviewer cover note; fiscal-period state (`status: open → locked`). |
| **Linked study scenarios** | scen_023, 024, 025, 027, 028 (month-close anchors); scen_051 (fixed-asset month-end); scen_055 (foreign-currency / FX revaluation); scen_056 (bad-debt write-off); scen_058 (Northstar Q1 partner package); scen_059 (WIP recognition); scen_063 (Northstar annual accounts as close artifact). |

## The close calendar

The firm runs on this standard rhythm:

| Day | What happens |
|-----|--------------|
| **BD0** (last day of period) | Partner runs the kickoff. Plan covers what entries are due, who reviews, when the lock target is. AP cuts off at end of day. A final bank feed runs. Currency rates are snapshotted and emailed. New fixed assets are added. Billing closes accounts receivable for the period. |
| **BD1** | Close-period **journal entries** posted: standard accruals, prepaid amortization releases, monthly depreciation (Oracle/SAP run this automatically in most cases; manual when a true-up is needed), ASC 606 deferred-revenue release (Acme), ASC 340-40 commission amortization (Acme), R&D accruals (Acme), credit-card accruals from the prior month's statement (some lines route to fixed-asset or prepaid accounts rather than expense). The 6 "June 1 BD1" JEs in this universe are FP-2026-05 BD1 postings (`je_855f1b9deccb4502` and siblings). |
| **BD2** | Reviewer feedback returns. Operating expense report run to verify charges are in the correct period. Credit card reconciliation prepared (matching transactions to employee receipts; chase missing receipts). Revenue and cash entries finalized. |
| **BD3** | Prepaid amortization entries and remaining expense entries finalized. **Period lock target.** `bd3_lock_at` is the *scheduled* lock timestamp on the fiscal period — for FP-2026-05 across all three entities, that target fell on 2026-06-03 (around midday ET; the exact timestamp varies slightly by entity). As of today (2026-06-12), the FP-2026-05 periods are **still `status=open`** (`locked_by=null`, `locked_at=null`) — the lock-target deadline has passed but no one has actually locked, which is itself a plausible task setup. Once a partner does lock, the period moves to `locked` and any further posting requires `late_post_authorization_id`. |
| **BD4** | All entries that affect expenses or revenue should be complete. |
| **BD5** | **Period close.** Non-revenue/expense entries finalized (e.g. internal reclassifications between asset accounts). Final reconciliations completed. Financial analysis begins. |
| **BD6–BD7** | Management Accounts Package (MAP) sign-off. |
| **BD8** | Archival — BlackLine reconciliations move to `archived` state. |

Quarter-end closes typically extend a few days past BD8. Some clients have shorter close windows by engagement; others longer.

## What sits inside a close

Two categories of work run inside a close, both essential:

### Adjusting journal entries

These post during BD1–BD3 and represent the bulk of the preparer's work. Sub-types:

- **Prepaid amortization.** Move funds from prepaid asset accounts to the expense accounts they should hit for the period. The five prepaid accounts in scope are `130000` Prepaid Insurance, `131000` Prepaid Software, `132000` Prepaid Facilities Maintenance, `133000` Prepaid CPE/CLE (Brookfield/Northstar only), `134000` Prepaid Other Operating, and the v47-added `135000` Prepaid Marketing (per-entity; "& Advertising" on Acme). Frequently routed by invoice and largely automated, but adjusting entries are made to correct errors that the AP team couldn't fix at source, or to amortize credit-card charges that came in late.
- **Depreciation.** Monthly depreciation of fixed assets, recorded as a debit to `570000` Depreciation Expense and a credit to the matching accumulated-depreciation contra-account (`158xxx`). Oracle and SAP run this automatically in most cases. Manual depreciation runs are occasional.
- **Deferred revenue release.** When a client prepays for services not yet delivered, the prepayment sits as a liability. As service months pass, the liability is released to revenue. Acme Cloud has heavy deferred-revenue exposure as a SaaS company — annual subscriptions need monthly release entries under ASC 606.
- **Unbilled (accrued) revenue recognition.** When work is performed but not yet invoiced, revenue must still be recognized. A contract that bills at 25 %, 50 %, and 100 % completion needs interim entries when only 10 % or 20 % of the work has happened. The account this sits on is `119000` — **Work in Process – Unbilled Services / Time**, commonly abbreviated **WIP** throughout this doc. WIP in this firm always means *unbilled revenue / unbilled services*, not the manufacturing meaning of work-in-process inventory. This is the WIP-to-revenue pattern that drives scen_059.
- **Deferred commissions amortization.** Sales commissions paid up front for multi-year contracts are capitalized as `120000` Deferred Commissions (Acme, ASC 340-40) and amortized monthly. Acme is the only entity with this.
- **Credit card accruals.** When the credit card statement arrives, AP creates a journal entry to recognize the expenses. Some lines route to fixed-asset or prepaid accounts rather than direct expense.
- **Bad-debt write-offs.** Aged receivables that are no longer expected to be collected are written off against the `117000` Allowance for Doubtful Accounts (the allowance method). The Ridgepoint write-off in scen_056 is the universe example.
- **FX revaluation.** Non-USD balances are revalued at the period-end exchange rate. The FP-2026-04 FX revaluation on Acme is scen_055.

**All adjusting journals require an attachment** (supporting calculation, invoice, screenshot, memo) filed to Records Vault, and **must be reviewed by someone other than the preparer**.

### Account reconciliations and financial-statement preparation

Account reconciliations (deeper coverage in Category 7) finalize during the close itself; financial statements are exported automatically from Oracle GL but the preparer must interpret and analyze the variances.

## Subcategories

### 1.1 Monthly & Quarter-End Close Execution

The standard BD0–BD8 cycle described above, end-to-end. Each entity (Brookfield, Northstar Legal, Acme Cloud) runs its own monthly close. Acme has the most complex close because of ASC 606/340-40 layering. **Quarter-end closes** follow the same shape but typically run a few days longer and produce more journal entries — the partner reporting deliverable that rides on top of a quarter-end close is covered in subcategory 1.3.

**Read:** `oracle_gl_get_fiscal_period_by_id`, `oracle_gl_list_journal_entries`, `blackline_list_reconciliations`, `blackline_list_close_tasks`, `records_vault_search_documents` (prior MAP), `airtable_list_records`, `calendar_list_events`, `conversations_history` on #monthly-close-coordination.

**Write:** `oracle_gl_create_journal_entry` → submit → approve → post, `oracle_gl_lock_period`, `blackline_submit_reconciliation` / approve / certify / archive, `records_vault_upload_document` (`kind: management_accounts_package`), `email_send_email`, `airtable_update_record`.

**Linked scenarios:** scen_023, 024, 025, 027, 028.

**Example.**

> The May close for Acme Cloud (`acme_cloud_FP-2026-05`) is at BD1. Jones Harrison's BD0 kickoff with Andrea Phil laid out the plan — the standard accruals, prepaid CPE amortization, monthly depreciation, ASC 606 deferred-revenue release, ASC 340-40 commission amortization, R&D accrual, plus a Datadog enterprise-renewal reclass (`500000` → `521000`) Andrea wants quantified before lock. Pull the FP-2026-04 MAP and the standing close-schedule support from Records Vault, post the BD1 JEs with correct `is_standard_entry` flags (recurring ones `true`, the Datadog reclass `false`), confirm every open BlackLine reconciliation has evidence attached, upload the draft MAP under `AICPA_SQMS_7Y`, and hand off to Daniel Jones for review in #monthly-close-coordination, tagging Andrea. Do not lock — that's the partner's call.
>
> *Prompt written by Andrea Phil, Partner, Accounting Services.*

### 1.2 Annual Accounts Preparation

The year-end deliverable. Senior collates the working file → manager drafts a review memo → partner performs the US GAAP review → partner signs off. Working papers are filed under `AICPA_SQMS_7Y`; the final annual accounts package is filed as `kind: annual_accounts_package`.

This subcategory overlaps Category 5 (Audit) when the engagement also carries an external audit. The annual accounts produced here are the input to the external auditor's fieldwork.

**Linked scenarios:** scen_063 (Northstar Legal FY2025 annual accounts).

**Example.**

> Northstar Legal's FY2025 annual accounts are ready for partner GAAP review. Daniel Jones's review memo is in Records Vault (Northstar FY2025 folder); George McAdam's working file went up the day before. Pull the working file, the FY2024 comparator, and the review memo. Cross-check every JE cited in Daniel's commentary against Oracle GL (`northstar_legal_FP-2025-*`). Spot-check fixed-asset depreciation against SAP. Verify the IOLTA-trust roll-forward reconciles. Flag any GAAP disclosure that looks thin against prior year. Upload the clean draft plus your reviewer cover note and email Andrea Phil for partner sign-off.
>
> *Prompt written by Daniel Jones, Accounts Manager.*

### 1.3 Quarterly Reporting / Partner Package

Build the quarterly dashboard plus the partner cover note: P&L, cash, AR, WIP, JE summary across the three months. Numbers come from the GL, narrative from the partner. Cross-references Category 8.4 (client-side delivery).

> **Design note.** Only one quarterly-package scenario is anchored in the universe (scen_058 Northstar Q1). Author additional 1.3 tasks by building from the BD0–BD8 close shape plus the quarterly extension — don't expect a scripted twin to exist for Acme or Brookfield Q1/Q2 packages. The realistic cadence is one quarterly package per entity per quarter, so additional 1.3 tasks must be designed against the closed periods rather than copied from a scenario.

**Read:** `oracle_gl_get_fiscal_period_by_id` (the three quarter periods), `oracle_gl_search_journal_entries`, `records_vault_search_documents` (prior quarterly package format), `blackline_list_reconciliations` (quarter-end recons).

**Write:** `records_vault_upload_document` (`kind: quarterly_reporting_package`, retention `AICPA_SQMS_7Y`), `email_send_email` (last-pass review → partner sign-off), `airtable_update_record`.

**Linked scenarios:** scen_058 (Northstar Q1 partner package).

**Example.**

> Northstar Legal's Q1 2026 partner package goes to Matthew Li by EOD Friday. Pull the closed `northstar_legal_FP-2026-01` through `northstar_legal_FP-2026-03` from Oracle GL and cross-check every JE cited in the draft Q1 package against the closed periods. Verify the IOLTA-trust roll-forward on `105000`, the WIP balance on `119000`, and the AR aging snapshot on `110000` all tie to the supporting workpapers. Update the partner cover note flagging the two largest write-offs and the most material new accrual. Upload the final package to Records Vault under `AICPA_SQMS_7Y` and email Daniel Jones for last-pass review before partner sign-off.
>
> *Prompt written by Edith Banda, Accounts Senior.*

### 1.4 WIP Recognition & Stage-Completion Recognition

When work has been performed but not yet billed (e.g. a fixed-fee engagement where 25 %/50 %/100 % billing milestones lag the actual hours worked), Andrea Phil produces a stage-completion schedule and the preparer books the WIP-to-revenue recognition JE against `119000` WIP.

**Read:** `records_vault_search_documents` (stage-completion schedule), `blackline_get_reconciliation_by_id` (WIP recon), `oracle_gl_search_journal_entries` (prior-period precedent).

**Write:** `oracle_gl_create_journal_entry` (`is_standard_entry: false`), `records_vault_upload_document` (support memo, `AICPA_SQMS_7Y`).

**Linked scenarios:** scen_059 (Brookfield FP-2026-05 WIP recognition, $4,390.62 on recon `BL-75810CD0FEE4`).

**Example.**

> Andrea Phil's May engagement-stage completion schedule landed in Records Vault yesterday. Pull it and the in-progress BlackLine WIP reconciliation `BL-75810CD0FEE4`, identify which WIP balances need to roll into recognized revenue this period, and post the WIP-to-revenue JE on `brookfield_FP-2026-05` (`is_standard_entry: false`). Mirror the FP-2026-04 line shape but pull amounts from Andrea's schedule. Route the JE through its full lifecycle (5-minute minimum between transitions). Upload a one-page support memo to Records Vault under `AICPA_SQMS_7Y` citing the schedule version and the recon ID, then tag Andrea in #monthly-close-coordination once posted.
>
> *Prompt written by George McAdam, Accounts Senior.*

### 1.5 Working Paper Preparation & Review

The reviewer chain that sits behind every formal deliverable — monthly close, quarterly package, annual accounts. The senior prepares the working file (calculations, tie-outs, source-doc references), the manager writes a review memo flagging anything that doesn't tie, and the partner signs off. The reviewer must verify **every JE cited in the working papers actually exists** in Oracle GL, depreciation ties to SAP, and trust roll-forwards reconcile.

**Read:** `records_vault_search_documents` (`kind: workpaper`, prior-period working files), `oracle_gl_search_journal_entries` (JE verification), `blackline_list_reconciliations`, `sap_subledger_list_fixed_assets`.

**Write:** `records_vault_upload_document` (`kind: workpaper`, retention `AICPA_SQMS_7Y`), `email_send_email` (review-memo handoff), `conversations_add_message`.

**Linked scenarios:** scen_058 (Northstar Q1 working-paper review pattern), scen_063 (annual accounts working-paper chain).

**Example.**

> The Northstar Q1 2026 working papers are ready for manager review before they go to Matthew Li. Pull Edith Banda's draft from Records Vault under the Northstar FY2026 Q1 folder. Verify every JE cited in her cover commentary against Oracle GL (`northstar_legal_FP-2026-01` through `northstar_legal_FP-2026-03`), spot-check the depreciation lines against SAP, and confirm the IOLTA-trust roll-forward ties end-to-end. Flag any number that doesn't tie or any disclosure that's thin against the FY2024 comparator. Write your review memo to Records Vault under `AICPA_SQMS_7Y` and email Edith with the items she needs to address before partner review.
>
> *Prompt written by Daniel Jones, Accounts Manager.*

---

# Category 2 — Bookkeeping

## What it is

Bookkeeping is the daily, transaction-level work that keeps the general ledger fed and trustworthy. It is what happens *between* closes. Before any close can run cleanly, bookkeepers have spent the month coding incoming transactions, attaching receipts, reconciling bank feeds, and pulling supporting documentation from clients. If the bookkeeping is sloppy, the close is sloppy.

Bookkeeping at Brookfield is performed both for the firm's own books and for outsourced clients (Acme Cloud's full bookkeeping is outsourced; Northstar Legal gets bookkeeping cleanup engagements). The people here are Ben Arinzo and Sean Williams (personas), with Mateo Kovac and Nia Okafor as NPC bookkeepers.

## Why it matters

The bookkeeper sits between three pressures:

- **The client's source documents** (invoices, receipts, credit-card statements) that need to be unpacked, coded, and attached.
- **The bank feed** which automatically pulls daily transactions and waits for human coding.
- **The senior/manager** reviewing the work who will flag bad coding during close.

Bookkeeping also feeds two specialist surfaces:

- **AML signal-checks** (Category 4.2) — when Compliance needs to know "did unusual cash activity happen on this client's account last month?", the bookkeeper is the source.
- **AP escalations** (Category 6.1) — when an aged invoice is being escalated, the bookkeeper carries the institutional memory on vendor history, accrual treatment, and prior cost classifications.

## Authoring checklist

> **🛠 No-CPA-required category.** Bookkeeping is transaction-level operational work: coding incoming items to the right GL account, attaching supporting documents, triaging the daily bank feed, and pulling context for other teams when they ask. The concepts that show up in Category 2 tasks are **GL coding** (matching a transaction to the right account number on the chart of accounts using the client's coding memo), **bank-feed triage** (deciding which automatically-imported feed lines need human coding versus which auto-match cleanly), and **context retrieval** (pulling transaction history when Compliance or AP asks for it). None of this requires CPA-grade accounting judgment — it requires care, attention to detail, and familiarity with the firm's coding conventions, all of which the narrative and examples below walk through.

| Field | Value |
|---|---|
| **Eligible acting personas** | **Ben Arinzo**, **Sean Williams** *(primary — Bookkeepers)*; **Daniel Jones** (manager — when bookkeeping cleanup rolls up to manager-led work); seniors **George McAdam**, **Edith Banda**, **Jones Harrison** and associates / trainees can also author 2.1 when they're supporting a senior's close prep. |
| **Other entities touched** | All three: `acme_cloud` (full outsourced bookkeeping — the heaviest 2.x footprint), `northstar_legal` (cleanup engagements), `brookfield` (internal firm books). |
| **External / NPC participants** | **Mateo Kovac**, **Nia Okafor** (NPC bookkeepers — participants in vendor-history pulls); **Marina Soko**, **Farah Dlamini** (consume Cat 2.2 context for AML triage); **Owen Mercer** (NPC AP specialist — receives Cat 2.3 history summaries); various client-side contacts (e.g., **Liam Scotman** at Marksman Hardware, **Brenda Abbas** vendor-side) for receipt chases and history confirmation. |
| **Primary systems** | **Oracle GL** (coding JEs, subledger feeds, transaction search); **SAP Subledger** (AP invoice coding + AP-manager-level approval ≤ $10K, vendor-master records); **Records Vault** (per-client coding memos, vendor SOWs); **Airtable** (Close Blocker Triage Log); **Email** (client receipt chases); **Slack `#vendor-bills-and-ap`**; **Messaging** (DM channel for AML signal-checks). |
| **Primary artifacts** | Coding journal entries (transaction-level postings); AP invoice records and their status / approver fields; per-client coding memos; Close Blocker Triage Log entries; bank-feed run logs; vendor-history summaries (Cat 2.3 output). |
| **Linked study scenarios** | scen_062 (Ben Arinzo pulls Northstar cash context on `101000` / `105000` for Marina Soko's AML triage — the canonical Cat 2.2 anchor); scen_066 (Acme AR cash receipts — Cat 2.1 / 2.3 overlap). Bookkeeping is also implicit across most close scenarios (scen_023–028) as the underlying coding work the close depends on. |

## Subcategories

### 2.1 Routine Coding & Bank-Feed Triage

The everyday workflow. Bank-feed transactions arrive automatically each night; AP invoices come in as `pending_approval`; client receipts land in email or shared inboxes. The bookkeeper codes each to the correct GL account, attaches supporting documents, and routes for AP-manager approval where the amount is ≤ $10K.

**Read:** `oracle_gl_list_subledger_feeds` (status, last_run), `oracle_gl_list_subledger_feed_runs`, `sap_subledger_list_ap_invoices` (filter `status=pending_approval`), `conversations_history` on `#vendor-bills-and-ap`, `email_search_emails`.

**Write:** `oracle_gl_create_journal_entry` (coding entries), `sap_subledger_update_ap_invoice` (coding + AP-manager-level approval ≤ $10K), `airtable_update_record` (close-blocker entry), `email_send_email` (client doc chase), `conversations_add_message`.

**Linked scenarios:** Implicit across most monthly closes; explicit references in scen_062 (Ben Arinzo provides cash-account context) and scen_066 (Acme AR cash receipts).

**Example.**

> Marksman Hardware's May bookkeeping is overdue. Liam Scotman replied last week with the missing receipts but the email never got fully unpacked. Pull the email thread, attach the receipts to the matching SAP AP invoices, code the bank-feed transactions in Oracle GL against the Marksman coding memo in Records Vault, and close out the May line in the Airtable Close Blocker Triage Log. Email Liam to confirm May is closed and ask for June submissions by the 8th.
>
> *Prompt written by Ben Arinzo, Bookkeeper.*

### 2.2 Transaction-Context Pull for AML

When Compliance gets an adverse-media hit on a client's beneficial owner, they DM the bookkeeper to ask "what does the cash activity look like on this client's accounts for the last two periods?" The bookkeeper pulls the GL transactions on the cash accounts (`101000` operating, `105000` trust/IOLTA on Northstar) for the requested fiscal periods and reports the patterns back. This is comms-led, not posting work.

**Read:** `oracle_gl_search_journal_entries` filtered to the cash accounts and requested periods, `sap_subledger_list_subledger_transactions` (counterparty detail if needed).

**Write:** `messaging_send_message` (DM reply to Compliance), no GL writes.

**Linked scenarios:** scen_062 (Ben Arinzo pulls Northstar cash context for Marina Soko's adverse-media triage on accounts `101000` and `105000` for FP-2026-03 / FP-2026-04).

**Example.**

> Marina Soko DM'd this morning asking for a quick cash-account context pull on Northstar Legal — she's triaging an adverse-media partial-name match on one of the beneficial owners and wants to see if recent activity on the operating cash account (`101000`) and the IOLTA trust account (`105000`) shows anything unusual. Pull every Oracle GL transaction on those two accounts for `northstar_legal_FP-2026-03` and `northstar_legal_FP-2026-04`, group by counterparty, and reply to Marina on messaging with the top five largest movements plus any pattern that looks out of cadence vs. prior months. Keep it on messaging — not in Slack channels — until disposition lands.
>
> *Prompt written by Ben Arinzo, Bookkeeper.*

### 2.3 AP Accrual History & Vendor-Master Verification

When an aged AP invoice is being escalated (Category 6), the bookkeeper carries the institutional memory: what was the accrual history on this vendor? Was there a prior superseded Statement of Work (SOW)? Did the vendor-master record have stale terms? In the AP escalations Ben Arinzo and Mateo Kovac pull this kind of context to feed the AP manager's disposition.

**Read:** `oracle_gl_search_journal_entries` filtered to the vendor's accrual account across multiple periods, `sap_subledger_get_ap_invoice_by_id`, `records_vault_search_documents` (SOW, vendor contract).

**Write:** `email_send_email` (history summary back to AP specialist), `conversations_add_message` in `#vendor-bills-and-ap`.

**Linked scenarios:** scen_031 (Ben Arinzo on GraniteRack accrual history), scen_034 (Ben Arinzo on CrownPeak Incident-Response engagement scope letter), scen_030, 032, 035 (Mateo Kovac NPC on vendor-master details).

**Example.**

> Owen Mercer flagged the GraniteRack Compute Services invoice `VEN-012-753165` (SAP record `apinv_6131b7c637aa4b6e`, $39,090.56 on account 219000) on this week's AP exceptions sweep — it's `pending_approval` past the 60-day SLA, and the SOW in Records Vault looks superseded (`SOW-2025-GR-rev1` dated 2025-10-15 replaced the earlier `SOW-2024-GR-rev3` this invoice was billed under). Before Daniel Jones routes the invoice for partner disposition, he needs the accrual history from the bookkeeping side. Pull every Oracle GL accrual entry against GraniteRack across the `acme_cloud_FP-2025-*` and `acme_cloud_FP-2026-*` periods, confirm whether each accrual was reversed cleanly in the following period, and reply to Owen with a one-screen summary so he can compare the cumulative accrued balance against the disputed invoice amount. Note any month where the reversal is missing.
>
> *Prompt written by Ben Arinzo, Bookkeeper.*

---

# Category 3 — Tax

## What it is

Tax compliance covers everything the firm must file with the IRS or state revenue authorities, plus the planning conversations that happen before filing. The tax team is small but high-stakes: every IRS filing window is non-negotiable, and a missed nexus threshold or mis-coded book-tax difference can cost a client real money in penalties.

There are four shapes of tax work:

1. **Quarterly multi-state sales tax** — for clients with sales nexus in multiple US states. Acme Cloud accrues in the four states that genuinely tax SaaS — **TX, NY, WA, AZ** — per the SaaS-taxability determination memo in Records Vault; Brookfield has its own filings.
2. **Quarterly estimated income tax payments** — federal and state quarterly estimates for entities that owe income tax. Acme Cloud is the entity with regular estimates in this universe (scen_046).
3. **Annual federal returns** — partnership Form 1065 for Northstar Legal (scen_068), corporate returns for Acme.
4. **Year-end tax-planning workshops** — partner-led sessions with the client to plan partnership distributions, depreciation elections, etc.

The fifth, smaller shape is **IRS challenged-treatment liaison**: when the IRS questions a position the firm has taken, Alex Cahoon liaises with Priya Singh (Corporation Tax Officer NPC) to argue or concede.

## Governing standards

- **Internal Revenue Code (IRC)** — the US federal tax code. Drives sales-tax nexus rules, ASC 740 book-tax differences, §179 / bonus depreciation elections, M-1 reconciliations (book-to-tax), K-1 allocations.
- **IRS filing deadlines** — quarterly sales tax windows and the annual return calendar are hard constraints.
- **Closed-period late-post authorization** — return-to-provision true-ups often need to post into a closed prior-period; the `late_post_authorization_id` requirement applies.

## Authoring checklist

> **🎓 CPA-heavy category.** Tax work runs on a dense stack of US tax concepts that all show up in Category 3 tasks: **sales-tax nexus** (the legal threshold — usually a dollar or transaction count per state — that obligates a business to collect and remit sales tax in that state), **ASC 740** (the GAAP standard for income-tax accounting — tracks the timing differences between book income and taxable income), **§179 / bonus depreciation** (IRS elections that let a business expense capital assets immediately rather than depreciating them over years), **M-1 reconciliation** (the schedule on Form 1065 / 1120 that reconciles book income to taxable income), **K-1 allocations** (Schedule K-1 — the form that reports each partner's share of partnership income, deductions, and credits), and **Form 1065** (the US Return of Partnership Income — what Northstar Legal files annually). The narrative below explains each as it first appears, and most subcategories anchor on one or two of these.

| Field | Value |
|---|---|
| **Eligible acting personas** | **Tom Chang** (Tax Associate) and **William White** (Corporate Tax Associate) — prepare returns, accrual JEs, projection memos; **Hannah Grant** (Corporate Tax Senior — owns the working file); **Alex Cahoon** (Corporate Tax Manager — reviews + handles IRS liaison); **Ming Chang** (Tax Partner — signs off, runs planning workshops). |
| **Other entities touched** | All three for sales tax and own-firm returns: `acme_cloud` (Texas sales tax, corporate annual return, quarterly estimates), `northstar_legal` (partnership Form 1065, year-end planning), `brookfield` (firm's own filings). |
| **External / NPC participants** | **Priya Singh** (Corporation Tax Officer NPC — IRS-side counterpart for challenged-treatment liaison in Cat 3.5); **Sofia Halabi** (Tax Specialist NPC — reviewer on scen_045 and scen_046); client-side CFOs and controllers as counterparties in planning workshops. |
| **Primary systems** | **Oracle GL** (`230000` Income Tax Payable, sales-tax accrual accounts — confirm per entity; ASC 740 book-tax true-up JEs; `late_post_authorization_id` for closed-period return-to-provision); **Records Vault** (tax packages under `IRS_TAX_7Y`, nexus memos, prior-year returns, projection memos); **Airtable** (Weekly Tax and Review Cadence table); **Email** (partner approval routing, IRS portal confirmations, Priya Singh liaison); **Slack `#tax-prep-and-filings`**. |
| **Primary artifacts** | Sales-tax accrual JEs (entity-specific accrual + expense accounts); annual federal-return packages (Form 1065 for Northstar, corporate for Acme); quarterly estimated-payment accruals; year-end planning recommendation memos (one-page); IRS-challenge rebuttal memos (`restricted`); nexus memos per jurisdiction. |
| **Linked study scenarios** | scen_045 (Brookfield April multi-state sales tax); scen_067 (Acme Q1 sales tax — TX/NY/WA/AZ, anchored on the SaaS-taxability determination memo); scen_046 (Acme Q1 estimated tax projection); scen_047 (Northstar year-end planning workshop); scen_068 (Northstar FY2025 partnership return, Form 1065). |

## ⚠️ Known CoA gap — sales tax

**There is no dedicated Sales Tax *Payable* account in the chart of accounts.** The expense side does exist — `525000` Sales Tax Expense is a real account on Acme, and the canonical sales-tax scenario (scen_067) debits it. The gap is on the liability side: that scenario books the payable to `225000`, which is otherwise labelled *Accrued Salaries & Bonuses*. **Before authoring any Category 3 sales-tax task, confirm the correct accrual (liability) + expense accounts against the entity's CoA** — don't assume a purpose-built "Sales Tax Payable" line exists. Treat this as the largest known correctness pitfall in this category.

## Subcategories

### 3.1 Quarterly Sales Tax

Per-state sales-tax accrual, nexus review, partner approval, filing confirmation.

**⚠️ SaaS sales-tax is jurisdiction-specific — anchor on Acme's four taxable states.** SaaS taxability differs sharply by state. For Acme Cloud, the SaaS-taxability determination memo in Records Vault (`tax_determination_memo`, FY2026, uploaded by Hannah Grant, retention `IRS_TAX_7Y`) concludes that **four states genuinely tax Acme's SaaS product: TX, NY, WA, AZ**. TX uses destination-based per-ZIP local rates (Acme crossed the $612K trailing-12 economic-nexus threshold). The other states with prior nexus footprints — CA, FL, IL, MA, NV, GA, NC — are SaaS-exempt or services-not-taxed; any references to those in older scenario data are either historical accruals (the CA-only standing monthly entries are the most material) or zero-balance protective filings tied to nexus cleanup. The Q1 2026 Acme sales-tax accrual is posted to `acme_cloud_FP-2026-03` as a **single combined entry of $42,180.55** (`JE-acme_cloud-acme_cloud_FP-2026-03-0076`, `525000` Sales Tax Expense Dr / `225000` Cr) — the GL does **not** carry a per-state JE breakdown, so verify against that one combined accrual rather than four separate state lines. When authoring 3.1 tasks: anchor on the determination memo, drive the agent toward the four taxable states, and route any nexus-shift question to Ming Chang rather than asking the agent to invent a determination.

When authoring 3.1 tasks: anchor on the existing TX nexus memo in Records Vault, ask the agent to flag any state where the prior taxability conclusion looks stale or under-supported, and route uncertain multi-state calls to Ming Chang rather than asking the agent to invent a determination. Don't assume the agent can derive multi-state SaaS taxability from first principles — that's a partner-judgment call.

**Brookfield's own sales-tax cycle** is separate and simpler — professional accounting services are generally not subject to sales tax in the states where Brookfield itself operates, so Brookfield-as-entity sales-tax tasks are minimal. Northstar (legal services) is similar.

**⚠️ Sales-tax CoA gap.** There is no dedicated `Sales Tax Payable` account in any entity's CoA. The expense account `525000` Sales Tax Expense *does* exist on Acme and is the correct debit; the payable side, in scen_067, lands on `225000` (otherwise Accrued Salaries & Bonuses). Before authoring a 3.1 prompt, confirm the correct accrual + expense account combination against the entity's CoA — and consider asking the agent to surface the gap rather than assume a purpose-built payable account.

**Read:** `oracle_gl_search_journal_entries` filtered to the sales-tax accrual account, `records_vault_search_documents` (nexus memo, prior return), `airtable_list_records` (tax-cycle workflow), `conversations_history` on `#tax-prep-and-filings`.

**Write:** `oracle_gl_create_journal_entry` (sales-tax accrual JE), `records_vault_upload_document` (jurisdiction breakdown — retention `IRS_TAX_7Y`), `email_send_email` (partner approval, IRS portal confirmation), `reminder_create_reminder` (next-quarter cycle), `conversations_add_message`.

**Linked scenarios:** scen_045 (Brookfield April multi-state), scen_067 (Acme Q1 TX/NY/WA/AZ — anchored on the SaaS-taxability determination memo; TX per-ZIP nexus correction is the central beat).

**Example.**

> Acme Cloud's Q1 2026 multi-state sales-tax filing is up for review. The four states where Acme's SaaS product is taxable are TX, NY, WA, AZ per the SaaS-taxability determination memo in Records Vault; the Q1 accrual is booked to `acme_cloud_FP-2026-03` as a single combined entry of $42,180.55, with TX the largest jurisdiction on per-ZIP local rates (Acme crossed the $612K trailing-12 TX economic-nexus threshold this cycle). Tom Chang opened the cycle kickoff in `#tax-prep-and-filings` in early April and reran TX from a $0 placeholder to the per-ZIP figure after Hannah Grant's nexus correction. Verify the Q1 combined sales-tax accrual JE (`JE-acme_cloud-acme_cloud_FP-2026-03-0076`, $42,180.55 — `525000` Sales Tax Expense Dr / `225000` Cr) was posted to `acme_cloud_FP-2026-03` against the correct accrual account with the right line shape, confirm the nexus positions in the determination memo are still current, then draft the partner-approval email to Ming Chang. CA-only standing entries from prior quarters (≈$29K) are a separate cleanup item — flag them but don't fold them into Q1. Set the Q2 reminder.
>
> *Prompt written by Hannah Grant, Corporate Tax Senior.*

### 3.2 Annual Corporate / Partnership Returns

Federal returns. Northstar Legal files **Form 1065** (US Return of Partnership Income); Acme files corporate. Book-tax differences (ASC 740) must be identified, capital allowances claimed (§179, bonus), partner allocations distributed via K-1, and the federal return tied back to the closed year-end trial balance.

**Linked scenarios:** scen_068 (Northstar FY2025 federal partnership return, Form 1065).

**Example.**

> Route Northstar Legal's FY2025 partnership return (Form 1065) for partner sign-off. The draft and the Step-1 data package are filed in Records Vault. Identify the book-tax differences (recurring ASC 842 operating-lease add-back; §179/bonus depreciation on FY2025 IT equipment; a SALT accrual shortfall), confirm the federal return ties to the closed `northstar_legal_FP-2025-12` trial balance, and email William White for partner authorization of the closed-period SALT true-up (credit `230000` Income Tax Payable; debit the appropriate tax-expense account per the entity CoA — closed-period posting will need `late_post_authorization_id`). His reply is the authorization of record.
>
> *Prompt written by Hannah Grant, Corporate Tax Senior.*

### 3.3 Quarterly Estimated Tax Payments

Projection memo → ledger tie-out → accrual JE for the Q1/Q2/Q3/Q4 estimate → partner approval → next-quarter reminder.

**Read:** `oracle_gl_search_journal_entries` (YTD activity), `records_vault_search_documents` (prior projection model, methodology memo), `airtable_get_record` (tax-cycle workflow).

**Write:** `oracle_gl_create_journal_entry` (estimated-payment accrual), `records_vault_upload_document` (projection memo, retention `IRS_TAX_7Y`), `email_send_email` (partner approval), `reminder_create_reminder` (next quarter).

**Linked scenarios:** scen_046 (Acme Q1 estimated tax projection).

**Example.**

> Acme Cloud's Q1 2026 estimated tax projection needs to go to Ming Chang by EOD Wednesday. Pull the YTD activity off the Acme ledger (`acme_cloud_FP-2026-01` through `acme_cloud_FP-2026-03`) and rebuild the projection methodology memo against the FY2025 model in Records Vault. Check the YTD JE set for any duplicate entries and post a reversing JE if needed (`is_standard_entry: false`, full lifecycle with 5-minute minimums) so the tie-out lands cleanly. Refresh the projection, upload the methodology memo to Records Vault under `IRS_TAX_7Y`, and email Ming for partner approval. Set the Q2 reminder.
>
> *Prompt written by Hannah Grant, Corporate Tax Senior.*

### 3.4 Tax Planning Workshops

Annual partner-led planning conversations with the client. Northstar's year-end partnership-distribution planning workshop is the universe example (scen_047): a calendar-driven workshop, prep communications, and a recommendation handoff before the workshop.

**Read:** `records_vault_search_documents` (prior-year distribution model, partner-allocation data), `oracle_gl_search_journal_entries` (FY YTD activity), `calendar_list_events` (workshop slot).

**Write:** `records_vault_upload_document` (one-page recommendation memo, retention `IRS_TAX_7Y`), `email_send_email` (partner pre-read), `reminder_create_reminder`.

**Linked scenarios:** scen_047 (Northstar year-end partnership-distribution planning).

**Example.**

> Northstar Legal's year-end partnership-distribution tax planning workshop is on the calendar for next month. Prep the recommendation handoff that will frame the workshop: pull last year's distribution model from Records Vault, review the FY2025 partner-allocation data, identify the three biggest tax-position decisions partners need to weigh in on (estimated SALT impact, §179 vs. bonus election on FY2025 IT equipment, K-1 allocation timing), and draft a one-page recommendation memo. File it to Records Vault under `IRS_TAX_7Y` and email William White and Matthew Li ahead of the workshop. Make sure Tom Chang has pulled the supporting JE references before the partner pre-read.
>
> *Prompt written by Hannah Grant, Corporate Tax Senior.*

### 3.5 IRS Liaison & Challenged Treatments

When the IRS challenges a position the firm has filed, Alex Cahoon (Corporate Tax Manager) liaises with Priya Singh (Corporation Tax Officer NPC) to argue, document, or concede the position. No scripted scenario today; the example below is constructed from the firm's existing tax-team structure and the Priya Singh / Alex Cahoon counterpart relationship documented in the persona briefs.

**Read:** `records_vault_search_documents` (prior return + election support), `oracle_gl_search_journal_entries` (the contested period), `sap_subledger_list_fixed_assets` (for depreciation-election challenges), `email_search_emails` (IRS correspondence thread).

**Write:** `records_vault_upload_document` (rebuttal memo, retention `IRS_TAX_7Y`, classification `restricted`), `email_send_email` (response to Priya Singh; partner routing if conceding).

**Example.**

> An IRS Examiner notice arrived overnight challenging the deductibility on the FY2024 Northstar partnership return — specifically the §179 election on FY2024 IT equipment. Priya Singh is the contact. Pull the FY2024 partnership return from Records Vault, find the §179 election support in the FY2024 fixed-asset roll-forward in SAP, confirm the position the firm took, and draft the response email to Priya. If the position is defensible, write the technical rebuttal citing the relevant IRC §179 provisions and the FY2024 election documentation; if the position is weak, route to Ming Chang for partner judgment on whether to concede. File the response draft under `IRS_TAX_7Y` with classification `restricted`.
>
> *Prompt written by Alex Cahoon, Corporate Tax Manager.*

---

# Category 4 — Compliance & Internal Controls

## What it is

This category covers the full set of compliance and internal-controls work the firm runs. AML is the most visible slice, but the bucket is broader — preparer/certifier independence tests, document-retention sweeps, state filings, and the GAAP-improper-request refusal pattern all live here. The common thread is **periodic or continuous controls testing**: someone is checking that the firm is following its own (or regulators') rules.

The exposure surface:

- **Anti-Money Laundering (AML)** under the US Bank Secrecy Act and FinCEN rules (Customer Due Diligence, Beneficial Ownership Information).
- **AICPA Statement on Quality Management Standards (SQMS 1)** for professional quality control — the umbrella the internal-controls program runs under.
- **Document retention** per AICPA and IRS rules.
- **Client confidentiality and data security** under AICPA Code of Professional Conduct §1.700 and applicable US state data-protection laws.
- **Preparer/certifier independence** controls — the prepare-and-certify same-person check.

The compliance team — Marina Soko (Compliance Officer), Peter Sanchez (Head of Compliance), and Farah Dlamini (AML Analyst NPC) — runs continuous and periodic controls across all three entities.

## Why it matters

AML failures carry **criminal exposure**, not just civil penalties. AICPA quality-management failures can cost the firm fines up to $10K per member and possible loss of practice rights. Privacy failures can carry GDPR-style penalties up to 4% of worldwide turnover. Every Category 4 sub-task is high-stakes by design.

## Authoring checklist

> **🎓 CPA-heavy category.** The concepts live in regulatory compliance and US GAAP, not in deep adjusting-entry mechanics: **BSA / FinCEN** (the US Bank Secrecy Act and the Financial Crimes Enforcement Network — the federal anti-money-laundering framework), **CDD** (Customer Due Diligence — the documented review of a counterparty and source of funds that the BSA requires for transactions over the wire-transfer threshold), **BOI** (Beneficial Ownership Information — who actually owns or controls a client entity with > 25% interest), **SQMS 1** (the AICPA Statement on Quality Management Standards — the umbrella under which the firm's internal-controls program operates), **preparer/certifier independence** (the rule that the person who prepares a reconciliation or workpaper cannot also be the person who certifies it), and **improper-request refusal** (the firm's professional duty to refuse client requests that would misstate the books under GAAP — e.g., booking a current-period expense as a prepaid asset to defer it). The narrative below defines each on first use; most subcategories anchor on one or two of these.

| Field | Value |
|---|---|
| **Eligible acting personas** | **Marina Soko** (Compliance Officer — primary on AML wire-flag, soft-flag triage, retention sweep); **Peter Sanchez** (Head of Compliance — quarterly control-test sign-off, retention-sweep escalations); **Daniel Jones** (Accounts Manager — authors the improper-request refusal in 4.7); **Andrea Phil** (Partner — cross-functional sign-off on improper-request escalations). |
| **Other entities touched** | All three: AML wire-flag review primarily on `acme_cloud` (scen_041); BO refresh on `acme_cloud` (scen_061); soft-flag triage on `northstar_legal` (scen_062, IOLTA-trust context); independence test and retention sweep run firm-internal; state filings on all three. |
| **External / NPC participants** | **Farah Dlamini** (AML Analyst NPC — runs the counterparty + BO + source-of-funds analysis that feeds 4.1, 4.2, 4.3); **Anita Knowles** (AML Supervisory Officer NPC — supervisory sign-off on wire-flag dispositions); **Julia Vance** (Audit Partner — cross-reviewer on quarterly control tests); client-side CFOs/BOs as counterparties in BO refresh and improper-request workflows. |
| **Primary systems** | **Records Vault** (AML monitoring files, disposition memos, BO files, control-test memos — all `restricted`; retention-sweep metadata pull); **Oracle GL** (wire-flag JE anchors — e.g., `JE-acme_cloud-FP-2026-04-0052`; cash-account context for soft-flag triage); **BlackLine** (recon sample for the preparer/certifier independence test, anchored on `BL-A81316258BCB` in scen_042); **Messaging** (DM-led soft-flag signal-checks — kept off Slack channels to avoid widening the audience prematurely); **Email + Slack `#compliance-and-registrations`**; **Linear** (`team_comp` — improper-request pressure-event tracker). |
| **Primary artifacts** | AML monitoring file + disposition memo (`AICPA_SQMS_7Y`, `restricted`); annual BO refresh file + AML risk-rating memo (`restricted`); quarterly preparer/certifier independence memo (`AICPA_SQMS_7Y`, `restricted`); quarterly retention-sweep summary; state annual-report filings; improper-request refusal email + Linear issue. |
| **Linked study scenarios** | scen_041 (Acme wire-flag, JE-level threshold review); scen_042 (quarterly preparer/certifier independence control test); scen_044 (quarterly document-retention sweep); scen_048 (state annual-report catch-up); scen_061 (Acme FY2026 BO refresh); scen_062 (Northstar AML soft-flag triage). |

## Subcategories

### 4.1 AML Wire-Flag Review (JE-level monitoring)

Brookfield runs a **standing monitoring rule that flags any journal entry crossing the $10,000 wire-transfer threshold** for mandatory Customer Due Diligence (CDD) review — the FinCEN reporting threshold. Hitting this rule does not mean the transaction is suspicious; it means the firm is required to document a counterparty + beneficial-owner + source-of-funds review *because* it crossed the threshold. The review is the control, not the accusation.

When a posted JE trips the wire-flag, Marina Soko pulls Farah Dlamini's counterparty + beneficial-owner + source-of-funds analysis, drafts an AML monitoring file in Records Vault under `restricted` classification, routes to Anita Knowles (AML Supervisory Officer NPC) for supervisory sign-off, then up to Matthew Li / Steven Perry for partner-level clearance. The disposition memo records that the threshold-triggered review was completed and the funds source is documented — not that anything was wrong.

**Linked scenarios:** scen_041 (Acme wire-flag review on `JE-acme_cloud-FP-2026-04-0052` — a routine $57K customer payment that tripped the threshold rule).

**Example.**

> JE `JE-acme_cloud-FP-2026-04-0052` (DR Cash $57,077.69 / CR AR — a settlement payment from Acme's largest enterprise SaaS customer, posted 2026-04-22) tripped the standing $10K wire-transfer monitoring rule. The trigger is the threshold, not the JE itself — but the CDD review is mandatory. Farah Dlamini already ran the counterparty + BO + source-of-funds review on that customer — pull her notes from Records Vault, cross-reference against the JE in Oracle GL to confirm the wire details match the documented source of funds, draft the AML monitoring file (`restricted`), route to Anita Knowles for supervisory sign-off, and file the final disposition memo under `AICPA_SQMS_7Y` (`restricted`). Email Matthew Li and Steven Perry for partner-level clearance once supervisory sign-off lands. The expected disposition is "threshold review complete, source documented" — flag for escalation only if Farah's BO file shows something inconsistent.
>
> *Prompt written by Marina Soko, Compliance Officer.*

### 4.2 AML Soft-Flag Triage (BO adverse-media match)

When the daily adverse-media screener kicks up a partial-name match on a beneficial owner with > 25 % LLP interest, the workflow is DM-led (not Slack-channel-led, to avoid widening the audience prematurely): Marina DMs Ben Arinzo for cash-account transaction context, gets George McAdam's signal-vs-noise second opinion, then frames the disposition question to Daniel Jones. If the disposition lands as "soft watch" (not full escalation), the written recap is filed under `AICPA_SQMS_7Y` with classification `restricted` and Daniel countersigns by email.

**Read:** `messaging_list_conversations` (DM threads), `oracle_gl_search_journal_entries` filtered to cash accounts, `records_vault_search_documents` (prior BO file, AML register).

**Write:** `messaging_send_message` (signal-check DMs), `records_vault_upload_document` (disposition memo, `restricted`), `email_send_email` (countersignature to manager), `reminder_create_reminder` (30-day follow-up).

**Linked scenarios:** scen_062 (Northstar Legal AML soft-flag triage on adverse-media partial-name match).

**Example.**

> The daily adverse-media screener kicked up a partial-name hit on a Northstar Legal beneficial owner with > 25% LLP interest. It looks ambiguous and may just be a name collision. Open a DM to Ben Arinzo asking for cash activity on accounts `101000` and `105000` for `northstar_legal_FP-2026-03` and `northstar_legal_FP-2026-04`, get George McAdam's signal-vs-noise second opinion, then frame the disposition question to Daniel Jones. If the disposition lands as "soft watch", draft the written recap, file it to Records Vault under `AICPA_SQMS_7Y` with classification `restricted`, and send the countersignature email to Daniel. Drop a 30-day follow-up reminder.
>
> *Prompt written by Marina Soko, Compliance Officer.*

### 4.3 Annual Beneficial Owner Refresh

Every year, high-volume clients get a full beneficial-owner refresh. Daniel Jones drives the FY refresh and AML risk re-assessment for Acme; Matthew Li reviews as engagement partner; Ryan Delgado approves the final risk rating.

**Read:** `records_vault_search_documents` (prior-year BO file, risk-rating memo), `oracle_gl_search_journal_entries` (recent client activity for source-of-funds confirmation).

**Write:** `records_vault_upload_document` (refreshed BO file + AML risk-rating proposal, classification `restricted`), `email_send_email` (partner review + risk-rating approval routing).

**Linked scenarios:** scen_061 (Acme Cloud FY2026 annual BO refresh).

**Example.**

> Acme Cloud's FY2026 annual beneficial-owner refresh kicks off this week. Pull the FY2025 BO file from Records Vault and the prior risk-rating memo, then build the FY2026 refresh checklist: confirm each named BO is still > 25% LLP interest, request updated identification documents from each, and verify the source-of-funds narrative against the FY2026 Q1 activity in Oracle GL. Draft the refreshed BO file and AML risk-rating proposal in Records Vault under classification `restricted`, email Matthew Li (engagement partner) for review, and route the final risk rating to Ryan Delgado for approval.
>
> *Prompt written by Daniel Jones, Accounts Manager.*

### 4.4 Quarterly Partner Sign-Off Control Test

Tests **preparer/certifier independence**: the same person cannot prepare and certify a reconciliation. Marina pulls a 5-recon sample anchored on a single BlackLine reconciliation (`BL-A81316258BCB` in scen_042), Farah compares preparer-vs-certifier names, Peter Sanchez signs the control-test memo, Julia Vance provides audit-partner review, Steven Perry gives final clearance.

**Read:** `blackline_list_reconciliations` (the 5-recon sample), `records_vault_search_documents` (prior quarter's control-test memo).

**Write:** `records_vault_upload_document` (independence memo, `restricted`), `email_send_email` (Peter → Julia → Steven sign-off chain).

**Linked scenarios:** scen_042.

**Example.**

> The quarterly partner sign-off control test is due before BD8. The anchor reconciliation is `BL-A81316258BCB`; sample the four neighboring recons to make five total. For each, pull the preparer name and the certifier name from BlackLine, confirm they're different people (preparer/certifier independence is the test), and document any case where they're the same — that's a control failure. Draft the independence memo, route to Peter Sanchez (Head of Compliance) for sign-off, copy Julia Vance for audit-partner review, and email Steven Perry for managing-partner clearance. File the final memo to Records Vault under `AICPA_SQMS_7Y` with classification `restricted`.
>
> *Prompt written by Marina Soko, Compliance Officer.*

### 4.5 Quarterly Document Retention Control Sweep

Firm-internal metadata-only review of Records Vault documents. Marina runs the retention sweep; Farah pulls metadata; Anita Knowles advises on edge-case retention rules; Peter Sanchez signs; Steven Perry clears.

**Read:** `records_vault_list_documents` filtered to recent additions, metadata only (no content reads required).

**Write:** `records_vault_upload_document` (control-test summary, `AICPA_SQMS_7Y` `restricted`), `email_send_email`, `messaging_send_message` (DM Anita Knowles on edge cases).

**Linked scenarios:** scen_044.

**Example.**

> The quarterly document retention control sweep is due before BD8. Pull a metadata sample of Records Vault documents added or modified in Q1 2026 — focus on tax workpapers and AML monitoring files. For each, confirm the `retention_policy_code` is one of the four valid codes (`AICPA_SQMS_7Y`, `IRS_TAX_7Y`, `FIRM_INTERNAL`, `INDEFINITE`) and that the classification is appropriate to content (AML files must be `restricted`). Where Anita Knowles needs to advise on an edge case, route to her on messaging. Write the control-test summary to Records Vault under `AICPA_SQMS_7Y`, route to Peter Sanchez for compliance leadership sign-off, then to Steven Perry for managing-partner clearance.
>
> *Prompt written by Marina Soko, Compliance Officer.*

### 4.6 State / Annual Report Compliance

Multi-state annual-report catch-up + late-penalty bills + go-forward controls memo. The universe example is Brookfield's own NY/NJ/DE catch-up — Linda Burns (Commercial Law Consultant NPC) leads, Anaya Patel (Workflow Administrator NPC) runs portal submissions, Priya Singh validates tax nexus, Peter Sanchez provides compliance partner sign-off.

**Read:** `airtable_list_records` ("Annual Report Filing Control" base), `sap_subledger_list_ap_invoices` (late-penalty bills), `records_vault_search_documents` (prior filings).

**Write:** `records_vault_upload_document` (go-forward controls memo, `AICPA_SQMS_7Y`), `email_send_email`, `airtable_update_record`.

**Linked scenarios:** scen_048.

**Example.**

> Brookfield's state annual report catch-up across NY, NJ, and DE is in flight. Anaya Patel is coordinating portal submissions; Priya Singh is validating nexus per state; Linda Burns is leading the legal-side work. Pull the workflow status from the Airtable "Annual Report Filing Control" table, verify each state's late-penalty AP invoice in SAP Subledger reconciles to a corresponding payment confirmation in Records Vault, and surface any state with a partial confirmation or missing fee bill before sign-off lands. Draft the go-forward controls memo (one page: what went wrong, the new calendar, the early-warning trigger), upload to Records Vault under `AICPA_SQMS_7Y`, and email me for sign-off.
>
> *Prompt written by Peter Sanchez, Head of Compliance.*

### 4.7 Improper-Request Refusal *(design surface, no scripted scenario)*

The v5 survey explicitly requires staff to **reject GAAP-improper client requests**. The realistic shape is a client asking the firm to mis-classify a current-period expense so it doesn't hit Q2 results — for example, asking for a *finished* marketing campaign to be coded into the `135000` Prepaid Marketing account and amortized over future months, when the campaign already delivered its benefit in-period. Note the nuance: `135000` is a legitimate account for genuine prepaid marketing (a campaign that runs in future months but was paid for in advance). The improper part is using it as a deferral mechanism for spend that has already burned through its benefit period. The firm must (a) refuse the treatment in clear terms, citing the matching principle and the relevant US GAAP framing, (b) reference the firm's Code of Conduct / improper-request policy, and (c) preserve the exchange under the client's engagement folder as `restricted`. A Linear issue is opened to track the pressure event so partners can see the pattern across clients. No scripted scenario today — design from the Authoring Guide framing.

**Example.**

> A client CFO emailed asking us to move a $42K marketing campaign that ran in April and finished in May into the `135000` **Prepaid Marketing** account to amortize over the next six months "so Q2 lands cleaner." The benefit period has already ended — this is a current-period expense, not a prepaid. The `135000` account is legitimate for genuine pre-paid marketing (a campaign scheduled to run in future periods), but using it to defer spend that has already delivered its benefit is improper. Read the CFO's email and the engagement letter, then draft a firm-but-respectful reply that refuses the treatment: explain that the matching principle requires the cost to be recognized in the period the marketing campaign delivered its benefit (April–May), and that booking a finished campaign as a prepaid would misstate Q2 expenses. Cite the firm's Code of Conduct and improper-request policy. Do **not** propose any workaround — the answer is a clean refusal. Cc Andrea Phil and Marina Soko. File the exchange under the client's engagement folder as `restricted`. Open a Linear issue on `team_comp` so the pressure event is tracked.
>
> *Prompt written by Daniel Jones, Accounts Manager.*

---

# Category 5 — Audit

## What it is

Brookfield's audit team supports the external audit of certain clients. Brookfield is not the external auditor — for Northstar Legal that role is held by E&P (and the firm's counterparty there is James Randall, an NPC). Brookfield's job is to **prepare the client to be auditable**: produce clean working papers, package supporting evidence, manage the Prepared-By-Client (PBC) list, and route partner sign-off on every audit deliverable.

Ryan Delgado runs audit day-to-day; Julia Vance is the audit partner.

**Audit team — full four-person stack.** As of v47 the audit-support practice has four named personas: **Mia Hartwell** (Audit Staff — tick-and-tie, detail testing on Northstar and Acme fieldwork), **Ryan Delgado** (Audit Senior — owns the day-to-day engagement plan, PBC chasing, and stale-SLA dismissals across Cat 7), **Devon Beale** (Audit Manager — engagement planning, in-charge review, partner-level memo prep; the bridge between staff fieldwork and partner sign-off), and **Julia Vance** (Audit Partner — final sign-off, US GAAP review). Devon and Mia are new v47 additions and don't yet appear in scripted scenarios; pair them with the existing Cat 5 anchors when you author new tasks. The cross-functional support seats (Daniel Jones as client-side audit lead for Northstar, Andrea Phil + Matthew Li as engagement partners, Hannah Grant on tax-touching audit questions) still apply.

## Why it matters

A failed audit means restated financials, lost client trust, and potential regulator exposure. The reviewer in this category must verify **every JE cited in a workpaper actually exists**, depreciation ties back to SAP, trust roll-forwards reconcile (Northstar IOLTA), and disclosures match prior-year format with appropriate updates.

## Governing standards

- **US GAAP disclosures** — the format and content rules for financial statements. Note: Brookfield's clients are private companies, so the relevant frame is internal working-paper completeness against prior-year comparators, not public-disclosure mechanics.
- **AICPA audit-support methodology** — workpaper structure, evidence requirements.
- **Records Vault discipline** — workpapers go under `AICPA_SQMS_7Y`; engagement letters under `FIRM_INTERNAL` (5-year); audit folder access is `restricted` to the assigned client team.
- **IOLTA trust roll-forward** — Northstar's `105000` Cash – Client Trust account must reconcile to client-level subledger detail.

## Authoring checklist

> **🎓 CPA-heavy category.** Audit support is about producing **defensible working papers** — files an external auditor will pull, sample, and challenge — and the core concepts that show up in Cat 5 tasks are: the **PBC list** (Prepared By Client — the running list of items the external audit firm asks the engagement team to produce, like trial balances, signed contracts, depreciation schedules), the **workpaper review chain** (staff → senior → manager → partner — every cited JE must tie to Oracle GL, every depreciation line must spot-check against SAP), **IOLTA trust roll-forward** (for Northstar's lawyer-trust account on `105000` — beginning balance + receipts − disbursements = ending balance, reconciled to client-level subledger detail), **engagement folder access controls** (audit-folder access is `restricted` to the assigned team, opened at engagement kickoff), and **client-consent letters** for cross-team work — when the audit team needs information from the firm's tax or accounting-services teams on the same client engagement, AICPA standards require a written client-consent letter on file in Records Vault (`kind: client_consent_letter`, classification `restricted`); v47 added the four FY2026 letters for Acme and Northstar (Audit↔Tax + Audit↔Accounting on each entity). The narrative below explains each.

| Field | Value |
|---|---|
| **Eligible acting personas** | **Mia Hartwell** (Audit Staff — tick-and-tie + detail testing on Northstar and Acme fieldwork; *new in v47, not yet anchored in scripted scenarios*); **Ryan Delgado** (Audit Senior — primary; runs PBC tracking, fieldwork support, and day-to-day kickoff coordination); **Devon Beale** (Audit Manager — engagement planning, in-charge review, partner-level memo prep; *new in v47, not yet anchored*); **Julia Vance** (Audit Partner — workpaper review and partner sign-off); **Daniel Jones** (Accounts Manager — client-side audit lead, especially on Northstar); **Andrea Phil**, **Matthew Li** (Partners — annual-accounts sign-off cross from Cat 1.2); seniors **George McAdam**, **Edith Banda**, **Jones Harrison** (working-file preparers on the annual-accounts side). |
| **Other entities touched** | Primarily `northstar_legal` (the FY2026 audit anchor + IOLTA work); `acme_cloud` (audit-readiness reviews); `brookfield` (internal-firm audit prep). |
| **External / NPC participants** | **James Randall** (Audit Senior at E&P — external audit firm counterpart on Northstar, the named approver on multiple orphan-exception scenarios); **Margaret Sullivan** (client-side reviewer on Q1 partner packages); various client controllers as PBC counterparties. |
| **Primary systems** | **Records Vault** (audit folder with `restricted` access scoped to the engagement team; workpapers under `AICPA_SQMS_7Y`; engagement letters under `FIRM_INTERNAL`; PBC list; planning memo; **client-consent letters** under `restricted` for cross-team work between audit and tax/accounting on Acme and Northstar engagements); **Oracle GL** (`northstar_legal_FP-2025-*` and `FY2026-*` for JE verification; IOLTA `105000` for trust roll-forward); **SAP Subledger** (fixed-asset depreciation spot-checks); **Airtable** (audit-engagement record with PBC closure %); **Calendar** (kickoff + milestone scheduling); **Reminder** (fieldwork / partner-review / sign-off milestones); **Email** (kickoff invites, PBC chase lists). |
| **Primary artifacts** | Engagement letter (`FIRM_INTERNAL`, 5-year retention); planning memo; PBC list (running queue); workpapers (`AICPA_SQMS_7Y`); reviewer cover note; audit-engagement Airtable record with `pbc_closure_pct`; IOLTA-trust roll-forward worksheet; **client-consent letters** (`kind: client_consent_letter`, `restricted` — 4 in the universe: Acme×2 and Northstar×2, each covering Audit↔Tax and Audit↔Accounting Services). |
| **Linked study scenarios** | scen_043 (Northstar FY2026 audit kickoff — the canonical 5.1 anchor); scen_058 (Northstar Q1 partner package — the working-paper review pattern that maps to 5.3); scen_063 (Northstar annual-accounts working-paper chain that bridges Cat 1.2 and Cat 5). |

## Subcategories

### 5.1 Audit Engagement Kickoff

Engagement letter signed → planning memo drafted → PBC list produced → recurring milestone reminders set → kickoff calendar event scheduled with both the client-side lead (Daniel Jones for Northstar) and the external audit firm (James Randall at E&P). The audit folder is restricted at engagement open. **One important kickoff check:** before the audit team can pull workpapers or context from Brookfield's tax or accounting-services teams on the same client engagement, AICPA standards require a written **client-consent letter** on file in Records Vault — the four FY2026 letters (Acme Audit↔Tax, Acme Audit↔Accounting, Northstar Audit↔Tax, Northstar Audit↔Accounting) live under `kind: client_consent_letter`, classification `restricted`. Verify the relevant consent letter is on file and current before the cross-team request goes out.

**Linked scenarios:** scen_043 (Northstar FY2026 audit kickoff).

**Example.**

> Northstar Legal's FY2026 audit kickoff is next Wednesday. Pull the FY2025 engagement letter and planning memo from Records Vault as templates, draft the FY2026 versions (workpapers `AICPA_SQMS_7Y`; engagement letter `FIRM_INTERNAL`), and prep the PBC list. Email the kickoff invite to Daniel Jones (client-side lead) and James Randall at E&P with the PBC list attached, create milestone reminders for fieldwork / partner review / signoff, and update the Airtable audit-engagement record. Restrict the audit folder's access grant to the assigned client team.
>
> *Prompt written by Ryan Delgado, Audit Senior.*

### 5.2 PBC Tracking & Fieldwork Support

The PBC list is the running queue of items the external auditor has requested from the client/firm. Ryan tracks status (open / pulled / delivered), chases gaps, and runs the weekly fieldwork-support call. Risk threshold: PBC closure below 80 % at a milestone date is a flag for cross-functional risk pull (Category 9.2).

**Read:** `records_vault_search_documents` (PBC list, workpapers), `airtable_get_record` (audit-engagement record), `reminder_list_reminders` (milestone reminders), `email_search_emails` (audit-firm exchanges).

**Write:** `email_send_email` (chase list to client-side lead + external audit firm), `airtable_update_record` (PBC closure percentage), `conversations_add_message` in `#audit-engagements`.

**Linked scenarios:** scen_043 (Northstar FY2026 audit kickoff sets up the PBC list that ongoing tracking maintains).

**Example.**

> Northstar Legal's FY2026 audit fieldwork is in week 2. Pull the PBC list from Records Vault under the Northstar FY2026 audit folder. For each open item, check status against the latest milestone reminder, identify which items are blocked (waiting on client docs, waiting on internal preparer), and which are stale (over 5 business days without movement). Email Daniel Jones (client-side lead) the consolidated chase list with specific actions per item, copy James Randall at E&P on the items he's blocking on, and update the Airtable audit-engagement record's PBC closure percentage. Flag any item that puts the audit kickoff-to-signoff timeline at risk.
>
> *Prompt written by Ryan Delgado, Audit Senior.*

### 5.3 Workpaper Review & Partner Sign-Off

Once workpapers are drafted, the partner (Julia Vance for audit; Andrea Phil for annual accounts) performs the partner review. Every JE cited in a workpaper is verified against Oracle GL; depreciation is spot-checked against SAP; IOLTA roll-forward is reconciled; working-paper narrative is checked against the prior-year comparator for any thin coverage that would draw a reviewer question. (Brookfield's clients are private — there is no public-company disclosure regime here. The review focuses on internal working-paper completeness, not statutory disclosures.)

**Read:** `records_vault_search_documents` (working file, prior-year comparator), `oracle_gl_search_journal_entries` (JE verification), `sap_subledger_list_fixed_assets`.

**Write:** `records_vault_upload_document` (signed workpaper), `email_send_email` (sign-off to delivery), `conversations_add_message`.

**Linked scenarios:** scen_058 (Northstar Q1 partner package — working-paper review pattern), scen_063 (Northstar annual accounts).

**Example.**

> The Northstar Q1 partner package workpapers landed in Records Vault yesterday and need partner sign-off. Daniel Jones's review memo is attached. Pull the working file, verify every JE cited against Oracle GL (`northstar_legal_FP-2026-01` through `northstar_legal_FP-2026-03`), confirm the IOLTA-trust roll-forward ties to `105000`, spot-check fixed-asset depreciation against SAP, and compare each working-paper narrative section against the FY2024 comparator. If anything doesn't tie or any working-paper note is thin against prior year, email Daniel back with the specific gaps; otherwise sign off in Records Vault and email Matthew Li to authorize delivery to the client.
>
> *Prompt written by Julia Vance, Audit Partner.*

---

# Category 6 — AP / Vendor Operations

## What it is

Accounts Payable (AP) is responsible for paying invoices owed to outside vendors. The work is process-heavy and has clear escalation paths when invoices don't move cleanly through the standard chain.

The standard AP process:

1. **Purchase Order (PO).** Procurement or a team member creates a PO, typically approved by the **owner of the cost center**.
2. **Goods/services received.** When goods arrive or services are completed, AP pays the invoice **matched against the PO**. For physical goods, AP verifies receipt with a packing slip (the three-way match: invoice ↔ PO ↔ packing slip).
3. **Approval chain.** AP routes the invoice through the appropriate approval chain by amount (see Category 6.3 below).

### Blanket POs

For long-term contracts with an indeterminate number of hours (consulting engagements, ongoing IT support), the firm issues a **blanket PO** with a single approved cap amount. Once cumulative invoices reach the cap, no more can be paid without a new PO. Because line items on blanket-PO invoices won't exactly match the PO, AP must collect supporting documentation (typically **time cards**) to validate each invoice. A **Statement of Work (SOW)** is frequently attached to a blanket PO to define the scope.

### As part of the close

During each close, the AP team runs a payables report and escalates any outstanding items (aged > 30 days, disputed amounts, missing credit memos, blocked items).

## Why it matters

AP is the largest single dollar volume of work the firm processes for outsourced clients, and a single miscoded invoice (e.g., a capex item posted as opex) can ripple into close, tax, and audit downstream.

## Authoring checklist

> **🛠 No-CPA-required category.** AP work is operational invoice-processing: receive an invoice, match it to a PO, route it through an approval chain by amount, and pay or void. The concepts that show up in Category 6 are **the three-way match** (invoice ↔ PO ↔ packing slip — verifying that what was invoiced is what was ordered and what arrived), **the approval ladder** (clerk codes everything → AP manager approves ≤ $10K → Controller ≤ $50K → Managing Partner > $50K), **blanket POs** (a single approved cap amount covering many invoices over time, typically with a Statement of Work — SOW — attached for scope), and **aged AP escalation** (any invoice still `pending_approval` past the 60-day SLA needs formal internal escalation). None of this requires CPA-grade judgment — it requires attention to detail and discipline routing through the approval chain.

**The full AP + Procurement cast (post-v47):**

- **Owen Mercer is an NPC, not a persona.** He surfaces invoices in the AP escalation queue; he does **not** author tasks. Treat him as the trigger source (the one who flagged the invoice in the queue), not the seat the task is written from.
- **Priya Khatri (AP Coordinator)** is the new v47 first-line acting seat for 6.1 — she owns invoice-intake routing, vendor-master accuracy, and the weekly AP exceptions triage; accountants escalate coding problems to her. She's the natural acting voice on most AP escalation prompts going forward.
- **Tariq Soto (AP Clerk)** handles invoice data entry, three-way-match verification, and routes exceptions up to Priya. He's a contained-step acting seat (e.g., "pull line-level invoice detail for Priya to review").
- **Lena Park (Procurement Officer)** owns the PO / SOW side — PO issuance, vendor onboarding diligence, SOW lifecycle. **Deliberately separated from AP per segregation-of-duties controls**, so she's the canonical acting voice when a Cat 6 task touches the procurement side (e.g., a SOW-supersession question of the shape that appears in scen_031, where the procurement check on which SOW version governs is a natural Lena task — though she isn't yet anchored into the scen_031 yaml as of v47). New `procurement` department.
- **Daniel Jones (Accounts Manager)** is the manager-tier acting seat — he triages systemic patterns, owns the escalation-to-partner routing, and is the natural voice for 6.2 (AP standardization on Linear). Still the canonical voice on the existing scripted 6.1 scenarios, since Priya / Tariq / Lena aren't yet anchored in those.
- **Steven Perry, Matthew Li, Andrea Phil** author the partner-disposition moment when the task is genuinely a final partner call, not just a routing step.
- **The bookkeepers** (Mateo Kovac, Ben Arinzo, Sean Williams, Nia Okafor) appear as participants pulling vendor history — they're rarely the acting seat for Category 6 (Ben/Sean more naturally anchor in Category 2 Bookkeeping).

| Field | Value |
|---|---|
| **Eligible acting personas** | **Priya Khatri** (AP Coordinator — *new in v47*, the natural canonical voice on 6.1 escalations going forward; not yet anchored in the 8 scripted scenarios); **Tariq Soto** (AP Clerk — *new in v47*, contained-step acting seat); **Lena Park** (Procurement Officer — *new in v47*, PO / SOW side); **Daniel Jones** (Accounts Manager — canonical voice on the existing scripted 6.1 scenarios + 6.2 standardization work); **Andrea Phil**, **Matthew Li**, **Steven Perry** (Partners — final disposition on > $50K and disputed invoices, by entity bucket); **Ben Arinzo**, **Sean Williams** (Bookkeepers — contained sub-steps like vendor-history pulls; rarely full escalations). |
| **Other entities touched** | All three: `acme_cloud` (heaviest AP volume; TimeLedger Nexus, GraniteRack, Pinecrest disputes); `northstar_legal` (CrownPeak Cyber Defense, IR engagement scope); `brookfield` (firm-internal LatticeHill orphan-approver gap). |
| **External / NPC participants** | **Owen Mercer** (AP Specialist NPC — surfaces every aged invoice in the queue, the trigger source on all 8 AP escalations); **Brenda Abbas** (vendor-side account manager NPC, confirms vendor-side context on 6 of 8 escalations); **Mateo Kovac** (NPC bookkeeper — vendor history pulls); **Anaya Wallace** (trainee — pulls history on 5 of 8 escalations). |
| **Primary systems** | **SAP Subledger** (AP invoices with `status`, `approver`, `pending_approval / approved / paid / voided` lifecycle; vendor-master records); **Records Vault** (vendor SOWs, IR scope letters, prior approval memos, dispute files); **Linear** (`linear_63697b7dff5c` — the AP workflow standardization project where systemic patterns get tracked as Linear issues); **Email** (partner routing); **Slack `#vendor-bills-and-ap`**; **Messaging** (private vendor-side coordination). |
| **Primary artifacts** | AP invoice records (status flips, approver assignments, voids with reason); vendor SOW + IR scope letter; partner-disposition email; approval memo (`AICPA_SQMS_7Y`); Linear issues on the AP standardization project. |
| **Linked study scenarios** | scen_029 (TimeLedger Nexus disputed Phase-3 + missing credit memo, Acme); scen_030 (LatticeHill orphan-approver routing gap, Brookfield); scen_031 (GraniteRack superseded SOW, Acme); scen_032 (TimeLedger Nexus vendor-master mismatch, Acme); scen_033 (CrownPeak Cyber Defense duplicate billing, Northstar); scen_034 (CrownPeak IR scope letter + cost classification, Northstar); scen_035 (Pinecrest license-provisioning audit, firm-internal); scen_036 (CrownPeak third stale cancellation, Northstar). |

## Subcategories

### 6.1 Aged AP Invoice Escalation

When an invoice has been `pending_approval` past the 60-day SLA, it requires formal internal escalation. Five of the eight scripted escalations sit in a **recent, realistic band**: scen_029 (TimeLedger), scen_030 (LatticeHill), scen_031 (GraniteRack), scen_033 (CrownPeak), and scen_036 (CrownPeak) all carry SAP `invoice_date`s in early March 2026 — roughly 90–100 days before the universe's 2026-06-12 "today." The in-universe Slack exception flags cite slightly tighter counts (TimeLedger **87 days**, GraniteRack **85**, CrownPeak **83**) because those messages were posted a couple of weeks before today. Treat this group as the realistic "past-the-60-day-SLA" pattern. The other three — scen_032 (a second TimeLedger item), scen_034 (CrownPeak), and scen_035 (Pinecrest) — are genuinely aged at **300+ days** (mid-2025 invoice dates) and read as deliberately stretched escalation cases. **⚠️ One data caveat on scen_030 / LatticeHill (`apinv_5e09decd035d4443`):** its SAP `invoice_date` was moved up to 2026-03-03 (~100 days), but its Slack exception message still reads "since 2025-06-30 … now 334 days old" — so that scenario shows *conflicting* aging between the SAP record and the Slack thread. Flag it rather than trusting either number blindly. When authoring new 6.1 prompts, cite day counts in the 60–100-day band for a realistic escalation, or simply frame it as "well past the 60-day SLA."

The pattern:

1. **AP specialist surfaces the aged invoice** — Owen Mercer (NPC) anchors all 8 AP escalations in the existing universe; in new task design Priya Khatri (AP Coordinator) is the natural acting voice.
2. **Clerk / trainee / bookkeeper pulls history** — historically Anaya Wallace (trainee, 5 of 8) or Mateo Kovac / Ben Arinzo (bookkeeper). Tariq Soto (AP Clerk, new v47) is the natural seat going forward for line-level invoice detail.
3. **Vendor account manager confirms vendor-side context** — Brenda Abbas (NPC, 6 of 8).
4. **Procurement confirms PO/SOW basis** — Lena Park (Procurement Officer, new v47) when the question is whether the invoice maps to a valid PO or whether the SOW was superseded. Natural acting seat for the scen_031-shaped SOW question, though Lena isn't anchored into the scen_031 yaml itself yet.
5. **AP manager triages and recommends disposition** — Daniel Jones (manager, all 8 of the scripted scenarios).
6. **Partner gives final disposition** — Steven Perry (Brookfield/Acme), Matthew Li (Northstar), Andrea Phil (de-minimis releases).

Each scenario varies in the underlying issue: disputed deliverable amount, missing credit memo, superseded SOW mismatch, vendor-master mismatch, suspected duplicate billing, IR-engagement scope letter + cost classification, license-provisioning audit, stale cancellation.

**Read:** `sap_subledger_get_ap_invoice_by_id`, `sap_subledger_list_ap_invoices` (filter `status=pending_approval`), `records_vault_search_documents` (vendor SOW, IR scope letter, prior approval memos), `linear_list_issues` (AP standardization tracker on `linear_63697b7dff5c`), `email_search_emails`, `conversations_history` on `#vendor-bills-and-ap`, `messaging_list_conversations` (private vendor-side coordination).

**Write:** `sap_subledger_update_ap_invoice` (status flip, approver assignment, void with reason), `email_send_email` (partner routing, vendor-side confirmation request), `linear_create_comment` / `linear_update_issue` (AP standardization tracker), `records_vault_upload_document` (approval memo, dispute file), `messaging_send_message`, `conversations_add_message`.

**Linked scenarios:** scen_029 (TimeLedger Nexus aged, disputed Phase-3, missing credit memo, Acme/Steven Perry), scen_030 (LatticeHill orphan-approver routing gap, Brookfield/Andrea Phil), scen_031 (GraniteRack aged, superseded SOW, Acme/Steven Perry), scen_032 (TimeLedger Nexus vendor-master mismatch, Acme/Steven Perry), scen_033 (CrownPeak Cyber Defense suspected duplicate billing, Northstar/Matthew Li), scen_034 (CrownPeak IR scope letter + cost classification, Northstar/Matthew Li), scen_035 (Pinecrest license-provisioning audit, firm-internal/Andrea Phil), scen_036 (CrownPeak third stale cancellation, Northstar/Matthew Li).

**Example.**

> Owen Mercer flagged this on this week's AP exceptions sweep: TimeLedger Nexus invoice `VEN-010-514242` on the Acme engagement (SAP record `apinv_d3019cdcc6ed44b2`, $24,475.25, account 210000) is `pending_approval` at 87 days — past the 60-day SLA. The escalation thread spans Slack, messaging, email, and Linear with a disputed Phase-3 deliverable amount and a missing credit memo; complicating it further, the AR contact on TimeLedger's side left the vendor in January and a new AR lead picked the issue up only recently. Reconstruct the thread, verify the Phase-3 dispute against the original SOW in Records Vault, confirm with Brenda Abbas (new AR lead now) whether the credit memo path is still alive, and draft the partner-disposition email to Steven Perry. If the disposition is "release with condition" or a split-payment workaround, update the SAP approver field and file the approval memo under `AICPA_SQMS_7Y`. Quick post in `#vendor-bills-and-ap` once the email goes out.
>
> *Prompt written by Daniel Jones, Accounts Manager.*

### 6.2 AP Workflow Standardization (Linear-tracked systemic issues)

The 8 AP escalations all surface recurring patterns: orphan-approver routing gaps, vendor-master mismatches, IR-scope ambiguity, CrownPeak duplicate billing. Systemic issues belong as Linear issues on the **AP workflow standardization for managed clients** project (`linear_63697b7dff5c`), not as one-off email threads. This subcategory is the meta-work of recognising a pattern across cases and writing the controls fix.

**Read:** `linear_list_issues` (existing AP-standardization tickets), `sap_subledger_list_ap_invoices` (the 8 escalation cases), `records_vault_search_documents` (prior controls memos).

**Write:** `linear_create_issue` / `linear_update_issue` (one per pattern, linked to source escalations), `records_vault_upload_document` (controls-fix memo, `AICPA_SQMS_7Y`), `email_send_email` (partner review routing).

**Linked scenarios:** Implicit across the 8 escalations (scen_029–036). No standalone scenario today.

**Example.**

> The 8 most recent AP escalations have surfaced three recurring patterns: orphan-approver routing gaps, vendor-master mismatches on TimeLedger Nexus, and CrownPeak Cyber Defense duplicate-billing risk. Open or update Linear issues on the AP workflow standardization project (`linear_63697b7dff5c`) — one issue per pattern — and link each issue to the specific escalation tickets that surfaced it. Draft a one-page controls-fix memo for the partner read: the routing-rule change, the vendor-master review cadence, and the CrownPeak invoice-verification step we should add. File the memo to Records Vault under `AICPA_SQMS_7Y` and email Andrea Phil and Steven Perry for partner review.
>
> *Prompt written by Daniel Jones, Accounts Manager.*

### 6.3 AP Threshold Approval Chain

The universe AP approval ladder, by invoice amount:

| Invoice amount | Approval chain |
|----------------|----------------|
| All amounts | AP clerk codes |
| ≤ $10,000 | AP clerk → cost-center manager (AP manager) |
| > $10,000, ≤ $50,000 | AP clerk → cost-center manager → **Controller** |
| > $50,000 | AP clerk → cost-center manager → Controller → **Managing Partner** |

The Managing Partner tier varies by entity: **Steven Perry** for Brookfield and Acme; **Matthew Li** for Northstar; **Andrea Phil** for de-minimis releases when partner-level approval is required but the amount is small.

Tasks in this subcategory verify the lower-tier approvals are documented before routing up, and ensure the right partner is targeted by entity.

**Example.**

> An Acme Cloud SAP Subledger AP invoice for $87,400 is sitting at "Controller signed" status — Owen Mercer flagged it for routing this morning. Verify the full lower-tier approval chain is documented (AP clerk coded → AP manager approved ≤ $10K → Controller signed ≤ $50K), confirm the supporting contract is in Records Vault under `AICPA_SQMS_7Y`, and check the cost-center allocation is correct. Once the chain is intact, route to Steven Perry (Acme is in his sign-off entity bucket) with a one-paragraph approval memo summarising the chain. Quick confirm in `#vendor-bills-and-ap` once the email goes out.
>
> *Prompt written by Daniel Jones, Accounts Manager.*

---

# Category 7 — BlackLine Close-Discipline & Variance

## What it is

Account reconciliations compare what the general ledger shows for an account against the supporting detail (subledger, bank statement, vendor confirmation, calculation worksheet). When the two don't match, the difference is a **variance**, and depending on size and source it gets booked, investigated, or accepted with documentation.

Reconciliations run in **BlackLine**, the close-and-reconciliation workflow system. They live alongside but are distinct from the close (Category 1) — reconciliations are typically prepared and signed off **after** the books close for the period, but they're monitored throughout the close.

The 15-scenario orphan-exception family makes this the **largest single workflow family in the universe** by anchored scenarios.

## Why it matters

Reconciliations are the trust layer over the GL. If a recon doesn't balance and the variance isn't explained, you don't know whether the GL is right. Auditors will pull recons to test, so a recon that's been certified must be defensible.

## Authoring checklist

> **🎓 CPA-heavy category.** Reconciliations require accounting judgment to decide whether a variance is real, immaterial, a timing artefact, or evidence of a posting error. The concepts a Cat 7 task leans on are: **the reconciliation itself** (matching the GL balance for an account to the supporting detail — subledger, bank statement, vendor confirmation), **variance materiality** (under $10 is immaterial; $10–$1K is addressable; over $1K is urgent), **preparer / reviewer / certifier independence** (different people own each role on the recon, mirroring the Cat 4 independence test), **the six BlackLine exception types** explained in the plain-English table below, and the **stale-SLA polling-bug pattern** (a reminder re-fires on an already-closed exception — the right response is to dismiss, not reopen). The narrative below works through each. Excel is the primary surface — the spreadsheet does the work; BlackLine is the workflow tracker around it.

| Field | Value |
|---|---|
| **Eligible acting personas** | **George McAdam** *(primary)*, **Edith Banda**, **Jones Harrison** (Seniors — own the reconciliation file and triage live exceptions); **Daniel Jones** (Manager — reviewer / certifier on month-end recons); **Ryan Delgado** (Audit Senior — identifier on many orphan-exception scenarios, audit-side approver on closures); **Mia Hartwell** (Audit Staff — tick-and-tie / detail-testing support on recons; *new in v47, not yet anchored in scripted scenarios*); **Harry Marks**, **Emily Adekole**, **Blue Evans** (Associates — prepare standard recons); **Ben Arinzo**, **Sean Williams** (Bookkeepers — prepare cash and AP recons); **Green Spatz**, **Anaya Wallace**, **Elita Moore** (Trainees — preparers under senior review, especially the FX-recon refreshes); **Tom Chang** (Tax Associate — common acting voice on stale-SLA dismissals when the original closure was tax-side). |
| **Other entities touched** | All three. The largest recon volume is on `acme_cloud` and `northstar_legal`; `brookfield` recons are firm-internal and run on the same BD0–BD8 cadence as the close. |
| **External / NPC participants** | **James Randall** (E&P Audit Senior NPC — original certifier on many stale-SLA exceptions, named approver across the orphan-exception family); **Hannah Grant** (Corporate Tax Senior — cross-discipline reviewer when the variance has a tax-treatment angle); **Mateo Kovac**, **Nia Okafor** (NPC bookkeepers — assigned preparers on some recons); **Anita Knowles** (AML Supervisory Officer NPC — receives the audit-trail recap when a stale-SLA dismissal touches AML). |
| **Primary systems** | **Microsoft Excel** (the reconciliation workbook itself — pulls GL balance, lists supporting items, computes variance, holds the explanation; attached to the BlackLine record); **BlackLine** (recon record with `gl_balance`, `supporting_balance`, `variance`, `state`; exception list; preparer/reviewer/certifier signatures; SLA reminders); **Oracle GL** (verify JE existence, find prior similar corrections); **SAP Subledger** (transaction detail behind variances); **Records Vault** (closure memos, dismissal rationale, support docs under `AICPA_SQMS_7Y`); **Email + Slack `#monthly-close-coordination`** (audit-trail recap routing). |
| **Primary artifacts** | Reconciliation workbook (Excel) + BlackLine recon record; corrective JE (`is_standard_entry: false`) with full lifecycle (draft → submit → approve → post); exception update with `state`, `root_cause`, `resolution_summary`, `corrective_journal_entry_id`; review note; dismissal memo (for stale-SLA pattern) under `AICPA_SQMS_7Y`. |
| **Linked study scenarios** | Stale-SLA dismissals: scen_001, 005, 006, 013, 014, 015, 018. Live exception triage: scen_009, 010, 011, 012, 019, 020, 021, 022. Variance JE (Cat 7.3): scen_053. FX variance review: scen_039, 040 (Cat 7.4); scen_055 (Cat 7.5, month-end FX revaluation). 19 anchored scenarios total — the largest single-family in the universe. |

## Variance materiality thresholds

| Variance | Treatment |
|----------|-----------|
| Under $10 | Immaterial. Acceptable as-is. |
| $10 – $1,000 | Should be addressed, but not critical. May be fixed via a journal entry in a subsequent month. |
| Over $1,000 | Urgent. Demands investigation and a documented explanation before the recon can be certified. |

Some accounts have a "normal" variance — a structural error that can't be cleanly fixed but is known and identified. These are documented in the recon's variance explanation rather than booked away.

## Tools

- **Microsoft Excel** is where the actual reconciliation work happens — pulling the GL balance for an account, listing the supporting items, computing the variance, writing the explanation. The Excel workbook is the artifact that has to make sense to a reviewer or auditor; everything else is metadata around it.
- **BlackLine** is the document store and workflow tracker — it holds the spreadsheet as an attachment, records the GL balance / supporting balance / variance fields, captures the preparer / reviewer / certifier signatures, and runs the SLA reminders. In a smaller firm or one without BlackLine, the same recs would live in a shared drive with the workflow tracked manually.

## Exception types — plain English

BlackLine flags six recurring problem patterns. The system labels them with schema codes; here's what each one actually means when you see it on a recon:

| Schema code | What it means in plain English |
|---|---|
| `duplicate_entry_detected` | The same transaction got posted to the ledger twice. The recon won't tie until one copy is reversed. |
| `unrecorded_invoice` | An invoice exists on the subledger or in supporting docs but never made it into the GL. The recon shows more on one side than the other. |
| `timing_difference_over_sla` | Something posted to the subledger after the GL cutoff, so the GL balance and the supporting balance are temporarily out of sync. Usually resolves on its own next period, but if it's been open past SLA it needs a documented explanation or a corrective accrual. |
| `fx_revaluation_drift` | A foreign-currency-denominated balance hasn't been revalued at the current period-end rate, so the GL balance no longer matches the supporting balance translated at the right rate. |
| `subledger_feed_drop` | The overnight feed from the subledger to the GL didn't run or didn't complete. The two systems are out of sync because data is missing, not because anything's wrong. |
| `missing_accrual_variance` | An expected accrual entry never got booked. The supporting calculation shows it should be there; the GL doesn't reflect it. |

## Subcategories

### 7.1 Stale-SLA Reminder Dismissal

A known polling-bug pattern: a stale SLA reminder re-fires on an **already-closed exception**. The right response is **not** to reopen — it is to confirm the closure trail (the prior closure document in Records Vault and the original approver's email), dismiss the reminder with a one-line reason, log the pattern in #monthly-close-coordination for the running occurrence list, and email the partner a one-paragraph audit-trail recap.

If the same exception has re-fired three or more times, open a Linear issue on `team_comp` so the systemic bug gets a real ticket.

**Read:** `reminder_list_reminders`, `blackline_get_exception_by_id` (closed exception lookup), `records_vault_search_documents` (prior closure docs), `email_search_emails` (original closure approval), `conversations_history` on `#monthly-close-coordination`.

**Write:** `reminder_dismiss_reminder` (with `dismissal_reason`), `blackline_create_review_note` (cleanup rationale), `records_vault_upload_document` (dismissal memo), `email_send_email` (partner audit-trail recap), `conversations_add_message` (running occurrence list), `linear_create_issue` (systemic ticket).

**Linked scenarios:** scen_001 (the canonical case — `exc_151b0bee7e374e` on AR `110000`, $647.97, closed August 2025), scen_005 (`exc_df0e3e636dfd4d`, account `219000`, $46.52), scen_006 (Cash Operating `101000`, Brookfield audit-prep week), scen_013 (Northstar July exception), scen_014 (Northstar FX-drift dismissal), scen_015 (Northstar payroll-tax-withholding), scen_018 (Acme February FX revaluation drift).

**Example.**

> A BlackLine reminder for exception `exc_151b0bee7e374e` on `110000` ($647.97) re-fired this morning, but the exception was closed in August 2025 by James Randall and the closure email is in Records Vault. Confirm the closure trail (closure doc + August approval email), surface the recurring polling-bug pattern in #monthly-close-coordination, dismiss the reminder with a one-line reason, and email Matthew Li a one-paragraph audit-trail recap for his sign-off. Do not reopen. If this is the third re-fire, open a Linear issue for the systemic bug.
>
> *Prompt written by Tom Chang, Tax Associate.*

### 7.2 Live Exception Triage & Approval Chase

For currently-open exceptions, the workflow is investigative: the assignee pulls SAP subledger detail, compares to prior similar JEs in Oracle GL, gets a tax or audit reviewer's input on domain context, and decides whether to post a corrective JE or accept it as a documented timing difference. The exception is updated with `state`, `root_cause`, `resolution_summary`, and (if a JE was posted) `corrective_journal_entry_id`. A review note is added.

**Read:** `blackline_get_exception_by_id`, `sap_subledger_list_subledger_transactions`, `oracle_gl_search_journal_entries` (prior similar corrections).

**Write:** `oracle_gl_create_journal_entry` (corrective JE if needed, `is_standard_entry: false`, full lifecycle with 5-minute minimums), `blackline_create_review_note`, exception update (state/root_cause/resolution_summary/corrective_journal_entry_id).

**Linked scenarios:** scen_009 (Brookfield FP-2026-05 payroll-tax-downstream), scen_010 (`exc_1ddfc978ce5a4d`), scen_011 (`exc_06b89e3937b04a` deferred-revenue context), scen_012 (`exc_652c0931bb2546` tax-associate), scen_019 (`exc_cb0a9a94a3084c` on account `132000`), scen_020 (urgent SLA-breached $6,328.86 duplicate-entry on AP `210000`), scen_021 (Northstar cash-operating `exc_af7274fb658844`), scen_022 (urgent $-6,068.91 duplicate-entry on prepaid software `131000`).

**Example.**

> BlackLine exception `exc_a0f77f2a19104e` on account `210000` for `brookfield_FP-2026-05` is high-urgency — $6,328.86 duplicate-entry, SLA-breached. Hannah Grant identified the duplicate; Ryan Delgado is the named approver. Pull the SAP subledger transactions behind the variance, find the duplicate posting, and post the reversing JE through its full lifecycle (`is_standard_entry: false`, draft → submit → approve → post with the 5-minute minimum between transitions). Update the exception with `state=closed`, root_cause, resolution_summary, and corrective_journal_entry_id. Add a BlackLine review note explaining the duplicate source and email Daniel Jones with the SLA-breach optics so he can frame it for partner.
>
> *Prompt written by George McAdam, Accounts Senior.*

### 7.3 Reconciliation Variance Triage

A recon surfaces a residual variance. The reviewer (sometimes a tax reviewer, since GBP-payment-timing or revenue-recognition angles are common) judges the booking direction. If the variance is over $1K, it's posted as an adjusting JE (`is_standard_entry: false`) in the current period. Under $1K and uncertain, it's documented and rolled to a subsequent month.

**Read:** `blackline_get_reconciliation_by_id`, `oracle_gl_search_journal_entries` (prior similar adjustments), `sap_subledger_list_subledger_transactions` (detail behind the variance).

**Write:** `blackline_create_review_note`, `oracle_gl_create_journal_entry` (corrective JE if posted).

**Linked scenarios:** scen_053 (Brookfield BlackLine residual variance $3,409.86 prepaid CPE on `BL-390E6284EC1D`).

**Example.**

> Reconciliation `BL-72E451657112` on `101000` for `northstar_legal_FP-2026-05` is flagging a `timing_difference_over_sla` exception (`exc_af7274fb658844`, currently `investigating`) — a $572.87 variance attributed to deposits that cleared on the subledger after the GL cutoff. Pull the SAP subledger transactions behind it and the prior-period similar adjustment from Oracle GL, decide whether to post a corrective accrual JE or accept it as a documented timing difference, then update the exception (`state`, `root_cause`, `resolution_summary`, `corrective_journal_entry_id`) and add a review note. If you post a JE, route it through its full lifecycle first.
>
> *Prompt written by George McAdam, Accounts Senior.*

### 7.4 FX Variance Review / Recon Currency Refresh

A standing review on FX-denominated reconciliations. The trainee (Green Spatz on Northstar EUR; Anaya Wallace on Acme GBP) runs the refresh, isolates the variance, and submits. The senior (George McAdam) reviews and coaches; a second senior (Edith Banda) cross-ties the closing rate independently; the engagement manager (Daniel Jones) authorizes disposition.

**Read:** `blackline_get_reconciliation_by_id`, `records_vault_search_documents` (FX rate snapshot, prior FX recon support).

**Write:** `blackline_create_review_note`, `oracle_gl_create_journal_entry` if a corrective FX JE is booked.

**Linked scenarios:** scen_039 (Northstar EUR FX revaluation rounding variance $2.31 on `BL-AA054D9F0898`), scen_040 (May FX variance $6,328.86 on `BL-516B536953DA`, single GBP Acme Research line).

**Example.**

> The May FX variance review on `BL-516B536953DA` flagged a $6,328.86 variance on account `210000` driven by a single GBP-denominated Acme Research line. Anaya Wallace ran the FX refresh and submitted the recon; Edith Banda cross-tied the GBP closing rate independently. Review the supporting workbook in Records Vault, confirm Edith's rate cross-tie matches the period-end rate snapshot in the FX standing record, and decide whether the variance should be booked as an FX revaluation adjusting JE or left as a documented timing difference that rolls to June. Add your review note in BlackLine and route to Daniel Jones for engagement-manager authorization.
>
> *Prompt written by George McAdam, Accounts Senior.*

### 7.5 Month-End FX Revaluation

Recurring month-end FX JE prep. Ryan Delgado owns the period-end rate snapshot and confirms it; Anaya Wallace (trainee) prepares the recurring revaluation JE; George McAdam approves and closes the period entry.

**Read:** `records_vault_search_documents` (period-end rate snapshot, prior FX revaluation memo), `oracle_gl_search_journal_entries` (FX-denominated balance JEs), `blackline_list_exceptions` (prior `fx_revaluation_drift` flags).

**Write:** `oracle_gl_create_journal_entry` (recurring FX revaluation, `is_standard_entry: true`, full lifecycle), `records_vault_upload_document` (rate-snapshot-anchored support memo, `AICPA_SQMS_7Y`).

**Linked scenarios:** scen_055 (Acme FP-2026-04 FX revaluation).

**Example.**

> Acme Cloud's FP-2026-04 month-end FX revaluation is ready to post. Ryan Delgado already confirmed the period-end rate snapshot and uploaded it to Records Vault. For each FX-denominated balance flagged in the prior month's `fx_revaluation_drift` exceptions, pull the closing balance from Oracle GL, apply the new rate, and book the revaluation JE as a single consolidated entry on `acme_cloud_FP-2026-04` (`is_standard_entry: true`, full lifecycle with 5-minute minimums). Upload one support memo to Records Vault under `AICPA_SQMS_7Y` with the rate-snapshot reference, refresh the affected BlackLine reconciliations, and email George McAdam for approval.
>
> *Prompt written by Anaya Wallace, Trainee Accountant.*

---

# Category 8 — Engagement Mgmt & Client Operations

## What it is

Engagement management is the **business side** of an engagement — keeping it scoped, profitable, and well-coordinated — rather than the technical accounting side. When a client engagement runs over budget, the firm has to decide whether to absorb the cost or formally amend the engagement letter (a change order). When an engagement quietly accumulates uncollected receivables, someone has to review and act on the aging. When a new client signs an engagement letter, someone has to stand up every system to support the new work.

## Why it matters

Bad engagement management bleeds margin. An OOS overrun absorbed quietly costs the firm partner-level economics; a change order conversation handled badly costs the firm the client. Quarterly AR aging that's ignored becomes a write-off (Category 1 bad-debt subcategory).

## Authoring checklist

> **🛠 No-CPA-required category.** Engagement management is scope, budget, and client-coordination work — the kind of business operations that any organized professional can author. The concepts that show up in Category 8 are **the engagement letter** (the signed contract that defines what work is in-scope and what the client agrees to pay), **out-of-scope (OOS) work** (client requests or firm recommendations for work beyond what the engagement letter covers — the firm has to decide whether to absorb, decline, or convert to a change order), **change orders** (formal addenda to the engagement letter that document additional work + additional fee, executed by both parties), **AR aging** (a quarterly review of unpaid invoices grouped by client and bucketed by how long overdue — the trigger for collection action or write-off), and **client onboarding** (standing up Airtable + Records Vault + Oracle GL access + AML kickoff + welcome for a new client). The narrative below walks through each. ⚠️ **Some 8.x subcategories are CPA-heavy** even though the category as a whole is generalist-friendly — flagged inline where they appear.

| Field | Value |
|---|---|
| **Eligible acting personas** | **Andrea Phil** (Partner — owns the absorb-vs-change-order disposition on the Acme overrun); **Matthew Li** (Partner — signs engagement-letter addenda); **Daniel Jones** (Manager — runs quarterly AR-aging reviews, coordinates change-order packages); **George McAdam** *(primary)*, **Edith Banda**, **Jones Harrison** (Seniors — draft change-order proposals, run the budget-overrun analysis); **Marcus Knell** (Billing Coordinator — *new in v47*, owns the WIP-to-invoice conversion that feeds AR aging; natural author on AR-aging review prep and billing-cycle coordination tasks; not yet anchored in scripted scenarios). |
| **Other entities touched** | Primarily `acme_cloud` (the canonical OOS / change-order anchor — scen_064, scen_065, scen_066); also `northstar_legal` and `brookfield` engagement-letter mechanics. New-client onboarding is entity-creating (Halcyon Bridge in scen_060 as design reference). |
| **External / NPC participants** | Client-side CFOs/controllers as counterparties on change-order negotiations; **Lucia Ferreira** (NPC — Client Onboarding Specialist who actions the admin steps on new-client setups); **Margot Reyes**, **Anaya Patel** (NPC coordinators — workflow administration on onboarding and AR follow-ups). |
| **Primary systems** | **Airtable** (engagement-budget queue — e.g., `ENG-BUDGET-acme_cloud-FY2026-Q1`; Client Access and Onboarding Admin table; Annual Report Filing Control); **Records Vault** (engagement letter under `FIRM_INTERNAL`; engagement change order; AR-aging review memos under `AICPA_SQMS_7Y`); **Oracle GL** (`110000` AR for the aging snapshot; chart-of-accounts provisioning for new clients); **Email** (CFO negotiation, partner routing); **Calendar + Reminder** (kickoff events, milestone reminders); **Linear** (workstream setup tasks for new clients). |
| **Primary artifacts** | Engagement letter (`FIRM_INTERNAL`); engagement change order (`AICPA_SQMS_7Y`); engagement-budget Airtable record with overrun annotation queue; AR-aging quarterly report (one per client bucket); new-client onboarding plan (`AICPA_SQMS_7Y`); welcome email + access-grant package. |
| **Linked study scenarios** | scen_064 (Acme OOS review + April overrun); scen_065 (Acme change-order package); scen_066 (Acme quarterly AR aging — the canonical 8.2 anchor, cross-discipline); scen_060 (Halcyon Bridge new-client onboarding — *design reference, deferred*); scen_049 (trainee onboarding — *design reference, deferred*). |

## Subcategories

### 8.1 Out-of-Scope Review & Change Orders

The pattern (scen_064 → scen_065): the Acme Cloud April engagement ran +15 hours over budget on multi-state sales-tax coding plus AR-aging cleanup. George McAdam (Accounts Senior) surfaced the overrun; Daniel Jones (manager) weighed the fee impact; Edith Banda (prior-year Acme senior) provided historical comparator data; Andrea Phil (partner) made the absorb-vs-change-order disposition. The disposition was change order, so a formal change-order package was drafted, emailed to Andrea cc Matthew Li, the draft uploaded under `AICPA_SQMS_7Y`, a calendar slot for CFO negotiation booked, and the signed engagement-letter addendum filed in Records Vault under `kind: engagement_letter_addendum`.

**Read:** `airtable_get_record` (engagement-budget annotation queue `ENG-BUDGET-acme_cloud-FY2026-Q1`), `records_vault_search_documents` (engagement letter, prior change orders), `oracle_gl_search_journal_entries` (work-volume proxy), `conversations_history` on the engagement-budget thread.

**Write:** `email_send_email` (partner routing, CFO negotiation), `records_vault_upload_document` (change order + addendum), `airtable_update_record` (status flip), `calendar_create_event` (CFO call), `conversations_add_message`.

**Linked scenarios:** scen_064 (Acme April OOS review), scen_065 (Acme formal change-order package).

**Example.**

> Per Andrea Phil's prior disposition on the April overrun, open Acme Cloud's formal change-order workflow for two scope lines: sales-tax work (TX/NY/WA/AZ taxable per the Cat 3.1 framing; the engagement-budget overrun absorbed the extra hours Tom Chang spent reworking TX nexus on per-ZIP local rates and unwinding the historical CA-only standing entries) and AR-aging bucket cleanup. Pull the engagement-budget annotation queue `ENG-BUDGET-acme_cloud-FY2026-Q1` from Airtable and the FY2026 engagement letter. Draft the change-order proposal citing the FP-2026-04 overrun data and the parent engagement letter, email it to Andrea cc Matthew Li, upload the draft under `AICPA_SQMS_7Y`, and post a breadcrumb in the engagement-budget thread.
>
> *Prompt written by George McAdam, Accounts Senior.*

### 8.2 Quarterly AR Aging Review

A multi-discipline workflow. Daniel Jones (manager) oversees Acme; Anaya Wallace (trainee) pulls AR aging buckets; George McAdam (senior) reviews and drafts the package; Ben Arinzo (bookkeeper) provides cash-receipts context for cited Acme customers; Hannah Grant (tax senior) frames tax-implication context. Anything that crosses the bad-debt threshold gets routed to Category 1's adjusting-entry workflow for write-off (allowance method on `117000`).

**Read:** `oracle_gl_search_journal_entries` (AR account `110000` aging), `sap_subledger_list_subledger_transactions` (cash-receipts history), `records_vault_search_documents` (prior AR package + bad-debt watchlist).

**Write:** `records_vault_upload_document` (Q1 AR review package, `AICPA_SQMS_7Y`), `email_send_email`, `conversations_add_message` in `#monthly-close-coordination`.

**Linked scenarios:** scen_066 (Acme Q1 2026 quarterly AR aging review).

**Example.**

> Acme Cloud's Q1 2026 quarterly AR aging review is due before partner read. Anaya Wallace has pulled the aging buckets from Oracle GL; Ben Arinzo has the cash-receipts context on the cited customers; Hannah Grant left prior-quarter comments framing the tax implications. Pull all three into a single package: walk the 30/60/90+ buckets on account `110000`, identify any balance that crosses the bad-debt threshold (over $1K with no payment activity in two quarters), and either propose a write-off (route to Category 1's adjusting-entry workflow against the `117000` allowance) or document the collectibility narrative for retention. Draft the Q1 AR review package to Records Vault under `AICPA_SQMS_7Y` and email George McAdam to draft the partner cover.
>
> *Prompt written by Daniel Jones, Accounts Manager.*

### 8.3 Client Onboarding *(design surface, deferred scenario only)*

The full new-client stand-up: signed engagement letter filed under `FIRM_INTERNAL` → Airtable client and engagement records created with portfolio assignment → Records Vault client folder opened with scoped access grants → Oracle GL chart-of-accounts provisioned → AML / beneficial-owner onboarding routed to Marina Soko → matching `restricted` placeholder opened in Records Vault → kickoff calendar event + milestone reminders for first close + first filing → client-side contacts added → Linear setup tasks opened for accounting, tax, compliance workstreams → welcome email sent. Confirm each system reflects the new engagement before closing the setup checklist.

**Linked scenarios:** scen_060 (Halcyon Bridge onboarding — **deferred; design reference**).

**Example.**

> A new outsourced-accounting client, Halcyon Bridge Advisory, has a signed engagement letter filed in Records Vault — I'm taking the engagement on for my book. Stand the engagement up end-to-end: have the onboarding admin team (Lucia Ferreira) create the client and engagement records in Airtable and assign the portfolio; open the Records Vault client folder with scoped access grants for the assigned team (engagement letter `FIRM_INTERNAL`, working papers `AICPA_SQMS_7Y`); provision the client's chart-of-accounts scope in Oracle GL; route the AML / beneficial-owner onboarding to Marina Soko and open the matching `restricted` placeholder in Records Vault; create the kickoff calendar event plus milestone reminders for the first close and first filing; add the client-side contacts; open the Linear setup tasks for the accounting, tax, and compliance workstreams; and send the welcome email. Confirm each system reflects the new engagement before closing the setup checklist.
>
> *Prompt written by Daniel Jones, Accounts Manager.*

### 8.4 Vendor & System Coordination

Oracle GL vendor support (Jane Founders for onboarding, Brenda Abbas for account management on Acme close + AP escalations), banking-side coordination (Amira Siddiqui), retained legal counsel (Linda Burns on state compliance + Code of Conduct matters), external audit firm (James Randall at E&P).

**Read:** `oracle_gl_list_subledger_feeds` / `list_subledger_feed_runs` (vendor-feed status), `contacts_list` (NPC counterpart records), `email_search_emails` (vendor escalation threads).

**Write:** `messaging_send_message` (DM to vendor account manager), `email_send_email` (partner-routed status update), `linear_create_issue` (Client Accounting Operations team for incident tracking).

**Linked scenarios:** No standalone scenario today. The example below is constructed from the existing NPC counterpart relationships documented in the persona briefs (Jane Founders, Brenda Abbas) and the Oracle GL subledger-feed infrastructure.

**Example.**

> The Oracle GL nightly subledger feed for Acme Cloud's intercompany allocation has failed two consecutive nights — Jane Founders escalated by email this morning. Pull the last successful run from Oracle GL, confirm the failure mode (feed config vs. source system), and DM Brenda Abbas for vendor-side context. If the failure looks vendor-side, draft a partner-routed update to Andrea Phil so she knows Acme close is at risk of a 12-hour delay; if it looks internal, open a Linear issue on the Client Accounting Operations team. Either way, file the incident note to Records Vault under `AICPA_SQMS_7Y` and post status in `#cash-management-and-banking`.
>
> *Prompt written by Daniel Jones, Accounts Manager.*

---

# Category 9 — Executive / Partner Oversight

## What it is

Partner-level cross-functional work: AP > $50K approvals, firm-state risk pulls that aggregate across every system, escalation routing on AML and OOS matters, and the refusal-handling pattern when client requests cross policy or GAAP lines.

This is the smallest training category by volume but the highest in stakes. Tasks here are written *as* a partner only when the work is genuinely theirs (sign-off, partner risk pull, refusal decision); partners appearing as reviewers inside other personas' tasks belong in those other categories.

## Authoring checklist

> **🎓 CPA-heavy category.** Partner oversight cuts across every other category, so the concepts that show up depend on what's being approved or escalated: **the AP approval ladder** (clerk → manager → controller → managing partner, by amount tier — Cat 6.3), **firm-state risk thresholds** (the watchlist of signals the partner expects rolled up: BlackLine open exceptions, AP aged > 60 days, AML dispositions > 30 days without follow-up, audit PBC < 80% at milestone, OOS threads stalled > 2 weeks), the **OOS / change-order disposition** (absorb vs. amend the engagement letter — Cat 8.1), and the **improper-request refusal** chain (Cat 4.7). The narrative below describes each at the partner level. Authoring tasks *as* a partner only makes sense when the partner is the genuinely-required decision-maker — if the work is a routing step or a draft, author from the manager or senior seat instead.

| Field | Value |
|---|---|
| **Eligible acting personas** | **Steven Perry** (Managing Partner — > $50K AP on Brookfield/Acme, firm-state risk pulls, refusal-handling escalations); **Matthew Li** (Accounting Services Partner — > $50K AP on Northstar, audit + annual-accounts sign-off); **Andrea Phil** (Partner, Accounting Services — de-minimis AP, OOS disposition on her engagements, cross-functional risk pulls); **Julia Vance** (Audit Partner — audit-side quarterly clearance, cross-review on independence control test); **Ming Chang** (Tax Partner — tax-side cross-functional risk, IRS challenge escalation); **Peter Sanchez** (Head of Compliance — quarterly control-test clearance bridging Cat 4 and Cat 9). |
| **Other entities touched** | All three. Partner sign-off and risk-roll-up runs firm-internal but draws data from every entity. |
| **External / NPC participants** | All the operational NPCs and externals feed signals up to this category: **Anita Knowles** (AML supervisory escalation), **James Randall** (audit-side counterpart at E&P), **Brenda Abbas** (vendor-side context), **Priya Singh** (IRS-side counterpart), **Margaret Sullivan** (client-side reviewer), **Owen Mercer** (AP queue trigger source). None author tasks. |
| **Primary systems** | **All systems.** Cat 9.2 (firm-state risk pull) is the only place in the universe where the task spec literally reads across every backend — Oracle GL, SAP Subledger, BlackLine, Records Vault, Airtable, Linear, Email, Slack, Messaging, Calendar, Reminder, Contacts. Other 9.x subcategories anchor on the systems that feed their decision (SAP for 9.1, Records Vault + Slack engagement-budget threads for 9.4). |
| **Primary artifacts** | Partner-approval memo (one-paragraph chain-summary); firm-state risk one-pager (`AICPA_SQMS_7Y`, firm-internal); quarterly control-test final clearance addendum; OOS disposition post in the engagement-budget thread; refusal email + Linear pressure-event issue (cross from Cat 4.7). |
| **Linked study scenarios** | 9.1 (AP > $50K): scen_029, 031, 032 (Steven Perry on Acme), scen_034, 036 (Matthew Li on Northstar), scen_030, 035 (Andrea Phil de-minimis). 9.2 (firm-state risk pull): **no scripted scenario** — built from the thresholds above; closest study templates are scen_062 (4-function AML soft-flag) and scen_066 (4-function quarterly AR) for the cross-system muscle. 9.3 (quarterly control-test clearance): scen_042 (independence test), scen_044 (retention sweep), scen_041 (AML wire-flag). 9.4 (escalation routing & refusal): scen_064 → scen_065 (Acme OOS → change-order disposition chain). |

## Subcategories

### 9.1 AP Threshold Approvals (> $50K)

Verifying the lower-tier approval chain is fully documented before the > $50K invoice routes to the Managing Partner. Steven Perry signs for Brookfield and Acme; Matthew Li signs for Northstar; Andrea Phil signs de-minimis cases. (Implementation details in Category 6.3.)

**Read:** `sap_subledger_get_ap_invoice_by_id`, `records_vault_search_documents` (supporting contract), `email_search_emails` (lower-tier approvals).

**Write:** `email_send_email` (sign-off + cost-center confirmation), `sap_subledger_update_ap_invoice` (approver field update), `conversations_add_message` in `#vendor-bills-and-ap`.

**Linked scenarios:** scen_029, 031, 032 (Steven Perry on Acme AP), scen_033, 034, 036 (Matthew Li on Northstar AP), scen_030, 035 (Andrea Phil de-minimis). *(These are partner-by-entity disposition references, not literal > $50K cases — every scripted AP escalation is under $50K, the largest being scen_031 at ~$39K. The > $50K Managing-Partner tier itself is illustrated by the hypothetical $87,400 invoice in the example below.)*

**Example.**

> A SAP Subledger AP invoice for $87,400 is sitting at "Controller signed" status — final approval needs the managing-partner sign-off. Pull the invoice from SAP, verify the full lower-tier approval chain is documented (AP clerk coded, AP manager approved ≤ $10K, Controller signed ≤ $50K), confirm the supporting contract is in Records Vault under `AICPA_SQMS_7Y`, and check that the cost-center allocation is correct. Route to me with a one-paragraph approval memo confirming the chain is intact; once I sign, update the SAP approver field and post a quick confirm in `#vendor-bills-and-ap`.
>
> *Prompt written by Steven Perry, Managing Partner.*

### 9.2 Cross-Functional Risk Pull (Firm-State Risk One-Pager)

**Concrete shape of this task.** Imagine Steven Perry walks into the Monday partner meeting and asks: *"What should I be worried about across the firm right now?"* The answer is a one-page memo that pulls every loose-end signal from every system and ranks them by how close they are to hurting a client engagement, a regulator response, or a partner sign-off deadline. This is the only place in the universe where the deliverable is genuinely cross-functional — the agent has to read **AP aging in SAP**, **open BlackLine exceptions**, **AML dispositions in Records Vault**, **audit PBC status in Airtable**, and **engagement-budget threads in Slack** and synthesize them into one prioritized view. The judgment is "what rises to partner attention" — most of what comes back from each system is noise; the partner only wants the signals that demand intervention this week.

A partner asks for the one-pager. The agent aggregates across all systems: BlackLine open exceptions, SAP AP invoices aged > 60 days, AML dispositions older than 30 days without follow-up, audit engagements with PBC closure < 80% by milestone, OOS / change-order threads that haven't moved in two weeks. The one-pager is filed to Records Vault under `AICPA_SQMS_7Y` (firm-internal), emailed to the partner group, with a two-line teaser in `#general`.

This is the most cross-functional task in the universe — it touches every category. There is **no scripted scenario** for the firm-state risk pull itself; the agent builds it from the thresholds above. The closest scripted study scenarios are scen_062 (4-function AML soft-flag) and scen_066 (4-function quarterly AR) — both useful templates for the "read across all systems" muscle.

**Example.**

> Steven needs a one-page firm-state risk view for Monday's partner meeting. Aggregate across BlackLine open exceptions, SAP AP invoices aged > 60 days, AML dispositions older than 30 days without follow-up, audit engagements with PBC closure < 80% by milestone, and any OOS / change-order threads that haven't moved in two weeks. Write the one-pager to Records Vault under `AICPA_SQMS_7Y` (firm-internal), email Steven and the partner group, and post a two-line teaser in #general.
>
> *Prompt written by Andrea Phil, Partner, Accounting Services.*

### 9.3 Quarterly Control-Test Clearance

Final partner clearance on the quarterly compliance control tests (Category 4.4, 4.5). Steven Perry provides managing-partner-level clearance.

**Read:** `records_vault_search_documents` (the control-test memo + lower-tier sign-offs), `email_search_emails` (the Peter Sanchez → Julia Vance chain).

**Write:** `records_vault_upload_document` (sign-off addendum if needed), `email_send_email` (partner group), `conversations_add_message`.

**Linked scenarios:** scen_042 (quarterly partner sign-off control test), scen_044 (quarterly document retention sweep), scen_041 (AML wire-flag).

**Example.**

> Marina Soko's quarterly partner sign-off control test (the 5-recon sample anchored on `BL-A81316258BCB`) is up for managing-partner clearance. Pull her independence memo from Records Vault, confirm Peter Sanchez has signed off as Head of Compliance, confirm Julia Vance has reviewed as Audit Partner, and verify no control failure was identified in the sample. If everything is clean, sign the final clearance line in the memo and email the partner group; if anything was flagged, route back to Marina with the specific concern before clearance.
>
> *Prompt written by Steven Perry, Managing Partner.*

### 9.4 Escalation Routing & Refusal Handling

Partner-routing decisions: absorb vs change order on OOS, soft-watch vs full escalation on AML soft-flags, and GAAP-improper-request refusal (Category 4.7). When the call is genuinely partner-level, the task is authored as a partner (or executive) and lives here in Category 9; when it's merely the routing of a question *to* a partner, the task is authored as the manager or senior making the routing decision and belongs in its originating category (e.g., Cat 4.7 or Cat 8.1), not here. Category 9 itself is authored only from partner / executive seats.

**Read:** `records_vault_search_documents` (overrun narrative, engagement letter, comparator data), `conversations_history` on the engagement-budget thread.

**Write:** `conversations_add_message` (disposition post in the engagement-budget thread), `email_send_email` (kickoff of formal workflow if needed).

**Linked scenarios:** scen_064 → scen_065 (Acme OOS → change-order disposition chain).

**Example.**

> The Acme Cloud April overrun has been sitting in the engagement-budget thread for a week without a partner call. George McAdam quantified +15 hours over budget on multi-state sales-tax coding and AR-aging cleanup. The choice is absorb or change-order. Read George's overrun narrative in Records Vault, the FY2026 engagement letter to confirm the scope-of-work boundary, and the prior-year comparator data Edith Banda pulled. Make the call: if absorb, post the disposition in the engagement-budget thread with reasoning; if change-order, post the kickoff disposition and email George to open the formal change-order workflow (Category 8.1).
>
> *Prompt written by Andrea Phil, Partner, Accounting Services.*

---

# Category 10 — HR & People Operations

## What it is

Category 10 covers HR & People Operations: onboarding access provisioning (often co-anchored with Category 8 onboarding), appraisal scheduling, dispute coordination, and EEOC liaison. The four HR personas (Brent Noah, Clint Peterson, Rachel Green, Reshma Patel) are valid acting seats for these tasks. They also appear as participants/counterparties in cross-functional tasks authored from other categories (a senior resigning mid-close, a new accountant's access provisioning).

**Yusuf Demir** is an NPC (Talent Operations Specialist, npc_027), not a persona; like every NPC he can be named as a participant inside a task but is never the acting seat.

Category 10 carries a 9 training / 3 benchmark allocation.

## Authoring checklist

> **🛠 No-CPA-required category.** HR work is people-operations and coordination — none of it requires accounting credentials. The concepts that show up in Category 10 are **onboarding access provisioning** (standing up Oracle GL scope, Records Vault scope, Slack channels, email, calendar holds for a new hire), **appraisal cycle mechanics** (templates, one-on-one scheduling, 360 feedback, outcome documentation under `FIRM_INTERNAL`), **dispute coordination** (incident note → response options → partner sign-off → preserved under `restricted` access), and **EEOC liaison** (Equal Employment Opportunity Commission — the federal body that handles workplace-discrimination matters; the firm liaises with James O'Brien when conciliation is needed). The narrative below walks through each.

| Field | Value |
|---|---|
| **Eligible acting personas** | **Clint Peterson** (HR Operations Manager — primary on onboarding routing, dispute coordination day-to-day); **Rachel Green** (HR Business Partner — appraisal cycle, partner-level HR coordination); **Brent Noah** (Director of People and Culture — director-level dispute escalations); **Reshma Patel** (HR Generalist — appraisal scheduling and admin work); **Daniel Jones**, **Edith Banda**, **George McAdam** (Accounts Manager / Seniors — author Cat 10 tasks when bringing a new hire onto their own team or running team-level appraisals); **Steven Perry** (Managing Partner — sign-off on EEOC-level escalations). |
| **Other entities touched** | Firm-internal (`brookfield`). HR work doesn't touch the client entities directly. |
| **External / NPC participants** | **Yusuf Demir** (Talent Operations Specialist NPC, npc_027 — actions onboarding admin steps on the HR side); **Lucia Ferreira** (Client Onboarding Specialist NPC — partner role on cross-functional new-hire onboarding when access provisioning bridges into Cat 8); **James O'Brien** (Conciliation Officer at the EEOC — external counterpart on workplace-disputes liaison). |
| **Primary systems** | **Airtable** (Client Access and Onboarding Admin table); **Records Vault** (onboarding plan under `AICPA_SQMS_7Y`; appraisal templates + Q-update memos under `FIRM_INTERNAL`; incident notes and HR-folder docs under `restricted`); **Calendar** (orientation, 30/60/90 check-ins, appraisal one-on-ones); **Email** (welcome emails, HR-logging cc); **Oracle GL + Records Vault access provisioning** (scoping the new hire's portfolio access); **Slack** (channel grants — `#monthly-close-coordination`, `#vendor-bills-and-ap`, `#cash-management-and-banking`, etc., depending on team). |
| **Primary artifacts** | New-starter Airtable record; onboarding plan (`AICPA_SQMS_7Y`); welcome email; appraisal templates + Q-update memos (`FIRM_INTERNAL`); incident notes + response-options memo (`restricted`); EEOC outreach email + partner sign-off chain. |
| **Linked study scenarios** | scen_049 (trainee onboarding — *design reference, deferred*) is the closest scripted anchor. No fully merged Cat 10 scenarios in the universe — design from the patterns described in the subcategories below. |

## Subcategories

### 10.1 Onboarding & Access Provisioning

When a new hire (especially a trainee) joins, the operational work is provisioning access — Oracle GL scope, Records Vault scope, Slack channels, email accounts, calendar holds for orientation and 30/60/90 check-ins — and filing the onboarding plan to Records Vault. Two natural acting seats: **(a)** the HR persona running onboarding centrally (Clint Peterson or Rachel Green), or **(b)** the Accounts Manager or Senior bringing the new hire onto their team (Daniel Jones, Edith Banda, George McAdam). Lucia Ferreira (NPC) is named as the participant who actions the Airtable record and access grants on the admin side.

**Read:** `airtable_list_records` ("Client Access and Onboarding Admin" table), `records_vault_search_documents` (onboarding-plan template), `contacts_list` (HR-persona recipients for the cc list).

**Write:** `airtable_create_record` (new-starter record), `records_vault_upload_document` (onboarding plan, `AICPA_SQMS_7Y`), `calendar_create_event` (orientation + check-ins), `email_send_email` (welcome), access-provisioning routing in Oracle GL / Records Vault.

**Linked scenarios:** scen_049 (Elita Moore trainee onboarding — **deferred; design reference**).

**Example.**

> A new Trainee Accountant joins Edith Banda's team next Monday. Open the Airtable "Client Access and Onboarding Admin" record for the new starter, file the onboarding plan to Records Vault under `AICPA_SQMS_7Y`, set up Day-1 orientation as a calendar event, and schedule the 30/60/90-day mentor check-ins with Edith. Coordinate with Lucia Ferreira to provision Oracle GL access scoped to Edith's portfolio (Northstar Legal and the Acme close), Records Vault scoped to the same, and Slack access to `#monthly-close-coordination`, `#vendor-bills-and-ap`, and `#cash-management-and-banking`. Send the welcome email cc'ing Edith and Daniel Jones (the receiving manager), and confirm every system reflects the new starter before Day-1.
>
> *Prompt written by Clint Peterson, HR Operations Manager.*

### 10.2 Appraisal & Performance Cycle

Annual/semi-annual appraisal scheduling, 360 feedback solicitation, outcome documentation. Two natural acting seats: the HR persona running the firm-wide appraisal cycle (Rachel Green or Brent Noah, depending on level), or the Accounts Manager building a review schedule for their own direct reports (Daniel Jones, George McAdam).

**Read:** `records_vault_search_documents` (FY2025 appraisal templates + outcomes), `calendar_list_events`.

**Write:** `calendar_create_event` (one-on-one slots), `records_vault_upload_document` (Q2-update memo per senior, `FIRM_INTERNAL`), `email_send_email` (cc Rachel Green for HR logging).

**Example.**

> Q2 appraisals for the seniors on my team (George McAdam, Edith Banda, Jones Harrison) are due before end of June. Pull the FY2025 appraisal templates from Records Vault and the FY2025 outcomes for each. Schedule 60-minute one-on-ones with each over the next two weeks. For each senior, draft a one-page Q2-update memo: their scenarios delivered (cross-reference against the scenario index), any escalations they handled, and the development conversations from the FY2025 check-ins. File the memos to Records Vault under `FIRM_INTERNAL` and email Rachel Green the schedule so HR is looped in for the formal recording.
>
> *Prompt written by Daniel Jones, Accounts Manager.*

### 10.3 Disputes & EEOC Liaison

When an employee dispute or workplace-rights issue arises, the routing point is James O'Brien (EEOC Conciliation Officer NPC). Natural acting seats are the HR persona managing the matter day-to-day (Clint Peterson, with Brent Noah on the director-level escalations), or the partner responsible for people decisions (Steven Perry) when the matter needs partner sign-off or has engagement implications.

**Read:** `records_vault_search_documents` (Clint Peterson's incident note + prior matters in the HR folder), `calendar_list_events`.

**Write:** `calendar_create_event` (partner-HR walkthrough), `records_vault_upload_document` (response options memo, `restricted` access scoped to a named list), `email_send_email` (EEOC outreach drafted internally, partner sign-off before sending).

**Example.**

> An employee dispute has been escalated to me by Clint Peterson — it involves a Senior on one of the engagement teams. Read Clint's incident note in Records Vault under the HR folder (`FIRM_INTERNAL`). Schedule a 30-minute call with Clint and Rachel Green to walk through the incident timeline and the response options. If the matter rises to EEOC liaison, draft the outreach to James O'Brien at EEOC and route to me for sign-off before sending. File every step of the conversation under `restricted` access scoped to me, Clint, Rachel, and Andrea Phil.
>
> *Prompt written by Steven Perry, Managing Partner.*

---

# Scenario → category mapping (all 52 merged scenarios)

The category each scenario primarily anchors. Where the scenario crosses categories meaningfully, the secondary category is noted. Use this index when you've picked a category and want a real built example to study before authoring.

| Scenario | Primary | Secondary | Entity |
|----------|:-------:|:---------:|--------|
| scen_001_orphan_exception | 7.1 | — | brookfield |
| scen_005_orphan_exception | 7.1 | — | brookfield |
| scen_006_orphan_exception | 7.1 | 5 | brookfield |
| scen_009_orphan_exception | 7.2 | — | brookfield |
| scen_010_orphan_exception | 7.2 | — | brookfield |
| scen_011_orphan_exception | 7.2 | — | brookfield |
| scen_012_orphan_exception | 7.2 | 3 | brookfield |
| scen_013_orphan_exception | 7.1 | — | northstar_legal |
| scen_014_orphan_exception | 7.1 | 3 | northstar_legal |
| scen_015_orphan_exception | 7.1 | — | northstar_legal |
| scen_018_orphan_exception | 7.1 | 5 | acme_cloud |
| scen_019_orphan_exception | 7.2 | — | brookfield |
| scen_020_orphan_exception | 7.2 | — | brookfield |
| scen_021_orphan_exception | 7.2 | — | northstar_legal |
| scen_022_orphan_exception | 7.2 | — | brookfield |
| scen_023_monthly_close | 1.1 | — | brookfield |
| scen_024_monthly_close | 1.1 | — | brookfield |
| scen_025_monthly_close | 1.1 | — | northstar_legal |
| scen_027_monthly_close | 1.1 | — | acme_cloud |
| scen_028_monthly_close | 1.1 | — | acme_cloud |
| scen_029_ap_escalation | 6.1 | — | acme_cloud |
| scen_030_ap_escalation | 6.1 | — | brookfield |
| scen_031_ap_escalation | 6.1 | — | acme_cloud |
| scen_032_ap_escalation | 6.1 | — | acme_cloud |
| scen_033_ap_escalation | 6.1 | — | northstar_legal |
| scen_034_ap_escalation | 6.1 | — | northstar_legal |
| scen_035_ap_escalation | 6.1 | — | firm-internal |
| scen_036_ap_escalation | 6.1 | — | northstar_legal |
| scen_039_recon_currency_refresh | 7.4 | — | northstar_legal |
| scen_040_recon_currency_refresh | 7.4 | — | brookfield |
| scen_041_audit_compliance | 4.1 | 9.3 | acme_cloud |
| scen_042_audit_compliance | 4.4 | 9.3 | firm-internal |
| scen_043_audit_compliance | 5.1 | — | northstar_legal |
| scen_044_audit_compliance | 4.5 | 9.3 | firm-internal |
| scen_045_tax_regulatory | 3.1 | — | brookfield |
| scen_046_tax_regulatory | 3.3 | — | acme_cloud |
| scen_047_tax_regulatory | 3.4 | — | northstar_legal |
| scen_048_audit_compliance | 4.6 | — | brookfield |
| scen_051_fixed_asset_lifecycle | 1.1 | 7 | acme_cloud |
| scen_053_rec_adjusting_je | 7.3 | 1.1 | brookfield |
| scen_055_month_end_fx | 7.5 | 1.1 | acme_cloud |
| scen_056_bad_debt_writeoff | 1.1 | — | brookfield |
| scen_058_quarterly_reporting | 1.3 | 5.3 | northstar_legal |
| scen_059_wip_recognition | 1.4 | — | brookfield |
| scen_061_aml_bo_review_acme | 4.3 | — | acme_cloud |
| scen_062_aml_review_general | 4.2 | 9.2 | northstar_legal |
| scen_063_annual_accounts_prep_northstar | 1.5 | 5 | northstar_legal |
| scen_064_oos_review_acme | 8.1 | — | acme_cloud |
| scen_065_change_order_acme | 8.1 | — | acme_cloud |
| scen_066_acme_quarterly_ar | 8.2 | 1.3, 9.2 | acme_cloud |
| scen_067_acme_multi_state_sales_tax | 3.1 | 8.1 | acme_cloud |
| scen_068_northstar_annual_corp_tax | 3.2 | 5 | northstar_legal |

---

# Coverage observations

Scripted-scenario coverage is uneven by category, by design:

| Cat | Train target | Bench target | Anchored scenarios | Notes |
|----:|-------------:|-------------:|-------------------:|-------|
| 1 | 90 | 30 | **10** | Strong study set: 5 month-close (scen_023, 024, 025, 027, 028), 1 quarter-close (scen_058), 1 WIP→revenue (scen_059), 1 annual accounts (scen_063), 1 fixed-asset month-end (scen_051), 1 bad-debt write-off (scen_056). Adjusting-entry sub-types are well covered. |
| 2 | 24 | 8 | **0 direct** | No bookkeeping-anchored scenarios; rich underlay from L1 noise themes and L2 baseline state. |
| 3 | 30 | 10 | **5** | All major tax cycles + planning workshop. |
| 4 | 30 | 10 | **6** | Strong — wire-flag + soft-flag + BO refresh + 2 quarterly control tests + state catch-up. Refusal pattern is unscripted. |
| 5 | 18 | 6 | **3** | Light — one audit kickoff, one annual accounts, one Q1 partner package. |
| 6 | 36 | 12 | **8** | One per pattern; complete coverage of the AP escalation playbook. |
| 7 | 30 | 10 | **19** | Largest single-family in the universe (15 orphan-exception triage + scen_053 variance + scen_039/040 FX + scen_055 month-end FX revaluation). Orphan-exception is overrepresented vs target. |
| 8 | 21 | 7 | **3** | scen_064 → 065 → 066 is the entire I anchor chain. Onboarding (8.3) is deferred. |
| 9 | 12 | 4 | **0 primary** | No scenario primarily anchored at the partner level — partners appear as endpoint in many. Firm-state risk pull is **unscripted**; build from thresholds. |
| 10 | 9 | 3 | **0 merged** | scen_049 anchor is deferred. Build from spec. |

> *The "anchored scenarios" column counts each scenario under both its primary and any secondary category, so it sums to more than the 52 distinct merged scenarios — scen_058 and scen_063 are each counted under both Cat 1 and Cat 5, which is the source of the 2-scenario overlap.*

**Where to start by category:**

- For **1.1 Monthly Close**: scen_028 (Acme May with Datadog reclass) is the richest study scenario.
- For **6.1 AP Escalation**: scen_029 (TimeLedger Nexus, aged past SLA) is the canonical setup.
- For **7.1 Stale-SLA**: scen_001 is the canonical case; scen_005 is the simplest variant.
- For **7.2 Live Triage**: scen_020 (urgent SLA-breached $6,328.86 duplicate-entry) has the highest urgency.
- For **8.1 OOS/Change Order**: scen_064 → scen_065 is the full chain.
- For **4.2 AML Soft-Flag**: scen_062 is the only example and is template-quality.

---

# Quick reference — useful accounts for prompt design

**⚠️ The account *number* is not a guarantee of meaning.** Many account numbers are reused across entities for completely different concepts. The role/name column below is **per-entity** — never assume an account number alone tells you what an account holds. Always confirm against the entity's chart of accounts before reusing in a prompt.

| Account | Brookfield | Northstar Legal | Acme Cloud | Notes |
|---------|-----------|-----------------|-----------|-------|
| `101000` | Cash – Operating | Cash – Operating | Cash – Operating | Consistent across all 3 |
| `105000` | **Cash – Client Trust** | **IOLTA – Client Trust Account** | **Short-term Investments** | **⚠️ Same number, three different concepts.** All three entities have a 105000 account. Brookfield's is a generic client trust; Northstar's is the IOLTA lawyer-trust account (segregated client funds, lawyer-trust rules apply); Acme's is a marketable-securities account entirely unrelated to client trust. Do not assume IOLTA when you see 105000. |
| `110000` | AR – Client Billings | AR – Client Billings | AR – Subscription Billings | All entities have AR on 110000 |
| `117000` | Allowance for Doubtful Accounts | Allowance for Doubtful Accounts | Allowance for Doubtful Accounts | Contra-asset, allowance method |
| `119000` | Work in Process – Unbilled Services / Time | Work in Process – Unbilled Services / Time | — | Brookfield + Northstar billable services. Commonly abbreviated **WIP**; in this firm WIP always means unbilled revenue, not inventory. |
| `120000` | *(not in CoA)* | **Client Cost Advances** | **Deferred Commissions – Current** | **⚠️ Same number, two different concepts.** Acme uses 120000 for ASC 340-40 capitalized commissions; Northstar uses 120000 for client-disbursement advances (court costs, expert-witness fees). Brookfield does not use 120000 at all. |
| `130000` | Prepaid Professional Liability Insurance | Prepaid Malpractice Insurance | Prepaid Insurance | Each entity carries a prepaid-insurance account at 130000 with an entity-specific name. |
| `131000` | Prepaid Software Subscriptions | Prepaid Software Subscriptions | Prepaid Software & SaaS Subscriptions | All three entities; Acme's name is more SaaS-flavoured. |
| `132000` | Prepaid Facilities Maintenance | Prepaid Facilities Maintenance | Prepaid Facilities Maintenance & Janitorial | All three entities. |
| `133000` | **Prepaid CPE & Training** | **Prepaid CLE & Bar Dues** | *(not in CoA)* | **⚠️ Same number, two different professional-ed concepts.** Brookfield's CPE is Continuing Professional Education (for CPAs); Northstar's CLE is Continuing Legal Education + bar dues (for lawyers). Acme does not have a 133000 account. |
| `134000` | Prepaid Other Operating Expenses | Prepaid Other Operating Expenses | Prepaid Other Operating Expenses | Catch-all prepaid bucket, all three entities. |
| `135000` | Prepaid Marketing | Prepaid Marketing | Prepaid Marketing & Advertising | **v47 addition.** Prepaid asset for marketing campaigns that will deliver their benefit in future months. Cat 4.7 improper-request refusal anchors here — using this account to defer spend that has already burned through its benefit period is the matching-principle violation the firm has to refuse. |
| `150200` | Fixed Assets – IT (≥ $5K) | Fixed Assets – IT (≥ $5K) | Fixed Assets – IT (≥ $5K) | Consistent |
| `153000` | ROU Asset | ROU Asset | ROU Asset | ASC 842 lease accounting. *ROU = Right-of-Use — the asset side of a lease obligation under ASC 842, paired with a lease-liability account on `221000` / `222000`.* |
| `155000` | — | — | **Capitalized Software** | Acme-specific |
| `158xxx` | Accumulated Depreciation | Accumulated Depreciation | Accumulated Depreciation | Contra-asset block |
| `175500` | Accum. Amortization | *(not in CoA)* | Accum. Amortization | Contra-asset. **⚠️ Brookfield + Acme only — Northstar has no `175500` account.** |
| `210000` | AP – External Vendors | AP – External Vendors | AP – External Vendors | All entities |
| `219000` | AP – Employee Reimbursements | AP – Employee Reimbursements | AP – Employee Reimbursements | All entities |
| `220000` | Accrued Professional Services | Accrued Professional Services | Accrued Professional Services | All entities |
| `221000` / `222000` | Lease Liability | Lease Liability | Lease Liability | ASC 842 |
| `225000` | Accrued Salaries & Bonuses | Accrued Salaries & Bonuses | Accrued Salaries & Bonuses | All entities. ⚠️ scen_067 also books Acme's Q1 sales-tax **payable** here, since there's no dedicated Sales Tax Payable account — see the CoA gap note below. |
| `230000` | Income Tax Payable | Income Tax Payable | Income Tax Payable | All entities |
| `500000` | Direct Engagement Costs – Subcontracted | Direct Engagement Costs – Co-Counsel | Cost of Revenue – Cloud Infrastructure | **⚠️ Same number, three different concepts.** |
| `521000` | Tax Preparation Software | Document Management Software | Engineering Tools & Observability | **⚠️ Same number, three different concepts.** The Datadog reclass (`500000` → `521000`) in scen_028 is meaningful *only* on Acme — don't copy it to other entities. |
| `525000` | *(not in CoA)* | *(not in CoA)* | **Sales Tax Expense** | **⚠️ Acme only.** This is the debit side of Acme's sales-tax accrual (scen_067 posts $42,180.55 here). It is a *real* account — earlier guidance that "525000 doesn't exist" was wrong. Brookfield and Northstar have no equivalent (their professional-services revenue isn't sales-taxable). |
| `530000` | Professional Services – Legal | Court Filing | Professional Services – Legal | **⚠️ Different roles per entity.** |
| `535000` | Continuing Professional Education (CPE) | Continuing Legal Education (CLE) | *(not in CoA)* | **⚠️ Brookfield + Northstar only.** Professional-development expense paired with the prepaid account at `133000`. Acme has neither `133000` nor `535000` — engineering training, if booked at Acme, lands elsewhere on the CoA. |
| `570000` | Depreciation | Depreciation | Depreciation | All entities |

### ⚠️ Known CoA gap — Sales Tax Payable

**There is no dedicated Sales Tax *Payable* account in any entity's CoA.** The expense side exists — `525000` Sales Tax Expense is a real account on Acme and is the account scen_067 debits — but there is no purpose-built payable: scen_067 credits the payable to `225000` (otherwise Accrued Salaries & Bonuses). Before authoring any Category 3 sales-tax task, confirm the correct accrual (liability) + expense accounts against the entity's CoA rather than assuming a "Sales Tax Payable" line exists.

For the full account list including every account on each entity's CoA, see [`05_ARTIFACTS - BROOKFIELD UNIVERSE`](05_ARTIFACTS%20-%20BROOKFIELD%20UNIVERSE.html).

---

# How to write a strong task prompt

A good Brookfield task prompt has these properties:

- **Written in the natural style** of a real colleague handing off work — not a template, not a checklist preamble. Drop straight into the request. The attribution line (`*Prompt written by …*`) goes **outside** the prompt body.
- **Anchored to specific universe artifacts** — period IDs, account numbers, scenario IDs, vendor names, persona names, recon IDs. Confirm anchors against the live data before committing.
- **Multi-system.** A genuine Brookfield task touches at least 3 services — typically Oracle GL + BlackLine + Records Vault for accounting work, or SAP + Linear + Slack + email for operations work.
- **Respectful of the universe constants.** Retention codes from the canonical 4. Entity-prefixed IDs. The 300-second JE-transition rule. Closed-period posting needs `late_post_authorization_id`. AP threshold ladder by entity.
- **Followed by an attribution line** identifying the authoring persona and their role.

## Difficulty levers

- **More systems to read across.** Force the agent to pull from Oracle GL + BlackLine + SAP Subledger + Records Vault + Slack rather than from one or two.
- **Verification of every cited number.** If the prompt references a JE, expect the agent to confirm the JE exists in Oracle GL. If it references a reconciliation, expect a BlackLine pull. If it references a retention code, expect one of the canonical four — not `SOX_7Y`.
- **Multi-step chained dependencies.** Step 2 depends on Step 1's correct output; Step 5 depends on Step 4. A missed step breaks the chain.
- **Specific technical correctness.** Right account number for the right entity, right entity-prefixed period ID, right retention code, right `is_standard_entry` flag, the `late_post_authorization_id` requirement when posting to a closed period, the 5-minute minimum between JE state transitions.
- **Filter at volume.** Make the agent surface the relevant 5 records from a pool of 500.
- **Deadline-driven sequencing.** BD0 → BD1 → BD3 → BD5 means actions need to land in the right order. Quarter-end + IRS filing windows + the 5-business-days-before-deadline review SLA all constrain timing.
- **Verification chains.** "Confirm the AP approval ladder is intact below the partner tier" requires four separate verifications to land before the routing email.
- **Cross-entity context.** Mixing brookfield + northstar_legal + acme_cloud work in one task surfaces entity-specific differences (IOLTA on Northstar, ASC 606/340-40 on Acme, internal-books rules on Brookfield).
- **Red herrings in the data.** Unrelated anomalies the agent should ignore — the right answer requires identifying which signals matter and which don't.

When you're stuck on which scenario backs your category, refer to the **scenario → category mapping** table above.