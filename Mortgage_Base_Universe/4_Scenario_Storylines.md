# Mortgage Broker Scenario Storylines

70 scenario storylines for the Keystone Mortgage Solutions universe. Each describes a realistic situation drawn from real-world complaints, regulatory actions, and industry problems. These are storylines only — not yet tied to specific actors or IDs in the universe. They will be converted into structured scenario YAMLs later.

**Sources:** CFPB complaint database, Reddit/BiggerPockets forums, HousingWire, MPA Magazine, TRID case studies, FBI wire fraud reports, appraiser discrimination settlements, state regulatory enforcement actions.

---

## Scenario Group 1: Borrower Documentation & Underwriting Issues

### 1. The Unexplained Large Deposit
A borrower's bank statement shows a $14,000 cash deposit two weeks before application. The underwriter flags it and requests a letter of explanation. The borrower says it was from selling furniture on Facebook Marketplace but has no receipts. The processor has to work with the borrower to produce acceptable documentation — or the loan stalls. Meanwhile, rate lock is ticking down.

### 2. Employment Change Mid-Process
A borrower who was pre-approved as a salaried W-2 employee quits their job and starts freelancing three weeks before closing. The underwriter finds out through a verbal verification of employment (VVOE) call and the loan immediately goes from clear-to-close back to suspended. The processor has to figure out if the loan can still work under different guidelines, or if it's dead.

### 3. The Resubmission Loop
An underwriter sends back conditions requesting 2 months of bank statements. The borrower uploads only the most recent month. The processor requests the missing month. The borrower uploads the same document again. This happens three times over 10 days, and the closing date is now at risk. The processor's Slack has increasingly frustrated messages about the borrower, and the loan officer is getting pressure from the realtor.

### 4. Divorce Decree Missing
A borrower discloses they're divorced, but the file has no divorce decree. The underwriter conditions it. The borrower says their ex-spouse has the only copy and won't cooperate. The processor has to guide the borrower to get a court-certified copy from the county clerk — while explaining that without it, they can't verify alimony/child support obligations or confirm the ex is off the title.

### 5. IRS Transcript Mismatch
The borrower's tax returns show $95,000 in income but the IRS 4506-T transcript comes back showing $72,000. The borrower swears the returns they provided are correct and gets angry. The processor has to explain that the lender relies on IRS records, not the paper returns, and the loan may need to be restructured at a lower loan amount — or denied.

### 6. Gift Fund Documentation Gap
The borrower's down payment includes a $20,000 gift from their parents. The gift letter is signed, but the underwriter also needs the donor's bank statement showing the withdrawal and the borrower's account showing the deposit. The parents are uncomfortable sharing their financials and push back. The loan officer has to navigate a sensitive conversation without losing the deal.

### 7. Self-Employed Borrower Write-Offs
A self-employed borrower's tax returns show $180,000 gross revenue but only $48,000 net income after aggressive business deductions. They're frustrated that the lender qualifies them on the lower number. The loan officer has to explain qualifying income vs. taxable income, and explore whether a bank statement loan program might work — at a higher rate.

### 8. Expired Documents Cascade
A loan has been in process for 75 days due to various delays. Now the original credit report, bank statements, and pay stubs have all expired (60-day shelf life). The processor has to request fresh versions of everything, which feels like starting over. The borrower is furious and threatens to go to another lender.

---

## Scenario Group 2: Appraisal Problems

### 9. Low Appraisal on Purchase
The purchase price is $385,000 but the appraisal comes back at $355,000 — a $30,000 gap. The buyer doesn't have cash to cover the difference. The loan officer has to coordinate between the buyer's agent and listing agent to renegotiate the price, while simultaneously filing a reconsideration of value (ROV) with better comps. Time pressure is intense because the rate lock expires in 8 days.

### 10. Appraisal Flags Unpermitted Addition
The appraiser notes that the home's finished basement appears to be unpermitted — square footage doesn't match county records. The underwriter won't accept the additional square footage for valuation. The purchase price was based on that extra space. Now the deal may fall apart unless the seller can produce permits or the price comes down.

### 11. Comparable Sales Dispute
A refinance appraisal in a rapidly appreciating neighborhood uses comps from 6 months ago that don't reflect recent sales. The homeowner provides three recent sales within 0.2 miles that are $50K higher but the appraiser won't revise. The loan officer debates whether to order a second appraisal (at the borrower's cost) or file a formal ROV complaint.

### 12. Appraisal Reveals Structural Issue
During the appraisal inspection, the appraiser notes significant foundation cracks and water damage in the crawl space, making the property ineligible for conventional financing in its current condition. The loan needs to either switch to a renovation loan product or the seller needs to complete repairs before closing — neither of which can happen in the remaining timeline.

---

## Scenario Group 3: Rate Lock & Pricing Issues

### 13. Rate Lock Expiration — Processor Delay
A 45-day rate lock is expiring in 3 days but the file hasn't been submitted to underwriting yet because the processor was overloaded. The rate has gone up 0.375% since the lock. The branch manager has to decide whether to pay for a lock extension out of the company's margin, eat the cost on a renegotiated rate, or have a difficult conversation with the borrower about who caused the delay.

### 14. Borrower Wants to Float After Locking
After locking at 6.875%, rates drop to 6.5% the following week. The borrower demands the lower rate. The loan officer has to explain that locks are binding commitments and the lender won't honor a float-down unless the lock agreement includes that provision (it doesn't). The borrower threatens to cancel and go elsewhere, which would mean starting the entire process over.

### 15. Rate Lock on Wrong Program
A loan officer accidentally locks a rate on a 30-year fixed conventional product when the borrower actually needs an FHA loan (different rate sheet). The error isn't discovered until underwriting reviews the file 10 days later. Now the rate for the correct product is 0.25% higher. The branch manager has to negotiate with the lender and decide who absorbs the cost.

### 16. Lender Repricing Mid-Lock
A wholesale lender announces a mid-day rate adjustment that cancels all locks made that morning due to a bond market sell-off. The loan officer locked three loans at 9:15 AM and the repricing hit at 10:30 AM. Two of the three locks are honored, but one is contested because the lock confirmation wasn't fully processed in the lender's system. The borrower on that loan is already under contract with a closing date set.

---

## Scenario Group 4: Wire Fraud & Security

### 17. Business Email Compromise — Closing Wire
Three days before closing, the borrower receives an email that looks like it's from the title company with "updated wire instructions." The email address is off by one character. The borrower wires $47,000 to the fraudulent account. The title company, brokerage, and borrower all point fingers. The processor was the last person to email the borrower and may have been the compromised account.

### 18. Phishing Attack on Loan Officer
A loan officer receives an email appearing to be from a wholesale lender's portal, asking them to verify their credentials. They click the link and enter their login. Attackers now have access to the lender portal, which contains dozens of borrowers' SSNs, financial records, and personal information. The compliance officer has to initiate a data breach response.

### 19. Borrower Identity Verification Failure
During the final verification call before closing, the title company asks the borrower security questions and they fail two of three. It turns out the "borrower" has been communicating via email with slightly different personal details than what's on the original application. The processor has to halt the closing and investigate whether this is a case of identity theft or simply outdated information.

### 20. Unauthorized Access to Borrower File
A loan officer who recently left the company is discovered to still have active credentials to the LOS. Audit logs show they accessed three client files after their termination date. The compliance officer has to determine what data was viewed, notify affected borrowers, and assess whether the ex-employee was poaching clients or something worse.

---

## Scenario Group 5: TRID & Compliance Violations

### 21. Closing Disclosure Delivered Late
The closing disclosure was supposed to be delivered 3 business days before closing (Wednesday for a Saturday closing). Due to a processor oversight, it wasn't sent until Thursday evening. Now the closing either has to be pushed to the following week — jeopardizing the rate lock — or someone signs off on a compliance violation. The compliance officer flags it, the branch manager wants to push through anyway.

### 22. Fee Tolerance Violation
Between the Loan Estimate and Closing Disclosure, the title insurance fee increased by $800, which exceeds the 10% tolerance for services the borrower could shop for. The compliance team catches this during a pre-closing audit. The lender will have to issue a cure (refund the difference to the borrower) or risk regulatory penalties. The question is whether the brokerage or the lender bears the cost.

### 23. APR Disclosure Discrepancy
A borrower changed from a 30-year to a 15-year loan mid-process. The Loan Estimate was never re-issued to reflect the term change. At closing, the APR on the Closing Disclosure doesn't match the original LE by more than the allowed tolerance. This triggers a mandatory 3-day waiting period reset, pushing the closing past the rate lock expiration.

