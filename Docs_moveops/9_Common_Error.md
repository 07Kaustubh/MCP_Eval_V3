# **Opposite Classic: Common Errors & How to Fix Them**

A practical guide about the most frequent errors observed in task and rubric creation.

---

## **Part 1: Prompt Writing Errors**

### **Error: Being too specific in the prompt**

**The problem:** Giving away IDs, or values the agent is supposed to *discover* defeats the purpose of the task. If you hand the agent the answer in the prompt, there's nothing to investigate.

❌ **Bad:** "Check the Heartland invoice HM-2026-Q1-0042 for overbilling." 

✅ **Good:** "The quarterly bill from our Midwest mover looks inflated."

❌ **Bad:** "Find the email from January 15th at exactly 3:47 PM mentioning $14,237.89."   
✅ **Good:** "I think there was a billing discrepancy in last quarter's invoices. Can you look into it?"

The rule: if the information is something the agent should *look up*, don't include it in the prompt.

---

### **Error: Writing sequential instructions instead of a natural request**

**The problem:** Step-by-step command lists tell the agent exactly what to do and in what order. This eliminates the investigation challenge and produces artificially short, scripted runs.

❌ **Bad:** "Search emails \> Check CRM \> Send apology email to Queen City Realty." 

❌ **Bad:** "First…Second…Third." 

✅ **Good:** "Queen City Realty seems upset about something. Figure out what's going on and handle it."

Real employees don't receive instruction scripts. They receive situations. Write situations.

---

### **Error: Mentioning tool names or parameter names**

**The problem:** Prompts should read like messages from a colleague, not API documentation. Tool names and parameter names don't belong in prompts.

❌ **Bad:** "Use crm\_search\_contacts to find Jason Park and then use send\_email with his address." 

✅ **Good:** "Can you pull up Jason Park's account and send him a follow-up?"

---

### **Error: Pre-solving the problem**

**The problem:** Telling the agent the root cause eliminates the core challenge of investigation. The agent should arrive at the answer - not be handed it.

❌ **Bad:** "Julian's demo is calling the weather API every 3 seconds, causing rate limiting. Fix the bug." 

✅ **Good:** "The API keeps failing and I'm getting paged. Something changed in the last few days. Figure out what's going on."

The second version requires the agent to connect Julian's demo to the rate limit problem across multiple services. The first is just a command.

---

### **Error: Bolting unrelated requests together**

**The problem:** Multiple tasks that share no common context don't test cross-service reasoning - they just inflate apparent complexity while giving the agent easy, isolated sub-tasks.

❌ **Bad (bolted):** "Check weather in Miami, send a Slack reminder for next week, email Carlos about Q3, and look up Seattle flights." 

✅ **Good (stacked):** "I'm meeting Patricia at UWM tomorrow and I need to walk in prepared. Make sure our internal tracking is up to date, get me caught up on any open items ops is working on for them, and block time with Amy this afternoon so we can align before the call."

In the good example, every sub-task flows from the same situation: preparing for the UWM meeting. In the bad example, the four tasks have nothing to do with each other.

---

### **Error: Every task ending with "send an email"**

**The problem:** It creates a monotonous pattern across tasks and misses more interesting write actions. **The agent should take diverse actions**.

Try using these instead or in combination: CRM deal updates, QuickBooks entries, Stripe payment actions, Stripe charges, Slack messages.

---

### **Error: Tasks that are too short or too simple**

**The problem:** A terse prompt like "Rebook the retreat" gives the agent nothing to work with. Real work requests include context, constraints, and multiple asks.

❌ **Bad:** "Rebook the retreat." 

✅ **Good:** "The MoveOps retreat venue fell through due to the storm. Find an alternative city that still works for the team, stays within roughly the same budget, and get the new details to everyone who needs to know. Make sure we're tracking this properly internally too."

---

**Part 2: Oracle Event Errors**

### **Error: Skipping discovery steps**

**The problem:** Oracle Events (OEs) should reflect *how* the agent finds information, not just what it finds. If your OE says "send email to Jordan" without a prior step to look up which Jordan and obtain their email, you've skipped a required discovery step.

❌ **Bad OE:** "Send email to Jordan about the delay." 

✅ **Good OE sequence:**

* OE 1: Search contacts for "Jordan" to identify the correct person and retrieve their email address.  
* OE 2: Send email to jordan.blake@moveops.com about the delay.

---

### 

### **Error: Describing findings instead of tool use steps**

OEs describe *actions the agent takes with tools*, not conclusions the agent reaches. The judgment about what the data means belongs in rubrics - the OE is the mechanical step.

❌ **Bad:** "The agent discovers that the Caliber Home Loans deal stage is closedwon." 

✅ **Good:** "Search CRM deals for the Caliber Home Loans account using crm\_search\_deals. The result will show the deal stage as 'closedwon'."

---

## **Part 3: Rubric Errors**

### **Error: Writing Process rubrics for things already covered by Outcome rubrics**

**The problem:** If you've already written an Outcome rubric confirming that ~~a tool was called with the right parameters, adding a TS or QC rubric for the same tool creates redundant, overlapping rubrics.~~ a write action happened with the right details or that a key fact was reported, adding a Process rubric for the same behavior creates redundant, overlapping rubrics.

**The fix:** Follow the Outcome-first workflow:

