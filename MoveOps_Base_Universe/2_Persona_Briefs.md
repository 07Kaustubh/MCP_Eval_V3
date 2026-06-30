# MoveOps Persona Briefs

---

## Executive

### Elena Rostova — Chief Executive Officer

**Active work:** Running company strategy and making final calls on high-stakes decisions. Recently issued a company-wide DOT compliance policy after a formal inquiry from the U.S. Department of Transportation about hazmat shipment documentation. Managing the Vectral Systems renewal negotiation where the client demanded a 15% discount.

**Key relationships:**
- *Internal:* David Chen (CE Lead — reports on client health), Marcus Thorne (Finance — reports on margins and compliance costs), Samira Tariq (Engineering — reports on platform issues), Chloe Vance (Operations — reports on capacity and compliance)
- *External:* Rachel Whitfield, VP of People at Vectral Systems (renewal negotiation)

**Open threads:**
- DOT compliance inquiry (Case No. PHMSA-2026-04-1187) — 15-day extension granted, deadline now June 5, 2026. Potential penalties up to $59,017/day.
- Vectral renewal — counter-offer at 10% discount + Preferred Partner Program sent; Rachel's board was meeting April 23, no response as of April 26.
- Expense auto-categorizer — Elena directed the project to continue with modifications after pilot bugs were discovered; auto-decisions currently disabled.
- BrightLoop expansion — Chloe and David requested temp coordinator authorization; Elena hasn't responded.
- NorthWind churn — David asked to redistribute Catalina's accounts; Elena said "handle it within the team" — no redistribution happened.
- Vendor strategy memo — Elena ordered Marcus to deliver a formal vendor response plan by end of week after both Heartland and Swift raised rates simultaneously.

**Recent activity:**
- Posted company-wide DOT compliance policy update in #general (April 21)
- Participated in executive discussion about Vectral renewal strategy
- Assigned Terraform Digital account to Mina after Catalina accidentally reply-all'd internal pricing to the client during the AM selection process
- Declined to formally redistribute Catalina's accounts despite David's escalation (April 15)
- Ordered vendor strategy memo from Marcus after dual rate increases (April 24)
- Did not respond to BrightLoop temp coordinator request (April 24)

---

### Priya Chakrabarti — Executive Assistant

**Active work:** Supports Elena Rostova with scheduling and administrative tasks. Limited direct presence in Slack channels and email threads.

**Key relationships:**
- *Internal:* Elena Rostova (direct report)

**Open threads:**
- No visible open threads in current artifacts.

**Recent activity:**
- Minimal artifact footprint. Primarily works through direct communication with Elena.

---

## Finance

### Marcus Thorne — Head of Finance

**Active work:** Managing multiple financial threads simultaneously: the DOT compliance penalty accrual ($50K contingent liability), the Heartland Movers billing dispute ($4,800 overcharge for canceled moves), and oversight of the stipend fraud investigation. Recently booked the $90K Mosaic prototype damage liability and the DOT penalty accrual in QuickBooks.

**Key relationships:**
- *Internal:* Elena Rostova (reports to), Hana Kim (direct report — invoicing), Alejandro Fuentes (direct report — analysis), Chloe Vance (vendor disputes), Samira Tariq (expense tool financial exposure), Dmitri Volkov (stipend fraud findings)
- *External:* Linda Castellano at U.S. DOT (compliance inquiry), Lisa Kwan at Heartland Movers (billing dispute)

**Open threads:**
- Heartland Movers Q1 dispute — $12,800 bill on hold; $4,800 for 3 canceled moves is contested. Formal dispute letter sent with cancellation evidence.
- DOT penalty accrual — $50K contingent liability booked; extension to June 5 granted.
- Mosaic prototype damage — $90K accrual booked; $50K insurance covers partial; $40K gap remains.
- Stipend fraud — 3 receipts flagged (STIP-2026-0089, 0094, 0097) with admin holds placed.
- Vendor consolidation crisis — Both Heartland (12% increase tied to dispute) and Swift (18% surcharge + $400 hazmat premium) raising rates simultaneously. Marcus owns the response memo for Elena. Alejandro modeling 6-8 point margin compression.
- KeyMove piano claim — $1,200 insurance rider for Emilia Cruz Steinway scratch during NorthWind relocation.
- Sunbelt/Palmetto invoice exposure — swapped PDFs revealed nonprofit pricing to for-profit client; pricing policy controls needed.
- StormCloud credit memo — $500 goodwill credit was posted to the wrong QuickBooks estimate.
- BrightLoop pricing gaps — no formalized international or white-glove tiers exist; pushed back on ad hoc premium pricing.