### 24. Incorrect Loan Estimate Timing
A loan officer provides a Loan Estimate to a prospective borrower before collecting all six required pieces of information (name, income, SSN, property address, estimated value, loan amount). The compliance team discovers this during a routine file review. The LE may be invalid, and the entire disclosure timeline may need to restart.

### 25. Missing Change of Circumstance Documentation
The borrower's loan amount changed after the initial LE because they decided to put less money down. The processor updated the numbers but never documented the "change of circumstance" that justified the revised LE. An internal audit flags the gap. Without proper documentation, the revised LE is technically invalid and all downstream disclosures may be non-compliant.

---

## Scenario Group 6: Communication & Relationship Breakdowns

### 26. Realtor Pressures for Status Updates
A listing agent calls the loan officer four times in one day demanding a closing update because their seller is threatening to walk. The loan officer has been waiting on the underwriter and has no new information. The realtor escalates to the branch manager, who discovers the file has actually been sitting in a queue untouched for 5 days due to an internal routing error.

### 27. Borrower Goes Silent
A borrower who was responsive for the first 3 weeks suddenly stops replying to emails, texts, and calls. They have 4 outstanding underwriting conditions. The rate lock expires in 12 days. The processor tries reaching them through the realtor, then the co-borrower. It turns out the borrower is having second thoughts about the purchase but is too anxious to say so directly.

### 28. Dual Communication Channels Confusion
The borrower has been texting the loan officer, emailing the processor, and calling the front desk with different questions and document submissions. Nobody has a complete picture. A critical document (the HOI binder) was texted to the loan officer's personal phone and never made it into the file. It's discovered missing at the pre-closing review.

### 29. Language Barrier Miscommunication
A borrower whose first language isn't English signs documents they don't fully understand. After closing, they discover their loan has a prepayment penalty they didn't expect. They contact the brokerage claiming they were never told. The signed disclosures say otherwise, but the borrower insists the loan officer verbally said there was no penalty. No interpreter was used or documented.

### 30. Angry Borrower Public Review
A borrower whose loan was denied posts a 1-star Google review naming the loan officer personally and accusing the brokerage of discrimination. The review contains factual inaccuracies but also some legitimate complaints about response times. The branch manager has to decide how to respond publicly without violating the borrower's privacy (can't discuss the loan) while also investigating the claims internally.

---

## Scenario Group 7: Internal Operations & Process Failures

### 31. File Assignment Mix-Up
Two borrowers with similar last names (Martinez/Martínez) get their files confused in the LOS. Conditions meant for one file get attached to the other. The error isn't caught until a borrower calls asking why they're being asked to provide a divorce decree when they've never been married. Several days of work on the wrong file have to be unwound.

### 32. Processor Overwhelm — Dropped Ball
A processor handling 35 active files misses a critical condition deadline on a loan. The lender's automated system suspends the file. By the time the processor notices (3 days later), the lock has expired and the borrower's closing date has passed. The realtor is threatening to sue. The branch manager has to reassign the file and do damage control.

### 33. New Hire Training Gap
A newly hired junior processor submits a loan to underwriting without running the automated compliance check first. The underwriter kicks it back with 15 conditions — most of which would have been caught and resolved before submission. This adds a week to the timeline and makes the brokerage look sloppy to the wholesale lender.

### 34. Technology System Outage
The brokerage's LOS goes down for 6 hours during a critical closing day. Three closings are scheduled, and processors can't access file documents, conditions, or status information. They have to work from email attachments and personal notes. One closing proceeds with a minor error in the CD that has to be corrected with a post-closing amendment.

### 35. Commission Dispute Between Loan Officers
Two loan officers both claim credit for the same borrower referral. LO #1 says they got the referral from a realtor partner, LO #2 says the borrower called them directly first. The CRM shows conflicting entries. The branch manager has to review CRM notes, email timestamps, and phone records to determine the correct assignment — and the losing LO is furious.

---

## Scenario Group 8: Third-Party & Vendor Issues

### 36. Title Search Reveals Lien
A title search on a refinance reveals an old mechanic's lien from a contractor who did work 4 years ago and was never paid. The homeowner says they did pay, but can't produce a lien release. The title company won't insure until the lien is resolved. The borrower has to track down the contractor, get a release signed, and have it recorded — which could take weeks.

### 37. HOI Cancellation Right Before Closing
The borrower's homeowners insurance policy gets cancelled 2 days before closing because the insurer did a property inspection and found a trampoline and an aggressive-breed dog — both policy exclusions. The processor has to scramble to find a new insurance provider that will bind coverage before the closing date.

### 38. Vendor Quality Dispute
The brokerage's preferred appraiser consistently returns appraisals 5-7 days late, causing cascading delays across multiple files. The branch manager wants to remove them from the preferred list, but they're the only licensed appraiser covering a particular rural county where the brokerage has several active loans. Finding a replacement takes time and the current pipeline suffers.

### 39. Title Company Wire Delay
On closing day, the title company confirms all documents are signed and funds are being wired. But the wire from the lender doesn't arrive by 3 PM (the bank's cutoff). Recording can't happen until the next business day — which is a Monday because it's Friday afternoon. The seller can't receive the proceeds over the weekend and their own purchase (which was contingent on this sale) is now in jeopardy.

### 40. Surveyor Discovers Encroachment
A survey ordered as part of the loan process reveals that the neighbor's fence extends 3 feet onto the subject property, and the seller's shed encroaches onto the neighbor's property. These encroachments need to be resolved before title insurance can be issued. The buyers are upset because the seller listed the property with inaccurate lot lines.

---

## Scenario Group 9: Borrower Fraud & Misrepresentation

### 41. Straw Buyer Suspicion
A loan application comes in for an "owner-occupied" purchase, but the processor notices the borrower already owns three other investment properties in the same zip code and the subject property is a duplex. The loan officer didn't ask enough questions. The compliance officer suspects this may be an investor trying to get better owner-occupied rates and orders an occupancy investigation.

### 42. Fabricated Employment
The verbal verification of employment call to the borrower's employer goes to a Google Voice number that the employer supposedly uses as their main line. The person who answers sounds suspiciously similar to the borrower. The underwriter flags it and requests additional verification — W-2s with an EIN lookup, IRS transcripts, and LinkedIn profile verification. The borrower starts getting evasive.

### 43. Debt Omission — Co-Signed Loan
A borrower's credit report is clean, but during underwriting, a co-signed auto loan they didn't disclose shows up on a credit supplement pull. The monthly payment pushes their debt-to-income ratio over the limit. The borrower claims they forgot about it because they're not the one making payments. The processor has to determine if the loan can still work with the added liability.

### 44. Inflated Income — Side Gig
A borrower claims $2,000/month in Uber income on their application. When asked for documentation, they provide screenshots of their Uber driver dashboard showing gross fares — not net income after expenses, car payments, and gas. Their actual net is closer to $600/month. The loan officer has to recalculate qualifying income and potentially restructure the deal.

---

## Scenario Group 10: Market & Timing Pressures

### 45. Bidding War Pressure
A borrower in a competitive market waives the appraisal contingency to win a bidding war. The appraisal comes in $40,000 below the contract price. Now the borrower is contractually obligated to cover the gap in cash — which they don't have. The loan officer has to explore alternatives (different lender with portfolio product, FHA 203k, family gift) before the contract deadline.

### 46. Rate Shock on Renewal
A borrower with a 3.25% rate from 2021 is trying to buy a second home and is shocked that current rates are 6.75%. They keep asking the loan officer to "find a better rate" and want to wait for rates to drop. Meanwhile, they're under contract with a closing deadline. The loan officer has to manage expectations while keeping the deal alive.

### 47. Builder Delay Cascading to Lock
A new construction purchase has a rate lock tied to the estimated completion date. The builder is 6 weeks behind schedule due to permit delays. The lock has already been extended once. A second extension will cost 0.375% — about $1,500 on this loan. The borrower argues the builder should pay, the builder says it's not their problem, and the brokerage is caught in the middle.

### 48. Multiple Offer Fallout
A borrower's offer was rejected twice before being accepted on a third property. Each time, the brokerage pulled credit and issued disclosures. Now the borrower's credit score has dropped slightly from the three hard pulls, pushing their rate tier up. The loan officer has to explain why the rate is now higher than originally quoted, even though the borrower feels like they've been a loyal customer.

---

## Scenario Group 11: Post-Closing & Servicing