1. Write all Outcome rubrics (1.1, 1.2, 2.1) first.  
2. Then look at the remaining non-write-action tool calls from your OEs.  
3. Apply the four-condition Decision Flow to decide if a Process rubric is warranted (not explicitly asked, required by every valid path, can't be captured by a stricter Outcome, behaviorally graded).  
4. Never write a Process rubric for a behavior that Outcome already covers.

---

### **Error: Process rubric phrased as a tool call**

**The problem:** Process rubrics must describe agent behavior, not name specific tools or query strings. A rubric like "Agent called crm\_search\_companies with query 'PennyMac Wholesale'" is a deprecated TS/QC-style check and locks in a single execution path.

❌ **Bad:** "The model must pass a query related to 'PennyMac Wholesale' (or similar) when calling crm\_search\_companies." 

✅ **Good:** "Agent verifies the PennyMac Wholesale account status from the CRM before responding."

If the same requirement can be captured by a stricter Outcome rubric (e.g., a precise figure or ID the agent could only get by doing the lookup), prefer the Outcome and drop the Process rubric.

---

### **Error: Forcing a single channel when the prompt allows multiple**

**The problem:** If the prompt says "send" or "share" without specifying a channel, both email and Slack may be valid. A rubric that requires only email would fail correct Slack-based runs.

❌ **Bad:** "The Agent sent an email to elena.marchetti@moveops.com." 

✅ **Good:** "The Agent notifies Elena Marchetti (elena.marchetti@moveops.com or Slack equivalent) about the coordinator issue."

When the prompt names a goal rather than a method, the rubric must match the prompt's level of specificity.

---

**Error: Bundling independent tool calls into one rubric**

**The problem:** A single rubric checking 3 recipients across 3 different tool calls to 3 different people for 3 different purposes cannot be graded atomically. If one fails and two succeed, the rubric fails - but you've lost signal on what actually went wrong.

**The only acceptable bundling** is for parameters of the *same* tool call, or for tightly coupled facts from the same data record.

❌ **Bad (bundled across calls):** The Agent sent emails to Carlos (about Q3), Grace (about the board meeting), and Elena (about the coordinator issue). 

✅ **Good (split):**

* Rubric 1: "The Agent sent an email to carlos.rivera@moveops.com about Q3 financials."  
* Rubric 2: "The Agent sent an email to grace.yamamoto@moveops.com about the board meeting."  
* Rubric 3: "The Agent sent an email to elena.marchetti@moveops.com about the coordinator issue."

**Acceptable bundling example:** The Agent sent an email to elena.marchetti@moveops.com, CC grace.yamamoto@moveops.com."  both are in the same tool call's parameters, so they're appropriately checked together.

---

### 

### **Error: Criterion that requires external knowledge to evaluate**

**The problem:** The judge only sees the trajectory. If your rubric says "email sent to the CEO" but doesn't tell the judge who the CEO is, the rubric cannot be evaluated.

Every rubric must be fully self-contained.

❌ **Bad:** "The Agent emailed the CEO."   
✅ **Good:** "The Agent sent an email to grace.yamamoto@moveops.com (Director of Operations)."

❌ **Bad:** "The Agent contacted the right coordinator."   
✅ **Good:** "The Agent sent an email to hana.kim@moveops.com (Bookkeeper)."

---

### **Error: Values in rubrics that don't match universe data**

**The problem:** If your rubric says a deal stage is "qualification" but the CRM actually shows "closedwon," every correct agent run will fail that rubric. This produces false negatives - runs that fail not because the agent was wrong, but because your rubric was wrong.

**Fix:** Always **verify rubric values against the explorer** and **trajectory runs** before finalizing. Run the agent and check the trajectory to confirm the data matches your expectations.

---

### **Error: Rubric requiring actions the prompt never asked for**

**The problem:** If the prompt never asked the agent to email rachel.whitfield@client.com, a rubric requiring that email will fail every run - not because the agent failed, but because you invented a requirement.

Rubric must map to: a direct ask from the prompt, an implicit ask (something a reasonable person would obviously do given the situation), or a write action that logically follows from the task.

If you can't point to why the prompt requires this action, the rubric shouldn't exist.

---

### **Error: Mixing reasoning into the criterion field**

**The problem:** The criterion field is what the judge evaluates. It must be a clean, standalone yes/no claim. Reasoning belongs in the justification field.

❌ **Bad criterion:** "The Agent CCs elena.marchetti@moveops.com on the reply to Darnell, as Grace's email instructs Darnell to loop in Elena." 

✅ **Good criterion:** "The Agent CCs elena.marchetti@moveops.com on the reply to Darnell." 

✅ **Good justification:** "Grace's email thread explicitly instructs Darnell to loop in Elena. Failing to CC her would mean Elena is unaware of the client issue."

---

### **Error: Using "approximately" for fixed static values**

**The problem:** "Approximately" signals that a calculated or rounded value is expected. Using it for exact counts, IDs, or dates implies uncertainty that doesn't exist - and can make the rubric too lenient or confusing.

❌ **Bad:** "The Agent created approximately 3 CRM deals."  
✅ **Good (count):** "The Agent reports 3 overdue loans in the pipeline (Thompson LN-2026-00401, Flores LN-2026-00512, Webb LN-2026-00598)." 

❌ **Bad (calculated value):** "The Agent's email body references the exact budget of $15,432.10"  
✅ **Good (calculated value):** "The Agent's email body references a budget of approximately $15,000."

Only use "approximately" when the agent has to calculate or round a value and slight variation is expected.

---

### 

### **Error: Unfair Rubric Criteria**

**The problem:** In the case that a rubric criterion/criteria fail all 6 trajectories, we need to investigate these criteria further to ensure they are fairly evaluating the trajectories.

For example, in the case where all outcome rubrics are met, but the trajectories keep failing a tool selection criteria, we need to identify this, and potentially remove this failing criterion. 

![][image1]

**If and only if** we can  **vehemently defend**  the existence of this criterion, should we keep it. Otherwise, we need to remove it.

**Fix:** Always **review the Rubrics Verifier Matrix** to identify any potentially unfair rubric criteria. **Always** investigate rubric criteria that fail all 6 trajectories.

---
