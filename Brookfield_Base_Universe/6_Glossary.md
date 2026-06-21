# Glossary — Brookfield CPAs & Advisors

Abbreviations, jargon, and conventions used across the doc set. Organized by theme. When a term has both a general accounting meaning *and* a Brookfield-universe-specific meaning, both are given.

---

## 1. US accounting standards & frameworks

| Term | Expansion | Meaning in this universe |
|------|-----------|---------------------------|
| **US GAAP** | Generally Accepted Accounting Principles | The accounting standard all three entities report under. Partner GAAP review is the final review step on annual accounts (Category 1.2 / 5). |
| **ASC** | Accounting Standards Codification | The FASB's organized body of US GAAP. Brookfield references four ASC topics often: |
| **ASC 606** | Revenue from Contracts with Customers | Revenue recognition standard. Drives Acme Cloud's deferred-revenue release JEs (close scenarios scen_027, 028). |
| **ASC 340-40** | Other Assets & Deferred Costs — Contracts with Customers | Deferred-commissions amortization for SaaS. Acme-specific (account `120000`). |
| **ASC 842** | Leases | Lease commencement + ROU asset + lease liability. Account `153000` ROU, `221000/222000` lease liability. |
| **ASC 740** | Income Taxes | Book-tax differences, deferred tax accounting. Used in Acme tax cycle (scen_046) and Northstar partnership return (scen_068). |
| **IFRS** | International Financial Reporting Standards | The non-US standard. Referenced in refusal-pattern prompts ("must follow IFRS/GAAP-compliant treatment"). Brookfield clients all report under US GAAP. |
| **FASB** | Financial Accounting Standards Board | US standard-setter behind ASC. Referenced indirectly. |
| **IRC** | Internal Revenue Code | The US federal tax code. Referenced in Category 3 governing standards. |
| **§179** | IRC Section 179 | Accelerated depreciation election — used in Northstar partnership return (scen_068). |
| **§6107** | IRC Section 6107 | Tax-preparer record-retention rule — basis of the `IRS_TAX_7Y` retention code. |
| **M-1** | Schedule M-1 | Book-to-tax reconciliation on corporate/partnership tax returns. |
| **K-1** | Schedule K-1 | Partnership allocations to partners. Relevant to Northstar's Form 1065. |
| **Form 1065** | US Return of Partnership Income | Northstar Legal's annual federal partnership tax return (scen_068). |
| **§179/bonus depreciation** | Accelerated depreciation rules | Referenced in book-tax difference identification. |
| **Allowance method** | Bad-debt accounting convention | Estimates uncollectibles via `117000` Allowance for Doubtful Accounts (contra-asset). Used in scen_056 Ridgepoint write-off. |
| **Matching principle** | GAAP accrual concept | Revenue and related expenses recognized in the same period. Foundational for close work (Category 1). |

---

## 2. Close calendar & workflow

| Term | Expansion | Meaning in this universe |
|------|-----------|---------------------------|
| **BD0** | Business Day 0 | Close kickoff — partner sets the plan. |
| **BD1** | Business Day 1 | Close-period entries posted: accruals, prepaid amortization, depreciation, ASC 606/340-40 for Acme. The 6 "June 1 BD1" JEs in this universe are FP-2026-05 BD1 postings. |
| **BD2** | Business Day 2 | Reviewer review window. |
| **BD3** | Business Day 3 | **Period lock target.** `bd3_lock_at` field is the *scheduled* lock timestamp, not a realized state. The May FP-2026-05 lock target was 2026-06-03 — but as of today (2026-06-12) the three FP-2026-05 periods are still `status=open`. After an actual lock (`status=locked`), any posting requires `late_post_authorization_id`. |
| **BD5** | Business Day 5 | **Period close.** `bd5_close_at` field. May FP-2026-05 close date is 2026-06-05. |
| **BD6–BD7** | Business Days 6–7 | MAP sign-off window. |
| **BD8** | Business Day 8 | Archival. BlackLine reconciliations move to `archived` state. |
| **MMA** | Monthly Management Accounts | The recurring monthly close deliverable. |
| **MAP** | Management Accounts Package | The packaged month-end deliverable (Records Vault `kind: management_accounts_package`). |
| **Close cadence** | The BD0→BD8 sequence | Universe-wide; some scenarios deviate by 1–2 BDs. |