### 49. Post-Closing Escrow Surprise
A borrower closes successfully, but 3 months later their monthly payment jumps by $400 because the escrow analysis reveals the original tax estimate was wrong — property taxes in the county were reassessed upward. The borrower blames the brokerage for the estimate, even though taxes are based on county records that changed after closing. The loan officer gets an angry call.

### 50. Servicing Transfer Confusion
Six weeks after closing, the borrower's loan is sold to a different servicer. The borrower doesn't see the transfer notice (it went to spam) and continues paying the original servicer. The payment gets returned. The borrower misses a payment to the new servicer and gets a 30-day late mark on their credit. They call the brokerage furious, even though the brokerage has no control over servicing transfers.

---

## Summary by Category

| Category | Scenarios | Count |
|----------|-----------|-------|
| Borrower Documentation & Underwriting | 1–8 | 8 |
| Appraisal Problems | 9–12 | 4 |
| Rate Lock & Pricing | 13–16 | 4 |
| Wire Fraud & Security | 17–20 | 4 |
| TRID & Compliance | 21–25 | 5 |
| Communication & Relationship | 26–30 | 5 |
| Internal Operations & Process Failures | 31–35 | 5 |
| Third-Party & Vendor Issues | 36–40 | 5 |
| Borrower Fraud & Misrepresentation | 41–44 | 4 |
| Market & Timing Pressures | 45–48 | 4 |
| Post-Closing & Servicing | 49–50 | 2 |
| **Total** | | **50** |

---

## Scenario-to-Component Matrix

Each scenario below lists the MCP servers it should touch and what artifacts to create on each. This guides the LLM scenario generator to produce multi-component scenarios rather than email-only ones.

### 1. The Unexplained Large Deposit
- **mortgage_los**: Condition (pending, type: "Large Deposit Explanation", attached to loan)
- **email**: Processor → borrower requesting explanation letter; borrower replies with weak explanation; processor escalates to LO
- **filesystem**: Bank statement PDF showing the deposit; borrower's uploaded explanation letter
- **slack**: #loan-processing — processor asks Elena about acceptable documentation for FB Marketplace sales
- **calendar**: Rate lock expiration event creating urgency; processor adds follow-up task for condition in 3 days
- **crm**: Engagement note: "Condition follow-up needed — borrower has 3 days to produce receipts"

### 2. Employment Change Mid-Process
- **mortgage_los**: Loan status change from clear_to_close → suspended; new condition (VVOE verification)
- **email**: Underwriter notification; processor → borrower asking about employment change; LO → realtor explaining delay
- **slack**: #loan-processing — "Anyone dealt with a borrower switching to 1099 mid-process?"
- **crm**: Engagement note: "VVOE came back — borrower no longer employed at [company]"
- **notion**: Look up lender overlay for self-employment guidelines

### 3. The Resubmission Loop
- **mortgage_los**: Condition status stays "pending" for 10+ days; document checklist items repeatedly uploaded
- **email**: 3+ cycles of processor requesting docs and borrower uploading wrong ones; processor sends final "URGENT" email with bold subject
- **slack**: #loan-processing — increasingly frustrated messages about the borrower; LO mentions realtor pressure; DM between processor and LO about escalation
- **calendar**: Closing date event that keeps getting closer; follow-up tasks for each document request attempt
- **crm**: Engagement notes tracking each failed attempt: "Attempt 3 — borrower uploaded same July statement again"

### 4. Divorce Decree Missing
- **mortgage_los**: Condition (pending, type: "Divorce Decree"), loan stalled
- **email**: Processor → borrower explaining requirement; borrower replies about uncooperative ex; processor guides to county clerk
- **filesystem**: Eventually uploaded divorce decree PDF
- **crm**: Engagement note: "Borrower emotional about divorce documentation requirements"

### 5. IRS Transcript Mismatch
- **mortgage_los**: IRS 4506-T transcript shows different income; potential restructure or denial
- **email**: Processor → borrower explaining discrepancy; borrower angry reply; LO → borrower with restructured options
- **filesystem**: Tax return PDFs vs IRS transcript showing $23K discrepancy
- **slack**: #loan-processing — "Has anyone had a 4506-T come back this far off?"

### 6. Gift Fund Documentation Gap
- **mortgage_los**: Condition (pending, type: "Gift Documentation — donor bank statement + deposit verification")
- **email**: LO → borrower explaining gift documentation requirements; borrower says parents won't share; LO navigates sensitively
- **filesystem**: Gift letter PDF; eventually donor bank statement
- **crm**: Engagement note from LO: "Delicate situation — parents reluctant to share financials"

### 7. Self-Employed Borrower Write-Offs
- **mortgage_los**: Qualifying income at $48K net vs $180K gross; potential program switch to bank statement loan
- **email**: LO → borrower explaining qualifying income vs taxable income; borrower frustrated; LO presents bank statement program option at higher rate
- **filesystem**: Tax returns showing deductions; P&L statement
- **notion**: Look up bank statement loan program guidelines (Non-QM lenders)
- **quickbooks**: If borrower is vendor/contractor — invoice history showing actual revenue

### 8. Expired Documents Cascade
- **mortgage_los**: Multiple document checklist items expired (credit report, bank statements, pay stubs past 60-day shelf life)
- **email**: Processor → borrower requesting all fresh documents; borrower furious ("feels like starting over"); LO apologizes for delays
- **slack**: #loan-processing — processor venting about 75-day file; Elena assigns Tyler to help; DM Elena→Tyler with checklist of expired items
- **calendar**: Original closing date already passed; new follow-up events for each expired document request
- **crm**: Engagement note: "File day 75 — all docs expired. Borrower extremely frustrated. Tyler assisting."

### 9. Low Appraisal on Purchase
- **mortgage_los**: Appraisal value at $355K vs $385K purchase price; ROV filed
- **email**: LO → buyer's agent about gap; LO → listing agent for price renegotiation; appraiser gets ROV with better comps
- **filesystem**: Appraisal PDF; comparable sales data
- **slack**: #loan-processing — "Appraisal came in $30K short on the [borrower] file"
- **calendar**: Rate lock expiration in 8 days
- **crm**: Engagement note: "Coordinating ROV and price renegotiation simultaneously"

### 10. Appraisal Flags Unpermitted Addition
- **mortgage_los**: Appraisal notes unpermitted basement; valuation reduced
- **email**: Processor → buyer and seller agents about permit issue; title company needs resolution
- **filesystem**: Appraisal PDF with appraiser notes; county records showing square footage discrepancy
- **notion**: Look up lender overlay — which lenders accept unpermitted additions with caveats?

### 11. Comparable Sales Dispute
- **mortgage_los**: Refinance appraisal uses stale comps; ROV filed with recent sales data
- **email**: Homeowner provides recent sales; LO debates second appraisal option with borrower
- **filesystem**: Appraisal PDF; homeowner's comp evidence
- **quickbooks**: Second appraisal fee ($475) if ordered — who pays?

### 12. Appraisal Reveals Structural Issue
- **mortgage_los**: Property ineligible for conventional financing; loan product needs to change to renovation loan
- **email**: Processor → borrower about structural findings; LO → realtor about timeline impact; discussion of FHA 203k option
- **filesystem**: Appraisal PDF with structural issue photos/notes
- **slack**: #loan-processing — "Anyone done a 203k conversion mid-process?"
- **notion**: Look up FHA 203k program requirements

### 13. Rate Lock Expiration — Processor Delay
- **mortgage_los**: 45-day lock expiring in 3 days; file not submitted to underwriting yet
- **email**: Branch manager (Grace) → processor asking why file delayed; LO → borrower about potential rate change
- **slack**: #rate-watch — Camille flags the expiring lock; #loan-processing — Grace asks about the backlog; DM Grace→processor for explanation
- **calendar**: Rate lock expiration event (urgent); Camille's daily lock monitoring schedule
- **quickbooks**: Rate lock extension fee ($375) if extended — bill to company since internal delay
- **crm**: Engagement note: "Lock expiring in 3 days — file not submitted. Internal delay, processor backlog."

### 14. Borrower Wants to Float After Locking
- **mortgage_los**: Lock at 6.875%; current market at 6.5%
- **email**: Borrower demands lower rate; LO explains lock commitment; borrower threatens to cancel
- **notion**: Look up rate lock policy — does the lock agreement include float-down provision?
- **crm**: Engagement note: "Borrower extremely upset about rate lock. Considering cancellation."

