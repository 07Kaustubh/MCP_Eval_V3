# Validator report: submission_gate

**Status:** FAIL  
**Fails:** 6 · **Warns:** 0 · **Notes:** 2

## FAIL
- [Eval5 P6 6.1b NON_ATOMIC_ENUM] rubric #11 enumerates ~3 items in one criterion under a completeness/step predicate - split into one rubric per item (the Airtable write was correctly split into 3; apply the same rule to the rest)
- [Eval5 P6 6.1b NON_ATOMIC_ENUM] rubric #15 enumerates ~5 items in one criterion under a completeness/step predicate - split into one rubric per item (the Airtable write was correctly split into 3; apply the same rule to the rest)
- [Eval5 P7 AMBIGUOUS_TARGET] rubric #2 pins record receb057b02f20052 but 3 records in tblMakeReady share entity 'Las Palmas 8D' and the prompt names none of them - a reasonable agent may write a sibling row and wrongly fail. Name the record in the prompt, or accept any matching record.
- [Eval5 P7 AMBIGUOUS_TARGET] rubric #3 pins record receb057b02f20052 but 3 records in tblMakeReady share entity 'Las Palmas 8D' and the prompt names none of them - a reasonable agent may write a sibling row and wrongly fail. Name the record in the prompt, or accept any matching record.
- [Eval5 P7 AMBIGUOUS_TARGET] rubric #4 pins record receb057b02f20052 but 3 records in tblMakeReady share entity 'Las Palmas 8D' and the prompt names none of them - a reasonable agent may write a sibling row and wrongly fail. Name the record in the prompt, or accept any matching record.
- [Eval5 P7 UNRECONCILED_FUTURE_EVT] confirmed calendar event 'Vendor Walk-Through - A Plus Carpet, Las Palmas 8D' dated 2026-07-07 references task entity 'Las Palmas 8D' but no Oracle Event cites that date - a future confirmed event is open work. Sweep every service (incl. Calendar) before asserting completeness / 'only open item'.

## NOTE
- [Eval5 P7] rubric census: 15 outcome / 0 process / 15 total
- [Eval5 P6] COUNCIL: under-strictness (6.3), exclusion coverage (6.6), UGT convergence (6.8), OE authority (6.9), strict feasibility (6.10), date-alignment ambiguity (6.11) require semantic judgment - flagged for council review
