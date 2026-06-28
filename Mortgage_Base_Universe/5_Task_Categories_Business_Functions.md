# Task Categories by Business Function — Keystone Mortgage Partners

## How to Use This Document

This document is a menu for designing evaluation tasks that test an AI agent operating inside a synthetic mortgage brokerage. Each category describes a class of realistic work, the MCP tools an agent would need, the data breadcrumbs ("artifacts") that must exist in the universe for the task to make sense, and a worked example prompt.

**Designing a good eval task:**

1. Pick a category below that matches the business function you want to test.
2. Read the "artifacts to inject" section to understand what scenario data must exist before the agent can attempt the task. If the data doesn't exist yet, you'll need to create a scenario that plants it.
3. Use the example prompt as a template. A strong eval prompt is written in first-person by a specific persona, references concrete entities (loan numbers, people, Slack channels), and requires the agent to read from 3+ MCP servers and write to 2+ servers.
4. Vary difficulty by adjusting how many systems the agent must correlate, whether the "right answer" is ambiguous, and whether the agent must exercise judgment (e.g., deciding whether to escalate vs. resolve directly).

**Difficulty levers:**
- Number of MCP servers involved (3 = moderate, 5+ = hard)
- Ambiguity of the situation (clear instructions vs. "something seems off, investigate")
- Write-action risk (sending an email vs. creating a refund vs. deleting access)
- Time pressure embedded in the narrative (lock expiring tomorrow, closing in 2 days)
- Red herrings in the data (unrelated anomalies the agent should ignore)

**Key mortgage terms used throughout:**

| Term | Meaning |
|------|---------|
| LOS | Loan Origination System -- the central database tracking every loan from application to closing |
| TRID | TILA-RESPA Integrated Disclosure -- federal rules requiring lenders to send a Loan Estimate within 3 business days of application, and a Closing Disclosure at least 3 business days before closing |
| Condition | A document or explanation the lender's underwriter requires before approving the loan (e.g., "provide 2 months of bank statements") |
| CTC | Clear to Close -- the underwriter's final approval, meaning all conditions are satisfied and the loan can proceed to closing |
| Rate lock | A guarantee from the lender that the borrower's interest rate won't change for a set period (typically 30-60 days). If the lock expires before closing, the borrower may face a higher rate or must pay for an extension |
| Pipeline | The set of loans currently in process, tracked by status (application, processing, submitted, approved, CTC, closed) |
| Wholesale lender | The institution that actually funds the loan. Keystone is a broker -- it doesn't lend its own money, it originates loans on behalf of wholesale lenders like UWM, AmeriHome, Caliber, etc. |
| Broker compensation | The fee the wholesale lender pays Keystone when a loan closes, typically 1-2.5% of the loan amount. This is Keystone's revenue. |
| Tolerance cure | A payment the broker must make when actual closing costs exceed the Loan Estimate by more than federal tolerance limits |
| HOI | Homeowner's insurance -- required by the lender before funding. If it falls through before closing, it's an emergency. |
| Trailing docs | Documents due after closing (signed note, recorded deed, final title policy). Lenders/investors won't purchase the loan without them. |

---

## 1. Loan Operations (30% of tasks)

Loan Operations is the engine of the brokerage. Processors manage 15-35 active files each, coordinating between borrowers, loan officers, lender underwriters, title companies, appraisers, and insurance agents. Tasks in this category test the agent's ability to navigate the LOS, cross-reference documents, manage deadlines, and coordinate across parties.

---

### 1.1 Condition Clearing & Pipeline Management

When a wholesale lender's underwriter reviews a loan file, they issue "conditions" -- items the borrower or broker must provide before the loan can be approved. A typical file has 5-15 conditions (bank statements, pay stubs, explanations for large deposits, etc.). Processors track these conditions, request documents from borrowers, verify them, and mark them cleared in the LOS. A stalled condition stalls the entire loan.

**Typical read tools:** `mortgage_los_search_loans`, `mortgage_los_get_loan_by_id` (check pipeline status, see outstanding conditions), `search_emails` / `get_email_threads` (find borrower correspondence about missing docs), `conversations_history` on #loan-processing (processor chatter about stuck files), `filesystem_read_file` (read uploaded borrower documents), `crm_get_deal` (check deal stage vs. LOS status)

**Typical write tools:** `mortgage_los_add_condition` (log new conditions), `mortgage_los_add_activity` (note that a doc was received or a condition cleared), `send_email` (request missing docs from borrower or LO), `conversations_add_message` to #loan-processing (flag a stuck file to the team), `crm_create_engagement` (log borrower interaction)

**Artifacts to inject:**
- A loan in "processing" or "submitted" status with 2-3 outstanding conditions in the LOS
- Email thread between the processor and borrower showing repeated doc requests
- A Slack message in #loan-processing where the processor mentions the file is stuck
- Optionally: a document in filesystem that partially satisfies a condition (e.g., 1 month of bank statements when 2 were required)
- A CRM deal whose stage is out of sync with the LOS status (e.g., deal says "Processing" but loan is actually "Submitted")

**Example prompt:**

> I'm Elena Marchetti, senior processor. I need you to review loan LN-2026-00610 for Sofia Reyes -- she's out sick today and this file has been stuck in underwriting for 8 days. Check the LOS for any outstanding conditions, then look through Sofia's recent emails for correspondence with the borrower about missing documents. There should also be something in #loan-processing from last week where Sofia flagged an issue with a large deposit. Once you understand what's outstanding, email the borrower requesting whatever documents are still needed (cc me and Carlos Rivera, the LO), add an activity note to the loan in the LOS summarizing the current status, and post an update in #loan-processing so the team knows I'm covering this file.

---

### 1.2 Rate Lock Management

A rate lock is a lender's guarantee that the borrower's interest rate won't change for a set period (usually 30-60 days). If the loan doesn't close before the lock expires, the borrower either pays for an extension ($375-$500) or risks a higher rate. Camille Foster manages all locks. Rate lock tasks test the agent's ability to track time-sensitive financial commitments across multiple systems.

**Typical read tools:** `mortgage_los_search_loans` (find loans with locks expiring soon), `mortgage_los_get_loan_by_id` (check lock date, expiration, file status), `search_emails` (find lock confirmation from lender, extension requests), `conversations_history` on #rate-watch (lock strategy discussions), `stripe_list_charges` (check if extension fee was already collected), `quickbooks_search_bills` (check if extension fee was billed)

**Typical write tools:** `send_email` (notify LO and borrower about expiring lock, request extension from lender), `mortgage_los_add_activity` (log lock extension request), `conversations_add_message` to #rate-watch or #loan-processing (alert team), `stripe_create_charge` (collect extension fee from borrower if applicable)

