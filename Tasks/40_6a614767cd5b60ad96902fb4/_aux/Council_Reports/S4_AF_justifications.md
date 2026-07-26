# S4 Always-Failing Justifications - Task 40_6a614767cd5b60ad96902fb4 (StarPM V4, per model)

Justifications for the criteria that every completed run failed, tagged by the model each describes.

## [OPUS] Arrears balance of 2,132.00 on bill QR-2026-0441
Across all six runs the email to Brooke carried the wrong arrears figure. Opus never queried the bills ledger in any run and worked only the customer, invoices, and payments. The bill QR-2026-0441 still surfaced in a search result every run, and its 2,132.00 balance was visible in the run 1 and run 3 results, yet every draft reported a reconstructed total near 2,287.50 (May arrears 1,125 plus June rent 975 plus late fees 187.50) or leaned on invoice 7214 at 8,173.44. The one authoritative number the owner review needed was in front of the agent and it still quoted a different total.

## [GEMINI] Arrears balance of 2,132.00 on bill QR-2026-0441
Gemini never opened the bills ledger in any run. It searched invoices and payments, found invoice 7214, and rebuilt a balance from the delinquency notes, landing near 2,287.50, and in one run fell back to the 8,173.44 invoice total. It never reached bill QR-2026-0441, so the authoritative 2,132.00 arrears never entered the email. Rebuilding the figure from the notes yields a different number than the bill carries, and the draft went to the owner review with that wrong total every time.

## [GEMINI] Approved reasonable accommodation (emotional support animal) on record
In every run Gemini pulled the accommodation into its own context and then left it out of the email. It searched the CRM objects and the mail threads for Tanya Mitchell, and the approved emotional support animal accommodation surfaced in the results each run, with the approval thread appearing in five of the six. Even with it in hand, none of the drafts to Brooke raised the accommodation or the fair housing consideration before turnover. Reading the record and then dropping it from the owner review is the real failure.