---

## 3. Journal entry (JE) lifecycle & states

| Term | Meaning |
|------|---------|
| **JE** | Journal Entry. Stored in Oracle GL `journal_entries`. ID format: `JE-<entity>-FP-YYYY-MM-NNNN`. |
| **draft** | New JE in preparation, not yet submitted for review. |
| **submitted** | Sent for reviewer approval. |
| **approved** | Reviewer cleared; not yet posted to ledger. |
| **posted** | Hit the general ledger. Affects account balances. |
| **rejected** | Reviewer pushed back; preparer revises. |
| **reversed** | Counter-JE booked to undo a prior post. Original carries `reversed_by_entry_id`; counter carries `reverses_entry_id`. |
| **`is_standard_entry: true`** | Recurring entry (monthly accrual, depreciation, prepaid amortization). |
| **`is_standard_entry: false`** | Adjusting entry (variance correction, reclass, one-off). |
| **`entry_type: adjusting`** | Explicit adjusting JE flag. |
| **5-minute / 300-second rule** | Minimum elapsed time between any two JE lifecycle state transitions. |
| **`late_post_authorization_id`** | Required when posting to a closed period. Without it, closed-period posts will be rejected. |

---

## 4. Account types & ranges

| Term | Meaning |
|------|---------|
| **CoA** | Chart of Accounts. Each entity has its own CoA in Oracle GL. |
| **`1xxxxx`** | Asset accounts |
| **`2xxxxx`** | Liability accounts |
| **`3xxxxx`** | Equity accounts |
| **`4xxxxx`** | Revenue accounts |
| **`5xxxxx`** | Expense accounts |
| **`158xxx`** | Accumulated Depreciation (contra-asset) |
| **`117000`** | Allowance for Doubtful Accounts (contra-asset) |
| **`175500`** | Accumulated Amortization (contra-asset) — **Brookfield + Acme only; not on Northstar** |
| **AR** | Accounts Receivable (`110000`) |
| **AP** | Accounts Payable (`210000`) |
| **WIP** | Work in Process – Unbilled Services / Time (`119000`) — billable but unbilled engagement time. In this firm, WIP always means unbilled revenue, not manufacturing inventory. |
| **ROU asset** | Right-of-Use asset (`153000`) — ASC 842 lease accounting |
| **D&O** | Directors & Officers insurance — Acme has annual D&O scenarios (scen_051 prepaid setup) |
| **IOLTA** | Interest on Lawyers Trust Account — segregated client funds under lawyer-trust rules. The IOLTA *concept* is **Northstar-only** and sits on Northstar's `105000`. ⚠️ Account `105000` itself exists on all three entities with different meanings (Brookfield: Cash – Client Trust; Northstar: IOLTA trust; Acme: Short-term Investments). |
| **CPE** | Continuing Professional Education — required for CPAs (**Brookfield only**). `133000` Prepaid CPE & Training, `535000` CPE expense. Northstar uses `133000` for *CLE* (Continuing Legal Education) + bar dues; Acme doesn't have `133000`. |
| **CLE** | Continuing Legal Education — lawyer-side equivalent of CPE (**Northstar only**); shares `133000` with Brookfield's CPE under different naming. |
| **Prepaid Marketing (`135000`)** | v47 addition. Prepaid asset for marketing campaigns that will deliver their benefit in future months; on all three entities (`Prepaid Marketing & Advertising` on Acme). See full entry in section 16. |
| **SALT** | State And Local Tax — referenced in Northstar partnership return as a closed-period true-up |

> **⚠️ Known CoA gap:** there is no dedicated *Sales Tax Payable* account. The expense account `525000` Sales Tax Expense *does* exist on Acme (scen_067 debits it); the payable side lands on `225000` (otherwise Accrued Salaries & Bonuses). Confirm the correct accrual (liability) + expense accounts per entity before authoring Category 3 sales-tax tasks, rather than assuming a purpose-built payable.

---

## 5. Reconciliation lifecycle (Excel-primary, BlackLine workflow)

