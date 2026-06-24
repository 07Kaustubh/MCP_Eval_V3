# S2 OE Solvability Report — Task 26_6a390e724c34487b95645dcc

## OE-to-prompt coverage map

Forward (every prompt sentence -> at least one OE step):

| Prompt sentence / clause | OE step |
|---|---|
| "Hannah just messaged that William cleared the Step 3 partner package for the Northstar Legal FY2025 return last night, including the state-and-local accrual piece" | OE1 + OE2 + OE3 |
| "I want to get this actually put to bed before the partner signature comes back" / "the e-file path shouldn't be sitting behind accrual housekeeping" | OE7 + OE9 + OE17 |
| "The federal return and the state returns both tie cleanly to the trial balance we locked in our December period for Northstar" | OE4 + OE5 |
| "The thing still hanging was the SALT shortfall that surfaced in review when Hannah re-tested the provision against year-end estimated payments" | OE3 + OE5 |
| "William's reply is the authorization of record we needed for a closed-period booking" | OE2 |
| "Before staging anything I want the shortfall traced back through our own records on the Northstar side so the number we book is one we can ourselves stand behind, not one we copied off the messaging trail" | OE5 (Lever 2 enforcement) |
| "Once you have a figure the records support, stage the closed-period entry on the Northstar December period and bind it back to William's reply as the authorization basis" | OE7 (late_post_authorization_id = email_scen_068_northstar_annual_corp_tax_0008) |
| "File a short support memo to the vault under the restricted classification with our long tax-return retention, tied to the entry so the audit trail is clean" | OE8 (kind=memo, classification=restricted, retention_policy_code=IRS_TAX_7Y, related_resource_id=staged JE) |
| "Then ping Hannah and William so they know the booking is live and the package can move to the client for signature" | OE9 |
| "The May timing recon I sent Daniel for sign-off on June 1 went past its deadline without a response coming back" | OE10 + OE11 |
| "Jones and I had landed on dismissing under materiality. I want that actually pushed through and the exception closed out this morning" | OE12 (with Lever 9 override -- reclass per proposed_resolution, not dismiss) |
| "The older one is the stale tickler that keeps firing on the Brookfield intercompany variance from last summer. That item closed in August" | OE13 |
| "I had partner-level confirmation back in March that the reminder was fine to dismiss, with a side note about the underlying polling bug behind these stale ticklers" | OE14 |
| "Please clear the reminder so it stops pinging me" | OE15 |
| "add a quick follow-up note on the open ops ticket for that polling bug so the running record reflects what is happening this week" | OE16 (find-or-create) |
| "Then drop a confirmation in the tax channel so Hannah and the team know the FY2025 close is moving and my exception backlog is clear" | OE17 |

Reverse (every OE step -> at least one prompt clause): all 17 OEs trace back. Zero scope creep.

## OE-to-rubric mapping preview (for S3)

| OE step | Rubric type | Notes |
|---|---|---|
| OE1, OE3 | Read / lookup | No rubric. Downstream Outcome rubrics prove the read happened. |
| OE2 | Read / lookup + load-bearing fact | Surfaces the late_post_authorization_id binding consumed by OE7. |
| OE4 | Read / lookup | Anchors the closed-period status the late-post requires. |
| OE5 | Read / lookup with Lever 2 enforcement | Likely no rubric, but its conclusion (figure stands at $4,820.30 only after GL trace) feeds OE7's amount. |
| OE6 | Read / lookup with Lever 10 (L25 anchor) recognition | No direct rubric, but its conclusion (proceed to stage despite Signed/E-Filed stub) feeds OE7. |
| OE7 | Outcome 1.1 (write) + Outcome 1.2 (content) | The closed-period JE is the central write. JE has DR 530000 $4,820.30, CR 230000 $4,820.30, late_post_authorization_id "email_scen_068_northstar_annual_corp_tax_0008", entity_id "northstar_legal", period_id "northstar_legal_FP-2025-12", and posted lifecycle. |
| OE8 | Outcome 1.1 (write) + Outcome 1.2 (content) | Vault memo upload. Content requirements: kind=memo, classification=restricted, retention_policy_code=IRS_TAX_7Y, related_resource_type=journal_entry, related_resource_id=staged JE id. |
| OE9 | Outcome 1.1 (write) + Outcome 1.2 (content) | Audit-trail email to Hannah cc William. Body must reference the booked figure, the staged JE id, William's reply as authorization basis, the vault memo doc id, and clearance of the return package + e-file path. |
| OE10, OE11 | Read / lookup with Lever 9 enforcement | OE10 surfaces the proposed_resolution=Reclassify that overrides the persona-relayed dismiss framing; OE11 confirms the missing Daniel reply. |
| OE12 | Outcome 1.1 (write) | BlackLine exception exc_652c0931bb2546 routed for reclassification per proposed_resolution, paired with reminder_delete on reminder_scen_012_orphan_exception_0000. |
| OE13, OE14 | Read / lookup | OE13 confirms exc_151b0bee7e374e is already closed; OE14 retrieves the James Randall + Matthew Li dismissal authorization chain (two replies deep in scen_001). |
| OE15 | Outcome 1.1 (write) | reminder_delete_reminder on reminder_scen_001_orphan_exception_0000 (the orphan stale-tickler). |
| OE16 | Outcome 1.1 (write) | Linear comment (or new issue + comment) on the polling-bug ops ticket per Matthew Li's escalation ask. Find-or-create allowance encoded. |
| OE17 | Outcome 1.1 (write) + Outcome 1.2 (content) | Slack post in C006 #tax-prep-and-filings. Payload must cover: SALT JE posted, vault memo filed, return package cleared, exc_652c0931bb2546 reclassified, exc_151b0bee7e374e stale tickler dismissed with polling-bug ticket updated. |

