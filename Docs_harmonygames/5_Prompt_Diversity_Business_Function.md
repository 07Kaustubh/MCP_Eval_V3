# **Diverse Prompts Tips**

## **For HarmonyGames:**

Start with the [`Docs/README.md`](README.md) index. [**HarmonyGames — Task Categories & Business Functions**](../HarmonyGames_Base_Universe/3_Task_Categories_Business_Functions.md) defines the 6 business functions, target shares, write-surface matrix, and grounded worked prompts. [`Evals/1_Prompt_Eval.md`](../Evals/1_Prompt_Eval.md) and [`Evals/5_Submission_Gate_Eval.md`](../Evals/5_Submission_Gate_Eval.md) control prompt evaluation. If an older example conflicts with those files, the live universe, or `HarmonyGames_Base_Universe/Tool_Access/*.json`, the current authority wins.

HarmonyGames tasks live at the intersection of game development and startup operations. Real work means triaging live-ops bugs across Linear + GitHub + Slack, reconciling a GDD spec against shipped code, threading a UA vendor arc from Gmail through Slack vendor channels to Trello and internally recorded attribution evidence, reconstructing a fundraise timeline from investor emails + board decks + founders Slack, or auditing internal documentation and discussions about a Firebase → BigQuery → Metabase pipeline against queryable Snowflake data. Firebase, BigQuery, and Metabase are business topics in that example, not directly accessible services. The failure mode is shallow — a prompt that just says "update the Linear ticket" or "post in Slack" isn't a HarmonyGames task, it's an inbox chore.

🎯 Use this guide to diversify by workflow shape. HarmonyGames' six business functions move at different tempos: Engineering & Live-Ops (25%) runs on sprint cycles, live bugs, and feature shipping; Product & Design (20%) runs on GDD-vs-implementation reconciliation and roadmap hygiene; Growth/UA/Marketing (15%) runs on vendor arcs and campaign cycles; Founders/Exec (15%) runs on board cadence and strategic bets; Finance/Legal/HR (15%) runs on legal closings, hiring, and vendor contracts; Analytics & Data (10%) runs on pipeline health and data-discrepancy hunts. Author across the range. A task where Brian triages Season Pass reward bugs reads nothing like a task where Leonard reconstructs the failed bridge round, and both should show up in your body of work.

Business function is not persona identity. The active
[`Persona_ACL_Roster.json`](../HarmonyGames_Base_Universe/Persona_ACL_Roster.json)
contains exactly 17 task personas across Design, Engineering, Executive, and
Product; it contains no Finance persona or CFO. Assign each prompt to a
plausible roster role rather than inventing one: Leonard or Arthur can own a
founder-level runway, contract, or company-closeout request; Frederick can own a
UA vendor-commercial workflow; Simon can own an analytics reconciliation; and
Julia can own a product planning workflow. Use the exact roster key/email and
validate role fit as part of Persona QC. See
[`15_Persona_ACL.md`](15_Persona_ACL.md).

⚡ Match the pattern, not the wording. Use grounded HarmonyGames anchors such as ENG-2349's Axe Arena/Win & Collect timer discrepancy, ZOM-387's Giant Analytics Ticket and match3d PR #319, the Helpshift wind-down, the failed $2.5M bridge round, or the Mattel “Dream Life Glow” pitch only after verifying the needed records in the live environment. `QC_Tasks/` is calibration history, not policy.

Design toward the authoring target of **40+ necessary average calls across 3+ enabled services**. Do not confuse that goal with the lower floors: prompt evaluation rejects tasks that do not require **more than 15** calls or **2+** services, and trajectory QC requires **at least 15 average** calls and **2+** services. A task that merely clears a floor may still be too shallow for the authoring goal.

Oracle Events may describe the intended path, but they are non-authoritative and cannot make an ungrounded example valid or override the prompt, universe, catalogs, or current Evals.

**⚠️ Key HarmonyGames tool constraints:**
* [`HarmonyGames_Base_Universe/Tool_Access/`](../HarmonyGames_Base_Universe/Tool_Access/) is authoritative; see the [Tool Access Guide](0_Tool_Access_Guide.md).
* Gmail supports reads and triage writes (labels, archive, trash/untrash/delete, label creation/deletion), but has no send/reply/compose tool.
* Snowflake is read/query-only (analytics warehouse).
* Exactly 13 catalogs are enabled: Gmail, GDrive, GitHub, Snowflake, Slack, GCal, GDocs, GSheets, GSlides, Trello, Linear, Contacts, and Confluence.
* Persona ACL scopes **reads only** for Gmail, Slack, GCal, and Contacts.
  GDrive, GitHub, Snowflake, GDocs, GSheets, GSlides, Trello, Linear, and
  Confluence reads remain unscoped; writes are outside ACL scope.
* Universe Explorer/local exports prove existence, not reachability by the
  assigned persona. Required Gmail, Slack, GCal, or Contacts evidence must be
  visible to that persona unless the intended outcome is an affirmative denial
  finding plus reporting, escalation, or an authorized alternative.
* No direct tools exist for CRM, Airtable, QuickBooks, Firebase, BigQuery, Metabase, App Store Connect, Google Play, AppLovin, Singular, Figma, Carta, or Stripe.
