## **New Universe: Keystone Mortgage Partners**

Opposite Classic  —  Replacing MoveOps Inc.

### **What Changed**

The in-task universe is moving from **MoveOps Inc.** (B2B travel/relocation) to **Keystone Mortgage Partners** (residential mortgage brokerage). The company has 30 employees, 8 wholesale lenders, 67 pre-built scenarios, and richer MCP server coverage. The domain introduces real regulatory complexity (TRID, fair lending, wire fraud) that creates natural difficulty without contrivance.

### **Key Numbers**

| Dimension | MoveOps (old) | Keystone (new) |
| :---- | :---- | :---- |
| Employees | 20–40 | 30 |
| Pre-built scenarios | Limited | 67 (21–67 artifacts each) |
| CRM records | Moderate | 500 contacts, 500 leads, 80 deals, 472 engagements |
| LOS (new) | N/A | \~700 borrowers, \~700 loans, conditions, doc checklists |
| Business functions | 5 | 6 (Loan Ops 30%, Compliance 20%, Sales 20%, Finance 15%, Executive 10%, IT 5%) |

**New MCP Servers**

* **mortgage\_los** — Central loan origination system. Borrower records, loan pipeline, underwriting conditions, document checklists, staff access list. The source of truth for every loan.  
* **Stripe** — Borrower fee collection (credit reports, appraisals, deposits), vendor payments via connected accounts, Financial Connections bank transaction data (\~40 borrowers), identity verifications (\~100 loans).  
* **filesystem** — Borrower document PDFs (tax returns, W-2s, bank statements, appraisals, closing disclosures), investigation reports, HR notes, QC audit files.

**Default vs. Non-Default Tools**

Same logic as MoveOps: 

* **Default** \= agent always uses these, skip TS.   
* **Non-default** \= agent might skip, write TS.

| Default (skip TS) | Non-Default (write TS) |
| ----- | :---- |
| Email: search\_emails, list\_emails, get\_email\_by\_id, get\_thread, etc. | mortgage\_los\_\*  |
| Slack: channels\_list, conversations\_history, conversations\_replies, conversations\_search\_messages | stripe\_\*  |
| Contacts: contacts\_search\_contacts, contacts\_get\_contacts, contacts\_get\_contact, etc. | crm\_\* |
| \- | filesystem\_\* |
| \- | quickbooks\_\* |

*Note: Write tools always go to Outcome rubrics (1.1/1.2), never TS or QC. This list is for read/lookup tools only.*

**What Stays the Same**

* **Rubric framework** — Outcome-first workflow, 3 categories (TS / QC / Outcome with 1.1, 1.2, 2.1), Process Rubric Decision Matrix, 50/50–80/20 outcome-to-process split.  
* **Prompt rules** — No tool names in prompts, no pre-solving, no command lists, no bolting, natural language, agent must fail on some rubrics.  
* **Difficulty targets** — Average 40+ tool calls, pass@1 ≤ 40% across 6 Opus 4.6 runs, 0% pass is acceptable.  
* **QC spec dimensions** — Unique ground truth, feasibility, tool dependence, cross-service requirement, coherence, persona match, business function, universe feasibility, OE completeness/accuracy, rubric quality thresholds, category balance, failure rate.  
* **Three fields per rubric** — Criterion \+ justification \+ evidence.

**What's Different for Task Design**

* **Domain knowledge matters.** TRID timing (LE within 3 biz days of app, CD at least 3 biz days before closing), fee tolerances, rate lock mechanics, and underwriting conditions create natural difficulty. Read the Universe Summary carefully.  
* **More non-default tools.** mortgage\_los, Stripe, and filesystem are all non-default. Agents will rely on email/Slack secondhand info instead of querying the LOS or reading actual PDFs. Your rubrics should test whether the agent went to the source.  
* **Richer write-action surface.** Beyond send\_email: mortgage\_los\_add\_activity, mortgage\_los\_add\_condition, stripe\_create\_charge, stripe\_create\_refund, filesystem\_write\_file, quickbooks\_create\_invoice, quickbooks\_create\_bill. **Diversify your write actions**.  
* **67 pre-built scenarios with artifact maps.** Each scenario lists which MCP servers have artifacts. Use the scenario-to-component matrix to find multi-service scenarios.  
* **Persona depth.** Persona briefs include open threads mapped to specific scenarios. Start from a persona's open threads to design tasks, not from scratch.

**Top Personas by Scenario Connectivity**

| Name | Title | Scenarios | Best For |
| :---- | :---- | :---- | :---- |
| **Denise Holloway** | Compliance Officer | 20+ | Fair lending, fraud, TRID, security incidents |
| **Grace Yamamoto** | Director of Ops | 18+ | Incident response, HR, performance, pipeline triage |
| **Elena Marchetti** | Senior Processor | 15+ | Condition clearing, loan-level ops, processing crises |
| **Carlos Rivera** | Loan Officer | 14+ | Borrower issues, rate locks, performance review |
| **Keisha Williams** | Loan Officer | 11+ | Fair lending, phishing, high-volume pipeline |
| **Sofia Reyes** | Processor | 9 | Wire fraud, lock crises, processor overload |

**Reference Documents**

* [**Keystone Mortgage Partners \- Universe Summary**](https://gist.github.com/sunjiehou-scale/7f779a9ae3b1d9e3f237992e97080f8f) — Universe bible: org chart, loan lifecycle, MCP server details, scenario catalogue, embedded anomalies.  
* [**Keystone Mortgage Partners \- Persona Briefs**](https://gist.github.com/sunjiehou-scale/8cb9f66c3e7d8cdd2c11de2b318ac68e) — All 30 employees with active work, relationships, open threads, and artifact footprints.  
* [**Mortgage Broker \- Scenario Storylines**](https://gist.github.com/sunjiehou-scale/552e0ce4729701bc3a717d30060f0858) — 70 storylines with required component artifacts and MCP server mapping.  
* [**Keystone Mortgage Partners \- Business Functions**](https://gist.github.com/sunjiehou-scale/62dfbc62abf024e11ec15bb98fd9a57b) — 6 business functions, 17 subcategories, read/write tool lists, artifact requirements, example prompts, write tool coverage matrix.

