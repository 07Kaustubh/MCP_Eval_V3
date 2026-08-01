# AUDIT: 6_Oracle_Events.txt (36 steps)

Task: Tasks/46_6a62ccb6ce2323b4b9e0c8d8
Universe: starpm, today 2026-07-01 America/Chicago
Method: every claim re-derived from `_aux/Universe_Split/` by direct query. No prior report was consulted or trusted.
Standard applied: 5 of 5 only. Every "should" read as "must".

## Scope of verification performed

- 127 identifier-shaped tokens extracted from the file (rec ids, comment ids, ticket ids, Slack message ids, calendar base ids and row ids, QuickBooks entity ids, DocNumbers, MT / DLQ numbers, emails, tbl / fld / sel / app ids, state ids, team ids, project ids, channel ids, Slack ts values). All 127 resolve verbatim in the universe. Zero misses.
- 76 double-quoted strings extracted. 71 match universe text verbatim. The 5 that do not are search query strings, one quotation from the prompt, and one hypothetical phrasing, none of which asserts universe content.
- All 33 tool names cross-checked against `StarPM_Base_Universe/7_Server_Tools_Details.json`.
- Every make-ready and maintenance row in the two clusters read in full.
- All 565 calendar rows grouped into 125 base events and swept.
- All QuickBooks rows for both owners read line by line.
- No em-dash or en-dash present in the file.

## What is correct (verified, not assumed)

Recorded so the revision does not disturb it.

- Tool names and parameters: all 33 tools exist verbatim, and every parameter named sits on the tool it is attached to. `search_records` correctly uses `table` while `update_records_for_table` correctly uses `tableId`. `get_table_schema` correctly uses `tables`. `slack_send_message` correctly uses `message` rather than `payload`. `create_draft` correctly uses `body` and the draft-only framing is right. `list_issue_statuses` correctly uses `team`. PASS on check 2.
- Every pinned record resolves to exactly one universe row. Calendar targets are named as per-calendar rows, never as bare base ids, and the claim that no stored row carries a bare base id is true across all 565 rows. The suffix-to-calendar mapping in OE 31 is exact: `-b6a1e41c` is teresa.wood, `-0f82233a` is brooke.phillips, `-b0504ab4` is lisa.smith. PASS on check 3.
- OE 1 to OE 12: OPS-10 is the only issue of 230 with "Mid-Year" in its title. Its `updated_at` equals its `created_at` at 2026-05-03T22:11:57.112604-05:00. OPS-11 and OPS-13 share a title. OPS-23 repeats it in different case. OPS-39 sits in state_OPS_3 with zero comments while OPS-93 sits in state_OPS_1 with the pair's only comment. C006 holds 43 rows, 12 top-level and 31 replies, 7 of the top-level belonging to the mass email campaign and 5 forming the named 2026-05-28 cluster. 346 of 580 Slack messages are thread replies. The parent's `latest_reply` of 1782860664.000001 matches no message anywhere. The two Lisa messages in C004 are 19 minutes apart. All exact.
- OE 11 and OE 21 sourcing claims: "94%" appears in exactly five rows, of which only Lisa's own message and the OPS-100 comment repeating it concern Mesa Vista or Finley, and the HubSpot Oakfield Commons occupancy deal named as the unrelated collision is real. "97%" appears in exactly one row, Lisa's own message. Exact.
- OE 22 to OE 26 money: Finley open invoices 2026-494 at 8,400.00 due 2026-05-31, 2026-303 at 2,190.00 due 2026-06-05, 4421 at 390.00 due 2026-06-12, summing to 10,980.00, with 5848 at 640.00 settled by a linked payment. Harris three invoices at 510.00, 60.00 and 1,345.00, each Balance 0.00, each matched by a payment of the same amount. Credit memos 3,655.00 and 1,975.00 with the exact DocNumbers given. All 117 credit memos in the universe carry Balance equal to TotalAmt, no LinkedTxn, and RemainingCredit 0. Four of the six wear BILL- or INV- prefixes. 10,980.00 less 3,655.00 is 7,325.00. Invoice 2026-494 is 31 days past due at 2026-07-01. Customer rows carry only Active, CompanyName, DisplayName and PrimaryEmailAddr. Every figure exact.
- OE 27 to OE 29 calendar: 20 calendars. Lisa holds 16 rows, latest 2026-06-02, none on or after today. `fullText "Portfolio Review"` returns exactly the four mid-year reviews and nothing else. The Harris original carries five rows with all four attendees accepted. The rescheduled instance carries four rows with Aurora and Patricia declined and Teresa accepted, and Lisa holds no row on it. The Finley review is 2026-05-19 11:45 to 13:15, four rows, Lisa and Aurora declined, Finley not an attendee. A sweep of 2026-06-01 through 2026-06-09 returns no Finley event. David Shea has zero calendar presence. The Slack source for the Harris "casual 45-minute morning call late June" description is real, in C004 from Teresa Wood. All exact.
- OE 10, 18, 20, 32: the three near-identical Mesa Vista move-out tickets exist and only ticket_87552e6b23bc5a92bd2641b9054b8c13 names Robert Finley, in its closing sentence. The three Mesa Vista deals do associate to comp_proj_fef06d5fa2b2, comp_proj_8a64d674466b and comp_riogrande while Finley sits under comp_mesaverde. Exactly seven maintenance rows are open, and the empty completion value is stored 3 times as an empty string and 4 times as null. The water heater records resolve as stated. Exactly one Brooke Phillips exists in contacts, Slack and HubSpot, with the contact id, email and job title given.
- OE 30 direction of correction: all three graded rows are genuinely selSched and all three are genuinely contradicted by their own sibling or cross-service evidence. The correction set is right; the reasoning around it is not (see issues 2, 3 and 4).

