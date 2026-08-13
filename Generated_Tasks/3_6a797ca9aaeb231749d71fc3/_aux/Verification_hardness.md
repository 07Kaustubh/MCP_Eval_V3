# Verification — HARDNESS phase (v16 cross-source verification)

## Verdict

**PASS.** HARDNESS phase complete. 5 levers selected (L1 latching, L2 structured-DB skip on both GitHub `review_comments` + Trello `check_items`, L6 four-Marcus disambiguation, L9 Friday-evening authority dismissal, L10 reversal / supersession). Density midpoint 56 across 7 services (github, trello, linear, contacts, gdocs, gdrive, gsheets), Slack fully excised after `check_persona_acl.py` confirmed Victor Barnes is a member of zero channels of any kind. HG framework authoring target (40+ calls AND 3+ services) cleared with 40% margin on calls, 133% margin on breadth. Trajectory QC floor of 15 average cleared by 3.7x. Four stump predictions carried forward for S1. See `Hardness_Plan.md` for the full plan.

## Sources consulted

- **Per-task data** :: `_aux/Universe_Split/` end-to-end. Grepped `slack.channels.json` + `slack.users.json` + `slack.files.json` (13 art/vfx-related channels; 4 Marcus + Ozhan identities; combofighter-vfx activity Jan-Feb 2026). Walked `github.pull_requests` (PR #1 draft `changed_files=0` since 2025-12-02 vs merged PR #36 vfx updates 2026-02-11 vs PR #16 win screen coin vfx 2025-12-21) + `github.review_comments` (10 unresolved comments on PR #37 Oliver Brooks CHANGES_REQUESTED) + `github.pull_request_comments` (CodeRabbit summaries hide L2 pushback). Walked `trello.boards` + `trello.cards` + `trello.check_items` + `trello.checklists` + `trello.actions` (ZM ROADMAP 79 cards; `Marcus to create VFX` incomplete on `6851a9942b47001e59c8e777` since 2025-06-20 last toggle). Cross-referenced `contacts.contacts` + `linear.users` + `github.users` for the four Marcus identities (Marcus Bennett `usr_c77c50cc15c5342d`, Marcus Lee `usr_b501f018a4c5319f`, `marcus@harmonygames.co` `usr_d7ae9de750a5640a`, GitHub PERSON_0396 with no linked email). Consulted `_aux/Fact_Ledger.json` (47 emails, 41 amounts, 1078 dates, 174 contacts) and `_aux/Universe_Index/graph_report.md` (Victor's mention density mid-tier). Persona ACL verified against `HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json` (Victor: Engineering, `EMPLOYEE_0030_SLACK_ID`).
- **Eval spec** :: `Evals_harmonygames/1_Prompt_Eval.md` (density hard gate >15 necessary calls + 2+ services; persona ACL parse-live-from-Access-matrix rule at :14/:42/:99/:432). Cross-checked authoring target with `Docs_harmonygames/1_Project_Instructions_Overall.md` (40+ calls AND 3+ services). Consulted `Docs_harmonygames/4_Prompt_Hard_Tips.md` for agent behavior patterns (agents skip structured DBs; agents latch first framing; agents miss thread replies) that inform the L1/L2/L10 lever choices. Consulted `Docs_harmonygames/9_Common_Error.md` for persona-ACL rules (writes are outside ACL scope; scoped seven services; unscoped four services after V5 retirement).
- **QC spec** :: `Docs_harmonygames/7_QC_Spec_Doc1.json` — Trajectory / Tool Call Count floor 15 average, Density thresholds triple (authoring vs prompt-gate vs trajectory), Universe Feasibility, Cross-service Coherence (all binary). `Docs_harmonygames/8_QC_Spec_Doc2.md` — per-sub-dim scoring bands + severity (Overly Broad = Moderate here; Overly Specific = Minor here; the pre-swap ordering, reversed from StarPM). Confirmed no injection-difficulty concern (HG floor 2.5, and this task is not injecting per `9_Universe_inject.sql` content; injection_difficulty_floor read from framework `hg` = 2.5).

## Data sources consulted
- `_aux/Universe_Split/slack.channels.json` :: grepped for art/vfx/animation/marketing/leapblock/ozhan — 13 relevant public channels including `god-gameart` (C04V7N09LE7), `god-vfx` (C05UQKDLGAU), `combofighter-vfx` (C0AA36TV9QA), `leapblock` (C05URGU759U).
- `_aux/Universe_Split/slack.users.json` :: confirmed 4 distinct Marcus identities + Ozhan.
- `_aux/Universe_Split/slack.files.json` :: 47,968 rows sampled for 2026 activity — only combofighter-vfx (16 files Jan-Feb 2026) and leapblock (1 file 2026-01-27) show 2026 activity; other god-* channels dormant.
- `_aux/Universe_Split/linear.teams.json` :: 5 teams (ART, DES, ENG, EPI, ZOM).
- `_aux/Universe_Split/linear.issues.json` :: 597 ART tickets all 2023-2024 (stale for a 2026-02-28 task); ZOM Q4 2025 - Jan 2026 activity mostly Canceled.
- `_aux/Universe_Split/linear.users.json` :: Victor, Marcus Bennett, Marcus Lee, marcus@, Martin Walsh, Leonard, Robert, Claire, Ozhan all present.
- `_aux/Universe_Split/github.repositories.json` :: 16 repos, Combo-Fighters is the live art/VFX target for Q1 2026.
- `_aux/Universe_Split/github.pull_requests.json` :: PR #1 draft (0 additions, "do not merge" label, since 2025-12-02); PR #36 "vfx updates" merged 2026-02-11; PR #37 "Combo Definition Updates" merged 2026-02-13; PR #16 "win screen coin vfx" merged 2025-12-21.
- `_aux/Universe_Split/github.review_comments.json` :: PR #37 = 10 line comments (Oliver Brooks CHANGES_REQUESTED with unresolved rarity-SO question); PR #35 = 27 comments; PR #24 = 14.
- `_aux/Universe_Split/github.pull_request_comments.json` :: top-level comments are CodeRabbit auto-summaries; substantive discussion lives in review_comments (L2 carrier confirmation).
- `_aux/Universe_Split/github.users.json` :: PERSON_0396 = "Marcus" with NO linked email (author of PRs #1, #16, #36).
- `_aux/Universe_Split/trello.boards.json` :: ZM ROADMAP `6851a6569f3bf818760632ab`; UA/BD `66da196af476ab78deaa0cef`.
- `_aux/Universe_Split/trello.cards.json` :: ZM ROADMAP holds 79 cards including `Reward Animations (VFX)` `6851aafe8c9e95ec0abbd262`, `Card upgrade VFX implementation` `6852f6014ef0266338b1728b`, `Equipped Card Item Infusion VFX implementation` `6851a9942b47001e59c8e777`.
- `_aux/Universe_Split/trello.check_items.json` + `trello.checklists.json` :: 9 of 79 ZM ROADMAP cards have checklists; 15 check_items across those; incomplete items include `Marcus to create VFX` (Equipped Card card), multiple `Provide engineering estimate`, `Backend team needs to read GDD`.
- `_aux/Universe_Split/trello.actions.json` :: `Marcus to create VFX` last state-toggled 2025-06-20, never marked complete despite subsequent merged VFX work.
- `_aux/Universe_Split/contacts.contacts.json` :: Ozhan, Leapblock, Martin Walsh, Leonard, Robert all present as contacts.
- `_aux/Fact_Ledger.json` :: 47 emails, 41 amounts, 1078 dates, 174 contacts. `personas_declared` field empty (HG-specific ledger gap noted).
- `_aux/Universe_Index/graph_report.md` :: usr_victor_barnes = 283 mentions (mid-tier density); top density usr_65c76e0b87aa7e9b = 1012 and usr_robert = 969.

## Reference docs consulted
- `Reference/Hardness_Playbook.md` :: 11-lever catalog consulted end-to-end. Selected L1 (5-8), L2 (4-7 per variant, x2), L6 (3-5), L9 (3-5), L10 (4-6). HG framework note: authoring target 40+ AND 3+ services; NOT V3-family 50/40.
- `Tasks/_meta/Learnings.md` :: L1-L35 consulted. Citations in plan: L1, L2, L3, L4, L5, L6, L7 (hard rule — no correct answer in any body), L8, L9, L10, L12, L13, L14, L15 (no explicit hint), L20, L24 (soft-verb convention on the L9 dismissal), L25 (existing-artifact anchor), L28 (tool-variant trap analog), L33 (design for margin).
- `Reference/Sessions/HARDNESS.md` :: runbook followed. HG framework-scoped density gate applied (authoring 40+ AND 3+ services), not the V3-family 50/40 scheme.

## Eval spec sub-dims relevant to this phase
- Trajectory / Tool Call Count :: HG floor 15 avg (QC trajectory floor). Projected midpoint 54 = 3.6x floor. HG authoring target 40+ AND 3+ services (Docs_harmonygames/7 spec doc). Projected midpoint 54 across 7 distinct services. PASS with margin.
- Trajectory / Multiple Meaningful Writes :: 5 write actions across 5 services planned (Linear comment, Trello check_item toggle, Slack post, GDocs status brief, GSheets vendor tracker). PASS.
- Prompt / Investigation :: 3 discoverable levers (L1, L2, L10) require the agent to reason past the anchored frame; no answer given verbatim. Expected PASS at S1.

## QC spec sub-dims relevant to this phase
- Trajectory T1 Tool Call Count :: projected midpoint 54, band PASS (well above HG's 40+ authoring target and 3.6x above the 15 QC floor). Applies rule L33 design-for-margin.
- Trajectory T2 Agent Failure Rate :: not projected at HARDNESS; deferred to S4.
- Universe / Universe Feasibility :: all 5 selected levers grounded in specific universe records with grep-verified evidence (no hallucinated ids).
- Universe / Cross-service Coherence :: L8 multi-link chain traverses 4 services with no contradiction between them; PR #1 vs PR #36/#16 supersession is a designed contrast, not a coherence bug.

## Verification statements
- [x] At least 3 levers selected (5: L1, L2, L6, L9, L10); each cites a Learnings.md entry (L1/L13, L2/L10/L28, L6, L9, L10/L25 respectively).
- [x] Density midpoint projection is one of {PASS ≥ 40 for HG, INSUFFICIENT < 40}. Projected midpoint 54 = PASS.
- [x] Service breadth table populated with 7 distinct services, 5 above 5% share.
- [x] Every environment-lever placement cites a surface the prompt gives the agent a natural reason to open (Combo-Fighters recent PRs, ZM ROADMAP, art / VFX Slack channels, contacts lookup).
- [x] L9 authority dismissal time-anchored Friday 2026-02-27, clear of the today-is-Saturday weekend-comms rule.
- [x] No lever design references Snowflake / Confluence / Airtable / QuickBooks / Firebase / BigQuery / wiki / knowledge base / analytics warehouse (V5 retired).
- [x] No lever requires gmail send / reply / compose / draft (HG gmail is read-only, and unlike StarPM has no `create_draft` either — oracle's initial density projection corrected).
- [x] No em-dashes in the plan.

## Discrepancies surfaced
1. **Oracle proposed 3 gmail `create_draft` calls in the density projection.** HarmonyGames Gmail catalog contains ZERO write / send / reply / compose / draft tools (weaker than StarPM). Corrected in the density projection: the 3 gmail calls have been reallocated to GDocs `create_document` + GSheets `create_spreadsheet`, both of which fit Victor's status-brief and vendor-tracker deliverables and are supported by the HG tool catalog. New midpoint 54 (down from oracle's 57).
2. **Persona ACL implication flagged for S1:** Victor is Engineering. ZM channels (`zombie-art` C08R8CHB0QL, `zm-animations` C09ATAJ220H, `combofighter-vfx` C0AA36TV9QA) are ART / Zombie-team channels. Persona brief lists Ozhan (freelance animator) in Victor's open threads, suggesting ZM is in scope, but this must be verified with `check_persona_acl.py` at S1 before writing any rubric anchored on those channels. If ACL blocks ZM reads for Victor, drop those channels from lever placement and re-anchor on the god-* channels only (still viable per `god-gameart` / `god-vfx` inclusion).

   **RESOLVED 2026-08-12.** Executed early on operator direction. `check_persona_acl.py` returned 0 findings on ACL-3 / ACL-4 (registry + roster hygiene). Per-channel membership scan against `slack.channels.json`: **Victor Barnes (`EMPLOYEE_0030_SLACK_ID`) is a member of zero channels of any type (public / private / archived / DMs / mpim), across all 985 channels.** The god-* fallback path in the original flag is also blocked (`#god-gameart` private 3 members, `#god-vfx` private 4 members and archived, `#leapblock` private 3 members — Victor in none). Slack dropped from lever anchoring entirely (reads AND writes). All 5 selected levers re-anchored on unscoped services (GitHub / Trello / Linear / Contacts) + Victor-owned Drive assets; every lever preserved; density re-projected 54 -> 56 midpoint across 7 services; Slack removed from breadth table, GDrive added. See `Hardness_Plan.md` section `## Lever changes from ACL re-verification` for the row-by-row diff.
3. **Slack `messages/` not in per-task split.** Base-export access exists but per-task split does not enumerate messages, so L3 / L5 (missing reply / thread-reply blindness) are `partial` — a specific decoy-parent-plus-flip-reply pair must be verified against the base export before S1 if the plan needs another lever. Held in reserve; not required for the 40+ density target.