> **Where the work actually happens.** Excel is the primary reconciliation surface — the workbook pulls the GL balance, lists supporting items, computes variance, and holds the explanation. BlackLine is the workflow tracker + evidence store around it: it attaches the workbook, records `gl_balance` / `supporting_balance` / `variance`, captures preparer / reviewer / certifier signatures, and runs SLA reminders. In a firm without BlackLine the same recs live in a shared drive with the workflow tracked manually.

| Term | Meaning |
|------|---------|
| **BlackLine** | Third-party close & reconciliation workflow system; in this universe a state-of-record service holding 683 reconciliations. Holds the spreadsheet, not the calculation. |
| **Reconciliation ID prefix `BL-…`** | All reconciliations carry this prefix, e.g. `BL-2E691B2E18FA` |
| **Exception ID prefix `exc_…`** | All exceptions carry this prefix, e.g. `exc_151b0bee7e374e` |
| **open** | Reconciliation has been created but not started |
| **in_progress** | Preparer working on it |
| **submitted** | Submitted to reviewer |
| **approved** | Reviewer cleared |
| **certified** | Senior/manager certified |
| **archived** | Period closed; reconciliation moved to archive |
| **overdue** | Past `sla_due_at`, not yet submitted |
| **Variance threshold policy** | `gl_balance − supporting_balance > variance_threshold` ⇒ exception logged |
| **Variance materiality** | Under $10 immaterial; $10–$1,000 should be addressed (may roll to next-month JE); over $1,000 urgent |
| **`sla_due_at`** | SLA timer for the reconciliation; firing past this triggers a tickler reminder |
| **Polling-bug pattern** | Universe-specific bug: stale SLA reminders re-fire on already-closed exceptions. The canonical example is scen_001 (`exc_151b0bee7e374e`). The fix is dismissal with documented audit trail (Category 7.1), not reopening. |

### Exception types (6 in the universe)

| Type | What it means |
|------|---------------|
| `duplicate_entry_detected` | Same transaction posted twice |
| `unrecorded_invoice` | Invoice known to exist but not in the subledger |
| `timing_difference_over_sla` | Items in transit at period close exceed SLA |
| `fx_revaluation_drift` | FX-denominated balances diverge from period-end rate revaluation |
| `subledger_feed_drop` | Nightly feed run failed or skipped records |
| `missing_accrual_variance` | Expected accrual not posted |

### Exception states (4)

`logged → investigating → awaiting_approval → closed`

---

## 6. SAP Subledger (AP) lifecycle

| Term | Meaning |
|------|---------|
| **AP invoice** | Accounts Payable invoice record in SAP Subledger. ID prefix `apinv_…`; vendor invoice number format `VEN-NNN-NNNNNN`. |
| **pending_approval** | New invoice received, awaiting threshold-tier approver |
| **approved** | Approver signed; ready to pay |
| **paid** | Disbursement recorded |
| **voided** | Cancelled/rejected (carries `void_reason`) |
| **Three-way match** | Invoice ↔ purchase order ↔ goods receipt verification |
| **PO** | Purchase Order — approved by cost-center owner before goods/services are ordered |
| **Blanket PO** | PO with a single approved cap amount for long-term/indeterminate-hours contracts. Supporting documentation (time cards) replaces line-item matching. SOWs are often attached. |
| **SOW** | Statement of Work — referenced in AP escalation scenarios when invoice amounts don't match contract |
| **IR engagement** | Incident Response engagement (CrownPeak Cyber Defense). Referenced as "IR engagement scope letter" in scen_034, 036. |
| **Credit memo** | Vendor-issued credit for over-billing or returns; missing credit memos are a common AP-escalation trigger |
| **AP approval ladder** | Clerk codes all; AP manager ≤ $10K; Controller ≤ $50K; **Managing Partner > $50K** — by entity: Steven Perry (Brookfield/Acme), Matthew Li (Northstar), Andrea Phil (de-minimis) |

---

## 7. Compliance & Internal Controls

