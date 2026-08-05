# All-Failing Rubric Diagnosis

Start with the [`Docs/README.md`](README.md) reading path. This specialist guide
supplements the scored QC specification and
[`Evals/4_Verifier_Fails_Eval.md`](../Evals/4_Verifier_Fails_Eval.md); it does
not override either one.

For tools, parameters, operations, and service limits,
[`HarmonyGames_Base_Universe/6_Server_Tools_Details.json`](../HarmonyGames_Base_Universe/6_Server_Tools_Details.json) is the sole authority. For rubric
wording and classification, use
[`2_Rubrics_Guidelines.md`](2_Rubrics_Guidelines.md),
[`Evals/3_Rubrics_Eval.md`](../Evals/3_Rubrics_Eval.md), and the current scored
QC specifications.

Persona ACL is active. Use
[`14_Persona_ACL.md`](14_Persona_ACL.md) and the exact key/email in
[`4_Persona_ACL_Roster.json`](../HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json).
Agent Runner and Run Verifiers must use the same persona; Universe Explorer
remains author god-mode.

## What “all-failing” means

An all-failing (AF) rubric failed **every completed run**. Exclude errored or
empty runs. If four of six runs completed, a rubric is AF only when it failed
all four. A rubric that passed at least one completed run is not AF.

Zero task-level passes can be a valid difficulty result. It does not make every
AF rubric valid. Each AF rubric still needs the platform's required 1–2 line
justification confirming that the repeated failure is a genuine Agent failure,
not a false negative caused by the criterion, judge, data, or environment.

## Diagnose before justifying

For each AF rubric:

1. Compare the criterion and its supporting fields with the prompt and any
   company record validly incorporated by the prompt.
2. Verify every expected fact in the live task state and base/injected ground
   truth.
3. Verify feasibility and observable precision against every relevant
   `HarmonyGames_Base_Universe/6_Server_Tools_Details.json` catalog, the assigned persona's applicable read scope,
   and the actual trajectory results.
4. Read each completed trajectory rather than relying on the verifier summary.
5. Classify the pattern:
   - **Legitimate Agent failure:** the criterion is valid and the completed runs
     genuinely missed it.
   - **Rubric invalid:** the criterion is ungrounded, beyond scope,
     non-atomic, over-specific, negatively phrased, or otherwise broken.
   - **Judge error:** the trajectory satisfies a valid criterion but the judge
     missed the evidence.
   - **Environment/tool-observability failure:** the required valid operation
     or precision systematically cannot be reached. This is an invalid AF, not
     model difficulty, and should be escalated.

For Gmail, Slack, GCal, and Drive-family (GDrive/GDocs/GSheets/GSlides) reads, reproduce the failure as the exact
assigned roster persona. A record found only through Explorer, local export, or
another persona does not establish Runner reachability. Required scoped-service
evidence inaccessible to the assigned persona makes the task/rubric invalid
unless the authorized outcome is an affirmative denial finding plus reporting,
escalation, or an authorized alternative. The other six services remain
unscoped, and writes are outside ACL scope.

The number of failures is only a prioritization signal. Repetition never proves
that the Agent is wrong.

## Outcome rubric checks

Outcome rubrics are the default. When one fails every run, check:

- **Grounding:** every ID, name, status, amount, date, count, destination, and
  expected conclusion exists and is tool-observable.
- **Prompt scope:** the criterion grades an authorized requirement, not an
  incidental OE or universe fact.
- **Atomicity:** one criterion checks one independently pass/fail condition.
- **Destination:** grade the artifact or action the prompt requested.
- **Precision:** use exact values for IDs, dates, counts, and discrete structured
  fields. Use “approximately” only for genuinely calculated or rounded values.
- **Generated wording:** allow equivalent free text with an objective rule or
  “(or similar)” where appropriate; do not loosen exact source values.
- **Affirmative, Agent-centric phrasing:** state what the Agent accomplishes,
  classifies, preserves, or leaves unchanged. Do not define success only as
  inactivity.
- **Scoped verifier evidence:** the verifier can grade from the trajectory,
  final response, visible write arguments, or evidence visible to that same
  persona, not hidden cross-persona state.

### Grounded HarmonyGames atomicity example

Invalid bundled criterion:

> The Agent reports that ENG-1456 is Done and identifies it as the issue for
> adding lock icons to the Season Pass and Social buttons.

The status and issue identification can pass or fail independently. Split them:

> The Agent reports that ENG-1456 is in the Done state.

> The Agent identifies ENG-1456 as “Put lock icon on "Season Pass" and "Social"
> (Bottom right of UI) buttons.”

Both values are grounded in
[`HarmonyGames_Base_Universe/Services_Data/linear/linear.issues.json`](../HarmonyGames_Base_Universe/Services_Data/linear/linear.issues.json).

### Affirmative exclusion example

Invalid prohibition-only criterion:

> The Agent does not mark the release approved.

Affirmative criterion:

> The Agent leaves the release-approval state unchanged.

Exclusions still require coverage; express the accepted scope or preserved
state positively. A negative factual finding remains valid when reported as an
affirmative behavior: “The Agent reports that human approval remains
unconfirmed.”

The same rule applies to ACL outcomes. “The Agent does not access another
mailbox” is prohibition-only and invalid. A task intentionally testing access
denial should grade the Agent's affirmative report, escalation, or authorized
alternative while preserving the factual denial.

## Process rubric checks

Process rubrics are optional and rare. Apply the current three-condition test to
every Process criterion. It is valid only when all three are true:

1. **Required by every valid solution path**, or phrased broadly enough to
   accept all valid paths.
2. **A stricter Outcome cannot capture the requirement.**
3. **It describes a behavioral verification property, not an execution trace.**

If any condition fails, delete the Process rubric, relabel a write action as an
Outcome, or tighten the relevant Outcome. Never make an invalid Process rubric
“flexible” by listing alternative tools, query strings, or call sequences.

Automatic `set_acting_user` application is environment configuration. It is
never a Process criterion, Oracle Event, Agent action, or complexity/call-count
item.

Only identify a **missing** Process rubric when the prompt or a validly
incorporated source creates a sequential or causal dependency that Outcomes
cannot verify. A genuinely missing dependency check is Non-Fail under current
QC; do not invent Process coverage when no dependency exists.

### Invalid Process example: Outcome can prove it

Process criterion:

> The Agent checks the ENG-2230 record directly before posting the Season Pass
> update.

If the prompt only asks for a status update, an Outcome can require the exact
grounded result—ENG-2230, “Season Pass Vfx Animations Implementation,” is Done.
The Process criterion unnecessarily fixes a path and adds no distinct signal.
Delete it and tighten the update's Outcome content criterion.

### Valid Process example: required ordering

Suppose the prompt explicitly requires the Agent to brief the team in
`#season-pass` before changing ENG-2230. Separate Outcomes can prove that both
actions happened, but neither can prove their order. This affirmative
behavioral criterion may be valid:

> The Agent posts the ENG-2230 briefing in `#season-pass` before updating
> ENG-2230.

It still must be grounded, required by every valid path, self-contained, and
verified against the trajectory.

## Writing the AF justification

A useful 1–2 line justification states:

- what exact requirement the completed runs missed; and
- why the criterion remains grounded, achievable, in scope, atomic,
  affirmative, and fair to every valid path.

Do not justify an AF rubric by saying only that “all runs failed.” If the
investigation reveals a rubric, judge, or environment defect, record that
classification and fix or escalate it instead of defending the false negative.
