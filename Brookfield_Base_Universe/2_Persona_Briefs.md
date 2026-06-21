# Persona Briefs — Brookfield CPAs & Advisors

This document profiles the **34 generated personas** at Brookfield CPAs & Advisors — the people eligible to be the **acting voice** on a task prompt. Each brief tells you what the person actually does, who they lean on, and the situations sitting in their inbox or workpaper queue that a task author can pick up and run with. **v47 note:** six new personas landed in this universe — Mia Hartwell (Audit Staff), Devon Beale (Audit Manager), Priya Khatri (AP Coordinator), Tariq Soto (AP Clerk), Lena Park (Procurement Officer, a new `procurement` department), and Marcus Knell (Billing Coordinator). They're full eligible authoring seats but don't yet appear in any of the 52 scripted scenarios; their "Open threads" sections describe where they naturally fit in new task design.

## How to use these briefs

For each persona you'll see six sections, in this order:

1. **Author tasks in:** which task categories (numbered 1–10) the persona can be the acting voice for. The legend below decodes the numbers.
2. **Style:** the persona's communication baseline — how formal, how verbose, how rigid, how warm. Use this as a quick guide when you write a prompt in their voice: a Tax Partner won't sound like a Trainee, and a Compliance Officer won't sound like a Bookkeeper. The descriptions come from the universe's communication profiles, so the way the persona talks across emails, Slack, and review notes should match what's here.
3. **Active work:** a few sentences of plain English about what this person does day-to-day.
4. **Key relationships:** the internal colleagues this person works with most closely, plus any named external counterparts (NPCs) who show up in their workflow.
5. **Open threads:** the scenarios from the 52-yaml set where this persona has a named role. Each thread is written as a short paragraph describing what's actually happening — the scenario IDs (e.g., `scen_001`) and anchors (BL-…, JE-…, exc_…) stay woven in so you can find the underlying data.
6. **Recent activity:** the typical artifact footprint you'd see if you opened this persona's recent history — the kinds of emails, Slack threads, JEs, and Records Vault documents that should look familiar for them.

### Category numbers — quick decoder

When a persona's "Author tasks in" row reads, say, "1, 5, 6, 8, 9", the numbers map to these categories from [`03_TASK_CATEGORIES`](03_TASK_CATEGORIES%20-%20BROOKFIELD%20UNIVERSE.html):

| # | Category | What it covers |
|---|----------|----------------|
| 1 | **Accounting Operations** | Monthly close execution, annual accounts, quarterly reporting, WIP recognition, working-paper review |
| 2 | **Bookkeeping** | Daily coding, bank-feed triage, transaction-context pulls for AML, AP accrual history |
| 3 | **Tax** | Quarterly sales tax, annual returns (Form 1065 partnership + corporate), estimated payments, tax planning workshops, IRS liaison |
| 4 | **Compliance & Internal Controls** | AML wire-flag review, BO adverse-media triage, annual BO refresh, quarterly partner sign-off control test (preparer/certifier independence), document retention sweep, state annual reports, improper-request refusal |
| 5 | **Audit** | Audit engagement kickoff, PBC tracking, workpaper review and partner sign-off |
| 6 | **AP / Vendor Operations** | Aged AP invoice escalation, AP workflow standardization (Linear-tracked), AP threshold approval chain |
| 7 | **BlackLine Close-Discipline & Variance** | Stale-SLA reminder dismissal, live exception triage, reconciliation variance triage, FX variance review, month-end FX revaluation |
| 8 | **Engagement Mgmt & Client Operations** | OOS reviews + change orders, quarterly AR aging, new-client onboarding, vendor/system coordination |
| 9 | **Executive / Partner Oversight** | AP > $50K approvals, cross-functional risk pulls, quarterly control-test clearance, escalation routing & refusal |
| 10 | **HR & People Operations** | Onboarding & access provisioning, appraisal cycle, EEOC disputes |

### Universe constants for prompt design

- **Today** = `2026-06-12 US/Eastern`
- **Email domain** for all personas and NPCs: `brookfieldcpas.com`
- **HR personas (Brent Noah, Clint Peterson, Rachel Green, Reshma Patel) can author Category 10 tasks** per the latest 03_TASK_CATEGORIES framing. They are full personas — not "non-acting" — and step into onboarding, appraisal-cycle, and EEOC-dispute work when those scenarios run.
- **NPCs are not personas.** External counterparts (regulators, vendors, client-side staff) and internal background NPCs — Owen Mercer, Brenda Abbas, James Randall, Lucia Ferreira, Margot Reyes, Anaya Patel, Mateo Kovac, Nia Okafor, Yusuf Demir, Sofia Halabi, Farah Dlamini, Linda Burns, Anita Knowles, Priya Singh, Margaret Sullivan, and the rest — appear in scenarios as named participants but **never as the acting voice** on a task. The full NPC roster lives in [`05_ARTIFACTS`](05_ARTIFACTS%20-%20BROOKFIELD%20UNIVERSE.html).
- For accounting abbreviations (JE, GL, AP, AR, WIP, MAP, MMA, AML, BO, FX, PBC, OOS, IOLTA, CPE, ASC 606/340-40/842/740, SLA), see [`06_GLOSSARY`](06_GLOSSARY%20-%20BROOKFIELD%20UNIVERSE.html) or the quick legend in [`01_SUMMARY`](01_SUMMARY%20-%20BROOKFIELD%20UNIVERSE.html) under "Reading this summary".

---

## Partners

### Steven Perry — Managing Partner

**Author tasks in:** 6, 9, 10

**Style:** Extremely formal, executive, and controlled. He communicates briefly but decisively, usually emphasizing firm standards, risk, commercial judgment, and final accountability.

**Active work:** Steven is the firm's final clearance authority. He's the partner who signs off on AP items over $50K for Brookfield and Acme (Matthew Li covers the same threshold on Northstar), who provides final partner-level clearance on AML wire-flag reviews, and who closes out the quarterly compliance control tests. Peter Sanchez (head of compliance) and Brent Noah (people and culture) report directly to him.

**Key relationships:** His partner peers are Andrea Phil, Matthew Li, Ming Chang, and Julia Vance. Peter Sanchez and Brent Noah are his direct reports. Outside the firm, he occasionally interacts with James O'Brien at the EEOC when conciliation matters reach his desk.

**Open threads:** Six scenarios sit on Steven's desk. Three are aged Acme AP escalations needing managing-partner clearance: scen_029 (a TimeLedger Nexus invoice — `VEN-010-514242` — well past the 60-day SLA with a disputed Phase-3 deliverable and a missing credit memo), scen_031 (GraniteRack Compute on a superseded SOW, also well past SLA), and scen_032 (a second TimeLedger Nexus item, `VEN-010-693199`, where the vendor master detail doesn't match the invoice). On the compliance side, he holds final clearance on scen_041 — the Acme AML wire-flag review on `JE-acme_cloud-FP-2026-04-0052`, a $57,077.69 payment from Acme's largest enterprise SaaS customer that tripped the firm's standing $10K FinCEN wire-monitoring rule. He also signs off on scen_042, the quarterly partner sign-off control test that proves preparer/certifier independence, and scen_044, the quarterly document retention control sweep.