| Term | Expansion | Meaning |
|------|-----------|---------|
| **AML** | Anti-Money Laundering | Compliance regime governing client onboarding and ongoing monitoring. Categories 4.1 (wire-flag), 4.2 (soft-flag triage), 4.3 (BO refresh) |
| **BSA** | Bank Secrecy Act | US AML statute |
| **FinCEN** | Financial Crimes Enforcement Network | US Treasury bureau enforcing BSA/AML |
| **CDD** | Customer Due Diligence | The FinCEN rule requiring identity verification + risk rating of clients |
| **BOI** | Beneficial Ownership Information | The information collected on persons with > 25% ownership / control. Acme BO refresh (scen_061) anchors this in the universe |
| **BO** | Beneficial Owner | Any person with > 25% ownership / significant control |
| **SAR** | Suspicious Activity Report | Filed with FinCEN when activity meets reporting threshold (no SAR-filing scenario in the current universe, but the concept underlies AML escalation) |
| **GDPR** | General Data Protection Regulation | EU privacy law; referenced as the model for the firm's privacy posture |
| **Data Protection Act 2018** | UK privacy statute | Cited in compliance exposure (up to 4% turnover penalty) |
| **PII** | Personally Identifiable Information | What AML and privacy regimes protect |
| **AICPA** | American Institute of Certified Public Accountants | US CPA profession's governing body |
| **AICPA SQMS 1** | Statement on Quality Management Standards #1 | The professional-standards basis of the `AICPA_SQMS_7Y` retention code |
| **Code of Professional Conduct §1.700** | AICPA confidentiality rule | Governs client confidentiality and data handling |
| **EEOC** | Equal Employment Opportunity Commission | US workplace-rights regulator; counterparty NPC James O'Brien |

### Records Vault retention codes (4)

| Code | Years | Use |
|------|-------|-----|
| `AICPA_SQMS_7Y` | 7 | **Default.** Tax workpapers, audit support, reconciliation evidence |
| `IRS_TAX_7Y` | 7 | Tax-preparer records and supporting work files (IRC §6107) |
| `FIRM_INTERNAL` | 5 | Engagement letters, client master files, operational records |
| `INDEFINITE` | — | Partnership agreements, statutory records, legal-hold-only documents |

**Do not use** `SOX_7Y`, `SEC_PERMANENT`, or any other code outside this list — they don't exist.

### Records Vault classifications (3)

| Code | Elevated role required | Use |
|------|:---------------------:|-----|
| `public` | no | Publicly available. **⚠️ Defined in schema but currently unused — 0 documents in the universe carry this classification.** Don't author prompts that produce `public` artifacts unless deliberately introducing the first one. |
| `internal` | no | Internal company use only (default — ~1,975 of 2,007 documents in v47). |
| `restricted` | **yes** | VP-level or above; AML disposition memos, executive comp, audit folders, partner-only memos, client-consent letters (32 documents). |

---

## 8. Audit terminology

| Term | Expansion | Meaning |
|------|-----------|---------|
| **PBC** | Prepared By Client | The list of items the audit team requests from the client/Brookfield to support fieldwork. Tracked as a closure-percentage in audit engagement scenarios. |
| **PBC closure %** | PBC completion ratio | Risk-pull threshold: < 80% by milestone is a concern |
| **Engagement letter** | Signed contract scoping an engagement | Records Vault `kind: engagement_letter`; retention `FIRM_INTERNAL` |
| **Engagement letter addendum** | Mid-cycle scope amendment | Records Vault `kind: engagement_letter_addendum`; signed at change-order completion (scen_065) |
| **Workpaper** | Audit working paper supporting an audit conclusion | Records Vault `kind: workpaper`; retention `AICPA_SQMS_7Y` |
| **Audit evidence** | Supporting documents underlying audit conclusions | Records Vault `kind: audit_evidence` |
| **Trial balance** | All-account balance listing as of period end | Pulled by audit team during fieldwork |
| **Walkthrough** | Process documentation tracing a transaction end-to-end | Standard audit fieldwork procedure |
| **Preparer/reviewer/certifier independence** | Same person cannot prepare and approve a reconciliation | Tested quarterly in scen_042 partner sign-off control test |

---

## 9. Engagement management terminology

| Term | Meaning |
|------|---------|
| **OOS** | Out Of Scope — work that exceeds the engagement-letter scope/budget. Triggers fee-impact judgment + partner disposition (scen_064 → scen_065 chain) |
| **Change order** | Formal scope-expansion package amending the engagement letter (scen_065) |
| **`ENG-BUDGET-<entity>-FY<YEAR>-Q<N>`** | Engagement budget annotation queue ID in Airtable, e.g. `ENG-BUDGET-acme_cloud-FY2026-Q1` |
| **Absorb vs change-order disposition** | Partner decision: does the firm eat the over-budget cost (absorb) or formally amend the engagement letter to bill the client (change order)? |
| **De-minimis release** | Partner-level authority to release a small or low-risk item without full escalation (Andrea Phil exercises this on Brookfield-side AP) |

