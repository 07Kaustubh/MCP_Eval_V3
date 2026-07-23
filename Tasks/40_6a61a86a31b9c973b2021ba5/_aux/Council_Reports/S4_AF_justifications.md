# S4 AF Justifications — Bucket 3 (Legitimate Model Failure)

Style contract: concise, human, first-person, no em-dashes, no rubric numbers, no internal artifact names. Two to four sentences per justification. Each cites the concrete data fact and the specific reasoning gap. Each entry is keyed by the rubric criterion text so the platform reviewer can match it directly.

---

## Slack #maintenance thread post to the tenant-relay parent

Rubric: The Agent posts a message in the #maintenance Slack channel (C001) as a reply in the thread anchored at thread_ts 1782824160.000302, using the send-message action rather than the draft action. (Opus 6/6 all-failing.)

Opus fails to post the Slack reply to the tenant-relay thread in every one of the six runs, and it fails in three distinct ways. In four of the six runs there is no slack_send_message call at all, and one of those runs makes the omission explicit in the final response with the line "One thing I did not do: post in #maintenance to Tony." In one run Opus does call slack_send_message on channel C001 but leaves thread_ts empty, landing the note as a top-level channel post rather than a reply inside the tenant thread. In the last run Opus posts with thread_ts 1782863220.000303, which is the evening escalation reply's timestamp, not the parent tenant-relay message at 1782824160.000302 that the prompt asks the agent to drop back into. Across all six runs the model either skips the required send or anchors the reply to the wrong message, which is the intended failure mode when the authority-figure Slack endorsement and the multi-thread structure make the correct thread anchor easy to lose.

---

## Slack post covers the corrected full-replacement scope

Rubric: The Agent's Slack message in the #maintenance thread anchored at 1782824160.000302 covers the corrected scope of a full water heater unit replacement. (Opus 6/6 all-failing.)

This rubric cascades off the missing valid slack_send_message on the parent tenant-relay thread. Because Opus never lands a valid post anchored to that thread across any run, there is no message body available to check for the corrected scope claim. The two runs that do call slack_send_message with wrong anchors carry the full-replacement language in their message bodies, so the content is being generated correctly. The failure is a tool-target failure that propagates through every downstream content check on the same thread.

---

## Slack post covers the escalation to High priority

Rubric: The Agent's Slack message in the #maintenance thread anchored at 1782824160.000302 covers the escalation to High priority. (Opus 6/6 all-failing.)

Same cascade as the corrected-scope Slack rubric. No valid post anchored to the parent tenant-relay thread across any run means there is no body to grade against for the priority-escalation claim. The two runs that post to the wrong thread do include the escalation language, so this is not a content-generation issue but the same tool-target failure propagating.

---

## Slack post covers Thursday install slot retention

Rubric: The Agent's Slack message in the #maintenance thread anchored at 1782824160.000302 covers that the Thursday install slot is being kept for the fuller scope. (Opus 6/6 all-failing.)

Same cascade. No valid post on the tenant-relay parent means the Thursday-slot content cannot be graded. Fails the same way as the two prior cascades, and the fix is the same fix at the send-side rather than the content-side.

---

## Airtable description note active leak with occupants at home

Rubric: The Agent's update to Airtable ticket rec92f4a1c8e17bd3 revises fldDescription to note the active leak with occupants at home (or similar phrasing). (Gemini 6/6 all-failing.)

Gemini's Airtable description mentions the active leak in all six runs but consistently drops the occupants-at-home atom that the evening thread reply on ts 1782863220.000303 makes prominent with the line "no hot water since 4 PM and there is a puddle spreading on the kitchen floor now. Kids are back home tonight." One run says "active kitchen floor leak reported 06/30", another says "puddle spreading on kitchen floor", another says "active floor leak", and the remaining three use similar leak-only phrasings without ever noting that the tenant, the children, or occupants are home. The leak atom lands but the safety-context atom does not, and the other model lands both atoms in five of six runs, which shows the criterion is achievable for a capable agent. The gap here is Gemini's generation style deprioritizing the secondary safety atom when a single leak phrase already covers the urgency.

---

## Linear OPS-231 update called

Rubric: The Agent updates Linear issue OPS-231. (Opus 1/6 in one run; Gemini 2/6 in two runs.)

The runs that fail this rubric never call save_issue on OPS-231, so the Linear write does not land. In each failing run the trajectory shows the agent inspecting the Linear issue on read but then jumping to save_comment or to the Gmail drafts without doing the description update. This is the standard multi-write attrition pattern where an agent orchestrating writes across five services drops the middle write when the write budget feels stretched, and the failure surfaces here rather than on a discovery-side rubric because the description update is the harder-to-justify step once a comment already exists.

---

## Linear OPS-231 description reflects full replacement, cost, and Thursday slot