**Recent activity:** Partner-clearance emails on AP > $50K items, AML disposition sign-offs sitting in Records Vault, quarterly control-test approval emails, and the occasional firm-state risk pull.

---

### Matthew Li — Accounting Services Partner

**Author tasks in:** 1, 5, 6, 8, 9

**Style:** Highly formal, calm, and commercially aware. He communicates in a polished partner style—measured, concise, and oriented toward decisions, quality, and client trust.

**Active work:** Matthew is the engagement-side partner on Northstar Legal. He signs engagement-letter addendums, takes the partner tier of AP escalations on his entity, approves change orders, and reviews BO refresh proposals. Andrea Phil reports to him.

**Key relationships:** Steven Perry above him as managing partner; Andrea Phil reports to him; Daniel Jones and Edith Banda sit one layer below in the operating chain. He works closely with Ryan Delgado on audit work and Marina Soko on the compliance side.

**Open threads:** Fourteen scenarios run through Matthew. He's the partner who signs off the audit-trail recap on a recurring cluster of stale-SLA dismissals — scen_001 is the canonical example, with scen_006, scen_013, scen_015, and scen_021 echoing the pattern across different periods and entities. On the Northstar close, he certifies April's management accounts package (scen_025) and signs off the Q1 partner package (scen_058) that Edith prepares. Three of the eight AP escalations are his to disposition — scen_033, scen_034, and scen_036, all CrownPeak Cyber Defense invoices for Northstar, with the third in the series eventually revealing itself as a stale August 2025 cancellation. He's the engagement partner on the Acme AML wire-flag review (scen_041), chairs the Northstar partnership-distribution tax planning workshop alongside William and Tom (scen_047), reviews the Acme FY2026 BO refresh (scen_061), and countersigns the engagement-letter addendum on the Acme change-order package (scen_065). He also gives the partner sign-off on Northstar's FY2025 annual accounts (scen_063).

**Recent activity:** Records Vault sign-off documents on Northstar Q1, the Acme change order, and the CrownPeak AP escalations. Partner-routed approval emails. Calendar holds for engagement reviews and audit sign-off windows.

---

### Ming Chang — Tax Partner

**Author tasks in:** 3, 9

**Style:** Very formal, succinct, and technically authoritative. He communicates with partner-level precision, usually keeping messages short while signaling strong command of tax risk and filing judgment.

**Active work:** Ming heads the tax line. His name is the final approval on multi-state sales tax cycles and Q1 estimated tax. Alex Cahoon reports to him.

**Key relationships:** Alex Cahoon directly below him; Hannah Grant, William White, and Tom Chang round out the tax team. Externally, he liaises with Priya Singh at the IRS.

**Open threads:** Two scenarios. He approves scen_045, the Brookfield April multi-state sales tax cycle, where he's the one who directs the resolution on a Pennsylvania threshold question. And he approves scen_046, Acme's Q1 estimated tax projection.

**Recent activity:** Tax-partner approval emails, Records Vault sign-offs, and appearances in `#tax-prep-and-filings` when the team needs his read on a state filing call.

---

### Andrea Phil — Partner, Accounting Services

**Author tasks in:** 1, 5, 6, 8, 9

**Style:** Very formal, polished, and commercially minded. She communicates with partner-level authority—measured, concise, and focused on decisions, risk, and client confidence.

**Active work:** Andrea runs accounting services day-to-day. She kicks off BD0 close cycles, gives final sign-off on management accounts packages, owns the difficult engagement-budget conversations on Acme, makes the absorb-vs-change-order call when out-of-scope work surfaces, and holds de-minimis AP partner authority. She reports to Matthew Li.

**Key relationships:** Matthew Li above her; Daniel Jones is her main manager; George McAdam, Edith Banda, and Jones Harrison are the seniors she leans on. Externally she works regularly with Margaret Sullivan (Controller on the client side for close threads), John Bartlett (CEO at Southgate Interiors), and Amira Siddiqui (Banking Relationship Manager).

**Open threads:** Fourteen scenarios run through Andrea. She certifies four monthly close packages: scen_023 (Brookfield April), scen_024 (Brookfield May, with a deductibility question on a meals/entertainment line that George quantifies in a clarifying memo), scen_027 (Acme April), and scen_028 (Acme May with the Datadog reclass from account 500000 to 521000). She's the orphan-exception partner of record on scen_011 (Brookfield deferred-revenue context), scen_018 (Acme accrued-comp FX revaluation drift), scen_020 (the urgent SLA-breached duplicate-entry on account 210000), and scen_022 (the high-urgency $-6,068.91 prepaid-software duplicate on account 131000). As the de-minimis AP partner, she handles scen_030 (LatticeHill for Brookfield) and scen_035 (the Pinecrest Workflow Works license-provisioning dispute). She reviews the Brookfield FP-2026-05 WIP recognition JE in scen_059, signs off Northstar's FY2025 annual accounts (scen_063) after US GAAP review, and owns the absorb-vs-change-order disposition on the Acme April out-of-scope review (scen_064) — which feeds directly into scen_065, the formal change-order package where she handles the CFO negotiation before Matthew countersigns.

**Recent activity:** BD0 kickoff calendar holds, Records Vault sign-offs on management accounts packages, the change order, and AP escalation memos. Engagement-budget Slack threads on Acme.

---

### Julia Vance — Audit Partner

**Author tasks in:** 5, 9

**Style:** Very formal, polished, and decisive. She communicates with partner-level confidence—succinct, authoritative, and focused on client stewardship, risk, and forward motion.

**Active work:** Julia is the engagement partner for client audit work. She schedules kickoffs, signs engagement letters, signs off final audit deliverables, and sits on the audit-side review of the quarterly preparer-vs-certifier independence sweep. She holds AP > $50K approval authority alongside Steven.

**Key relationships:** Ryan Delgado is her day-to-day audit senior lead. Daniel Jones is her client-lead counterpart on Northstar. Peter Sanchez is her compliance counterpart. Externally, James Randall (audit senior at E&P) recurs throughout.

**Open threads:** Two. She handles the audit-side partner review on scen_042 — the quarterly partner sign-off control test, where she's signing off that certifier independence held across the sample. And she's the engagement partner on scen_043, the Northstar FY2026 audit kickoff: she schedules the kickoff, signs the engagement letter, and gets the PBC list in motion.

**Recent activity:** Calendar holds for audit kickoffs, Records Vault engagement letters and PBC packages, partner sign-off emails in `#audit-engagements`.

---

## Admin & Operations

### Daniel Jones — Accounts Manager

**Author tasks in:** 1, 2, 5, 6, 7, 8

**Style:** Highly formal, controlled, and managerial. He communicates with authority and clarity, usually in a concise but complete way that emphasizes standards, approvals, and accountability.