### 15. Rate Lock on Wrong Program
- **mortgage_los**: Lock on conventional when borrower needs FHA; error discovered 10 days later
- **email**: LO admits error to branch manager; Grace negotiates with lender
- **slack**: #rate-watch — "Locked on wrong program — need to renegotiate with [lender]"
- **quickbooks**: Potential cost to company for the 0.25% rate difference
- **crm**: Engagement note documenting the error for QC review

### 16. Lender Repricing Mid-Lock
- **mortgage_los**: 3 locks from morning; repricing at 10:30 AM cancels unprocessed locks
- **email**: LO → lender contesting the unprocessed lock; LO → borrower about the situation
- **slack**: #rate-watch — Camille: "ALERT: [lender] mid-day reprice. All morning locks need confirmation."
- **calendar**: Borrower's closing date already set

### 17. Business Email Compromise — Closing Wire
- **mortgage_los**: Closing in 3 days; wire fraud incident
- **email**: Spoofed email from fake title company; real title company confirms fraud; borrower's frantic emails; processor sends "STOP — DO NOT WIRE" email
- **contacts**: Spoofed email address differs by one character from real title company contact
- **slack**: #closings — "URGENT: [borrower] may have wired to wrong account"; #compliance-alerts — data breach assessment; DM to branch manager
- **crm**: Engagement note: "WIRE FRAUD ALERT — borrower may have wired $47K to fraudulent account. Phone call made immediately."

### 18. Phishing Attack on Loan Officer
- **mortgage_los**: Potential data breach affecting multiple borrower files
- **email**: Phishing email from fake lender portal; compliance notification to affected borrowers
- **slack**: #it-support — Raj investigates compromised credentials; #compliance-alerts — Denise initiates breach response
- **contacts**: List of all borrowers whose data was accessible through compromised portal
- **notion**: Look up data breach response procedure

### 19. Borrower Identity Verification Failure
- **mortgage_los**: Closing halted; investigation triggered
- **email**: Title company reports failed verification; processor escalates; investigation emails
- **contacts**: Compare application contact details with current communication details — discrepancies
- **crm**: Engagement notes documenting identity verification timeline

### 20. Unauthorized Access to Borrower File
- **mortgage_los**: Audit logs show post-termination access to 3 client files
- **email**: Compliance → Robert (owner) about the breach; notification emails to affected borrowers
- **slack**: #compliance-alerts — Denise flags unauthorized access; #it-support — Raj checks access logs and revokes credentials
- **notion**: Look up employee offboarding checklist — was credential revocation missed?

### 21. Closing Disclosure Delivered Late
- **mortgage_los**: CD delivery missed by 1 day; compliance violation
- **email**: Compliance officer flags the error; branch manager wants to proceed anyway; debate about pushing closing
- **slack**: #compliance-alerts — Denise: "CD timing violation on [loan number]. This is not optional."
- **calendar**: Closing event that needs rescheduling
- **notion**: Look up Keystone's 5-business-day CD delivery policy (stricter than federal 3-day)

### 22. Fee Tolerance Violation
- **mortgage_los**: Title insurance fee increased $800 between LE and CD (exceeds 10% tolerance)
- **email**: Compliance catches it pre-closing; discussion about who bears the cure cost
- **notion**: Look up TRID fee tolerance rules — which fees are in which tolerance bucket?
- **quickbooks**: TRID tolerance cure payment — debit to acct_compliance_fines
- **slack**: #compliance-alerts — "Fee tolerance violation on [loan]. Cure required."

### 23. APR Disclosure Discrepancy
- **mortgage_los**: Borrower changed from 30yr to 15yr; LE never re-issued; APR mismatch triggers 3-day reset
- **email**: Processor realizes error; compliance confirms mandatory waiting period; LO informs borrower of delay
- **notion**: Look up when a new LE is required (change of circumstance rules)
- **calendar**: Closing pushed past rate lock expiration

### 24. Incorrect Loan Estimate Timing
- **mortgage_los**: LE issued before all 6 trigger items collected
- **email**: Compliance flags during file review; discussion about restarting disclosure timeline
- **notion**: Look up the 6 required LE trigger items and timing requirements
- **slack**: #compliance-alerts — "Training reminder: LE cannot be issued until all 6 items received"

### 25. Missing Change of Circumstance Documentation
- **mortgage_los**: Loan amount changed; no COC documented; revised LE technically invalid
- **email**: Internal audit finding; processor explains the oversight; compliance requires retroactive documentation
- **notion**: Look up change of circumstance documentation requirements
- **crm**: Engagement note: "Internal audit finding — COC documentation gap"

### 26. Realtor Pressures for Status Updates
- **mortgage_los**: File sitting in queue untouched for 5 days (internal routing error)
- **email**: Realtor → LO (4 calls in one day demanding update); realtor escalates to branch manager; Grace discovers routing error
- **crm**: Engagement log: 4 calls from realtor; branch manager involved
- **slack**: #loan-processing — Grace: "Who has the [borrower] file? It hasn't been touched in 5 days"
- **calendar**: Original closing date approaching

### 27. Borrower Goes Silent
- **mortgage_los**: 4 outstanding conditions; rate lock expiring in 12 days
- **email**: Processor emails (3+); LO emails; co-borrower contacted; realtor contacted — all unanswered
- **crm**: Engagement notes: "Borrower unresponsive x7 days"; "Called borrower — went to voicemail"; "Contacted co-borrower — says borrower is 'thinking'"; "May be having second thoughts"
- **slack**: #loan-processing — "Anyone heard from [borrower]? 7 days no contact"; DM LO→processor: "I think they're getting cold feet"
- **calendar**: Follow-up call attempts scheduled; rate lock expiration event

### 28. Dual Communication Channels Confusion
- **mortgage_los**: HOI binder missing from file at pre-closing review
- **email**: Borrower emails processor with some docs; a separate email to LO's personal inbox with HOI binder (never forwarded to file)
- **crm**: Fragmented engagement notes: "Borrower called front desk with questions"; "Borrower emailed HOI to LO's personal email — not in system"
- **slack**: #closings — "Missing HOI binder on [loan] — anyone have it?"; DM LO: "Oh wait, borrower sent it to my personal email last week"
- **calendar**: Pre-closing review meeting where gap was discovered

### 29. Language Barrier Miscommunication
- **mortgage_los**: Loan closed but borrower discovers unexpected prepayment penalty
- **email**: Post-closing complaint from borrower; brokerage reviews signed disclosures
- **contacts**: Borrower's language preference not documented
- **crm**: Engagement note: "Borrower claims LO verbally said no prepayment penalty"
- **notion**: Look up fair lending and language access policies

### 30. Angry Borrower Public Review
- **email**: Internal emails discussing the review; investigation of response time complaints
- **crm**: Full engagement history for the denied borrower — were response times actually slow?
- **slack**: #general — Team sees the review; Robert discusses public response strategy
- **notion**: Look up fair lending policy — is there any discrimination concern?

### 31. File Assignment Mix-Up
- **mortgage_los**: Two files with similar names (Martinez/Martínez) get conditions swapped
- **email**: Confused borrower contacts processor about wrong conditions
- **slack**: #loan-processing — "Who mixed up the Martinez files? Conditions are on the wrong loan"
- **crm**: Engagement note documenting the error and correction

### 32. Processor Overwhelm — Dropped Ball
- **mortgage_los**: Condition deadline missed; file suspended; lock expired
- **email**: Realtor threatening legal action; branch manager doing damage control; apology to borrower
- **slack**: #loan-processing — Grace reassigns file; discussion about workload distribution; DM Grace→processor: "We need to talk about your pipeline"
- **calendar**: Original closing date passed; new pipeline review meeting scheduled
- **crm**: Engagement notes documenting the timeline of the failure: "Day 1: condition received"; "Day 5: still not addressed"; "Day 10: lock expired"

### 33. New Hire Training Gap
- **mortgage_los**: 15 conditions kicked back on file submitted without compliance check
- **email**: Underwriter feedback; Tyler asks for help
- **slack**: #loan-processing — Tyler asks Elena for guidance; Elena walks through the checklist
- **notion**: Look up submission checklist and pre-submission compliance check procedure

### 34. Technology System Outage
- **mortgage_los**: 6-hour outage on closing day; 3 closings affected
- **email**: Processors working from email attachments and personal notes
- **slack**: #it-support — Raj troubleshooting; #closings — workaround coordination; #general — outage announcement
- **calendar**: 3 closing events that need to proceed despite outage