**Recent activity:**
- Forwarded DOT inquiry letter to Chloe and requested immediate hazmat audit (April 21)
- Requested 15-day extension from DOT (April 22)
- Posted Heartland dispute evidence in #finance with cancellation dates
- Placed admin holds on suspicious stipend reimbursements
- Inherited vendor strategy memo ownership from Elena (April 24)
- Identified Sunbelt/Palmetto invoice swap as pricing policy exposure (April 15)
- Processed KeyMove $1,200 piano insurance claim rider (April 17)
- Discovered StormCloud $500 credit posted to wrong estimate (April 24)
- Pushed back on BrightLoop ad hoc premium pricing without margin guardrails (April 24)

---

### Hana Kim — Accountant

**Active work:** Generating invoices for the April relocation wave across all active clients, tracking vendor reconciliation, and marking duplicate stipend records in the reconciliation tracker. Recently booked accounting entries for the Mosaic prototype damage claim.

**Key relationships:**
- *Internal:* Marcus Thorne (reports to), Chloe Vance (vendor billing coordination), Blessing Okafor / Fatimah Al-Rashidi (relocation cost tracking)
- *External:* Vendor billing contacts (Heartland, Swift, Atlas)

**Open threads:**
- Vendor reconciliation on Heartland disputed items still in progress — found additional gaps beyond original $4,800.
- Terraform Digital preliminary estimate (EST-2026-0423, $6,560) in progress.
- Sunbelt/Palmetto invoice swap — accidentally sent Sunbelt the Palmetto nonprofit PDF and vice versa. Both clients escalated. Root cause: no attachment validation in invoice email workflow.

**Recent activity:**
- Created invoices for Canopy, Vectral, GreenStack, BrightLoop, Mosaic, and Terraform relocations
- Tracked duplicate stipends (STIP-2026-0089, 0094, 0097) in reconciliation
- Booked Mosaic damage claim accounting entries (credit memo CM-2026-0415, accrual)
- Booked DOT $50K penalty accrual
- Batch-sent April invoices with swapped Sunbelt/Palmetto PDFs (April 10)
- Found broader Heartland reconciliation gaps during vendor consolidation crisis (April 15)

---

### Alejandro Fuentes — Financial Analyst

**Active work:** Completed Q1 deal margin analysis comparing account managers' performance. Identified the 3x AWS cost spike ($42,870 vs $14,300 baseline) and traced it to the Vantage Distributed onboarding. Gathering 6-month cost comparison data for an upcoming pricing strategy meeting.

**Key relationships:**
- *Internal:* Marcus Thorne (reports to), David Chen (margin analysis shared with CE), Samira Tariq (AWS cost investigation)

**Open threads:**
- AWS cost trend analysis for pricing model meeting — in progress.
- 6-month cost comparison data collection ongoing.
- Vendor margin exposure model — modeling impact of dual Heartland/Swift rate increases across all active client contracts (6-8 point compression).
- BrightLoop pricing gaps — tiered model (sent to Marcus April 3) covers domestic only; no international or white-glove tiers.
- NorthWind retention pricing — drafted unfinished discount model for retention proposal but never finalized.

**Recent activity:**
- Published Q1 margin analysis in #finance
- Identified AWS cost anomaly and shared findings in #root-cause-aws-spike
- Modeled 6-8 point margin compression from vendor rate increases (April 15)
- Mapped BrightLoop pricing gaps — no international/white-glove tiers (April 24)
- Drafted unfinished NorthWind retention pricing model (April 16, never finalized)

---

## Customer Engagement

### David Chen — Customer Engagement Lead

**Active work:** Overseeing account manager team through Q2 pipeline execution. Assigned Terraform Digital to Mina after Catalina accidentally reply-all'd internal pricing to the client. Monitoring NorthWind account health after service escalation and coordinating response to Vectral renewal risk. Also played a key role in managing the expense auto-categorizer crisis — directed client communication strategy for affected accounts.

**Key relationships:**
- *Internal:* Mina Hashimoto, Catalina Dubois, Emeka Diallo (direct reports), Elena Rostova (reports to), Chloe Vance (ops coordination)
- *External:* Pam Kowalski at NorthWind (escalation recipient), Rachel Whitfield at Vectral (renewal)