## Issues

Ten issues. Each is a claim the universe contradicts or a graded conclusion resting on evidence no step retrieves. Numbered for tracking. Replacement wording is given verbatim and contains no em-dash or en-dash.

### Issue 1 (MAJOR, check 6). OE 13's uniqueness claim is false.

Claim: "This is the only row anywhere in the universe that names Harry Harris alongside a property."

Universe: five further rows carry CustomerRef Harry Harris and name a property.
- 317923399822, invoice B2026-086: "April landscaping - perimeter beds and irrigation check, Palomar Gardens (Verde Grounds LLC)".
- 879979204592, invoice 2026-057: "Monthly property management fee - Fernwood Gardens, June 2026".
- 390637322875, credit memo 2026-CM-089: "Credit adjustment - HVAC materials overcharge reversal, Maple Ridge Building 2", with PrivateNote "Apply against next management invoice for Maple Ridge Residential LLC".
- 120329707702, credit memo INV-2026-0841-572: "Monthly property management fee - 4402 Larkspur Ave, Unit 7".
- 262820673328, credit memo BILL-2026-0336: "Electrical outlet repair and panel inspection - 233 Elmsworth Blvd, Unit 7A".

The claim is false as written, and the file itself retrieves three of those five rows at OE 24 and OE 25, so it contradicts its own later steps.

### Issue 2 (MAJOR, check 6). The ItemRef discriminator does not settle ownership, and the universe refutes it in both directions.

Claim: "the Harris invoice carries ItemRef 'Monthly Management Fee', which is the charge a manager raises against a property owner, while the Okafor invoice carries ItemRef 'Unit Turn / Make-Ready'. Harris is therefore the Sunset Ridge owner".

Universe: the item is not owner-specific.
- Simone Okafor, the party the step calls the decoy, carries 2 "Monthly Management Fee" lines of her own.
- Tanya Mitchell, a delinquent tenant, carries 3. Connor Beaumont, a departing tenant, carries 3.
- Robert Finley, the universe's other confirmed owner and this task's second owner, carries zero "Monthly Management Fee" lines. All four of his invoices and all three of his credit memos carry "Drywall / Water-Damage Repair" or "Unit Turn / Make-Ready".

An agent applying the stated rule symmetrically would also conclude Harris owns Maple Ridge Building 2, from credit memo 390637322875 which carries the same ItemRef, and would conclude Robert Finley owns nothing.

### Issue 3 (MAJOR, checks 4 and 6). OE 13 scopes the Sunset Ridge cluster to Harris using the one unit OE 18 declares ungradeable.

