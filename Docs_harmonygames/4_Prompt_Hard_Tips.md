# **Hard Prompts Tips**

---

This doc shares empirical search and difficulty patterns. Use it for intuition, not as policy or a checklist. Start from the [`Docs/README.md`](README.md) index and validate prompts with [`Evals/1_Prompt_Eval.md`](../Evals/1_Prompt_Eval.md) and [`Evals/5_Submission_Gate_Eval.md`](../Evals/5_Submission_Gate_Eval.md). Current Evals override older trajectory anecdotes.

For current service availability, exact operations, parameters, and pagination controls, treat [`HarmonyGames_Base_Universe/Tool_Access/`](../HarmonyGames_Base_Universe/Tool_Access/) as authoritative. For company facts, use the live HarmonyGames services and [`HarmonyGames_Base_Universe/`](../HarmonyGames_Base_Universe/). Examples here describe task patterns; they do not add tools, facts, or evaluation rules. Oracle Events are non-authoritative plans.

## Observations: How agents search

*These observations are from Claude Opus on investigation-heavy tasks.*

Agents do broad keyword searches and work with whatever comes back first. Once they have a plausible answer, they move on. They rarely follow up unless results explicitly point somewhere else.

**Agents skip structured systems.** Agents discover information through Slack and email conversations, but may fail to query authoritative systems like Linear, GitHub, GSheets, or Snowflake directly. In one trajectory, the agent read many messages where colleagues discussed structured records but relied on that secondhand discussion instead of checking the source.

If a task requires an authoritative source, make the expected outcome depend on facts available there. Add a Process rubric for source verification only when it passes the normal three-condition test; do not reward a particular tool call by default.

**Agents must plan scoped searches around membership.** Persona ACL is active:
Gmail, Slack, GCal, and Contacts reads depend on the assigned persona's mailbox,
conversation membership/visibility, calendar ownership/sharing/invites, and
contact visibility. The other nine services—GDrive, GitHub, Snowflake, GDocs,
GSheets, GSlides, Trello, Linear, and Confluence—remain unscoped, and writes are
outside ACL scope. Use [`15_Persona_ACL.md`](15_Persona_ACL.md) and the exact
identity in
[`Persona_ACL_Roster.json`](../HarmonyGames_Base_Universe/Persona_ACL_Roster.json).
Universe Explorer is author god-mode, so finding a record there or in a local
export proves existence but not Agent Runner reachability. Build the intended
path from persona-visible anchors or an authorized unscoped source.

**Agents don't search for follow-up evidence after finding a plausible status.** In the grounded HarmonyGames Helpshift wind-down arc, an internal discussion is not enough: the external invoice/termination evidence and the match3d/GoD integration PRs determine whether the invoices and migrations are actually closed. A shallow run can stop at the first “we're moving off it” discussion and miss the remaining back-invoices or implementation state.

If you add a dispute, complaint, or open question to the universe, also add a response from the other party. The response changes the correct answer. Most agents will find the dispute but not the response.

**Agents latch onto the first framing they encounter.** When a client complaint named 2 incidents and an internal engineering audit documented 5 (including the same 2), the agent reported 2\. It adopted the client's framing rather than the more complete internal data, even though it had access to both.

If the same issue appears in multiple sources with different levels of detail, agents tend to go with whichever version they find first. Placing the most complete version in a less obvious location (a Linear ticket description vs a Slack thread) makes the task harder.

**Data past the first result page is easy to miss.** Many enabled list/search tools expose a cursor, page token, page number, offset, or limit, but the exact controls differ by catalog. Agents often stop after the first response instead of paginating or narrowing the query. If your edit uses the same keywords as many existing messages, it may get pushed behind more recent traffic. Keep required evidence discoverable through a realistic query and verify the retrieval path against `HarmonyGames_Base_Universe/Tool_Access/*.json`; do not rely on an arbitrary result cap to manufacture difficulty. Slack thread replies are also easy to miss if the agent reads only channel history instead of the thread.

---

## Designing edits that create difficulty