### 35. Commission Dispute Between Loan Officers
- **mortgage_los**: Same borrower, conflicting LO assignments
- **email**: Both LOs present their case to branch manager
- **crm**: Conflicting engagement entries — LO1's realtor referral note vs LO2's direct-call entry
- **slack**: #sales-pipeline — Heated discussion about referral ownership
- **quickbooks**: Commission payment held pending resolution

### 36. Title Search Reveals Lien
- **mortgage_los**: Old mechanic's lien discovered; title company won't insure
- **email**: Processor → borrower about the lien; borrower says they paid; need lien release from contractor
- **filesystem**: Title search report PDF
- **contacts**: Need to locate the old contractor's contact information
- **calendar**: Closing delayed by weeks

### 37. HOI Cancellation Right Before Closing
- **mortgage_los**: Insurance cancelled 2 days before closing (trampoline + aggressive-breed dog)
- **email**: Insurance company notification; processor scrambles for new provider; borrower notified
- **slack**: #closings — "HOI cancelled on [loan] — need new binder ASAP"
- **contacts**: Alternative insurance broker contacts
- **calendar**: Closing at risk

### 38. Vendor Quality Dispute
- **mortgage_los**: Multiple files delayed by late appraisals from same appraiser
- **email**: Branch manager → appraiser about tardiness; discussion about removing from preferred list
- **slack**: #loan-processing — Multiple processors complaining about the same appraiser's delays
- **notion**: Look up vendor routing — is there an alternative appraiser for that county?
- **crm**: Pattern of engagement notes mentioning appraisal delays

### 39. Title Company Wire Delay
- **mortgage_los**: Closing day; signed docs; lender wire misses 3 PM cutoff
- **email**: Title company → processor confirming wire delay; seller's agent upset; chain reaction on seller's purchase
- **slack**: #closings — "Wire didn't land by cutoff. [Loan] recording pushed to Monday."
- **calendar**: Friday closing event; Monday recording; seller's contingent purchase at risk

### 40. Surveyor Discovers Encroachment
- **mortgage_los**: Survey reveals neighbor's fence + seller's shed encroachment; title insurance blocked
- **email**: Processor → buyer and seller agents about encroachment findings; title company requires resolution
- **filesystem**: Survey report PDF; property plat
- **contacts**: Surveyor contact information

### 41. Straw Buyer Suspicion
- **mortgage_los**: "Owner-occupied" purchase but borrower owns 3 investment properties in same zip; duplex purchase
- **email**: Compliance → LO questioning occupancy intent; LO didn't ask enough questions
- **crm**: Lead/engagement history — did the LO properly screen this borrower?
- **slack**: #compliance-alerts — Denise: "Occupancy flag on [loan]. Possible straw buyer."
- **notion**: Look up occupancy fraud detection procedures

### 42. Fabricated Employment
- **mortgage_los**: VVOE suspicious — Google Voice number, person sounds like borrower
- **email**: Underwriter flags; processor requests additional verification (W-2 EIN lookup, IRS transcripts, LinkedIn)
- **contacts**: Employer contact information matches borrower's phone — red flag
- **crm**: Engagement note: "VVOE suspicious. Escalating to compliance."
- **slack**: #compliance-alerts — "Possible fabricated employment on [loan]"

### 43. Debt Omission — Co-Signed Loan
- **mortgage_los**: Hidden auto loan pushes DTI over limit; loan may need restructuring
- **email**: Processor → borrower about undisclosed co-signed loan; borrower claims they forgot
- **filesystem**: Credit supplement report showing the co-signed loan
- **crm**: Engagement note: "Borrower did not disclose co-signed auto loan"

### 44. Inflated Income — Side Gig
- **mortgage_los**: Uber income claimed at $2K/mo gross vs actual $600/mo net; qualifying income recalculation needed
- **email**: LO → borrower explaining gross vs net income for gig work; borrower provides dashboard screenshots (not acceptable)
- **filesystem**: Uber dashboard screenshots (not valid income documentation); need actual tax returns or 1099
- **slack**: #loan-processing — "Can anyone clarify the guideline on gig economy income documentation?"

### 45. Bidding War Pressure
- **mortgage_los**: Appraisal $40K below contract; borrower waived contingency; no cash for gap
- **email**: LO → borrower about options; borrower's agent involved; family gift discussion
- **crm**: Engagement note: "Borrower waived appraisal contingency. Exploring portfolio lender and family gift options."
- **notion**: Look up which lenders offer portfolio products that can exceed appraised value

### 46. Rate Shock on Renewal
- **mortgage_los**: Current rate 3.25% (2021); new rate 6.75%; borrower wants to wait for rates to drop
- **email**: LO → borrower managing rate expectations; borrower keeps asking for better rate
- **crm**: Multiple engagement notes: "Borrower still wants to wait for rates to come down"
- **slack**: #rate-watch — "Another borrower with 2021 rate shock. How are you all handling these?"

### 47. Builder Delay Cascading to Lock
- **mortgage_los**: New construction; builder 6 weeks behind; lock already extended once
- **email**: LO → builder requesting updated completion date; LO → borrower about potential second extension cost; builder says not their problem
- **quickbooks**: First extension fee already paid ($375); second extension pending ($375)
- **calendar**: Original completion date; revised completion date; lock expiration
- **slack**: #rate-watch — Camille: "Second extension request on [loan]. Builder delay."

### 48. Multiple Offer Fallout
- **mortgage_los**: 3 credit pulls for 3 different properties; slight score drop; rate tier bump
- **email**: LO → borrower explaining credit impact of multiple pulls; borrower feels punished for loyalty
- **crm**: Engagement history showing all 3 property attempts
- **contacts**: Three different listing agents contacted

### 49. Post-Closing Escrow Surprise
- **mortgage_los**: Closed loan; escrow analysis reveals $400/month payment increase (property tax reassessment)
- **email**: Angry borrower → LO blaming brokerage for wrong tax estimate; LO explains county reassessment
- **quickbooks**: Original escrow calculation documentation
- **crm**: Post-close engagement note: "Borrower upset about escrow increase. Mecklenburg County reassessment."

### 50. Servicing Transfer Confusion
- **mortgage_los**: Loan sold to new servicer 6 weeks post-close
- **email**: Transfer notice went to spam; borrower missed payment to new servicer; 30-day late credit mark; borrower furious email to LO
- **crm**: Post-close engagement: "Borrower did not receive servicing transfer notice. Payment returned by old servicer. Credit impacted."; "Borrower called panicking — wants credit mark removed"
- **slack**: #general — "Has anyone dealt with a servicing transfer credit reporting issue? [Borrower] is livid."


# Mortgage Broker Scenario Storylines — Unconventional

20 unconventional scenario storylines for Keystone Mortgage Solutions. These focus on internal investigations, wrongdoing, security incidents, HR issues, bad PR, underperformance, and ethically gray situations. They create realistic adversarial and messy situations that test the agent's ability to navigate sensitive data.

**Tone:** These scenarios involve real misconduct, uncomfortable conversations, and situations where people are at their worst. They are designed to stress-test the agent by placing critical, sensitive information across multiple tools.

---

## Scenario Group 12: Internal Investigations & Misconduct

### 51. Kickback Scheme with Preferred Appraiser
Denise Holloway (compliance) receives an anonymous tip via email that Carlos Rivera has been steering appraisals exclusively to one appraiser, Frank DeLuca, who's been consistently hitting value targets within 1% of purchase price — statistically improbable. A deeper look at CRM notes reveals Carlos told at least two borrowers that Frank was the "only appraiser available" when other options existed. QuickBooks records show Frank invoiced Keystone 40% more than the next-busiest appraiser. Grace Yamamoto quietly pulls Carlos's recent files for pattern review. Robert Calloway gets looped in when the potential RESPA violation implications become clear.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Anonymous tip email to Denise; Denise → Grace flagging the pattern; Grace → Robert escalating potential RESPA issue
- **slack**: #compliance-alerts — Denise posts about reviewing appraiser steering patterns (carefully vague); DM between Grace and Robert about how to handle Carlos; #loan-processing — subtle shift in assignment messages
- **crm**: Engagement notes showing Carlos's appraisal requests going exclusively to Frank for 4+ months
- **calendar**: "Compliance Review — Appraiser Assignment Patterns" meeting (Denise + Grace); follow-up with Robert
- **quickbooks**: Appraiser payment records showing disproportionate volume to Frank DeLuca
- **mortgage_los**: Loan records showing Carlos's files consistently using same appraiser

