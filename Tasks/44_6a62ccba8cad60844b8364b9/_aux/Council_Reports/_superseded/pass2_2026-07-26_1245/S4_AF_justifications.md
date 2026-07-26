# All-Failing Criteria: Justifications

Verification ran on two models with six runs each. Every criterion below failed in all six runs of at least one model. Each entry is keyed by its title and states the concrete fact the agent had available and the gap that kept it out of the deliverable.

Eight criteria failed in all six runs on **both** models. Twenty-three further criteria failed in all six Gemini runs while passing at least once on Opus 4.8, so the Opus passes are the achievability proof for those.

---

# Part 1. All-failing on both models

**"The Agent raises a tracking item for the portfolio HVAC filter replacement run that was never finished."**

No run on either model raised a tracking item for the unfinished portfolio filter run. John Smith posted in the maintenance channel on May 23, 2026 that the supply closet was almost out of 20x25 filters and he needed a restock before he could finish the run, and nothing later in that channel records the restock arriving or the run being completed. Ten of the twelve runs instead treated the portfolio filter spot-check as a clean pass and closed it out. The filter block is the fact that falsifies the all-units basis of that spot-check, so missing it removes the agent's only reason to question the record. This is a genuine model gap, not a rubric issue.

**"The Agent's filter run tracking item states that John Smith reported on May 23, 2026 that a 20x25 filter shortage was blocking him from finishing the run."**

Every run had John Smith's May 23, 2026 message in its first read of the maintenance channel and none carried the shortage forward into any record it wrote. The message is explicit that the restock is a blocker on finishing the run rather than a routine supply note. One Opus run reached the finding and put it in a comment on an existing record instead of the item the work called for, and no Gemini run surfaced it at all. This is a genuine reasoning gap, not a rubric issue.

**"The Agent's filter run tracking item records Brooke Phillips's outstanding request to Elias Navarro for a filter stock count ahead of a bulk order."**

Brooke Phillips replied to John Smith the same afternoon asking Elias Navarro for a quick count on filter stock before placing a bulk order, and no reply to that ask exists anywhere in the records. That message was returned in the same channel read that returned John Smith's post, so it was available in all twelve runs. None recorded it. The pending stock count is what keeps the filter run blocked rather than merely delayed, which is why it belongs on the item. This is a genuine model gap, not a rubric issue.

**"The Agent's filter run tracking item names the owner of that work, which must be one of: John Smith, Elias Navarro, or Brooke Phillips."**

Because no run raised the filter run item, no run named who holds that work. John Smith was executing the run, Elias Navarro was asked for the stock count, and Brooke Phillips owns the bulk order decision, so three defensible owners were available and each is a named contact. The instruction to name the person who owns each open piece of work is direct and every run applied it correctly on the items it did raise. This is a genuine model gap, not a rubric issue.

**"The Agent's tracking work for outstanding tenant access covers the two North cluster units that OPS-56 records as still held up by tenant scheduling conflicts."**

OPS-56 records that Tony flagged two North cluster units still pending because of tenant scheduling conflicts and asked Carlos to push a second round of access notices, with no closing reply on that ask. Every Opus run collapsed those two units into the two North units Jaime Salinas flagged on May 23, 2026 as needing HVAC attention, which are a different pair: the flagged pair was walked and found deficient, the OPS-56 pair was never entered at all. No Gemini run logged tenant access work of any kind. Two Opus runs had OPS-56 and its access-notice text in their results and still did not separate the pairs. This is a genuine reasoning gap, not a rubric issue.

**"The Agent records that OPS-99 and OPS-108 carry the same East cluster HVAC QC title while sitting in two different workflow states."**

OPS-99 and OPS-108 carry the identical title "East cluster HVAC service complete - QC passed" while OPS-99 sits In Progress and OPS-108 sits Backlog. Three Opus runs retrieved both records, correctly called them duplicates of one another, and still never compared their workflow states. Every Gemini run retrieved both and moved both to Done without noting that they disagreed. The agents read the prose on both records and did not read the state column that decides whether either one closes anything. This is a genuine model gap, not a rubric issue.