**Open threads:**
- Vectral renewal — flagged as critical (2nd-largest client); awaiting board decision.
- NorthWind expansion — 2 new Denver relocations in coordination.
- Q2 pipeline targets — team surpassed Q1 targets, maintaining momentum.
- NorthWind churn crisis — Pam's final warning received April 24; assembling retention proposal by Friday. Multiple failures: chain-of-custody breach, piano damage, Catalina's broken promise.
- StormCloud failures — Ridgeline Robotics referral dropped; David realized it was never entered into CRM.
- Sunbelt/Palmetto — forced cross-functional reckoning after invoice swap exposed nonprofit pricing.
- Vendor exposure mapping — asked AMs for client impact; Mina flagged Vectral/BrightLoop, Emeka flagged Mosaic, Catalina went silent.
- BrightLoop expansion — requested temp coordinator hire from Elena; no response.

**Recent activity:**
- Conducted Q1 one-on-one performance reviews with all account managers
- Made final call on Terraform account reassignment
- Flagged Vectral discount request as critical in #executive
- Received Pam Kowalski's final warning; assembling NorthWind retention response (April 24)
- Asked Elena to redistribute Catalina's accounts; denied — "handle it within the team" (April 15)
- Requested client exposure map from all AMs after vendor rate increases (April 15)
- Forced cross-functional reckoning on Sunbelt/Palmetto invoice swap (April 22)
- Celebrated Ridgeline Robotics referral in Slack but failed to operationalize it (April 18)
- Requested temp coordinator hire for BrightLoop expansion; Elena didn't respond (April 24)

---

### Mina Hashimoto — Account Manager

**Active work:** Managing three major active situations: the Vectral Systems Q3 renewal negotiation (15% discount demand, 10% counter-offer pending), the newly-assigned Terraform Digital account (3 relocations starting May 5), and the Canopy Health executive relocation for Dr. Anand Mehta (CMO). Also managing BrightLoop Analytics relocations and handling aftermath of expense auto-categorizer bugs on Vectral account.

**Key relationships:**
- *Internal:* David Chen (reports to), Samira Tariq (expense tool escalations), Javier Morales (Vectral relocation coordinator), Suki Patel (BrightLoop coordinator)
- *External:* Rachel Whitfield at Vectral Systems (renewal negotiation), Tessa Moreno at BrightLoop (relocations), Rachel Nguyen at Terraform Digital (onboarding), Patricia Langford at Canopy Health (Dr. Mehta relocation)

**Open threads:**
- Vectral renewal — counter-offered 10% discount + Preferred Partner Program + 3 service sweeteners. Rachel's board met April 23; no response by May 1.
- Terraform Digital — 3 relocations (Priya Dasgupta May 5, Samantha Obi May 8, Marcus Liu May 12) to coordinate as new account owner.
- BrightLoop — Jordan Whitfield (Denver) and Preethi Nair (Raleigh) relocations in progress.
- Expense auto-categorizer — 2 Vectral false rejections manually corrected; monitoring for recurrence.
- BrightLoop expansion — 6 new May relocations (UK transfer, ADA service animal, CTO white-glove, 3 standard). First batch still broken: Simone Richter wrong apartment (8 days unanswered), Marcus Webb car stuck in Indianapolis.
- StormCloud recovery — reconstructed chain of missed handoffs (unsigned lease, misprioritized ticket, misapplied credit, dropped referral). Preparing recovery plan for Liam Park.
- Vendor exposure — flagged Vectral and BrightLoop as most exposed to rate increases.

**Recent activity:**
- Delivered final Vectral renewal proposal (10% + sweeteners) on April 19
- Assigned Terraform Digital account after Catalina's reply-all incident
- Coordinating Dr. Mehta's executive relocation with Fatimah Al-Rashidi
- Resolved StormCloud flight booking mistake same-day
- Secured StormCloud Analytics contract ($26,400 for 3 relocations)
- Escalated BrightLoop combined crisis (expansion + unresolved first batch) to Chloe and David (April 22)
- Reconstructed StormCloud internal failures after Liam Park's multi-issue escalation (April 24)
- Prepared StormCloud service recovery plan and belated Ridgeline Robotics response (April 24)
- Flagged Vectral and BrightLoop as most exposed to vendor rate increases (April 15)