**Artifacts to inject:**
- A loan with a rate lock expiring within 1-3 days and a pipeline status that indicates it won't close in time (e.g., still in "submitted" or "processing")
- Email thread between Camille and the lender about the original lock
- Slack messages in #rate-watch discussing the lock
- Optionally: a prior Stripe charge for a lock extension fee on the same loan (indicating this is a repeat extension)
- A QuickBooks bill for the extension fee from a previous extension on the same loan

**Example prompt:**

> I'm Camille Foster, lock desk. I just pulled the morning lock report and LN-2026-00619 for Carlos Rivera's borrower is expiring in 2 days. The file is still in processing -- there's no way it closes by Thursday. I need you to figure out where the file is stuck by checking the LOS conditions and any recent emails or Slack messages about this loan. Then email Carlos and Sofia Reyes (the processor) with a summary of what needs to happen before I can request an extension from the lender. Also check Stripe and QuickBooks to see if we already charged or billed the borrower for a prior extension on this loan -- if this is a second extension, Carlos needs to have a conversation with the borrower about the additional $500 fee before I submit anything. Post a heads-up in #rate-watch with the loan number, expiration date, and current file status.

---

### 1.3 Closing Coordination

Closing is the final step: the borrower signs documents, funds are wired, and the deed is recorded. In North Carolina, a licensed attorney must conduct the closing. A successful close requires alignment between the borrower, closing attorney, title company, lender (wiring funds), homeowner's insurance provider, and Keystone. If any party is misaligned -- wrong date, missing wire instructions, lapsed insurance policy, unsigned disclosure -- the closing falls through.

**Typical read tools:** `mortgage_los_get_loan_by_id` (check CTC status, closing date, lender), `search_emails` (closing attorney coordination, title company clearance, HOI binder confirmation, wire instructions), `conversations_history` on #closings (last-minute issues), `contacts_search_contacts` (find closing attorney, title officer, insurance agent contact info), `filesystem_read_file` (read closing disclosure PDF, title commitment), `stripe_list_charges` filtered by borrower (verify all pre-closing fees collected)

**Typical write tools:** `send_email` (confirm closing date with all parties, request missing items), `conversations_add_message` to #closings (flag issue or confirm readiness), `mortgage_los_add_activity` (log closing coordination steps), `crm_create_engagement` (log closing confirmation with borrower)

**Artifacts to inject:**
- A loan in "Clear to Close" or late "Approved" status with a closing date 1-3 days away
- Email from the closing attorney (Catherine Grayson or a title company contact) with logistics
- An HOI binder email that's either missing or shows a lapsed policy
- Slack thread in #closings about the upcoming closing
- Contact records for the closing attorney and title officer
- Stripe charges showing pre-closing fees (appraisal, credit report) -- optionally with one charge still pending

**Example prompt:**

> I'm Tyler Washington, closing coordinator. We have a closing scheduled for this Thursday on LN-2026-00613 -- Elena asked me to do a final check that everything is in order. I need you to pull up the loan in the LOS and verify we have Clear to Close status, then check my email for confirmation from Catherine Grayson's office (Grayson & Associates, the closing attorney) and Kevin Tran at Tryon Title. Also verify that the borrower's homeowner's insurance binder is on file -- look in the filesystem for the loan documents folder and in email for anything from South Park Insurance. Check Stripe to make sure we've collected the appraisal fee and credit report fee. If anything is missing or not confirmed, email the responsible party to get it resolved, cc Elena Marchetti, and post a status update in #closings listing what's confirmed and what's still outstanding.

---

### 1.4 Post-Close & QC

After a loan closes, Keith Langford packages the file and delivers "trailing documents" (the signed mortgage note, recorded deed, final title policy) to the investor who purchased the loan. If trailing docs are late or missing, the investor can reject the loan -- forcing Keystone to buy it back, a catastrophic financial event. Raymond Chen audits 10% of closed files for compliance errors. Post-close tasks test attention to detail and regulatory awareness.

**Typical read tools:** `mortgage_los_search_loans` with status "closed" (find recently closed loans), `mortgage_los_get_loan_by_id` (check trailing doc status, investor delivery status), `search_emails` (investor rejection notices, trailing doc requests), `filesystem_list_directory` / `filesystem_read_file` (check post-close file package), `quickbooks_search_invoices` (verify broker compensation was invoiced), `conversations_history` on #compliance-alerts (QC findings)

**Typical write tools:** `send_email` (request trailing docs from title company, respond to investor rejection), `mortgage_los_add_activity` (log delivery status, QC findings), `conversations_add_message` to #compliance-alerts (report QC finding), `filesystem_write_file` (update QC checklist or tracking spreadsheet), `crm_create_engagement` (log post-close issue)

**Artifacts to inject:**
- A recently closed loan (1-4 weeks ago) with incomplete trailing docs in the LOS
- An email from the investor or lender flagging a missing document
- A QC finding email from Raymond Chen identifying a compliance issue (e.g., TRID timing error, missing signature)
- A QuickBooks invoice for broker compensation on the loan
- Filesystem folder with the loan's post-close package, missing one document

**Example prompt:**

> I'm Keith Langford, post-closer. I got an email from AmeriHome this morning saying they're rejecting delivery of loan LN-2026-00628 because we're missing the final title policy and the recorded deed. This loan closed 3 weeks ago. I need you to check the LOS for the loan details and see what trailing docs are logged as outstanding, then search my email for anything from Tryon Title or Piedmont Settlement about this file -- they should have sent the recorded deed by now. Also check if Raymond Chen flagged anything on this file during his QC review (look in #compliance-alerts and his recent emails). Once you know what's missing, email the title company requesting the documents with a 48-hour deadline, add a note in the LOS that delivery was rejected and why, and post in #compliance-alerts tagging this as an investor rejection so Denise Holloway is aware.

---

## 2. Compliance & Risk (20% of tasks)

Compliance tasks are high-stakes: regulatory violations can result in fines, license revocation, or lawsuits. Denise Holloway (compliance officer) and Raymond Chen (QC analyst) are the primary actors. These tasks test the agent's ability to investigate across systems, identify patterns, apply regulatory knowledge, and take careful action.

---

### 2.1 TRID & Disclosure Tracking

TRID (TILA-RESPA Integrated Disclosure) is a set of federal rules with hard deadlines: the Loan Estimate must be sent within 3 business days of application, and the Closing Disclosure must be sent at least 3 business days before closing. If a disclosure is late, the closing must be delayed. If fees on the Closing Disclosure exceed the Loan Estimate beyond tolerance limits, Keystone may owe the borrower a "tolerance cure" -- a payment from the broker's pocket.

