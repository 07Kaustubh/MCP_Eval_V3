# S4 Bucket 2 Judge Errors (post-trajectory-walk update)

Task: `Tasks/35_6a4421ec8169e23828bb442d`

Bucket 2 = the rubric is correct; the agent's trajectory shows the agent satisfied the rubric; the judge misread. Log for potential platform appeal.

## Instance 1 — R5 Run 3 (semantic-equivalence miss on Raj's LOS-integrity caveat)

**Rubric:** "The Agent's email to Megan Sloane covers Raj Anand's caveat that LOS integrity cannot be promised until tested after the restore." Evidence authorizes "or similar phrasing".

**Judge decision (verifier fails file):** Fail.

**Judge justification (verbatim):** "Neither the email to Sloane nor the memo contain language about 'LOS integrity cannot be confirmed until tested.' The email asks for 'independent IT re-validation' but does not carry Raj's specific LOS integrity caveat forward."

**Trajectory-walk evidence (Run 3, email_send tool call to megan.sloane@wardbarrettlaw.com):** The email body explicitly contains "LOS integrity is unverifiable until tested" at char position 703 (section 1, PAY vs. RESTORE). Full context: "cloud snapshot ~72 hours stale; environment rebuild + validation is required; **LOS integrity is unverifiable until tested**; and ~3 days of pipeline activity needs manual reconstruction."

**Semantic-equivalence analysis:** "unverifiable until tested" is substantively equivalent to "cannot be promised until tested" (or "cannot be confirmed until tested"). Both express: LOS integrity cannot be asserted / confirmed / promised without testing after the restore. The rubric evidence authorizes "or similar phrasing"; the judge applied label-strict interpretation.

**Bucket 2 verdict:** Judge Error. Rubric is correct; agent satisfied on Run 3 with equivalent phrasing; judge missed the semantic equivalence.

**Downstream effect if platform accepts appeal:** R5 fail count moves from 6/6 to 5/6. R5 is then no longer an AF rubric. Post-appeal AF count = 2 (R14, R33). All-Failing Rubrics sub-dim remains 5/5 PASS (Bucket 1 ratio still 0/2 = 0%).

**Bonus finding on Run 3:** the same email also correctly identifies **Evan Mercer** as the post-term employee AND flags the LN drift verbatim: "Evan Mercer post-termination access: three borrower notices are drafted but unsent. Note a discrepancy — IT's log names LN-2026-00009 as the third file, but the drafted notice names LN-2025-00229. Different borrowers; needs reconciliation before anything goes out." This is direct evidence that (a) the Round 2 Marcus-to-Evan rubric fix is correct, and (b) the universe drift between Denise's notice-drafts (00229) and Raj's audit trail (00009) is real and was correctly identified by at least one agent trajectory. Run 3 was scored Fail on R10 (Marcus-labeled pre-Round-2 rubric) despite giving the universe-correct attribution — the rubric was punishing the correct answer.

## No other Bucket 2 instances

R14 and R33 trajectory walks confirm 6/6 legitimate AF: no leadership DM in any run contains "seven" / "7 files" / aggregate-count language, and no final response in any run aggregates the seven-file count into a single reported scope figure. Every failing decision on R14 and R33 is internally consistent with the trajectory.

The two prior-pass Bucket 2 instances (R20-old = R13-current Run 1 label-strictness; R26-old = R33-current Run 3 decision-vs-reasoning inconsistency) both resolved on the fresh re-grade — those failure decisions are now consistent with reasoning and internal to the run.
