# MoveOps Inc. — Universe Summary

## The Company

MoveOps Inc. started in 2019 as a boutique luxury travel agency. When the pandemic hit, it nearly went bankrupt. CEO Elena Rostova pivoted the company into a **B2B remote-work relocation service** — helping tech companies relocate employees by sourcing long-term apartments, booking flights, coordinating with moving companies, and managing home-office equipment stipends through a proprietary platform.

**Headquarters:** San Francisco, CA
**Founded:** 2019
**Size:** ~21 employees across 6 departments
**Email domain:** moveops.com
**Timeline:** January–April 2026

### Products & Pricing

| Service | Price |
|---------|-------|
| Apartment sourcing | $1,000 finder's fee per user |
| Flight booking | $20 per flight per user |
| Moving company coordination | $500 per move |
| Stipend platform (SaaS) | $2,000/month flat per client |

Custom pricing can be negotiated per client.

---

## Org Chart

### Executive (2)

| Name | Title | Location | Personality |
|------|-------|----------|-------------|
| **Elena Rostova** | CEO | San Francisco | Visionary, impatient, sends 3 AM emails, demands high-level summaries |
| **Priya Chakrabarti** | Executive Assistant | San Francisco | Elena's gatekeeper — organized, diplomatic, fiercely protective of Elena's time |

### Finance (3)

| Name | Title | Location | Personality |
|------|-------|----------|-------------|
| **Marcus Thorne** | Head of Finance | San Francisco | Stressed, detail-oriented, fixated on margins, distrusts legacy Wanderlust data |
| **Hana Kim** | Accountant | San Francisco | Meticulous, handles daily bookkeeping, frustrated by late expense reports |
| **Alejandro Fuentes** | Financial Analyst | New York | Sharp, numbers-driven, builds pricing models and flags margin risks |

### Customer Engagement (4)

| Name | Title | Location | Personality |
|------|-------|----------|-------------|
| **David Chen** | CE Lead | San Francisco | Empathetic but disorganized, over-promises to VIP clients |
| **Mina Hashimoto** | Account Manager | San Francisco | Diligent, thorough follow-ups, sometimes overwhelmed by David's promises |
| **Catalina Dubois** | Account Manager | Chicago | Confident, handles Midwest enterprise accounts, occasionally over-promises timelines |
| **Emeka Diallo** | Account Manager | Miami | Warm, deep client trust, slow to escalate problems |

### Operations (5)

| Name | Title | Location | Personality |
|------|-------|----------|-------------|
| **Chloe Vance** | Operations Manager | Oakland | Hyper-organized, pragmatic, resents impossible promises from client-facing teams |
| **Fatimah Al-Rashidi** | Relocation Coordinator | San Francisco | Calm under pressure, specializes in international relocations and visa issues |
| **Blessing Okafor** | Relocation Coordinator | Austin | Energetic, great negotiator, sometimes takes shortcuts on documentation |
| **Javier Morales** | Relocation Coordinator | San Francisco | Steady, dependable, thorough docs but slow to adapt to last-minute changes |
| **Suki Patel** | Relocation Coordinator | New York (remote) | Independent, handles East Coast/intl relocations, sometimes out of sync with SF team |

### Engineering (4)

| Name | Title | Location | Personality |
|------|-------|----------|-------------|
| **Samira Tariq** | Engineering Manager | San Jose | Pragmatic, overwhelmed, hates undocumented Slack requests, manages legacy system merge |
| **Lena Bjorkstrom** | Software Engineer | San Francisco | Quiet, productive, backend specialist, prefers async communication |
| **Dmitri Volkov** | Software Engineer | San Francisco (remote) | Opinionated, clashes with Samira on architecture, strong testing advocate |
| **Anh Nguyen** | Software Engineer | Austin (remote) | Junior, eager, overcommits, good at frontend, still ramping on legacy code |

### Customer Support (3)

| Name | Title | Location | Personality |
|------|-------|----------|-------------|
| **Julian Brooks** | Lead CS Specialist (T2) | San Francisco | Charismatic, handles escalations, sometimes promises out-of-policy perks, ex-Wanderlust |
| **Zara Kovacevic** | CS Specialist (T1) | San Francisco | Empathetic, patient, follows process strictly, sometimes escalates too cautiously |
| **Omar Ibrahim** | CS Specialist (T1) | Miami (remote) | Covers afternoon/evening East Coast shifts, quick but can miss nuance |

---

## Communication Channels (Slack)

| Channel | Purpose | Who's in it |
|---------|---------|-------------|
| #general | Company-wide discussions | Everyone |
| #customer-engagement | Client onboarding, account management, relocation scoping | CE team |
| #engineering | Platform dev, bugs, deployments, stipend platform | Engineering team |
| #executive | Leadership strategy, high-level decisions | Executive team |
| #finance | Budgeting, invoicing, vendor payments, margins | Finance team |
| #operations | Apartment sourcing, flight booking, move coordination, vendor mgmt | Operations team |
| #customer-support | Support tickets, escalations, flight delays, platform issues | CS team |
| #announcements | Company-wide updates and milestones | Everyone |

---

## Scenarios

### core_clients — 6 Core Client Relocations

Six active client companies with employee relocations in progress. Relationships range from 2–20 months.

