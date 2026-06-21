# **Brookfield CPAs & Advisors — A New In-Task Universe**

## **The short version**

After Keystone Mortgage Partners, the next in-task universe is **Brookfield CPAs & Advisors** — a US public accounting and advisory firm, partner-led, headquartered in Chicago with about 140 employees. Brookfield handles three sets of books at once: its own (`brookfield`), a law-firm client (`northstar_legal`), and a B2B SaaS client (`acme_cloud`).

The universe leans hard into real accounting and regulatory machinery — US GAAP (the umbrella US accounting standards), the ASC standards (606 for deferred revenue, 340-40 for deferred commissions, 842 for leases, 740 for income tax), IRS deadlines, the AICPA's quality-management standard (SQMS 1), the US Bank Secrecy Act and FinCEN's anti-money-laundering rules, and a strict business-day (BD0–BD8) close calendar. That depth is where the difficulty comes from; nothing has to be contrived.

Today inside the universe is **2026-06-12 (US/Eastern)**.

## **By the numbers**

| Dimension | Keystone (old) | Brookfield (new) |
| :---- | :---- | :---- |
| Employees | 30 | ~140 (**34 authoring personas + 29 NPCs**, as of v47) |
| Client entities served | 1 (the firm itself) | 3 (Brookfield + Northstar Legal + Acme Cloud) |
| Pre-built scenarios | 67 | **52 merged** + 9 partial + 10 stage-1 checkpoint (71 YAMLs total) |
| Task categories | 6 business functions | **10 categories**, a mix of CPA-heavy and No-CPA-required |
| Tasking target | — | **300 training tasks + 100 benchmark tasks** |
| Total artifact volume | LOS-anchored, ~700 borrowers | **22,950 entries** across 12 services |

## **The systems Brookfield runs on**

Four of the twelve services do the heavy lifting — they're the firm's **state-of-record** systems, the place where the source of truth lives:

- **oracle_gl** is the main accounting platform. Every journal entry (JE), every fiscal period's state, and the BD0–BD8 close lock live here. About 2,933 entries (245 chart-of-accounts entries — v47 added `135000 Prepaid Marketing` on all three entities — 36 fiscal periods, 2,388 JEs, plus subledger feeds and runs). **v47 framing:** Oracle GL is consolidating the SAP Subledger into itself by an Oct 2026 cutover per the SAP→Oracle migration plan in Records Vault.
- **sap_subledger** is the detail layer behind the GL — accounts-payable (AP) invoices, fixed assets, prepaid amortization schedules, lease schedules, and a long tail of subledger transactions. About 4,060 entries (987 AP invoices, 240 fixed assets, 2,752 subledger transactions, and the rest). Being decommissioned by Oct 2026.
- **blackline** is the close-and-reconciliation workflow — 683 reconciliations, 24 exceptions, 396 close tasks, evidence, audit trail. About 6,800 entries. **One nuance worth knowing:** Excel is the *primary* reconciliation surface in this firm; BlackLine holds the Excel workbook as an attachment and tracks the preparer / reviewer / certifier chain around it.
- **records_vault** is where every document lives — workpapers, Management Accounts Packages (MAPs), engagement letters, AML files, control-test memos. About 4,554 entries (2,007 documents — v47 added 7: four `client_consent_letter` files for Acme/Northstar audit↔tax + audit↔accounting cross-team consent, two ERP-migration docs, one `tax_determination_memo` for Acme SaaS — 2,356 versions, 184 access grants), governed by 4 retention codes and 3 classification levels.

Two lighter specialized services round out the workflow layer:

- **airtable** for workflow management (2 bases, 5 tables, 21 records).
- **linear** for systemic-issue tracking (30 issues across 8 projects and 6 teams). The AP standardization project is the primary destination (`linear_63697b7dff5c`).

Around all of that sits the **coordination layer** — the comms tools you already know: email (1,379 messages), slack (2,545 messages across 11 channels), messaging (202 private conversations), calendar (51 events), reminder (53 SLA/deadline tickets), and contacts (63 records — v47 added 6 entries for the new personas).

## **What carries over**