Rubrics: The Agent's Linear OPS-231 update revises the description to reflect a full water heater unit replacement scope rather than the exchanger-only quote. The Agent's Linear OPS-231 update revises the description to reflect the approximately $1,850 cost figure. The Agent's Linear OPS-231 update revises the description to reflect that the Thursday install slot is retained. (Opus 2/6 in two runs; Gemini 2/6 in two runs.)

These three cascade off the missing Linear update. When the failing runs skip save_issue entirely there is no description to check for the corrected scope, the corrected cost, or the retained Thursday slot. One Opus run does call save_issue on OPS-231 but with an empty description string, which lands the update as a technical success but leaves nothing to grade against, so the same three atoms fail. In both models the failure is real and traces to the model dropping content it correctly produced elsewhere in the run.

---

## Owner draft identifies the unit as a Ruud RS75

Rubric: The Agent's draft to robert.finley@gmail.com identifies the unit as a Ruud RS75 (or similar phrasing). (Opus 2/6 in two runs.)

Two Opus runs write the owner-facing draft to Robert with the phrase "12-year-old Ruud heater" but drop the "RS75" model suffix, while the same run's Diane draft and Linear comment correctly include "Ruud RS75". The model number lives explicitly in the QuickBooks diagnostic bill line description that Opus has already read, so this is not a data-availability failure. It is Opus tuning the owner-facing register slightly more conversational and stripping the SKU as unnecessary detail for a property owner audience, missing that the criterion requires the model identifier for owner-side traceability back to the asset.

---

## Airtable description note tenant without hot water (single-run)

Rubric: The Agent's update to Airtable ticket rec92f4a1c8e17bd3 revises fldDescription to note the tenant is without hot water (or similar phrasing). (Opus 1/6 in the first run.)

Opus first run's Airtable description says "intermittent hot water on 06-29; follow-up call the evening of 06-30 reported the problem worsening" but never says the tenant is currently without hot water. The evening thread reply is explicit ("no hot water since 4 PM") and the other five runs land the atom cleanly, so this is a single-run generation slip on a first-draft description that Opus wrote more sparsely than its later runs. Real fail, low incidence.

---

## Airtable description note active leak with occupants at home (single-run Opus)

Rubric: The Agent's update to Airtable ticket rec92f4a1c8e17bd3 revises fldDescription to note the active leak with occupants at home (or similar phrasing). (Opus 1/6 in the first run.)

Same thin-description pattern as the same-run without-hot-water failure. The description references "problem worsening" instead of naming the puddle spreading on the kitchen floor and the children being home. The other five runs include both atoms, so the failure is a run-level generation slip rather than a systematic omission.

---

## Linear comment note tenant without hot water (single-run)

Rubric: The Agent's comment on Linear issue OPS-231 notes that the tenant is without hot water (or similar phrasing). (Opus 1/6 in the first run.)

The Linear comment on OPS-231 in the same first run says "Tanya's follow-up call the evening of 06-30 confirmed the problem worsened" but does not name the no-hot-water condition. The same run correctly cites the diagnostic write-up and the model and the age and the supersession, so the model has full context in scope but drops the specific tenant-impact phrasing in the comment body. Later runs land it.

---

## Linear comment note active water pooling with occupants at home

Rubric: The Agent's comment on Linear issue OPS-231 notes active water pooling with occupants at home (or similar phrasing). (Opus 1/6 in the first run; Gemini fails 3 or 4 of 6 runs across the batch.)

Opus first run shows the same thin-comment pattern as the same run's Airtable failure, dropping the safety atoms. Gemini shows the same systematic omission pattern as its Airtable failure: the leak atom lands but occupants-at-home does not. Runs where Gemini skips the Linear comment entirely fail for the cascade reason. The consistent atom drop across both the Airtable and Linear surfaces on Gemini confirms this is a stable model tendency, not a rubric defect.

---

## Airtable priority set to selHigh (single-run Gemini)

Rubric: The Agent's update to Airtable ticket rec92f4a1c8e17bd3 sets fldPriority to selHigh. (Gemini 1/6 in the fourth run.)

Gemini's fourth run is the run where multiple downstream writes drop off (the Linear update rubric group all fail in the same run because there is no save_issue there). The Airtable priority miss in the same run traces to the same run-wide attrition rather than a stumping lever specific to the priority atom.

---

## Owner draft references initial $310 quote (single-run Gemini)

Rubric: The Agent's draft to robert.finley@gmail.com references the initial approximately $310 quote (or the exact $310). (Gemini 1/6 in the fourth run.)

Same run attrition pattern. Gemini's fourth run writes the Robert draft but omits the initial $310 quote reference. Other Gemini runs land the atom, so the failure is a run-level shortening rather than a systematic omission.