Invoice 113714702211's only property reference is "Unit 14, Sunset Ridge Apartments", and OE 13 generalises from it to "the whole Sunset Ridge cluster". OE 18 then states that ownership of Sunset Ridge Unit 14 "is contested in the universe and must not be asserted", citing Gmail 2ae48555b3009a95, which is real: Brooke Phillips writes to linda.castillo@gmail.com requesting "your written authorization to proceed with an eviction petition against Tanya Mitchell at Unit 14".

The file therefore builds a graded scoping decision on a record whose subject it later rules out of bounds. Every route from Harris to Sunset Ridge in this universe runs through Unit 14: invoice 4422, OPS-32 ("the Tanya Mitchell eviction case at one of Harry Harris's units"), and calendar event nuh928ma4rwhwf1bnap30rmfli ("JP court hearing for the Mitchell eviction at the Harris property"). Two of those three are never cited by OE 13, and the third is the contested one.

### Issue 4 (MAJOR, checks 4 and 5). OE 30's stated reason for excluding reca8230a8fd9ff51 is factually false.

Claim: "reca8230a8fd9ff51 (Sunset Ridge Unit 14) is conditional on the balance remaining unresolved and the unit becoming vacant, neither of which has happened."

Universe, three independent records, all dated before 2026-07-01:
- rec8005502043b755: "Payment Plan Breached - No Response after the June 23 installment went unmet ... Total outstanding balance remains unresolved."
- rec3782834f35df50: "Tenant did not cure the outstanding balance before the June 29 three-day notice deadline and made no contact with the office. Delinquency confirmed."
- Gmail 2ae48555b3009a95: "the cure deadline expired June 29 with no payment received."

The balance limb has plainly happened. Only the vacancy limb has not. The row's own note, which records that Mitchell "committed to a payment timeline", is superseded, which by the file's own correction logic makes this row out of step with the ground in exactly the way rec987aae7d522057 is. The exclusion may still be right, but not for the reason given, and a rubric derived from this sentence would be wrong.

### Issue 5 (MAJOR, checks 4 and 7). The "only unresolved and untracked item" claim is false, which makes OE 35's target ambiguous.

OE 15 claims the Mesa Vista 310C subfloor assessment is "the only item in either cluster that is both unresolved and untracked". OE 35 repeats it as "the only open item in either cluster that is carried nowhere".

Universe: reca06d89f1a4ac5b (Sunset Ridge 309C) reads "Waiting on final utility transfer confirmation before scheduling vendor access. John to confirm whether HVAC filter replacement is included in base scope or billed separately." The string "utility transfer" occurs in exactly one row in the entire universe, that one. Nothing resolves it and no ticket, issue or calendar event carries it. OE 30 concedes the point in its own words: "waiting on a utility transfer that no record resolves".

Two items in the clusters are therefore unresolved and untracked, and an agent that opens its single new issue for the 309C blocker satisfies the prompt's "whatever is still genuinely unresolved" on the file's own criteria while failing OE 35.

### Issue 6 (MAJOR, check 4). A confirmed future calendar event contradicts OE 30's reading of Mesa Vista 4C and is never reconciled.

OE 30 states that Mesa Vista 207A and 4C "each carry selProg rows alongside a selReady row stating the unit is finished and cleared for leasing, so those rows are also out of step with the ground".

Universe: base event 0hjw400xgjb3j7ay7ynuaqbnpi, status confirmed, 2026-07-15 10:00, location "Mesa Vista, Unit 4C", description "Final make-ready QC inspection on Mesa Vista Unit 4C after interior repaint and deep clean; confirm the unit is rent-ready and release it to leasing." The unit is not cleared for leasing; the clearance step is still ahead. A second confirmed future event, j3ulusavtqgvwge31s21ep5c8w on 2026-07-08, is a "Mesa Vista HOA Management Review". Neither appears anywhere in the file.

Of the nine confirmed events on or after 2026-07-01, the file reconciles one (42b119cbt7xd0vnhw6dwvdqizo). Two more sit on a property inside the graded scope.

### Issue 7 (MODERATE, check 7). OE 13 asserts QuickBooks findings with no QuickBooks tool call, and invoice 110274597983 is never retrieved by any step.

