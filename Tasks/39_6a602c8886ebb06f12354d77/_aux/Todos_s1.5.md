# S1.5 Todos — Tasks/39_6a602c8886ebb06f12354d77

Linter round 1 — platform AI-helper raised two Class A findings: [Prompt] Persona check + [Prompt] Business alignment check. No similarity (Class B) raised.

- [x] phase_ready --phase s1.5 (all upstream artifacts present)
- [x] Write Todos_s1.5.md (this file) + Reads_s1.5.md
- [x] Detect mode: CB (6_/7_ are empty scaffold placeholders, no candidate content) -> fixes land in 5_Prompt.txt in place
- [x] Classify block: Class A (persona authority/voice + business-function seat)
- [x] Skeptical-first score vs per-task universe (PersonaBrief + Hardness Plan + prior Council A/B): strong grounded counters to the linter claim
- [x] Decide revise vs invalidate -> INVALIDATE both. Persona is a fixed input (reauthor-from-Carlos swaps a given); load-bearing item is James's OWN Cat 4 disposal ticket (OPS-227/MT-2026-1271); all decisions route to lead John Smith; BF finding factually wrong (James authors, John receives). Oracle re-adjudication (~16m) confirmed INVALIDATE on both.
- [x] Revise 5_Prompt.txt -> N/A (invalidate path; prompt left UNCHANGED, still the S1-cleared draft)
- [x] Re-check for issues the helper missed: no new prompt-blocking issue. Surfaced 2 upstream S0 hygiene items (Fact_Ledger.today null; S0 report injection claim) as carry-forward to S2. Named watch-item: #make-ready crew-post = yellow pushback-risk, NOT a defect.
- [x] validate.py --phase prompt -> N/A (prompt unchanged; already clean from S1)
- [x] Council A/B re-grep on flagged dimension -> served by the independent oracle adjudication (persona + business-function)
- [x] AUDIT -> SKIPPED (S1.5 step 8: AUDIT fires only on a prompt revision; this is a justification-only resolution)
- [x] Linter_Justifications.md written as TWO justifications (one per finding: Persona check + Business alignment check) + check_justification.py 0 hits exit 0; Tasks/_meta/Linter_Justifications.md appended
- [x] Linter_Decision.md written
- [x] STOP gate (next: resubmit ORIGINAL prompt + justification to platform; if it clears -> PIPELINE S2)