| Company | Industry | HQ | Client Since | HR Contact | Relocating |
|---------|----------|----|--------------|------------|------------|
| Canopy Health | Healthcare Tech | Chicago | Jul 2024 | Patricia Langford (Dir. of HR, patricia.langford@canopyhealth.io) | Dr. Yusuf Abdi, Lily Marchetti |
| Vectral Systems | Enterprise Software | Denver | Nov 2024 | Rachel Whitfield (VP of People, rachel.whitfield@vectralsystems.com) | Kevin Tran, Danielle Osei |
| GreenStack Energy | Clean Energy | Seattle | May 2025 | Derek Hollis (People Ops Mgr, derek.hollis@greenstackenergy.com) | Priya Venkatesh, Noah Fitzgerald |
| PivotPoint Labs | Product Design | Austin | Sep 2025 | Sam Delgado (Co-founder & CEO, sam@pivotpointlabs.com) | Ines Kovac |
| BrightLoop Analytics | Data Analytics | Boston | Dec 2025 | Tessa Moreno (Head of People Ops, tessa.moreno@brightloopanalytics.com) | Jordan Ekwueme |
| Mosaic Robotics | Robotics | Atlanta | Jan 2026 | Tamara Byrd (HR Manager, tamara.byrd@mosaicrobotics.com) | Andre Washington |

**Vendors:** UrbanNest (apartments), Heartland Movers (Midwest), Swift Relocations (long-distance), Atlas Corporate Travel (flights)

**Status:** 4 relocations completed (Abdi, Tran, Venkatesh, Kovac), 5 in progress (Marchetti, Osei, Fitzgerald, Ekwueme, Washington).

### aws_outage — The AWS Bill Mystery

Julian lands the biggest deal ever: **Terraform Digital** (1,200+ employees). They onboard via self-serve portal starting 3/21. AWS costs quietly 3x. Marcus and Alejandro spot the massive invoice on 3/30, escalate to Samira. She creates #root-cause-aws-spike, investigates with Lena, and traces it to the Terraform onboarding traffic. Elena directs the team to add cost alerts and fix the pricing model.

| Who | Role in this scenario |
|-----|-----------------------|
| Julian Brooks | Closed the deal |
| Rachel Nguyen | Customer contact (Terraform Digital) |
| Marcus Thorne, Alejandro Fuentes | Flagged the invoice |
| Samira Tariq, Lena Bjorkstrom | Led the investigation |
| Elena Rostova | Set directives |

### am_productivity — Account Manager Performance Benchmarking

Q1 2026 performance data for three AMs (Mina, Catalina, Emeka) designed to enable productivity comparisons. Includes cold outreach to 13 new prospect companies, contract negotiations, customer complaints, satisfaction surveys, and repeat business. Catalina closes the biggest deals but has the worst CSAT (5.5/10) and 2 escalations; Mina has the best margin (38%) and zero escalations; Emeka builds the deepest relationships with 8.5 CSAT and repeat customers.

| AM | Revenue | Margin | CSAT | Escalations | Style |
|----|---------|--------|------|-------------|-------|
| Mina Hashimoto | $40,200 | 38% | 8.5 | 0 | Detail-oriented, thorough |
| Catalina Dubois | $64,800 | 32% | 5.5 | 2 | Aggressive, over-promises |
| Emeka Diallo | $46,700 | 29% | 8.5 | 0 | Relationship-driven, warm |

**Clients closed (8 new contracts):**

| Company | AM | Relocations | Deal Value | Notes |
|---------|----|-------------|-----------|-------|
| Greenleaf Design Studio | Mina | 2 | $9,000 | Repeat customer, reference client candidate |
| StormCloud Analytics | Mina | 3 | $26,400 | Premium package; had flight booking complaint |
| Mosswood Development | Mina | 2 | $4,800 | Repeat customer from Q4 2025 |
| NorthWind Technologies | Catalina | 5 | $60,000 | Enterprise tier; aggressive timeline caused issues |
| Prairie Data Consulting | Catalina | 1 | $4,800 | Basic package; declined upsell |
| Sunbelt Venture Partners | Emeka | 3 | $21,000 | Repeat customer, strong personal relationship |
| Palmetto Community Foundation | Emeka | 1 | $3,200 | Custom nonprofit rate (5% margin) |
| Tideway Hospitality Tech | Emeka | 3 | $22,500 | Long 2.5-month sales cycle |

### active_relocations — April Relocation Wave

The biggest relocation batch since the Terraform onboarding — 10 employees across all 6 core clients moving in April 2026. Each client's HR contact emails their assigned AM to request 1–2 new relocations, the AM acknowledges and coordinates logistics, then Hana generates QuickBooks invoices. Chloe posts an ops capacity breakdown assigning coordinators, and David runs a team check-in in #customer-engagement.

| Who | Role in this scenario |
|-----|-----------------------|
| Catalina Dubois | AM for Canopy Health (2 relocations) and PivotPoint Labs (1) |
| Mina Hashimoto | AM for Vectral Systems (2 premium) and BrightLoop Analytics (2) |
| Emeka Diallo | AM for GreenStack Energy (1) and Mosaic Robotics (2) |
| Hana Kim | Invoicing — 6 invoices totaling $56K |
| Chloe Vance | Ops capacity planning and coordinator assignments |
| David Chen | CE team check-in on the relocation wave |

### expensebot — The Expense Auto-Categorizer Fiasco

The engineering team builds an internal tool to auto-categorize and approve/deny relocation expense reimbursements — replacing the old manual email process. After 2 months of architecture debates and development, Samira launches a prototype with Vectral Systems and Mosaic Robotics. It immediately breaks both ways: Vectral employees get legitimate expenses rejected (stale default policy limits), while Mosaic employees get out-of-policy expenses approved (malformed JSON config). AMs intervene, leadership escalates, and Elena mandates a rollout pause. Dmitri's audit finds an 83% accuracy rate (39/47 correct), and the team pivots to human-review mode while fixing the config pipeline.