**Active work:** Daniel is the most-loaded persona in the entire scenario set — 25 scenarios touch him. He oversees the accounts seniors (George McAdam, Edith Banda, Jones Harrison) and their client portfolios; he reviews completed account files, answers technical GAAP questions, watches deadlines, manages the more demanding client relationships, **triages every single AP escalation**, and **owns the disposition call on AML soft-flag triage**.

**Key relationships:** Andrea Phil above him; George, Edith, and Jones below him; Hannah Grant on the tax side; Marina Soko on compliance. Externally, he works with Rakesh Ambani (mental-wellbeing practice CEO), Maya Streamer (IRS technical advisor), Linda Burns (commercial law consultant), and Owen Mercer + Brenda Abbas — the AP-side NPCs he's on with daily.

**Open threads:** Daniel's plate is wide. On the orphan-exception family he sits in the manager seat for scen_005, scen_009, scen_020, scen_021, and scen_022, and as the named approver on scen_012 and scen_015. He's the reviewer on the Northstar April management accounts (scen_025), the Northstar Q1 partner package (scen_058), and the Northstar FY2025 annual accounts (scen_063) where he drafts the review memo. **All eight AP escalations sit in his triage queue** — scen_029 through scen_036, the workflow where he frames the issue for the partner who'll ultimately disposition. He authorizes the disposition on both recon currency refresh scenarios (scen_039, scen_040) as engagement manager. He's the client-lead on the Northstar FY2026 audit kickoff (scen_043). On AML, he's the preparer driving the Acme FY2026 BO refresh + AML risk-rating proposal in scen_061, and he countersigns the disposition recap on scen_062 (Northstar AML soft-flag triage). He weighs fee impact and routes to partner on scen_064 (Acme April OOS review), and he's the manager on the Acme Q1 quarterly AR aging cross-cut (scen_066).

**Recent activity:** Heavy footprint across `#monthly-close-coordination`, `#audit-engagements`, `#compliance-and-registrations`, `#client-onboarding`, and `#vendor-bills-and-ap`. Records Vault review memos, partner-routed approval emails, and Linear AP-standardization triage cards.

---

### George McAdam — Accounts Senior *(primary persona)*

**Author tasks in:** 1, 2, 5, 7, 8

**Style:** Professional, steady, and moderately formal. He communicates in a clear accountant's style—practical, concise, and structured, with enough explanation to guide others without becoming wordy.

**Active work:** George is the universe's primary persona — 20 scenarios. He's the working owner on a mixed portfolio of client files, the senior who bridges bookkeepers, junior accountants, graduate trainees, managers, and partners. He keeps files moving, checks numbers, coordinates with tax specialists, watches deadlines, reviews junior work, handles client communication, and pushes deliverables up to manager review.

**Key relationships:** Daniel Jones is his manager and Andrea Phil his partner. Harry Marks is his associate, and Ben Arinzo + Sean Williams are the bookkeepers in his workstream. Hannah Grant is his tax counterpart; Edith Banda and Jones Harrison are his peer seniors. Outside the firm: Jane Founders (Oracle GL vendor), Ron Atkins (XYZ Recruitment), James Randall (E&P).

**Open threads:** George shows up across every accounting workflow. On orphan exceptions, he's the peer on scen_009 and scen_011, the assignee on scen_010, the identifier on scen_015 and scen_018, and the bank-rec lead on scen_021. He prepares the BD1 close entries plus the management accounts package draft on both scen_023 (Brookfield April) and scen_024 (Brookfield May with the meals/entertainment deductibility question). He reviews and coaches the trainee preparers on the recon currency refresh pair (scen_039, scen_040). He owns the Acme D&O insurance prepaid amortization schedule (scen_051). He prepares the adjusting JE for the $3,409.86 prepaid CPE residual variance on `BL-390E6284EC1D` (scen_053). He's the approver who closes the period entry on the Acme FP-2026-04 FX revaluation (scen_055). He prepares the JE on the Brookfield Ridgepoint AR write-off (scen_056) and the WIP-to-revenue JE on the Brookfield FP-2026-05 WIP recognition (scen_059, recon `BL-75810CD0FEE4`, $4,390.62). On the AML soft-flag triage (scen_062) he gives the signal-vs-noise second opinion. For Northstar's FY2025 annual accounts he collates the working file (scen_063). And on the Acme engagement-management trio — he surfaces the overrun on scen_064, drafts and files the change order on scen_065, and reviews the aging + drafts the package on the Acme quarterly AR (scen_066).

**Recent activity:** Pervasive Slack across `#monthly-close-coordination`, `#vendor-bills-and-ap`, and `#client-onboarding`. Daily Oracle GL JEs and Records Vault working papers + adjusting JE memos.

---

### Edith Banda — Accounts Senior

**Author tasks in:** 1, 2, 5, 7, 8

**Style:** Professional, steady, and pragmatic. She speaks with moderate formality and balanced detail, usually focusing on getting work cleaned up, reviewed, and moved forward efficiently.

**Active work:** Edith owns the Northstar Legal portfolio and plays the Acme historical-comparator role. She's the firm's **standing FX second-eye reviewer** on recon currency refresh scenarios. Eleven scenarios.

**Key relationships:** Daniel Jones above her; Blue Evans is her associate and Elita Moore her trainee; George McAdam and Jones Harrison are her peer seniors; Green Spatz and Anaya Wallace are the junior preparers whose FX recons she reviews. Externally, she works with Olivia Steenkamp at Marigold Property Services.

**Open threads:** On orphan exceptions, she's the Records Vault partner on scen_010, peer on scen_013 and scen_014 (where she contributes FX-recon experience to the FX-drift dismissal), and identifier on scen_021. She's the preparer on the Northstar April management accounts (scen_025) and the preparer on the Northstar Q1 partner package (scen_058). On both recon currency refresh scenarios (scen_039, scen_040) she does the independent FX rate cross-tie as second eye. She identified the prepaid setup issue on the Acme D&O insurance scenario (scen_051) and prepared the file. On the Acme April OOS review (scen_064) she's the comparator, providing prior-year scope context from her time as the Acme senior. And on the Acme multi-state sales tax cycle (scen_067) she's the approver who posts the quarter-end accrual as Acme file owner.

**Recent activity:** Northstar and Acme Records Vault working papers; Slack threads in `#monthly-close-coordination` and `#tax-prep-and-filings`; FX recon review notes.

---

### Jones Harrison — Accounts Senior

**Author tasks in:** 1, 2, 5, 7, 8

**Style:** Moderately formal, practical, and organized. He communicates in a steady operational style, usually clear and reasonably concise, with attention to process and client deliverables.

**Active work:** Jones is the Acme close file owner and a recurring identifier on orphan-exception scenarios — he's known internally as the reconciliation expert. Seven scenarios.

**Key relationships:** Daniel Jones above; Emily Adekole is his associate, Green Spatz his trainee; George and Edith are his peer seniors. Externally: Jane Founders (Oracle GL vendor).

**Open threads:** He's the identifier on five orphan exceptions — scen_010 (as peer senior), scen_012, scen_013, scen_019, and scen_022 (where he originally flagged the prepaid-software duplicate). And he prepares the BD1 close entries on both the Acme April close (scen_027) and the Acme May close (scen_028, including the Datadog reclass).