OE 13 reads two invoices and their line items without naming a tool. The first QuickBooks call in the file is at OE 22. Worse, the decoy invoice 110274597983 carries CustomerRef "Simone Okafor" and contains no occurrence of "Harris", so `search_invoices` with query "Harris" at OE 24 cannot return it, and no other step queries for it. The comparison OE 13 rests on is unreachable.

### Issue 8 (MODERATE, check 7). The two Ridgeview calendar events that justify the graded correction of rec8b679d92f30753 are unreachable.

OE 19 relies on `whd6zys0hw7zbsh11m9vqv4m4i` (2026-06-08) and `42b119cbt7xd0vnhw6dwvdqizo` (2026-07-13). Verified: neither sits on lisa.smith@starpm.com, so OE 27 does not return them; neither contains the string "Portfolio Review", so OE 28's `fullText` filter does not return them; OE 29 calls `get_event` on a specific Finley row id. No step in the file retrieves either event, yet one of the three graded corrections in OE 30 depends on them.

### Issue 9 (MODERATE, check 7). OE 18 cites a Gmail message no step retrieves.

Gmail 2ae48555b3009a95 carries the subject "Eviction Filing Authorization. Tanya Mitchell. Unit 14" and its body contains neither "collections" nor "past due", the two queries OE 21 offers. OE 18 names no Gmail tool of its own. The record that establishes the contested ownership ruling is not shown to be reachable.

### Issue 10 (MODERATE, check 1). OE 33 directs the email to assert a cleared late payment that does not exist.

Claim: "the cleared late payment is a Sunset Ridge tenant rather than a Mesa Vista one".

Universe: the only past-due tenant near either owner is Tanya Mitchell, and her balance was never cleared. It ran first notice on June 6, payment plan June 11, missed installment June 23, breach June 25, three-day notice June 26, cure deadline expired June 29 with no payment. The correct correction is that no cleared late payment exists for either portfolio, not that it belongs to a different property. As written this becomes a graded criterion asserting a universe fact that is false.

## Minor observations (not blocking, listed for the revision pass)

- OE 30 justifies excluding the 207A and 4C rows from the graded set on the ground that "each of those unit strings matches several rows, so no criterion can pin one without becoming ambiguous". Sunset Ridge 104B matches two rows and Sunset Ridge 309C matches four, and both are in the graded set. The real distinction is that the graded rows are pinned by record id. The sentence as written will mislead S3.
- OE 26 states a conclusion with no tool call. It aggregates OE 23 and OE 25 and adds no new retrieval, which is acceptable as synthesis, but it is the only step of the 36 with no tool anywhere in it.
- OE 20 concludes that nothing supports Lisa's water heater attribution without noting that two OPS-100 comments do narratively place a water heater repair in Robert Finley's May report (comment_5a6d779a715f587392dd00b9c8dbbd4a, "the water heater subfloor repair called out as a pass-through", and comment_b575411ba2be5ceaa0ab28094905f844, "On the water heater flooring repair"). The records still resolve to 412 Mesquite, so the finding holds, but the counter-evidence should be named rather than left for an agent to trip over.
- OE 21 states flatly that Tanya Mitchell's unit "is Sunset Ridge Unit 14". The universe carries seven make-ready rows for her or for a bare "Unit 14", including "Rio Bend - Unit 14", "Unit 14 - Tanya Mitchell Eviction" and two rows titled only "Unit 14". OE 13 correctly warns that the bare string collides across properties; OE 21 then relies on the collision-prone attribution without the qualification.

## Exact replacement wording

### Replacement 1: OE 13, first half. Replace from "QuickBooks invoice 113714702211" through "rather than only the unit this invoice happens to name."