| Who | Role in this scenario |
|-----|-----------------------|
| Samira Tariq | Project lead, coordinates remediation |
| Lena Bjorkstrom | Root cause analysis — finds config pipeline bugs |
| Dmitri Volkov | Writes audit + schema validation tests |
| Anh Nguyen | Built the frontend dashboard |
| Mina Hashimoto | Escalates Vectral false rejections, apologizes to Rachel Whitfield |
| Emeka Diallo | Discovers Mosaic false approvals ($885 exposure) |
| Marcus Thorne | Raises financial concern about out-of-policy approvals |
| David Chen | Escalates client relationship impact |
| Elena Rostova | Issues pause directive, mandates full audit |
| Rachel Whitfield (Vectral) | Complains about Danielle Osei's rejected $475 chair |

### noah_move — The Two Noahs Mix-Up

Axiom Precision Manufacturing responds to Emeka's cold outreach wanting to relocate senior engineer Noah Fitzpatrick from Philadelphia to Seattle in April 2026. Emeka hands coordination to Fatimah, who is already managing GreenStack Energy's Noah Fitzgerald relocation to Seattle in the same timeframe. Despite explicitly confirming "Fitzpatrick = Axiom, Fitzgerald = GreenStack," Fatimah searches her files for "Noah," pulls the wrong record, and sends GreenStack's confirmed apartment, flight, and shipping details to the Axiom employee. Noah Fitzpatrick accepts without question, forwards it to his HR director, and the error becomes embedded in CRM, Linear, and Slack — completely undetected.

| Who | Role in this scenario |
|-----|-----------------------|
| Emeka Diallo | Account manager; hands off Axiom coordination to Fatimah |
| Fatimah Al-Rashidi | Relocation coordinator; makes the critical mix-up between the two Noahs |
| Carla Mendenhall (Axiom) | HR Director; signs off on the (wrong) confirmation |
| Noah Fitzpatrick (Axiom) | Senior engineer; unknowingly accepts GreenStack's itinerary |
| Noah Fitzgerald (GreenStack) | Employee whose confirmed move details are mistakenly reused |
| Derek Hollis (GreenStack) | Provides finalized details that get sent to the wrong person |

### cold_outreach — Sales Pipeline (54 Prospect Companies)

54 prospect companies across diverse industries (tech, biotech, fintech, consulting, healthcare, legal, manufacturing, etc.) contacted via cold outreach emails by three account managers (Catalina, Mina, Emeka). Outreach spread across Jan–Mar 2026.

- Each company received 1–2 cold emails (initial + optional follow-up)
- 6 prospects replied with interest (questions about services, pricing, or specific relocation needs)
- 3 of those got follow-up replies from account managers

### relocate — Andre Washington's Columbus-to-Seattle Move

Tamara Byrd at Mosaic Robotics requests a relocation for Andre Washington from Columbus, GA to Seattle, WA. Emeka acknowledges and hands off to ops; Chloe assigns Suki Patel as coordinator. Suki emails Atlas Corporate Travel to book a flight, and the vendor confirms Columbus (CMH) to Seattle (SEA). Suki posts the confirmation in #operations and Emeka sends the full relocation package — flight, apartment, movers — back to Tamara.

| Who | Role in this scenario |
|-----|-----------------------|
| Tamara Byrd (Mosaic Robotics) | Initiates the relocation request |
| Emeka Diallo | Account manager; coordinates between client and ops |
| Chloe Vance | Ops manager; assigns coordinator |
| Suki Patel | Relocation coordinator; handles logistics and vendor contact |
| Derek Saunders (Atlas Corporate Travel) | Flight vendor; confirms CMH→SEA booking |

### vendor_dispute — Heartland Movers Overbilling

Heartland Movers submits their Q1 2026 bill for 8 moves ($12,800) but Chloe's review against the Airtable Relocations table finds only 5 legitimate charges. Two moves (Lily Marchetti and Danielle Osei) were cancelled in February — Chloe emailed Jake Loomis at Heartland both times but never got an acknowledgment. The 8th charge is for Priya Venkatesh, whose move was handled by Swift Relocations, not Heartland. Marcus puts a $12,800 payment hold in QuickBooks and sends a formal dispute requesting a corrected invoice for $8,000. Total overbilling: $4,800.

| Who | Role in this scenario |
|-----|-----------------------|
| Chloe Vance | Reviews bill against Airtable, identifies $4,800 overbilling, creates Linear tracking ticket |
| Marcus Thorne | Puts payment hold in QuickBooks, sends formal dispute to Heartland |
| Hana Kim | Flags discrepancy in reconciliation tracker |
| Jake Loomis (Heartland Movers) | Vendor contact; submitted the Q1 invoice, never acknowledged cancellation emails |

### bulk_canopy — Canopy Health Q2 Triple Relocation (Visa, Cold-Chain, Storage Gap)

Patricia Langford requests three new relocations for Canopy Health — each with a distinct complication. Dr. Renata Kovacs (Nashville → Toronto) is an international cross-border move requiring TN visa documentation, Canadian customs broker (BorderEase Customs), and personal effects declaration. Marcus Webb (Detroit → Chicago) has cryogenic lab equipment (-20°C) that Heartland Movers can't handle, requiring a split-vendor arrangement with Swift Relocations for cold-chain freight. Tyler Okonkwo (Philadelphia → Denver) must vacate by April 18 but his Denver lease doesn't start until May 1, creating a 13-day storage gap. Chloe flags a coordinator scheduling conflict on April 11 in #operations and shifts Tyler's dates by one day. Fatimah flags visa/customs complexity, Blessing discovers the cold-chain limitation and proposes the split-vendor workaround, and Chloe confirms all airtable records updated — all coordinated via Slack threads in #operations. Hana posts the invoice breakdown in #finance with Marcus replying on surcharge approval process. Total invoice: $9,210 (including $2,650 in surcharges pending client approval).