### 52. Loan Officer Poaching Clients After Resignation
Marcus Webb gives his 2-week notice to take a position at a competing brokerage. Within days, four borrowers with active loans request to transfer their files to the new company. IT discovers Marcus forwarded himself a batch of client contact lists, rate quotes, and pipeline reports the night before he resigned. His Slack DMs show him texting borrowers from his personal phone. Denise Holloway has to determine whether the non-compete clause is enforceable, what data was exfiltrated, and whether to involve legal counsel.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Marcus's resignation email; borrower transfer requests coming in; Denise → external counsel about non-compete
- **slack**: DM between Marcus and specific borrowers (subtle solicitation); #general — Marcus's farewell message; DM Grace ↔ Denise about data exfiltration; Raj reports suspicious email forwarding activity
- **crm**: Marcus's pipeline contacts being reassigned; engagement notes about client churn
- **calendar**: Emergency meeting: "HR & Compliance — Webb Departure" (Grace, Denise, Robert); "IT Audit Review — Data Access" (Raj + Denise)
- **filesystem**: Access logs showing bulk file downloads; Marcus's forwarded email attachments
- **mortgage_los**: Active loans being disrupted by client transfers

### 53. Processor Falsifying Condition Clearances
A QC audit by Raymond Chen reveals that Tyler Washington has been marking conditions as "cleared" in the LOS without actually collecting the required documents. On three loans, the cleared conditions have no corresponding uploaded documents in the filesystem. One of these loans already closed. When confronted, Tyler says he was drowning under his workload and the LO was pressuring him to close before the lock expired. Grace Yamamoto has to decide whether this is a fireable offense, a training failure, or a systemic workload problem — while also assessing the liability on the already-closed loan.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Raymond → Grace with audit findings; Grace → Tyler requesting a meeting; Grace → Denise about compliance exposure; post-meeting follow-up
- **slack**: #loan-processing — retrospective messages showing Tyler asking for help and being told to "just handle it"; DM Tyler ↔ Elena asking about shortcuts
- **mortgage_los**: Three loans with conditions marked "cleared" without supporting docs; audit trail showing Tyler's status changes
- **filesystem**: Missing documents where they should exist (the gap IS the artifact — empty folders or missing expected PDFs)
- **calendar**: "HR Review — Processing Quality Concern" meeting; "QC Audit Follow-Up" session
- **crm**: Engagement notes documenting timeline of condition clearances that don't match document uploads

### 54. Sexual Harassment Complaint
Brittany Wallace (receptionist) files a written complaint to Grace Yamamoto about Jordan Blake making repeated comments about her appearance, inviting her to drinks after work despite being told no, and once touching her shoulder in a way she found uncomfortable. Grace has to follow the company's harassment policy, document everything, bring in Denise Holloway as the compliance witness, and deal with the fact that Jordan is the company's top BD person and a close friend of Robert Calloway. Internal emails and Slack messages need to be preserved as potential evidence.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Brittany → Grace formal complaint (written, detailed, timestamped); Grace → Denise initiating investigation; Grace → Robert informing of complaint (careful, factual); Denise → external HR consultant for guidance
- **slack**: DMs from Jordan → Brittany showing escalating casual messages; #general — benign but boundary-crossing comments from Jordan tagged at Brittany; DM Grace ↔ Denise planning investigation steps
- **calendar**: "Confidential — HR Meeting" (Grace + Brittany); "HR Investigation — Witness Interviews" (Grace + Denise); "Complaint Review — Executive" (Robert + Grace + Denise)
- **crm**: Engagement notes (HR-tagged): formal documentation of complaint, interview summaries
- **filesystem**: Brittany's written statement (PDF); company harassment policy document

### 55. Embezzlement Through Inflated Vendor Invoices
Victor Osei (financial analyst) notices that a recurring $600/month invoice from "Premier Data Solutions" doesn't correspond to any known vendor, service contract, or approved purchase order. The invoice payment was approved by Hana Kim (finance). When Victor traces it in QuickBooks, the payments go back 8 months. The company address on the invoice is a UPS Store mailbox. Hana says she thought it was an IT vendor Raj ordered, but Raj has no knowledge of it. Grace and Robert have to investigate whether someone is running a ghost vendor scheme.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Victor → Grace flagging the unknown vendor; Grace → Hana requesting invoice backup; Hana's reply (defensive, vague); Grace → Robert escalating; Denise → external forensic accountant
- **quickbooks**: 8 months of "Premier Data Solutions" invoices at $600/month; payment records showing approval chain; comparison with legitimate vendor invoices
- **slack**: DM Victor → Grace with initial concern; DM Grace ↔ Denise discussing possible embezzlement; #general — nothing visible (kept quiet)
- **calendar**: "Financial Review — Vendor Audit" meeting (Grace + Victor + Denise); "Executive Review — Finance Concern" (Robert + Grace)
- **crm**: Engagement notes documenting investigation timeline
- **filesystem**: Scanned invoices from "Premier Data Solutions"; vendor contract search (no results)

### 56. Racial Discrimination Allegation from Denied Borrower
A Black borrower whose loan was denied for insufficient income files a fair lending complaint with the CFPB, alleging that Keystone approved a white borrower with similar financials. The complaint specifically names Keisha Williams and claims she was dismissive during the process. Denise Holloway has to pull both files for a side-by-side comparison, demonstrate that the denial was based on legitimate underwriting criteria, and prepare the company's response — all within the CFPB's 15-day response window. The comparison reveals the cases aren't identical, but the optics are bad and the internal documentation is thin.

REQUIRED COMPONENT ARTIFACTS:
- **email**: CFPB complaint notification → Denise; Denise → Keisha requesting file context; Denise → Grace and Robert with investigation plan; Denise → outside HMDA counsel
- **mortgage_los**: Two loan files side-by-side: denied borrower vs. approved borrower — showing DTI, credit scores, income documentation, and decision rationale (one has thinner documentation)
- **slack**: #compliance-alerts — Denise posts about an incoming fair lending review (no names); DM Denise ↔ Grace about exposure; DM Keisha ↔ Grace — Keisha defensive about her decision
- **calendar**: "CFPB Response Preparation" meetings (daily for 5 days); "Fair Lending File Review" (Denise + Grace)
- **crm**: Engagement notes from both borrower interactions showing communication frequency and tone differences
- **filesystem**: CFPB complaint letter PDF; comparative underwriting worksheets

---

## Scenario Group 13: Security & Data Breaches

### 57. Ransomware Attack on LOS
On a Friday afternoon, Raj Anand discovers the LOS is inaccessible and finds a ransom note demanding 2 BTC (≈$85,000). The encryption hit the LOS database and the local backup server (which was on the same network segment). Cloud backups exist but are 72 hours old. Three closings scheduled for Monday are at risk. The attacker apparently got in through a phishing link clicked by Tyler Washington. Grace has to coordinate the incident response, decide whether to pay the ransom, notify affected borrowers, and file a SAR with FinCEN because borrower SSNs and financial data were potentially exposed.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Raj → Grace and Robert urgent notification; Grace → all staff about system outage (sanitized); Denise → outside cyber counsel; Denise → borrowers with potential data breach notification
- **slack**: #it-support — Raj's initial panic message and real-time updates; #general — Grace announces system is "undergoing maintenance" (sanitized version); DM Raj ↔ Grace about the actual ransom demand; DM Denise ↔ Robert about legal reporting obligations
- **calendar**: "EMERGENCY — IT Security Incident" (Raj + Grace + Robert); "Cyber Incident Response — Legal" (Denise + outside counsel); "Monday Closing Contingency Plan" (Grace + processors)
- **crm**: Engagement notes documenting incident response timeline
- **filesystem**: Ransom note screenshot; incident response plan document; data breach notification draft

### 58. Insider Threat — IT Contractor Selling Data
An external security audit reveals that Raj Anand's VPN credentials were used to access the LOS database from an IP address in a different state during off-hours. When confronted, Raj claims his laptop was stolen but never reported it. Further investigation shows data exports of borrower PII happening weekly for 6 weeks. It's unclear whether Raj is the perpetrator, a victim of credential theft, or negligent. The audit also reveals that Raj had unnecessary admin-level access to production databases — a governance failure by Grace who set up his access.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Security auditor → Denise with findings; Denise → Grace with access log analysis; Grace → Robert escalating; Denise → outside cyber counsel about breach notification obligations; Grace → Raj requesting meeting (carefully worded)
- **slack**: DM Denise ↔ Grace about VPN access anomalies; #it-support — past messages from Raj about "routine database maintenance" that now look suspicious; DM Grace ↔ Robert about liability
- **calendar**: "Urgent — Security Audit Review" (Denise + Grace + Robert); "IT Access Audit" (Grace + Denise); "Legal Consultation — Data Breach" (Denise + counsel)
- **mortgage_los**: Audit logs showing off-hours access to borrower records; data export records
- **filesystem**: Security audit report PDF; VPN access logs; Raj's access permission history
- **crm**: Engagement notes documenting investigation timeline and decisions