**"The Agent records that neither East cluster QC record, OPS-99 nor OPS-108, is in a completed workflow state."**

Neither East record was in a completed state when any run retrieved it, and both say in their own text that the East service passed QC. Opus runs that reached the correct conclusion got there from Jaime Salinas never having run the East inspection rather than from the records' states, and one wrote that OPS-99 was In Review without addressing OPS-108. Every Gemini run set both to Done, which is the opposite finding. This is the structured-field observation the task turns on and it is a genuine model gap, not a rubric issue.

**"The Agent leaves a note on OPS-98 stating that the record was never moved to a completed workflow state despite its own text saying both cluster issues were moved to Done."**

OPS-98 sits In Progress while its own comment of May 25, 2026 says "I'm moving both cluster issues to Done." Four Opus runs left a substantive note on OPS-98 retracting the sign-off on field grounds and none noted that the record was never actually moved. One Opus run reached that exact finding and wrote it on a sibling record instead, which shows the observation is available and was simply not placed where the work called for it. Every Gemini run commented on OPS-98 affirming the pass and then moved it to Done itself. This is a genuine reasoning gap, not a rubric issue.

---

# Part 2. All-failing on Gemini, passing at least once on Opus 4.8

**"The Agent's new maintenance ticket describes the two North cluster units Jaime Salinas flagged on May 23, 2026 as needing HVAC attention right away."**

Jaime Salinas posted on May 23, 2026 that the North cluster walk-throughs were done and two units needed HVAC looked at right away, with coil, plumbing and panel notes. No follow-up record for those two units exists anywhere. All six Gemini runs created maintenance tickets, and every one of them covered South cluster plumbing only. All six Opus runs put the two flagged units in a ticket, so the finding is reachable from the same channel read. This is a genuine model gap, not a rubric issue.

**"The Agent's West cluster tracking item states that OPS-186, dated June 17, 2026, records the West Cluster work as still underway."**

OPS-186 is dated June 17, 2026 and states in its own description that the West Cluster work is still underway, which is the latest dated statement on that cluster anywhere in the records. No Gemini run carried it into a tracking item; two of the six moved OPS-186 to Done with a note saying the electrical inspections it describes were complete, which reads the first half of the description and drops the second. One Opus run carried the statement correctly. This is a genuine reasoning gap, not a rubric issue.

**"The Agent raises tracking work or a maintenance ticket covering the push units still waiting on tenant access."**

Two separate access holdovers are on the record: a South cluster unit that was never entered because the tenant was out during the scheduled window, and two North cluster units held up by tenant scheduling conflicts. No Gemini run raised any work item covering either. Three Opus runs did, using the same records, so the material is discoverable. This is a genuine model gap, not a rubric issue.

**"The Agent's tracking work or maintenance ticket for outstanding tenant access covers the single South cluster unit that was never serviced because the tenant was not home during the scheduled access window."**

OPS-43 records the no-access unit in its own description and the reschedule ask with Carlos appears in the maintenance channel as well. No Gemini run logged that unit in any ticket or tracking item. Three Opus runs created a dedicated ticket for it naming the access reschedule and the service that follows. This is a genuine model gap, not a rubric issue.

**"The Agent's tracking work for outstanding tenant access names the owner, which must be one of: Carlos Mendez, Elias Navarro, or Tony Reyes."**

Because no Gemini run raised tenant access work, none named who holds it. Carlos Mendez was asked to re-coordinate access, Elias Navarro runs the service once access is set, and Tony Reyes raised the North scheduling conflicts, so three defensible owners were available. Every Gemini run named owners correctly on the items it did raise, so the instruction was understood and the gap is the missing item. This is a genuine model gap, not a rubric issue.

**"The Agent's plumbing tracking item states that the water heater replacements were escalated to a budget priority."**

