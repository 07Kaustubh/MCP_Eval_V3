# **→ Core Rules for Prompt Writing**

**NEW**: The agent is now capable of inferring time. In the Brookfield (v3) universe it will take **June 12, 2026 (a Friday, US/Eastern)** as today's date, which means you are able to create relative time scenarios in prompts now.

* "*Daniel sent me this email 3 days ago*" means the email was received June 9, 2026.
* "*... and* *schedule a partner review for next Friday*" is referring to June 19, 2026.
* Fixed dates are also valid; just beware anything before June 12, 2026, is in the past, and after it is obviously in the future.

## 

## **Post on OC**

Hi team,

Quick but important update for everyone to be aware of going forward.

**Agents Can Now Infer Time**

The agent is now capable of understanding and interpreting time references. For the Brookfield universe it will treat June 12, 2026 as today's date, which opens up a great opportunity for you to incorporate relative time scenarios into your prompts.

**How This Works in Practice**

To give you a clear picture, here are a couple of examples:

* If a prompt states "Daniel sent me this email 3 days ago," the agent will understand the email was received on June 9, 2026.
* If a prompt says "...and schedule a partner review for next Friday," the agent will interpret that as June 19, 2026.

**A Note on Fixed Dates**

You can also use fixed, specific dates in your prompts. Just be mindful of the following:

* Any date before June 12, 2026, will be treated as a past event.
* Any date after June 12, 2026, will naturally be treated as a future event.

This is a straightforward but meaningful change, so please keep it in mind when crafting your prompts. Being intentional with your time references will help ensure accuracy and consistency across the board.

**A note on the close calendar:** June 12, 2026 sits *after* the FP-2026-05 BD3 lock target (June 3) and BD5 close target (June 5), but the three FP-2026-05 fiscal periods are still `status=open` (nobody actually locked them). FP-2026-06 has not started. Keep this between-state in mind - close-cycle prompts should be coherent with "lock target passed, ledger still open."

**For reviewers**

For those of you on the review side, not much changes in terms of workflow. The main thing to be aware of is that you **may** (or **may not**, since it's not a requirement) start seeing prompts come through that use relative time references rather than fixed dates. As long as you keep the **June 12, 2026** baseline in mind, you should have no trouble evaluating these accurately. Just flag anything that seems off or inconsistent with the time logic outlined above.

Thanks, everyone!

## 

## **Prompt Examples**

* Prompt 1 – Accounting Operations / Close

*"So Edith flagged something earlier this week - apparently the FP-2026-05 reconciliations for Acme Cloud aren't matching what we've got in the GL, and honestly I haven't had a chance to dig in. Andrea's been on my case about getting the close package buttoned up before partner sign-off, and Daniel already sent me something about this back on June 4th that I completely dropped the ball on. Can you pull the BlackLine reconciliations and the GL balances for those accounts and figure out what's off? Fix whatever needs fixing, drop review notes so we have a paper trail, and shoot me an email with the full picture. Oh, and post a rundown in \#monthly-close-coordination for Daniel - he'll need to know what's still hanging."*

– Time logic: "Earlier this week" ≈ June 8–11, 2026. June 4th is a fixed past date. Today is Friday, June 12, 2026.

* Prompt 2 – AP / Vendor Operations

*"I'm a little worried about the CrownPeak invoice. Owen logged it maybe ten days ago and as far as I can tell, nobody's approved it since. The vendor's payment terms are supposedly up next week and we can't afford a late fee right now. Can you piece together what's actually going on - the SAP invoice, the emails, the Slack thread in \#vendor-bills-and-ap, whatever you can find - and check if there's anything unresolved that could block approval? Update the AP exception record with what you learn, route it to Daniel for the approval since it's over $10K, and ping Owen in Slack so he knows where things stand before the due date lands."*

– Time logic: "Maybe ten days ago" ≈ June 2, 2026. "Next week" \= week of June 15, 2026.

* Prompt 3 – Compliance / Internal Controls

*"This doesn't feel right - I'm seeing AML reviews that got auto-cleared last night, but didn't we flag a missing beneficial-owner doc on those Acme files like three days ago? Something's still going through that shouldn't be. Can you check the BlackLine exception records for anything that cleared since the flag and look at the audit trail to see if the fix actually went out? If reviews are still clearing on incomplete BO evidence, we need a note added to each affected file, a heads-up in \#compliance-and-registrations for Marina's team, and someone needs to email Steven because there's real regulatory risk here."*

– Time logic: "Last night" \= evening of June 11, 2026. "Three days ago" \= June 9, 2026.
