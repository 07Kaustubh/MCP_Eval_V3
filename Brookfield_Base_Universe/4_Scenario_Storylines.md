# Scenario Storylines — Brookfield CPAs & Advisors

This is the narrative tour of the **52 scripted scenarios** that live as merged yamls under `metadata/scenarios/`. Another nine yamls sit in checkpoint/partial state — Stage-2 generation pathology cases that haven't been recovered yet.

Each scenario is a beat-by-beat artifact chain — a Slack thread leading to a JE, a review email, a support memo, a sign-off — strung across Oracle GL, BlackLine, the SAP Subledger, Records Vault, Airtable, email, Slack, messaging, calendar, reminder workflows, and Linear. Think of each one as a starting-condition template: the agent picks the situation up "as of" `scenario_start`, which is uniformly `2026-05-31T09:00:00Z` in this set.

The scenarios are grouped into eight workflow families. Within each family, every scenario is told as a short story — what's happening, who's holding which piece, what the anchor IDs reference — so a task author can pick one up and start writing prompts without needing to re-read the underlying yaml.

**Universe constants:** today = `2026-06-12 US/Eastern`; FYE `12-31`; email domain `brookfieldcpas.com`. The fiscal periods labeled `FP-2026-05` are still `status=open` — the lock target's passed, but nobody's actually locked them. **Category numbers 1–10** map to [`03_TASK_CATEGORIES`](03_TASK_CATEGORIES%20-%20BROOKFIELD%20UNIVERSE.html).

---

## Family summary

| # | Family | Count | Primary category |
|---|--------|------:|-----------------|
| 1 | Monthly Management Accounts / Close | 5 | **1** |
| 2 | Orphan Exception / Stale SLA / Live Triage | 15 | **7** |
| 3 | AP Escalation | 8 | **6** |
| 4 | Recon Currency Refresh | 2 | **7** |
| 5 | Audit & Compliance | 5 | **4 / 5** |
| 6 | Tax & Regulatory | 3 | **3** |
| 7 | Adjusting / Recon / FX / Bad Debt / WIP / Fixed Asset | 6 | **1 / 7** |
| 8 | AML, Engagement Mgmt, Quarterly AR, Sales Tax, Annual Tax | 8 | **3 / 4 / 8** |
| | **Total** | **52** | |

---

## Family 1 — Monthly Management Accounts / Close (5 scenarios) — Category 1

The heartbeat of the firm. Every month, on the standard BD-day calendar: BD0 kickoff, BD1 close-period entries, reviewer feedback, revisions, reviewer green-light, BD3 period lock, BD5 close, and the partner's sign-off on the management accounts package. Five scenarios in this family — two Brookfield closes, one Northstar, two Acme — each with its own texture.

### scen_023 — Brookfield April Close
*Entity: brookfield · Period: brookfield_FP-2026-04 · Category 1.1*

Brookfield's own April books need to close on the standard BD-day calendar. George McAdam (Accounts Senior) posts the BD1 entries — the usual accruals, prepaid CPE amortization, monthly depreciation — and hands the working file to Margaret Sullivan, the client-side Controller, for end-of-BD2 review. Andrea Phil signs off after the lock target. This is the Mode-A baseline scenario: the canonical close-cycle setup that the audit-loop SOP was built against, and the one to reference when you want a clean close pattern to compare other scenarios to.

*Components: calendar, email, oracle_gl, records_vault, reminder, slack*

### scen_024 — Brookfield May Close (with a deductibility question)
*Entity: brookfield · Period: brookfield_FP-2026-05 · Category 1.1*

Same shape as the April close, but the wrinkle is that during reviewer green-light Andrea raises a deductibility question on a meals/entertainment line — something doesn't look right in the way it's been coded. George has to quantify the misclassification before lock and commit a clarifying memo so the package can move forward cleanly. Standard cycle with a tax-flavored detour.

*Components: calendar, email, oracle_gl, records_vault, reminder, slack*

### scen_025 — Northstar Legal April Close
*Entity: northstar_legal · Period: northstar_legal_FP-2026-04 · Category 1.1*

Edith Banda prepares the BD1 entries for Northstar's April close — expert-witness and co-counsel accruals, WIP recognition, the CLE prepaid release. Daniel Jones reviews. Matthew Li certifies as the Accounting Services Partner on the Northstar engagement. The legal-industry rhythm shows up here in the specific accruals and the WIP treatment.

*Components: blackline, calendar, email, oracle_gl, records_vault, reminder, slack*

### scen_027 — Acme Cloud April Close (outsourced)
*Entity: acme_cloud · Period: acme_cloud_FP-2026-04 · Category 1.1*

Acme is fully outsourced — Brookfield runs the close. Jones Harrison drafts the entries, Brenda Abbas (NPC, on the client side) reviews, Andrea signs off. The Acme-specific items are what make it interesting: deferred revenue release, ASC 340-40 sales-commissions amortization, and the cloud-infrastructure accrual that's part of any SaaS close.

*Components: blackline, calendar, email, oracle_gl, records_vault, reminder, slack*

### scen_028 — Acme Cloud May Close (Datadog reclass)
*Entity: acme_cloud · Period: acme_cloud_FP-2026-05 · Category 1.1*

