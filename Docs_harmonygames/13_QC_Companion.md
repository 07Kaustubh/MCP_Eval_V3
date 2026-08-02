# HarmonyGames QC Companion

This plain-language companion explains four QC dimensions that commonly trip up
task authors. It is **supplementary**, not a scoring source. Start with the
[`Docs/README.md`](README.md) reading path, then use
[`7_QC_Spec_Doc1.json`](7_QC_Spec_Doc1.json),
[`8_QC_Spec_Doc2.md`](8_QC_Spec_Doc2.md), and the current
[`Evals/`](../Evals/) for authoritative evaluation rules.

[`HarmonyGames_Base_Universe/Tool_Access/*.json`](../HarmonyGames_Base_Universe/Tool_Access/) is the sole authority for enabled
services, exact operations, parameters, pagination, and read/write limits. Live
task data plus its injection/changelog controls task-specific facts; the base
export is the local grounding source. Current authorities override any stale
example wording.

Apply Persona ACL within the dimensions below rather than as a separate score.
[`15_Persona_ACL.md`](15_Persona_ACL.md) defines read visibility, and
[`Persona_ACL_Roster.json`](../HarmonyGames_Base_Universe/Persona_ACL_Roster.json)
defines the exact 17 persona key/email bindings. Gmail, Slack, GCal, and
Contacts reads are scoped; the other nine services are unscoped; writes are
outside ACL scope. Agent Runner and Run Verifiers use the same persona, while
Universe Explorer remains author god-mode.

The paired snippets below isolate one QC dimension at a time. They are not
complete task prompts and should not be copied as submissions.

## Scoring reminder

- **1–2:** Fail
- **3–4:** Pass with a Non-Fail issue, when that dimension defines a middle band
- **5:** Perfect

Some dimensions, including Unique Ground Truth, have no 3–4 band.

## 1. Unique Ground Truth

**What it checks:** every reasonable reading reaches the same correct outcome.
Different searches, reasoning paths, and free-text wording are fine. Different
write actions, destinations, or act-versus-defer outcomes are not.

- **1–2 — Multiple Valid Answers:** two reasonable readings can produce
  different correct end states.
- **3–4:** not available for this dimension.
- **5:** the artifacts, action, and destination are sufficiently anchored that
  experts converge on one result.

Paired HarmonyGames example:

❌ “Pick the most important Season Pass issue and post an update to the right
team channel.”

Many Season Pass issues exist. Different agents can reasonably select different
records and produce different updates.

✅ “Use ENG-2230, ‘Season Pass Vfx Animations Implementation,’ as the issue
anchor and post its current-state brief in `#season-pass`.”

The source path remains open, but the issue and write destination are pinned.
`ENG-2230` and `#season-pass` both exist in the base data.

## 2. Agent-Centric, Affirmative Rubric Phrasing

**What it checks:** every criterion describes an affirmative action,
classification, scope boundary, or preserved state attributable to the Agent.
Criteria must not name implementation-specific tools.

- **1–2:** at least one criterion drops the Agent as actor, uses passive or
  artifact-only framing, names a tool, or defines acceptance only through a
  prohibition/no-op.
- **3–4:** the wording is still Agent-centric and affirmative but does not
  follow the preferred “Agent + verb + context” pattern exactly.
- **5:** clear Agent actor, positive acceptance condition, necessary context,
  and no tool name.

Paired rubric example:

❌ “A Season Pass update was posted, and the release was not approved.”

This is passive, bundles two conditions, and expresses the exclusion
negatively.

✅ “The Agent posts the ENG-2230 status update in `#season-pass`.”

✅ “The Agent leaves the release-approval state unchanged.”

The two independently pass/fail requirements are split and phrased
affirmatively. Negative factual states remain valid when the Agent reports them:
“The Agent reports that human approval remains unconfirmed.”

## 3. Prompt Clarity and Specificity

**What it checks:** the intent is understandable and specific enough to avoid
different side effects, without turning the prompt into a runbook. The Agent
should still determine how to investigate.

- **1–2 — Major Clarity / Specificity:** the core ask or required details cannot
  be reasonably understood.
- **1–2 — Action Decision Ambiguity:** reasonable readings lead to different
  write actions, write versus no-write, or act versus defer.
- **3–4:** minor ambiguity remains, but all reasonable readings produce the same
  writes and external side effects.
- **5:** natural internal language, anchored outcome, and at most one minor
  assumption.

Paired HarmonyGames example:

❌ “Handle the Season Pass issue before release and update everyone if needed.”

The issue, destination, action, and meaning of “if needed” are all open. One
Agent may update Linear, another may only post, and another may defer.

✅ “Reconcile ENG-2230 against the current implementation and project record,
then post the current-state brief in `#season-pass`. Keep release approval
unchanged.”

The Agent still has to investigate the evidence, but the requested side effect
and preserved state are clear.

## 4. Truthfulness

**What it checks:** every concrete fact in the prompt matches the task
environment and is reachable through the enabled services under the assigned
persona's applicable read scope.

- **Major factual errors:** wrong tight identifiers—including channel names,
  document IDs, repository names, paths, dates, issue IDs, amounts, and email
  addresses. One major error fails the dimension.