> Harry Harris's property has to be established from outside Airtable, because the make-ready table carries no owner field. Three records place him on Sunset Ridge, and all three run through the same unit. Linear OPS-32 "Eviction Hearing - Mitchell, Harris Property" describes "the Tanya Mitchell eviction case at one of Harry Harris's units". Calendar event nuh928ma4rwhwf1bnap30rmfli "Mitchell Eviction Court Hearing" describes "JP court hearing for the Mitchell eviction at the Harris property". Airtable row reca8230a8fd9ff51 puts Tanya Mitchell on fldUnit "Sunset Ridge Unit 14". Search QuickBooks using search_invoices with query "Harris" and open the results with read_invoice: invoice 113714702211 (DocNumber 4422, CustomerRef Harry Harris) bills him for "Lease document scanning and filing fee - Unit 14, Sunset Ridge Apartments, October 2026", which is the fourth record on the same chain. That is the weight of evidence for the cluster, and it is not clean. Invoice 110274597983 (DocNumber 4418, $325.00) bills Simone Okafor for the same unit on the same TxnDate 2026-05-13 and the same DueDate 2026-06-12, and Gmail 2ae48555b3009a95 has Brooke Phillips asking linda.castillo@gmail.com, not Harris, for written owner authorization to evict the tenant in that unit. The line item does not break the tie either: ItemRef "Monthly Management Fee" appears on Okafor's own rows, on Tanya Mitchell's and on Connor Beaumont's, while Robert Finley, the confirmed owner of the other portfolio, carries none of it at all. Harris's other QuickBooks rows name five further properties, Palomar Gardens on 317923399822, Fernwood Gardens on 879979204592, Maple Ridge Building 2 on 390637322875, 4402 Larkspur Ave on 120329707702 and 233 Elmsworth Blvd on 262820673328, so no single row establishes a portfolio. The Sunset Ridge cluster is treated as Harris's on the strength of OPS-32, the hearing event and invoice 4422 together, and the Castillo authorization request is the reason the two Unit 14 delinquency records stay out of the graded set at OE 18 rather than a reason to drop the cluster.

### Replacement 2: OE 15, third sentence. Replace "This is the only item in either cluster that is both unresolved and untracked: the turn scope cannot be set until someone assesses the subfloor, and the assessment exists nowhere except this row's fldNotes2."

> The turn scope cannot be set until someone assesses the subfloor, and the assessment exists nowhere except this row's fldNotes2. Two items in the clusters are unresolved and carried nowhere. This is one. The other is reca06d89f1a4ac5b on Sunset Ridge 309C, whose fldNotes2 waits on a final utility transfer confirmation that appears in no other row in the universe. The subfloor item is the one to raise, because it blocks a turn scope outright while the 309C row's siblings show that unit's vendor work already booked for July 21 and July 22, but an agent that raises the 309C blocker instead has picked a defensible target and must not be marked down for it.

### Replacement 3: OE 30, the exclusion sentence. Replace "reca8230a8fd9ff51 (Sunset Ridge Unit 14) is conditional on the balance remaining unresolved and the unit becoming vacant, neither of which has happened."

> reca8230a8fd9ff51 (Sunset Ridge Unit 14) is conditional on two things together, the balance remaining unresolved and the unit becoming vacant. The balance limb has been met, because rec8005502043b755 records the payment plan breached on June 23, rec3782834f35df50 records that the tenant did not cure before the June 29 deadline, and Gmail 2ae48555b3009a95 confirms the cure deadline expired with no payment. The vacancy limb has not, and possession has not been returned, so the turn is still contingent. It stays out of the graded set on that ground and on the contested ownership described at OE 18, and an agent that leaves it alone and an agent that advances it are both acceptable.

### Replacement 4: OE 30, the 207A and 4C sentence. Replace "Mesa Vista 207A and Mesa Vista 4C each carry selProg rows alongside a selReady row stating the unit is finished and cleared for leasing, so those rows are also out of step with the ground. They sit outside the graded correction set for a different reason: each of those unit strings matches several rows, so no criterion can pin one without becoming ambiguous."

> Mesa Vista 207A and Mesa Vista 4C each carry selProg rows alongside a selReady row stating the unit is finished and cleared for leasing. Those pairs are not graded, and the reason is that the calendar contradicts the selReady reading rather than the selProg one. A confirmed event 0hjw400xgjb3j7ay7ynuaqbnpi sits on 2026-07-15 at "Mesa Vista, Unit 4C" as a "Final make-ready QC inspection ... confirm the unit is rent-ready and release it to leasing", which is work still ahead of universe today, so 4C is not finished and neither row on it can be called settled. 207A is left alone alongside it for consistency.