This is the same project framework you've been working in, with the latest rubric conventions:

- **Rubrics (V3).** Two categories only: **Outcome** (mandatory — the default training signal) and **Process** (optional — only when a necessary behavior can't be captured by a stronger Outcome rubric). Outcome has three sub-types — **1.1** write-action results, **1.2** action content, **2.1** key facts in the final response. There's no fixed outcome-to-process ratio; default to making Outcomes stricter rather than reaching for Process.
- **Phrasing convention.** Every rubric reads as a behavior of *the Agent* — *"The Agent sends an email to chloe.vance@…"* rather than *"An email was sent to Chloe."*
- **Same prompt rules.** No pre-solving, no command lists, no bolting, natural language throughout, agent must fail on some rubrics.
- **Same difficulty targets.** Average 40+ tool calls, pass@1 ≤ 40% across 6 Opus runs, 0% pass is acceptable.
- **Same spec-quality dimensions we evaluate against:** unique ground truth, feasibility, cross-service requirement, coherence, persona match, business function, universe feasibility, OE completeness/accuracy, rubric quality thresholds, category balance, failure rate.
- **Same three fields per rubric:** criterion + justification + evidence.

## **What's new for task design**

A few things make this universe different from Keystone in ways worth knowing up front:

- **Accounting depth is real, but explained.** The BD0–BD8 close calendar, the JE lifecycle (`draft → submitted → approved → posted → reversed`, with a 300-second minimum between transitions and a `late_post_authorization_id` required for closed-period posting), ASC 606 deferred revenue, ASC 340-40 deferred commissions, ASC 842 right-of-use (ROU) leases, AML wire-flag thresholds, preparer/certifier independence — all of these create natural difficulty. The good news: [`03_TASK_CATEGORIES`](03_TASK_CATEGORIES%20-%20BROOKFIELD%20UNIVERSE.html) defines every concept inline, so a generalist can author from it without an accounting degree.
- **Categories are tagged for credentialing routing.** 🎓 **CPA-heavy** categories: Cat 1 (Close), 3 (Tax), 4 (Compliance & Internal Controls), 5 (Audit), 7 (BlackLine), 9 (Executive Oversight). 🛠 **No-CPA-required** categories: Cat 2 (Bookkeeping), 6 (AP / Vendor Operations), 8 (Engagement Mgmt), 10 (HR & People Ops). The tags route the tasking pipeline; the guide itself remains generalist-friendly.
- **Account numbers can mean different things on different entities.** `105000` is a generic client-trust account on Brookfield, the IOLTA (Interest On Lawyers Trust Account — the segregated client-funds account US lawyer-trust rules require) on Northstar, and short-term investments on Acme. `120000` exists only on Northstar (Client Cost Advances) and Acme (Deferred Commissions). `133000` is Prepaid CPE on Brookfield, Prepaid CLE on Northstar, and not in Acme's chart of accounts (CoA) at all. Always confirm the account against the entity's CoA before reusing.
- **Some fiscal periods are `open` past their lock target.** As of today, the three `FP-2026-05` periods are `status=open` with `locked_by=null` — the BD3 lock target passed on 2026-06-03 but no partner has actually locked. That's a plausible task setup, not a data bug.
- **Agents tend to skip the heavy state-of-record systems.** Oracle GL, SAP Subledger, BlackLine, Records Vault, Airtable, and Linear are where the truth lives — yet agents often fall back to email and Slack secondhand info instead of querying the GL, reading actual workpapers, or checking BlackLine state. Design tasks (and rubrics) that test whether the agent actually went to the source.
- **The write-action surface is much richer than just `send_email`.** You can have the agent post a journal entry through its full lifecycle, submit / approve / certify / archive a reconciliation, leave a BlackLine review note, upload a document with retention and classification metadata, flip an AP invoice's status (or void it with reason), update an Airtable record, or open and update Linear issues. Diversify your write actions across these.
- **The 52 pre-built scenarios are fully role-assigned.** Every scenario lists its anchor IDs (BL-…, JE-…, exc_…, VEN-…), entity, period, primary category, and which personas play which role — assignee, identifier, approver, reviewer, manager, partner, peer. The catalog lives in [`04_SCENARIO_STORYLINES`](04_SCENARIO_STORYLINES%20-%20BROOKFIELD%20UNIVERSE.html), told as short stories you can pick up directly.
- **Personas come with a Style.** Each persona brief now includes a `Style:` line describing how that person actually communicates — formal vs. approachable, verbose vs. terse, rigid vs. warm. Start from a persona's open threads to design tasks; lean on Style to write in their voice.
- **v47 added 6 new authoring seats** — Audit Staff (Mia Hartwell) + Audit Manager (Devon Beale) fill out the audit team; AP Coordinator (Priya Khatri) + AP Clerk (Tariq Soto) + Procurement Officer (Lena Park — a new `procurement` department, deliberately segregated from AP per segregation-of-duties) fill out AP / vendor; Billing Coordinator (Marcus Knell) fills out internal billing. **None are yet anchored in the 52 scripted scenarios**, but they're the natural acting voices for new Cat 5 / Cat 6 / Cat 8 task design. Author from spec when you reach for one of them.
- **Acme sales tax = TX / NY / WA / AZ** (not TX-only or TX/GA/NC). The v47 SaaS-taxability determination memo in Records Vault concludes those four states genuinely tax SaaS; the older nexus footprints (CA, FL, IL, MA, NV, GA, NC) are exempt or services-not-taxed. TX uses destination-based per-ZIP local rates after Acme crossed the $612K trailing-12 economic-nexus threshold. The Q1 2026 accrual posts as a single combined entry of $42,180.55 (account `525000`).

## **The personas you'll see most often**

These six anchor the largest share of scenarios. If you're stuck for a starting point, pick one of their open threads:

| Name | Title | Scenarios | Best for |
| :---- | :---- | ----: | :---- |
| **George McAdam** | Accounts Senior *(primary persona)* | 20 | Close execution, BlackLine triage, working-paper prep, FX revaluation |
| **Daniel Jones** | Accounts Manager | 25 | AP escalation triage, manager review, close coordination, AML soft-flag disposition |
| **Matthew Li** | Accounting Services Partner | 14 | Northstar engagement sign-off, audit + annual accounts, AP partner clearance |
| **Andrea Phil** | Partner, Accounting Services | 14 | Close kickoffs + MAP sign-off, OOS / change-order disposition, de-minimis AP partner |
| **Hannah Grant** | Corporate Tax Senior | 14 | Sales tax cycles, annual partnership returns, estimated tax projection, cross-discipline tax review |
| **Ryan Delgado** | Audit Senior | 10 | Audit kickoff + PBC tracking, orphan-exception identifier, FX rate snapshot, BO refresh approver |

## **Where to dig deeper**

The full doc set lives next to this one-pager. They're written to be read in any order, but the Summary is the friendliest place to land first:

- [**Summary**](01_SUMMARY%20-%20BROOKFIELD%20UNIVERSE.html) — The universe overview: firm, entities, systems, close calendar, account numbers, persona table. Start here.
- [**Persona Briefs**](02_PERSONA_BRIEFS%20-%20BROOKFIELD%20UNIVERSE.html) — All 34 personas with Style, active work, relationships, open threads, and artifact footprints.
- [**Task Categories**](03_TASK_CATEGORIES%20-%20BROOKFIELD%20UNIVERSE.html) — The 10 categories with subcategories, authoring checklists, CPA-heavy / No-CPA-required tags, and worked examples. Every concept is defined inline.
- [**Scenario Storylines**](04_SCENARIO_STORYLINES%20-%20BROOKFIELD%20UNIVERSE.html) — All 52 merged scenarios told as short stories, grouped into 8 workflow families.
- [**Artifacts Reference**](05_ARTIFACTS%20-%20BROOKFIELD%20UNIVERSE.html) — The dense reference: full personas + NPCs + system schemas + per-entity useful-accounts grid + complete scenario index.
- [**Glossary**](06_GLOSSARY%20-%20BROOKFIELD%20UNIVERSE.html) — Every accounting term and universe convention defined.