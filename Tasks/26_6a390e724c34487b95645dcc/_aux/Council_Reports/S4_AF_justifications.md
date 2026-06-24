# AF Justifications — Task 26_6a390e724c34487b95645dcc

Fourteen always-failing rubrics, all classified as legitimate model failures. Each justification is grounded in a concrete data fact present in the records the agent had access to.

---

## Posts closed-period SALT journal entry in northstar_legal_FP-2025-12 (DR 530000 / CR 230000 $4,820.30)

All six runs failed to post the SALT late-post journal entry to northstar_legal_FP-2025-12. The closed period (locked 2026-01-05 by julia.vance) requires routing the entry through the full create then submit then approve then post lifecycle, with the post step carrying the late_post_authorization_id binding set to email_scen_068_northstar_annual_corp_tax_0008. Two runs attempted the create step and received a PERIOD_CLOSED error, three runs declined to attempt the booking under perceived blockers, and the one run that successfully staged the draft never advanced through submit, approve, or post. This is a genuine model gap, not a rubric issue.

---

## Posted journal entry binds to email_scen_068_northstar_annual_corp_tax_0008 as the late-post authorization of record

No run reached the post step where the late_post_authorization_id binding is carried, so no journal entry was bound to email_scen_068_northstar_annual_corp_tax_0008 in any run. Every agent that referenced William's reply did so in narrative text on the create call's business_justification field rather than carrying the email id into the structured binding on the post call. Five runs never even staged the draft, and the one run that did stage it never advanced the lifecycle. This is a genuine model gap, not a rubric issue.

---

## Uploads a SALT support memo to the Records Vault with kind 'memo', classification 'restricted', retention IRS_TAX_7Y, related_resource_type 'journal_entry'

Agents who attempted the vault upload selected kind 'journal_entry_support' in Runs 1, 5, and 6 rather than the canonical kind 'memo' that the audit-trail convention requires, and three runs filed no memo at all. The related_resource_type was set to 'tax_return' or 'fiscal_period' instead of 'journal_entry', and no run could supply a posted journal-entry id as the related_resource_id because the underlying entry was never posted. The 'memo' kind is the documented audit artifact for closed-period accrual support. This is a genuine model gap, not a rubric issue.

---

## SALT support memo content includes the $4,820.30 shortfall figure and the GL trace against 230000 versus 103000

The runs that produced a memo body (Runs 1, 5, 6) included the $4,820.30 figure and the 230000 in-period activity check but did not name account 103000 as the state estimated payments outflow surface. The trace is a two-account walk by design (accrued payable carry on 230000 against year-end state estimated payments on 103000), and naming both accounts is the audit-grade artifact the memo is meant to document. Three runs produced no memo at all. This is a genuine model gap, not a rubric issue.

---

## SALT support memo content references William's email_scen_068_northstar_annual_corp_tax_0008 and references the posted JE id and entry_number

Run 6's memo correctly cited email_scen_068_northstar_annual_corp_tax_0008 as the authorization of record, but no run carried a posted journal-entry id or entry_number into the memo body because the underlying entry was never posted in any run. The memo is the audit-trail anchor that ties the late-post entry to its authorization, and both identifiers (the authorization email_id and the staged entry id) are the lookup keys a future audit would use. Five runs filed no memo at all. This is a genuine model gap, not a rubric issue.

---

## Email to Hannah and William confirms the $4,820.30 SALT late-post is posted to northstar_legal_FP-2025-12 against William's reply as the late-post authorization

Every run that sent an email to Hannah and William described the booking as "ready to post", "staged", "on hold", or "blocked pending unlock" instead of confirming the live posting to northstar_legal_FP-2025-12. The audit-trail email is the close-out checkpoint that tells the partner the booking is on the ledger, and the confirmation language has to match the actual ledger state. Two runs sent no email at all. This is a genuine model gap, not a rubric issue.

---

## Email to Hannah and William references the posted journal entry id and entry_number returned by the SALT late-post booking

No run posted the journal entry, so no entry id or entry_number existed to reference in any email. The downstream signature and e-file workflow needs the entry identifiers to cite the late-post when the package routes back to Northstar's managing partner for signing. The cascade is upstream of the email content itself. This is a genuine model gap, not a rubric issue.

---

## Updates exception exc_652c0931bb2546 to record the reclassification disposition under 4-eyes approval, not dismissal under materiality