### Replacement 5: OE 33, the correction list. Replace "and the cleared late payment is a Sunset Ridge tenant rather than a Mesa Vista one."

> and no cleared late payment exists for either portfolio: the only past-due tenant anywhere near these owners is Tanya Mitchell, whose balance was never cleared but ran from first notice on June 6 through a breached payment plan on June 25 to a cure deadline that expired on June 29 with no payment.

### Replacement 6: OE 19, add a retrieval sentence after "Finley therefore carries two properties, Mesa Vista and Ridgeview, and the Ridgeview roof is the counterpart to the open ticket in OE 18."

> Reach the calendar side of this with list_events using fullText "Ridgeview" across brooke.phillips@starpm.com, teresa.wood@starpm.com and john.smith@starpm.com, and confirm each hit with get_event. Neither Ridgeview event sits on Lisa's own calendar and neither carries the words "Portfolio Review", so the persona-scoped read at OE 27 and the titled search at OE 28 both miss them.

### Replacement 7: OE 18, add a retrieval sentence before "Ownership of that unit is contested in the universe and must not be asserted".

> Reach the correspondence with search_threads using query "eviction" or "authorization" and open the result with get_thread, decoding payload.body.data.

### Replacement 8: OE 20, add after "so the finding is that nothing supports Lisa's attribution rather than that the universe proves a negative."

> Two OPS-100 comments do repeat the attribution in prose, comment_5a6d779a715f587392dd00b9c8dbbd4a calling out "the water heater subfloor repair" as a pass-through in Robert's May report and comment_b575411ba2be5ceaa0ab28094905f844 answering his question on "the water heater flooring repair". Both are narrative restatements of Lisa's own claim, and no ticket, invoice or make-ready row places any water heater work on a Finley property.

### Replacement 9: OE 21, the Mitchell attribution. Replace "belongs to Tanya Mitchell, whose unit is Sunset Ridge Unit 14 (reca8230a8fd9ff51), not Mesa Vista."

> belongs to Tanya Mitchell. Her unit is recorded seven ways in tblMakeReady, as "Sunset Ridge Unit 14" on reca8230a8fd9ff51, as bare "Unit 14" on rec91517a5acab558 and recc83c05d889b354, as "Unit 14 - Tanya Mitchell Eviction" on receee45491536859, and as two tenant-named rows, alongside an unrelated "Rio Bend - Unit 14" on rec94e86a3007dd5e. Only reca8230a8fd9ff51 qualifies the unit by property, and none of them is Mesa Vista.

### Replacement 10: OE 35, the uniqueness justification. Replace "It is the correct target because the prompt asks for an item so the work does not quietly disappear at hand-off, and the subfloor assessment is the only open item in either cluster that is carried nowhere: MT-2026-047 already exists as a ticket and the Ridgeview follow-up already has a booked walk-through, so neither of those needs a new item to survive."

> The prompt asks for one item so the work does not quietly disappear at hand-off. MT-2026-047 already exists as a ticket and the Ridgeview follow-up already has a booked walk-through on 2026-07-13, so neither of those needs a new item to survive. Two candidates are carried nowhere, the Mesa Vista 310C subfloor assessment and the Sunset Ridge 309C utility transfer confirmation on reca06d89f1a4ac5b. The subfloor assessment is the expected target because it blocks a turn scope outright, and an agent that raises the 309C blocker instead has picked a defensible target and must not be marked down.

## Verdict rationale

The file's spine is sound and independently re-derivable: the three-row correction set is right and correctly directed, every money figure and every identifier is exact, the duplicate Harris review and the stale Finley review are real and correctly characterised, the deliverables map cleanly to the prompt, and the tool surface is clean. Nothing here requires a rebuild and no hardness lever is lost.

What blocks a pass is that three graded conclusions rest on statements the universe contradicts (issues 1, 2, 4, 5, 6 and 10), one scoping decision is circular against a later ruling in the same file (issue 3), and four bodies of evidence the file leans on are not reachable by any step it specifies (issues 7, 8, 9 and part of 5). Under the strict reading each of those is a fail on its own. Every one is repairable by wording, and replacement text is supplied above.

VERDICT: REVISE