Expected rubric count: 5 to 7 Outcome 1.1 rubrics (one per write surface in OE7, OE8, OE9, OE12, OE15, OE16, OE17), 3 to 4 Outcome 1.2 content rubrics (OE7 JE binding, OE8 vault metadata, OE9 email body, OE17 slack payload), zero Outcome 2.1 (no facts the user asked to be told directly), zero Process rubrics (no ordering constraint that an Outcome cannot verify).

## Verdicts

| Gate | Verdict |
|---|---|
| Validator (validate.py --phase oe) | PASS (0 fails, 0 warns, 1 note) |
| Council A (Grounding + Convention) | GO -- zero ungrounded claims, zero convention drift |
| Council B (Adversarial QC + Density + Hardness) | GO -- all QC sub-dims at 5, density 42 to 60 midpoint ~51, all 5 levers triggered, no phrasing hits, no PROPAGATE TO S1 |
| Strict veteran AUDIT (oracle, 5 lenses) | PASS (STRICT) -- 0 BLOCKERs, all 5 levers trace prompt sentence to OE step to Fact_Ledger atom with cited evidence |

## Density summary

Hardness Plan midpoint 52. Council B projection 42 to 60 with midpoint ~51. AUDIT hyper-strict floor ~36; realistic-strict midpoint ~46 to 48. Sits above the 40 floor on every reading and comfortably at the 50 comfort midpoint on the realistic Council B projection. Real Opus 4.8 trajectories will run higher once natural validation hops layer in.

## Hardness lever preservation (end-to-end traceability)

| Lever | Prompt sentence | OE step | Fact_Ledger atom |
|---|---|---|---|
| L1 Latching | "Hannah just messaged that William cleared the Step 3 partner package" | OE1, OE2, OE3 | slack ts 1781013600.100000; emails _0006 + _0008 |
| L2 Structured-DB skip | "Before staging anything I want the shortfall traced back through our own records" | OE5 | account 230000 northstar in-period activity (zero SALT JE); account 103000 cash tax reserve outflows |
| L8 Multi-link chain | "Once you have a figure the records support, stage the closed-period entry ... bind it back to William's reply ... File a short support memo ... ping Hannah and William" | OE1 to OE9 (4 hop chain: anchor read -> GL trace -> JE stage -> vault memo + email) | slack ts 1781119800.200000; email_scen_068_northstar_annual_corp_tax_0008; account 230000; doc id of vault memo tied to JE id |
| L9 Universe-grounded gotcha | "Jones and I had landed on dismissing under materiality. I want that actually pushed through" | OE10, OE12 (override persona framing with BlackLine proposed_resolution=Reclassify) | exc_652c0931bb2546.proposed_resolution string |
| L10 Reversal/supersession via L25 anchor | (Deliberate omission of the Signed/E-Filed stub from the prompt) | OE6 (discover doc_8f821bbad10c4eb4, recognize 107-byte placeholder, proceed to stage JE) | doc_8f821bbad10c4eb4 metadata (107 bytes, restricted, uploaded 2026-06-12 09:30 by persona_027) |

## Notes for downstream S3

- Encode the JE late_post_authorization_id binding (= email_scen_068_northstar_annual_corp_tax_0008) at the Outcome 1.2 level for OE7.
- Encode the kind=memo + classification=restricted + retention_policy_code=IRS_TAX_7Y + related_resource binding at the Outcome 1.2 level for OE8.
- Encode the BlackLine disposition = reclassify (per proposed_resolution) NOT dismiss (per persona) at the Outcome 1.2 level for OE12.
- For OE16, allow find-or-create at the Outcome 1.1 level: either linear_create_comment on an existing polling-bug ticket OR linear_create_issue + linear_create_comment under the closest active ops project. Universe has no exact polling-bug ticket.
- Account 530000 (chart name "Court Filing & Expert Witness Costs") is named "SALT expense" in William's authorization. Rubric must follow William's binding as the universe's only northstar SALT mapping. Do NOT add a rubric requiring the agent to flag the account-name mismatch. The OE faithfully relays William's authorization; rubrics must match.
- 7 write surfaces (OE7, OE8, OE9, OE12, OE15, OE16, OE17) implies up to 7 Outcome 1.1 rubrics. Default to zero Process rubrics unless a strict ordering constraint emerges that no Outcome can verify.