**Recent activity:** Acme-focused JE posting, review-handoff emails, Slack across `#monthly-close-coordination` for both Acme close cycles.

---

### Harry Marks — Accounts Associate

**Author tasks in:** 1, 2, 7

**Style:** Moderately formal and fairly brief. He tends to communicate in a practical, task-oriented way, focusing on what needs to be done and what evidence supports it.

**Active work:** Harry prepares basic working papers, reconciles control accounts, checks bank balances, and prepares fixed-asset schedules. Meticulous and detail-oriented. Two scenarios.

**Key relationships:** George McAdam manages him. He works closely with Anaya Wallace, and with Ben Arinzo + Sean Williams as the bookkeepers in his workstream. Externally, Randall Peters (Payroll Officer at XYZ Recruitment).

**Open threads:** He's the assignee on scen_013, a Northstar July-period orphan exception. And on scen_019 he's the accounts associate driving the live approval chase on `exc_cb0a9a94a3084c` — a Brookfield FP-2026-05 exception on account 132000 that's sitting in comm-only state waiting on James Randall's named approval.

**Recent activity:** Working-paper activity and orphan-exception approval-chase Slack threads.

---

### Emily Adekole — Accounts Associate

**Author tasks in:** 1, 2, 7

**Style:** Moderately professional with a slightly more approachable tone than senior staff. She tends to be brief, practical, and focused on completing assigned work accurately.

**Active work:** Emily handles accounts prep, bookkeeping cleanup, sales-tax record checking, and bank reconciliations. She's the **AR aging signal owner** on bad-debt write-off scenarios. Three scenarios.

**Key relationships:** Jones Harrison manages her; Green Spatz is the trainee in the same workstream. Externally: Mark Price (Finance Assistant).

**Open threads:** On scen_005 she runs the occurrence count for the polling-bug pattern as peer. She's the assignee on scen_022, driving urgent triage on the high-urgency $-6,068.91 prepaid-software duplicate on account 131000. And she's the AR owner on scen_056 — Brookfield's Ridgepoint write-off — where she's the one monitoring AR aging and first receiving the Ridgepoint signal that the receivable's gone bad.

**Recent activity:** AR-aging Slack and review-handoff emails; orphan-exception triage threads.

---

### Blue Evans — Accounts Associate

**Author tasks in:** 1, 2, 7

**Style:** Approachable, practical, and fairly concise. He communicates in a clear working style, usually focusing on calculations, adjustments, and what needs review.

**Active work:** Blue does accounts prep, bookkeeping cleanup, sales-tax record checking, and payroll vetting. She has a particular interest in payroll accounting. One scenario.

**Key relationships:** Edith Banda manages her; Elita Moore is her peer trainee on Edith's team. Externally: Olivia Steenkamp (Marigold Property Services).

**Open threads:** She's the assignee on scen_009 — driving the live triage on a Brookfield FP-2026-05 payroll-tax-downstream exception, with Hannah Grant providing the payroll-tax-downstream peer review and Daniel Jones approving the proposed treatment.

**Recent activity:** Thin scenario footprint outside that orphan-exception assignment.

---

### Green Spatz — Trainee Accountant

**Author tasks in:** 1, 2, 7

**Style:** Relatively informal, brief, and eager-to-please. He communicates simply and directly, often seeking confirmation that he has understood instructions correctly.

**Active work:** Green does document checks, bookkeeping, reconciliations, basic schedules, and filing. She has advanced BI/reporting skills that get pulled into ad-hoc work. Two scenarios.

**Key relationships:** Jones Harrison manages her; Emily Adekole is her associate-level peer; George and Edith are in the review chain on recon work.

**Open threads:** On scen_039 she's the preparer who submitted the Northstar recon `BL-AA054D9F0898` with the $2.31 EUR FX revaluation rounding variance. And on scen_053 she's the recon preparer who surfaced the $3,409.86 prepaid CPE variance that George then turned into an adjusting JE.

**Recent activity:** BlackLine review notes and reconciliation evidence; Slack in `#monthly-close-coordination` on residual-variance threads.

---

### Anaya Wallace — Trainee Accountant

**Author tasks in:** 1, 2, 7

**Style:** Professional but approachable, with moderate formality and concise wording. She communicates clearly, tends to stay close to process, and asks direct questions when something is unclear.

**Active work:** Anaya handles document checking, bookkeeping, reconciliations, basic schedules, and client file admin. She's the **standing trainee on the AP escalation family** (five of the eight) and the **FX JE preparer** on month-end revaluations. Ten scenarios.

**Key relationships:** Harry Marks is technically her manager, though Daniel Jones is the one she pairs with on AP escalation triage. Ben Arinzo and Sean Williams are the bookkeepers she works alongside. Externally, Owen Mercer (AP specialist) is her constant partner on escalation work.

**Open threads:** On orphan exceptions she preps the May close support on scen_010 and sits as trainee assignee on scen_011's deferred-revenue context thread. Of the eight AP escalations, she's the trainee on five: scen_029, scen_030, scen_033, scen_035, and scen_036. On the recon currency refresh side, she's the preparer who ran the May FX refresh and isolated the GBP Acme Research variance in scen_040. She prepares the month-end FX JE for the Acme FP-2026-04 FX revaluation in scen_055. And on scen_066 she's the trainee pulling the AR aging buckets for the Acme Q1 quarterly AR cross-cut.

**Recent activity:** Oracle GL JE postings on FX; SAP AP invoice context pulls; Slack threads in `#cash-management-and-banking`, `#monthly-close-coordination`, and `#vendor-bills-and-ap`; messaging DMs with Owen Mercer that feel like a daily routine.

---

### Elita Moore — Accounts Graduate Trainee

**Author tasks in:** 1, 2, 7

**Style:** Fairly informal by firm standards, concise, and earnest. She communicates in a straightforward, practical way and tends to appreciate clear instructions and quick feedback.

**Active work:** Elita is the most junior of the trainees — document checks, bookkeeping, basic schedules, learning the trade. Zero scripted scenarios in the present set.

**Key relationships:** Edith Banda manages her; Blue Evans is her peer associate on Edith's team.

**Open threads:** Her anchor scenario is the deferred scen_049 (trainee onboarding) — the design reference for Category 10.1 onboarding tasks, which would be authored by the relevant manager bringing her on rather than by Elita herself.

**Recent activity:** Thin scenario footprint. Task designers should use her as a *participant* in Category 10.1 onboarding tasks.

---

### Priya Khatri — AP Coordinator *(new in v47)*

**Author tasks in:** 6

**Style:** Formal, prompt, and detail-oriented. She communicates with the brisk precision of an AP-coordination style — confirms what's in the queue, flags the specific exception, and routes to the right approver without unnecessary preamble.

**Active work:** Priya coordinates the AP function across Brookfield internal and client books. She owns invoice intake routing, vendor master accuracy, and the weekly AP exceptions triage. She works closely with Owen Mercer on day-to-day AP execution and is the first escalation point for accountants when invoice coding goes sideways.