May rolls around and Jones is back with three BD1 JEs, but the close-cycle coordination this time centers on a Datadog enterprise renewal that's been miscoded. The reclass moves it from account 500000 to 521000, and Jones puts together a supporting memo so the final management accounts package can be signed off cleanly.

*Components: blackline, calendar, email, oracle_gl, records_vault, slack*

---

## Family 2 — Orphan Exception / Stale SLA / Live Triage (15 scenarios) — Category 7

This is the expanded BlackLine-discipline family — the firm's biggest single cluster of scenarios. Two flavors live underneath the same umbrella:

The first flavor — **stale-SLA tickler re-fires on an already-closed exception** (Category 7.1) — is the polling-bug pattern. The assignee gets an old reminder for an exception that was actually closed weeks or months ago; the identifier and approver confirm the closure still stands; somebody documents the dismissal; and ideally somebody else notices the polling bug is systemic.

The second flavor — **live triage on a currently-open exception** (Category 7.2) — is the active-work version. The assignee drives the resolution path, the identifier explains how it got flagged, the tax or audit reviewer adds domain context, the manager frames the SLA-breach optics, and the partner provides clearance.

All fifteen scenarios use the same lean component set: `email, messaging, reminder, slack`. The design point is the persona rotation — the same scenarios get authored with different personas in the assignee/identifier/approver/reviewer/manager/partner/peer slots.

### scen_001 — Brookfield AR (the canonical example)
*Entity: brookfield · Category 7.1 · Exception: exc_151b0bee7e374e on AR 110000, $647.97, period brookfield_FP-2025-07, recon BL-2E691B2E18FA*

The canonical stale-tickler thread. Tom Chang gets a reminder for an exception that was closed last summer — $647.97 on AR 110000 from FP-2025-07, recon `BL-2E691B2E18FA`. Ryan Delgado, who identified it originally, confirms the closure. James Randall (NPC) is the approver standing behind the August sign-off. Hannah Grant, peering in from the tax side, notes that this looks like the recurring polling-bug pattern. Matthew Li gives the partner-side audit-trail recap. If you want to study the family's structure, start here.

### scen_005 — Brookfield AP-employee-reimbursements
*Entity: brookfield · Category 7.1 · Exception: exc_df0e3e636dfd4d, account 219000, $46.52*

A $46.52 stale-SLA tickler on the AP-employee-reimbursements account. Tiny dollar amount, full process. Ben Arinzo is the assignee; Alex Cahoon identified it; James Randall approved the original closure; Daniel Jones is the manager on the recap; Emily Adekole is the peer running an occurrence count to see whether this is another polling-bug instance.

### scen_006 — Brookfield Cash Operating (audit-prep week)
*Entity: brookfield · Category 7.1 · Account: 101000 Cash Operating · Closed in January*

The wrinkle on this one is timing: the stale tickler hits during audit-prep week, so it gets extra eyes. Sean Williams is the assignee; Alex Cahoon identified it; James Randall stands behind the original closure (which dates back to January); Ryan Delgado is the audit lead reading the recap with audit-prep eyes; Matthew Li signs off as partner.

### scen_009 — Brookfield FP-2026-05 payroll-tax-downstream
*Entity: brookfield · Category 7.2*

A live-triage case — currently open, on FP-2026-05, with a downstream payroll-tax angle. Blue Evans is driving the resolution. Ryan Delgado identified it. Hannah Grant takes the payroll-tax-downstream peer review. George McAdam contributes precedent from a prior accept-timing call. Daniel Jones approves the proposed treatment.

### scen_010 — Brookfield FP-2026-05 May close
*Entity: brookfield · Category 7.2 · Exception: exc_1ddfc978ce5a4d*

A live exception that surfaces during the May close itself. George McAdam is the assignee. Anaya Wallace is supporting the close prep. Jones Harrison weighs in with peer-senior precedent. Edith Banda holds the Records Vault partner role and checks the records-vault metadata trail. Hannah Grant pulls the recommendation together and frames the escalation.

### scen_011 — Brookfield deferred-revenue context
*Entity: brookfield · Category 7.2 · Exception: exc_06b89e3937b04a*

A live exception with a deferred-revenue dimension. Anaya Wallace is the trainee assignee. Ryan Delgado identified the issue. Hannah Grant is the tax/revenue-recognition reviewer. Andrea Phil holds partner visibility on the weekly revenue numbers. George McAdam contributes peer precedent from a prior deferred-revenue variance.

### scen_012 — Brookfield tax-associate assignment
*Entity: brookfield · Category 7.2 · Exception: exc_652c0931bb2546*

A live exception that lands on a tax associate. Tom Chang is preparing the response. Jones Harrison is the identifier. Daniel Jones is the named approver. Hannah Grant is the tax reviewer confirming the variance. Reshma Patel (in a procedural peer slot) reinforces the need for closure verification.

### scen_013 — Northstar July exception
*Entity: northstar_legal · Category 7.1*

A stale tickler on a Northstar exception originally dated July. Harry Marks was the original assignee. Jones Harrison reconfirms the closure as identifier. James Randall (NPC) stands behind the August closure. Matthew Li sets the client-presentable tone on the recap. Edith Banda brings Northstar engagement context as peer.