### Linked edit chains

Single edits are binary: found or not found. Chains are where real difficulty comes from.

**The pattern:** Edit A creates a problem. Edit B resolves or changes it. The agent needs both to get the right answer.

**Grounded HarmonyGames example:** A Helpshift wind-down discussion (A) points toward closure, while Gmail invoice evidence and the match3d/GoD integration PRs (B and C) establish the remaining back-invoices and migration state. The correct write-up requires following the chain rather than treating the first internal status as final.

Three-link chains are harder. A describes a problem, B hints where the resolution might be ("I filed that on a different ticket"), C is the actual evidence on another service. The agent has to follow two hops.

### Making edits findable

Difficulty should come from connecting evidence, not from hiding it.

- **Use words the agent will search for.** If the agent searches "invoice", your edit needs "invoice" somewhere in it. An email with subject "Re: Follow-up on account" won't surface when the agent searches for "invoice" or "dispute."  
- **Stay inside result limits.** Date edits recently, or make them replies to existing threads that will appear in search results.  
- **The first link must be discoverable.** If Edit A can't be found through normal broad searches, the entire chain is invisible. The difficulty should be in connecting A to B, not in finding A.

### Ideas for edits (starting points, not an exhaustive list)

- A reply that changes a conclusion (vendor pushes back, someone corrects a number, insurer threatens denial)  
- A Linear issue filed with no corresponding Slack discussion  
- Conflicting data across services (Trello says one thing, a Linear investigation says another)  
- A near-miss entity (similar names in related contexts)  
- An unanswered message (agents notice what's there, not what's missing)  
- A dependency chain (answering X requires first looking up Y on a different service)

---

## Writing prompts that push the agent

**Go broad, not specific.** "Compile the quarterly financial summary" forces investigation. "Check if the cancellation met the SLA deadline" is a lookup with one answer.

**Hint without giving it away.** Phrases like "I've been using estimates but the real numbers might be different" or "double-check my assumptions" tell the agent to dig without saying where.

**You can name services or leave them unnamed  \-- both work differently.** "Cross-check GSheets, GitHub, Slack, and email" directs multi-service investigation but tells the agent where to look. "Figure out what's really going on and fix it" is harder because the agent has to decide which services to check on its own.

**Use the write actions the business outcome requires.** Appropriate HarmonyGames actions include updating Linear or Trello records, creating a Drive artifact, editing a Sheet, scheduling a calendar event, or posting in Slack. Do not add an action only to diversify tools.

**Do not add writes to increase the tool-call count.** Multiple write actions are valid only when each one is a realistic part of the requested outcome. Difficulty should come from necessary investigation, reconciliation, and action—not from manufacturing calls.

**Ask for both investigation and action when the scenario needs both.** Research-then-act tasks are harder than pure investigation. One thing we noticed: in 5 of 6 runs on one task, the agent wrote a great report but never posted the requested update. If the prompt asks for a Slack post, ticket update, or created artifact, cover that completed action with an Outcome rubric.

---

## Calibrating difficulty

**Too easy:** Edit shows up in the first search, agent grabs it, done. A Slack message saying "the budget is $75K not $50K." No reasoning needed.

**Sweet spot:** Findable with normal searches, but the Agent has to notice it matters and follow up. In the Helpshift wind-down, internal status, external invoice evidence, and implementation PRs each answer a different part of “are we fully moved off and paid up?” The Agent must reconcile all three before documenting what remains.

For HarmonyGames authoring, design toward **40+ necessary average calls across 3+ enabled services**. That is higher than the rejection floors: prompt evaluation requires **more than 15** necessary calls and **2+** services, while trajectory QC requires **at least 15 average** calls and **2+** services. Difficulty comes from necessary evidence and dependencies, not from padding calls to clear a number.

ACL-denied reads and repeated retries against the same inaccessible record are
not necessary work and do not count toward these targets. The platform's
`set_acting_user` step is environment configuration and is likewise excluded
from Oracle Events, rubrics, Process checks, and call counts.