**Key relationships:** Daniel Jones above her on AP escalation triage; Tariq Soto reports to her on AP clerical work; Lena Park is her procurement-side counterpart on PO/SOW questions; Marina Soko is her compliance counterpart on vendor due-diligence checks. External / NPC: Owen Mercer (AP Specialist NPC, day-to-day AP execution partner); vendor account managers (Brenda Abbas, etc.).

**Open threads:** None yet — Priya isn't anchored into the 52 scripted scenarios. **She's the natural canonical acting voice for new Cat 6.1 escalation tasks going forward** — any of the AP-escalation patterns in scen_029 / 031 / 033 / 036 are natural fits for Priya-authored prompts, since the AP-Coordinator role is exactly the seat that triages those exceptions.

**Recent activity:** SAP Subledger AP invoice updates; Slack in `#vendor-bills-and-ap`; vendor-master cleanup work and weekly AP exceptions runs.

---

### Tariq Soto — AP Clerk *(new in v47)*

**Author tasks in:** 6

**Style:** Moderately formal and brief. He communicates in short, operational messages — line-level invoice details, simple status updates, and quick asks when a three-way-match doesn't reconcile. New to professional services; checks in with Priya before escalating.

**Active work:** Tariq handles invoice data entry, three-way-match verification (invoice ↔ PO ↔ packing slip), and routing exceptions up to the AP Coordinator. Quick to spot vendor-master inconsistencies despite the junior seat.

**Key relationships:** Priya Khatri is his direct manager; Owen Mercer (NPC) is the AP-specialist colleague on day-to-day execution; Lena Park on the procurement side when a PO is missing or doesn't match.

**Open threads:** None yet — Tariq isn't anchored into the 52 scripted scenarios. Natural authoring seats: contained sub-step tasks like "pull line-level invoice detail on this exception for Priya to review" or "run the three-way match on this week's batch and flag mismatches."

**Recent activity:** SAP Subledger invoice entry; Slack in `#vendor-bills-and-ap`; messaging Priya with line-level questions.

---

### Marcus Knell — Billing Coordinator *(new in v47)*

**Author tasks in:** 1, 8

**Style:** Formal, methodical, and revenue-aware. He communicates with the cadence of a billing-cycle owner — references specific engagements, billing-term details, and WIP balances, and is careful about revenue-recognition timing when invoice dates and service periods don't line up.

**Active work:** Marcus runs Brookfield's internal billing function. He converts approved time and WIP into client invoices, manages billing terms by engagement, and coordinates with Accounting Services on revenue-recognition timing. He's the system-of-record owner for client AR before it lands in Oracle GL.

**Key relationships:** Daniel Jones (Accounts Manager) on engagement billing coordination; the seniors (George McAdam, Edith Banda, Jones Harrison) on WIP balances and billable-time approvals; Andrea Phil and Matthew Li when revenue-recognition timing crosses partner sign-off.

**Open threads:** None yet — Marcus isn't anchored into the 52 scripted scenarios. Natural authoring seats: Cat 1.4 WIP-to-revenue tasks where the trigger is the billing side ("convert May WIP into June invoices for engagement X"), and Cat 8 quarterly-AR-aging prep where Marcus is the natural author of the billing-cycle context Daniel reviews.

**Recent activity:** Engagement-billing records (Airtable + Records Vault); Slack in `#monthly-close-coordination`; coordination with Accounting Services on revenue-recognition timing.

---

## Bookkeeping

### Ben Arinzo — Bookkeeper

**Author tasks in:** 2, 6, 7

**Style:** Professional, practical, and concise. He tends to communicate in short, operational messages centered on records, coding, and whether required evidence is available.

**Active work:** Ben maintains client bookkeeping records, codes transactions, reconciles ledger accounts, and checks bank feeds. He's the **standing bookkeeper for AML transaction-context checks** — when Marina needs cash activity pulled from accounts, Ben's the one she messages. Eight scenarios.

**Key relationships:** George McAdam manages him; Sean Williams is his peer bookkeeper; Marina Soko DMs him for AML signal-checks; Daniel Jones leans on him for AP escalation context. Externally, Liam Scotman at Marksman Hardware and Owen Mercer round out his regulars.

**Open threads:** On orphan exceptions he's the assignee on scen_005 (the stale-SLA $46.52 on account 219000), peer on scen_019, the urgent assignee on scen_020 (the SLA-breached $6,328.86 on account 210000), and peer on scen_022 (the prepaid-software duplicate, where he owns the underlying amortization schedules). He pulls accrual history on the GraniteRack AP escalation (scen_031) and sorts the IR scope letter + cost classification on the CrownPeak escalation (scen_034). On scen_062 — the Northstar AML soft-flag triage — he's the bookkeeper pulling cash activity on accounts 101000 and 105000 for FP-2026-03 and FP-2026-04. And on the Acme Q1 quarterly AR (scen_066) he provides cash-receipts context.

**Recent activity:** Oracle GL bookkeeping postings, SAP AP context pulls, Records Vault receipts and transaction support, and DMs with Marina Soko on AML work.

---

### Sean Williams — Bookkeeper

**Author tasks in:** 2, 6, 7

**Style:** Moderately professional, concise, and methodical. He communicates in a straightforward operational way, usually centered on reconciliations, exceptions, and completion status.

**Active work:** Sean maintains client bookkeeping records and is the Oracle GL expert favored by SME clients. Two scenarios.

**Key relationships:** George McAdam manages him; Ben Arinzo is his peer; he works with Edith Banda on Northstar. Externally: Brenda Abbas (Oracle GL vendor), Taye Chestnut.

**Open threads:** He's the assignee on scen_006 — a Brookfield Cash Operating orphan exception that surfaced during audit-prep week. And he drives the live triage on scen_021, the Northstar live exception `exc_af7274fb658844` (still in `investigating` state) on cash operating.

**Recent activity:** Routine GL/AP bookkeeping; cash-operating orphan-exception threads.

---

## Tax

### Alex Cahoon — Corporate Tax Manager

**Author tasks in:** 3

**Style:** Very formal, technical, and thorough. He communicates like a tax manager: precise, structured, and comfortable giving fuller explanations where compliance or technical interpretation matters.

**Active work:** Alex is the IRS liaison and the manager over the corporate tax seniors (Hannah Grant in particular). He reviews tax computations and does strategic tax planning. He's the **recurring identifier** on closed-exception verifications — the second voice confirming that a prior dismissal still stands. Four scenarios.

**Key relationships:** Ming Chang above him; Hannah Grant, William White, and Tom Chang on the team. Externally: Priya Singh (IRS), John Bartlett (Southgate Interiors).

**Open threads:** He's the identifier on three closed-exception verifications — scen_005 (account 219000), scen_006 (account 101000), and scen_014 (the Northstar FX-drift dismissal where he explains why the prior call was correct). And he's the approver on scen_018, the Acme accrued-comp FX revaluation drift, confirming the closure stands.

