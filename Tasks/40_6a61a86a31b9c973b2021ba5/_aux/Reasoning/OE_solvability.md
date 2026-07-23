# OE Solvability + OE-to-Rubric Preview (Task 40, StarPM V4)

## OE-to-prompt coverage map (forward)

| Prompt sentence / ask | OE step(s) |
|---|---|
| "close out today before Hill Country's Thursday install slot" | OE 12-19 (all writes wrap up today) |
| "want a fresh look before I sign off" | OE 10 (QB Line[0].Description read = the "fresh look" load-bearing loop) |
| "Diane, their AP contact at Hill Country, emailed me the summary" | OE 5 (Gmail thread d1e2f3a4b5c6789a) |
| "Tony posted in the maintenance channel Monday night endorsing that scope" | OE 3 (Slack C001 ts 1782789240.000301) |
| "The ticket went in Monday night at medium priority" | OE 7 (Airtable MT-2026-1327, fldPriority selMedium) |
| "Then last night Tanya called again... turned into something different" | OE 4 (Slack thread reply ts 1782863220.000303 — L5 lever) |
| "I dropped an update into the tenant thread I had going" | OE 4 (reads Carlos's tenant-relay thread) → OE 15 (writes back to same thread) |
| "have not touched the actual maintenance ticket yet" | OE 12 (Airtable ticket update, first time this pass) |
| "actually go through Diane's diagnostic write-up on the bill itself" | OE 9-10 (QB search_bills + get-bill Line[0].Description read = L2 lever) |
| "check whether the detail she has captured lines up with the summary" | OE 5 + OE 10 read both surfaces; OE 10 Conclude clause resolves the mismatch |
| "Whatever the diagnostic actually points to is the scope I want to move on" | OE 10 conclusion drives OE 12-18 write payload |
| "Bring the maintenance ticket current with the priority from last night's call and the scope we're actually going with" | OE 12 (Airtable update: selHigh + description) |
| "Update the operations tracking issue" | OE 13 (Linear save_issue OPS-231) |
| "drop a note walking through the rationale" | OE 14 (Linear save_comment) |
| "Drop back into the tenant thread with the same rationale" | OE 15 (Slack thread reply via slack_send_message, not draft) |
| "Draft Diane the revised confirmation so she can pull the right parts" | OE 16 (Gmail create_draft to ap@hillcountryplumbing.com) |
| "Tanya an update on the timing for the week" | OE 17 (Gmail create_draft to tanya.mitchell@gmail.com) |
| "Robert a heads-up on the cost" | OE 18 (Gmail create_draft to robert.finley@gmail.com) |
| "put the install on my calendar for Thursday morning" | OE 19 (GCalendar create_event 2026-07-02) |
| "Parts need pulling today so Hill Country's ready for Thursday morning" | OE 12 timeliness + OE 16 vendor draft close the loop |

Coverage: every prompt ask maps to at least one OE step. Reverse map: every OE step traces to a prompt sentence (no scope creep).

## OE-to-rubric preview (for S3)

| OE | Type | Likely rubric | Notes |
|---|---|---|---|
| 1 | Contact lookup | none (subsumed by OE 17 Outcome 1.1) | pure discovery |
| 2 | Owner CRM lookup | none (subsumed by OE 18 Outcome 1.1) | pure discovery |
| 3 | Slack discovery | none | discovery |
| 4 | Slack thread expansion | Outcome 2.1 candidate | L5 lever — priority conclusion is a fact the CB wants reported in rationale |
| 5 | Gmail read | none | discovery |
| 6 | Airtable base+table lookup | none | discovery |
| 7 | Airtable ticket search | none | discovery |
| 8 | Linear issue lookup | none | discovery |
| 9 | QB bill search | none | discovery |
| 10 | QB Line[0].Description read | **Outcome 2.1** (rationale content) | L2 load-bearing — the scope conclusion is the key fact the prompt asks to be told |
| 11 | Linear user id lookup | none | discovery |
| 12 | Airtable ticket update | **Outcome 1.1** (write action) + **Outcome 1.2** (priority + scope content) | selHigh + revised description |
| 13 | Linear issue update | **Outcome 1.1** (write action) + **Outcome 1.2** (description content) | scope reflected in description |
| 14 | Linear comment | **Outcome 1.1** (write action) + **Outcome 1.2** (rationale content) | walk-through rationale |
| 15 | Slack thread reply | **Outcome 1.1** (write action; must be `slack_send_message`, NOT draft) + **Outcome 1.2** (rationale content) | same rationale into tenant thread |
| 16 | Gmail draft to Diane | **Outcome 1.1** (draft to ap@hillcountryplumbing.com) + **Outcome 1.2** (revised scope + confirm parts) | draft-only in StarPM |
| 17 | Gmail draft to Tanya | **Outcome 1.1** (draft to tanya.mitchell@gmail.com) + **Outcome 1.2** (timing update) | tenant-appropriate framing |
| 18 | Gmail draft to Robert | **Outcome 1.1** (draft to robert.finley@gmail.com) + **Outcome 1.2** (cost heads-up ~$1,850) | owner-appropriate framing |
| 19 | GCalendar event | **Outcome 1.1** (create_event Thursday 2026-07-02 morning) + **Outcome 1.2** (summary/description/timezone) | America/Chicago CDT -05:00 |

Projected rubric count for S3: **~15-17 Outcome 1.1/1.2 rubrics + 1-2 Outcome 2.1 rubrics (scope conclusion + priority-flip rationale)**. Zero Process rubrics anticipated (no ordering constraints that Outcome cannot verify).

## AUDIT verdict
PASS (STRICT). One hard flag on density THIN under strictest lens (~28-30 midpoint AUDIT re-projection, 38-40 Council B re-projection). ACCEPTED under Hardness_Plan.md documented per-task THIN carry. Carry forward to FINAL for platform-run monitoring — if real-run average across 6 runs falls below 40 tool calls, treat as L31 pattern confirmed and route to `PIPELINE REDO`.
