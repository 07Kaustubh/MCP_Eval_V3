## **Valid All Failures Rubrics**

When you run the verifier and see rubrics failing across multiple runs while the agent is clearly solving the task, the rubric, not the agent, is usually the problem. Under the current framework there are only two places this happens:

* **Process rubric failures**: the Process rubric is enforcing a single path the agent isn't required to take. Re-apply the three-condition [Decision Flow](https://docs.google.com/document/d/181pnDNIbiRKnlnqFD4Y9QWeDOYRkmIPk1TZLlTVLqXI/edit?tab=t.0#heading=h.b2efco7z2gf); if any condition fails, delete the rubric or tighten the Outcome instead.  
* **Outcome rubric failures**: the Outcome is either too strict (rounding/equivalent values) or bundles multiple independent facts. Loosen or split.

If all Outcomes pass and a Process rubric is failing, the agent found a valid solution. Process rubrics exist to verify necessary work that outcomes alone cannot prove. When a Process rubric punishes a valid path, fix the rubric; do not treat it as a legitimate failure.

* **Delete** when the rubric should never have been written (three-condition test fails, or a stricter Outcome would prove the same thing).  
* **Tighten the Outcome** when the underlying behavior can be captured by a precise value the agent could only produce by doing the work.

Never make a Process rubric "flexible" by enumerating alternative tools or query strings, that's deprecated TS/QC thinking and locks the rubric into a single execution path.

## **Outcome**

Check what the agent actually reported or did.

* **Agent reported an equivalent value:** If the rubric expects an exact number from raw data but the agent reasonably rounded or reformatted it, the rubric is too strict. Use "approximately" for calculated or non-discrete values, and accept any unambiguous reference to entities (e.g., "Thompson (LN-2026-00401)" instead of requiring "James Thompson").  
* **Rubric bundles multiple independent facts:** If the rubric checks two or more facts that can independently pass or fail, a single missed fact causes the entire rubric to fail, even when the agent got everything else right. Split into separate atomic rubrics so each fact is evaluated on its own.

## **Process (Optional)**

Check what the rubric is actually enforcing.

* **An Outcome rubric already captures the same requirement:** The Outcome rubric checks precise results that could only be produced by doing the work. The Process rubric adds no signal. Delete it.  
* **A stricter Outcome could capture the same requirement:** If you can name a precise value (an ID, an exact figure, a derived calculation) that the agent could only produce by doing the underlying work, the Outcome alone is enough. Delete the Process rubric and tighten the Outcome.  
* **The rubric names a specific tool or query path:** Process rubrics must be behavioral ("Agent verifies X"), not execution traces ("Agent calls tool\_Y"). If the rubric is tool-named, delete it and rewrite as a behavior, or drop it entirely if the behavior is already covered by an Outcome.

#### **Examples**

**Example 1: Process rubric where Outcomes already prove the work**

**Rubric:** "The Agent searches the CRM for Fatimah's clients before responding."

**Prompt says**: "Search the CRM for all of Fatimah's clients and tell me what you find."

**What happened:** All 6 runs searched the CRM. 2 runs searched a different way (e.g., engagements first, then contacts) and the rubric flagged it as a fail. All Outcomes pass.

**Why it's invalid:** The Outcome rubrics check five specific clients with names, companies, and cities from CRM data. Getting all five right proves the agent searched the CRM - the Process rubric adds no signal beyond what the Outcomes already enforce.

**Fix:** Delete the Process rubric.

**Example 2:** **Process rubric where a stricter Outcome would prove the work**

**Rubric:** "Agent consults the Stripe payment records and the closing disclosure document before reporting the fee discrepancy on the Flores file."

**What happened:** ~~The rubric is reward-hackable, the agent could pull unrelated artifacts from each source and still pass.~~ Across all 6 runs, the agent finds the Stripe charge amount ($792) and the closing disclosure amount ($528) mentioned in a processor's email thread to the borrower; it never calls Stripe directly and never opens the closing disclosure PDF. The Process rubric fails all 6 runs. The Outcome rubrics pass in every run.

**Why it's invalid:** The Process rubric prescribes a specific path (Stripe records \+ closing disclosure document), but the agent consistently reaches the same correct data through a different valid path (email thread). The rubric penalizes a valid alternative, creating a false negative.

**Fix:** Delete the Process rubric. Make the Outcome stricter:  
"Agent identifies a $264 overcharge on the Flores file, the difference between the $792 charge and the $528 closing disclosure amount.""

**Example 3:** Outcome fails because the rubric expects an exact value, but the agent reported an equivalent

**Rubric:** "The Agent identifies the loan amount as $347,289.50."

**What happened:** All 6 runs reported "approximately $347,000" or "$347,290". All other Outcomes pass.

**Why it's invalid:** The rubric uses an exact dollar amount from raw data, but the agent reasonably rounded it. The rubric should use "approximately" for calculated/non-discrete values.

**Fix:** "The Agent identifies the loan amount as approximately $347,000."

**Example 4:** Outcome fails because the rubric bundles multiple independent facts

**Rubric:** "The Agent reports the Thompson loan with outstanding appraisal conditions and a closing date of May 5."

**What happened:** All 6 runs correctly reported Thompson's appraisal conditions. 2 runs omitted the closing date. Those 2 fail the rubric entirely.

**Why it's invalid:** The rubric bundles two independent facts, condition status and closing date. The agent got one right but is penalized for both. This violates atomicity.

**Fix:** Split into two rubrics: (1) "The Agent identifies the Thompson loan as having outstanding appraisal conditions." (2) "The Agent includes the closing date of May 5 for the Thompson loan."