| Who | Role in this scenario |
|-----|-----------------------|
| Patricia Langford (Canopy Health) | Requests all 3 relocations, needs to approve surcharges |
| Catalina Dubois | Account manager; coordinates with Patricia and ops |
| Chloe Vance | Ops manager; identifies coordinator conflict in #operations, assigns Fatimah/Blessing/Javier |
| Fatimah Al-Rashidi | Coordinator for Dr. Kovacs — flags visa/customs complexity in #operations |
| Blessing Okafor | Coordinator for Marcus Webb — discovers Heartland can't do cold-chain, proposes split-vendor in #operations |
| Javier Morales | Coordinator for Tyler Okonkwo — handles temp storage arrangement |
| Hana Kim | Posts invoice to #finance, flags pending surcharge approval |
| Marcus Thorne | Replies in #finance on surcharge approval process |

### bulk_brightloop — BrightLoop April Relocations (Rush + Vehicle Shipping)

BrightLoop's Tessa Moreno requests two new employee relocations to Boston. Simone Richter (Data Platform Lead, Chicago → Boston) is a rush 5-day turnaround — her lease ends April 6, requiring expedited packing, temp housing, and a $750 rush surcharge. Marcus Webb (Senior Analyst, Atlanta → Boston) needs his 2019 Honda Civic shipped via a third-party auto transporter (Road Runner Auto Transport) since Swift Relocations doesn't handle vehicles — adding $1,100 to the invoice. Total invoice: $11,350.

| Who | Role in this scenario |
|-----|-----------------------|
| Tessa Moreno (BrightLoop) | Initiates both relocation requests, approves vehicle shipping add-on |
| Mina Hashimoto | Account manager; coordinates logistics, flags vehicle shipping as new service line |
| Chloe Vance | Ops manager; confirms Swift capacity and rush feasibility |
| David Chen | Receives internal account update from Mina |

### bulk_mosaic — Mosaic Robotics April Relocations (Prototypes, Trade Show Deadline, Laser Cutter)

Tamara Byrd requests three relocations for Mosaic Robotics. Zara Okoye (Savannah → Atlanta) is relocating two proprietary robotic arm prototypes ($180K insured) requiring anti-vibration foam crating and climate-controlled transport via Heartland Movers. Deshawn Hartley (Tampa → Denver) has a hard April 19 delivery deadline — he's the lead presenter at Automate 2026 trade show (April 21–24, Denver Convention Center). Keiko Tanaka (Columbus → Seattle) has a 400-lb Epilog Fusion Pro industrial laser cutter (Class 3B CO2 laser, DOT hazmat placarding required) plus an 8-day lease gap needing interim storage. Dual-client flag: Deshawn's partner is Simone Richter (BrightLoop), currently being relocated by MoveOps. Total invoice: $9,010.

| Who | Role in this scenario |
|-----|-----------------------|
| Tamara Byrd (Mosaic) | Requests all 3 relocations with detailed equipment specs |
| Emeka Diallo | Account manager; coordinates logistics, hands off to ops, updates David Chen |
| Chloe Vance | Ops capacity review, vendor assignments, confirms dual-client flag doesn't need COI |
| Blessing Okafor | Coordinator for Zara Okoye (Savannah → Atlanta) |
| Suki Patel | Coordinator for Deshawn Hartley (Tampa → Denver, trade show deadline) |
| Javier Morales | Coordinator for Keiko Tanaka (Columbus → Seattle, laser cutter + storage) |
| Hana Kim | Posts invoice to #finance |

### bulk_pivotpoint — PivotPoint Labs April Relocations (H-1B Visa, Brooklyn Walkup CNC Mill)

Sam Delgado requests two relocations for PivotPoint Labs — both to Austin. Nadia Okonjo (San Francisco → Austin) is an H-1B visa holder (Nigerian national) whose address change must be coordinated with immigration attorney Lorraine Pham within the USCIS 10-day reporting window. Diego Castañeda (Brooklyn → Austin) has a 600-lb Tormach CNC mill ($42K insured) in a 5th-floor walkup with no elevator — requiring walkup surcharge, custom vibration-dampened crating, climate-controlled freight, cargo insurance rider, and 10 days of interim storage (lease gap). Total invoice: $10,650.

| Who | Role in this scenario |
|-----|-----------------------|
| Sam Delgado (PivotPoint) | Requests both relocations, provides detailed equipment specs |
| Catalina Dubois | Account manager; coordinates logistics, sends internal update to David Chen |
| Hana Kim | Posts invoice to #finance, flags non-standard surcharges |

### bulk_greenstack — GreenStack Energy April Relocations (HAZMAT Batteries, Oversize Solar Rig)

Derek Hollis requests two relocations for GreenStack Energy — both involving specialty lab/industrial equipment. Mei-Lin Zhao (Houston → Portland) is relocating with Class 9 lithium-ion battery test modules (~350 lbs, 4 crated modules) requiring UN3481-certified packaging and DOT-certified hazmat transport via Swift Relocations. Joaquín Reyes (Phoenix → Seattle) has a 900-lb rooftop solar panel testing rig (8ft × 4ft × 3ft) needing custom crating and flatbed transport via Heartland Movers. Chloe flags vendor concerns and storage leads in Slack. Total invoice: $9,440 (including $1,800 hazmat surcharge, $950 overweight equipment surcharge, and $150 interim hazmat storage).

| Who | Role in this scenario |
|-----|-----------------------|
| Derek Hollis (GreenStack) | Requests both relocations, provides detailed equipment specs and shutdown schedule |
| Emeka Diallo | Account manager; coordinates logistics, sends internal update to David Chen |
| Chloe Vance | Flags vendor capacity and storage concerns in Slack |
| Hana Kim | Posts invoice to #finance, flags non-standard line items |

### bulk_vectral — Vectral Systems April Relocations (ESA Dog, ADA Housing, Tight Lease)