---

### Catalina Dubois — Account Manager

**Active work:** Managing Canopy Health (largest client — Q2 relocation wave) and PivotPoint Labs. Also managing NorthWind Technologies, which had service quality issues in Q1 (slow response times led to Pam Kowalski escalating to David). Recovering from the Terraform Digital reply-all incident where internal pricing was accidentally shared with the client — Elena removed her from consideration for that account.

**Key relationships:**
- *Internal:* David Chen (reports to), Blessing Okafor (Canopy relocations), Fatimah Al-Rashidi (complex relocations)
- *External:* Patricia Langford at Canopy Health (ongoing), Sam Delgado at PivotPoint Labs, Pam Kowalski at NorthWind

**Open threads:**
- Canopy Q2 wave — 3 additional relocations (Dr. Kovacs Nashville→Toronto with visa/customs complexity, Tyler Okonkwo, Marcus Webb with cold-chain lab equipment).
- NorthWind expansion — 2 new Denver relocations (Raj Patel with server lab, Emilia Cruz). Relationship needs rebuilding after Q1 service issues.
- PivotPoint — Nadia Okonjo (H-1B visa) and Diego Castañeda (CNC equipment) dual relocation.
- NorthWind churn crisis — Account imploding. Chain-of-custody breach (Raj Patel servers), piano damage (Emilia Cruz), broken recovery promise (April 14). Pam bypassed Catalina on April 24 with a final warning mentioning PathFinder Logistics competitor.
- Vendor exposure — did not respond to David's exposure mapping request. Went silent.

**Recent activity:**
- Processed Canopy Q2 relocation requests
- Coordinated NorthWind timeline revisions with Pam Kowalski
- Reply-all'd internal pricing strategy email to Rachel Nguyen at Terraform Digital — removed from account consideration
- Lost Lakeline Logistics $78K deal to a competitor
- Promised Pam Kowalski a NorthWind recovery plan (April 14) — never delivered
- Admitted capacity overload in #operations (April 13)
- Went silent on David's vendor exposure request (April 15)

---

### Emeka Diallo — Account Manager

