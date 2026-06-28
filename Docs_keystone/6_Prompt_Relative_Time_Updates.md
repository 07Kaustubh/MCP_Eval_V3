# **→ Core Rules for Prompt Writing**

**The agent is capable of inferring time.** The Keystone Mortgage universe has a fixed "today" date:

| Universe | Fixed Date | Day of Week |
|----------|-----------|-------------|
| **Keystone Mortgage (v3.1)** | **April 28, 2026** | **Tuesday** |

**For Keystone Mortgage tasks, the fixed date is April 28, 2026 (a Tuesday, US/Eastern).**

* "*Elena sent me this email 3 days ago*" means the email was received April 25, 2026 (Saturday — verify the data has weekend activity).
* "*... and schedule a follow-up for next Monday*" is referring to May 4, 2026.
* Fixed dates are also valid; just beware anything before April 28, 2026, is in the past, and after it is in the future.

---

## 

## **Post on OC**

Hi team,

Quick but important update for everyone to be aware of going forward.

**Agents Can Now Infer Time**

The agent is now capable of understanding and interpreting time references. For the Keystone Mortgage universe it will treat April 28, 2026 as today's date, which opens up a great opportunity for you to incorporate relative time scenarios into your prompts.

**How This Works in Practice**

To give you a clear picture, here are a couple of examples:

* If a prompt states "Grace sent me this email 3 days ago," the agent will understand the email was received on April 25, 2026.
* If a prompt says "...and schedule a review meeting for next Monday," the agent will interpret that as May 4, 2026.

**A Note on Fixed Dates**

You can also use fixed, specific dates in your prompts. Just be mindful of the following:

* Any date before April 28, 2026, will be treated as a past event.
* Any date after April 28, 2026, will naturally be treated as a future event.

This is a straightforward but meaningful change, so please keep it in mind when crafting your prompts. Being intentional with your time references will help ensure accuracy and consistency across the board.

**A note on the loan pipeline calendar:** April 28, 2026 sits in the middle of a busy closing week — several loans have rate locks expiring April 29–30 and closings scheduled for April 28–May 2. Keep this time pressure in mind — pipeline prompts should be coherent with "locks expiring imminently, closings this week."

**For reviewers**

For those of you on the review side, not much changes in terms of workflow. The main thing to be aware of is that you **may** (or **may not**, since it's not a requirement) start seeing prompts come through that use relative time references rather than fixed dates. As long as you keep the **April 28, 2026** baseline in mind, you should have no trouble evaluating these accurately. Just flag anything that seems off or inconsistent with the time logic outlined above.

Thanks, everyone!

## 

## **Prompt Examples**

* Prompt 1 – Loan Pipeline / Closing Coordination

*"So Elena flagged something earlier this week - apparently the rate lock on the Martinez file is about to expire and the closing docs still aren't back from the title company. Robert already sent me something about this back on April 22nd that I completely dropped the ball on. Can you pull the loan file details and the Stripe payment history for their lock extension fees, figure out what's holding things up? Fix whatever needs fixing in the LOS activity notes, and shoot me an email with the full picture. Oh, and post a rundown in \#loan-processing for Tyler - he'll need to know what's still hanging before his Wednesday review."*

– Time logic: "Earlier this week" = April 27, 2026 (Monday). April 22nd is a fixed past date (the previous week). Today is Tuesday, April 28, 2026.

* Prompt 2 – Compliance / Borrower Escalation

*"I'm a little worried about the Henderson appraisal. The appraiser submitted it maybe ten days ago and as far as I can tell, nobody's reviewed the gap analysis since. The borrower's rate lock expires next week and we can't afford to miss that window. Can you piece together what's actually going on - the loan file notes, the emails, the Slack thread in \#loan-processing, whatever you can find - and check if there's anything unresolved that could block clear-to-close? Update the loan activity record with what you learn, route a heads-up to Grace since the lock is about to expire, and ping Elena in Slack so she knows where things stand before the borrower calls again."*

– Time logic: "Maybe ten days ago" ≈ April 18, 2026. "Next week" = week of May 4, 2026.

* Prompt 3 – Financial / Payment Discrepancy

*"This doesn't feel right - I'm seeing a Stripe charge on the Flores file from last night that looks like a duplicate lock extension fee, but didn't we already process that payment like three days ago? Something got charged twice. Can you check the Stripe payment records against the QuickBooks entries and the loan file to see what actually happened? If there really is a duplicate charge, we need a note added to the loan activity, a heads-up in \#general for the finance team, and someone needs to email Robert because we'll need to issue a refund before the borrower notices."*

– Time logic: "Last night" = evening of April 27, 2026. "Three days ago" = April 25, 2026.