**Typical read tools:** `mortgage_los_search_loans` (find loans approaching disclosure deadlines), `mortgage_los_get_loan_by_id` (check disclosure dates, application date, closing date), `search_emails` (find disclosure delivery confirmations from Nadia Osman), `filesystem_read_file` (read Loan Estimate or Closing Disclosure PDFs), `quickbooks_search_bills` (check for tolerance cure payments), `conversations_history` on #compliance-alerts

**Typical write tools:** `send_email` (notify Nadia/processors about deadline, escalate violation to Denise), `mortgage_los_add_activity` (log disclosure issue), `conversations_add_message` to #compliance-alerts (flag TRID violation), `crm_create_engagement` (log borrower notification if closing must be delayed), `quickbooks_create_bill` (log tolerance cure if owed)

**Artifacts to inject:**
- A loan where the application date + 3 business days is approaching or past, and no Loan Estimate delivery is logged
- OR: a loan closing in 1-3 days where the Closing Disclosure was sent late (less than 3 business days before closing)
- Email from Nadia Osman about the disclosure (sent or not sent)
- A Closing Disclosure PDF in the filesystem with fees that don't match the Loan Estimate
- Slack discussion in #compliance-alerts about TRID timing

**Example prompt:**

> I'm Denise Holloway, compliance officer. Grace just flagged that loan LN-2026-00603 might have a TRID violation -- the Closing Disclosure may have been delivered less than 3 business days before the scheduled closing. I need a thorough investigation. Pull up the loan in the LOS and find the exact dates: application date, Loan Estimate sent date, Closing Disclosure sent date, and scheduled closing date. Then check Nadia Osman's emails for the disclosure delivery confirmation (she always emails the borrower with disclosures attached). Also look in the filesystem for the actual Closing Disclosure PDF and compare the fees against the Loan Estimate to see if we have any tolerance issues. If there is a TRID violation, email Grace Yamamoto and Robert Calloway with a summary including the exact dates and the regulatory requirement, add a compliance note to the loan in the LOS, and post a finding in #compliance-alerts. If the closing needs to be delayed, also email the LO and processor assigned to this loan.

---

### 2.2 Suspicious Activity Investigation