### scen_014 — Northstar FX-drift dismissal
*Entity: northstar_legal · Category 7.1 · Exception: exc_344bcd6e4c7a4c (closed, FX-drift dismissal stands)*

A closed-exception verification where the original dismissal was FX-drift related. William White, as assignee, briefly re-doubts the prior call before Alex Cahoon walks him through why the dismissal was correct. Ryan Delgado confirms closure as approver. Hannah Grant adds the tax angle — no FX-tax-treatment exposure here. Edith Banda contributes FX-recon experience as peer.

### scen_015 — Northstar payroll-tax-withholding
*Entity: northstar_legal · Category 7.1 · Exception: exc_5221568d4e4047*

A stale tickler that lands first on the AP-specialist NPC desk. Owen Mercer (NPC) receives the reminder. George McAdam, on the firm side, recognizes the prior closure. Daniel Jones confirms it as approver. Matthew Li gives the light-touch engagement-side sign-off. Reshma Patel pattern-matches against similar Northstar items as peer.

### scen_018 — Acme accrued-comp FX revaluation drift
*Entity: acme_cloud · Category 7.1 · Exception: exc_49d97c6abdc14d (closed, Acme February 2026)*

A closed Acme exception from February that re-fires its tickler. Nia Okafor (NPC, Senior Bookkeeper) is the recipient. George McAdam reconfirms the prior dismissal. Alex Cahoon, as approver, confirms the closure stands. Andrea Phil reviews the tone of the dismissal as Acme engagement partner. Ryan Delgado, watching short-interval stale-SLA recurrences, treats this as one more data point on the polling-bug pattern.

### scen_019 — Brookfield FP-2026-05 live approval chase
*Entity: brookfield · Category 7.2 · Exception: exc_cb0a9a94a3084c, account 132000, FP-2026-05 (live, comm-only)*

A live, comm-only exception on account 132000 — Harry Marks is the accounts associate driving the approval chase. Jones Harrison originally identified it. James Randall (NPC) is the named approver. Hannah Grant reviews from the tax side, particularly on the GBP payment-timing angle. Ben Arinzo contributes peer context — he runs the underlying prepaid amortization schedule.

### scen_020 — Brookfield AP duplicate-entry SLA-breach
*Entity: brookfield · Category 7.2 · Exception: exc_a0f77f2a19104e, account 210000, $6,328.86, high-urgency SLA-breached*

A high-urgency, SLA-breached duplicate-entry exception — $6,328.86 sitting on account 210000. Ben Arinzo is chasing the urgent approval. Hannah Grant — Corporate Tax Senior — is the identifier; she's the one who originally caught the duplicate. Ryan Delgado, audit senior, is the named approver. Daniel Jones frames the SLA-breach optics in the recap. Andrea Phil holds partner visibility.

### scen_021 — Northstar cash-operating live triage
*Entity: northstar_legal · Category 7.2 · Exception: exc_af7274fb658844 (investigating status)*

A live Northstar exception still in `investigating` status. Sean Williams is driving the live triage. Edith Banda explains context as identifier. Daniel Jones handles escalation triage as manager. Matthew Li gives the light-touch Northstar-engagement sign-off. George McAdam, who runs the Northstar bank rec, sits in the peer slot.

### scen_022 — Brookfield prepaid-software duplicate-entry
*Entity: brookfield · Category 7.2 · Exception: exc_4d5d3582698946, account 131000 Prepaid Software Subscriptions, $-6,068.91, high-urgency*

A high-urgency negative-balance duplicate — $-6,068.91 on account 131000 (Prepaid Software Subscriptions). Emily Adekole is driving urgent triage. Jones Harrison originally identified it. Daniel Jones names the approver and frames the issue. Andrea Phil is copied for partner sight. Ben Arinzo, who owns the prepaid amortization schedules, sits as peer.

---

## Family 3 — AP Escalation (8 scenarios) — Category 6

This family covers aged AP invoices stuck in `pending_approval` that need formal internal escalation. The pattern is consistent across all eight: the AP specialist surfaces the aged invoice, the trainee or bookkeeper pulls the accrual and accounting history, the vendor account manager confirms vendor-side context, the AP manager triages the issue, and the partner provides the final disposition.

**v47 update on aging.** Five of the eight invoices now carry early-March-2026 SAP `invoice_date`s (scen_029 / 030 / 031 / 033 / 036). Four of those also had their Slack/email/messaging/Linear narratives rewritten to realistic aging windows — scen_029 (87 days), scen_031 (85), scen_033 (83), scen_036 (81). **scen_030 LatticeHill is the anomaly:** its SAP `invoice_date` was moved up to 2026-03-03 (~100 days to today) but its Slack messages were *not* rewritten and still cite 334 days — so that scenario shows conflicting aging between the SAP record and the Slack thread; flag it rather than trusting either number. The remaining three invoices (scen_032 / 034 / 035) keep their original mid-2025 dates and are genuinely aged at 300+ days. Cite the specific aging numbers below in new task design; they're backed by the universe data.

