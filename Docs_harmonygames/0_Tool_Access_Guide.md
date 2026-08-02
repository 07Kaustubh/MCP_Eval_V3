# Tool Access Guide

Start with the [documentation index](README.md). [`HarmonyGames_Base_Universe/Tool_Access/*.json`](../HarmonyGames_Base_Universe/Tool_Access/) is the sole authority for enabled services, exact tool names, parameters, requiredness, parameter types, and available operations. [`15_Persona_ACL.md`](15_Persona_ACL.md) is the authority for task-visible identity and read visibility. This guide is a human-readable capability summary; when it conflicts with a catalog, the catalog controls.

## Authority and scope

Use the narrowest authority for the question:

1. **Tool feasibility and capabilities:** `HarmonyGames_Base_Universe/Tool_Access/*.json`.
2. **Persona identity and read visibility:** [`15_Persona_ACL.md`](15_Persona_ACL.md) and its exact linked roster.
3. **HarmonyGames facts:** the live enabled services and the source data under [`HarmonyGames_Base_Universe/`](../HarmonyGames_Base_Universe/); task injections and changelogs may add task-specific facts.
4. **Requested work:** the prompt plus any uniquely discoverable company record it validly incorporates.
5. **Evaluation policy:** [`Evals/`](../Evals/), especially the [Prompt](../Evals/1_Prompt_Eval.md), [OE](../Evals/2_OE_Eval.md), [Rubrics](../Evals/3_Rubrics_Eval.md), and [Submission Gate](../Evals/5_Submission_Gate_Eval.md) evaluators.
6. **Authoring help and examples:** `Docs/` and `QC_Tasks/`. Examples illustrate patterns; they do not create tools, facts, or policy.

Oracle Events are internal plans, not authority. They cannot override the prompt, universe evidence, tool catalogs, trajectory, or current evaluation rules.

## Enabled catalogs

There are exactly 13 task-visible service catalogs:

1. Gmail
2. GDrive
3. GitHub
4. Snowflake
5. Slack
6. GCal
7. GDocs
8. GSheets
9. GSlides
10. Trello
11. Linear
12. Contacts
13. Confluence

No direct tools exist for CRM, Airtable, QuickBooks, Firebase, BigQuery, Metabase, App Store Connect, Google Play, AppLovin, Singular, Figma, Carta, or Stripe. These may be business topics or evidence recorded in enabled services, but prompts, Oracle Events, rubrics, and examples must not imply direct access.

All personas receive these same 13 service catalogs, but that does not mean all
reads return the same data. Persona-scoped reads apply only to Gmail, Slack,
GCal, and Contacts. GDrive, GitHub, Snowflake, GDocs, GSheets, GSlides, Trello,
Linear, and Confluence reads are unscoped. See
[`15_Persona_ACL.md`](15_Persona_ACL.md) for list/search/get and by-ID behavior.
Writes are outside Persona ACL scope; determine write availability only from
the catalogs.

## Capability summary

* **Gmail — triage-capable, not send-capable:** read/search messages and threads; retrieve attachments; list/get/create/delete labels; modify message/thread labels; archive threads; trash, untrash, or permanently delete messages and threads. There is no send, reply, or compose tool.
* **GDrive — read and write:** search/list/read files; list spreadsheet tabs and read a sheet by index; inspect metadata and paths; create folders/files; update metadata/content; move, trash, restore, permanently delete, and share files.
* **GitHub — read and write:** inspect repositories, branches, pull requests, reviews, comments, commits, files, users, issues, labels, tags, and releases; create/update issues and pull requests; comment/review/reply; create/update/delete labels; merge pull requests; create branches; create/update/delete or push files. The catalog does not provide repository creation.
* **Snowflake — read/query-only:** list databases, schemas, and tables; describe tables; execute/submit queries; inspect query history. It has no data-definition or data-mutation write tool.
* **Slack — read and write:** list/read/search channels, messages, threads, users, files, reactions, and metadata; post or edit messages; send/schedule messages and drafts; add/remove reactions; create conversations. The catalog does not provide message or channel deletion.
* **GCal — read and write:** list/read/search calendars and events; query free/busy; create, update, patch, delete, and respond to events.
* **GDocs — read and write:** search/read documents; create documents; batch-update content; delete documents.
* **GSheets — read and write:** search/read spreadsheets and ranges; create spreadsheets; update or append values; batch-update spreadsheets. The catalog has no spreadsheet-delete tool.
* **GSlides — read and write:** search/read presentations and pages; create presentations; batch-update presentations. The catalog has no presentation-delete tool.
* **Trello — read and write:** inspect/search boards, lists, cards, members, actions, comments, checklists, labels, and attachments; create/update/move/archive/delete cards; add comments, members, and labels; create/archive lists; create labels, checklists, and checklist items; update checklist items.
* **Linear — read and write:** inspect users, teams, projects, issues, statuses, labels, cycles, and comments; create users, teams, projects, issues, and comments; update projects and issues. The catalog has no delete tools.
* **Contacts — read and write:** list/get/search, add, edit, and delete contacts.
* **Confluence — read and write:** inspect/search spaces, pages, history, versions, diffs, comments, labels, attachments, and users; create spaces and pages; update/delete/restore pages; add comments and labels. The catalog does not provide space, comment, label, attachment, or user deletion.

Health, job-status, and job-result tools exist only where listed in the individual catalogs. The environment automatically applies `set_acting_user` with the exact roster email after universe load and reapplies it each run and turn. It is environment configuration, not an Agent tool, Oracle Event, rubric process requirement, or task call-count contribution.

## Authoring rules

* Keep implementation-specific tool names and parameter names out of task prompts and rubric criteria.
* Oracle Events may name exact tools and parameters. Copy those names from `HarmonyGames_Base_Universe/Tool_Access/*.json`; do not infer them from service branding or old examples.
* Feasibility must be evaluated against the enabled operations, not merely the presence of a service. For example, Gmail evidence can be searched and triaged, but Gmail correspondence cannot be sent or replied to.
* Validate required Gmail, Slack, GCal, and Contacts evidence from the assigned persona's view. Universe Explorer is author god-mode and can expose scoped records that the Agent Runner and Run Verifiers cannot read.
* Select the persona through taxonomy and use the exact roster email. Do not use the AMV persona dropdown because it overrides and persists.
* Agent Runner and Run Verifiers must use the same required persona. A read denial or filtered result is scoped absence, not proof that a record does not exist globally.
* Do not assume Persona ACL enforces write-side permissions.
* Use write actions only on cataloged write surfaces. Snowflake is not one; Gmail triage operations are, although sending email is not.
* Validate prompt feasibility with [`Evals/1_Prompt_Eval.md`](../Evals/1_Prompt_Eval.md), OE accuracy with [`Evals/2_OE_Eval.md`](../Evals/2_OE_Eval.md), and final tool/rubric compatibility with [`Evals/5_Submission_Gate_Eval.md`](../Evals/5_Submission_Gate_Eval.md).