---

## 10. Universe systems

| System | Role | Backing data |
|--------|------|--------------|
| **Oracle GL** | Main accounting platform: accounts, fiscal periods, JEs, subledger feeds | `services/oracle_gl/data.json` |
| **SAP Subledger** | Transaction-level detail: AP invoices, fixed assets, prepaid + lease schedules | `services/sap_subledger/data.json` |
| **BlackLine** | Close & reconciliation workflow | `services/blackline/data.json` |
| **Records Vault** | Document repository (working papers, contracts, returns, schedules) | `services/records_vault/data.json` |
| **Airtable** | Portfolio & workflow management | `services/airtable/data.json` |
| **Linear** | Work tracking — used for systemic issues, not routine close | `services/linear/data.json` |
| **MCP** | Model Context Protocol — the interface layer agents use to call these systems | n/a (interface, not data) |

---

## 11. Universe conventions & ID formats

| Convention | Example | Meaning |
|------------|---------|---------|
| **Entity slug** | `brookfield`, `northstar_legal`, `acme_cloud` | The three entities. Always lowercase + underscore. |
| **Fiscal period ID** | `brookfield_FP-2026-04` | `<entity>_FP-YYYY-MM`. Bare `FP-2026-04` will fail. |
| **JE ID** | `JE-acme_cloud-FP-2026-05-0012` | `JE-<entity>-FP-YYYY-MM-NNNN` |
| **BlackLine recon ID** | `BL-2E691B2E18FA` | `BL-` + 12 hex chars |
| **Exception ID** | `exc_151b0bee7e374e` | `exc_` + 14 hex chars |
| **AP invoice ID** | `apinv_5d1655afd49a4917` | `apinv_` + 16 hex chars |
| **Vendor invoice number** | `VEN-010-514242` | `VEN-NNN-NNNNNN` |
| **Document version ID** | `dv_584a5dabeb214c` | `dv_` + 14 hex chars |
| **Scenario ID** | `scen_023_monthly_close` | `scen_NNN_<family>` |

---

## 12. Currency & geography

| Term | Meaning |
|------|---------|
| **FX** | Foreign Exchange — month-end revaluation of non-USD balances |
| **USD** | United States Dollar — base currency for all entities |
| **EUR** | Euro — referenced in Northstar FX rounding scenarios (scen_039) |
| **GBP** | British Pound — referenced in Acme Research line FX variance (scen_040) |
| **Acme multi-state nexus** | TX (Texas), NY (New York), WA (Washington), AZ (Arizona) — the four states where Acme Cloud's SaaS is taxable per the v47 determination memo. The older TX/GA/NC framing is superseded; GA/NC/CA/FL/IL/MA/NV are exempt or services-not-taxed. |
| **Brookfield state annual reports** | NY (New York), NJ (New Jersey), DE (Delaware) — Brookfield itself files annual reports in these (scen_048 catch-up) |

---

## 13. Universe coverage & meta terms

| Term | Meaning |
|------|---------|
| **L1 — Noise themes** | Background slack/email/messaging chatter simulating ongoing conversation about a workflow |
| **L2 — Baseline accounting state** | Routine recurring artifacts: CoA, fiscal periods, recurring close JEs, baseline AP invoices, baseline reconciliations |
| **L3 — Scripted scenarios** | Specific named, traceable workflow instances with full beat structure |
| **Study scenario** | An existing scenario yaml to open as a reference template when authoring tasks in a category |
| **Anchor scenario** | The single scenario most representative of a category's pattern |
| **scenario_start** | The "as of" timestamp inside each scenario yaml. Uniformly `2026-05-31T09:00:00Z` in the present set. Not the same as universe "today" (`2026-06-12`). |
| **Mode A / Mode B** | Scenario generation modes. Mode B is "comm-only setup" (no new state-of-record artifacts; agent walks into pre-existing communications). |
| **Stage-2 pathology** | A known LLM-pathology in scenario generation where non-slack artifact beats (email/airtable/calendar) get miscoerced into `DraftSlackArtifact`. Hit by the 9 partial + 10 stage-1 checkpoint yamls (19 mid-generation files in the scenarios dir; only the 52 merged are usable anchors). |