All eight scenarios use `email, linear, messaging, slack` (scen_036 additionally pulls in calendar). The standing cast is Owen Mercer (NPC, AP Specialist) on every one of them and Daniel Jones triaging every one of them. Brenda Abbas (NPC, vendor account manager) is on six of the eight. Anaya Wallace is the trainee on five; Mateo Kovac (NPC) covers three; Ben Arinzo is the bookkeeper on two. The new v47 personas (Priya Khatri AP Coordinator, Tariq Soto AP Clerk, Lena Park Procurement Officer) aren't yet woven into any of these eight yamls but are the natural acting seats for new Cat 6.1 task design.

### scen_029 — Acme / TimeLedger Nexus VEN-010-514242
*Entity: acme_cloud · Partner: Steven Perry (Managing Partner) · Category 6.1 · SAP record: apinv_d3019cdcc6ed44b2 ($24,475.25, account 210000) · Aging: 87 days*

A TimeLedger Nexus invoice (`VEN-010-514242`) for Acme has been `pending_approval` for 87 days — past the 60-day SLA. There's a disputed Phase-3 deliverable on file and a missing credit memo that should reconcile the dispute. **v47 added the AR-contact-departure framing**: the AR contact who originally chased the credit memo at TimeLedger left the vendor in January 2026; a new AR lead picked the issue up only recently, which is part of why it stalled. Anaya Wallace pulls history as trainee, Brenda Abbas (NPC, new AR lead) confirms vendor-side context, Steven Perry holds final managing-partner clearance. The resolution path Brenda proposes is a split payment — release $17,825 now, hold $6,650.25 pending credit memo.

### scen_030 — Brookfield / LatticeHill Learning Center VEN-033-86573
*Entity: brookfield · Partner: Andrea Phil (de-minimis release) · Category 6.1 · SAP record: apinv_5e09decd035d4443 ($887.04, AP account 210000; expense line coded to 535000)*

A long-stale `pending_approval` on `VEN-033-86573` from LatticeHill Learning Center for Brookfield. There's no dispute on the invoice itself — what surfaced is an orphan-approver routing-rule gap that left it hanging. Mateo Kovac (NPC) sits in the bookkeeper slot. Andrea handles the de-minimis release. **v47 anomaly note:** scen_030's SAP `invoice_date` was re-dated to 2026-03-03 (~100 days) like the other recent invoices, but its Slack messages were *not* rewritten and still cite "334 days" — so the SAP record and the Slack thread disagree on aging. Treat it as an outlier / data-inconsistency case rather than the typical pattern.

### scen_031 — Acme / GraniteRack Compute VEN-012-753165
*Entity: acme_cloud · Partner: Steven Perry · Category 6.1 · SAP record: apinv_6131b7c637aa4b6e ($39,090.56, account 219000) · Aging: 85 days*

GraniteRack Compute invoice `VEN-012-753165` for Acme, 85 days `pending_approval`. The complication: a superseded SOW that doesn't match the invoice — the active `SOW-2025-GR-rev1` dated **2025-10-15** replaced the earlier `SOW-2024-GR-rev3` that this invoice was billed under. Ben Arinzo pulls the accrual history to compare against the disputed invoice amount. Steven gives final clearance. **v47 framing note:** the SOW-supersession question is a natural fit for Lena Park (Procurement Officer, new v47), but Lena isn't yet anchored into the scen_031 yaml itself — the changelog promised her inclusion but the yaml wasn't updated.

### scen_032 — Acme / TimeLedger Nexus VEN-010-693199
*Entity: acme_cloud · Partner: Steven Perry · Category 6.1*

Another TimeLedger Nexus invoice (`VEN-010-693199`) for Acme — aged `pending_approval` with a vendor-master detail mismatch. Mateo Kovac (NPC) is the bookkeeper. Daniel Jones approves release-with-condition. Steven sits at the partner endpoint.

### scen_033 — Northstar / CrownPeak Cyber Defense VEN-030-353041
*Entity: northstar_legal · Engagement partner: Matthew Li · Category 6.1 · SAP record: apinv_e0235997b4964a8f ($459.84, account 219000) · Aging: 83 days*

A CrownPeak Cyber Defense invoice (`VEN-030-353041`) for Northstar — 83 days `pending_approval` with suspected duplicate billing. **v47 added the platform-migration backdrop**: a sibling CrownPeak charge was already paid in a separate cycle, and a Feb-2026 platform-migration event on CrownPeak's side appears to have generated the duplicate. Anaya Wallace covers trainee, Matthew Li is the engagement partner on disposition.

### scen_034 — Northstar / CrownPeak Cyber Defense VEN-030-817856
*Entity: northstar_legal · Partner: Matthew Li · Category 6.1*

A second CrownPeak invoice (`VEN-030-817856`) for Northstar, long-pending. The substance: an IR engagement scope letter plus a cost-classification call that has to be resolved before the partner can sign off. Ben Arinzo pulls the bookkeeping context. Matthew is the partner.

### scen_035 — Pinecrest Workflow Works VEN-006-193120
*Entity: firm-internal · Partner: Andrea Phil · Category 6.1*

A firm-internal AP escalation — Pinecrest Workflow Works (`VEN-006-193120`). License-provisioning issue tangled with a usage audit and a formal dispute path. Anaya Wallace is the trainee, Mateo Kovac (NPC) sits as bookkeeper, Andrea is the partner.