- **Minor factual errors:** loose descriptive mismatches that natural language
  can absorb. Two or more fail; exactly one may fit the 3–4 band unless it
  actually causes Agent failure.
- **5:** no factual errors or misleading claims.

Paired HarmonyGames example:

❌ “Review ENG-2230, ‘Season Pass Vfx Animations Implementation,’ and post the
result in `#season_pass`.”

The issue is grounded, but `#season_pass` is not the exact channel name. A
single wrong tight identifier is a major factual error.

✅ “Review ENG-2230, ‘Season Pass Vfx Animations Implementation,’ and post the
result in `#season-pass`.”

The corrected issue and channel are grounded in the current base export.

## Actual local data layout

Use
[`HarmonyGames_Base_Universe/Services_Data/`](../HarmonyGames_Base_Universe/Services_Data/)
for local grounding. This checkout contains full exported service data; large
surfaces are stored either in full service-level JSON files or in shards. Do
not look for a legacy `Data/` directory or `__sample30` files.

Key paths:

- Combined export:
  [`Services_Data/Base_Universe_Complete_Data.json`](../HarmonyGames_Base_Universe/Services_Data/Base_Universe_Complete_Data.json)
- Linear:
  [`linear/linear.issues.json`](../HarmonyGames_Base_Universe/Services_Data/linear/linear.issues.json)
  and
  [`linear/linear.comments.json`](../HarmonyGames_Base_Universe/Services_Data/linear/linear.comments.json)
- Slack metadata:
  [`slack/slack.channels.json`](../HarmonyGames_Base_Universe/Services_Data/slack/slack.channels.json)
  and
  [`slack/slack.users.json`](../HarmonyGames_Base_Universe/Services_Data/slack/slack.users.json)
- Slack message shards:
  `Services_Data/slack/messages/<channel-or-DM-id>/<YYYY-MM>.json`
- Gmail metadata:
  `Services_Data/gmail/gmail.users.json`,
  `gmail.labels.json`, and `gmail.manifest.json`
- Gmail thread shards:
  `Services_Data/gmail/threads/<owner-or-service>_EMAIL_<thread-id>.json`
- GitHub:
  [`github/github.pull_requests.json`](../HarmonyGames_Base_Universe/Services_Data/github/github.pull_requests.json),
  [`github/github.reviews.json`](../HarmonyGames_Base_Universe/Services_Data/github/github.reviews.json),
  and the other full `github/github.*.json` tables
- GDrive index and content:
  [`gdrive/gdrive.drive_files.json`](../HarmonyGames_Base_Universe/Services_Data/gdrive/gdrive.drive_files.json)
  plus `Services_Data/gdrive/root/<owner>/...`
- Contacts:
  [`contacts/contacts.contacts.json`](../HarmonyGames_Base_Universe/Services_Data/contacts/contacts.contacts.json)

The local base export does not supersede the live task state. Check the task
injection/changelog for additions or modifications, and use the live service
response when grading what the Agent could actually observe. Explorer/local
existence alone does not prove that the assigned persona can read Gmail, Slack,
GCal, or Contacts evidence.

## HarmonyGames truthfulness checks

- Task personas and exact emails must come from
  [`Persona_ACL_Roster.json`](../HarmonyGames_Base_Universe/Persona_ACL_Roster.json);
  use
  [`HarmonyGames_Base_Universe/2_Persona_Briefs.md`](../HarmonyGames_Base_Universe/2_Persona_Briefs.md)
  for role context. External contacts may be referenced but cannot author the
  prompt.
- The roster covers Design, Engineering, Executive, and Product and contains
  no Finance persona or CFO; assign Finance/Legal/HR work to a plausible roster
  role.
- Brian Foster's grounded email is `brian@harmonygames.co`.
- The GitHub organization is `harmonygames-Games`.
- Gmail supports reading and triage actions but not send, reply, compose, or
  draft.
- Snowflake is query/read-only.
- Persona ACL scopes reads only for Gmail, Slack, GCal, and Contacts. GDrive,
  GitHub, Snowflake, GDocs, GSheets, GSlides, Trello, Linear, and Confluence
  reads remain unscoped, and writes are outside ACL scope.
- A CodeRabbit review is not automatically human approval.
- Redacted `PERSON_XXXX` and `EMPLOYEE_XXXX` identities should not carry unique
  ground truth when they cannot be resolved.
- Exact Linear keys, Slack channels, repositories, contacts, dates, and amounts
  must be checked rather than inferred from a nearby name.
- Required Gmail, Slack, GCal, or Contacts data inaccessible to the assigned
  persona hard-fails feasibility unless the intended outcome is an affirmative
  access-denial finding plus reporting, escalation, or an authorized
  alternative.
- `set_acting_user` is automatic environment configuration, not Agent work, an
  OE, rubric/Process requirement, or call-count item. Leave the AMV persona
  dropdown untouched so it cannot override Taxonomy.

## One-line takeaway

Anchor the outcome, keep criteria affirmative and Agent-centric, make the side
effects unambiguous, and verify every concrete value against the actual
HarmonyGames data and tool-visible task state.
