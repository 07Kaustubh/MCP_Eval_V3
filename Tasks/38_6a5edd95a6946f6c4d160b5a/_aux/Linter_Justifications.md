# Linter Justifications - Task 38 (6a5edd95)

**Date:** 2026-07-22
Two linter checks returned FALSE against the current Brooke-authored prompt. Each check gets its own self-contained pushback below.

---

## Justification 1 - Persona/scope check (paste into Persona check response)

The prompt is authored by Brooke Phillips (Apartment Property Supervisor), not Denise Morales. `2_Persona.txt` and the persona brief on file both name Brooke; the prompt voice, scope, and asks all reflect her seat. I think this check was scored against an earlier version of the submission.

Every scope complaint resolves cleanly against Brooke's actual work. Her recurring lane covers cross-portfolio ops sync, vendor invoice approval, budget oversight, owner reporting, and the CapEx approval flow with owners. The mid-year owner portfolio review scenario has her working directly with Aurora Winona, and there are 22 calendar events where they both appear. A brief for Aurora combining an active maintenance ticket, an owner-billing reconciliation, and a resident escalation is on-brand for her.

The Ridgeview roof piece is squarely hers. The $8,400 approved scope with Robert is the Ridgeview Roof Section Repair authorization from owner Robert Finley, with Pete Donovan confirmed as the vendor. Owner exposure on a CapEx roof job is exactly what a portfolio supervisor carries into an owner-facing update.

The Tony Reyes reference is also fine. Tony is an internal maintenance tech at tony.reyes@starpm.com, active in the #maintenance channel and the on-site tech who filed the initial dirty-filter note on MT-2026-063 for Sunset Ridge Unit 208B. Referencing his Slack post as the current-status baseline Brooke needs to verify is how tickets actually get worked here.

Happy to revise if you can point me at a specific record that says otherwise.

---

## Justification 2 - Business-alignment check (paste into Business alignment response)

I checked each flag against the actual records and the universe data disagrees with the check.

Sunset Ridge is a managed property with multiple ticketed units. The Airtable maintenance record MT-2026-063 in tblMaintenanceTickets covers Sunset Ridge Unit 208B, currently open, with Tony Reyes' on-site dirty-filter note as the description. Sunset Ridge Units 208B, 309C, 104B, and Unit 14 all appear across Airtable records, Slack #maintenance threads, calendar events, and the Gmail thread with Alamo HVAC. Tanya Mitchell's payment plan and late-rent records are keyed to Sunset Ridge Unit 14.

Tony Reyes is on staff at Star PM, not an NPC at a sister property. His Slack handle is tony.reyes and his address is tony.reyes@starpm.com, present in the internal Slack user list and the contacts book. He posts in #maintenance and closes tickets, and he is the tech who wrote the on-site note on MT-2026-063.

"Her make-ready record" for Tanya Mitchell reads unambiguously against the data. Airtable holds multiple records keyed on her as the subject: the fldunit values include "tanya mitchell - eviction track", "tanya mitchell - delinquency escalation", "unit 14 - tanya mitchell eviction", plus the Sunset Ridge Unit 14 and Unit 4B entries. The prompt also asks the agent to confirm the unit reference on that record, which forces the disambiguation explicitly.

MT-2026-063 and MT-2026-047 are both real records in tblMaintenanceTickets. The description on MT-2026-063 still carries Tony's early dirty-filter guess, which the follow-up inspection contradicts (the actual finding is compressor failure). "Update the maintenance record with the current status" is natural language for correcting the description to match what was actually found; the record target is unambiguous and the field choice is routine agent judgment.

On the scope questions: the prompt is authored by Brooke Phillips, the portfolio-level supervisor. Cross-portfolio ops sync, vendor invoice approval, budget oversight, owner reporting, and the CapEx approval flow with owners are all her canonical work. The owner-portfolio-review scenario has her coordinating with Aurora Winona directly, and there are 22 calendar events pairing them. The Ridgeview roof billing reconciliation and the Aurora Gmail are both on-brand for her seat.

Happy to revise any of these if you can point me at a specific record that says otherwise.