Brooke Phillips escalated the water heater replacements to a budget priority on June 3, 2026, and the June 2 check-in agenda names the budget implications of the water heaters Carlos flagged. All six Gemini runs wrote a plumbing item and described the two water heaters as past serviceable life, and none carried the escalation. Five of six Opus runs did. The escalation is what separates a flagged repair from an approved one, which is the difference the supervisor needs. This is a genuine reasoning gap, not a rubric issue.

**"The Agent leaves a note on OPS-87 stating that the record does not stand as a close-out of the South and North cluster QC."**

OPS-87 sits in Todo, its title says both cluster spot-checks passed, and its description says the results were commented on each cluster's issue and both were moved from In Review to Done. All six Gemini runs left a note on OPS-87 confirming the pass and then moved the record to Done. Five of six Opus runs left a note stating the record does not close out the QC. The agent is required to record where its own spot-check landed, and affirming a pass that the field evidence contradicts is the failure this criterion detects. This is a genuine model gap, not a rubric issue.

**"The Agent leaves a note on OPS-96 stating that the portfolio filter spot-check does not stand because the filter run was still blocked on a 20x25 filter restock when it was logged."**

OPS-96 claims a spot-check across all units where filter replacements were completed, logged on May 30, 2026, one week after the run was reported blocked on a 20x25 restock with no record of the restock arriving. Every Gemini run commented that the filter spot-check passed with no deficiencies and moved OPS-96 to Done. Five of six Opus runs treated it as a clean pass as well, and the sixth scoped it to filters only rather than withdrawing it. The blocked run is the fact that makes the all-units claim unsupportable. This is a genuine reasoning gap, not a rubric issue.

**"The Agent's channel status update states that one South cluster unit was never serviced because the tenant was not home during the scheduled access window."**

The no-access unit is the one South cluster item that was never worked at all, so the crew's shared picture is wrong without it. No Gemini channel post mentions it. Four of six Opus posts do, naming the access reschedule and the owner. This is a genuine model gap, not a rubric issue.

**"The Agent's channel status update states that the two units Jaime Salinas flagged in the North cluster on May 23, 2026 still need the HVAC work she called out."**

Every Gemini channel post reported the North cluster as complete and passed. All six Opus posts reported the two flagged units as still needing a tech, from the same May 23 channel message. Telling the crew North is clean when two units were walked and found deficient is the specific misstatement this criterion detects, and the Opus run set shows the correct statement is reachable. This is a genuine model gap, not a rubric issue.

**"The Agent's channel status update states that the access follow-up on two North cluster units held up by tenant scheduling conflicts is still open."**

OPS-56 records the two North units held up by tenant scheduling conflicts and the second round of access notices Tony asked Carlos to send, with no reply on that ask. No Gemini post carries it. One Opus post does. The pair is distinct from the two units flagged on the walk-through, and no run on either model separated them cleanly, which makes this the hardest single item in the set. This is a genuine reasoning gap, not a rubric issue.

**"The Agent's channel status update states that the East cluster QC record is not in a completed workflow state."**

Both East cluster QC records were in non-completed states when every run retrieved them. Every Gemini post reported East as complete and passed, and four of the six had already moved both records to Done before posting. Four of six Opus posts stated the East QC was not confirmed. This is a genuine model gap, not a rubric issue.

**"The Agent's channel status update states that the latest dated status statement on the West cluster records that work as still underway."**

OPS-186 of June 17, 2026 is the most recent dated statement about the West cluster and says the work is still underway. No Gemini post reports it; the posts that mention West describe remaining inspection scope in the agent's own words instead. One Opus post cites the dated statement. Grounding the West position in the latest record rather than in a summary of it is what the criterion asks for. This is a genuine reasoning gap, not a rubric issue.

**"The Agent's draft to Brooke Phillips states that the South cluster's open item is the unit that was never serviced because the tenant was not home during the scheduled access window."**