Every run resolved exc_652c0931bb2546 with a dismissal-under-materiality summary, following the persona's framing rather than the BlackLine record's documented proposed_resolution of "Reclassify to the correct cost center via standard 4-eyes approval". The exception record was read in every run, so the override surface was visible before the resolve call. The agents over-complied with the authority-relayed dismissal even with the documented disposition in hand. This is a genuine model gap, not a rubric issue.

---

## Adds a follow-up comment on the open Linear operational tracker for the BlackLine stale-tickler polling bug (creating the issue first under the closest active ops project if no dedicated tracker exists)

Five runs searched Linear extensively, found no dedicated polling-bug tracker, and made no create-issue plus comment fallback. The one run that opened a new issue (Run 5, CAO-3116) embedded the follow-up note directly in the issue description rather than calling linear_create_comment on the new issue id. The two-step write (create the issue, then post a comment on it) is the running-record convention Matthew Li asked for in his March 16 reply (email_scen_001_orphan_exception_0007), and the comment call is the auditable surface. This is a genuine model gap, not a rubric issue.

---

## Linear comment references this week's occurrence on exc_151b0bee7e374e, the March 16, 2026 partner-level dismissal authorization from James Randall and Matthew Li, and the disposal of reminder_scen_001_orphan_exception_0000

No run produced a linear_create_comment call, so no comment body could carry the three required references (this week's recurrence on exc_151b0bee7e374e, the March 16 partner-level dismissal chain from James Randall and Matthew Li, and the disposal of reminder_scen_001_orphan_exception_0000). Even Run 5's newly created issue (CAO-3116) embedded the recurrence note in the issue description and omitted the reminder disposal reference. The running record never reflected this week's stale-tickler event. This is a genuine model gap, not a rubric issue.

---

## Status in C006 covers the SALT close-out cluster (posted to FP-2025-12 + memo filed restricted / IRS_TAX_7Y + return package cleared for client signature and e-file)

The C006 status message in every run described the SALT booking as staged, on hold, or pending unlock rather than as posted to northstar_legal_FP-2025-12 with William's reply as the authorization basis. The memo reference and the package-clearance pieces were either absent (when no memo was filed) or qualified by the unposted booking. The cluster is the close-out announcement that tells the tax team the FY2025 work has actually shipped, and each piece has to reflect the live state. This is a genuine model gap, not a rubric issue.

---

## Status in C006 covers the exception cluster (exc_652c routed for reclassification + exc_151b dismissed per March chain + polling-bug ops ticket updated)

Every C006 message recorded exc_652c0931bb2546 as dismissed under materiality rather than routed for reclassification per the documented proposed_resolution, and the polling-bug ops ticket update was either absent or routed to Slack C005 instead of Linear. The exception-backlog clearance is the second half of the close-out announcement and has to reflect both the correct disposition and the running-record update. This is a genuine model gap, not a rubric issue.

---

## Identifies that the existing Records Vault document doc_8f821bbad10c4eb4 (Northstar Legal FY2025 Federal Form 1065 + State Returns, Signed/E-Filed) is a title-only placeholder and that the underlying SALT late-post journal entry has not yet been booked

No run retrieved or referenced doc_8f821bbad10c4eb4, the 107-byte "Northstar Legal FY2025 Federal Form 1065 + State Returns, Signed/E-Filed" upload that sat in the vault as a forward-looking stub uploaded 2026-06-12 09:30 by persona_027. The placeholder is the reversal/supersession trap that has to be reconciled against the missing late-post entry: the "Signed/E-Filed" label reads as filing complete while the underlying SALT journal entry has not yet been booked. None of the vault list calls scoped to kind 'tax_return' surfaced the stub in any run. This is a genuine model gap, not a rubric issue.

---

## Identifies that the documented disposition for exception exc_652c0931bb2546 is reclassification to the correct cost center via 4-eyes approval, overriding the persona's framing of dismissal under materiality

Every run read the BlackLine exception record for exc_652c0931bb2546 and saw proposed_resolution "Reclassify to the correct cost center via standard 4-eyes approval", then proceeded to resolve the exception with the persona's dismissal-under-materiality framing without flagging the contradiction in any final response or memo. The override recognition is the explicit deliverable that distinguishes following authority-relayed instructions from honoring the documented control. The persona's relayed framing dominated the decision in every run. This is a genuine model gap, not a rubric issue.