### scen_036 — Northstar / CrownPeak Cyber Defense (third in series)
*Entity: northstar_legal · Partner: Matthew Li · Category 6.1 · SAP record: apinv_e42396e9bdd64294 ($422.32, account 219000) · Aging: 81 days*

The third CrownPeak escalation for Northstar — 81 days `pending_approval`. **v47 added the IR-retainer-cancellation framing**: the long-pending invoice turns out to be a stale Q1-2026 cancellation on a CrownPeak IR-retainer service that never got properly closed in the system. Tariq-style line-level pull is the natural prep step here (Tariq Soto is the new v47 AP Clerk, though not anchored in the yaml). Matthew dispositions. This one's the only AP-escalation scenario that includes calendar in its component set.

*Components: calendar, email, linear, messaging, slack*

---

## Family 4 — Recon Currency Refresh (2 scenarios) — Category 7.4

FX variance review on BlackLine reconciliations — Mode-B (comm-only) setup. Two scenarios.

### scen_039 — Northstar EUR FX rounding variance
*Entity: northstar_legal · Recon: BL-AA054D9F0898, $2.31 EUR FX revaluation rounding variance, account 220000, northstar_legal_FP-2026-05*

A tiny rounding variance — $2.31 — surfaces on a Northstar EUR recon (`BL-AA054D9F0898`) for FP-2026-05 on account 220000. Green Spatz prepared the recon as trainee. George McAdam reviews. Edith Banda does the FX second-eye cross-tie on the rate. Daniel Jones authorizes the disposition as engagement manager. The dollar size is small; the workflow is the point.

*Components: calendar, email, messaging, reminder, slack*

### scen_040 — May FX variance review (GBP vendor line)
*Entity: brookfield · Recon: BL-516B536953DA, $6,328.86 variance on account 210000, single GBP-denominated line tied to the vendor "Acme Research" (a Brookfield AP counterparty, not the acme_cloud entity)*

A bigger variance — $6,328.86 — concentrated in a single GBP Acme Research line on account 210000 (`BL-516B536953DA`). Anaya Wallace ran the May FX refresh and isolated the line. George reviews. Edith does the FX second-eye. Daniel authorizes.

*Components: calendar, email, messaging, slack*

---

## Family 5 — Audit & Compliance (5 scenarios) — Categories 4 / 5

### scen_041 — Acme AML wire-flag review
*Entity: acme_cloud · Anchor: JE-acme_cloud-FP-2026-04-0052 · Category 4.1*

A routine $57,077.69 settlement payment from Acme's largest enterprise SaaS customer — posted as `JE-acme_cloud-FP-2026-04-0052` in Oracle GL — trips the firm's standing $10K wire-transfer monitoring rule under FinCEN reporting. The trigger here is the threshold itself, not anything intrinsically suspicious about the underlying JE. The workflow is the mandatory customer due diligence review that the threshold requires. Farah Dlamini (NPC AML analyst) does the analyst pass. Marina Soko coordinates as compliance officer and works with Anita Knowles (NPC AML Supervisory Officer) for supervisory sign-off. Matthew Li is the engagement partner. Steven Perry holds final managing-partner clearance.

*Components: calendar, email, messaging, records_vault, reminder, slack*

### scen_042 — Quarterly partner sign-off control test
*Anchor: BL-A81316258BCB (5-recon sample for preparer-vs-certifier independence) · Category 4.4*

The firm's quarterly control test on preparer/certifier independence — does the same person ever prepare and certify the same recon? Marina Soko runs the test using a 5-recon sample (`BL-A81316258BCB`) and drafts the independence memo. Farah Dlamini (NPC) is her analyst partner. Peter Sanchez signs off as head of compliance. Julia Vance reviews from the audit-partner side. Steven Perry gives final clearance.

*Components: calendar, email, messaging, slack*

### scen_043 — Northstar FY2026 audit kickoff
*Entity: northstar_legal · Category 5.1*

The Northstar FY2026 audit officially kicking off. Julia Vance, as audit partner, schedules the kickoff and signs the engagement letter. Ryan Delgado is the audit senior leading day-to-day coordination and the PBC list. James Randall (NPC) provides audit senior support at E&P on the external side. Daniel Jones is the client lead inside the firm.

*Components: calendar, email, oracle_gl, records_vault, reminder, slack*

### scen_044 — Quarterly document retention control sweep
*Firm-internal · Category 4.5*

A firm-internal metadata-only review of Records Vault documents against the retention policy. Marina Soko runs the sweep. Farah Dlamini (NPC) is her analyst partner. Anita Knowles (NPC) sits in the technical-advisor slot. Peter Sanchez signs off as head of compliance. Steven Perry holds final clearance.

*Components: calendar, email, messaging, slack*

### scen_048 — Brookfield state annual report catch-up
*Entity: brookfield · Firm-internal · Category 4.6*

A multi-state annual report catch-up for Brookfield — NY, NJ, and DE all behind on filings, with late penalties to quantify and a go-forward controls memo to draft. Linda Burns (NPC, Commercial Law Consultant) provides the legal read. Anaya Patel (NPC, Workflow Administrator) handles the workflow side. Priya Singh (NPC) does the tax nexus check. Peter Sanchez is the compliance partner with oversight and final sign-off.

*Components: email, oracle_gl, records_vault, reminder, slack*

---