No Gemini draft names the no-access unit. Every Gemini draft frames the South cluster's open work as the plumbing repairs alone, which are real but are not the unit that never received service. Four of six Opus drafts name it. The supervisor cannot schedule what the email does not surface. This is a genuine model gap, not a rubric issue.

**"The Agent's draft to Brooke Phillips states that the missed South cluster unit still has to be re-scheduled for service before the push can close."**

The reschedule is the action that closes the no-access unit, and it is named in the records as an ask to Carlos that was never answered. No Gemini draft names it, because no Gemini draft identified the unit. Four of six Opus drafts name the reschedule as a close condition. This is a genuine model gap, not a rubric issue.

**"The Agent's draft to Brooke Phillips states that the two North cluster units flagged on May 23, 2026 still need a technician back onsite."**

Every Gemini draft reports the North cluster as complete with no open work. All six Opus drafts state that the two flagged units still need a tech. This is the same May 23 field note that all twelve runs had in their channel read, and the divergence is entirely in what each model did with it. This is a genuine model gap, not a rubric issue.

**"The Agent's draft to Brooke Phillips separately identifies two North cluster units held up by tenant scheduling conflicts whose access follow-up is still open."**

The access-held pair and the deficiency-flagged pair are different units with different remedies, and both are open. No Gemini draft carries the access-held pair. One Opus draft carries both separately. Collapsing them understates the North cluster's open work by half. This is a genuine reasoning gap, not a rubric issue.

**"The Agent's draft to Brooke Phillips states that the East cluster QC is unconfirmed because the East cluster QC record is not in a completed workflow state."**

Every Gemini draft reports East as complete and QC passed. Three of six Opus drafts report East QC as unconfirmed, though most reach it from Jaime Salinas never having run the inspection rather than from the record state. The record state is the durable basis, because the prose on both East records asserts the opposite. This is a genuine model gap, not a rubric issue.

**"The Agent's draft to Brooke Phillips states that the East cluster QC has to be confirmed before the push can close."**

Five of six Gemini drafts present East as closed, so no close condition is stated for it. Five of six Opus drafts name the East QC as a prerequisite for closing. One Gemini draft did name it and is being appealed separately as a grading error. This is a genuine model gap on the remaining five runs, not a rubric issue.

**"The Agent reports in its final response that none of Jaime Salinas's three QC spot-check records, OPS-87, OPS-96, and OPS-98, was in a completed workflow state as the Agent found them."**

All three spot-check records were in non-completed states at retrieval while their own text claims moves to Done or In Review. No Gemini response reports the as-found states; all six moved the records to Done and reported that as the reconciliation. Two of six Opus responses report the as-found states. The criterion accepts a response that reports the states as found and then corrects one of them, so moving a record is not itself the failure. This is a genuine model gap, not a rubric issue.

**"The Agent reports in its final response that the South cluster still has one unit that was never serviced because of a missed tenant access window."**

No Gemini response mentions the no-access unit. Four of six Opus responses do. The unit is recorded in the South cluster issue description that every run retrieved, so this is a reading gap rather than a retrieval gap. This is a genuine model gap, not a rubric issue.

**"The Agent reports in its final response that the two North cluster units Jaime Salinas flagged on May 23, 2026 still require the HVAC work she called out."**

Every Gemini response reports the North cluster as complete and passed. All six Opus responses report the two flagged units as still open. Both models read the same May 23 field note in the same channel, and the whole divergence is whether the agent let that note override the cluster records that say North is clean. This is the sharpest cross-model split in the set and it is a genuine model gap, not a rubric issue.

**"The Agent reports in its final response that the East cluster QC is unconfirmed rather than complete."**

Five of six Gemini responses report East as complete and QC passed. Four of six Opus responses report the East QC as unconfirmed. One Gemini response reported East QC as pending and is being appealed separately as a grading error. This is a genuine model gap on the remaining five runs, not a rubric issue.
