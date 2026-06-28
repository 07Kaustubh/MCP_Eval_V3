# Persona Briefs -- Keystone Mortgage Partners

This document profiles every employee at Keystone Mortgage Partners, a 30-person residential mortgage brokerage in Charlotte, NC. Each brief summarizes what the person does, who they interact with, and -- most importantly -- what unresolved situations from the scenario data could become evaluation tasks for an AI agent.

**How to use this as a task designer:** Pick a person. Read their open threads. Each thread is a situation where an agent could be dropped in and asked to investigate, resolve, audit, or communicate something. The richer the person's artifact footprint (emails, Slack messages, CRM notes, filesystem docs), the more angles you have for task construction. People with thin footprints are noted; they may still be useful as secondary actors or for tasks that require the agent to notice the *absence* of expected activity.

**Artifact types available:** email, Slack, CRM engagements, calendar, mortgage LOS (loan origination system), filesystem (PDFs, reports), Stripe (payments, Financial Connections bank data), QuickBooks (invoices, bills, vendor records).

---

## Executive & Administration

### Robert Calloway -- Owner / Licensed Mortgage Broker

**Active work:** Robert is the final decision-maker on every escalation. He reviews major compliance incidents, signs off on response strategies for regulatory complaints, and weighs in on personnel decisions that could affect the company's reputation or legal exposure. He does not originate loans himself but holds the company's broker license.

**Key relationships:** Internal: Grace Yamamoto (his operational right hand), Denise Holloway (compliance -- they confer on every legal/regulatory matter), Priya Chakrabarti (manages his schedule). External: outside counsel (Laura Bennett for employment, Megan Sloane for cyber/privacy), wholesale lender AEs, referral-partner realtors.

**Open threads:**
- Ransomware incident (scenario_14b3ffde): Robert is weighing whether to pay a 2 BTC ransom or restore from 72-hour-old cloud backups. Monday closings are at risk. No decision has been made, and outside cyber counsel has been engaged.
- Marcus Webb departure (scenario_7da8f37a): Four borrowers are requesting file transfers to Marcus's new brokerage. Evidence of pre-resignation data exfiltration exists. Robert's instinct is to let Marcus go quietly, but Denise is pushing back -- the forwarding pattern looks deliberate.
- Appraisal bias investigation (scenario_2ab2a103, scenario_9639912b): Multiple LOs have complained about appraisal valuations. An anonymous tip about systematic bias triggered a compliance review that Robert must oversee.
- Glassdoor toxic-culture reviews (scenario_e2f94849): Three reviews from apparent current employees describe a hostile work environment. Robert needs to decide on a response strategy.
- Grace pressuring processors (scenario_6232deb5): Processors have complained that Grace pushes them to cut compliance corners. Robert must investigate his own operations director.
- CFPB fair lending complaint (scenario_e3be5565): A denied Black borrower filed a discrimination complaint. Robert must approve the response strategy within 15 days.
- Brittany Wallace harassment complaint (scenario_2b42ecf2): Jordan Blake, Robert's close friend and top BD person, is the subject. Robert has been notified factually but told not to intervene.

**Recent activity:** Slack DMs with Grace and Denise about ransomware pay-vs-restore decision. Email to cyber counsel Megan Sloane requesting guidance on ransom payment. Calendar holds for "Ransom decision review," "Complaint Review -- Executive," and "Confidential review -- Amy."

---

### Grace Yamamoto -- Director of Operations

**Active work:** Grace is the operational hub. She tracks every KPI, coordinates incident response, manages LO performance, and serves as the first escalation point for processing issues, borrower complaints, and personnel problems. She touches nearly every scenario in the universe.

**Key relationships:** Internal: Robert (she escalates to him), Elena Marchetti (senior processor -- her operational backbone), Denise Holloway (compliance partner on investigations), all LOs (she reviews their pipelines). External: EAP provider Morgan Ellis, outside counsel.