**Recent activity:** Email correspondence on orphan-exception verifications; appearances in `#monthly-close-coordination` and `#tax-prep-and-filings`.

---

### Hannah Grant — Corporate Tax Senior

**Author tasks in:** 3

**Style:** Formal, thorough, and analytical. She communicates with careful precision, often giving context, rationale, and technical detail when discussing tax matters.

**Active work:** Hannah prepares and reviews tax computations and returns and advises on tax-aligned treatment back at the bookkeeping stage. She's a capital-allowances specialist and pulls double duty as the **tax-side reviewer overlay on a wide swath of orphan-exception scenarios**, plus the standard tax-cycle reviewer. Fourteen scenarios.

**Key relationships:** Alex Cahoon manages her; William White and Tom Chang are her associates; George McAdam and Edith Banda are the accounting seniors she pairs with most. Externally: Remy Mas (client Finance Officer).

**Open threads:** On orphan exceptions she's the peer noting the running polling-bug pattern on the canonical scen_001, the reviewer on scen_009 (the payroll-tax-downstream exception), scen_010, and scen_011, the tax reviewer on scen_012 and scen_014, and again the tax reviewer on scen_019 (the GBP payment-timing angle on account 132000). On scen_020 she's actually the identifier — she's the one who originally flagged the duplicate AP entry. She reviews the Acme Q1 estimated tax (scen_046) and sits on the Northstar partnership-distribution tax planning workshop (scen_047). On scen_053 she's the recon reviewer who judges the $3,409.86 prepaid CPE residual variance should be booked. On the Acme quarterly AR (scen_066) her prior comments frame the tax implications. And she's the reviewer on the Acme multi-state sales tax cycle (scen_067, on nexus + per-state coding) and the tax manager reviewing William's draft on the Northstar annual partnership tax return (scen_068).

**Recent activity:** Heavy email and Slack across `#tax-prep-and-filings`; BlackLine review notes on the residual variance; Records Vault tax memos; messaging DMs with Tom Chang.

---

### William White — Corporate Tax Associate

**Author tasks in:** 3

**Style:** Moderately formal, careful, and methodical. He communicates clearly and with enough detail to show his working, especially on tax preparation and technical checks.

**Active work:** William prepares federal tax returns and handles book-tax differences. Note that the scenario yamls label him "Tax Partner of record" for Northstar engagements — that's a scenario-specific engagement-authorization role rather than his actual persona title. Three scenarios.

**Key relationships:** Hannah Grant manages him; Tom Chang is his peer associate.

**Open threads:** On scen_014 he's the assignee who briefly re-doubts the prior FX-drift dismissal before Alex talks him through why the original call was right. He chairs the Northstar partnership-distribution tax planning workshop (scen_047) as tax partner. And he's the tax partner of record on the Northstar annual partnership tax return (scen_068), authorizing the draft returns Tom prepared.

**Recent activity:** Records Vault tax-return drafts; Slack in `#tax-prep-and-filings`; orphan-exception verification on Northstar.

---

### Tom Chang — Tax Associate

**Author tasks in:** 3

**Style:** Approachable, fairly concise, and moderately formal. He communicates in a straightforward working style, usually focused on task completion and clarifying technical requirements.

**Active work:** Tom prepares federal and multi-state tax returns. He's the named assignee on the canonical scen_001 stale-tickler thread. Five scenarios.

**Key relationships:** Hannah Grant manages him; William White is his peer; he works with Ryan Delgado on audit-adjacent items and gets Matthew Li at the partner endpoint.

**Open threads:** He's the assignee on the canonical scen_001 stale-tickler thread on `exc_151b0bee7e374e`. He's also the tax associate assigned to scen_012's `exc_652c0931bb2546`. On the Northstar partnership-distribution tax planning workshop (scen_047) he pulls prior-year JE references. He's the preparer who opened the Acme multi-state sales tax cycle (scen_067). And he prepares the federal partnership return on the Northstar annual partnership tax (scen_068).

**Recent activity:** Reminder workflow exchanges on stale SLAs; Slack in `#monthly-close-coordination` and `#tax-prep-and-filings`; Records Vault tax-return drafts.

---

## Compliance

### Peter Sanchez — Head of Compliance

**Author tasks in:** 4, 9

**Style:** Highly formal, controlled, and authoritative. He communicates with clear compliance leadership, balancing precision, confidentiality, and firm decision-making.

**Active work:** Peter leads compliance oversight — GDPR procedures, AML policy application, professional-body requirements, risk reviews. He **signs off the quarterly partner sign-off control test and the quarterly document retention sweep**. Three scenarios.

**Key relationships:** Steven Perry above him; Marina Soko is his compliance officer; Julia Vance is his audit-partner counterpart. Externally: Anita Knowles (AML Supervisory Officer), Robin Woods (AICPA).

**Open threads:** He reviews and signs the control-test memo on scen_042 (quarterly partner sign-off control test). He provides compliance leadership sign-off on scen_044 (quarterly document retention control sweep). And he's the compliance partner with oversight and final sign-off on scen_048 — the Brookfield state annual report catch-up across NY, NJ, and DE, including late penalties and go-forward controls.

**Recent activity:** Records Vault compliance memos; Slack in `#compliance-and-registrations`; quarterly control-test sign-offs.

---

### Marina Soko — Compliance Officer

**Author tasks in:** 4

**Style:** Highly formal, calm, and compliance-driven. She communicates in a controlled, factual way, with careful wording that reflects confidentiality, risk awareness, and policy discipline.

**Active work:** Marina makes sure the firm's work happens in compliance with GDPR/privacy, AML, and accounting standards. She **runs the AML wire-flag review, the quarterly partner sign-off control test, the quarterly document retention sweep, and the Northstar AML soft-flag triage**. Four scenarios.

**Key relationships:** Peter Sanchez above her; Daniel Jones is her escalation partner on AML triage; Ben Arinzo is her go-to for transaction-context pulls. Externally, Farah Dlamini (AML analyst — her quarterly control-test partner), Robin Woods (AICPA), Anita Knowles (AML Supervisory Officer).

**Open threads:** She coordinates the Acme AML wire-flag review (scen_041) on `JE-acme_cloud-FP-2026-04-0052` — the $57,077.69 payment from Acme's largest enterprise SaaS customer that tripped the $10K FinCEN monitoring threshold — getting Anita Knowles's supervisory sign-off in the process. She runs the quarterly partner sign-off control test (scen_042), drafting the independence memo around a 5-recon sample (`BL-A81316258BCB`). She runs the quarterly document retention control sweep (scen_044). And on scen_062 she's the compliance officer who surfaced the adverse-media partial-name match on a Northstar BO with > 25% LLP interest — the trigger for the Northstar AML soft-flag triage.

**Recent activity:** Messaging DMs to Ben Arinzo for transaction context on accounts 101000 and 105000; Slack in `#compliance-and-registrations`; Records Vault disposition memos.

---

## Audit