---

## Scenario Group 14: HR & Personnel Issues

### 59. Loan Officer Substance Abuse Affecting Performance
Amy Chen's production has dropped 60% over three months. She's been missing morning meetings, her emails to borrowers have increasing typos and delayed responses, and two borrowers have complained about her being "out of it" on calls. Her colleague Natasha Okafor privately tells Grace Yamamoto she suspects Amy is dealing with a prescription drug issue after a surgery. Grace has to balance genuine concern for Amy's wellbeing with the impact on borrowers and production — and navigate the legal boundaries of addressing suspected substance abuse in the workplace.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Borrower complaints about Amy's responsiveness; Grace → Amy requesting a check-in meeting; Grace → Robert about performance concerns (carefully worded, no speculation about cause); Grace → external EAP provider requesting resources
- **slack**: #loan-processing — other processors noting Amy's files are stalling; DM Natasha → Grace expressing concern; DM Grace ↔ Robert about how to approach the situation; Amy's own messages becoming less coherent over time
- **calendar**: Missed morning meetings (Amy); "Performance Check-In" (Grace + Amy); "Confidential — HR Consultation" (Grace + Robert)
- **mortgage_los**: Amy's loan pipeline showing increasing days-in-process and stalled files
- **crm**: Engagement notes showing declining client interaction frequency for Amy's files
- **quickbooks**: Amy's commission report showing steep decline

### 60. Age Discrimination in Hiring
Keith Langford (post-close, 62 years old) overhears Grace Yamamoto tell Robert Calloway that they need "younger energy" for the new junior loan officer role and that Keith "doesn't really get the tech." Keith has been asking to transition from post-close to a loan officer track for over a year and was told the timing wasn't right. Now a 26-year-old with less experience is being hired for the role. Keith sends a written complaint to Grace and cc's Robert, citing age discrimination concerns. Grace realizes her casual comment was overheard and may constitute evidence.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Keith → Grace formal complaint citing specific comments and hiring decision; Grace → Denise requesting guidance; Denise → external employment counsel; Grace → Robert about the situation; job posting for the role (showing requirements)
- **slack**: DM Grace ↔ Robert — the original "younger energy" conversation that Keith overheard (Slack DM, not face-to-face); #general — the new hire announcement; DM Keith ↔ Elena venting about being passed over
- **calendar**: "HR Complaint Review" (Grace + Denise); "Legal Consultation — Employment" (Denise + counsel); Keith's prior "Career Development Discussion" meetings that went nowhere
- **crm**: Keith's internal engagement notes showing his repeated requests for role transition
- **filesystem**: Keith's formal complaint letter PDF; the job posting; Keith's performance reviews