Rachel Whitfield requests three new relocations for Vectral Systems. Priya Suresh (Portland → Denver) is relocating with an 85-lb emotional support German Shepherd, requiring pet-friendly housing and ESA documentation coordination. Terrence Nakamura (Austin → San Francisco) is a wheelchair user needing ADA-accessible housing with roll-in shower, 36-inch doorways, and no-step entry — plus a split shipment for his motorized wheelchair. Camille Oduya (Boston → Seattle) has a tight 2-day window due to an early lease release on April 12. Total invoice: $15,900 (including pet relocation, ADA housing premium, and split-shipment surcharges).

| Who | Role in this scenario |
|-----|-----------------------|
| Rachel Whitfield (Vectral) | Requests all 3 relocations with detailed employee needs |
| Mina Hashimoto | Account manager; coordinates logistics, sends internal update to David Chen |
| Hana Kim | Posts invoice to #finance |

### bulk_northwind — NorthWind Technologies Denver Expansion (Chain-of-Custody, Grand Piano)

Pam Kowalski requests two relocations for NorthWind Technologies' new Denver satellite office — both from Chicago. Raj Patel (Principal Architect) is relocating a home server lab (4 rack-mounted servers, ~2,400 lbs, lithium UPS batteries = hazmat) containing proprietary source code — NorthWind's CISO Victor Huang mandates supervised loading with an IT security escort, direct transport with no warehouse storage, and a signed chain-of-custody log. This is brand-new territory for MoveOps. Emilia Cruz (Director of Marketing) is relocating with her partner's Steinway Model B grand piano (7ft, 480 lbs) requiring a specialty subcontractor since neither Heartland nor Swift handle pianos, plus her Chicago lease runs until May 15 but NorthWind needs her in Denver by April 18 — creating a 27-day double-rent overlap. Chloe flags both moves as high-complexity in #operations; David Chen frames the account as a recovery opportunity after Catalina's earlier timeline issues. Total invoice: $14,700.

| Who | Role in this scenario |
|-----|-----------------------|
| Pam Kowalski (NorthWind) | Requests both relocations, sends lease details for early termination |
| Victor Huang (NorthWind CISO) | Sends chain-of-custody and security escort requirements for Raj's server lab |
| Catalina Dubois | Account manager; coordinates logistics, sends internal update to David Chen |
| Chloe Vance | Ops assessment in #operations — flags chain-of-custody as new territory, evaluates vendor capacity |
| Hana Kim | Posts invoice to #finance with provisional surcharge line items |
| David Chen | Responds in #customer-engagement — frames NorthWind as account recovery opportunity, flags chain-of-custody as potential new service line |

### canopy_exec_relocation — Canopy CMO White-Glove Relocation (Chain-of-Custody, Pregnant Partner)

Canopy Health's Patricia Langford emails Mina requesting an urgent executive relocation for newly hired CMO Dr. Anand Mehta (Boston → Chicago, May 5 start). Complications: two calibrated lab monitors worth ~$12K each plus a 350-lb secured filing cabinet requiring chain-of-custody documentation, 3–4 weeks temporary corporate housing while his condo closes, and his partner is 7 months pregnant — fully white-glove required. Mina escalates to Chloe, who assigns Fatimah as coordinator. Fatimah creates Linear issues for three workstreams (housing, equipment/chain-of-custody, main move), contacts Dr. Mehta directly for his equipment inventory, and emails UrbanNest for temporary furnished housing in River North. Marcus creates a QuickBooks estimate for the full-service package. David notes the strategic retention signal in #customer-engagement; Mina updates the Canopy CRM deal with the executive relocation add-on.

| Who | Role in this scenario |
|-----|-----------------------|
| Patricia Langford (Canopy Health) | Initiates the request, provides Dr. Mehta's contact info |
| Dr. Anand Mehta (Canopy Health) | New CMO being relocated; replies with equipment inventory and housing preferences |
| Mina Hashimoto | Account manager; receives request, escalates to ops, updates CRM |
| Chloe Vance | Ops manager; assigns Fatimah, asks Marcus to flag priority billing |
| Fatimah Al-Rashidi | Coordinator; creates Linear issues, contacts Dr. Mehta and UrbanNest |
| Marcus Thorne | Creates QuickBooks estimate for the executive relocation package |
| Carmen Reyes (UrbanNest) | Responds with temporary housing options in River North |
| David Chen | Notes retention signal in #customer-engagement |

### damage_claim — Mosaic Prototype Damage ($90K Insurance Claim)

One of Mosaic Robotics' two robotic arm prototypes ($90K insured each) arrives in Atlanta with a cracked servo motor housing and misaligned joint calibration after transport by Heartland Movers. Tamara Byrd demands a full incident report within 48 hours. Emeka escalates to Chloe in #operations, who pulls the original bulk_mosaic move details and compiles a chain-of-custody timeline. Blessing Okafor admits she signed off on the packing without verifying the anti-vibration foam crating density spec — she was juggling Tyler Okonkwo's Canopy move the same day. Chloe discovers the delivery receipt was signed by a Mosaic intern (not Zara), complicating the claim window. Marcus flags a $40K insurance coverage gap — MoveOps' vendor liability only covers $50K per item. Hana books an insurance claim and liability accrual in QuickBooks. Emeka sends the formal incident report to Tamara proposing replacement shipping at MoveOps' cost.

| Who | Role in this scenario |
|-----|-----------------------|
| Tamara Byrd (Mosaic) | Demands incident report, copies VP of Engineering |
| Zara Okoye (Mosaic) | Reports the prototype damage |
| Emeka Diallo | Account manager; escalates to ops, sends formal incident report |
| Chloe Vance | Compiles timeline, discovers intern delivery receipt issue |
| Blessing Okafor | Coordinator who didn't verify foam density spec |
| Marcus Thorne | Flags $40K insurance gap in #finance |
| Hana Kim | Books insurance claim and liability accrual |

