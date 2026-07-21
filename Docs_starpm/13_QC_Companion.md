Hi\! 👋 This is a friendly companion to the QC spec doc for the four entries that trip authors up most often in the StarPM universe.

A quick reminder on scoring:

- **1–2 → Fail**  
- **3–4 → Pass (Non-Fail)**  
- **5 → Perfect**

For each entry below, you'll see what each band actually means and a paired good/bad example using the same underlying request.

---

## 1\. Unique Ground Truth (UGT)

**What it's checking:** the prompt should lead to one correct *outcome*. It's totally fine if there are multiple ways for the agent to get there — but the place it ends up (the file it creates, the email it sends, the JE it posts) should be the same across any reasonable agent run.

**Heads up (06/09 change):** having a "leading interpretation" no longer saves a prompt. If two different reasonable readings of the prompt land the agent at two *different* final universe states (file vs. defer, write A vs. write B), it's a fail — even if most people would pick the same one.

**Score 1–2 (Fail) — "Multiple Valid Answers"** The prompt can reasonably produce two or more different correct answers, and there's no clear signal which one was intended. Classic shape: the agent could act now *or* defer; could escalate to partner A *or* partner B; could file in folder X *or* folder Y.

**Score 3–4 (Pass) — ⚠️ REMOVED on 06/09** **There is no longer a passing middle band for UGT.** The previous "Non-Fail – Multiple Valid Answers" category (which used to rescue prompts where a leading interpretation existed, or where a small logical assumption could disambiguate) was removed. **For UGT, the prompt is either clean or it's a Fail — there's no in-between.**

**Score 5 (Perfect)** Every expert reading the prompt would arrive at the same answer. The artifacts are anchored, the action is unambiguous, the recipients are pinned.

**A paired example — same request, two phrasings:**

❌ *Owen flagged a couple of aged TimeLedger invoices this morning — can you take a look and route the worst one to Steven for partner disposition? The SOW dispute's been dragging on.*

Two equally-aged invoices could be defensibly picked as "the worst one." Two agents, two different routing emails, two different final states.

✅ *Owen flagged TimeLedger invoice VEN-010-514242 this morning — 87 days past SLA, Phase-3 dispute still open. Pull the SOW from Airtable, check whether the credit memo Brenda promised actually landed, and route the disposition email to Steven Perry.*

Same casual tone, but the invoice is pinned, the receiving partner is named, and the path to the answer is the agent's to figure out.

### The prompt that caused this change:

Attempt ID *`6a27278b3cc447588955148f`* | Airtable filing

*Something about the Acme Cloud Q1 AR aging review from back in April has been bugging me. Anaya pulled the aging, Ben and Hannah weighed in on the bigger overdue accounts, and I put a package together and sent it up the chain but I've honestly lost track of where it ended up after that. Can you go back through everything tied to that review and work out exactly where it really stands now: what the aging actually came to, which accounts we flagged and what we decided on each, and whether it ever got signed off, filed, and out to the client, or whether it's just been sitting half-done since April? Then get it sorted based on what you actually find, **\>if\<** the sign-off never came through, chase whoever it's waiting on; **\>if\<** it was never filed, put the package where it should live; and make sure the people who'd need to know are looped in if this slipped, so we don't let it happen again on the Q2 cycle. And flag anything that doesn't look right along the way, I've got a nagging feeling a couple of the details on those overdue accounts weren't handled as cleanly as they should have been.*

Under the old spec, this prompt could land at NON-FAIL on both UGT and Clarity because a "*leading interpretation*" existed.

Under the new spec, it's a FAIL on both :

* UGT FAIL: Two correct end-states — (a) file the package now per literal text, (b) defer until sign-off is complete per universe state. Different final states of the universe → no longer rescued by NON-FAIL.  
* Clarity FAIL — Action Decision Ambiguity: The prompt is open to file-now vs. defer interpretations leading to different write actions. Triggers the new clause.

## 2\. Agent-Centric Phrasing

**What it's checking:** the *rubric* (not the prompt itself) describes the behavior of the Agent — Agent as subject, an actual verb, and just enough context to know what was done. And: no tool names anywhere.

**Score 1–2 (Fail) — "Rubric not written as an action performed by the Agent"** At least one criterion either:

- Uses passive voice or world-state framing ("*An email was sent…*", "*The May close is locked*")  
- Names a tool ("*The Agent calls `quickbooks_create_journal_entry`…*", "*via send\_email…*")  
- Talks about "the model," "the response," or the assistant instead of the Agent