**Open threads:**
- Ransomware response (scenario_14b3ffde): Grace is running incident command. She sent a sanitized "system outage" email to all staff, flagged three at-risk Monday closings, and is coordinating contingency planning with processors.
- Intern data breach (scenario_6b64e58c): Grace must terminate Leo Park (Aiden's brother) after 34 unauthorized borrower file accesses, including a celebrity file whose address was shared on social media. She has not yet executed the termination conversation.
- Amy Chen performance crisis (scenario_870b4152): Amy's production dropped 60%, borrowers are complaining, and Natasha privately suspects a post-surgery issue. Grace has documented everything to Robert, requested EAP guidance, and scheduled a private check-in with Amy.
- Brittany Wallace complaint (scenario_2b42ecf2): Grace received the formal harassment complaint against Jordan Blake, brought Denise in as witness, notified Robert, and placed confidential meeting holds. Investigation interviews have not yet occurred.
- Carlos Rivera 60-day drought (scenario_d8b2b048): Carlos has not closed a loan in two months. Grace is reviewing his pipeline.
- TRID violation discovered (scenario_18ad15aa): Grace found a Closing Disclosure (the federally required document sent 3 business days before closing) was delivered late.
- Appraisal undervaluation pattern (scenario_c1c2b4bd): Grace is tracking a preferred appraiser who consistently undervalues properties in minority neighborhoods.
- Security audit gaps (scenario_bc9076f9): An external audit revealed Raj's admin practices have holes. Grace is coordinating the remediation.
- Processor pressure complaints (scenario_6232deb5): Grace herself is the subject -- processors say she pressures them to skip steps. Robert is aware.

**Recent activity:** Emails to all-staff about borrower-file access rules. Slack incident command thread during ransomware. DMs with Denise about fair lending optics. Calendar: "Emergency incident command," "Monday closing contingency," "Urgent -- intern access review," "Confidential -- Brittany," "Performance check-in" (Amy), "Staff Meeting -- Data Access Policies."

---

### Priya Chakrabarti -- Executive Assistant / Office Manager

**Active work:** Priya manages Robert's calendar, handles office logistics, coordinates meeting scheduling, and serves as the diplomatic gatekeeper for anyone trying to reach the owner. She remembers everyone's birthday and handles onboarding paperwork for new hires.

**Key relationships:** Internal: Robert (protects his time), Grace (coordinates scheduling), Raj (office infrastructure/IT setup for new hires). External: vendors, office supply contacts, Regus (office space).

**Open threads:** Priya has minimal direct scenario involvement. However, her role makes her relevant to tasks involving:
- Access provisioning for new hires or interns (the Leo Park incident exposed gaps in how intern access was set up)
- Scheduling for the many confidential meetings Grace and Robert are juggling
- Offboarding logistics for Marcus Webb's departure

**Recent activity:** Limited artifact footprint. Task designers should note that Priya's *absence* from incident documentation could itself be a task angle -- e.g., "Did the office manager follow proper onboarding/offboarding procedures?"

---

### Brittany Wallace -- Receptionist / Front Desk

**Active work:** Brittany is the first voice callers hear and the first face visitors see. She handles call routing, visitor check-ins, mail distribution, and front-desk overflow. She also fields borrower calls that come in to the general line.

**Key relationships:** Internal: Grace (her direct report path), Jordan Blake (the subject of her complaint), all staff (she routes calls/visitors). External: walk-in borrowers, visiting realtors, delivery vendors.

**Open threads:**
- Harassment complaint filed (scenario_2b42ecf2): Brittany submitted a formal written complaint to Grace documenting Jordan Blake's repeated comments about her appearance, drink invitations after she said no, and an unwelcome shoulder touch. She prepared a timestamped written statement saved as a PDF. The investigation is in intake phase -- no interviews have occurred yet.
- Chaotic borrower (scenario_d8361499): A borrower on LN-2026-00621 is simultaneously texting, emailing, and calling multiple Keystone staff. Brittany is fielding some of these calls at the front desk.

**Recent activity:** Formal complaint email to Grace. Written statement PDF saved in `documents/hr_notes/brittany_wallace/`. Slack message noting the shoulder incident. Draft email documenting the incident while still fresh.

---

## Loan Officers

### Amy Chen -- Senior Loan Officer (Conventional, Non-QM)

**Active work:** Amy specializes in conventional loans and non-QM products (loans that don't meet standard qualification rules -- useful for self-employed borrowers or unusual income situations). Historically meticulous with zero fallout rate, but her recent production has collapsed.

**Key relationships:** Internal: Elena Marchetti (her primary processor), Grace (performance oversight), Natasha Okafor (colleague who raised private concern), Marcus Webb (she often sought his advice). External: Stephanie Boyd (Keller Williams realtor, exclusive referral partner), borrowers on her pipeline.

**Open threads:**
- 60% production drop (scenario_870b4152): Borrowers Carlos Mendez (LN-2026-00609) and Tiffany Brooks (LN-2026-00211) have complained about delayed responses and confusing communication. Amy's Slack messages have become incoherent ("I did ping borrower on 00184 I thnk we're good just waiting on banking thing / maybe title?"). Grace has scheduled a private check-in. Natasha privately told Grace she suspects a post-surgery issue. Grace contacted an EAP provider for guidance.
- IRS transcript mismatch (scenario_f824b80f): A borrower's IRS transcript shows $72K income vs $95K on tax returns on LN-2026-00628. The loan may need restructuring.
- Self-employed write-off problem (scenario_eeb9a9ab): A borrower shows $180K gross but only $48K net after write-offs on LN-2026-00625. The qualifying income calculation is in dispute.
- Gift fund standoff (scenario_fc18b4d0): Parents of a borrower on LN-2026-00631 provided a $20K gift but refuse to give bank statements for donor verification.
- Unpermitted basement (scenario_fed5a54d): An appraisal on LN-2026-00632 found an unpermitted finished basement. Square footage doesn't match county records.
- Stale comps on refi (scenario_6102d251): An appraiser used 6-month-old comparable sales on a refinance and refuses to revise.
- Commission dispute (scenario_e8fb9029): Amy and either Carlos or Derek both claim credit for the same referral on LN-2026-00192.
- Rate lock issues (scenario_32d5374e, scenario_7538bb02, scenario_c66dd583): Multiple rate lock complications across several files.
- Escrow surprise (scenario_55f1ee46): A post-close escrow issue surfaced after closing.

**Recent activity:** Incoherent Slack messages in #loan-processing about file statuses. Missed multiple morning pipeline huddles. Borrower complaint emails forwarded to Grace. No CRM engagement logged in 12+ days on some files.

---

### Carlos Rivera -- Loan Officer (FHA, Conventional)

**Active work:** Carlos handles FHA and conventional loans and is bilingual (Spanish), serving Charlotte's Spanish-speaking borrower community. He tends to over-promise timelines to borrowers.

**Key relationships:** Internal: Sofia Reyes (primary processor, also bilingual), Camille Foster (rate lock issues), Grace (pipeline oversight), Jordan Blake (referral partnerships). External: Brian Foster (RE/MAX realtor, FHA/first-time buyer referrals), borrowers.

**Open threads:**
- 60-day closing drought (scenario_d8b2b048): Carlos has not closed a loan in 60 days. Grace and Robert are reviewing his pipeline (LN-2026-00009, LN-2026-00211, LN-2026-00622).
- $14K cash deposit (scenario_883ed327): Carlos is the LO on LN-2026-00610 where borrower Destiny Pham's $14K Facebook Marketplace furniture sale deposit lacks documentation. Sofia escalated to him because the explanation is too weak for underwriting and the rate lock expires 3/23.
- Wrong bank statements 3x (scenario_f5fab8f7): A borrower on LN-2026-00626 has uploaded the wrong bank statement three times over 10 days. Closing date at risk.
- Foundation cracks (scenario_a2c4c9ef): An appraisal on LN-2026-00612 revealed structural foundation cracks, making the property ineligible for conventional financing.
- Rate lock expiring (scenario_cdc013ad): A 45-day lock on LN-2026-00619 expires in 3 days and the file hasn't been submitted. Sofia is overloaded.
- Borrower demands lower rate (scenario_32d5374e): After locking on LN-2026-00602, rates dropped and the borrower threatens to cancel.
- Mid-day repricing (scenario_7538bb02): A lender canceled morning locks mid-day on LN-2026-00607.
- Builder delays (scenario_c66dd583): New construction on LN-2026-00184 has repeated builder delays causing lock extensions. Borrower Evan Mercer refuses the second extension fee.
- Live-tweet closing disaster (scenario_aaff6156): A borrower live-tweeted a bad closing experience. Carlos was the LO.
- Phishing attack (scenario_69a37c71): Carlos was one of the affected LOs when Keisha's portal was compromised.
- Undisclosed credit issues (scenario_513e724e): Underwriting discovered undisclosed issues on LN-2026-00009.
- Systematic appraisal bias (scenario_2ab2a103): Carlos is involved in the bias investigation.
- Commission dispute (scenario_e8fb9029): Carlos claims credit for a referral that another LO also claims.
- Servicer problems post-close (scenario_5412669f): A servicer reported issues 3 months after closing on one of Carlos's loans.
- Chaotic borrower (scenario_d8361499): A borrower on LN-2026-00621 is contacting multiple staff simultaneously.
- Processor missed lock deadline (scenario_bf492a8b): Sofia missed a rate lock deadline on LN-2026-00616 while handling 35 active files.

**Recent activity:** Email from Sofia escalating the $14K deposit condition on LN-2026-00610. Slack messages in #loan-processing and #closings on multiple files. CRM engagement notes on borrower follow-ups.

---

### Derek Moss -- Loan Officer (VA, Conventional)

**Active work:** Derek handles VA loans (mortgages guaranteed by the Department of Veterans Affairs for military service members) and conventional products. Former Marine, direct communicator, loyal veteran client base.

**Key relationships:** Internal: processors (Elena, Darnell), Grace (pipeline reviews). External: veteran borrowers, VA-focused referral partners.

**Open threads:**
- Commission dispute (scenario_e8fb9029): Derek is one of the LOs claiming credit for the same borrower referral on LN-2026-00192.
- Servicer problems post-close (scenario_5412669f): A servicer reported issues 3 months after closing on a loan Derek was involved with.
- Escrow surprise (scenario_55f1ee46): Derek is the primary LO on a post-close escrow issue where the borrower was surprised by escrow costs after closing.

**Recent activity:** Limited artifact footprint compared to Carlos or Keisha. Derek's directness means his files tend to be cleaner, but the post-close scenarios provide investigation angles.

---

### James Thornton -- Loan Officer (FHA, USDA)

**Active work:** James originates FHA and USDA loans (USDA loans are zero-down-payment mortgages for properties in designated rural areas). He serves first-time buyers in the rural Charlotte exurbs -- Union, Cabarrus, and Iredell counties. Patient, folksy style.

**Key relationships:** Internal: processors, Grace. External: rural referral partners, first-time homebuyers.

**Open threads:** James has no named scenario involvement. His value to task design is as a stable baseline -- a loan officer whose files are presumably clean and whose pipeline could be used as a comparison point in performance reviews (e.g., "Compare James's pipeline metrics to Carlos's 60-day drought").

**Recent activity:** Minimal artifact footprint. He likely has standard loan activity in the LOS and CRM but no crisis-level artifacts.

---

### Keisha Williams -- Loan Officer (Conventional, Jumbo)

**Active work:** Keisha is the highest-volume LO at Keystone, handling conventional and jumbo loans (loans exceeding conforming limits, currently $766,550 in most areas). Ambitious but sometimes cuts corners on documentation.

**Key relationships:** Internal: Elena Marchetti and Sofia Reyes (processors), Grace (pipeline oversight), Denise (compliance friction point). External: high-volume referral partners, borrowers.

**Open threads:**
- CFPB fair lending complaint (scenario_e3be5565): Aisha Walker, a denied Black borrower, named Keisha as dismissive in a CFPB discrimination complaint. Keisha insists the denial was income-based and the complaint ignores material differences. She is defensive in Slack. The side-by-side file comparison reveals documentation gaps and tone differences in borrower communication.
- Racial discrimination allegation (scenario_e3be5565 overlap): This is the same CFPB matter -- Keisha's communication cadence with the denied borrower vs. the approved white comparator is a key optics problem.
- Phishing portal compromise (scenario_69a37c71): Keisha clicked a phishing link, giving attackers access to a lender portal containing borrower SSNs and financials for LN-2026-00008, 00009, and 00010.
- Appraisal undervaluation (scenario_c1c2b4bd, scenario_9639912b): Keisha flagged that a preferred appraiser consistently undervalues properties in minority neighborhoods. She is both a complainant and someone whose lending patterns are under scrutiny.
- IRS transcript mismatch (scenario_f824b80f): Keisha is involved in the $72K vs $95K income discrepancy on LN-2026-00628.
- Wrong bank statements (scenario_f5fab8f7): LN-2026-00626 borrower uploaded wrong statements repeatedly. Keisha is involved.
- Undisclosed credit (scenario_513e724e): LN-2026-00009 has undisclosed credit issues discovered in underwriting.
- 1-star Google review (scenario_dd376e4f): A denied borrower on LN-2026-00624 posted a detailed 1-star Google review. Keisha was the LO.
- Chaotic borrower (scenario_d8361499): LN-2026-00621 borrower contacting multiple staff simultaneously.
- Mid-day repricing (scenario_7538bb02): LN-2026-00607 affected by lender repricing.
- Servicer problems (scenario_5412669f): Post-close servicer issue on one of her loans.
- Escrow surprise (scenario_55f1ee46): Another post-close issue.

**Recent activity:** Defensive Slack messages about the CFPB complaint ("Aisha's denial was not some arbitrary call"). Email trail showing different communication tone with Walker vs. Goldstein. CRM engagement notes. Phishing-related Slack activity in #compliance-alerts.

---

### Marcus Webb -- Senior Loan Officer (Conventional, FHA)

**Active work:** Marcus is (was) the LO other LOs asked for advice. He gave his 2-week notice and is leaving for a competing brokerage. His 15-loan pipeline needs reassignment. His last day is April 4.

**Key relationships:** Internal: Aiden Park (his LOA), Grace, Denise, Raj (investigating his data access). External: Laura Bennett (outside employment counsel engaged by Keystone), four borrowers requesting transfers (Abigail Clark, Stephen Hamilton, Keisha Perry, Joshua Cruz).

**Open threads:**
- Resignation and data exfiltration (scenario_7da8f37a): The night before resigning, Marcus forwarded himself pipeline snapshots, rate quotes, borrower/realtor contact lists, and loan docs to a personal Gmail. Four borrowers have emailed Grace asking to transfer their files (LN-2026-00008, 00009, 00525, 00527), with at least one saying "Marcus told me to email." Raj found the forwarding activity and after-hours bulk downloads. Denise is consulting outside employment counsel on non-compete enforceability.
- Conflict of interest (scenario_f90fb17d): Marcus's wife is the buyer's agent on a loan he originated. Denise is investigating the conflict of interest.
- IRS transcript mismatch (scenario_f824b80f): Marcus was consulted on the $72K vs $95K income problem.
- Self-employed write-offs (scenario_eeb9a9ab): Marcus provided guidance on the $180K gross / $48K net situation.
- Gift fund standoff (scenario_fc18b4d0): Marcus is involved in the $20K gift where parents refuse verification.

**Recent activity:** Resignation email to Grace. Farewell post in #general. Four emails forwarded to personal address the night before notice (pipeline snapshot, rate quotes, contact export, loan docs). Slack message: "Still cleaning up my pipeline notes tonight." Borrower transfer request emails arriving at Grace's inbox.

---

### Natasha Okafor -- Loan Officer (Conventional, Jumbo)

**Active work:** Natasha handles conventional and jumbo loans for high-net-worth clients. She is confident and polished but was recently involved in an incident where she told a client something she shouldn't have.

**Key relationships:** Internal: Grace, Denise, Elena (processing). External: Monique Tate (Allen Tate realtor, Ballantyne market referrals), high-net-worth borrowers.

**Open threads:**
- Inappropriate disclosure to client (scenario_e7b325dc): An email surfaced where Natasha told a high-net-worth client something she shouldn't have. Denise, Grace, and Robert are involved in the review.
- Amy Chen concern (scenario_870b4152): Natasha privately told Grace she suspects Amy is dealing with a post-surgery issue. This is the only internal source of that information.
- Self-employed write-offs (scenario_eeb9a9ab): Natasha is involved in the $180K gross / $48K net qualifying income issue.
- Stale comps on refi (scenario_6102d251): Natasha's refinance client's appraisal used outdated comparables.
- Builder delay lock extensions (scenario_c66dd583): Natasha is involved in LN-2026-00184's repeated lock extensions.

**Recent activity:** Confidential Slack DMs to Grace about Amy. Emails on jumbo file processing. CRM notes on high-net-worth client interactions.

---

### Priya Desai -- Loan Officer (Conventional, VA)

**Active work:** Priya handles conventional and VA loans with particular skill at calming anxious first-time buyers. Detail-oriented and empathetic.

**Key relationships:** Internal: Elena (processing), Marcus Webb (consulted on difficult files), Grace. External: first-time homebuyers, veteran borrowers.

**Open threads:**
- Gift fund standoff (scenario_fc18b4d0): Priya is the LO on LN-2026-00631 where parents provided a $20K gift but refuse to provide bank statements for donor verification. This is a common underwriting requirement that the parents don't understand or won't comply with.

**Recent activity:** Limited scenario artifact footprint. Priya's files are generally well-managed, making her useful as a comparison baseline in quality or process audits.

---

## Processing & Operations

### Elena Marchetti -- Senior Processor

**Active work:** Elena is the most experienced processor at Keystone. She manages document collection from borrowers, coordinates with wholesale lender underwriting teams, and knows every lender's quirks. She is the person other processors (and LOs) ask when they don't know what documentation underwriting will accept.

**Key relationships:** Internal: all LOs (she processes their files or advises on them), Sofia/Tyler/Darnell (junior processors she mentors), Grace (operational coordination). External: lender underwriting desks (Patricia Langford at UWM, Mark Grayson at Caliber), title companies, appraisers.

**Open threads:**
- Ransomware Monday closings (scenario_14b3ffde): Elena confirmed that the Monday closings are in jeopardy because LOS is down. She noted that one file was "tight even before this" with "no clean fallback copy on shared drive."
- $14K deposit guidance (scenario_883ed327): Sofia asked Elena in Slack what documentation underwriting might accept for Facebook Marketplace furniture sales. Elena advised: "Need more than just the letter. Best shot is FB Marketplace listing screenshots, Messenger convos..."
- Amy Chen stalled files (scenario_870b4152): Elena's pipeline scrubs with Amy are on the calendar. She has been covering for Amy's stalled files in processing.
- IRS transcript mismatch (scenario_f824b80f): Elena is processing the $72K vs $95K income discrepancy file.
- Self-employed write-offs (scenario_eeb9a9ab): Elena is handling the $180K gross / $48K net file.
- Gift fund standoff (scenario_fc18b4d0): Elena is working on the $20K gift where parents refuse bank statements.
- Unpermitted basement (scenario_fed5a54d): Elena is processing the file where the appraisal found unpermitted work.
- Foundation cracks (scenario_a2c4c9ef): Elena is on the file where the appraisal found structural issues.
- Stale comps (scenario_6102d251): Elena is coordinating the appraiser dispute on the refinance.
- TRID violation (scenario_18ad15aa): Elena was involved in the late Closing Disclosure delivery.
- QC audit findings (scenario_5f5c9e81): Elena is named in the audit where Tyler cleared conditions without supporting docs.
- Grace pressuring processors (scenario_6232deb5): Elena is one of the processors who complained about Grace pushing them to cut corners on LN-2026-00604.
- Keith's investigation trigger (scenario_34e517fe): Elena is involved in a post-close investigation Keith Langford triggered.
- Processor missed lock (scenario_bf492a8b): Elena is involved in the aftermath of Sofia missing a rate lock deadline.
- 30yr-to-15yr switch (scenario_afc0c41f): Elena is managing a mid-process loan-term switch on LN-2026-00613 that triggered a redisclosure crisis (when loan terms change, new federal disclosures must be sent with fresh timing requirements).
- Wrong bank statements (scenario_f5fab8f7): Elena is escalating repeated wrong uploads on LN-2026-00626.
- Undisclosed credit (scenario_513e724e): Elena discovered undisclosed credit issues during processing.

**Recent activity:** Slack messages in #loan-processing across nearly every active file. CRM engagement notes on condition tracking. Calendar: pipeline scrub meetings, Monday closing contingency. Email: escalation chains to LOs about stalled conditions.

---

### Darnell Price -- Processor

**Active work:** Darnell handles conditions clearing (items the lender's underwriter requires before approving a loan) and closing coordination. Methodical and reliable -- tracks every condition in a personal spreadsheet in addition to the LOS.

**Key relationships:** Internal: Elena (senior guidance), LOs (conditions follow-up), Tyler (closing coordination overlap). External: lender underwriting desks, title companies.

**Open threads:** Darnell has no named scenario involvement. His methodical nature and personal spreadsheet make him relevant to tasks about process consistency ("Does Darnell's tracking match the LOS records?") or as a reliable handoff point when other processors are overwhelmed.

**Recent activity:** Minimal artifact footprint. Standard processing activity in LOS and CRM.

---

### Sofia Reyes -- Processor (Title, Insurance, Compliance)

**Active work:** Sofia handles complex FHA/VA files, title and insurance coordination, and compliance-sensitive processing. She is bilingual (Spanish) and works late, often carrying the heaviest caseload among processors.

**Key relationships:** Internal: Carlos Rivera (primary LO -- they share the bilingual borrower pipeline), Elena (mentorship), Camille Foster (rate lock coordination). External: Barbara Hensley at Tryon Title, title companies, insurance providers.

**Open threads:**
- $14K deposit condition (scenario_883ed327): Sofia is the assigned processor on LN-2026-00610. She emailed borrower Destiny Pham requesting a letter of explanation, received a weak response ("no receipts"), asked Elena for guidance in Slack, escalated to Carlos, and set a 3-day follow-up. The rate lock expires 3/23 and the condition is unresolved.
- $47K wire fraud (scenario_6ac0f3c9): Sofia was the last legitimate Keystone sender to the borrower before a spoofed wire instruction email caused $47,000 to be wired to a fraudulent account on LN-2026-00605. Her mailbox may have been compromised -- breach review is underway. She sent the "STOP -- DO NOT WIRE" email and flagged the incident to Grace.
- Wrong bank statements (scenario_f5fab8f7): Sofia is processing LN-2026-00626 where the borrower uploaded wrong statements three times.
- Rate lock expiring (scenario_cdc013ad): Sofia is overloaded with 35 active files and the 45-day lock on LN-2026-00619 is about to expire without the file being submitted to the lender.
- Missed rate lock deadline (scenario_bf492a8b): Sofia missed a critical rate lock deadline on LN-2026-00616 while juggling too many files.
- Chaotic borrower (scenario_d8361499): LN-2026-00621 borrower is contacting multiple staff simultaneously.
- Foundation cracks (scenario_a2c4c9ef): Sofia is working on LN-2026-00612 where the appraisal found structural damage.
- Undisclosed credit (scenario_513e724e): Sofia is processing LN-2026-00009.
- 30yr-to-15yr switch (scenario_afc0c41f): Sofia is coordinating the redisclosure on LN-2026-00613.

**Recent activity:** Email to Destiny Pham requesting deposit explanation. Slack messages in #loan-processing asking Elena about acceptable documentation. Email to Carlos escalating the weak LOX. Slack alert in #closings about wire fraud: "Real Barbara at Tryon just confirmed they did NOT send any updated wiring." CRM notes: "Condition follow-up needed," "Escalated weak deposit docs."

---

### Tyler Washington -- Junior Processor / Closing Coordinator

**Active work:** Tyler is a new hire (6 months) who handles closing scheduling and final document preparation. Eager but error-prone -- he is the source of at least two significant incidents.

**Key relationships:** Internal: Elena (supervision), Grace (escalation), Raj (IT -- his phishing click caused the ransomware). External: closing attorneys, title companies.

**Open threads:**
- Ransomware entry vector (scenario_14b3ffde): Tyler clicked a phishing link that appears to be the initial intrusion vector for the ransomware attack on the LOS. Raj traced the credential capture to Tyler's browser at 11:18 AM. Grace told Raj not to message Tyler yet.
- QC audit: cleared conditions without docs (scenario_5f5c9e81): Raymond Chen's QC audit found that Tyler cleared underwriting conditions on loans LN-2026-00211, 00224, and 00603 without the supporting documents actually being in the file. This is a serious compliance finding.

**Recent activity:** Browser history showing credential capture page. Named in Raj's preliminary phishing assessment email to Grace. QC audit findings documented in filesystem.

---

### Nadia Osman -- Loan Setup / Disclosure Coordinator

**Active work:** Nadia registers new loans in the LOS, triggers TRID disclosures (the federal Truth in Lending/RESPA Integrated Disclosure rules that mandate specific document delivery timelines), and orders third-party services like appraisals, title, and credit reports. Precise and fast -- the TRID clock starts when she clicks send.

**Key relationships:** Internal: LOs (she sets up their loans), processors (she hands off to them), Denise (TRID compliance). External: appraisal management companies, title companies, credit report vendors.

**Open threads:**
- Appraisal undervaluation (scenario_c1c2b4bd): Nadia is involved in tracking the appraiser who undervalues minority-neighborhood properties, since she orders appraisals as part of loan setup.

**Recent activity:** Limited named scenario activity, but Nadia is critical infrastructure for every loan. Task designers could build tasks around TRID timing audits ("Did Nadia's disclosure delivery meet the 3-business-day requirement?").

---

### Keith Langford -- Post-Closer

**Active work:** Keith handles trailing documents (items the lender needs after closing but before the loan is sold to investors), investor delivery, and post-close QC preparation. He is methodical and deadline-driven.

**Key relationships:** Internal: Raymond Chen (QC -- Keith prepares files for Raymond's audits), Elena (processing handoff), Denise (compliance). External: investor delivery contacts at wholesale lenders.

**Open threads:**
- Post-close investigation trigger (scenario_34e517fe): Keith overheard something that triggered a formal post-close investigation involving Grace, Robert, Denise, and Elena. The nature of what he overheard is the scenario's core mystery.

**Recent activity:** CRM engagement notes related to the investigation. Emails in the investigation chain. Keith's role as the post-close person means he sees files after everyone else is done with them -- he catches things others miss.

---

### Camille Foster -- Lock Desk / Pricing Analyst

**Active work:** Camille manages rate locks (commitments from lenders to hold a specific interest rate for a set period), processes lock extensions, handles re-locks when locks expire, and distributes daily rate sheets at 9:15 AM. She is sharp and numbers-oriented.

**Key relationships:** Internal: all LOs (they request locks through her), Sofia (lock timing coordination on complex files), Grace (extension cost approvals), Hana Kim (extension fees and cost tracking). External: wholesale lender pricing desks.

**Open threads:**
- $14K deposit lock clock (scenario_883ed327): Camille flagged LN-2026-00610's lock expiring 3/23 on her morning sweep while the file is still in conditional approval.
- 45-day lock expiring (scenario_cdc013ad): LN-2026-00619's lock expires in 3 days and the file hasn't been submitted. This is a direct lock desk crisis.
- Borrower demands lower rate (scenario_32d5374e): The borrower on LN-2026-00602 wants a float-down after rates dropped.
- Mid-day repricing (scenario_7538bb02): A lender's mid-day repricing canceled morning locks on LN-2026-00607. Camille has to figure out which locks survived and which need re-pricing.
- Builder delays (scenario_c66dd583): Repeated lock extensions on LN-2026-00184 due to construction delays. Three escalating extension charges in Stripe/QuickBooks.
- Missed lock deadline (scenario_bf492a8b): The lock on LN-2026-00616 expired because Sofia couldn't submit in time.
- 30yr-to-15yr switch (scenario_afc0c41f): The mid-process term change on LN-2026-00613 requires new lock pricing.

**Recent activity:** Slack in #rate-watch and #loan-processing: "Flagging LN-2026-00610 on my lock sweep. 3/23 exp and still sitting in cond approval." CRM note: "Lock exp 3/23. File still in cond approval on morning sweep." Calendar: lock expiration monitoring events.

---

## Sales & Business Development

### Jordan Blake -- Business Development Manager

**Active work:** Jordan manages 40+ referral partner relationships (realtors, builders, financial advisors) and is the company's top business development person. Charismatic, always networking.

**Key relationships:** Internal: all LOs (he feeds them referrals), Grace, Robert (close personal friend). External: 40+ referral partners including Jason Park (Coldwell Banker), real estate offices across Charlotte.

**Open threads:**
- Harassment complaint (scenario_2b42ecf2): Brittany Wallace filed a formal complaint against Jordan for repeated appearance comments, unwanted drink invitations, and unwelcome physical contact (shoulder touch). Slack DMs show escalating personal messages. Public #general comments are also preserved. Jordan's importance to the business and his friendship with Robert make the investigation politically sensitive.
- Glassdoor reviews (scenario_e2f94849): Jordan is named in the scenario examining anonymous employee reviews about toxic culture.
- Carlos 60-day drought (scenario_d8b2b048): Jordan's referral pipeline connects to Carlos's performance review.
- Commission dispute (scenario_e8fb9029): Jordan is involved in the commission dispute between LOs over a shared referral.

**Recent activity:** Slack DMs to Brittany: "Front desk looks way better when you're up there," "Not gonna lie that green top is distracting today." Public #general: "@Brittany Wallace front desk has a whole different vibe today." Grace warned in Slack: "Let's keep #general work-related please."

---

### Maya Torres -- Marketing Coordinator

**Active work:** Maya runs Keystone's Instagram, manages Zillow/LendingTree lead generation, coordinates marketing campaigns, and handles social media monitoring.

**Key relationships:** Internal: Jordan (BD coordination), LOs (lead distribution), Grace (marketing budget). External: Zillow, LendingTree, social media audiences.

**Open threads:**
- 1-star Google review (scenario_dd376e4f): A denied borrower posted a detailed 1-star review on Google. Maya is involved in the response strategy -- monitoring and potential reputation management.
- Live-tweet closing disaster (scenario_aaff6156): A borrower live-tweeted a bad closing. Maya is coordinating the social media response.

**Recent activity:** Social media monitoring activity. Coordination emails with Grace on reputation management.

---

### Aiden Park -- Loan Officer Assistant (LOA)

**Active work:** Aiden works under Marcus Webb, handling pre-qualification paperwork, borrower follow-ups, and pipeline support. He is junior and working toward his LO license.

**Key relationships:** Internal: Marcus Webb (his mentor, now departing), Grace, Raj. External: Marcus's borrower pipeline (Aiden has had direct contact with many of them). Family: Leo Park (his younger brother, the intern).

**Open threads:**
- Marcus Webb departure (scenario_7da8f37a): Aiden's mentor and direct supervisor is leaving. Marcus's 15-loan pipeline must be reassigned, and Aiden's role during the transition is uncertain.
- Intern data breach (scenario_6b64e58c): Aiden's younger brother Leo, hired as a summer intern as a favor, accessed 34 unauthorized borrower files and shared a celebrity borrower's address on social media. Grace summoned Aiden for an uncomfortable meeting: "Need you to come by my office at 12:15 re Leo. Please keep it tight and don't text/call him about it yet." Aiden responded: "Is he in some kind of trouble?"

**Recent activity:** Slack DM from Grace about Leo situation. Slack reply in #general welcoming Leo ("lol appreciate that. Welcome bro"). Calendar: "Talk w Aiden -- Leo" meeting with Grace.

---

## Compliance & Risk

### Denise Holloway -- Compliance Officer

**Active work:** Denise is a former bank auditor who handles every compliance, regulatory, and legal-risk matter at Keystone. She is meticulous and by-the-book -- respected but feared. She consults outside counsel proactively and maintains her own documentation timeline for every incident.

**Key relationships:** Internal: Grace (operational partner on every investigation), Robert (she escalates regulatory exposure to him), Raymond Chen (QC findings feed her reviews), all LOs (she reviews their files for compliance). External: multiple outside counsel (Laura Bennett for employment, Megan Sloane for cyber/privacy, Laura Bennett again for fair lending, Melissa Grant for privacy), CFPB, FinCEN.

**Open threads:**
- CFPB fair lending complaint (scenario_e3be5565): Denise received the CFPB complaint about Aisha Walker. She opened a fair lending review, requested chronology from Keisha, pulled both files for comparison, found documentation/tone gaps, and is consulting outside HMDA counsel Laura Bennett. The 15-day response deadline is running.
- Ransomware reporting (scenario_14b3ffde): Denise engaged cyber counsel Megan Sloane about breach notification, SAR filing with FinCEN (Suspicious Activity Reports required when financial institutions suspect criminal activity), and borrower data exposure. She is queuing breach notification drafts while Raj confirms the scope of data exposure.
- Wire fraud breach review (scenario_6ac0f3c9): Denise is assessing whether Sofia's mailbox was compromised (vendor spoofing only vs. actual account compromise) on the $47K wire fraud.
- Marcus Webb non-compete (scenario_7da8f37a): Denise is consulting employment counsel Laura Bennett on whether Marcus's non-compete is enforceable. She privately believes the borrower-directed transfer requests are stronger solicitation evidence than the data forwards alone, and she is concerned Robert may soft-pedal the response.
- Intern privacy violation (scenario_6b64e58c): Denise is consulting outside privacy counsel Melissa Grant about notification obligations after Leo Park accessed 34 borrower files and may have shared a celebrity address publicly.
- Brittany harassment investigation (scenario_2b42ecf2): Denise was brought in as compliance witness/process partner. She contacted external HR consultant for evidence preservation guidance.
- Security audit gaps (scenario_bc9076f9): An external security audit revealed admin gaps in Raj's practices. Denise is coordinating remediation.
- Systematic appraisal bias (scenario_2ab2a103): Denise is leading the investigation triggered by an anonymous tip.
- Portfolio-wide appraisal complaints (scenario_9639912b): Denise is reviewing broader appraisal patterns.
- Phishing portal compromise (scenario_69a37c71): Denise is handling the compliance response to the phishing attack.
- TRID violation (scenario_18ad15aa): Denise is reviewing the late Closing Disclosure delivery.
- QC findings (scenario_5f5c9e81): Denise is reviewing Raymond's findings about Tyler clearing conditions without docs.
- Marcus conflict of interest (scenario_f90fb17d): Denise is investigating the conflict where Marcus's wife is the buyer's agent.
- Racial discrimination allegation (scenario_e3be5565 overlap): This is the CFPB complaint.
- Natasha inappropriate disclosure (scenario_e7b325dc): Denise is reviewing what Natasha told a client.
- Grace corner-cutting complaints (scenario_6232deb5): Denise is involved in the complaint that Grace pressures processors.
- Departed LO commission (scenario_644f352f): Denise is reviewing the ongoing commission payments to a departed LO.
- Glassdoor reviews (scenario_e2f94849): Denise is part of the leadership response.
- Unpermitted basement (scenario_fed5a54d): Denise is reviewing compliance implications.

**Recent activity:** Email to CFPB outside counsel with investigation plan. Email to cyber counsel about ransomware SAR and breach notification. Slack in #compliance-alerts: "Preserve all file notes, emails, texts, and call logs." Email to Keisha requesting chronology. Email to Grace about wire fraud breach assessment. DMs with Grace about fair lending optics. Calendar: daily "CFPB Response Prep" meetings, "Privileged reporting review," "Cyber counsel call," "Fair Lending File Review."

---

### Raymond Chen -- QC Analyst (Part-time, 3 days/week)

**Active work:** Raymond is a semi-retired former underwriter who audits 10% of closed loan files for compliance errors. He works 3 days per week. Dry humor. Catches everything.

**Key relationships:** Internal: Denise (findings go to her), Elena (file preparation), Keith (post-close handoff), Grace (operational findings). External: none significant.

**Open threads:**
- Tyler cleared conditions without docs (scenario_5f5c9e81): Raymond's QC audit discovered that Tyler Washington cleared underwriting conditions on at least three loans (LN-2026-00211, 00224, 00603) without the supporting documentation actually being present. This is a significant compliance finding -- conditions are items the lender requires proof of before approving a loan, and clearing them falsely means the loan was approved on incomplete evidence.

**Recent activity:** QC audit findings documented in filesystem. CRM engagement notes. Emails to Grace and Denise about audit results.

---

## Finance & Accounting

### Hana Kim -- Bookkeeper / Accountant

**Active work:** Hana handles all lender compensation tracking (verifying Keystone received the correct commission on each closed loan), vendor payments, LO commission calculations, and general bookkeeping in QuickBooks. Detail-oriented and quiet.

**Key relationships:** Internal: Grace (financial reporting), Victor (P&L collaboration), Camille (lock extension fees), all LOs (commission questions). External: wholesale lender accounting departments, vendors (appraisers, title companies).

**Open threads:**
- Rate lock extension costs (scenario_cdc013ad): Hana is tracking the financial impact of the expiring lock on LN-2026-00619, including potential extension fees.
- Builder delay extension charges (scenario_c66dd583): Three escalating lock extension charges on LN-2026-00184 are visible in both Stripe and QuickBooks.
- Commission dispute (scenario_e8fb9029): Hana must calculate and potentially split the commission on LN-2026-00192.
- Departed LO still receiving commissions (scenario_644f352f): Victor Osei noticed a recently departed LO is still being paid commissions. Hana handles the commission payments and will need to explain how this happened.
- Self-employed write-offs (scenario_eeb9a9ab): Hana is involved in the financial analysis of the $180K gross / $48K net situation.
- Glassdoor reviews (scenario_e2f94849): Hana is named in the toxic-culture review response.
- Servicer problems (scenario_5412669f): Financial impact tracking on the post-close servicer issue.
- Escrow surprise (scenario_55f1ee46): Financial tracking on the post-close escrow issue.

**Recent activity:** QuickBooks activity on lock extension bills, commission invoices, and vendor payments. CRM engagement notes on financial tracking.

---

### Victor Osei -- Financial Analyst (Part-time, 2 days/week)

**Active work:** Victor prepares the monthly P&L (profit and loss statement) for Robert, analyzes revenue trends, and flags financial anomalies. Sharp and numbers-driven, 2 days per week.

**Key relationships:** Internal: Robert (monthly financial reporting), Grace (operational metrics), Hana (data sourcing). External: none significant.

**Open threads:**
- Departed LO still receiving commissions (scenario_644f352f): Victor discovered that a recently departed LO is still receiving commission payments in QuickBooks. He flagged this to Grace and Hana, triggering a review that also involves Raj (system access) and Denise (compliance implications).
- Portfolio-wide appraisal complaints (scenario_9639912b): Victor is analyzing the financial impact of appraisal issues across the portfolio.
- Carlos 60-day drought (scenario_d8b2b048): Victor's P&L data would show the revenue impact of Carlos's zero closings.
- Servicer problems (scenario_5412669f): Victor is tracking the financial impact.
- Escrow surprise (scenario_55f1ee46): Victor is involved in the financial analysis.

**Recent activity:** QuickBooks P&L analysis. Email/Slack flagging the departed LO commission issue. CRM engagement notes on financial anomalies.

---

## Client Relations

### Jasmine Brooks -- Client Relations Specialist

**Active work:** Jasmine is the de-escalation expert. She handles angry borrowers, complaint calls, and serves as the buffer between frustrated clients and the rest of the team. Patient and empathetic.

**Key relationships:** Internal: Grace (escalation coordination), LOs (she takes over when borrowers are upset), Robert (she handles responses when he's named). External: borrowers in distress.

**Open threads:**
- 1-star Google review (scenario_dd376e4f): A denied borrower on LN-2026-00624 posted a detailed 1-star Google review. Jasmine is part of the response team working to manage the situation.
- Marcus Webb borrower transfer (scenario_7da8f37a): Joshua Cruz emailed Jasmine directly (not Grace) asking for his loan LN-2026-00527 to be transferred to Marcus, saying he's "pretty stressed and don't want this messed up right before closing."

**Recent activity:** Email from Joshua Cruz requesting file transfer. CRM engagement notes on borrower de-escalation.

---

### Tomas Herrera -- Retention & Refinance Specialist

**Active work:** Tomas handles post-close follow-up, manages the past-client database, calls borrowers on their closing anniversaries, and identifies refinance opportunities when rates drop. He bridges the gap between a closed loan and a future relationship.

**Key relationships:** Internal: LOs (they hand off closed borrowers to him), Maya (marketing coordination for refi campaigns). External: past Keystone borrowers.

**Open threads:** Tomas has no named scenario involvement. His role is relevant for:
- Rate-drop refinance outreach tasks (when rates drop, which existing borrowers should Keystone contact?)
- Post-close borrower satisfaction follow-up
- The rate lock and closing disaster scenarios create borrowers who may need retention outreach

**Recent activity:** Minimal artifact footprint. Standard post-close follow-up activity.

---

## IT

### Raj Anand -- IT Consultant (Contract, 2 days/week)

**Active work:** Raj is the sole IT person -- he manages the LOS (Encompass) administration, CRM, email system, network infrastructure, and security. He works 2 days per week on contract. When the LOS goes down, the company stops.

**Key relationships:** Internal: Grace (he reports findings to her), Denise (compliance implications of security issues), Robert (major incident escalation), all staff (password resets, system access). External: ICE Mortgage Technology (LOS vendor), network/security vendors.

**Open threads:**
- Ransomware response (scenario_14b3ffde): Raj discovered the ransomware on Friday afternoon. He found the ransom note (2 BTC), confirmed the LOS database and local backup server are encrypted, and identified that cloud backups are 72 hours old. He traced the entry point to Tyler Washington's phishing click. He is actively managing the technical response.
- Phishing investigation (scenario_69a37c71): Keisha clicked a phishing link that compromised a lender portal. Raj is investigating the scope of the compromise.
- Intern access logs (scenario_6b64e58c): Raj pulled Leo Park's LOS access history and found 34 unauthorized borrower file accesses over two weeks, including repeat views on a celebrity borrower file and after-hours/weekend access. He prepared the access review report (CSV and summary) and is recommending tighter intern LOS permissions.
- Marcus Webb data exfiltration (scenario_7da8f37a): Raj found four late-night email forwards from Marcus's Keystone account to a personal Gmail, plus bulk file access logs. He is preserving the evidence for Denise.
- Security audit gaps (scenario_bc9076f9): An external security audit revealed that Raj's own admin practices have gaps (shared admin accounts, inconsistent access provisioning, weak offboarding procedures).
- Departed LO system access (scenario_644f352f): Raj needs to confirm whether the departed LO's system access was properly revoked -- the ongoing commission payments suggest offboarding was incomplete.

**Recent activity:** Slack in #it-support: "Anyone else unable to get into LOS? getting db connection errors." Email to Grace/Robert: "Immediate escalation: ransomware impacting LOS and backups." Slack: "Likely initial entry point was a phishing email opened by Tyler." Email to Grace: "Leo Park access log review" with attached CSV. Slack: "found 4 manual forwards from Marcus mailbox last night." Calendar: "LOS outage triage," "Leadership incident huddle," "Preserve Marcus access logs." IT policy notice in #it-support about borrower file access.

---

## Other

### Zoe Brennan -- Summer Intern (Seasonal, May-August)

**Active work:** Zoe is a college junior studying finance who works May through August doing document scanning, data entry, and phone overflow in the processing department.

**Key relationships:** Internal: Elena (processing supervision), Grace (intern oversight). External: none significant.

**Open threads:** Zoe has no named scenario involvement. However, the Leo Park intern incident (scenario_6b64e58c) creates policy changes that would directly affect Zoe's access level and supervision when she arrives for the summer. A task designer could build scenarios around:
- Onboarding a new intern after the Leo Park incident
- Verifying that new access restrictions are properly configured
- Whether Zoe's scanning role gives her appropriate (or inappropriate) access to borrower documents

**Recent activity:** No artifacts -- Zoe is seasonal and the scenario timeline is March 2026.

---

## Cross-Reference: People by Scenario Count

For task designers who want to start with the most "connected" people:

| Person | Scenario count | Notes |
|--------|---------------|-------|
| Denise Holloway | 20+ | Involved in every compliance/legal matter |
| Grace Yamamoto | 18+ | Involved in every operational crisis |
| Elena Marchetti | 15+ | Touches nearly every loan-level scenario |
| Robert Calloway | 12+ | Final decision-maker on escalations |
| Carlos Rivera | 14+ | Most scenario-involved LO |
| Sofia Reyes | 9 | Processing-heavy, wire fraud, lock crises |
| Keisha Williams | 11+ | Fair lending, phishing, high volume |
| Raj Anand | 6 | Every security/IT incident |
| Camille Foster | 7 | Every rate lock scenario |
| Amy Chen | 9 | Performance crisis + multiple loan issues |
| Marcus Webb | 5 | Departure + exfiltration + conflict of interest |
| Hana Kim | 6 | Financial tracking across multiple scenarios |
| Tyler Washington | 2 | Ransomware vector + QC findings |
| Brittany Wallace | 2 | Harassment complaint + chaotic borrower |
| Jordan Blake | 3 | Harassment subject + culture issues |
| Natasha Okafor | 5 | Client disclosure + Amy concern + loan issues |
| Victor Osei | 4 | Financial anomaly detection |
| Aiden Park | 2 | Marcus departure + brother's data breach |
| Keith Langford | 1 | Post-close investigation trigger |
| Raymond Chen | 1 | QC audit findings |
| Jasmine Brooks | 2 | Borrower de-escalation |
| Maya Torres | 2 | Social media crises |
| Nadia Osman | 1 | Appraisal ordering |
| Priya Desai | 1 | Gift fund standoff |
| Derek Moss | 3 | Commission dispute + post-close issues |
| James Thornton | 0 | Baseline LO -- no scenario involvement |
| Darnell Price | 0 | Baseline processor -- no scenario involvement |
| Tomas Herrera | 0 | Post-close retention -- no scenario involvement |
| Priya Chakrabarti | 0 | Office management -- no scenario involvement |
| Zoe Brennan | 0 | Seasonal intern -- not yet on-site |