## Family 6 — Tax & Regulatory (3 scenarios) — Category 3

### scen_045 — Brookfield April multi-state sales tax
*Entity: brookfield · Category 3.1 · ⚠️ CoA gap on sales-tax account — confirm against entity CoA*

Brookfield's April multi-state sales tax cycle. Priya Singh (NPC, Corporation Tax Officer) prepares. Sofia Halabi (NPC, Tax Specialist) reviews and flags a Pennsylvania threshold question. Ming Chang approves and directs the PA threshold resolution.

*Components: email, oracle_gl, records_vault, reminder, slack*

### scen_046 — Acme Q1 estimated tax projection
*Entity: acme_cloud · Category 3.3*

Acme's Q1 estimated tax projection. Sofia Halabi (NPC) prepares; Hannah Grant reviews; Ming Chang approves. The system scheduler queues Q2 in the background as a follow-on.

*Components: email, oracle_gl, records_vault, reminder, slack*

### scen_047 — Northstar partnership-distribution tax planning workshop
*Entity: northstar_legal · Category 3.4*

The standing annual tax planning workshop for Northstar partnership distributions. Calendar trigger fires, prep communications go out, and a recommendation handoff lands afterward. William White chairs as tax partner. Tom Chang pulls prior-year JE references as tax associate. Hannah Grant sits in the tax-senior slot. Matthew Li is the engagement partner.

*Components: calendar, email, messaging, reminder, slack*

---

## Family 7 — Adjusting Entries, Reconciliation, FX, Bad Debt, WIP, Fixed Asset (6 scenarios) — Categories 1 / 7

> **Reconciliation surface note.** Per the Cat 7 framing in 03, **Excel is the primary reconciliation surface** at this firm — the spreadsheet holds the GL balance, the supporting items, the variance, and the explanation. BlackLine is the workflow and evidence store around the Excel workbook. Several scenarios in this family route around that distinction; keep it in mind when authoring prompts.

### scen_051 — Acme D&O insurance prepaid setup
*Entity: acme_cloud · AP invoice: VEN-018-857632 · Category 1.1*

An Acme D&O insurance policy needs to be set up as a prepaid asset and amortized properly. The AP invoice is `VEN-018-857632`. Edith Banda prepares and identifies the prepaid setup issue. Margaret Sullivan (NPC Controller) reviews. George McAdam owns the resulting amortization schedule.

*Components: email, oracle_gl, records_vault, sap_subledger, slack*

### scen_053 — Brookfield BlackLine residual variance
*Recon: BL-390E6284EC1D, $3,409.86 prepaid CPE variance · Category 7.3*

A $3,409.86 residual variance shows up on a Brookfield prepaid CPE recon (`BL-390E6284EC1D`). Green Spatz prepared the recon as trainee. Hannah Grant reviews and judges the variance should be booked rather than left to drift. George McAdam prepares the adjusting JE.

*Components: blackline, oracle_gl, records_vault, slack*

### scen_055 — Acme FP-2026-04 FX revaluation
*Entity: acme_cloud · Category 7.5*

The month-end FX revaluation for Acme's FP-2026-04 period. Ryan Delgado owns the rate snapshot — he's the one confirming the month-end FX rate. Anaya Wallace prepares the JE as trainee. George McAdam approves and closes the period entry.

### scen_056 — Brookfield Ridgepoint AR write-off
*Entity: brookfield · Category 1.1*

Brookfield has a receivable from Ridgepoint that's gone bad and needs to be written off. Emily Adekole is the AR owner watching the aging. Margaret Sullivan (NPC Controller) provides the client-side view. George McAdam prepares the JE.

### scen_058 — Northstar Q1 partner reporting package
*Entity: northstar_legal · Category 1.3*

Northstar's Q1 partner reporting package — quarterly reporting with a partner audience. Edith Banda prepares. Daniel Jones reviews. Matthew Li signs off. The working-paper review pattern here overlaps Category 5.3 work.

### scen_059 — Brookfield FP-2026-05 WIP recognition
*Entity: brookfield · Recon: BL-75810CD0FEE4, $4,390.62 · Category 1.4*

WIP recognition on Brookfield FP-2026-05. The recon (`BL-75810CD0FEE4`) carries $4,390.62 needing WIP-to-revenue treatment. Andrea Phil reviews as partner. George McAdam prepares the JE. Margaret Sullivan (NPC) reviews on the client side.

*Components: blackline, email, oracle_gl, records_vault, slack*

---

## Family 8 — AML, Engagement Mgmt, Quarterly AR, Sales Tax, Annual Tax (8 scenarios) — Categories 3 / 4 / 8

### scen_061 — Acme FY2026 annual BO refresh
*Entity: acme_cloud · Category 4.3*

The Acme annual beneficial-ownership refresh for FY2026. Daniel Jones drives the refresh as preparer and puts together the AML risk-rating proposal. Matthew Li reviews as engagement partner. Ryan Delgado approves the AML risk-rating decision in a managing-partner-style slot for the AML side.

*Components: calendar, email, records_vault, slack*

### scen_062 — Northstar AML soft-flag triage
*Entity: northstar_legal · Category 4.2*