**Score 3–4 (Pass) — "Agent-centric but doesn't follow the exact pattern"** The rubric is still an Agent action — it just doesn't follow the strict "Agent \+ verb \+ context" structure. Example from the spec: *"The Agent's status update to Peter Sanchez covers the AML threshold calibration session…"* — this is valid, just phrased a little differently.

**Score 5 (Perfect)** Clean, active, Agent as the subject, action and context both present, no tool names anywhere.

**A paired example — same rubric, two phrasings:**

❌ *A reclass entry of $12,400 between 500000 and 521000 is recorded on Acme's May period (via the create\_journal\_entry tool).*

Passive voice \+ a tool name. Both kill it.

✅ *The Agent posts the Datadog reclass journal entry on Acme's May period, moving $12,400 from 500000 to 521000\.*

Agent does the thing. The accounting detail stays in plain language, no flags or tool calls leaking through.

## 

## 3\. Prompt Clarity and Specificity

**What it's checking:** the prompt is clear enough that the user's intent comes through, *and* specific enough that the agent isn't guessing at what was actually asked. Importantly — this isn't about over-explaining. A good prompt sounds like a real internal message; the agent should still have real thinking to do.

**Heads up (06/09 change):** if the prompt is open to two reasonable interpretations that lead to *different write actions* (or to write vs. no-write, or act vs. defer), it's now an automatic fail — "Action Decision Ambiguity." Wording differences are fine; outcome differences are not.

**Score 1–2 (Fail)** Either:

- *Major Clarity / Specificity Issues* — the ask is too vague, the prompt is hard to follow, or critical details are missing and can't be reasonably assumed.  
- ***Action Decision Ambiguity (06/09)*** — the prompt could plausibly send the agent down two different action paths, and nothing in the prompt resolves which was meant.

**Score 3–4 (Pass) — "Minor Clarity / Specificity Issues"** The prompt could be read multiple ways, but every reasonable reading lands the agent on the *same* set of write actions. Only surface details vary — like email vs. Slack DM to the same person, or "the partner" where context makes it obvious who's meant. The outcome is the same; only the wrapper changes.

**Score 5 (Perfect)** The prompt sounds like a real internal message. The artifacts and people involved are clear, but the agent still has to work out *how* — which systems to check first, what to verify, what to flag. Natural language throughout, at most one tiny assumption needed.

**A paired example — same request, two phrasings:**

❌ *Help with the Acme May close — there's a reclass Andrea wants done before we lock.*

Which reclass? Which accounts? "Before we lock" — does that mean post now, or wait for the lock signal? An agent could plausibly defer or act, and they'd land on different write actions.

✅ *Acme May close is at BD1. Andrea's BD0 plan covered the standard accruals plus a Datadog enterprise-renewal reclass between 500000 and 521000 she wants quantified before lock. The April MAP has the prior line shape if you need a reference. Hand off to Daniel in \#monthly-close-coordination once posted — don't lock, that's the partner's call.*

Reads like a real Slack message. The agent still has to figure out the amount, the supporting JEs, the standing-entries flag pattern, what evidence to attach — none of that is pre-solved.

Note: The prompt that caused this change is also Attempt ID *`6a27278b3cc447588955148f`*, you can check how it affects **Clarity**, in section 1\. 

---

## 4\. Truthfulness *(major changes 06/10)*

**What it's checking:** every concrete fact in the prompt actually matches the StarPM universe. The 06/10 update introduced a clearer way to grade these errors — separating *major* (the kind that breaks tool calls) from *minor* (the kind that natural language can absorb).

**The 06/10 rule for classifying errors:**

- **Major errors** — wrong values in tight identifiers that get passed literally into tool calls: channel names, document IDs, JE IDs, vendor or entity names, account numbers, dollar amounts, dates, fiscal periods, ticket/issue IDs. These don't tolerate near-matches.  
- **Minor errors** — wrong values in loose descriptors that natural language can handle: first-name-only references where context makes the person obvious, slightly-off role titles, casual entity references.  
- **Escalation rule** — a "minor" error escalates to "major" if it actually causes the agent to fail. Example: using a first name where two people in the universe share it.

**Score 1–2 (Fail)**

- *Major Factual Errors* — the prompt contains 1 or more major errors.  
- *Minor Factual Errors* — the prompt contains 2 or more minor errors (especially common when there are throwaway sentences not strictly needed for the request).

**Score 3–4 (Pass) — "Minor Factual Errors"** The prompt contains exactly 1 minor factual error, and that error doesn't trip the agent up.

**Score 5 (Perfect)** No factual errors. No misleading statements.

**StarPM-specific landmines worth a quick glance before submitting:**