---

## 14. Task authoring conventions

| Term | Meaning |
|------|---------|
| **Acting seat** | The persona authoring (i.e., voicing) the task prompt. All 34 generated personas — HR personas included — are eligible acting seats. HR has a smaller scenario footprint than the accounting/tax/audit teams; that's a volume difference, not an eligibility rule. **NPCs are never acting seats.** v47 added 6 new personas (Audit Staff + Audit Manager, AP Coordinator + AP Clerk, Procurement Officer, Billing Coordinator) that aren't yet anchored in any of the 52 scripted scenarios. |
| **Participant / counterparty** | Persona or NPC named in the task but not the acting voice — may receive emails, be DM'd, sign off, etc. External NPCs, HR personas, and internal background NPCs are *always* participants, never acting seats. |
| **Author tasks in** | Per the persona → category mapping in `03_TASK_CATEGORIES` §"Persona → Category mapping", the list of categories (1–10) a given persona can act in. |
| **Natural style** | Prompt-writing convention: no "I'm X, my role is Y" framing — start with the request as a real colleague would; attribution line (`*Prompt written by …*`) goes *outside* the prompt body. |
| **Refusal pattern** | When the agent must reject a GAAP-improper or policy-violating client request rather than comply. No scripted scenario; build from the Authoring Guide Category 4.7 example. |
| **Long-horizon task** | A task that spans many systems and beats — the design target for Category 10 and many Category 9 tasks. |

---

## 15. Roles & seniority

| Level | In this universe |
|-------|------------------|
| **Trainee Accountant** | Junior bench (drafts, prepares); Green Spatz, Anaya Wallace, Elita Moore |
| **Accounts Associate** | Mid-level (owns prep, light review); Harry Marks, Emily Adekole, Blue Evans |
| **Accounts Senior** | Working file owner (preparer, peer reviewer, identifier); George McAdam *(primary)*, Edith Banda, Jones Harrison |
| **Accounts Manager** | Reviewer + escalation triage; Daniel Jones |
| **Partner** | Sign-off + clearance authority; Andrea Phil, Matthew Li, Ming Chang, Julia Vance, Steven Perry |
| **Managing Partner** | Top of firm; Steven Perry |
| **Tax Partner / Audit Partner / Accounting Services Partner** | Discipline-specific partner roles |
| **Compliance Officer / Head of Compliance** | Compliance discipline track; Marina Soko, Peter Sanchez |
| **Audit Staff** | Junior audit role — tick-and-tie, detail testing, fieldwork support; **Mia Hartwell** *(v47)* |
| **Audit Manager** | Audit engagement planning, in-charge review, partner-memo prep; bridge between staff fieldwork and partner sign-off; **Devon Beale** *(v47)* |
| **AP Specialist** | Owen Mercer (NPC) — anchor of the AP escalation family as participant; surfaces aged invoices in the queue |
| **AP Coordinator** | Persona-level AP triage seat — invoice intake routing, vendor-master accuracy, weekly AP exceptions triage; the natural canonical voice for new Cat 6.1 escalations; **Priya Khatri** *(v47)* |
| **AP Clerk** | Junior AP role — invoice data entry, three-way-match verification, routes exceptions up to the AP Coordinator; **Tariq Soto** *(v47)* |
| **Procurement Officer** | Owns PO issuance, vendor onboarding diligence, and SOW lifecycle. **Deliberately separated from AP per segregation-of-duties controls.** Brookfield's `procurement` department is a one-person function in v47; **Lena Park** *(v47)* |
| **Billing Coordinator** | Internal billing function — converts approved time and WIP into client invoices, manages billing terms by engagement, coordinates revenue-recognition timing with Accounting Services; **Marcus Knell** *(v47)* |

---

## 16. Other terms appearing in the doc set