Mortgage fraud takes many forms: wire fraud (spoofed closing wire instructions), identity fraud (borrower is not who they claim), income fraud (inflated pay stubs), appraisal fraud (inflated valuations to support higher loan amounts), and occupancy fraud (borrower says they'll live there but intends to rent it out). Investigating fraud requires correlating data across every system -- emails, LOS records, Stripe payments, CRM notes, filesystem documents, and Slack conversations.

**Typical read tools:** `mortgage_los_get_loan_by_id` (loan details, borrower info), `mortgage_los_get_borrower_by_id` (income, employment, credit), `search_emails` (suspicious correspondence, wire instructions, identity docs), `stripe_list_charges` / `stripe_list_identity_verifications` (payment anomalies, identity check results), `stripe_list_fc_transactions` (bank transaction history for unexplained deposits), `filesystem_read_file` (borrower documents -- tax returns, bank statements, pay stubs), `crm_get_contact` / `crm_get_lead` (prior interaction history), `conversations_search_messages` (internal discussions about the borrower)

**Typical write tools:** `send_email` (escalate to Denise/Robert, notify lender if required), `conversations_add_message` to #compliance-alerts (flag finding), `mortgage_los_add_activity` (log investigation notes), `crm_create_engagement` (document investigation), `filesystem_write_file` (write investigation summary report)

**Artifacts to inject:**
- A loan with suspicious indicators: income on application doesn't match tax transcript, unexplained large deposit on bank statement, or identity verification flags
- Stripe Financial Connections transaction data showing anomalous deposits
- Emails containing wire instructions that don't match the title company's known account
- A borrower document (W-2, pay stub, bank statement) in the filesystem with inconsistencies
- CRM engagement notes from the LO about borrower behavior
- Slack messages where someone raised a concern about the file

**Example prompt:**

> I'm Denise Holloway, compliance officer. Raymond Chen just flagged something concerning during his QC review of loan LN-2026-00610. The borrower's bank statements show a $14,000 cash deposit two weeks before application with no explanation. I need a full investigation. Pull the loan and borrower details from the LOS, including income, employment, and credit data. Check the Stripe Financial Connections data for this borrower's linked bank account -- look at all transactions around the deposit date for patterns. Read the bank statement PDF from the filesystem and cross-reference it against the LOS application data. Search emails between the LO (Carlos Rivera), the processor (Sofia Reyes), and the borrower for any discussion about this deposit. Also check if the lender has already issued a condition for a letter of explanation. Document your findings in a report: write a summary file to the filesystem at `compliance/investigation_LN-2026-00610.txt`, add an investigation note to the loan in the LOS, and email me and Robert Calloway with a recommendation on whether to proceed, request more documentation, or escalate to the lender's fraud department.

---

### 2.3 QC Audit & Remediation

Raymond Chen reviews 10% of closed loan files. He checks that disclosures were timely, conditions were properly cleared (with actual supporting documents, not just marked "done"), fees match between the Loan Estimate and Closing Disclosure, and HMDA data is accurate. When he finds errors, the team must remediate -- sometimes by re-sending corrected disclosures, sometimes by issuing tolerance cure refunds, sometimes by retraining staff.

**Typical read tools:** `mortgage_los_search_loans` with status "closed" (select files for audit), `mortgage_los_get_loan_by_id` (full file review -- conditions, disclosures, dates), `filesystem_read_file` (read disclosures, condition documents, closing package), `search_emails` (processor/LO correspondence about conditions), `quickbooks_search_invoices` (verify compensation amounts), `stripe_list_charges` (verify fees collected match what was disclosed), `conversations_history` on #compliance-alerts (prior findings)

**Typical write tools:** `send_email` (notify processor/LO of finding, escalate to Denise), `mortgage_los_add_activity` (log QC finding against the loan), `conversations_add_message` to #compliance-alerts (report finding), `filesystem_write_file` (write QC audit report), `quickbooks_create_bill` (log tolerance cure if applicable)

**Artifacts to inject:**
- 2-3 recently closed loans, at least one with a QC-detectable error (condition cleared without a supporting document, fee discrepancy between LE and CD, late disclosure)
- Filesystem containing the loan documents (disclosures, condition docs, signed closing package)
- Stripe charges for the loans' fees
- QuickBooks invoices for broker compensation
- Email from Raymond Chen to the team about his findings

**Example prompt:**

> I'm Raymond Chen, QC analyst. I'm running my monthly audit and I've selected three recently closed loans to review: LN-2026-00211, LN-2026-00224, and LN-2026-00603. For each loan, I need you to pull the full file from the LOS -- check all conditions and whether they have supporting documentation, verify the disclosure dates against TRID timelines (LE within 3 business days of application, CD at least 3 business days before closing), and compare the fees on the Closing Disclosure against the original Loan Estimate. Check the filesystem for the actual disclosure PDFs and condition documents. Cross-reference the Stripe charges for these borrowers to make sure what was charged matches what was disclosed. For any findings, create a QC report file in the filesystem at `compliance/qc_audit_march_2026.txt` with the loan number, finding, severity (critical/major/minor), and recommended corrective action. Then email Denise Holloway and Grace Yamamoto with a summary, and post the finding count in #compliance-alerts.

---

### 2.4 Security Incident Response

Security incidents at a mortgage brokerage are especially dangerous because the company handles sensitive PII (Social Security numbers, bank account numbers, tax returns) and large wire transfers. Incidents range from phishing attacks that compromise lender portal credentials to ransomware that locks the LOS to unauthorized data access by employees or interns.

**Typical read tools:** `search_emails` (phishing emails, suspicious messages, breach notifications), `conversations_history` on #it-support and #compliance-alerts (incident reports), `mortgage_los_list_staff` (check who has system access), `filesystem_read_file` (access logs, security audit reports), `contacts_search_contacts` (identify affected parties), `crm_get_contact` (check for affected borrowers), `stripe_list_identity_verifications` (check if identity checks were compromised)

**Typical write tools:** `send_email` (notify affected borrowers, alert lenders, coordinate with Raj), `conversations_add_message` to #it-support and #compliance-alerts (incident updates), `filesystem_write_file` (write incident report), `mortgage_los_add_activity` (log access-related notes on affected loans), `contacts_edit_contact` (update contact info if compromised)

**Artifacts to inject:**
- A phishing email in someone's inbox (or a forwarded phishing email to #it-support)
- Filesystem access logs showing unauthorized access patterns
- Slack messages in #it-support describing the incident
- LOS staff list showing who has active access (including people who shouldn't)
- CRM contacts for affected borrowers who need to be notified
- Email from Raj Anand about system changes or vulnerability findings

**Example prompt:**

> I'm Grace Yamamoto, Director of Ops. Raj Anand just called me -- he found evidence that Keisha Williams clicked a phishing link yesterday that may have compromised her lender portal credentials. She has active sessions with UWM, AmeriHome, and Caliber. I need you to investigate the scope immediately. Search Keisha's email for the phishing message and any suspicious emails sent from her account in the last 24 hours. Check #it-support for anything Raj has posted about this. Pull the LOS staff list to confirm which systems Keisha has access to, and search the LOS for all loans currently assigned to her -- those borrowers' SSNs and financial data may be exposed. Write an incident report to the filesystem at `compliance/incident_keisha_phishing_2026-03.txt` covering what happened, what data may be compromised, and recommended next steps. Email Robert Calloway and Denise Holloway with an urgent summary, and post an alert in #compliance-alerts telling the team not to click any links from Keisha's account until further notice.

---

## 3. Sales & Client Relations (20% of tasks)

Sales tasks test the agent's ability to manage relationships, communicate diplomatically, and juggle CRM data with email outreach. Client relations tasks involve de-escalation, reputation management, and cross-system investigation into what went wrong.

---

### 3.1 Lead Management & Outreach

Keystone generates leads from realtor referrals, Zillow/LendingTree online ads, open houses, and walk-ins. Leads enter the CRM and are assigned to loan officers. Many leads go stale -- contacted once, never followed up. Effective lead management requires understanding the lead's needs, checking if they've already been contacted, and crafting personalized outreach.

**Typical read tools:** `crm_get_lead` / `crm_search_leads` (find stale leads, check status/rating/source), `crm_get_contact` (check if lead has an existing contact record), `search_emails` (prior outreach attempts), `conversations_history` on #sales-pipeline (LO discussions about leads), `mortgage_los_search_borrowers` (check if lead already has an application), `contacts_search_contacts` (find the referring realtor's contact info)

**Typical write tools:** `send_email` (personalized outreach to lead), `crm_create_engagement` (log the outreach), `crm_update_lead` (update status from "new" to "contacted"), `conversations_add_message` to #sales-pipeline (report on outreach batch), `contacts_add_new_contact` (create contact record if lead converts)

**Artifacts to inject:**
- 5-10 CRM leads in "new" or "contacted" status that are 2+ weeks old
- Lead notes describing what the person is looking for ("FHA in Ballantyne, pre-approval needed by end of month")
- Email records showing one prior outreach attempt with no reply
- A Slack message in #sales-pipeline where the BD manager asks about lead follow-up
- Optionally: a referring realtor in the contacts database linked to some of these leads

**Example prompt:**

> I'm Jordan Blake, BD manager. I just reviewed our lead pipeline and we have 23 leads in "contacted" status that haven't been touched in over 2 weeks -- that's money walking out the door. I need you to pull all leads from the CRM with status "contacted" and a last-activity date older than 14 days. For the top 5 by rating (prioritize "hot" leads), check if there's an existing email thread with the lead, look up whether they're already in the LOS as a borrower, and find the referring realtor if one is listed in the lead source. For each of these 5 leads, send a personalized follow-up email from the assigned LO (use their name and reference what the lead was looking for from the CRM notes). Log each outreach as an engagement in the CRM, update the lead status to "contacted" with today's date, and post a summary in #sales-pipeline listing the 5 leads you reached out to, their assigned LOs, and what you said.

---

### 3.2 Referral Partner Management

Realtors are Keystone's primary lead source. Jordan Blake manages 40+ referral partners. Healthy partnerships require regular check-ins, deal flow tracking, and quick resolution of any friction (a loan that closed late, a borrower who complained, a realtor who stopped sending referrals).

**Typical read tools:** `crm_search_contacts` / `crm_get_company` (find realtor contacts and their firm), `crm_search_deals` (deals sourced from a specific realtor), `crm_search_leads` (leads from a specific realtor), `search_emails` (correspondence with the realtor), `mortgage_los_search_loans` (loans where the realtor was involved), `conversations_history` on #sales-pipeline (discussions about partner relationships), `quickbooks_search_invoices` (revenue from deals sourced by this partner)

**Typical write tools:** `send_email` (check-in email to realtor, thank-you for referral), `crm_create_engagement` (log partner touchpoint), `conversations_add_message` to #sales-pipeline (report on partner health), `crm_update_contact` (update realtor's notes)

**Artifacts to inject:**
- CRM company records for referral partner firms (Queen City Realty, Fairview Homes, etc.)
- Contact records for key realtors (Jason Park, Stephanie Boyd, Brian Foster, Monique Tate)
- Deals in the CRM sourced from these realtors
- Email threads between LOs and realtors
- A Slack thread in #sales-pipeline about a realtor who's gone quiet

**Example prompt:**

> I'm Jordan Blake, BD manager. Jason Park at Coldwell Banker has been our top referral source for two years -- usually 3-4 deals a month. But looking at the CRM, I only see one deal from him in the last 6 weeks. I need you to dig into this. Pull Jason Park's contact record from the CRM, then search for all deals and leads sourced from him in the last 90 days. Check email for recent correspondence between Jason and any of our LOs -- see if there's been a problem (a loan that went sideways, a complaint, a missed closing date). Look up any loans in the LOS that were Jason's referrals and check their status -- did any recently get denied or delayed? Also check QuickBooks to see the revenue we've generated from his referrals this quarter vs. last quarter. Based on what you find, draft a personal email from me to Jason acknowledging the relationship and asking if there's anything we can do better, and log this as an engagement in the CRM. Post a summary of your findings in #sales-pipeline so the team is aware.

---

### 3.3 Complaint Resolution & Reputation Management

When a borrower has a bad experience -- denied loan, closing delay, rude service, misunderstanding -- they may escalate through a variety of channels: angry email, phone call, Google review, social media post, or even a discrimination complaint. Resolving complaints requires understanding what happened (reading the loan file, emails, internal communications), empathizing with the borrower, and taking concrete action.

**Typical read tools:** `search_emails` (borrower complaint email, internal discussion about the complaint), `mortgage_los_get_loan_by_id` (what happened with the loan), `crm_get_contact` / `crm_get_deal` (relationship history), `conversations_search_messages` (internal Slack discussion about the complaint), `stripe_list_charges` (refund eligibility -- did we overcharge?), `filesystem_read_file` (review letter if filed formally, or a screenshot of the social media post)

**Typical write tools:** `send_email` (respond to borrower, coordinate with LO/processor), `crm_create_engagement` (log complaint and resolution), `conversations_add_message` to relevant channel (alert leadership), `mortgage_los_add_activity` (note complaint on the loan), `stripe_create_refund` (refund overcharged fee if applicable)

**Artifacts to inject:**
- An angry borrower email or a formal complaint document in the filesystem
- The loan record in the LOS showing what happened (denial, delay, fee issue)
- CRM contact/deal records for the borrower
- Internal email or Slack thread where staff discussed the situation
- Optionally: a Stripe charge that should be refunded
- Optionally: a Google review or social media post (as a filesystem document or email forwarding it)

**Example prompt:**

> I'm Jasmine Brooks, client relations. Robert Calloway just forwarded me an email from a borrower named Marcus Thompson -- he's furious that his loan LN-2026-00624 was denied after 45 days in process, and he's threatening to post a detailed 1-star Google review today. He says Keisha Williams told him he was "guaranteed to be approved" during the initial consultation. I need you to investigate. Pull the loan from the LOS to understand why it was denied. Search emails between Keisha, the processor, and the borrower for any communication where expectations were set. Check the CRM for all engagements logged on this deal. Look at Stripe to see what fees were collected -- if we charged an appraisal fee and application deposit, we may need to refund the deposit since the loan was denied. Draft a compassionate but professional response email from me to Marcus acknowledging his frustration, explaining (in plain language) why the loan couldn't be approved, and letting him know we're refunding his application deposit. If a Stripe refund is warranted, process it. Add a detailed engagement note to the CRM, and email Robert and Keisha with a summary of what happened and the refund.

---

### 3.4 Retention & Refinance Outreach

Tomas Herrera manages post-close relationships. When interest rates drop or a borrower's closing anniversary approaches, there may be an opportunity to refinance -- generating new revenue from an existing client. This requires identifying eligible borrowers, checking their current loan terms, and crafting outreach that's helpful rather than pushy.

**Typical read tools:** `mortgage_los_search_loans` with status "closed" (find past borrowers), `mortgage_los_get_loan_by_id` (check current rate, loan amount, close date), `crm_get_contact` (relationship history), `crm_search_deals` (prior deals with this borrower), `search_emails` (prior post-close communication), `contacts_search_contacts` (current contact info), `conversations_history` on #rate-watch (current rate environment discussion)

**Typical write tools:** `send_email` (personalized refinance outreach), `crm_create_engagement` (log outreach), `crm_create_lead` (create a refi lead in the pipeline), `conversations_add_message` to #sales-pipeline (report on refi opportunities)

**Artifacts to inject:**
- Closed loans with rates meaningfully above current market (50+ basis points)
- CRM contact records for past borrowers
- A Slack thread in #rate-watch noting that rates have dropped
- Prior post-close check-in emails from Tomas
- Optionally: a borrower who recently inquired about refinancing (email or CRM engagement)

**Example prompt:**

> I'm Tomas Herrera, retention specialist. Rates just dropped 50 basis points this week and Camille posted about it in #rate-watch. I want to identify past borrowers who closed conventional loans at 7.25% or higher in the last 12 months -- they could save significantly by refinancing. Search the LOS for closed conventional loans with rates at or above 7.25% and close dates within the last year. For each match, pull the borrower's contact info from the contacts database and check the CRM for any recent interactions (I don't want to email someone who's already in a refi conversation). For the top 5 candidates by loan amount (bigger loans = bigger savings), send a personalized email from me explaining the rate environment and what they could save monthly, create a new "refinance" lead in the CRM for each one, and post a summary in #sales-pipeline with the borrower names, original rates, loan amounts, and estimated monthly savings at today's rate.

---

## 4. Finance & Accounting (15% of tasks)

Finance tasks test the agent's ability to reconcile numbers across systems: LOS (what loans closed), Stripe (what was charged), QuickBooks (what was invoiced/billed), and email (lender compensation statements). Hana Kim and Victor Osei are the primary actors.

---

### 4.1 Commission Reconciliation

When a loan closes, the wholesale lender pays Keystone a broker compensation fee (typically 1-2.5% of the loan amount). Hana Kim must verify that the lender's payment matches what was expected based on the loan amount and comp rate. Discrepancies happen: lenders miscalculate, apply the wrong comp rate, or deduct fees. This requires cross-referencing the LOS (loan amount, lender, comp rate) with QuickBooks (invoiced amount, payment received) and email (lender compensation statements).

**Typical read tools:** `mortgage_los_search_loans` with status "closed" (find recently closed loans), `mortgage_los_get_loan_by_id` (loan amount, lender, comp rate), `quickbooks_search_invoices` (broker compensation invoices), `quickbooks_search_customers` (match QB customer to LOS borrower), `search_emails` (lender compensation statements, payment confirmations), `stripe_list_transfers` (if lender pays via Stripe connected account)

**Typical write tools:** `send_email` (dispute email to lender, summary to Robert/Grace), `quickbooks_create_invoice` (create missing compensation invoice), `mortgage_los_add_activity` (log compensation discrepancy), `conversations_add_message` to #general or a finance channel (flag discrepancy)

**Artifacts to inject:**
- Recently closed loans with known comp rates in the LOS
- QuickBooks invoices for broker compensation -- at least one with a discrepancy vs. expected amount
- An email from a lender with a compensation statement or payment remittance
- Optionally: a Stripe transfer from a lender connected account that doesn't match the invoice
- A loan where no compensation invoice exists in QuickBooks (missed billing)

**Example prompt:**

> I'm Hana Kim, bookkeeper. I just received the monthly compensation statement from UWM (check my email -- they send it around the 5th of each month) and some numbers don't look right. I need you to pull all loans in the LOS that closed with UWM as the lender in the last 30 days, then compare each loan's expected compensation (loan amount times the comp rate) against the corresponding QuickBooks invoice amount. Also check if there are any closed UWM loans that don't have a QuickBooks invoice at all -- those are missed billings. For any discrepancies over $100, compile a list showing the loan number, borrower name, expected comp, invoiced amount, and the difference. Email Victor Osei and Grace Yamamoto with the reconciliation summary, create QuickBooks invoices for any missed loans, and add an activity note in the LOS on each discrepant loan flagging the comp issue.

---

### 4.2 Fee & Vendor Audit

Keystone pays vendors for per-loan services: appraisal firms ($350-$750), credit report provider ($25-$85), and title companies (varies). These fees are collected from borrowers via Stripe and paid to vendors as QuickBooks bills. A fee audit checks that what Keystone charged the borrower matches what the vendor charged Keystone, and that no vendor is systematically overcharging.

**Typical read tools:** `stripe_list_charges` (fees collected from borrowers, filter by metadata), `stripe_list_connected_accounts` (vendor accounts), `stripe_list_transfers` (payments to vendors), `quickbooks_search_bills` (vendor bills), `quickbooks_search_vendors` (vendor details), `mortgage_los_search_loans` (loan details to cross-reference), `search_emails` (vendor invoices, fee disputes)

**Typical write tools:** `send_email` (dispute email to vendor, summary to management), `quickbooks_create_bill` (correct a miscategorized bill), `conversations_add_message` to #general (flag vendor pricing concern), `filesystem_write_file` (write audit report)

**Artifacts to inject:**
- Stripe charges for appraisal fees, credit report fees, and application deposits across multiple loans
- QuickBooks bills from appraisal firms, title companies, and CoreLogic Credco
- At least one vendor (e.g., Ballantyne Appraisal) with bills consistently $100-$150 higher than other vendors for the same service
- Stripe transfers to vendor connected accounts
- Email from a vendor with an invoice that doesn't match the QB bill

**Example prompt:**

> I'm Victor Osei, financial analyst. Grace asked me to investigate whether Ballantyne Appraisal Services is overcharging us. I've heard anecdotal complaints from processors. I need you to pull all QuickBooks bills from Ballantyne Appraisal, DeLuca Appraisal, and Carolina Appraisal Group for the last 6 months and compare their average per-appraisal cost. Then check Stripe for charges tagged as appraisal fees -- compare what we charged borrowers against what each vendor billed us. For any loan where Ballantyne's bill exceeded the Stripe charge to the borrower (meaning Keystone ate the difference), flag it. Cross-reference 5-10 of Ballantyne's bills against the loan details in the LOS to see if higher fees correlate with property type, loan amount, or location. Write an analysis to the filesystem at `reports/appraisal_vendor_audit_2026_Q1.txt` with your findings, average costs by vendor, and a recommendation. Email Grace and Robert with the summary, and post a heads-up in #loan-processing that processors should be aware of the pricing variance.

---

### 4.3 Financial Reporting

Victor Osei produces monthly P&L reports and production summaries for Robert Calloway. This requires aggregating data from QuickBooks (revenue and expenses), the LOS (loan volume, LO production), and Stripe (fee collection). The agent must synthesize numbers from multiple systems into a coherent narrative.

**Typical read tools:** `quickbooks_search_invoices` (revenue), `quickbooks_search_bills` (expenses), `quickbooks_search_accounts` (account balances), `quickbooks_show_data` (summary views), `mortgage_los_get_pipeline_summary` (loan volume, status breakdown), `mortgage_los_search_loans` (production by LO, by loan type), `stripe_list_charges` (fee revenue), `stripe_list_refunds` (refund volume), `conversations_history` on #rate-watch (market context)

**Typical write tools:** `filesystem_write_file` (write report), `send_email` (deliver report to Robert/Grace), `conversations_add_message` to #general (share highlights with team)

**Artifacts to inject:**
- QuickBooks invoices (broker compensation) and bills (expenses) spanning at least 2-3 months
- A meaningful mix of loan types and statuses in the LOS
- Stripe charges and refunds for the reporting period
- Prior monthly reports in the filesystem (for comparison/trend analysis)

**Example prompt:**

> I'm Victor Osei, financial analyst. It's the first week of the month and Robert needs the March production report. I need you to compile the following: (1) total broker compensation revenue from QuickBooks invoices closed in March, (2) total operating expenses from QuickBooks bills paid in March, broken out by category (appraisals, credit reports, title, software, rent, marketing, payroll, other), (3) number of loans closed in March from the LOS, broken out by loan type and assigned LO, (4) total fees collected and refunds issued via Stripe in March. Pull the pipeline summary from the LOS for current active loan count. Compare March revenue to the prior 2 months from QuickBooks to identify the trend. Write the report to the filesystem at `reports/monthly_production_march_2026.txt` and email it to Robert Calloway and Grace Yamamoto. Include a 3-line executive summary at the top highlighting the most important takeaway.

---

## 5. Executive (10% of tasks)

Executive tasks test the agent's ability to synthesize information across the entire organization, identify patterns, and present recommendations. Robert Calloway (owner) and Grace Yamamoto (Director of Ops) are the primary requestors. These tasks require reading from nearly every MCP server.

---

### 5.1 Cross-Functional Risk Assessment

Robert periodically asks for a "state of the business" risk assessment: are there compliance exposures? Stalled loans? Unhappy borrowers? Vendor problems? Financial irregularities? The agent must scan every system and surface the most important issues.

**Typical read tools:** `mortgage_los_get_pipeline_summary` (overall pipeline health), `mortgage_los_search_loans` (find stalled or at-risk loans), `conversations_search_messages` (search Slack for "escalation", "urgent", "risk", "violation"), `search_emails` (complaints, lender warnings, regulatory notices), `quickbooks_search_bills` (overdue bills, unusual expenses), `stripe_list_disputes` (payment disputes), `crm_search_deals` (stalled deals), `filesystem_list_directory` on compliance folder (recent incident reports)

**Typical write tools:** `filesystem_write_file` (write risk assessment report), `send_email` (deliver report to Robert with action items), `conversations_add_message` to #general (share key findings with leadership)

**Artifacts to inject:**
- A mix of issues across systems: a stalled loan in the LOS, an overdue QB bill, a Stripe dispute, a compliance finding in the filesystem, a Slack thread about a problem
- No single artifact is the "answer" -- the agent must aggregate and prioritize

**Example prompt:**

> I'm Robert Calloway, owner. I'm preparing for our quarterly board review and I need a comprehensive risk assessment across the company. Scan the LOS pipeline for any loans that have been in "processing" or "submitted" status for more than 45 days -- those are at risk of expiring rate locks or losing borrowers. Check QuickBooks for any vendor bills more than 60 days overdue. Search Slack across all channels for messages containing "urgent," "violation," "escalation," or "risk" from the last 30 days. Check Stripe for any open disputes or unusual refund activity. Look in the filesystem under the compliance folder for any recent incident reports or QC findings. Search email for any correspondence from lenders flagging issues with our files. Compile everything into a risk assessment document at `reports/quarterly_risk_assessment_Q1_2026.txt` organized by severity (critical, high, medium, low) with a recommended action for each item. Email it to me and Grace, and post a brief summary in #general noting how many issues were found by severity level.

---

### 5.2 LO Performance Review

Grace Yamamoto tracks loan officer performance: pipeline volume, conversion rate (applications to closings), average days to close, pull-through rate (locked loans that actually close), and revenue per LO. Underperformance may indicate coaching needs, personal issues, or market shifts.

**Typical read tools:** `mortgage_los_get_pipeline` (all loans by LO), `mortgage_los_search_loans` (closed/denied/withdrawn by LO, date ranges), `crm_search_deals` (deal conversion by LO), `crm_search_leads` (leads assigned by LO), `quickbooks_search_invoices` (revenue by LO's closed loans), `search_emails` (borrower complaints about specific LOs), `conversations_history` on #loan-processing and #sales-pipeline (team discussions about LO performance)

**Typical write tools:** `filesystem_write_file` (write performance report), `send_email` (deliver report to Robert, schedule coaching if needed), `conversations_add_message` to #general (share team-level metrics)

**Artifacts to inject:**
- A meaningful volume of loans in the LOS assigned to each LO (a mix of closed, active, denied, withdrawn)
- CRM deals at various stages per LO
- QuickBooks invoices for broker compensation (linked to loans/LOs)
- Optionally: an LO with notably poor metrics (Carlos Rivera with a 60-day dry spell, Amy Chen with declining production)
- Internal Slack or email discussion about LO performance concerns

**Example prompt:**

> I'm Grace Yamamoto, Director of Ops. I need a production scorecard for all 8 loan officers covering the last 90 days. For each LO, pull from the LOS: total active loans, loans closed, loans denied or withdrawn, and average days from application to closing. From the CRM, get each LO's lead-to-deal conversion rate (leads assigned to them that converted to deals). From QuickBooks, calculate total broker compensation revenue per LO. Flag any LO who has zero closings in the last 60 days or whose denial rate exceeds 20%. I know Carlos Rivera has been struggling -- pay special attention to his pipeline and see if his loans are stalled at a particular stage. Write the full scorecard to `reports/lo_scorecard_Q1_2026.txt` with a table format, and email it to me and Robert Calloway. Include a brief narrative for any LO who's significantly above or below the team average, with a recommended action (coaching, pipeline review, recognition, etc.).

---

### 5.3 Strategic Account & Vendor Review

Robert and Grace periodically review vendor costs and lender relationships to make strategic decisions: should Keystone drop a vendor, renegotiate terms, or add a new wholesale lender? This requires analyzing spending patterns, service quality, and revenue contribution.

**Typical read tools:** `quickbooks_search_bills` (vendor spending by vendor, category, date range), `quickbooks_search_vendors` (vendor details), `quickbooks_search_invoices` (revenue by lender), `mortgage_los_search_loans` (loan volume by lender), `stripe_list_transfers` (vendor payments via Stripe), `stripe_list_connected_accounts` (vendor accounts), `search_emails` (vendor negotiations, lender account rep correspondence), `crm_get_company` (lender relationship details)

**Typical write tools:** `filesystem_write_file` (write analysis report), `send_email` (share findings with Robert/Grace, request updated pricing from vendor), `conversations_add_message` (share strategic insight)

**Artifacts to inject:**
- QuickBooks bills from multiple vendors over 6+ months
- Invoices showing revenue by lender
- LOS loans showing volume and close rates by lender
- Stripe connected accounts and transfers for vendor payments
- CRM company records for lenders and vendors
- Email correspondence with vendor/lender account reps

**Example prompt:**

> I'm Robert Calloway, owner. I want to evaluate our vendor relationships for the annual budget review. Pull all QuickBooks bills for the last 6 months and break down total spending by vendor. Compare our three appraisal firms (DeLuca, Carolina Appraisal Group, Ballantyne Appraisal) on cost per appraisal and volume. Check Stripe transfers to each appraisal vendor's connected account to cross-reference against what QuickBooks shows. Then look at our wholesale lender relationships: for each lender in the LOS, how many loans did we close with them in the last 6 months, and what was the total broker compensation (from QuickBooks invoices)? Check email for any pricing updates or compensation changes from our lender account reps (UWM, AmeriHome, Caliber especially). Write a vendor and lender review to `reports/vendor_lender_review_2026.txt` that includes a spending summary, a cost comparison across similar vendors, revenue per lender, and my top 3 recommended actions (renegotiate, drop, add). Email it to me and Grace.

---

## 6. IT & Security (5% of tasks)

IT tasks at Keystone are primarily handled by Raj Anand, a part-time contractor (2 days/week). This means problems often sit for days before being addressed, and the agent must sometimes act as a first responder. Tasks focus on access management and incident response.

---

### 6.1 System Administration

Access management is critical at a mortgage brokerage: every employee needs appropriate system access (LOS, email, CRM, Slack), and departing employees must be promptly de-provisioned. Raj also handles onboarding (new hires get LOS accounts, email, Slack access) and routine admin (password resets, permission changes).

**Typical read tools:** `mortgage_los_list_staff` (current system users), `search_emails` (access requests, HR notifications about departures), `conversations_history` on #it-support (access requests, complaints), `contacts_search_contacts` (employee contact info), `filesystem_read_file` (access logs, security reports)

**Typical write tools:** `send_email` (confirm access changes, notify HR/compliance), `conversations_add_message` to #it-support (confirm completion), `filesystem_write_file` (update access log or onboarding checklist), `mortgage_los_add_activity` (log access change against relevant loans if applicable)

**Artifacts to inject:**
- LOS staff list including someone who shouldn't have access (departed employee, intern with too many permissions)
- An email or Slack message requesting access changes (new hire, departure, permission change)
- Filesystem containing an access log or security audit showing anomalies
- An HR notification email about an employee departure

**Example prompt:**

> I'm Raj Anand, IT. Grace Yamamoto just sent me an email saying Marcus Webb gave his two-week notice and his last day is Friday. I need to prepare the offboarding checklist. Check the LOS staff list for all of Marcus's current system access. Search email for any shared credentials or system logins that mention Marcus. Also check #it-support for any recent access requests he's made. Look in the filesystem for our offboarding checklist template. I need you to identify every system Marcus has access to, write an offboarding plan to `it/offboarding_marcus_webb.txt` listing each system and the deactivation steps, email Grace and Denise Holloway confirming the plan and asking Grace to confirm his exact last day, and post in #it-support that Marcus's accounts will be deactivated at COB on his last day. Also flag in the email to Grace that we need to reassign his active LOS loans before we disable his account.

---

### 6.2 Incident Response

IT incidents at a small brokerage are high-impact: if the LOS goes down, no one can process loans. If email is compromised, wire fraud risk spikes. Raj is only on-site 2 days a week, so incidents often start with someone posting in #it-support and waiting. The agent must triage, contain, communicate, and remediate.

**Typical read tools:** `conversations_history` on #it-support (incident reports, symptoms), `search_emails` (vendor support tickets, system alerts), `mortgage_los_list_staff` (who's affected), `filesystem_read_file` (error logs, system status files), `contacts_search_contacts` (vendor support contacts), `mortgage_los_get_pipeline` (assess impact -- how many active loans are affected)

**Typical write tools:** `conversations_add_message` to #it-support and #general (status updates), `send_email` (contact vendor support, notify management), `filesystem_write_file` (write incident report, document workaround), `mortgage_los_add_activity` (log impact on affected loans)

**Artifacts to inject:**
- Slack messages in #it-support reporting the incident (multiple employees describing symptoms)
- Email from the LOS vendor (ICE Mortgage Technology) or another vendor about the issue
- System log files in the filesystem showing errors
- A pipeline of active loans that would be impacted by the outage

**Example prompt:**

> I'm Raj Anand, IT. I just woke up to 12 messages in #it-support -- the LOS has been down since 6 AM and nobody can access loan files. Elena Marchetti says she has 3 files due to lenders today and Camille Foster can't process rate locks. I need you to check #it-support for all the messages about this outage and compile the symptoms. Search my email for any notifications from ICE Mortgage Technology (our LOS vendor) about scheduled maintenance or known issues. Check the filesystem for any recent error logs under the `it/` directory. Pull the LOS pipeline to understand how many active loans are affected (or try to -- if the LOS is truly down, the API may return errors, which is useful diagnostic info itself). Post a status update in #it-support acknowledging the issue and giving an ETA of 30 minutes for an update. Post in #general telling the team the LOS is down and to hold all lender submissions until further notice. Email ICE Mortgage Technology support (find their contact in my email history) with the symptoms and a priority request. Write a preliminary incident report to `it/incident_los_outage_2026-03.txt` with timeline, symptoms, affected staff, and business impact.

---

## Write Tool Coverage Matrix

This matrix shows which write-capable MCP tools are exercised by each business function. Use it to ensure eval tasks provide broad coverage of the agent's action space.

| Write Tool | Loan Ops | Compliance | Sales/Client | Finance | Executive | IT |
|---|---|---|---|---|---|---|
| **Email** | | | | | | |
| `send_email` | X | X | X | X | X | X |
| `reply_to_email` | X | X | X | | | X |
| `forward_email` | | X | X | | X | |
| `move_email` | | X | | | | |
| `set_email_keywords` | | X | | | | |
| `delete_email` | | | | | | X |
| **Contacts** | | | | | | |
| `contacts_add_new_contact` | X | | X | | | |
| `contacts_edit_contact` | | X | X | | | |
| `contacts_delete_contact` | | | | | | X |
| **Mortgage LOS** | | | | | | |
| `mortgage_los_add_activity` | X | X | | X | | X |
| `mortgage_los_add_condition` | X | X | | | | |
| `mortgage_los_create_borrower` | X | | X | | | |
| `mortgage_los_create_loan` | X | | X | | | |
| **Stripe** | | | | | | |
| `stripe_create_charge` | X | | | | | |
| `stripe_create_refund` | | | X | X | | |
| **CRM** | | | | | | |
| `crm_create_engagement` | X | X | X | | | |
| `crm_create_deal` | | | X | | | |
| `crm_create_lead` | | | X | | | |
| `crm_create_contact` | | | X | | | |
| `crm_create_company` | | | | | | |
| **Filesystem** | | | | | | |
| `filesystem_write_file` | X | X | | X | X | X |
| `filesystem_create_directory` | | X | | | X | X |
| `filesystem_copy_file` | X | | | | | |
| `filesystem_delete_file` | | | | | | X |
| **Slack** | | | | | | |
| `conversations_add_message` | X | X | X | X | X | X |
| **QuickBooks** | | | | | | |
| `quickbooks_create_invoice` | | | | X | | |
| `quickbooks_create_bill` | | X | | X | | |
| `quickbooks_create_customer` | | | | X | | |
| `quickbooks_create_vendor` | | | | X | | |

**Coverage notes:**

- `send_email` and `conversations_add_message` are universal -- every business function uses them. Don't rely on these alone to test write breadth.
- `mortgage_los_add_activity` appears in 4 of 6 functions. It's the most common LOS write action because most tasks need to document what happened on a loan.
- QuickBooks writes are concentrated in Finance. If you want to test QB writes outside of Finance, use Compliance tasks that require logging tolerance cures.
- Stripe writes are rare by design -- `stripe_create_charge` (collecting fees) and `stripe_create_refund` (complaint resolution) are the only two common actions. Most Stripe interaction is read-only investigation.
- Filesystem writes appear across 4 functions but serve different purposes: Loan Ops writes doc checklists, Compliance writes investigation reports, Finance writes analysis reports, IT writes incident reports. Vary the file path and format.
- CRM writes cluster in Sales/Client Relations. If you want CRM write coverage in other functions, have the agent log engagements as part of compliance investigations or post-close follow-up.