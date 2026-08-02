# Persona ACL Policy

Persona ACL is active and fully implemented for HarmonyGames. This document is
the authority for task-visible identities and persona-scoped read visibility.
[`HarmonyGames_Base_Universe/Tool_Access/*.json`](../HarmonyGames_Base_Universe/Tool_Access/) remains the authority for service
capabilities, exact tools, parameters, and available read and write operations.

## Two policy layers

1. **Identity configuration:** the assigned taxonomy persona resolves to one
   exact roster email. The environment uses that email as the acting user.
2. **Read enforcement:** Gmail, Slack, GCal, Contacts, GDrive, GDocs, GSheets,
   and GSlides filter reads to data visible to the acting user. The other five
   task-visible services do not apply persona-scoped read filtering.

Persona ACL does not govern writes. A cataloged write may still be available,
but this policy must not be cited as granting or denying it.

## Task-visible personas

The exact 17-record roster is
[`HarmonyGames_Base_Universe/Persona_ACL_Roster.json`](../HarmonyGames_Base_Universe/Persona_ACL_Roster.json).
Use its `persona_key`, `name`, `email`, `role`, and `department` values exactly.
Never construct, normalize, or infer an email from a person's name.

There is no task-visible Finance persona or CFO. Finance remains a business
function, not an identity; assign it only to an appropriate persona from the
roster.

## Access matrix

Here, **unscoped** means shared across task personas, not public outside the
HarmonyGames evaluation environment.

| Service | Persona-scoped reads | Visibility |
|---|:---:|---|
| Gmail | Yes | Acting user's mailbox-visible messages, threads, labels, profile, and attachments |
| Slack | Yes | Conversations, messages, threads, files, and related records visible to the acting Slack user |
| GCal | Yes | Calendars, events, and free/busy data visible to the acting user |
| Contacts | No | Contacts visible in the acting user's contact scope |
| GDrive | Yes | Files and folders the acting user owns or that are shared with them, including metadata, content, and search results |
| GDocs | Yes | Documents readable by the acting user through the same Drive file visibility |
| GSheets | Yes | Spreadsheets, sheet metadata, and cell ranges readable by the acting user through the same Drive file visibility |
| GSlides | Yes | Presentations, pages, and page elements readable by the acting user through the same Drive file visibility |
| GitHub | No | Unscoped |
| Snowflake | No | Unscoped |
| Trello | No | Unscoped |
| Linear | No | Unscoped |
| Confluence | No | Unscoped |

The unscoped group is the policy's **public-service group**. It contains exactly
GitHub, Snowflake, Trello, Linear, and Confluence.

The four Google document services share Drive's underlying file ACL. A file that
is invisible to the acting user in GDrive is also invisible through GDocs,
GSheets, and GSlides, including by-ID reads.

## Scoped read behavior

For Gmail, Slack, GCal, Contacts, GDrive, GDocs, GSheets, and GSlides:

- **List operations** return only records visible to the acting user.
- **Search operations** search only within that visible set and do not reveal
  inaccessible matches.
- **Get/read operations** enforce the same visibility rule. Supplying a known
  object ID does not bypass the ACL.
- A by-ID request for an inaccessible object is denied or returned as not
  found; its protected content is not disclosed.
- Child and related reads, such as a thread, attachment, event, conversation,
  document body, cell range, or slide page lookup, inherit the applicable scoped
  visibility.

Authors must not treat a read denial or filtered result as proof that the
underlying company record does not exist globally. It establishes only that the
record is unavailable to the selected persona.

## Author, Agent, and verifier contexts

- **Universe Explorer:** authors operate in god-mode so they can inspect the
  full universe while designing and validating a task.
- **Agent Runner:** the run uses the task's required persona and therefore its
  scoped read visibility.
- **Run Verifiers:** every verifier uses the same required persona as the Agent
  Runner. A verifier must not depend on broader author visibility.

Author god-mode is for universe inspection only. It does not make author-visible
evidence in any of the eight scoped services reachable by the Agent or verifier.

## Persona lifecycle and precedence

1. Select the required persona through the task taxonomy.
2. Resolve the persona through the exact ACL roster email.
3. For Agent Runner and Run Verifiers, the taxonomy sends that exact roster
   email as `persona_email` in the run payload. Universe Explorer omits
   `persona_email` and remains author god-mode.
4. After the universe loads, the environment automatically applies
   `set_acting_user` with that email.
5. The environment reapplies the same acting user on every agent or verifier
   run and every turn.

Do not touch the separate platform AMV persona dropdown: it overrides the
taxonomy selection and persists. Taxonomy selection plus the exact roster
mapping is the required source of persona identity.

`set_acting_user` requires the exact `email`. It is environment configuration,
not an Agent tool, not an Oracle Event or rubric process requirement, and not a
task call to include in complexity or trajectory call counts.

## Google viewer-context tools

The catalog no longer exposes any `*_get_viewer` or `*_set_viewer` tool. GCal,
GDrive, GDocs, GSheets, and GSlides each had a get/set pair; all ten were removed
from `5_Server_Tools_Details.json`. A new task may not call one, and a rubric or
Oracle Event that names one cites a phantom tool.

The rule below still governs archived material. Viewer calls appear in the
V5_HG_Buckets QC reference trajectories, and one `8_Verifier_Fails.txt` cites
`gcal_get_viewer`, so anyone grading those runs still needs it.

Viewer context was never task persona identity and never replaced taxonomy, the
roster, `persona_email`, or `set_acting_user`. It could not authorize an ACL
bypass, and viewer calls earned no Oracle Event, Process, or complexity credit.
Where a manual viewer change caused scoped Google reads under the wrong identity,
or otherwise defeated the assigned persona scope, the execution is
**Excluded (environment/config/path violation)**.

## Task-authoring and evaluation rules

- Validate every required read in the eight scoped services from the assigned
  persona's Agent/Verifier view, not only from Universe Explorer.
- Design prompts so all required evidence is reachable by that persona. A
  deliberate read denial may be contextual evidence, but inaccessible content
  cannot be required ground truth.
- Treat list/search omissions and by-ID denied/not-found results consistently;
  do not instruct the Agent to bypass persona visibility.
- Keep implementation-specific ACL configuration out of natural task prompts.
- Use the same persona for trial runs, final runs, and Run Verifiers.
- Do not assume an ACL-based write denial or make one necessary to a prompt,
  Oracle Event, or rubric. Determine write feasibility only from the
  authoritative tool catalogs.
- A shared catalog does not imply shared read visibility: all personas have the
  same 13 task-visible services, while eight of those services enforce
  persona-scoped reads.
