# **→ Core Rules for Prompt Writing**

**NEW**: The agent is now capable of inferring time. In the StarPM (v4) universe it will take **July 1, 2026 (a Wednesday, US/Eastern)** as today's date, which means you are able to create relative time scenarios in prompts now.

* "*Sarah sent me this email 3 days ago*" means the email was received June 28, 2026.
* "*... and schedule a project review for next Friday*" is referring to July 10, 2026.
* Fixed dates are also valid; just beware anything before July 1, 2026, is in the past, and after it is obviously in the future.

## 

## **Post on OC**

Hi team,

Quick but important update for everyone to be aware of going forward.

**Agents Can Now Infer Time**

The agent is now capable of understanding and interpreting time references. For the StarPM universe it will treat July 1, 2026 as today's date, which opens up a great opportunity for you to incorporate relative time scenarios into your prompts.

**How This Works in Practice**

To give you a clear picture, here are a couple of examples:

* If a prompt states "Sarah sent me this email 3 days ago," the agent will understand the email was received on June 28, 2026.
* If a prompt says "...and schedule a project review for next Friday," the agent will interpret that as July 10, 2026.

**A Note on Fixed Dates**

You can also use fixed, specific dates in your prompts. Just be mindful of the following:

* Any date before July 1, 2026, will be treated as a past event.
* Any date after July 1, 2026, will naturally be treated as a future event.

This is a straightforward but meaningful change, so please keep it in mind when crafting your prompts. Being intentional with your time references will help ensure accuracy and consistency across the board.

**A note on the calendar:** July 1, 2026 is the first day of Q3 and the start of H2. June close activities (FP-2026-06) should be wrapping up or recently completed. Keep this quarter-boundary state in mind — prompts referencing "end of quarter" or "Q2 close" should be coherent with "Q2 just ended, Q3 just started."

**For reviewers**

For those of you on the review side, not much changes in terms of workflow. The main thing to be aware of is that you **may** (or **may not**, since it's not a requirement) start seeing prompts come through that use relative time references rather than fixed dates. As long as you keep the **July 1, 2026** baseline in mind, you should have no trouble evaluating these accurately. Just flag anything that seems off or inconsistent with the time logic outlined above.

Thanks, everyone!

## 

## **Prompt Examples**

* Prompt 1 – Project Operations / Status Review

*"So the client flagged something earlier this week - apparently the milestone deliverables for the Apex Digital migration aren't matching what we committed in the SOW, and honestly I haven't had a chance to dig in. Marcus has been on my case about getting the status report buttoned up before the steering committee on Friday, and the PM lead already sent me something about this back on June 25th that I completely dropped the ball on. Can you pull the project tracker and the deliverable log for those milestones and figure out what's off? Fix whatever needs updating, drop notes so we have a paper trail, and shoot me an email with the full picture. Oh, and post a rundown in \#project-updates for Marcus - he'll need to know what's still hanging."*

– Time logic: "Earlier this week" ≈ June 29–30, 2026. June 25th is a fixed past date. Today is Wednesday, July 1, 2026.

* Prompt 2 – Resource Management / Allocation

*"I'm a little worried about the contractor assignment. HR logged the onboarding request maybe ten days ago and as far as I can tell, nobody's confirmed the start date since. The project kickoff is supposedly next week and we can't afford to start without the full team. Can you piece together what's actually going on - the resource request, the emails, the Slack thread in \#resource-planning, whatever you can find - and check if there's anything unresolved that could block the assignment? Update the resource tracker with what you learn, route it to the hiring manager for approval, and ping the recruiter in Slack so they know where things stand before the kickoff date."*

– Time logic: "Maybe ten days ago" ≈ June 21, 2026. "Next week" = week of July 6, 2026.

* Prompt 3 – Risk / Compliance Review

*"This doesn't feel right - I'm seeing risk assessments that got auto-approved last night, but didn't we flag a missing security clearance on those vendor files like three days ago? Something's still going through that shouldn't be. Can you check the compliance records for anything that cleared since the flag and look at the audit trail to see if the remediation actually went through? If assessments are still clearing on incomplete documentation, we need a note added to each affected file, a heads-up in \#risk-and-compliance for the governance team, and someone needs to email the compliance officer because there's real regulatory exposure here."*

– Time logic: "Last night" = evening of June 30, 2026. "Three days ago" = June 28, 2026.