> As of v47 the audit-support team is a four-person stack: Mia Hartwell (Audit Staff), Ryan Delgado (Audit Senior), Devon Beale (Audit Manager), and Julia Vance (Audit Partner). Mia and Devon are new in v47 and don't yet appear in any of the 52 scripted scenarios — they're available authoring seats for new Cat 5 / Cat 7 task design.

### Mia Hartwell — Audit Staff *(new in v47)*

**Author tasks in:** 5, 7

**Style:** Professional, moderately formal, and concise. She communicates with the practical brevity of audit-fieldwork work — short status notes, specific evidence references, and quick questions when something on tick-and-tie doesn't reconcile.

**Active work:** Mia joined Brookfield from a Big-4 audit rotation. She handles tick-and-tie work, vouches detail testing on the Northstar and Acme engagements, and is the day-to-day fieldwork partner to the audit senior. CPA-exam-track.

**Key relationships:** Ryan Delgado is her senior on day-to-day fieldwork; Devon Beale reviews her workpapers; Julia Vance is the partner above. She works alongside the Cat 1 / Cat 5 senior team (George McAdam, Edith Banda, Jones Harrison) on the audit side of annual-accounts work.

**Open threads:** None yet — Mia isn't anchored into the 52 scripted scenarios. Natural authoring seats: any of the Cat 5 audit-staff prep, PBC chasing, or Cat 7 fieldwork-recon-review tasks where the existing scripted role assignments don't already burn the audit-senior slot. Pair her with Ryan as the reviewer above on new designs.

**Recent activity:** Tick-and-tie spreadsheets attached to BlackLine reconciliations; Slack in `#audit-engagements`; Records Vault PBC items.

---

### Ryan Delgado — Audit Senior

**Author tasks in:** 5, 7

**Style:** Formal, careful, and documentation-oriented. He communicates with audit-style precision, usually clear and moderately detailed, especially where controls, access, or evidence are involved.

**Active work:** Ryan does cross-client audit work — trial balances, internal controls walk-throughs, fieldwork sections of workpapers. He's on the Acme Q1 audit and the Northstar annual audit. He's the **recurring identifier and audit-side approver on orphan-exception scenarios**. Ten scenarios.

**Key relationships:** Julia Vance above him; Devon Beale (new v47) is his manager-tier review counterpart; Mia Hartwell (new v47) is his staff fieldwork partner; Daniel Jones is his Northstar client-lead counterpart; he works with Alex Cahoon and Marina Soko regularly. Externally: James Randall (E&P audit senior).

**Open threads:** On orphan exceptions he's the identifier on scen_001 (the canonical thread), scen_009, and scen_011, the audit lead on scen_006 (during audit-prep week), the audit senior on scen_018, and the approver on scen_014 (the Northstar FX-drift dismissal) and scen_020 (the urgent AP duplicate-entry). On scen_043 he's the audit senior lead for the Northstar FY2026 audit kickoff, handling day-to-day coordination and the PBC list. On scen_055 he owns the rate snapshot — confirming the month-end FX rate for the Acme FP-2026-04 FX revaluation. And on scen_061 he's the approver on the AML risk-rating decision in the Acme BO refresh, sitting in a managing-partner-style slot for the AML side of the work.

**Recent activity:** Records Vault workpapers and PBC checklists; Slack in `#audit-engagements` and `#compliance-and-registrations`; Oracle GL trial-balance pulls.

---

### Devon Beale — Audit Manager *(new in v47)*

**Author tasks in:** 5

**Style:** Highly formal, measured, and managerial. He communicates with the structured detail of an audit-review style — frames the issue, cites the relevant standard, recommends a disposition, and flags what the partner needs to see before sign-off.

**Active work:** Devon is the audit manager — engagement planning, in-charge review, and partner-level memo prep across Brookfield's client audits. He's the bridge between staff fieldwork (Mia, Ryan) and partner sign-off (Julia).

**Key relationships:** Julia Vance above him on sign-off; Ryan Delgado is the senior under him on fieldwork; Mia Hartwell is the staff on the same engagements; Daniel Jones (Accounts Manager) is the client-side counterpart on Northstar; Matthew Li and Andrea Phil are the engagement partners he routes annual-accounts memos to.

**Open threads:** None yet — Devon isn't anchored into the 52 scripted scenarios. Natural authoring seats: the planning-memo and in-charge review steps that sit between scen_043 (Northstar audit kickoff) and the partner sign-off in scen_058 / scen_063, and any Cat 5.2 PBC-tracking task that needs a manager-tier escalation seat above Ryan.

**Recent activity:** Records Vault planning memos and review notes; Slack in `#audit-engagements`; calendar holds for partner-review slots.

---

## Procurement *(new department in v47)*

### Lena Park — Procurement Officer *(new in v47)*

**Author tasks in:** 6

**Style:** Highly formal, organized, and procurement-aware. She communicates with the structured precision of a procurement function — references specific PO numbers, SOW versions, and contract dates, and keeps procurement and AP responsibilities cleanly separated.

**Active work:** Lena owns the procurement function for Brookfield — PO issuance, vendor onboarding diligence, and the SOW lifecycle. **Deliberately separated from AP per segregation-of-duties controls**, so she coordinates with AP (Priya / Tariq) on PO-to-invoice matching and with Compliance (Marina) on vendor due-diligence checks.

**Key relationships:** Priya Khatri on the AP side; Marina Soko on compliance / vendor due diligence; Daniel Jones when an escalation crosses procurement into AP-disposition territory. External: vendor account managers (e.g., Brenda Abbas NPC).

**Open threads:** None yet — Lena isn't anchored into the 52 scripted scenarios. The natural fit is the scen_031 GraniteRack SOW-supersession question (the active `SOW-2025-GR-rev1` dated 2025-10-15 replaced the earlier SOW the disputed invoice was billed under), but she isn't woven into that yaml yet. Other natural Cat 6 authoring spots: any task where the question is "which SOW version actually governs this invoice" or "did this vendor pass onboarding diligence before the first PO went out."

**Recent activity:** Records Vault vendor SOWs and PO packets; Slack in `#vendor-bills-and-ap`; vendor-side coordination via messaging.

---

## HR & People Operations

The four HR personas below **can author Category 10 tasks** — onboarding & access provisioning, the appraisal cycle, and EEOC disputes. They're full personas, not background NPCs. The Category 10 scenario anchors (scen_049 for trainee onboarding, scen_060 for new-engagement setup) sit in the deferred set, so a lot of Category 10 task design draws on the framework in [`03_TASK_CATEGORIES`](03_TASK_CATEGORIES%20-%20BROOKFIELD%20UNIVERSE.html) plus the participant slots HR personas hold in cross-functional scenarios.

### Brent Noah — Director of People and Culture

**Author tasks in:** 10

**Style:** Highly formal, composed, and executive in tone. He communicates with authority and people-leadership focus, typically concise but complete enough to signal judgment and policy alignment.

**Active work:** Brent leads people strategy, recruitment planning, culture initiatives, leadership support, staff engagement, and retention planning. He reports to Steven Perry.

**Key relationships:** Steven Perry above him; Clint Peterson is his direct report; Rachel Green and Reshma Patel sit one layer below.

