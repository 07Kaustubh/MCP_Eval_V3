# **Hard Prompts Tips**

---

This doc shares what we learned from analyzing 10+ task trajectories, combined with tips from CBs who built the hardest tasks so far. Use it for intuition, not as a checklist. Overfitting to these patterns makes the dataset less useful.

## Observations: How agents search

*These observations are from Claude Opus 4.6 on investigation-heavy tasks.*

Agents do broad keyword searches and work with whatever comes back first. Once they have a plausible answer, they move on. They rarely follow up unless results explicitly point somewhere else.

**Agents skip structured databases.** Agents discover information through Slack and email conversations, but rarely query structured systems like QuickBooks, CRM, or Airtable directly. In one trajectory, the agent read hundreds of Slack messages and emails where colleagues discussed QuickBooks data, referenced invoice numbers, and mentioned CRM records by name. Despite seeing these systems mentioned constantly, the agent never called a QuickBooks or CRM tool. It used secondhand information from conversations instead of querying the source.

If your task requires data from CRM, QuickBooks, or Airtable, the agent may find a workaround through Slack and email. Your rubrics should check whether the agent actually used the right data source.

**Agents don't search for responses to things they find.** If an agent finds an email where Carlos disputes a $4,800 title fee, it reports the dispute. It doesn't search for "did the vendor reply?" In one task, the vendor Tryon Title had emailed back explaining that one of the three disputed charges was actually valid because the file cancellation missed their 48-hour SLA window. Four of five runs never found the vendor's reply. The one that did had searched for the vendor contact by name.

If you add a dispute, complaint, or open question to the universe, also add a response from the other party. The response changes the correct answer. Most agents will find the dispute but not the response.

**Agents latch onto the first framing they encounter.** When a client complaint named 2 incidents and an internal engineering audit documented 5 (including the same 2), the agent reported 2\. It adopted the client's framing rather than the more complete internal data, even though it had access to both.

If the same issue appears in multiple sources with different levels of detail, agents tend to go with whichever version they find first. Placing the most complete version in a less obvious location (a CRM record vs a Slack thread) makes the task harder.

**Data past search result limits is invisible.** Search results cap at the top results returned. If your edit uses the same keywords as many existing messages, it may get pushed out of results by more recent traffic. Date edits recently, or make them replies to existing threads so they appear near the top. Slack thread replies are also hard for agents to find  \-- if someone asks "Is this approved?" in a thread, the agent often sees the question but not the answer in the replies.

---

## Designing edits that create difficulty

### Linked edit chains

Single edits are binary: found or not found. Chains are where real difficulty comes from.

**The pattern:** Edit A creates a problem. Edit B resolves or changes it. The agent needs both to get the right answer.

**Example from a real task:** Carlos disputes Tryon Title's $4,800 fee (A, easy to find). Denise at Tryon Title replies saying one charge is actually valid because the file cancellation missed the 48-hour SLA (B, harder to find). Only 1 of 5 runs found Denise's reply. That run was the only one with the correct financial total.

Three-link chains are harder. A describes a problem, B hints where the resolution might be ("I filed that on a different ticket"), C is the actual evidence on another service. The agent has to follow two hops.

### Making edits findable

Difficulty should come from connecting evidence, not from hiding it.

- **Use words the agent will search for.** If the agent searches "invoice", your edit needs "invoice" somewhere in it. An email with subject "Re: Follow-up on account" won't surface when the agent searches for "invoice" or "dispute."  
- **Stay inside result limits.** Date edits recently, or make them replies to existing threads that will appear in search results.  
- **The first link must be discoverable.** If Edit A can't be found through normal broad searches, the entire chain is invisible. The difficulty should be in connecting A to B, not in finding A.

### Ideas for edits (starting points, not an exhaustive list)

- A reply that changes a conclusion (vendor pushes back, someone corrects a number, insurer threatens denial)  
- A CRM note filed with no corresponding Slack discussion  
- Conflicting data across services (CRM says one thing, a loan file note says another)  
- A near-miss entity (similar names in related contexts)  
- An unanswered message (agents notice what's there, not what's missing)  
- A dependency chain (answering X requires first looking up Y on a different service)

---

## Writing prompts that push the agent

**Go broad, not specific.** "Compile the quarterly financial summary" forces investigation. "Check if the cancellation met the SLA deadline" is a lookup with one answer.

**Hint without giving it away.** Phrases like "I've been using estimates but the real numbers might be different" or "double-check my assumptions" tell the agent to dig without saying where.

**You can name services or leave them unnamed  \-- both work differently.** "Cross-check QuickBooks, CRM, Slack, and email" forces multi-service investigation but tells the agent where to look. "Figure out what's really going on and fix it" is harder because the agent has to decide which services to check on its own.

**Diversify your write actions.** Most tasks right now end with "send an email." Try prompts that end with updating CRM deal stages, adding loan activity notes, or posting status updates in Slack. For example: "Update every open loan condition with the current status, reassign anything that's stuck, and send a follow-up reminder for next week" targets CRM, the LOS, and Slack instead of email.

**Use multiple write actions to push tool calls above 40\.** "Update the tickets, then email the report to Elena, CC Hana and Priya." Every write action needs reads first (contact lookups, ticket IDs, channel names). This naturally increases tool call count.

**Ask for both investigation and action.** Research-then-act tasks are harder than pure investigation. One thing we noticed: in 5 of 6 runs on one task, the agent wrote a great report but never actually sent it. It confused producing content with executing the action. If your prompt says "send Robert a summary," your rubrics should check that `send_email` was actually called.

---

## Calibrating difficulty

**Too easy:** Edit shows up in the first search, agent grabs it, done. A Slack message saying "the budget is $75K not $50K." No reasoning needed.

**Sweet spot:** Findable with normal searches, but the agent has to notice it matters and follow up. The agent finds a vendor dispute, and the vendor's reply says "two of these charges are valid per our SLA." Now the agent has to re-examine which charges are actually disputed, look up the SLA, and revise its numbers.  