A comm-only investigation that runs across messaging, Slack, email, and reminder — no GL entries, just judgment-call work. The trigger: an adverse-media partial-name match on a Northstar BO with more than 25% LLP interest. Marina Soko surfaces the hit as compliance officer. Ben Arinzo pulls cash activity from accounts 101000 and 105000 for FP-2026-03 and FP-2026-04 as bookkeeper. George McAdam gives the signal-vs-noise second opinion as accounts senior. Daniel Jones makes the disposition call as accounts manager and countersigns the recap.

*Components: email, messaging, reminder, slack*

### scen_063 — Northstar FY2025 annual accounts
*Entity: northstar_legal · Category 1.2*

The FY2025 annual accounts for Northstar Legal. George McAdam collates the working file as preparer. Daniel Jones reviews and drafts the review memo. Andrea Phil approves — she does the US GAAP review and signs off.

*Components: calendar, email, messaging, oracle_gl, records_vault, slack*

### scen_064 — Acme April OOS review
*Entity: acme_cloud · Category 8.1*

A +15-hour variance surfaces on the Acme April engagement, tied to multi-state sales-tax coding and AR-aging cleanup that wasn't in the original scope. George McAdam surfaces the overrun as senior. Daniel Jones weighs the fee impact as manager. Edith Banda comes in as comparator — she was the prior-year Acme senior and can speak to historical scope. Andrea Phil makes the absorb-vs-change-order disposition as partner.

*Components: email, messaging, slack*

### scen_065 — Acme formal change order
*Entity: acme_cloud · Category 8.1*

The formal scope-expansion workflow that follows directly from scen_064's OOS review. George McAdam drafts and files the change order as preparer. Andrea Phil reviews the proposal and handles the CFO negotiation. Matthew Li countersigns the engagement-letter addendum as approver.

*Components: calendar, email, records_vault, slack*

### scen_066 — Acme Q1 quarterly AR aging
*Entity: acme_cloud · Category 8.2 · 4-function cross-cut*

The Acme Q1 quarterly AR aging — a four-function cross-cut that pulls in accounts, bookkeeping, tax, and the manager layer. Daniel Jones is the manager. Anaya Wallace pulls the AR aging buckets as trainee. George McAdam reviews the aging and drafts the package as senior. Ben Arinzo provides cash-receipts context as bookkeeper. Hannah Grant's prior comments frame the tax implications.

*Components: calendar, email, messaging, oracle_gl, slack*

### scen_067 — Acme Q1 multi-state sales tax cycle
*Entity: acme_cloud · Category 3.1 · ⚠️ CoA gap on sales-tax account*

The Q1 2026 multi-state sales tax cycle for Acme. **v47 rewrote the scenario** around a SaaS-taxability determination memo (now in Records Vault, `tax_determination_memo` uploaded by Hannah Grant under `IRS_TAX_7Y`) that narrows Acme's taxable footprint to **four states: TX, NY, WA, AZ**. The other states with prior nexus references (CA, FL, IL, MA, NV, GA, NC) are exempt or services-not-taxed; existing CA-only standing monthly entries (~$29K) are a separate cleanup item rather than current accruals. The central beat is a TX nexus correction: Tom Chang opens the cycle at a $0 TX placeholder, Hannah Grant catches that Acme crossed the $612K trailing-12 economic-nexus threshold and the TX line needs to be rerun on destination-based per-ZIP local rates, Tom reruns TX, and the four-state quarter-end accrual is posted as a **single combined entry of $42,180.55** (`JE-acme_cloud-acme_cloud_FP-2026-03-0076`, `525000` Sales Tax Expense Dr / `225000` Cr) — the GL does not carry a per-state JE breakdown. Edith Banda approves as Acme file owner and posts the quarter-end accrual.

*Components: oracle_gl, records_vault, slack*

### scen_068 — Northstar FY2025 federal partnership tax
*Entity: northstar_legal · Category 3.2*

The FY2025 federal partnership return for Northstar. Tom Chang prepares the federal partnership return as tax staff. Hannah Grant reviews as tax manager. William White, sitting as tax partner of record for the Northstar engagement, authorizes the draft returns and the book-tax differences.

*Components: email, messaging, oracle_gl, records_vault, slack*

---

## Checkpoint / partial scenarios (not merged)

These have `.partial.yaml` and `.stage1_checkpoint.yaml` files but no merged `.yaml`. They hit Stage-2 generation pathology — component-confusion where non-slack artifact beats got coerced into a `DraftSlackArtifact` shape.

- **scen_002, 004, 007, 008, 016, 017** — orphan_exception variants
- **scen_037, 038** — recon_currency_refresh variants
- **scen_043_diag** — diagnostic build of scen_043

### Earlier v2-loop deferrals documented in `SCENARIO_LOG.md`

- **scen_026** — Northstar May MMA
- **scen_049** — Trainee Onboarding (anchored to Elita Moore — design reference for Category 10.1)
- **scen_052** — ASC 842 lease commencement
- **scen_054** — AP recon reversing JE
- **scen_057** — Northstar bookkeeping cleanup partial
- **scen_060** — Halcyon Bridge new-engagement setup (design reference for Category 8.3 onboarding)

---

## Scenario → category mapping (compact index)

