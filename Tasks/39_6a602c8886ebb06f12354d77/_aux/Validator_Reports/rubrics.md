# Validator report: rubrics

**Status:** FAIL  
**Fails:** 6 · **Warns:** 0 · **Notes:** 5

## FAIL
- [Eval5 P6 6.1b NON_ATOMIC_ENUM] rubric #11 enumerates ~3 items in one criterion under a completeness/step predicate - split into one rubric per item (the Airtable write was correctly split into 3; apply the same rule to the rest)
- [Eval5 P6 6.1b NON_ATOMIC_ENUM] rubric #15 enumerates ~5 items in one criterion under a completeness/step predicate - split into one rubric per item (the Airtable write was correctly split into 3; apply the same rule to the rest)
- [Eval5 P7 AMBIGUOUS_TARGET] rubric #2 pins record receb057b02f20052 but 3 records in tblMakeReady share entity 'Las Palmas 8D' and the prompt names none of them - a reasonable agent may write a sibling row and wrongly fail. Name the record in the prompt, or accept any matching record.
- [Eval5 P7 AMBIGUOUS_TARGET] rubric #3 pins record receb057b02f20052 but 3 records in tblMakeReady share entity 'Las Palmas 8D' and the prompt names none of them - a reasonable agent may write a sibling row and wrongly fail. Name the record in the prompt, or accept any matching record.
- [Eval5 P7 AMBIGUOUS_TARGET] rubric #4 pins record receb057b02f20052 but 3 records in tblMakeReady share entity 'Las Palmas 8D' and the prompt names none of them - a reasonable agent may write a sibling row and wrongly fail. Name the record in the prompt, or accept any matching record.
- [Eval5 P7 UNRECONCILED_FUTURE_EVT] confirmed calendar event 'Vendor Walk-Through - A Plus Carpet, Las Palmas 8D' dated 2026-07-07 references task entity 'Las Palmas 8D' but no Oracle Event cites that date - a future confirmed event is open work. Sweep every service (incl. Calendar) before asserting completeness / 'only open item'.

## NOTE
- universe: starpm
- Feasible_Surface loaded: 15 tables with enum maps
- using Fact_Ledger.json for groundedness (403 amounts, 206 emails indexed)
- counts: outcome=15, process=0
- Overall Rubric Quality: 0/15 (0%) with Major, 0/15 (0%) with Moderate+ , 0/15 (0%) with any issue