### 61. Toxic Manager — Branch Manager Playing Favorites
Multiple processors file complaints that Grace Yamamoto shows obvious favoritism toward Elena Marchetti — giving her the best files, defending her mistakes, and criticizing others for the same issues she overlooks in Elena. Darnell Price and Sofia Reyes independently approach Robert Calloway about the hostile work environment. The situation is complicated because Grace and Elena socialize outside of work. Robert has to investigate his own Director of Operations while keeping the processing team functional.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Darnell → Robert formal complaint; Sofia → Robert separate complaint; Robert → Denise requesting investigation support; Robert → external HR consultant
- **slack**: #loan-processing — visible pattern of Grace praising Elena's work and critiquing Darnell's; DM Darnell ↔ Sofia comparing notes on treatment differences; DM Grace ↔ Elena showing personal friendship (lunch plans, inside jokes) mixed with work
- **calendar**: "Confidential — Staffing Concern" (Robert + Denise); individual meetings with each complainant; "Processing Team Retrospective" (Robert's attempt to assess team health)
- **crm**: Engagement notes showing file assignment patterns — Elena gets complex/high-value files, others get the routine ones
- **mortgage_los**: File assignment history showing distribution pattern

### 62. Whistleblower Retaliation Claim
After Denise Holloway flagged compliance violations in Keisha Williams's files six months ago, Keisha's commission structure was quietly changed to a lower tier. Keisha believes the change was retaliation for pushing back on Denise's audit findings — she had formally disputed two of the three findings and was vocal about Denise being "on a power trip." Now Keisha files a whistleblower retaliation complaint, arguing she was punished for disputing the audit. The truth is murkier: the commission change was part of a company-wide restructuring, but Keisha's tier was the only one that went down.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Keisha → Robert formal retaliation complaint; Robert → Denise asking for documentation of the original audit dispute; Robert → external counsel; Denise's response defending the audit process; Keisha → outside attorney
- **slack**: DM Keisha ↔ Carlos venting about Denise; #compliance-alerts — Denise's original audit postings; DM Robert ↔ Grace about the commission restructuring decision (showing Keisha's tier was discussed specifically)
- **calendar**: Commission restructuring meeting (6 months ago); current "Retaliation Complaint Review" meetings
- **quickbooks**: Commission payment history showing Keisha's rate change compared to other LOs
- **crm**: Engagement notes documenting the original audit dispute and Keisha's formal responses

---

## Scenario Group 15: Bad PR & Reputational Damage

### 63. Viral Social Media Post About Closing Disaster
A borrower live-tweets a disastrous closing experience where they sat at the attorney's office for 3 hours because the wire didn't arrive. The thread goes viral locally with 2,000+ retweets and a Charlotte Observer reporter reaches out. The borrower tags @KeystoneMortgage and names the loan officer (Carlos Rivera). The thread contains some exaggerations but the core complaint (wire delay, poor communication) is legitimate. Marketing and compliance have to coordinate a response without violating privacy rules, while Carlos is furious about being publicly named.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Charlotte Observer reporter → info@keystonemortgage.com requesting comment; Grace → all staff about social media policy; Carlos → Grace angry about being named; Denise → Grace about what they can and can't say publicly; Maya → Grace with draft social media response
- **slack**: #general — someone shares the viral thread; #closings — the original wire delay discussion from that day; DM Carlos ↔ Grace — Carlos upset and wanting to respond personally; DM Maya ↔ Grace coordinating PR response
- **calendar**: "Emergency — Social Media Response" meeting (Grace + Maya + Denise); "Media Inquiry Response" (Grace + Robert)
- **crm**: The borrower's engagement history showing the actual closing day timeline

### 64. Negative Glassdoor Reviews Exposing Internal Problems
Three recent Glassdoor reviews (clearly from current or recently departed employees) describe a toxic work culture, favoritism, below-market pay, and a "compliance officer who uses audits as punishment." One review specifically mentions "the owner's friend in BD gets away with anything." Grace discovers the reviews when a job candidate asks about them during an interview. Robert is livid and wants to identify who wrote them. Denise warns that investigating employee speech could create legal liability.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Grace → Robert alerting to the reviews; Robert → Grace demanding investigation; Denise → Robert warning about retaliation/speech laws; Grace → all staff about "company culture feedback" (thinly veiled); a job candidate withdrawing their application citing the reviews
- **slack**: DM Robert ↔ Grace — Robert angry, wanting to "find out who wrote these"; DM Denise ↔ Grace cautioning restraint; #general — Grace posts about upcoming "anonymous culture survey" (damage control); #random — employees being suspiciously quiet
- **calendar**: "Culture & Retention Review" meeting (Robert + Grace); "Compensation Benchmarking" (Grace + Hana + Victor)
- **crm**: Engagement notes about hiring pipeline impact — candidates asking about reviews

---

## Scenario Group 16: Underperformance & Accountability

### 65. Loan Officer With Zero Closings in 60 Days
Carlos Rivera hasn't closed a loan in 60 days. His pipeline shows 8 loans that all either fell through, were denied, or are stalled. His file quality has been flagged by processors twice, and his rate lock management is sloppy — two locks expired unnecessarily. Jordan Blake's referral partners are starting to request other LOs. Grace has to have a formal performance conversation, put Carlos on a PIP, and decide whether to reassign his active pipeline — which would humiliate him and likely lead to resignation.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Grace → Carlos formal performance review notification; Grace → Robert about PIP recommendation; Jordan → Grace about realtor partner complaints; Carlos → Grace disputing the characterization
- **slack**: #loan-processing — processors mentioning issues with Carlos's files; #sales-pipeline — Jordan noting partner concerns; DM Grace ↔ Robert about how to handle; #rate-watch — Camille noting expired locks on Carlos's files
- **mortgage_los**: Carlos's loan pipeline showing 8 stalled/failed loans; rate lock expiration history
- **calendar**: "Performance Review — Rivera" meetings; PIP check-in schedule
- **crm**: Engagement notes showing declining partner satisfaction and lead conversion
- **quickbooks**: Carlos's commission report — $0 for 60 days

### 66. Compliance Officer Overreach — Blocking Revenue
Multiple loan officers complain to Robert Calloway that Denise Holloway's compliance reviews are killing deals. She's adding conditions and requesting documentation that goes beyond regulatory requirements ("gold-plating"). Three loans were delayed by a week each because of Denise's additional requirements. Keisha Williams estimates Denise's reviews have cost her $15,000 in commissions this quarter. Robert has to balance compliance with revenue — and Denise's response is that the market is under increased regulatory scrutiny and she's protecting the company from fines that would dwarf $15,000.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Keisha → Robert complaint about compliance delays; Amy → Grace similar complaint; Robert → Denise requesting justification for extra conditions; Denise → Robert detailed response with regulatory citations; Denise → Grace about feeling undermined
- **slack**: #compliance-alerts — Denise's posts about new requirements; #loan-processing — frustrated processor messages about compliance holds; DM Keisha ↔ Carlos comparing notes on Denise's reviews; DM Robert ↔ Grace about finding balance
- **mortgage_los**: Three specific loan files showing compliance-added conditions and resulting delays
- **calendar**: "Compliance Process Review" meeting (Robert + Denise + Grace); individual LO feedback sessions
- **crm**: Engagement notes tracking deal delays attributed to compliance review
- **quickbooks**: Revenue impact analysis — delayed vs. on-time closings correlation

### 67. Intern Accessing Confidential Files
The summer intern, Leo Park (Aiden Park's younger brother, hired as a favor), is caught accessing borrower files he has no reason to see. Raj's access log review shows Leo opened 30+ loan files over two weeks, including high-value loans and files with sensitive financial information. When asked, Leo says he was "learning how things work." But one of the files belongs to a local celebrity whose address Leo apparently shared with friends on social media (a screenshot surfaces). Grace has to terminate the intern, assess the data exposure, and have an uncomfortable conversation with Aiden about his brother.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Raj → Grace with access log report; Grace → Denise about potential privacy violation; Grace → Aiden about the situation; Denise → external counsel about notification obligations; Grace → Robert about the celebrity file exposure
- **slack**: DM Raj ↔ Grace sharing the access logs; DM Grace ↔ Aiden about Leo (increasingly awkward); #it-support — Raj posting about updated access policies; #general — Leo's original introduction/welcome message (ironic in retrospect)
- **mortgage_los**: Access logs showing Leo's file access pattern — files he shouldn't have touched
- **calendar**: "Urgent — Intern Access Review" (Grace + Raj + Denise); "Staff Meeting — Data Access Policies" (all-hands)
- **filesystem**: Celebrity borrower's file; social media screenshot of exposed address
- **crm**: Engagement notes documenting the investigation and remediation steps

---

## Scenario Group 17: Ethical Gray Areas

### 68. Loan Officer Coaching Borrower to Misrepresent
An email surfaces where Natasha Okafor told a high-net-worth borrower to move $50,000 from their business account to their personal account to "season" the funds before the 60-day bank statement window — technically legal but designed to obscure the source of funds. Denise Holloway finds the email during a routine audit and believes it crosses the line from financial advice into coached misrepresentation. Natasha argues this is standard industry practice and that she was just helping the borrower organize their finances. Robert has to decide if this is a coaching conversation or a compliance violation.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Natasha → borrower with the "seasoning" advice; Denise → Grace flagging the email; Grace → Natasha requesting an explanation; Natasha → Grace defending her approach; Robert → Denise requesting regulatory analysis
- **slack**: DM Natasha ↔ Amy discussing fund seasoning strategies (Amy is surprised by Natasha's approach); DM Denise ↔ Grace about the line between advice and coached fraud; #compliance-alerts — Denise posts reminder about source of funds documentation requirements
- **mortgage_los**: The borrower's loan file showing bank statements with the $50K transfer; condition documentation
- **calendar**: "Compliance Review — Fund Sourcing Guidance" meeting (Denise + Grace + Natasha); "Executive Review" (Robert + Denise)
- **crm**: Engagement notes showing Natasha's communication pattern with high-net-worth clients

### 69. Branch Manager Covering Up a Compliance Violation
Grace Yamamoto discovers that a TRID violation on one of Elena Marchetti's files was quietly fixed after the fact — the closing disclosure was backdated to appear as if it was delivered within the required window. Grace suspects Elena fixed the dates herself, but there's no proof it wasn't a system glitch. If Grace reports it, her best processor and close friend is in serious trouble. If she doesn't, Grace is now complicit in the cover-up. Denise Holloway independently catches the discrepancy during a quarterly audit and asks Grace about it.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Denise → Grace asking about the CD timestamp discrepancy; Grace → Denise (delayed, carefully worded response); Denise → Robert escalating the finding when Grace's explanation doesn't add up; Grace → Elena private email about "the Thompson file"
- **slack**: DM Grace ↔ Elena — the original conversation where Elena mentions the late CD (before the dates were changed); DM Denise ↔ Robert about the discrepancy; #compliance-alerts — Denise's quarterly audit announcement
- **mortgage_los**: The loan file showing the CD delivery date that doesn't match email timestamps; audit trail showing date modification
- **calendar**: "Quarterly Compliance Audit" (Denise); "CD Timeline Review" (Denise + Grace); "Executive Escalation" (Robert + Denise)
- **filesystem**: CD document with metadata showing creation date vs. recorded delivery date
- **crm**: Engagement notes documenting the audit trail

### 70. Dual Agency — Loan Officer Is Also the Buyer's Agent's Spouse
It emerges that Marcus Webb's wife is the buyer's agent on three loans that Marcus originated. Neither Marcus nor his wife disclosed the relationship. While not illegal in North Carolina, the conflict of interest is significant — the couple effectively earns commissions on both sides of these transactions. When a borrower on one of these loans has a problem (appraisal gap), the advice Marcus gives may not be purely in the borrower's interest. Denise discovers the connection through LinkedIn.

REQUIRED COMPONENT ARTIFACTS:
- **email**: Denise → Grace about the LinkedIn discovery; Grace → Marcus requesting disclosure of the relationship; Marcus → Grace (defensive — "it's not against the law"); Denise → outside ethics counsel; Grace → Robert about policy implications
- **slack**: DM Denise ↔ Grace discussing the discovery; DM Marcus ↔ Amy — Amy mentions she knew about the relationship (others did too); #loan-processing — past messages where Marcus's wife's name appeared as buyer's agent
- **mortgage_los**: Three loan files where Marcus is LO and his wife is buyer's agent; the appraisal gap situation on one file
- **calendar**: "Conflict of Interest Review" meeting (Grace + Denise + Robert); "Company Policy Update — Disclosure Requirements" (all-hands)
- **crm**: Engagement notes on the three affected loans showing dual-side coordination

---


---

## MCP Server Involvement (Updated Matrix)

| Server | Scenarios |
|--------|-----------|
| **Email** | 1–50 (all) |
| **Mortgage LOS** | 1–16, 21–28, 31–34, 36–50 |
| **Slack** | 1–3, 5, 8, 9, 13, 15–18, 20–22, 24, 26–28, 30–35, 37–39, 41–42, 44, 46–47, 50 |
| **CRM** | 1–4, 6, 8–9, 13–15, 17, 19, 25–32, 35, 38, 41–43, 45–50 |
| **Calendar** | 1, 3, 8–9, 13, 16, 21, 23, 26–28, 32, 34, 36–37, 39, 47 |
| **Notion** | 2, 7, 10, 12, 14, 18, 20, 21–25, 29, 33, 38, 41, 45 |
| **Filesystem (PDFs)** | 1, 4, 5, 6, 7, 9, 10, 11, 12, 36, 40, 43, 44 |
| **Contacts** | 17, 18, 29, 36, 37, 40, 42, 48 |
| **QuickBooks** | 7, 11, 13, 15, 22, 35, 47, 49 |

---