**Open threads:** Zero scripted scenarios. Brent shows up as a participant in cross-functional people-impact tasks and as the author of higher-level Category 10 work (firm-wide appraisal cycle kickoff, strategic onboarding decisions for senior hires).

**Recent activity:** Thin scenario footprint. Calendar holds for people-strategy reviews.

---

### Clint Peterson — HR Operations Manager

**Author tasks in:** 10

**Style:** Professional, composed, and people-oriented. He communicates with moderate formality and enough detail to clarify expectations, policy, and next steps without overcomplicating matters.

**Active work:** Clint handles headcount, performance, and resource planning, the appraisal cycle, promotions, conflict resolution, employment law, and firm policy.

**Key relationships:** Brent Noah above him; Rachel Green and Reshma Patel are his direct reports. Externally: James O'Brien (EEOC Conciliation Officer).

**Open threads:** Zero scripted scenarios. Clint is the natural acting voice when an EEOC dispute lands or when an appraisal-cycle process question needs HR ops judgment.

**Recent activity:** Thin scenario footprint.

---

### Rachel Green — HR Business Partner

**Author tasks in:** 10

**Style:** Professional, empathetic, and policy-aware. She communicates with moderate-to-high formality, usually balancing warmth with discretion and procedural clarity.

**Active work:** Rachel supports managers with recruitment, onboarding, appraisals, training plans, disciplinary matters, employee relations, wellbeing, and grievances.

**Key relationships:** Clint Peterson above her; Reshma Patel is her peer generalist.

**Open threads:** Zero scripted scenarios. She's the likely participant in scen_049 (the deferred trainee-onboarding anchor) and the natural acting voice for Category 10.1 onboarding tasks when the prompt centers on the HR-side coordination rather than the manager-side decision.

**Recent activity:** Thin scenario footprint.

---

### Reshma Patel — HR Generalist

**Author tasks in:** 10

**Style:** Professional, discreet, and people-focused. She communicates with fairly high formality and moderate detail, often aiming for clarity, reassurance, and policy consistency.

**Active work:** Reshma handles day-to-day HR operations.

**Key relationships:** Clint Peterson above her; Rachel Green is her peer.

**Open threads:** Named in two orphan-exception yamls — scen_012 and scen_015 — but in non-HR "Accounts-side peer" roles. That's a scenario-generator quirk; the Reshma slot in those yamls is procedural color, not actual HR work. For genuine Category 10 task authoring she's a clean acting voice on day-to-day HR ops.

**Recent activity:** The two non-HR peer appearances in the orphan-exception data. Otherwise thin.

---

## Cross-reference: People by scenario count

For task designers who want to start with the most "connected" personas:

| Persona | Scenario count | Authors in | Notes |
|---------|---------------:|------------|-------|
| **Daniel Jones** | **25** | 1, 2, 5, 6, 7, 8 | Manager-layer triage across MMA, all 8 AP escalations, orphan exceptions, AML, audit, OOS |
| **George McAdam** | **20** | 1, 2, 5, 7, 8 | Primary persona; preparer/identifier/peer across all major workflows |
| **Hannah Grant** | **14** | 3 | Tax-side reviewer overlay on orphan exceptions + tax cycles + recon-residual review |
| **Andrea Phil** | **14** | 1, 5, 6, 8, 9 | Partner certifier across Brookfield + Acme closes; OOS/change-order disposition |
| **Matthew Li** | **14** | 1, 5, 6, 8, 9 | Partner-level signoffs across Northstar engagement, orphan exceptions, AP escalations, change order |
| **Edith Banda** | **11** | 1, 2, 5, 7, 8 | Northstar preparer + FX second-eye + Acme historical comparator |
| **Anaya Wallace** | **10** | 1, 2, 7 | Trainee anchor across AP escalations, FX JE prep, AR aging, orphan-exception live triage |
| **Ryan Delgado** | **10** | 5, 7 | Audit + identifier across orphan exceptions + FX rate snapshot + BO-refresh approver |
| **Ben Arinzo** | **8** | 2, 6, 7 | Bookkeeper context across AML triage, AP escalations, orphan-exception assignments |
| **Jones Harrison** | **7** | 1, 2, 5, 7, 8 | Acme close preparer + recurring identifier on orphan exceptions |
| **Steven Perry** | **6** | 6, 9, 10 | Managing-partner final clearance across AP > $50K + AML + control tests; EEOC partner sign-off |
| **Tom Chang** | **5** | 3 | Stale-reminder triage + multi-state sales tax + annual partnership tax + tax planning |
| **Marina Soko** | **4** | 4 | AML + quarterly compliance control tests |
| **Alex Cahoon** | **4** | 3 | Identifier on closed-exception verifications |
| **Peter Sanchez** | **3** | 4, 9 | Head-of-compliance sign-off on quarterly control + state catch-up |
| **Emily Adekole** | **3** | 1, 2, 7 | AR aging + orphan-exception peer/assignee |
| **William White** | **3** | 3 | Northstar tax partner of record + orphan-exception assignee |
| **Harry Marks** | **2** | 1, 2, 7 | Orphan-exception assignee on Northstar + Brookfield |
| **Green Spatz** | **2** | 1, 2, 7 | Trainee recon preparer + residual variance recon preparer |
| **Sean Williams** | **2** | 2, 6, 7 | Cash-operating orphan-exception assignee |
| **Julia Vance** | **2** | 5, 9 | Audit partner on Northstar kickoff + quarterly control test |
| **Ming Chang** | **2** | 3, 9 | Tax-partner approver on Brookfield + Acme tax cycles |
| **Reshma Patel** | **2** | 10 | Named in non-HR peer roles in scen_012/015; clean acting voice for HR ops |
| **Blue Evans** | **1** | 1, 2, 7 | Orphan-exception assignee |
| **Clint Peterson** | **0** | 10 | HR ops manager — natural acting voice on EEOC + appraisal cycle |
| **Rachel Green** | **0** | 10 | HR business partner — natural acting voice on onboarding |
| **Brent Noah** | **0** | 10 | Director of People and Culture — strategic HR work |
| **Elita Moore** | **0** | 1, 2, 7 | Anchored in deferred scen_049 |
| **Mia Hartwell** *(v47)* | **0** | 5, 7 | Audit Staff — tick-and-tie + detail testing; available authoring seat |
| **Devon Beale** *(v47)* | **0** | 5 | Audit Manager — engagement planning + in-charge review; available authoring seat |
| **Priya Khatri** *(v47)* | **0** | 6 | AP Coordinator — natural canonical voice for new Cat 6.1 escalations |
| **Tariq Soto** *(v47)* | **0** | 6 | AP Clerk — contained-step acting seat (line-level invoice detail, three-way match) |
| **Lena Park** *(v47)* | **0** | 6 | Procurement Officer — PO/SOW side of Cat 6; SoD-separated from AP |
| **Marcus Knell** *(v47)* | **0** | 1, 8 | Billing Coordinator — WIP-to-invoice conversion; natural author for billing-cycle tasks |