| Scenario | Primary cat | Entity |
|----------|:-----------:|--------|
| scen_001 | 7.1 | brookfield |
| scen_005 | 7.1 | brookfield |
| scen_006 | 7.1 | brookfield |
| scen_009 | 7.2 | brookfield |
| scen_010 | 7.2 | brookfield |
| scen_011 | 7.2 | brookfield |
| scen_012 | 7.2 | brookfield |
| scen_013 | 7.1 | northstar_legal |
| scen_014 | 7.1 | northstar_legal |
| scen_015 | 7.1 | northstar_legal |
| scen_018 | 7.1 | acme_cloud |
| scen_019 | 7.2 | brookfield |
| scen_020 | 7.2 | brookfield |
| scen_021 | 7.2 | northstar_legal |
| scen_022 | 7.2 | brookfield |
| scen_023 | 1.1 | brookfield |
| scen_024 | 1.1 | brookfield |
| scen_025 | 1.1 | northstar_legal |
| scen_027 | 1.1 | acme_cloud |
| scen_028 | 1.1 | acme_cloud |
| scen_029–036 | 6.1 | varies |
| scen_039 | 7.4 | northstar_legal |
| scen_040 | 7.4 | brookfield |
| scen_041 | 4.1 | acme_cloud |
| scen_042 | 4.4 | firm-internal |
| scen_043 | 5.1 | northstar_legal |
| scen_044 | 4.5 | firm-internal |
| scen_045 | 3.1 | brookfield |
| scen_046 | 3.3 | acme_cloud |
| scen_047 | 3.4 | northstar_legal |
| scen_048 | 4.6 | brookfield |
| scen_051 | 1.1 | acme_cloud |
| scen_053 | 7.3 | brookfield |
| scen_055 | 7.5 | acme_cloud |
| scen_056 | 1.1 | brookfield |
| scen_058 | 1.3 | northstar_legal |
| scen_059 | 1.4 | brookfield |
| scen_061 | 4.3 | acme_cloud |
| scen_062 | 4.2 | northstar_legal |
| scen_063 | 1.2 | northstar_legal |
| scen_064 | 8.1 | acme_cloud |
| scen_065 | 8.1 | acme_cloud |
| scen_066 | 8.2 | acme_cloud |
| scen_067 | 3.1 | acme_cloud |
| scen_068 | 3.2 | northstar_legal |

---

## Entity coverage

| Entity | Scenarios touching it |
|--------|----------------------:|
| **Brookfield CPAs & Advisors** | 27 |
| **Northstar Legal LLP** | 14 |
| **Acme Cloud Inc** | 15 |
| **Mixed / firm-internal** | ~5 |

---

## Coverage observations for task design

### Where scenarios are dense

- **Category 7 (BlackLine close-discipline):** 19 anchored scenarios (15 orphan-exception + scen_039/040 FX recon + scen_053 variance + scen_055 month-end FX) — overrepresented relative to the 30/10 target. Plenty of study material; rotate personas through different roles when authoring.
- **Category 6 (AP escalation):** eight scenarios, one per template. Complete playbook coverage.
- **Category 1 (Accounting Operations):** ten scenarios — five close (scen_023/024/025/027/028) plus annual accounts (scen_063), quarterly package (scen_058), WIP (scen_059), bad-debt write-off (scen_056), and fixed-asset prepaid (scen_051). A strong study set.
- **Category 4 (Compliance & Internal Controls):** six scenarios spanning wire-flag, soft-flag, BO refresh, quarterly control tests, and state catch-up. Note that **4.7 improper-request refusal is a design surface with no scripted scenario** — the canonical Cat 4.7 framing for prompt authoring is the client CFO asking to move a finished marketing campaign into a prepaid asset (a matching-principle violation), not asking to capitalize marketing as an intangible.

### Where scenarios are thin

- **Category 5 (Audit):** only three scenarios (scen_043, scen_058, scen_063). Budget will draw on these plus design-from-spec.
- **Category 8 (Engagement Mgmt):** only three anchored scenarios (scen_064 → scen_065 → scen_066). Build variants from the chain and from the workflow descriptions.
- **Category 9 (Executive / Partner Oversight):** **no scenarios primarily anchored at the partner level.** Partners appear as endpoint in many scenarios. The firm-state risk pull is unscripted — build from the threshold list in 03_TASK_CATEGORIES §9.2.
- **Category 10 (HR & People Operations):** **zero merged scenarios.** Both anchor candidates (scen_049, scen_060) are deferred. Build from spec, with HR personas as the natural acting voices.

### Notes on derivation

- **Entity field** is the primary client touched by each scenario. Some scenarios cross-reference multiple entities (e.g., scen_062 is internal Brookfield work on a Northstar BO; scen_042 is firm-internal but the recon sample crosses entities).
- **Components list** is the components field declared in each scenario yaml. Communication-only scenarios — the orphan-exception family, AP escalations, AML triage, control tests — use `email + slack + messaging + reminder`. Accounting state-of-record scenarios add `oracle_gl + blackline + sap_subledger + records_vault`.
- **Stage-2 pathology** affects scenarios with non-slack artifact beats (email/airtable/calendar) — the Stage-2 generator sometimes miscoerces them into `DraftSlackArtifact`. The nine partial + ten stage-1 checkpoint yamls (19 total mid-generation files) hit this pattern.