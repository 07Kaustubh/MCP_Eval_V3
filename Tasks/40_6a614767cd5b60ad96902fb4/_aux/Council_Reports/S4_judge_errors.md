# S4 Judge Errors (Bucket 2) - Task 40_6a614767cd5b60ad96902fb4

Bucket 2 (rubric correct, agent satisfied it, judge misread): none.

Probed and cleared as NOT Bucket 2:
- [OPUS] R13 runs 4,5 - a loose text scan suggested accommodation content, but the tight read shows no genuine ESA statement in either draft; the only hits were "esa" inside "Teresa" and the common word "reasonable". Genuine omission, judge correct.
- [OPUS] R8 runs 1,5 - the agent used "Harris property"/"Harry Harris" with no Sunset Ridge naming or Rio Bend distinction; passing runs used the "1402 Rimrock" address the judge credits. Genuine miss, judge correct.
- [GEMINI] R13 all runs - the approved ESA surfaced in the CRM/thread results, but the email omitted it every run; the judge correctly failed the omission. This is a carry-through failure, not a judge error.

Related but classified elsewhere:
- [RESOLVED - both models] R12 showed genuine judge INCONSISTENCY on the pre-split combined rubric (Gemini runs 4,5 pass while runs 1,2,6 fail in the same EVF-id-absent state). Root cause: the rubric's ambiguous "(EVF-2026-014)" parenthetical, so R12 was Bucket 1 (rubric invalid), not Bucket 2; fix in S4_fixes.md. UPDATE (dual-model post-split re-verify): the split (R12a owner-approved + R12b JP-coordination/not-closed) is applied to 7_Rubrics.json and re-graded on BOTH models - Opus 8a (R12a 6/6 pass, R12b fails only run 1 on a genuine omission) and Gemini 8b (R12a 6/6 pass, R12b 6/6 pass). Both halves grade CONSISTENTLY on both models; the flip-flop is eliminated everywhere. Closed.
