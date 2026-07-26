# Validator report: submission_gate

**Status:** FAIL  
**Fails:** 1 · **Warns:** 0 · **Notes:** 4

## FAIL
- [Eval5 P7 AMBIGUOUS_TARGET] rubric #1 pins record recc83c05d889b354 but 5 records in tblMakeReady share entity 'Unit 14' and the prompt names none of them - a reasonable agent may write a sibling row and wrongly fail. Name the record in the prompt, or accept any matching record.

## NOTE
- [Eval5 P2] rubric #15 future date 2026-07-06 is a prompt-sanctioned calendar/reminder write target (<= 2026-08-01) - COUNCIL confirm resolved day
- [Eval5 P2] rubric #15 future date 2026-07-07 is a prompt-sanctioned calendar/reminder write target (<= 2026-08-01) - COUNCIL confirm resolved day
- [Eval5 P7] rubric census: 17 outcome / 0 process / 17 total
- [Eval5 P6] COUNCIL: under-strictness (6.3), exclusion coverage (6.6), UGT convergence (6.8), OE authority (6.9), strict feasibility (6.10), date-alignment ambiguity (6.11) require semantic judgment - flagged for council review
