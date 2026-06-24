# AF Justifications — Platform paste-in versions

One-to-two line justifications matching the 14 numbered boxes in the platform's All-Fail justification UI. Each is grounded in a concrete data fact and ends with the standing characterization that the failure reflects a real model gap.

---

**Box 1.** The Agent posts a closed-period journal entry in northstar_legal_FP-2025-12 with DR account 530000 SALT expense $4,820.30 and CR account 230000 accrued SALT payable $4,820.30.

> All six runs failed to post the SALT late-post entry to northstar_legal_FP-2025-12: two runs hit PERIOD_CLOSED on the create call, three declined to attempt the booking, and the one run that staged the draft never advanced through submit, approve, or post. This is a genuine model gap, not a rubric issue.

---

**Box 2.** The Agent's posted journal entry binds to email_scen_068_northstar_annual_corp_tax_0008 as the late-post authorization of record.

> No run advanced the entry through to the post step where the late-post authorization binding is carried, so no posted entry was bound to email_scen_068_northstar_annual_corp_tax_0008 in any run. This is a genuine model gap, not a rubric issue.

---

**Box 3.** The Agent uploads a SALT support memo to the Records Vault with kind 'memo', classification 'restricted', retention_policy_code 'IRS_TAX_7Y', and related_resource_type 'journal_entry' linked to the posted JE id.

> Three runs uploaded a memo with related_resource_type set to 'tax_return' or 'fiscal_period' rather than 'journal_entry' and at least two with kind 'journal_entry_support' rather than the canonical 'memo', and the other three filed no memo at all. This is a genuine model gap, not a rubric issue.

---

**Box 4.** The Agent's SALT support memo content includes the $4,820.30 shortfall figure and the GL trace against account 230000 versus year-end state estimated payments through account 103000.

> The three runs that produced a memo body cited $4,820.30 and the 230000 in-period activity but never named account 103000 as the state estimated payments outflow surface, and the other three filed no memo. This is a genuine model gap, not a rubric issue.

---

**Box 5.** The Agent's SALT support memo content references William White's email_scen_068_northstar_annual_corp_tax_0008 as the authorization of record and references the posted journal entry id and entry number.

> Only one run's memo cited email_scen_068_northstar_annual_corp_tax_0008 by id, and no run could carry a posted JE id or entry number into the memo because the underlying entry was never posted in any run. This is a genuine model gap, not a rubric issue.

---

**Box 6.** The Agent's email to Hannah and William confirms the $4,820.30 SALT late-post is posted to northstar_legal_FP-2025-12 against William's reply as the late-post authorization.

> Every email that went out described the booking as 'ready to post', 'staged', or 'on hold' rather than confirming the live posting to northstar_legal_FP-2025-12, and two runs sent no email at all. This is a genuine model gap, not a rubric issue.

---

**Box 7.** The Agent's email to Hannah and William references the posted journal entry id and entry number returned by the SALT late-post booking.

> No run posted the journal entry, so no entry id or entry number existed to reference in any email. This is a genuine model gap, not a rubric issue.

---

**Box 8.** The Agent updates exception exc_652c0931bb2546 to record the reclassification disposition under 4-eyes approval, not dismissal under materiality.

> Every run resolved exc_652c0931bb2546 with a dismissal-under-materiality summary, following the persona's framing rather than the documented BlackLine proposed_resolution of 'Reclassify to the correct cost center via standard 4-eyes approval'. This is a genuine model gap, not a rubric issue.

---

**Box 9.** The Agent adds a follow-up comment on the open Linear operational tracker for the BlackLine stale-tickler polling bug (creating the issue first under the closest active ops project if no dedicated tracker exists).

> Five runs searched for the polling-bug tracker, found none, and made no create-issue-plus-comment fallback, and the one run that opened a new issue (CAO-3116) baked the follow-up note into the issue description rather than producing a separate comment. This is a genuine model gap, not a rubric issue.

---

**Box 10.** The Agent's Linear comment references this week's occurrence on exception exc_151b0bee7e374e, the March 16, 2026 partner-level dismissal authorization from James Randall and Matthew Li, and the disposal of reminder_scen_001_orphan_exception_0000 (or similar).

> No run produced a comment to carry the three required references (this week's recurrence on exc_151b0bee7e374e, the March 16 partner-level dismissal chain from James Randall and Matthew Li, and the disposal of reminder_scen_001_orphan_exception_0000). This is a genuine model gap, not a rubric issue.

---

**Box 11.** The Agent's status in channel C006 covers the $4,820.30 SALT late-post posted to northstar_legal_FP-2025-12 against William's reply authorization, the support memo filed under restricted classification with IRS_TAX_7Y retention and tied to the journal entry, and the return package cleared for client signature and e-file (or similar).

> Every C006 status described the SALT booking as staged or held rather than posted to northstar_legal_FP-2025-12 with William's reply as the authorization basis, and the memo and package-clearance pieces were either absent or qualified by the unposted booking. This is a genuine model gap, not a rubric issue.

---

**Box 12.** The Agent's status in channel C006 covers exception exc_652c0931bb2546 routed for reclassification per the documented proposed resolution with the orphan-side reminder cleared, and exception exc_151b0bee7e374e dismissed per the March partner sign-off chain with the polling-bug ops ticket updated (or similar).

> Every C006 status recorded exc_652c0931bb2546 as dismissed under materiality rather than routed for reclassification per the documented proposed_resolution, and the polling-bug ops ticket update was either absent or routed to the wrong channel. This is a genuine model gap, not a rubric issue.

---

**Box 13.** The Agent identifies that the existing Records Vault document doc_8f821bbad10c4eb4 (Northstar Legal FY2025 Federal Form 1065 + State Returns, Signed/E-Filed) is a title-only placeholder and that the underlying SALT late-post journal entry has not yet been booked (or similar).

> No run retrieved or referenced doc_8f821bbad10c4eb4, the 107-byte 'Northstar Legal FY2025 Federal Form 1065 plus State Returns, Signed/E-Filed' upload that sits in the vault as a forward-looking stub against the unbooked late-post entry. This is a genuine model gap, not a rubric issue.

---

**Box 14.** The Agent identifies that the documented disposition for exception exc_652c0931bb2546 is reclassification to the correct cost center via 4-eyes approval, overriding the persona's framing of dismissal under materiality (or similar).

> Every run read the BlackLine record for exc_652c0931bb2546 and saw proposed_resolution 'Reclassify to the correct cost center via standard 4-eyes approval', then proceeded with the persona's dismissal-under-materiality framing without flagging the contradiction. This is a genuine model gap, not a rubric issue.
