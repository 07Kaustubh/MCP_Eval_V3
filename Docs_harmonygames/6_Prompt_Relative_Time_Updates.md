# **→ Core Rules for Prompt Writing**

**NEW**: The agent is now capable of inferring time. In the HarmonyGames universe it will take **February 28, 2026 (a Saturday)** as today's date, which means you are able to create relative time scenarios in prompts now.

Any action in a time-based example must also be supported by [`HarmonyGames_Base_Universe/6_Server_Tools_Details.json`](../HarmonyGames_Base_Universe/6_Server_Tools_Details.json); relative-time wording does not add a service or capability.

* "*Leonard sent me this email 3 days ago*" means the email was received February 25, 2026.
* "*... and schedule a project review for next Friday*" is referring to March 6, 2026.
* Fixed dates are also valid; just beware anything before February 28, 2026, is in the past, and after it is obviously in the future.

## 

## **Post on OC**

Hi team,

Quick but important update for everyone to be aware of going forward.

**Agents Can Now Infer Time**

The agent is now capable of understanding and interpreting time references. For the HarmonyGames universe it will treat February 28, 2026 as today's date, which opens up a great opportunity for you to incorporate relative time scenarios into your prompts.

**How This Works in Practice**

To give you a clear picture, here are a couple of examples:

* If a prompt states "Leonard sent me this email 3 days ago," the agent will understand the email was received on February 25, 2026.
* If a prompt says "...and schedule a project review for next Friday," the agent will interpret that as March 6, 2026.

**A Note on Fixed Dates**

You can also use fixed, specific dates in your prompts. Just be mindful of the following:

* Any date before February 28, 2026, will be treated as a past event.
* Any date after February 28, 2026, will naturally be treated as a future event.

This is a straightforward but meaningful change, so please keep it in mind when crafting your prompts. Being intentional with your time references will help ensure accuracy and consistency across the board.

**A note on the calendar:** February 28, 2026 is a Saturday and the last day of February — the second month of Q1/H1. January close is done; February month-end close activities are just beginning. Q1 does not end until March 31, so keep this mid-quarter state in mind — prompts referencing "end of quarter" or "Q1 close" should be coherent with "Q1 still in progress, one month remaining," and anything framed as "Q1 results are final" is incoherent.

**For reviewers**

For those of you on the review side, not much changes in terms of workflow. The main thing to be aware of is that you **may** (or **may not**, since it's not a requirement) start seeing prompts come through that use relative time references rather than fixed dates. As long as you keep the **February 28, 2026** baseline in mind, you should have no trouble evaluating these accurately. Just flag anything that seems off or inconsistent with the time logic outlined above.

Thanks, everyone!

## 

## **Prompt Examples**

* Prompt 1 – Engineering & Live-Ops / Status Review

*"The Season Pass on Zombie Match keeps throwing weird reward bugs after launch and I can't tell what's actually been fixed vs still open. Can you get to the bottom of it, make sure the right tickets reflect reality, and flag anything that's slipped through so the right engineer picks it up?"*

– Time logic: Season Pass bugs are recent; today is February 28, 2026. The agent reads Linear ZOM tickets, match3d PRs, `#season-pass`/`#zombie-bugs`, and the reward spec sheet to reconcile open vs fixed.

* Prompt 2 – Founders / Exec / Strategy

*"Where did the Mattel Barbie pitch actually end up, and what's outstanding if they come back? Put together a tight status brief for the founders."*

– Time logic: The Mattel pitch is a past event. The agent reads `#mattel_proposal`, pitch decks (Slides/Drive), the Gmail Mattel thread, and investor-update emails; writes a brief doc + `#founders` summary.

* Prompt 3 – Growth / UA / Marketing

*"I need to know where the Adjoe test actually landed before the board call — what we spent, what the retention looked like, and why we paused. Pull the whole picture together and drop a clean summary in the UA channel."*

– Time logic: The Adjoe test is a past event. The agent reads the Adjoe Gmail/Slack thread, internally recorded Singular figures, `#executives`, and available analytics evidence, computes spend/ROAS/D30 metrics, and posts a summary. Singular is a business topic here, not a directly accessible service.

## **Author checklist**

1. Resolve every relative phrase to an exact date or interval before submitting.
2. Check that the resolved date has the intended weekday, quarter, and business context.
3. Verify the relevant source records actually exist inside the resolved window; do not use a relative date to hide missing evidence.
4. Confirm names, dates, channels, repositories, and other tight identifiers against the HarmonyGames data.
5. Confirm every requested action is supported by [`HarmonyGames_Base_Universe/6_Server_Tools_Details.json`](../HarmonyGames_Base_Universe/6_Server_Tools_Details.json). Relative wording does not add a service or capability.
6. Resolve the assigned persona through the exact key/email in
   [`4_Persona_ACL_Roster.json`](../HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json)
   and verify that time-window evidence in Gmail, Slack, GCal, or Drive-family (GDrive/GDocs/GSheets/GSlides) is
   visible to that persona. Explorer/local-export existence alone is
   insufficient. See [`14_Persona_ACL.md`](14_Persona_ACL.md).

## **Reviewer note**

Apply the same fixed-date resolution before judging truthfulness, feasibility, or date alignment. For scoped reads, the resolved window must contain evidence reachable to the assigned Agent Runner persona, not merely author-visible evidence. A relative phrase fails when it makes the request impossible or incoherent, or when its resolved window does not contain the data needed for the ask. The `_changelog.timestamp` field is auto-generated and is not itself a date-alignment defect.
