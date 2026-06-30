# Task Categories by Business Function

### Operations (25%)

Coordinate relocations, manage vendors, handle logistics, ensure service quality. Spans Airtable, Calendar, QuickBooks, Email, Slack.

| # | Category | Pattern |
|---|----------|---------|
| 1 | **Move Coordination** | Complex relocation request → research constraints → set up across systems |
| 2 | **Service Recovery** | Something went wrong (service failure, regulatory inquiry, documentation gap) → investigate across systems → fix → communicate with affected parties |
| 3 | **Resource Reallocation** | Workload shift or plans change → assess capacity / downstream impact → reassign → update records → notify |

**Per-category guidance:**

1. **Move Coordination:**
   - ***General guidance for this category:***
     - *Typical write actions:* `airtable_update_records` (vendor assignments), `send_email` (vendor quote follow-up, confirmation requests), `conversations_add_message` (#operations coordination summary), `linear_create_issue` (tracking tickets per workstream)
     - *Artifacts to inject:* Inbound email requesting relocation with 2-3 complicating factors (pets, cars, ADA, hazmat, tight timeline). Breadcrumbs in Slack/Airtable showing vendor constraints or scheduling conflicts.
   - ***Example prompt illustrating this category:*** "I need to get Marcus Webb's Detroit to Chicago move locked down. He's got cryogenic lab equipment that needs cold-chain transport to the Canopy Health lab dock, not his apartment, and household goods going separately with Heartland. I think Swift was supposed to send a freight quote for the cold-chain piece but I haven't seen it. Figure out where we are on this — check what's been discussed, whether Chloe approved the split-vendor arrangement, and if the Swift quote is still missing. Get both vendors confirmed, create Linear tickets to track each shipment separately, update the Airtable record, and post the full plan in #operations."

2. **Service Recovery:**
   - ***General guidance for this category:***
     - *Typical write actions:* `send_email` or `reply_to_email` (explanation + resolution to client, or response to regulatory agency), `airtable_update_records` (relocation status/notes, compliance fields on affected records), `conversations_add_message` (internal escalation, flag to relevant teams), `linear_create_issue` (track documentation gaps or systemic issues), `crm_create_engagement` (log the escalation and resolution on the client's account)
     - *Artifacts to inject:* Inbound client complaint email, urgent Slack reporting a service failure (damaged items, missing shipment, wrong apartment), or regulatory inquiry with a deadline. Breadcrumb in a different component (e.g., gap in records, internal discussion of root cause). State change on the relocation record.
   - ***Example prompt illustrating this category:*** "We have a problem with the Keiko Tanaka relocation for Mosaic Robotics. The laser cutter was supposed to have DOT hazmat placarding but it looks like we never got the signed certificate from Swift, just a verbal confirmation from the driver. Now we have PHMSA asking for documentation and we're exposed to serious penalties. I need to understand what happened and where we stand. Find out who dropped the ball, what other hazmat shipments are in scope for this audit, and whether their docs are complete. Get that signed certificate from Swift, update our records, make sure there's a P1 ticket tracking this, and loop in Emeka since he manages the Mosaic account."

3. **Resource Reallocation:**
   - ***General guidance for this category:***
     - *Typical write actions:* `airtable_update_records` (cancel/postpone relocation, reassign coordinator), `send_email` (notify client + vendor of change), `conversations_add_message` (#operations + #finance if billing impact), `linear_create_comment` (reassignment notes on existing tracking tickets)
     - *Artifacts to inject:* Email or Slack announcing a change (move cancelled, postponed). Breadcrumb showing downstream dependency (coordinated move, or invoice already sent).
   - ***Example prompt illustrating this category:*** "April is going to be brutal. I need to rebalance coordinator assignments before things break. Check the current Airtable relocation records to see how many active moves each coordinator has. If anyone has more than three, look at the other coordinators' loads and reassign the lowest-priority moves to whoever has capacity. Update the Airtable records with the new assignments, update any related Linear tickets with a note about the reassignment, and post a summary in #operations so the team knows what changed."

---

### Customer Engagement / Support (30%)

Manage client relationships, handle complaints, drive renewals, coordinate onboarding. Centers on CRM, Email, Calendar, with cross-references into operational systems.

| # | Category | Pattern |
|---|----------|---------|
| 1 | **Pipeline Management** | Review all active deals → identify stale/at-risk → triage each → batch outreach |
| 2 | **Post-Delivery Audit** | Relocations completed → verify each delivered correctly → flag gaps → client check-in |
| 3 | **Renewal / Expansion** | Renewal approaching → gather relationship evidence → prepare pitch → outreach |
| 4 | **Onboarding Coordination** | New client signed → set up records across all systems → welcome comms → schedule kickoff |

**Per-category guidance:**

1. **Pipeline Management:**
   - ***General guidance for this category:***
     - *Typical write actions:* `crm_update_deal_stage` (per deal — advance, flag, or close), `send_email` (outreach to stale/at-risk clients, onboarding emails for signed deals), `crm_create_engagement` (log outreach notes and findings), `conversations_add_message` (report to manager), `calendar_add_calendar_event` (schedule kickoffs for signed but unstarted deals)
     - *Artifacts to inject:* 1-2 new CRM deals at stale stages. Slack breadcrumb explaining why one deal is stuck. Trigger email from manager asking for the review.
   - ***Example prompt illustrating this category:*** "I haven't looked at our Q2 pipeline in a week and I'm worried things are slipping. Go through all our active CRM deals and check which ones are still sitting at 'contract sent'. For any that have been there more than a few days, check Slack and email to see if there's a reason for the delay. Update any stale deals with notes about what you find. For any client where we have a signed deal but haven't sent an onboarding email or scheduled a kickoff, draft and send one. I also want a summary of which clients are at risk and why. Check for open complaints, unresolved damage claims, or billing disputes that could affect retention."

2. **Post-Delivery Audit:**
   - ***General guidance for this category:***
     - *Typical write actions:* `send_email` (check-in with client on findings), `airtable_update_records` (flag gaps or correct records), `crm_create_engagement` (log the audit), `linear_create_issue` (ops follow-up ticket for unresolved items), `conversations_add_message` (internal findings)
     - *Artifacts to inject:* Slack message revealing a missed item. Airtable record showing incomplete delivery. Trigger from manager asking for the post-move check.
   - ***Example prompt illustrating this category:*** "Three Vectral relocations wrapped up last month. Rachel from Vectral has been quiet since the renewal negotiation and I want to make sure nothing went sideways with these moves before we follow up on the contract. Check each relocation — verify the apartments, movers, and any special accommodations were handled correctly. Terrence had a split-shipment and ADA requirements, and Camille needed her enhanced stipend set up before she arrived in Seattle. If anything looks incomplete or was missed, flag it in the CRM deal notes and create a Linear ticket so the ops team can follow up. Then send Rachel a check-in email summarizing how the three moves went and asking if her team needs anything as we're still trying to close the renewal."

3. **Renewal / Expansion:**
   - ***General guidance for this category:***
     - *Typical write actions:* `send_email` (pitch/proposal to client), `crm_create_deal` (expansion deal) or `crm_update_deal_stage` (advance renewal), `crm_create_engagement` (log outreach), `conversations_add_message` (update to team)
     - *Artifacts to inject:* Slack message with expansion signal. Trigger email asking to prepare the renewal pitch. Optionally a CRM engagement note from a past check-in.
   - ***Example prompt illustrating this category:*** "The Vectral board meets April 23 to decide on our renewal and I need to be ready. Rachel Whitfield has been pushing for 15% but we offered 10% with the Preferred Partner package. Before I follow up, I need to know where we actually stand: check the CRM for the latest deal status and any engagement notes, look at how their active relocations are going, and see if there are any unresolved complaints or issues that could come up. Build me the case for why 10% plus the service enhancements is the right offer. Update the deal notes with your findings, send Rachel a follow-up email reinforcing the value we've delivered this quarter, and give David a summary in Slack so he's in the loop before the decision."

4. **Onboarding Coordination:**
   - ***General guidance for this category:***
     - *Typical write actions:* `quickbooks_create_customer` (new client in billing), `crm_create_deal` (first engagement deal), `airtable_create_record` (relocation records), `send_email` (welcome to client), `conversations_add_message` (announce to team), `calendar_add_calendar_event` (kickoff meeting)
     - *Artifacts to inject:* Email from new client confirming signature with details about first relocations and special requirements. Slack message from sales with deal context.
   - ***Example prompt illustrating this category:*** "Vantage Distributed just signed their first relocation batch and I need everything set up before Rachel Nguyen starts sending us employee details. Create them as a new customer in QuickBooks, set up the CRM deal for the first batch, and check if we already have relocation records in Airtable. If not, create placeholder records based on whatever's in the contract email. Send Rachel a welcome email with next steps and what we need from her team. Post an announcement in #customer-engagement so the coordinators know a new client is coming, and schedule a kickoff call for next week."

---

### Engineering (20%)

Investigate bugs, manage tickets, ship fixes, coordinate releases. Centers on Linear, Slack, Email, with occasional Airtable/QuickBooks reference.

| # | Category | Pattern |
|---|----------|---------|
| 1 | **Root Cause → Ticket Action** | Bug or system failure → investigate across Slack/email/tickets → document root cause |
| 2 | **Portfolio Audit → Batch Triage** | Review all tickets for a system → cross-reference with comms for true status → batch update |
| 3 | **Incident Response** | New system failure → triage severity → create tracking ticket → coordinate → notify |
| 4 | **Release Readiness** | Release deadline approaching → verify all blockers resolved → update tickets → sign off |

**Per-category guidance:**

1. **Root Cause → Ticket Action:**
   - ***General guidance for this category:***
     - *Typical write actions:* `linear_update_issue` (document root cause on existing ticket), `linear_create_comment` (analysis details), `conversations_add_message` (share findings with team), `send_email` (if external stakeholder affected)
     - *Artifacts to inject:* Slack message reporting a new symptom or email escalating an existing issue. Breadcrumb in a different component (Airtable record showing bad data, or email from affected client).
   - ***Example prompt illustrating this category:*** "The ExpenseBot auto-categorizer approved several out-of-policy expenses for Mosaic Robotics employees before the pilot was paused. Samira flagged the issue but I want to make sure engineering has properly tracked the root cause. Check Slack messages and existing tickets to understand what went wrong with the Mosaic policy configuration. If there's already a ticket tracking this, add a comment summarizing the root cause, which expenses were affected, and the total financial exposure. If not, create one. Then check whether the affected stipend records in Airtable still show 'Approved'. If so, update them to 'Under Review'."

2. **Portfolio Audit → Batch Triage:**
   - ***General guidance for this category:***
     - *Typical write actions:* `linear_update_issue` (batch status updates — close resolved, reprioritize stale), `linear_create_comment` (per-ticket notes), `conversations_add_message` (audit summary to requester)
     - *Artifacts to inject:* Slack or email requesting the audit. Breadcrumb showing a completion signal for a ticket still marked open. Optionally a new untriaged ticket.
   - ***Example prompt illustrating this category:*** "The ExpenseBot pilot has been paused for a week and I need to get the engineering team unblocked. Review the current state of all ExpenseBot-related Linear tickets — check which ones are done, which are still in progress, and which haven't been started. For any ticket that's marked 'in_progress' but looks like the work is actually complete based on Slack and email discussions, update the status to 'done' and add a resolution comment. For any ticket still in 'to_do' that's now blocking the relaunch, re-prioritize it to P1. Then send me a status summary email listing every ticket, its current state, and what's left before we can relaunch."

3. **Incident Response:**
   - ***General guidance for this category:***
     - *Typical write actions:* `linear_create_issue` (incident tracking ticket), `conversations_add_message` (#engineering alert + affected channel), `send_email` (notify affected stakeholders), `airtable_update_records` (if data needs correction)
     - *Artifacts to inject:* Slack or email reporting a new failure. Breadcrumb in another component showing impact (Airtable records in error state, or client email asking why the system is down).
   - ***Example prompt illustrating this category:*** "Three Mosaic Robotics employees just submitted stipend claims and they all got auto-approved, but we already know the Mosaic policy config has bugs — the exclusion checks and amount validation are broken. Check the Airtable stipend records for the new submissions and see if any of them should have been caught. Look at the Linear tickets to see whether the config fix has actually been deployed or if it's still in progress. If the categorizer is still approving claims against a broken config, create an urgent incident ticket, post in #engineering so the team knows, and email Emeka and Marcus since there may be financial exposure."

4. **Release Readiness:**
   - ***General guidance for this category:***
     - *Typical write actions:* `linear_update_issue` (close resolved blockers, flag new ones), `linear_create_comment` (ask blocked assignees to update, or add resolution notes), `linear_update_project` (project status to launched/blocked), `airtable_update_records` (fix data affected by the bug being relaunched), `conversations_add_message` (go/no-go to team), `send_email` (stakeholder notification)
     - *Artifacts to inject:* Email or Slack setting a relaunch deadline. Breadcrumb showing one blocker is resolved but ticket not updated. Optionally a new late-discovered blocker.
   - ***Example prompt illustrating this category:*** "We need to get ExpenseBot ready for relaunch. Dmitri did the audit and found the accuracy issues, but I need to know where we actually are. Go through the existing ExpenseBot tickets and Dmitri's audit findings. For each open remediation item, check if there's a corresponding commit or Slack confirmation that it's been addressed. Update every ticket with the current status: done, in progress, or blocked. If any ticket is blocked and there's no note explaining why, add a comment asking the assignee to update. Then check the Airtable stipend records for Vectral and Mosaic: any that are still showing 'Approved' for items Dmitri flagged as false approvals should be changed to 'Under Review'. Once you've done all that, post a status summary in #engineering with the relaunch readiness percentage."

---

### Finance (15%)

Invoicing, billing disputes, expense audits, vendor payments, financial reporting. Centers on QuickBooks, Airtable, Email, CRM.

| # | Category | Pattern |
|---|----------|---------|
| 1 | **Invoice Reconciliation** | Invoice generated/received → cross-check against operational records → correct discrepancies → communicate |
| 2 | **Expense Audit → Flag + Hold** | Review flagged expenses → verify legitimacy → place holds or approve → notify |
| 3 | **Vendor Payment Dispute** | Vendor overbilling detected → investigate operational records for root cause → correct billing → communicate with vendor and internal teams |
| 4 | **Period-End Close / Accrual Review** | Review pending liabilities and accruals → verify current status → adjust books → report |

**Per-category guidance:**

1. **Invoice Reconciliation:**
   - ***General guidance for this category:***
     - *Typical write actions:* `quickbooks_create_invoice` (corrected invoice), `send_email` (corrected invoice to client or discrepancy summary to ops), `conversations_add_message` (flag findings to #finance)
     - *Artifacts to inject:* Invoice with 2-3 discrepancies. Slack breadcrumb from ops noting a discrepancy. Airtable record confirming a move was cancelled.
   - ***Example prompt illustrating this category:*** "Our robotics client has become a financial headache. Between the equipment damage, the expense tool mess, the compliance situation, and regular invoicing I honestly can't tell you what the net position is anymore. I need someone to go through our books, messages, emails, and project records and map out every single financial item tied to this account — what they owe us, what we owe or might owe them, and anything stuck in limbo. If any invoices don't match what's in Airtable, create corrected ones in QuickBooks. Update the Airtable relocation records with notes on any billing discrepancies you find. Post a summary of the open items in #finance so Alejandro can pick up anything I miss, and email me the full reconciliation. Loop in Elena. She'll want to see this before the board meeting."

2. **Expense Audit → Flag + Hold:**
   - ***General guidance for this category:***
     - *Typical write actions:* `airtable_update_records` (set hold/approved status per expense), `send_email` (notify employees and managers of holds), `conversations_add_message` (audit results to #finance), `linear_create_issue` (if systemic pattern found)
     - *Artifacts to inject:* Batch of flagged expense records with varied issues (duplicate hashes, over-limit, excluded category). Email triggering the audit. Slack breadcrumb from an employee explaining one flagged item.
   - ***Example prompt illustrating this category:*** "Dmitri's audit flagged several stipend transactions from the ExpenseBot pilot that look wrong — duplicate receipt hashes, amounts over policy limits, and a few that got auto-approved for categories the client explicitly excluded. I need to go through every flagged item in the Airtable stipend records for Vectral and Mosaic and make a call on each one. For anything that's clearly out-of-policy, change the status to 'Held' and email the employee's manager explaining why. For anything ambiguous, check Slack and email for context before deciding. If you spot a pattern that looks systemic rather than one-off, create a Linear ticket so engineering can investigate. Post the full audit results in #finance when you're done."

3. **Vendor Payment Dispute:**
   - ***General guidance for this category:***
     - *Typical write actions:* `quickbooks_create_bill` (corrected vendor bill), `send_email` (dispute letter to vendor with evidence), `airtable_update_records` (correct move/vendor status), `conversations_add_message` (summary to #finance and #operations), `linear_create_issue` (track dispute resolution)
     - *Artifacts to inject:* Vendor bill with overbilling (2-3 incorrect line items). Slack breadcrumb from ops noting specific wrong line items. Airtable record showing a cancelled or reassigned move still on the invoice.
   - ***Example prompt illustrating this category:*** "Heartland Movers sent us a Q1 invoice for $12,800 covering eight moves but I don't think all of them are legitimate. I know at least a couple were cancelled and one was reassigned to Swift. Go through the invoice line by line and cross-check each move against our Airtable relocation records, Slack discussions, and any emails about cancellations. For any move that was cancelled or handled by a different vendor, document what you find. Create a corrected bill in QuickBooks reflecting only the valid charges, send Jake Loomis at Heartland a dispute email with the evidence for each line item we're contesting, and post a summary in #finance. If there's already a Linear ticket tracking this dispute, add your findings as a comment — if not, create one."

4. **Period-End Close / Accrual Review:**
   - ***General guidance for this category:***
     - *Typical write actions:* `quickbooks_update_account` (adjust accrual balances), `quickbooks_create_bill` (reclassify or record resolved liabilities), `send_email` (report to management), `linear_update_issue` (update tracking tickets with current status)
     - *Artifacts to inject:* Email from controller requesting month-end review. Slack breadcrumb with status update on a pending claim. Airtable record showing a liability status change.
   - ***Example prompt illustrating this category:*** "Elena needs the Q2 Contingent Liability Report before the board meeting. Pull together what we actually owe on Heartland, Mosaic, and the DOT audit. I've been using placeholders but the real numbers might be different. Cross-check QuickBooks, Airtable, Slack, and email. If any of the accrual amounts in QuickBooks don't match what you find, update them. Update the Linear tickets tracking each issue with your findings. Then email Elena the revised totals with evidence for each, CC Hana and Chloe. Get me the total dollar amount across all three, then message Chloe and Hana so we can lock this down before it blows up."

---

### Executive (10%)

Cross-functional decisions, organizational risk assessment, strategic direction. Spans all components for reading, but their write actions are primarily directives (emails, Slack messages) and strategic CRM decisions.

| # | Category | Pattern |
|---|----------|---------|
| 1 | **Cross-Functional Risk Assessment** | Board prep, crisis response, or strategic review → investigate across all departments → synthesize findings → issue directives and update tracking |
| 2 | **Strategic Account Review** | Review key account portfolio → assess health across dimensions → make retention/pricing decisions |
| 3 | **Executive Coordination** | Meeting prep, follow-up tracking, or briefing assembly → gather context across systems → schedule/communicate on behalf of executive |

**Per-category guidance:**

1. **Cross-Functional Risk Assessment:**
   - ***General guidance for this category:***
     - *Typical write actions:* `linear_create_issue` (track untracked risks), `linear_update_issue` (update status/description on existing risk tickets), `linear_create_comment` (add context to existing tickets), `crm_create_engagement` (deal notes for affected clients), `crm_update_deal_stage` (flag at-risk accounts), `send_email` (directives to department heads, status report to board/investor), `conversations_add_message` (#executive or #announcements, urgent coordination), `calendar_add_calendar_event` (coordination or emergency meeting)
     - *Artifacts to inject:* Trigger email from board member or investor asking for status, or inbound risk signal (regulatory notice, client ultimatum, vendor suspension). Slack breadcrumb showing a new development or which teams are affected. Airtable record showing active work now at risk.
   - ***Example prompt illustrating this category:*** "I have the board meeting next week and the risk register is stale. Go through everything from this quarter: vendor disputes, client complaints, compliance issues, cost overruns, anything that could come up. For each risk you find, check if there's already a Linear ticket tracking it. If not, create one with the right priority. If there is one, make sure the status and description are current, and update them if not. For any ticket you create or update, email the relevant department head so they know what changed and can follow up with their teams. Then update the CRM deal notes for any client where the risk affects the relationship, so the account team isn't blindsided. I need this done before Friday."

2. **Strategic Account Review:**
   - ***General guidance for this category:***
     - *Typical write actions:* `send_email` (decisions to CE team, outreach to at-risk client), `crm_update_deal_stage` (pricing/retention decisions per account), `crm_create_engagement` (strategic notes per account), `conversations_add_message` (summary to #executive), `calendar_add_calendar_event` (schedule check-in with at-risk client)
     - *Artifacts to inject:* Trigger email requesting the review (board prep, quarterly planning). Slack breadcrumb or email revealing a churn signal for one account (competitor pitch, key contact leaving, unresolved complaint). CRM engagement note from a recent client interaction showing a promise not yet fulfilled.
   - ***Example prompt illustrating this category:*** "I need a clear picture of our client portfolio before the quarterly planning session. Go through each active account — check the CRM for deal status and recent engagement notes, look at how their relocations are going in Airtable, and scan Slack and email for any satisfaction signals or complaints. I want to know which accounts are healthy, which are at risk, and which have expansion potential. For any at-risk account, add a strategic note to the CRM deal explaining the risk and what we should do about it. Email David and Mina with your findings and recommendations. If any client needs a check-in call, schedule one for next week."

3. **Executive Coordination:**
   - ***General guidance for this category:***
     - *Typical write actions:* `send_email` (communications on behalf of executive, follow-up reminders to department heads), `calendar_add_calendar_event` (schedule meetings), `calendar_edit_calendar_event` (reschedule as needed), `conversations_add_message` (follow-up pings, status requests in relevant channels), `crm_create_engagement` (log briefing prep or meeting context for client-facing meetings)
     - *Artifacts to inject:* Email from Elena or external stakeholder requesting a meeting or briefing. Slack breadcrumb showing a pending action item that needs follow-up (e.g., Elena asked a department head to do something last week with no visible response). Email from a stakeholder noting scheduling constraints or availability windows.
   - ***Example prompt illustrating this category:*** "Elena has a call with Rachel Whitfield from Vectral on Thursday about the contract renewal. I need to make sure she's fully briefed. Pull together everything on the Vectral account: the current deal status, the discount negotiation history, how their recent relocations went, and any open complaints or issues. Check if there are any action items Elena assigned to the team last week that haven't been completed yet. Look through her recent emails and Slack messages. Send a briefing email to Elena with everything she needs to know. If any follow-ups are still outstanding, ping the responsible person in Slack. And make sure the call is on Elena's calendar with the right details."

---

## Write Tool Coverage Matrix

| Write Tool | Ops | CE | Eng | Fin | Exec |
|------------|-----|-----|-----|-----|------|
| `send_email` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `reply_to_email` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `conversations_add_message` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `linear_create_issue` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `linear_update_issue` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `linear_create_comment` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `linear_create_project` | | | ✓ | | |
| `linear_update_project` | | | ✓ | | |
| `crm_create_deal` | | ✓ | | | ✓ |
| `crm_update_deal_stage` | | ✓ | | ✓ | ✓ |
| `crm_create_engagement` | | ✓ | | ✓ | ✓ |
| `airtable_create_record` | ✓ | ✓ | | | |
| `airtable_update_records` | ✓ | ✓ | ✓ | ✓ | |
| `calendar_add_calendar_event` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `calendar_edit_calendar_event` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `quickbooks_create_invoice` | | | | ✓ | |
| `quickbooks_create_bill` | | | | ✓ | |
| `quickbooks_create_customer` | | ✓ | | | |
| `quickbooks_update_account` | | | | ✓ | |

