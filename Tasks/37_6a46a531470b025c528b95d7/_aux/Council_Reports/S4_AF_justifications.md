# S4 AF justifications — Bucket 3 (Legitimate Model Failure) — Task 37

Seven unique failing rubrics, 12 total fail instances. All 5 checklist items answered YES for every rubric below. Justifications follow the strict style: concise, no em-dashes, concrete data facts, specific reasoning gap, no references to guides or specs.

Aggregate pattern for the file: 6 of 7 failing rubrics concentrate on Run 1, where the agent chose to compress aged files under a single relative-time phrase instead of naming each loan's lock expiration date. The two remaining rubrics (A and E) fail across Runs 1, 3, and 5 on the same depth-vs-breadth trap: the agent summarised the 26-file pipeline but did not surface the two anomaly loans (LN-2026-00623 premature clear-to-close and LN-2026-00010 max-outstanding-docs) in the final response.

---

## Rubric A — Final response names LN-2026-00623 as clear-to-close with 5 outstanding documents

**Runs failing:** 1, 3, 5 (3 of 6). Runs passing: 2, 4, 6.

**Justification.**
Three of six runs surfaced LN-2026-00623 in the final response but did not describe it as clear-to-close with 5 outstanding required documents. Run 1, tool call 231 wrote "00623 V. Pham signed, but lender wire missed cutoff; recording pushed" and filed the loan under a post-signing wire anecdote instead of the premature clear-to-close anomaly. Run 3 omitted the loan number from the final response entirely, mentioning only Kang LN-2026-00613 and Wilson LN-2026-00008 as anomaly examples. Run 5 filed "M. Pham" under "dormant files (9 to 13 months, no closing on record)" which misclassifies a live clear-to-close file with an expired 2026-04-01 lock. The premature clear-to-close anomaly is one of two headline findings in the queue and requires the agent to trace the document checklist for the loan rather than lean on status labels alone.

---

## Rubric B — Amy Chen update includes LN-2024-00123 lock expiration 2024-10-07

**Runs failing:** 1 (1 of 6). Runs passing: 2, 3, 4, 5, 6.

**Justification.**
Run 1, tool call 174 sent Amy Chen's email with "Lock long expired, flagged critical" for LN-2024-00123 and did not state the specific 2024-10-07 expiration date. The email correctly gave the 2026-03-24 date for LN-2026-00532 in the same message. The other five runs supplied both dates. The failure is compression on aged files: the agent picked a relative-time phrase instead of the atom the loan officer needs to price a relock or extension.

---

## Rubric C — Keisha Williams update includes 4 loan lock expiration dates

**Runs failing:** 1 (1 of 6). Runs passing: 2, 3, 4, 5, 6.

**Justification.**
Run 1, tool call 168 sent Keisha Williams's email with "all locks expired 250+ days" as a single grouped statement for LN-2024-00103, LN-2025-00330, and LN-2025-00380 and gave the specific 2026-03-20 date only for LN-2026-00376. The 2024-09-08, 2025-06-22, and 2025-08-30 dates are present in the LOS records but did not surface in the update. The other five runs listed each of the four dates individually. Aggregating three loans under one relative-time phrase drops the atom the loan officer needs to file per-loan relock quote requests.

---

## Rubric D — Marcus Webb update includes LN-2024-00125 lock expiration 2024-10-17

**Runs failing:** 1 (1 of 6). Runs passing: 2, 3, 4, 5, 6.

**Justification.**
Run 1, tool call 180 sent Marcus Webb's email with "stale (target close 10/10/24, lock long expired, flagged critical)" for LN-2024-00125 and did not state the specific 2024-10-17 lock expiration. The 2026-04-03 date for LN-2026-00539 appeared correctly in the same message. The other five runs supplied both dates. Same aged-file compression pattern that recurs across the per-LO cohort in Run 1.

---

## Rubric E — Final response identifies LN-2026-00010 with 7 outstanding required documents

**Runs failing:** 1, 3, 5 (3 of 6). Runs passing: 2, 4, 6.

**Justification.**
Three of six runs surfaced LN-2026-00010 in the final response but did not identify it as the loan with the most outstanding required documents at 7 items. Run 1 discussed LN-2026-00010 only in a compromised-portal impacted list ("00008 Wilson and 00010 Ferguson on Compliance's compromised-portal impacted list, borrower comms on hold") and never gave the document count. Run 3 omitted the loan number from the final response entirely. Run 5 mentioned Ferguson only inside a lock-age range ("from 4 days (Ferguson) to ~660 days") and did not name the 7-document count or identify LN-2026-00010 as the outstanding-docs leader. The max-outstanding-docs anomaly is the second headline finding a capable agent must trace through the document checklist and name in the summary.

---

## Rubric F — Natasha Okafor update includes LN-2025-00286 and LN-2026-00010 with lock dates and doc counts

**Runs failing:** 1 and 2 (2 of 6, for different reasons). Runs passing: 3, 4, 5, 6.

**Justification.**
Two runs failed the two-loan Natasha update. Run 1, tool call 186 covered both loans but wrote "lock long expired, flagged critical" for LN-2025-00286 instead of the 2025-05-12 date. Run 2, tool call 154 sent Natasha's email covering LN-2026-00010 but dropped LN-2025-00286 (O'Connor, clear-to-close, 2025-05-12 lock, $382,800) from the email entirely, leaving Natasha without a status on one of her two active files. Both shortcuts hit the same LN-2025-00286 atom: Run 1 compressed its date, Run 2 omitted the loan.

---

## Rubric G — James Thornton update includes LN-2025-00344, LN-2025-00363, LN-2026-00541 with lock dates

**Runs failing:** 1 (1 of 6). Runs passing: 2, 3, 4, 5, 6.

**Justification.**
Run 1, tool call 192 sent James Thornton's email that gave the specific 2026-04-06 date for LN-2026-00541 but flagged LN-2025-00344 (2025-07-05) and LN-2025-00363 (2025-07-29) as stale files without their expiration dates. The other five runs supplied all three dates individually. The failure is the same aged-file compression pattern that recurs across the per-loan-officer cohort updates in Run 1: the agent selected a relative-time phrase over the per-loan atom.

---

## Summary

Total Bucket 3 fails: 12 fail-instances across 7 unique rubrics. All justifications trace to trajectory tool calls in `trajectory-runs/trajectory-run-{1..6} (N).json` and universe-grounded atoms.

The concentrated Run 1 pattern (5 of 7 per-loan-officer cohort rubrics fail there) is one of the intended failure modes: a capable agent must commit to per-loan atom fidelity for aged files rather than compressing them to a single relative-time phrase. The final-response depth pattern across Runs 1, 3, and 5 is the second intended failure mode: the agent must trace document-checklist depth on the two anomaly loans (LN-2026-00623 premature clear-to-close and LN-2026-00010 max-outstanding-docs) rather than lean on the 26-file pipeline breadth.