### contract_renegotiation — Vectral Threatens to Leave (10% Loyalty Discount Negotiation)

Rachel Whitfield sends a formal email to Mina demanding a 15% discount on Vectral's Q3 2026 contract or they walk — citing the ExpenseBot fiasco (Danielle Osei's $475 chair rejected), the stipend fraud investigation friction (Kevin Tran's flagged receipt), and Catalina's original onboarding timeline failures. Mina escalates to David in #customer-engagement, who loops Marcus and Alejandro for financial impact analysis. Alejandro calculates Vectral's total value at $109,900+ with 32% margin — a 15% discount drops margin below MoveOps' 25% floor. Elena weighs in via #executive: approved counter is 10% loyalty discount with 12-month extension and 8-relocation minimum commitment. Mina sends the counter-proposal; Rachel pushes back at 12%; David holds firm at 10% with added sweeteners (dedicated coordinator, priority scheduling). CRM deal updated through stages (at risk → negotiation → renewal pending). Airtable Client Accounts record updated with renegotiation notes.

| Who | Role in this scenario |
|-----|-----------------------|
| Rachel Whitfield (Vectral) | Sends formal discount demand citing pattern of service failures |
| Mina Hashimoto | Account manager; escalates, drafts counter-proposal, holds firm at 10% |
| David Chen | CE lead; loops in finance, briefs Mina on approved strategy, advises holding firm |
| Alejandro Fuentes | Runs detailed financial analysis ($109.9K revenue, 32% margin) |
| Marcus Thorne | Posts financial summary in #finance |
| Elena Rostova | Approves 10% discount + 12-month extension in #executive |

### compliance_audit — DOT Hazmat Documentation Audit ($50K+ Fine Exposure)

A DOT compliance officer (Linda Castellano, PHMSA) sends a formal inquiry to Marcus requesting documentation for all hazmat-classified shipments coordinated by MoveOps in 2026 — triggered by a routine audit of Swift Relocations. Marcus immediately forwards to Chloe and posts in #finance flagging $50K+ fine exposure. Chloe searches Airtable Relocations and identifies 4 hazmat-related moves: Mei-Lin Zhao / GreenStack (lithium batteries), Keiko Tanaka / Mosaic (laser cutter), Raj Patel / NorthWind (UPS batteries), and Joaquín Reyes / GreenStack (oversize solar rig). She discovers a critical gap: Blessing never filed the DOT placarding certificate for the Mosaic laser cutter move — she has Swift's verbal confirmation but no signed document. Chloe creates Linear tickets for each move's documentation status and contacts Swift to obtain a retroactive copy. Marcus requests a 15-day extension from DOT (granted). Hana books a fine accrual in QuickBooks. Elena mandates a new policy in #general: all hazmat moves require a signed DOT documentation checklist before completion in Airtable. Chloe schedules mandatory hazmat training for all coordinators.

| Who | Role in this scenario |
|-----|-----------------------|
| Linda Castellano (DOT/PHMSA) | Sends formal compliance inquiry, grants 15-day extension |
| Marcus Thorne | Forwards DOT inquiry, flags financial exposure, requests extension |
| Chloe Vance | Compiles hazmat move list, discovers Blessing's documentation gap, creates Linear tickets, contacts Swift |
| Blessing Okafor | Admits she never filed the placarding certificate for Mosaic laser cutter |
| Greg Pallone (Swift Relocations) | Confirms placarding was done, sends signed certificate retroactively |
| Hana Kim | Books fine accrual in QuickBooks |
| Elena Rostova | Mandates new hazmat documentation policy company-wide |

### terraform_onboarding — Terraform Digital's Chaotic First Relocations (Reply-All Disaster)

Rachel Nguyen requests the first 3 employee relocations under Terraform Digital's new contract. Julian forwards the request to David excitedly, but all three AMs decline ownership — Mina is buried in Vectral's renegotiation, Catalina is managing NorthWind's complex moves, and Emeka is handling the Mosaic damage claim. David escalates the AM capacity crisis to Elena in #executive. While internal pricing discussions circulate via email, Catalina accidentally Reply-Alls the internal thread to Rachel — exposing MoveOps' volume discount modeling. Rachel immediately demands the discussed discount. Elena intervenes: assigns the account to Mina, orders Catalina to apologize, and announces a dedicated Terraform coordinator hire in #announcements. Mina begins scoping the 3 relocations and creates CRM/Airtable/QuickBooks records.

| Who | Role in this scenario |
|-----|-----------------------|
| Rachel Nguyen (Terraform Digital) | Requests first 3 relocations, exploits leaked pricing to demand volume discount |
| Julian Brooks | Forwards request with excitement, triggers account ownership debate |
| David Chen | CE lead; pushes back on Julian owning the account, escalates AM capacity crisis to Elena |
| Mina Hashimoto | Declines initially (Vectral crisis), later assigned as account owner, begins scoping |
| Catalina Dubois | Declines initially (NorthWind), accidentally Reply-Alls internal pricing to Rachel |
| Emeka Diallo | Declines citing Mosaic damage claim workload |
| Alejandro Fuentes | Provides volume discount financial modeling |
| Elena Rostova | Assigns account to Mina, mandates apology, announces coordinator hire |

### stipend_fraud — Suspicious Expense Patterns

After the ExpenseBot pause, Dmitri runs a data quality audit on all Airtable stipend transactions and discovers three suspicious submissions from employees at three different clients — all involving the same vendor (TechComfort Supply). Kevin Tran (Vectral) and Andre Washington (Mosaic) submitted byte-for-byte identical $89 receipts (same SHA-256 hash), while Jordan Ekwueme (BrightLoop) submitted a $245 receipt generated from the same PDF template. Marcus puts holds on pending payments ($634 exposure) and the AMs contact client HR to verify. Elena mandates a new policy: receipt verification required for all stipend submissions over $200.

| Who | Role in this scenario |
|-----|-----------------------|
| Dmitri Volkov | Runs the audit, discovers duplicate receipt hashes and PDF template matches |
| Marcus Thorne | Investigates QuickBooks payments, puts holds on pending reimbursements, raises $1,023 exposure |
| Mina Hashimoto | Contacts Rachel Whitfield at Vectral to verify Kevin Tran's receipt |
| Emeka Diallo | Contacts Tamara Byrd (Mosaic) and Tessa Moreno (BrightLoop) to verify receipts |
| Elena Rostova | Mandates receipt verification policy for submissions >$200 |
| Samira Tariq, Lena Bjorkstrom | Weigh in on engineering approach for automated duplicate detection |

### brightloop_expansion — BrightLoop Series B Expansion Overwhelms MoveOps

BrightLoop Analytics closes its Series B and Tessa Moreno requests 6 new May relocations — including a first-ever UK transfer (Oliver Bancroft from London), an ADA service animal case, and a CTO expecting white-glove treatment. Meanwhile, the first batch is still broken: Simone Richter's apartment is a studio instead of the promised 1BR (8 days unanswered), and Marcus Webb's car is stuck in Indianapolis with Blessing's unread Road Runner email. A buried January cold email from UK vendor Meridian Global Mobility becomes the only lead for international capability. Chloe flags coordinator capacity at breaking point; Elena doesn't respond.

| Who | Role in this scenario |
|-----|-----------------------|
| Tessa Moreno (BrightLoop) | VP of People; requests 6 May relocations, cites board visibility |
| Mina Hashimoto | Account manager; realizes first batch isn't clean, escalates combined crisis |
| Chloe Vance | Ops manager; surfaces policy gaps, flags capacity crisis to executive |
| Fatimah Al-Rashidi | International coordinator; assesses UK relocation risk and gaps |
| Blessing Okafor | Coordinator who missed Road Runner's delay email while overloaded |
| Julian Brooks | Takes over service recovery for Simone and Marcus Webb |
| Alejandro Fuentes | Maps pricing gaps — no international or white-glove tiers exist |
| Marcus Thorne | Pushes back on ad hoc premium pricing without margin guardrails |
| David Chen | Requests temp coordinator hire; Elena doesn't respond |

### client_churn_crisis — NorthWind Account Implodes (Competitor Threat + Multiple Failures)

NorthWind Technologies' account is falling apart on multiple fronts. CISO Victor Huang sends a furious breach report after Raj Patel's server lab relocation violated chain-of-custody protocol (movers arrived 2 hours early, loaded without the IT escort, servers sat overnight in a warehouse). Meanwhile, Emilia Cruz's Steinway piano was scratched during extraction. Catalina Dubois promises Pam Kowalski a recovery plan on April 14 but never follows through. On April 24, Pam bypasses Catalina entirely and sends David Chen a formal final warning — NorthWind has been talking to PathFinder Logistics and wants a retention proposal by Friday or they walk.

| Who | Role in this scenario |
|-----|-----------------------|
| Victor Huang (NorthWind CISO) | Sends furious security breach report about server lab violation |
| Pam Kowalski (NorthWind HR) | Issues final warning to David, mentions PathFinder competitor |
| Catalina Dubois | Account manager; overwhelmed, promises recovery plan but never delivers |
| Chloe Vance | Reconstructs ops timeline, finds Linear/Airtable documentation gaps |
| Craig Nguyen (KeyMove) | Reports piano damage with stairwell photos |
| Blessing Okafor | Admits walkup assessment underestimated the turn radius |
| Julian Brooks | Logs Emilia Cruz's unanswered complaint call |
| Alejandro Fuentes | Drafts unfinished retention pricing model |
| David Chen | Escalates Catalina's overload to Elena; assembles retention response after Pam's warning |
| Elena Rostova | Declines to formally redistribute accounts — "handle it within the team" |

### stormcloud_expansion_gone_wrong — StormCloud's Premium Account Unravels (Lease Failure + Dropped Referral)

StormCloud Analytics was supposed to be MoveOps' showcase premium client, but everything quietly fell apart. Suki Patel's Jae-won Kim relocation to Austin hit a wall when UrbanNest flagged an unsigned lease — the landlord wants guarantor paperwork MoveOps never sent. Suki promised to follow up but got buried in Deshawn Hartley's trade show deadline, and the Linear ticket was closed prematurely while Airtable still shows "Completed." Meanwhile, Omar Ibrahim misprioritized Jae-won's lease inquiry as low-priority, Simone Richter's standing desk stipend is stuck in Marcus's blanket freeze, and a warm referral from StormCloud's Anya Petrova to Ridgeline Robotics went completely unanswered — David celebrated it in Slack but nobody contacted the prospect. CFO Liam Park escalates all failures at once, forcing Mina to reconstruct the hidden chain of missed handoffs.

| Who | Role in this scenario |
|-----|-----------------------|
| Liam Park (StormCloud CFO) | Escalates multi-issue failure, demands resolution before leadership review |
| Jae-won Kim (StormCloud) | Employee with unsigned Austin lease, sends polite follow-ups |
| Anya Petrova (StormCloud) | Sends warm referral to Ridgeline Robotics — never answered |
| Kenji Watanabe (Ridgeline Robotics) | Prospect who followed up twice with no response |
| Mina Hashimoto | Account manager; reconstructs failures, prepares recovery plan |
| Suki Patel | Coordinator who dropped Jae-won's lease follow-up during Deshawn scramble |
| Chloe Vance | Audits ops breakdown, reopens Airtable record, creates remediation Linear issues |
| Omar Ibrahim | Misprioritizes Jae-won's support ticket as low-priority |
| Marcus Thorne | Discovers $500 goodwill credit was posted to wrong estimate |
| Julian Brooks | Contextualizes the original flight complaint fix that never fully landed |
| David Chen | Realizes the Ridgeline referral was never entered into CRM or answered |

### sunbelt_palmetto_cross_contamination — Swapped Invoices Expose Nonprofit Pricing to For-Profit Client

Hana Kim batch-sends April invoices but accidentally swaps the PDF attachments for Sunbelt Venture Partners ($4,800 standard rate) and Palmetto Community Foundation ($2,400 nonprofit rate). Sunbelt's Raj Greenfield sees the nonprofit header and realizes he's been paying double what a nonprofit gets for the same service. Palmetto's Carmen Delgado-Reyes sees the inflated $4,800 amount and flags it as an audit risk for their nonprofit records. Emeka Diallo — who manages both accounts — goes quiet for days as the situation festers. The root cause traces back further: Lena deprioritized an engineering safety ticket for invoice-attachment validation, and Emeka had flagged his overload weeks earlier but Chloe acknowledged it without reassigning. Marcus frames it as pricing policy exposure comparable to the Terraform leak.

| Who | Role in this scenario |
|-----|-----------------------|
| Hana Kim | Sends the invoice batch with swapped PDF attachments |
| Raj Greenfield (Sunbelt VP) | Spots the nonprofit rate and escalates to David, bypassing Emeka |
| Carmen Delgado-Reyes (Palmetto) | Flags the inflated invoice as an audit risk |
| Emeka Diallo | Account manager for both clients; goes quiet, eventually reconstructs the error |
| David Chen | Forces cross-functional reckoning, compares to Terraform exposure |
| Marcus Thorne | Identifies pricing policy exposure, pushes for invoice controls |
| Lena Bjorkstrom | Had deprioritized the invoice safety ticket months earlier |
| Samira Tariq | Inherits the backlog context on the dormant safeguard ticket |
| Chloe Vance | Had acknowledged Emeka's overload warning but never reassigned |

### vendor_consolidation — Both Moving Vendors Raise Rates Simultaneously

Heartland Movers and Swift Relocations both announce rate increases in the same week. Swift imposes an immediate 18% surcharge plus a $400 hazmat premium, while Heartland ties its 12% increase to the unresolved Q1 overbilling dispute — refusing to finalize new rates until the $4,800 discrepancy is settled. Chloe probes backup vendor Lakeline Moving but they can only cover local Austin/Houston moves, not MoveOps' national footprint. Blessing reports Swift drivers pushing back on new paperwork requirements. Hana discovers additional Heartland reconciliation gaps beyond the original dispute. Alejandro models margin exposure showing 6-8 point compression across all active client contracts. David asks AMs to map client exposure — Mina flags Vectral and BrightLoop, Emeka flags Mosaic, but Catalina goes silent. Elena orders a formal vendor strategy memo by end of week; Marcus inherits the unfinished crisis.

| Who | Role in this scenario |
|-----|-----------------------|
| Chloe Vance | Probes backup vendor capacity, signals ops concern early |
| Greg Pallone (Swift) | Announces 18% rate increase and hazmat surcharge |
| Jake Loomis (Heartland) | Ties rate hike to unresolved dispute |
| Blessing Okafor | Reports driver pushback on new Swift paperwork |
| Hana Kim | Discovers broader Heartland reconciliation gaps |
| Alejandro Fuentes | Models margin exposure across client contracts |
| David Chen | Requests client exposure map from AMs |
| Mina Hashimoto | Flags Vectral and BrightLoop as most exposed |
| Emeka Diallo | Flags Mosaic exposure |
| Catalina Dubois | Goes silent — doesn't respond to exposure request |
| Elena Rostova | Orders vendor strategy memo |
| Marcus Thorne | Inherits the unfinished crisis as response owner |

---

## Airtable — MoveOps Operations (`appMoveOpsOps001`)

### Relocations (`tblRelocations01`) — 63 records

Tracks all employee relocations managed by MoveOps.

| Field | Type | Options |
|-------|------|---------|
| Name | singleLineText | |
| Company | singleLineText | |
| Status | singleSelect | Inquiry, In Progress, Completed, Cancelled |
| Origin | singleLineText | |
| Destination | singleLineText | |
| Move Start Date | date | |
| Move End Date | date | |
| Assigned Coordinator | singleLineText | |
| Special Requirements | multilineText | |

### Stipend Transactions (`tblStipends00001`) — 33 records

Tracks home-office stipend expense submissions and approvals for client employees.

| Field | Type | Options |
|-------|------|---------|
| Employee Name | singleLineText | |
| Account | singleLineText | |
| Expense Category | singleLineText | |
| Amount Requested | number | |
| Has Receipt | checkbox | |
| Date | date | |
| Approval Status | singleSelect | Pending, Approved, Partially Approved, Rejected |
| Approved Amount | number | |
| Review Notes | multilineText | |

### Client Accounts (`tblClientAccts01`) — 69 records

Maps client companies to their assigned MoveOps account managers with relationship details.

| Field | Type | Options |
|-------|------|---------|
| Client | singleLineText | |
| Account Manager | singleLineText | |
| Relationship Start Date | date | |
| Contract Type | singleLineText | |
| Monthly Stipend Fee | number | |
| Total Relocations | number | |
| Status | singleSelect | Active, Onboarding, Churned, Prospect, Cold Outreach |
| Notes | multilineText | |