- **Personas vs NPCs.** NPCs can be *mentioned* in prompts, but they can't be the author or the acting voice. Owen Mercer, Lucia Ferreira, Brenda Abbas, Mateo Kovac, Yusuf Demir, Priya **Singh** (IRS) — all NPCs. Priya **Khatri** (AP Coordinator) is a persona — easy mix-up because of the first name.  
- **Acme sales tax \= TX / NY / WA / AZ.** Not TX-only. Not TX/GA/NC. Q1 2026 liability is $40,364.55.  
- **Audit team \= 4 people:** Mia Hartwell, Ryan Delgado, Devon Beale, Julia Vance. Don't invent extras.  
- **Account `135000 Prepaid Marketing`** exists on all three entities and is legitimate. The Cat 4.7 refusal pattern is about misusing it for a *finished* campaign, not the account itself.  
- **Account `525000` doesn't exist.** There's no dedicated Sales Tax Payable account in the CoA.  
- **Fiscal period IDs are entity-prefixed:** `acme_cloud_FP-2026-04`, never bare `FP-2026-04`.  
- **Retention codes:** only `AICPA_SQMS_7Y`, `IRS_TAX_7Y`, `FIRM_INTERNAL`, `INDEFINITE`. No SOX, no SEC.  
- **AP escalation aging:** the canonical scripted invoices sit at 81–87 days now. Only scen\_030 (LatticeHill) keeps older 300+d framing — it's the outlier.  
- **AP threshold ladder:** clerk → AP manager (≤$10K) → Controller (≤$50K) → Managing Partner (\>$50K). Steven for StarPM/Acme; Matthew for Northstar; Andrea for de-minimis.

**A paired example — same request, two phrasings:**

❌ *Need a partner-disposition memo on the Ledger invoice (`apinv_d3019cdc`) — it's been sitting at 87 days. Post the reversal on `FP-2026-04` against account 525000 for $24,400, and file the memo under SOX\_7Y once Steven signs off.*

Five major errors, and every one of them lives in a *tight identifier*: the invoice ID is truncated and won't resolve, the fiscal period is missing its entity prefix, account 525000 doesn't exist in the CoA, the dollar amount doesn't match the real invoice ($24,475.25), and SOX\_7Y isn't a valid retention code. Any one of these would either fail a tool call outright or could push the agent toward the wrong record.  
✅ *Need a partner-disposition memo on the TimeLedger Nexus invoice (`apinv_d3019cdcc6ed44b2`, $24,475.25, 87 days past SLA). Daniel Jones has already signed off as AP manager. Pull the SOW from Airtable, route to Steven Perry for clearance on `acme_cloud_FP-2026-04`, and file under AICPA\_SQMS\_7Y.*

Same references — "Daniel Jones," "Steven Perry," "the SOW" — but every tight identifier is exact: the invoice ID resolves, the dollar amount matches the real invoice, the fiscal period is entity-prefixed, and the retention code is valid. The takeaway: names and role references can stay in natural-language form, but anything the agent will pass literally into a tool call has to be right.

### The prompt that caused this change:

Attempt ID *`6a26b9aa1bb38faf2649f06e`* | The “vendor-bills” channel

*Steven signed off on releasing the undisputed portion of the TimeLedger Nexus invoice last month and I need this processed. The escalation file is complete, Brenda Abbas at TimeLedger confirmed the split, and the Linear issue is still sitting in the queue waiting for the payment to go through.*

*Can you pull the file together, finalize the release amount against the current AP position, get the payment documentation ready, notify Brenda Abbas that the undisputed portion is being released, close out the Linear ticket, and drop a wrap-up note in the **\>vendor-bills\<** channel so the team knows this one is done. Copy Steven on the final confirmation once the payment is queued.*

* The prompt names a Slack channel *`vendor-bills`* that does not exist in the universe (actual channel: *`vendor-bills-and-ap`*, ID *`C010`*, per *slack\_channels.json*). This is a phantom entity reference — exactly the pattern Truthfulness already catches under "1+ major factual errors."  
* Every named entity in the prompt — channels, people, vendors, IDs, dollar amounts, dates — needs to be verified against the universe data files before you submit. If a search in the relevant universe JSON turns up nothing, it's a Truthfulness fail. No exceptions, and a leading interpretation won't rescue it. This is Phase 2.3 of the prompt eval — please don't skip it.

---

**One-line takeaway for the four together:** anchor your artifacts (UGT), keep the Agent doing the verbs (Agent-Centric), let the prompt sound human while pinning the outcome (Clarity), and double-check every concrete value against the universe (Truthfulness).

Happy tasking\! 🌱  