| Term | Meaning |
|------|---------|
| **CFO** | Chief Financial Officer (client-side) |
| **CEO** | Chief Executive Officer (client-side) |
| **LLP** | Limited Liability Partnership — Northstar Legal LLP |
| **SaaS** | Software as a Service — Acme Cloud's business model |
| **B2B** | Business to Business — Acme Cloud's market |
| **R&D** | Research & Development — Acme R&D accrual JE in close scenarios |
| **HR** | Human Resources — full acting seat for Category 10 (HR & People Operations) per [`03_TASK_CATEGORIES`](03_TASK_CATEGORIES%20-%20BROOKFIELD%20UNIVERSE.html). HR has a smaller scripted-scenario footprint than the accounting/tax/audit teams; that's a volume difference, not an eligibility rule. |
| **HRIS** | Human Resources Information System — Brookfield does not have one. HR tasks anchor on Records Vault (HR folder under `FIRM_INTERNAL`), Airtable, calendar, and email rather than a dedicated HRIS. |
| **IT** | Information Technology |
| **DM** | Direct Message (Slack or messaging service) |
| **NPC** | Non-Player Character — external counterpart in the universe (regulator, vendor, client-side) or internal background admin/bench staff. **NPCs never author tasks**; they appear as participants or are coordinated *with*. The 29 NPCs are catalogued in [`05_ARTIFACTS`](05_ARTIFACTS%20-%20BROOKFIELD%20UNIVERSE.html). |
| **KPI** | Key Performance Indicator |
| **CoA gap** | Universe-specific term for known chart-of-accounts inconsistency (most prominently, the missing Sales Tax Payable account) |
| **scen_NNN** | Scenario yaml filename pattern, e.g. scen_023, scen_062 |
| **Yaml** | YAML — the file format used for scenario specifications |
| **client_consent_letter** | Records Vault document kind. AICPA standards require a written client-consent letter on file before the firm's audit team can pull workpapers or context from the firm's tax or accounting-services teams on the same client engagement. v47 added the four FY2026 letters covering Acme×2 + Northstar×2 (Audit↔Tax + Audit↔Accounting on each), all classification `restricted`. |
| **tax_determination_memo** | Records Vault document kind. The Acme SaaS multi-state sales-tax determination memo (v47, uploaded by Hannah Grant, retention `IRS_TAX_7Y`, `internal`) is the authoritative anchor for the TX/NY/WA/AZ taxable-states position. |
| **SAP→Oracle migration** | v47 framing — Brookfield is mid-migration from SAP Subledger to Oracle GL, with a target Oct 2026 cutover. Two Records Vault docs anchor this: `internal_strategy` Migration Plan FY2025-2026 + `internal_status_update` Q2 2026 Decommission Status. |
| **TX nexus threshold (SaaS)** | Acme crossed **$612K** in trailing-12 Texas sales, triggering TX economic nexus on its SaaS product. That flips TX to destination-based per-ZIP local tax rates instead of a single blended state rate. Referenced in scen_067. |
| **Prepaid Marketing** | Account `135000` (v47 addition, all three entities; "& Advertising" on Acme). Prepaid asset for marketing campaigns that will deliver their benefit in future months. The legitimate counterpart to the Cat 4.7 improper-request example, where mis-using this account to defer a *finished* campaign is the matching-principle violation. |
| **procurement (department)** | New department in v47; one persona (Lena Park, Procurement Officer). Deliberately segregated from AP per segregation-of-duties controls. |

---

## How this glossary is used

Open this doc alongside the other refs when writing a task and you hit an unfamiliar term. Cross-references:

- For **task categories 1–10** and the persona ↔ category mapping, see [`03_TASK_CATEGORIES`](03_TASK_CATEGORIES%20-%20BROOKFIELD%20UNIVERSE.html).
- For the **universe constants** ("today", FYE, totals), see [`01_SUMMARY`](01_SUMMARY%20-%20BROOKFIELD%20UNIVERSE.html).
- For **per-persona scenario footprints** and "Author tasks in" mapping, see [`02_PERSONA_BRIEFS`](02_PERSONA_BRIEFS%20-%20BROOKFIELD%20UNIVERSE.html).
- For **all 52 scenarios with full role assignments**, see [`04_SCENARIO_STORYLINES`](04_SCENARIO_STORYLINES%20-%20BROOKFIELD%20UNIVERSE.html).
- For **schemas, useful accounts, scenario index, NPC roster, persona ↔ scenario matrix**, see [`05_ARTIFACTS`](05_ARTIFACTS%20-%20BROOKFIELD%20UNIVERSE.html).