**Active work:** Managing GreenStack Energy and Mosaic Robotics accounts, plus new business development. Handling the high-severity Mosaic prototype damage claim ($90K robotic arm damaged during Zara Okoye's relocation). Also coordinating Mosaic's April batch (Zara Okoye, Deshawn Hartley, Keiko Tanaka), GreenStack relocations (Priya Venkatesh Houston→Seattle, Noah Fitzgerald Philadelphia→Seattle), and new clients Axiom Precision, Sunbelt VP ($14K, 2 Denver relocations), and Palmetto Foundation ($3,200, 1 Atlanta→Raleigh relocation).

**Key relationships:**
- *Internal:* David Chen (reports to), Fatimah Al-Rashidi (complex relocations), Blessing Okafor / Chloe Vance (ops coordination), Marcus Thorne (damage claim financials)
- *External:* Tamara Byrd at Mosaic Robotics (damage claim), Derek Hollis at GreenStack Energy, Carla Mendes at Sunbelt VP (new client), Rev. at Palmetto Foundation (new client)

**Open threads:**
- Mosaic damage claim — $90K prototype (robotic arm Unit #1) damaged during Zara Okoye's Savannah→Atlanta move. Insurance covers $50K; $40K gap. Incident report sent to Tamara Byrd. Account at risk.
- Mosaic stipend fraud — suspicious receipts for Andre Washington flagged; verification request sent to Tamara.
- Mosaic April batch — Deshawn Hartley (Tampa→Denver, April 19 deadline for Automate 2026), Keiko Tanaka (Columbus→Seattle, Class 3B laser with DOT hazmat requirements).
- GreenStack relocations — Priya Venkatesh and Noah Fitzgerald both heading to Seattle.
- GreenStack hazmat — DOT compliance docs needed for Mei-Lin Zhao (Class 9 lithium).
- Sunbelt/Palmetto invoice crisis — swapped PDFs exposed nonprofit pricing to Sunbelt. Raj Greenfield bypassed Emeka and escalated to David. Carmen Delgado-Reyes flagged audit risk. Emeka eventually sent corrected invoices but damage is done.
- Capacity overload — flagged weeks ago in #operations; acknowledged by Chloe but no reassignment happened.
- Mosaic vendor exposure — flagged Mosaic as exposed to rate increases.

**Recent activity:**
- Filed formal incident report on Mosaic prototype damage (April 15)
- Sent receipt verification request to Tamara Byrd for Andre Washington's suspicious $89 keyboard receipt
- Reported expense auto-categorizer false approvals for Mosaic (coworking exclusion bug, $1,550 exposure)
- Closed Sunbelt VP contract ($14K for 2 relocations) and Palmetto Foundation ($3,200 nonprofit deal)
- Coordinated Axiom intake with Fatimah (under 1 day turnaround)
- Flagged overload in #operations (April 5)
- Went quiet for days after Sunbelt/Palmetto invoice complaints surfaced (April 10-15)
- Eventually reconstructed the invoice swap error and sent corrected communications (April 22)
- Flagged Mosaic as exposed to vendor rate increases (April 15)

---

## Operations

### Chloe Vance — Operations Manager

**Active work:** Running operations at ~85% capacity (11 ongoing relocations across 6 clients in the March 23 week) while managing the DOT hazmat compliance audit. Completed audit of Q1/Q2 hazmat moves and identified 4 shipments requiring documentation; one gap found (Keiko Tanaka's missing placarding certificate). Also coordinating the Heartland Movers billing dispute with Marcus and managing coordinator assignments for complex relocations.

**Key relationships:**
- *Internal:* Fatimah Al-Rashidi, Blessing Okafor, Javier Morales, Suki Patel (coordinators she manages), Marcus Thorne (vendor disputes, DOT costs), Elena Rostova (DOT policy)
- *External:* Greg Pallone at Swift Relocations (volume pricing, hazmat certs), Lisa Kwan at Heartland Movers (billing dispute), Carmen Reyes at UrbanNest (housing)

**Open threads:**
- DOT compliance audit — 4 hazmat moves documented; Keiko Tanaka missing placarding cert (Swift confirmed they'll provide). Hazmat training scheduled April 24 2:00 PM Pacific. Policy implementation in progress.
- Heartland dispute — $4,800 overcharge for 3 moves: Lily Marchetti cancelled Feb 10, Danielle Osei cancelled Feb 13, Priya Venkatesh completed by Swift (not Heartland). Payment hold placed.
- Dr. Mehta executive relocation — assigned Fatimah; 3 workstreams (temp housing, international logistics, closing costs).
- Marcus Webb cold-chain issue — Heartland can't handle lab equipment; coordinated split-vendor with Swift.
- Vendor consolidation — Both vendors raising rates simultaneously. Lakeline backup only covers Austin/Houston. National coverage gap. Flagged capacity crisis to Elena in #executive.
- NorthWind ops timeline — reconstructed chain-of-custody failure (movers arrived 2hrs early, servers warehoused overnight). Found Linear ticket closed without custody log, Airtable showing "In Progress" despite completed move.
- BrightLoop capacity — flagged May as busiest month in MoveOps history (8+ relocations from BrightLoop alone). Surfaced UK relocation and ADA vs ESA service animal policy gaps. Asked about Terraform coordinator hire — not even posted yet.
- StormCloud ops breakdown — reopened Jae-won Kim's Airtable record, created remediation Linear issues.

**Recent activity:**
- Completed hazmat shipment audit and sent results to Marcus (April 21)
- Requested urgent placarding certificate from Swift for Keiko Tanaka move
- Assigned coordinator coverage for April relocation wave
- Coordinated split-vendor solution for Marcus Webb's cold-chain equipment
- Reconstructed NorthWind chain-of-custody timeline in #operations (April 11)
- Surfaced BrightLoop policy/vendor gaps (UK relocation, service animal ADA vs ESA) (April 22-24)
- Flagged coordinator capacity crisis to Elena in #executive (April 24)
- Audited StormCloud ops breakdown, reopened Airtable record (April 24)
- Probed Lakeline Moving for backup vendor capacity — limited to Austin/Houston (April 8)
- Acknowledged Emeka's overload warning but did not reassign (April 5)

---

### Fatimah Al-Rashidi — Relocation Coordinator

**Active work:** Handling the most complex relocations: Dr. Anand Mehta's executive white-glove move (Boston→Chicago, pregnant partner, medical equipment, May 5 deadline), Dr. Kovacs's Nashville→Toronto international move with customs/visa complexity, and GreenStack's lab equipment relocations. Specialist in sensitive equipment and complex logistics.

**Key relationships:**
- *Internal:* Chloe Vance (reports to), Catalina Dubois (Canopy account), Emeka Diallo (GreenStack/Mosaic accounts)
- *External:* Carmen Reyes at UrbanNest (housing), Greg Pallone at Swift (specialized movers), Michael Stern at Atlas (flights), Dr. Anand Mehta at Canopy Health, Patricia Langford at Canopy Health

**Open threads:**
- Dr. Mehta executive relocation — 3 workstreams: temporary housing (River North options sent), medical equipment chain-of-custody (Eizo monitors, secured filing cabinet), household move coordination. May 5 deadline.
- Dr. Kovacs Nashville→Toronto — customs and visa documentation in progress.
- DOT hazmat training — completing certification.

**Recent activity:**
- Sent comprehensive welcome email to Dr. Mehta outlining full relocation process (April 22)
- Forwarded UrbanNest housing options for Dr. Mehta (3 River North/Gold Coast options)
- Confirmed equipment inventory for Dr. Mehta's medical research equipment
- Completed Axiom Precision intake in under 1 day

---

### Blessing Okafor — Relocation Coordinator

**Active work:** Coordinating Canopy Health relocations (Dr. Abdi completed, Lily Marchetti cancelled — employee decided not to relocate) and the Canopy Q2 wave. Identified the cold-chain issue for Marcus Webb's move (Heartland can't handle lab equipment) and arranged split-vendor solution with Swift. Transparent about DOT documentation gaps during compliance audit.

**Key relationships:**
- *Internal:* Chloe Vance (reports to), Catalina Dubois (Canopy account)
- *External:* Carmen Reyes at UrbanNest, Lisa Kwan at Heartland Movers, Greg Pallone at Swift

**Open threads:**
- Marcus Webb Detroit→Chicago — split-vendor coordination (Heartland for household, Swift for cold-chain lab equipment).
- Canopy Q2 wave coordination — multiple moves in pipeline.
- DOT hazmat training — completing certification.
- NorthWind piano damage — admitted walkup assessment underestimated Emilia Cruz stairwell turn radius; Craig Nguyen (KeyMove) sent damage photos.
- BrightLoop vehicle delay — missed Road Runner Auto Transport's April 11 delay email about Marcus Webb's Honda Civic stuck in Indianapolis. Julian took over service recovery.
- Swift driver pushback — reported drivers pushing back on new paperwork requirements during vendor consolidation.

**Recent activity:**
- Flagged missing DOT placarding certificate for Keiko Tanaka's Colorado pickup
- Confirmed Swift has DOT hazmat documentation for tanaka shipment
- Coordinated Dr. Abdi's completed relocation (Minneapolis→Chicago, April 18-19)
- Admitted walkup assessment underestimated Emilia Cruz piano stairwell turn radius (April 11)
- Missed Road Runner delay email for Marcus Webb's Honda Civic (April 11, discovered later)
- Reported Swift driver pushback on new paperwork (April 13)

---

### Javier Morales — Relocation Coordinator

**Active work:** Handling Vectral Systems relocations. Completed Kevin Tran's Portland→Denver economy move. Danielle Osei's Phoenix→Denver move was cancelled (budget reallocation). Now coordinating premium relocations for Daniel Reeves (Seattle→Denver, business class) and Maya Johansson (Portland→Denver, business class).

**Key relationships:**
- *Internal:* Chloe Vance (reports to), Mina Hashimoto (Vectral account)
- *External:* Greg Pallone at Swift, Michael Stern at Atlas, Carmen Reyes at UrbanNest, Kevin Tran / Daniel Reeves / Maya Johansson at Vectral

**Open threads:**
- Daniel Reeves — Seattle→Denver, business class flight confirmed August 14, furnished 2BR downtown. In progress.
- Maya Johansson — Portland→Denver, business class flight being arranged, 1BR quiet area. In progress.

**Recent activity:**
- Coordinated Kevin Tran's Portland→Denver move (economy, $312, completed April 19-20)
- Secured business class tickets for Daniel Reeves; arranging Maya Johansson's

---

### Suki Patel — Relocation Coordinator

**Active work:** Managing BrightLoop Analytics relocation for Jordan Ekwueme (San Diego→Boston) with special requirement — employee wants to visit apartments in person before selecting.

**Key relationships:**
- *Internal:* Chloe Vance (reports to), Mina Hashimoto (BrightLoop account)
- *External:* Jordan Ekwueme at BrightLoop Analytics

**Open threads:**
- Jordan Ekwueme relocation — in-person apartment visits to be scheduled before finalizing housing.
- StormCloud/Jae-won Kim — unsigned Austin lease; promised UrbanNest the guarantor packet but got buried in Deshawn Hartley's trade show deadline. Linear closed prematurely. Airtable shows "Completed" incorrectly. Admitted the miss after Liam Park's escalation.

**Recent activity:**
- Coordinating BrightLoop relocation logistics
- Admitted dropping Jae-won Kim's lease follow-up during Deshawn Hartley scramble (April 24)
- Promised UrbanNest guarantor paperwork — never sent (April 8)
- Sent corrective email to UrbanNest after StormCloud escalation (April 24)

---

## Engineering

### Samira Tariq — Engineering Manager

**Active work:** Leading the expense auto-categorizer project through its post-pilot recovery. After discovery of configuration bugs affecting Vectral (false rejections) and Mosaic (false approvals), she directed the root cause analysis, coordinated the fix deployment, and created a launch readiness gate checklist. Also published the formal AWS cost spike RCA (Vantage Distributed onboarding caused 3x increase). Now planning the receipt hash-check system for duplicate detection.

**Key relationships:**
- *Internal:* Lena Björkström, Dmitri Volkov, Anh Nguyễn (direct reports), Elena Rostova (executive directives), Marcus Thorne (financial exposure), Mina Hashimoto (Vectral client impact), Emeka Diallo (Mosaic client impact)

**Open threads:**
- Expense auto-categorizer relaunch — auto-decisions disabled; fixes deployed for both Vectral and Mosaic configs. Launch readiness checklist defined. Awaiting client validation before re-enablement.
- Duplicate receipt detection (ENG-220) — hash fingerprinting system planned based on Dmitri's audit findings.
- AWS cost controls — CloudWatch alarms and pricing model adjustments being implemented.
- Invoice attachment safeguard — dormant ticket resurfaced after Sunbelt/Palmetto invoice swap; needs prioritization decision.

**Recent activity:**
- Published formal AWS cost spike RCA with recommendations
- Confirmed auto-decisions disabled for Vectral and Mosaic (March 18)
- Completed 47-expense audit: 39 correct (83%), 5 false rejections, 3 false approvals, $885 total exposure
- Created launch readiness gate checklist
- Inherited backlog context on invoice safety ticket after Sunbelt/Palmetto incident (April 16)

---

### Lena Björkström — Software Engineer

**Active work:** Designed and built the core expense auto-categorizer modules (CategoryMatcher, PolicyValidator). Identified the root cause of configuration bugs: string vs. number type mismatch in policy JSON causing incorrect limit comparisons, and silent fallback to default template values. Deployed fixes for both Vectral and Mosaic configurations.

**Key relationships:**
- *Internal:* Samira Tariq (reports to), Dmitri Volkov (testing/QA partner), Anh Nguyễn (dashboard partner)

**Open threads:**
- Schema validation improvements — implementing type-checking in policy loader to prevent future config bugs.
- Policy configuration validation tests integration into deployment gate.
- Invoice attachment safeguard — deprioritized ticket that would have prevented the Sunbelt/Palmetto swap. Now being reconsidered after the incident.

**Recent activity:**
- Fixed Vectral config: corrected string-vs-number type mismatch in policy limits (ergonomic $600, furniture $400, etc.)
- Fixed Mosaic config: changed excluded_categories from string to array, fixed amount validation types
- Identified autoscaling group spike (moveops-api-prod: 4→18 instances) during AWS investigation
- Gathered CloudWatch/Cost Explorer data for RCA
- Deprioritized invoice-attachment safety ticket (became relevant after Sunbelt/Palmetto swap)

---

### Dmitri Volkov — Software Engineer

**Active work:** Led the comprehensive audit of all 47 auto-processed pilot expenses and discovered the duplicate receipt fraud pattern (2 identical SHA-256 hashes across clients). Filed ENG-220 for receipt hash fingerprinting and PDF metadata similarity detection. Conducting edge case testing for the expense auto-categorizer.

**Key relationships:**
- *Internal:* Samira Tariq (reports to), Lena Björkström (development partner), Marcus Thorne (audit findings shared)

**Open threads:**
- Duplicate receipt detection implementation (ENG-220) — receipt hash fingerprinting and PDF metadata similarity scoring system.
- Launch readiness gate checklist — completing remaining items.
- Edge case coverage tests — 6 schema validation tests implemented.

**Recent activity:**
- Completed pilot audit: 47 expenses, found 5 false rejections + 3 false approvals, $885 total exposure
- Discovered duplicate receipt anomalies: identical $89 keyboard receipts (SHA-256 match) submitted by Kevin Tran (Vectral), Andre Washington (Mosaic); identical $45 monitor stand template by Jordan Ekwueme (BrightLoop)
- Filed ENG-220 for hash-check system
- Implemented 6 schema validation tests

---

### Anh Nguyễn — Software Engineer

**Active work:** Built and deployed the expense admin dashboard in staging. Implementing type validation in the policy configuration editor to prevent the kind of config errors that caused the pilot incidents.

**Key relationships:**
- *Internal:* Samira Tariq (reports to), Lena Björkström (backend integration)

**Open threads:**
- Frontend type validation — numeric validation for max_amount fields and array validation for excluded_categories in the policy config editor.
- Dashboard functionality improvements ongoing.

**Recent activity:**
- Deployed expense review dashboard to staging with category, policy limit, and submitted amount display
- Working on type-checking in policy configuration editor

---

## Customer Support

### Julian Brooks — Lead Customer Support Specialist

**Active work:** Secured the largest enterprise contract to date: Vantage Distributed (Terraform Digital), 1,047 employees + ~180 contractors. Coordinating onboarding — requested Catalina set up 3 admin accounts for the self-service portal (Rachel Nguyen, Derek Liu, Sarah Chen). First relocation batch (3 employees, May 5-12) in progress. Acknowledged responsibility for not flagging infrastructure cost implications of the enterprise deal.

**Key relationships:**
- *Internal:* David Chen (coordination), Mina Hashimoto (Terraform account handoff), Samira Tariq (AWS spike attribution)
- *External:* Rachel Nguyen at Terraform Digital/Vantage Distributed

**Open threads:**
- Terraform Digital onboarding — portal live, 3 admin accounts created by Catalina. 3 relocations requested (May 5, 8, 12).
- Infrastructure cost forecasting — needs process for flagging cost implications of large enterprise onboardings.
- BrightLoop service recovery — sent direct apology/status replies to Simone Richter (apartment) and Marcus Webb (car). Escalated to UrbanNest on apartment mismatch.
- NorthWind callback — logged Emilia Cruz's April 12 complaint call about piano damage; no one followed up.
- StormCloud — explained original flight complaint context during Mina's failure reconstruction.

**Recent activity:**
- Forwarded Terraform's first relocation batch request to David Chen (May 1)
- Requested Catalina set up 3 admin accounts for Vantage portal
- Identified as root cause contributor to AWS cost spike during #root-cause-aws-spike investigation
- Took over BrightLoop service recovery for Simone and Marcus Webb (April 23)
- Escalated to UrbanNest about Simone's studio-vs-1BR mismatch (April 23)
- Logged Emilia Cruz phone complaint about piano damage — no follow-up (April 12)
- Contextualized StormCloud's prior flight complaint fix during reconstruction (April 24)

---

### Zara Kovačević — Customer Support Specialist

**Active work:** Handles customer support tickets and escalations. Limited direct presence in tracked Slack channels and email threads.

**Key relationships:**
- *Internal:* Julian Brooks (reports to)

**Open threads:**
- No visible open threads in current artifacts.

**Recent activity:**
- Minimal artifact footprint in the current dataset.

---

### Omar Ibrahim — Customer Support Specialist

**Active work:** Handles customer support tickets and escalations. Limited direct presence in tracked Slack channels and email threads. Misprioritized Jae-won Kim's StormCloud lease document inquiry as low-priority — contributing to the chain of missed handoffs that led to CFO Liam Park's escalation.

**Key relationships:**
- *Internal:* Julian Brooks (reports to)

**Open threads:**
- No visible open threads in current artifacts.
- StormCloud misprioritization — tagged Jae-won Kim's lease document request as low-priority because Airtable showed "Completed." Jae-won's lease was actually unsigned.

**Recent activity:**
- Minimal artifact footprint in the current dataset.
- Logged Jae-won Kim's lease document inquiry as low-priority (April 15)
- Sent polite reply promising to check with relocation team — no follow-through