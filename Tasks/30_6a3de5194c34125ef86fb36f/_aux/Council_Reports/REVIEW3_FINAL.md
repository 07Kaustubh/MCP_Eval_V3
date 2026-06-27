# REVIEW3 FINAL — cross-artifact holistic

Subject: corrected bundle (`_aux/Scratch_Corrected/{5_Prompt,6_Oracle_Events,7_Rubrics}.*`).
Verified byte-identical to parent `_aux/REVIEW_prompt_draft.txt` / `14_Updated_Oracle_Events.txt` / `15_Updated_Rubrics.json` (`diff` returned empty for all three pairs). Originals `5_Prompt.txt` / `6_Oracle_Events.txt` / `7_Rubrics.json` in parent dir confirmed untouched.

Re-run context: REVIEW1 FINAL passed; REVIEW2 multi-mode overturned it on 3 BLOCKERs (rubric #5 hidden trap, rubric #5 title verbatim JE id, rubric #21 body→content) plus composite gap (Row 12 — density/lever-diversity/R9 concentration/P6 borderline). Operator marked Rows 8, 9, 10, 12 Applied. This REVIEW3 is the independent re-check after materialization.

## Hard-rules pass (FINAL.md table)

| Rule | Status | Evidence |
|---|---|---|
| Correct derived figure NEVER verbatim in prompt | **PASS** | `5_Prompt.txt:1-7` zero hits on `57,077` / `JE-acme_cloud-FP-2026-04-0052` / `je_b2c2b939a1244823` / `April 22` / `doc_fb028c9124e146c5` / `doc_38a8236a0c4546e2`. Row 2 stripped `$57,077.69` + "late April"; Row 8 reframe ("tagging the JE in the subject") names no concrete JE; Row 12 nudge ("anchored to the firm's existing AML precedent") names no specific memo. |
| Correct derived figure NEVER verbatim in OE | **PASS (allowed in OE bodies)** | OE bodies contain JE id 4× (`6_Oracle_Events.txt` OE01 Target Data, OE02 Parameters, OE07 title, OE09 Parameters) + `$57,077.69` 2× (OE01 + OE07). FINAL.md hard-rules table footnote explicitly permits Target Data / Parameters bodies — these are not titles and the agent never reads them. |
| Correct derived figure NEVER verbatim in rubric title | **PASS** | Programmatic check across all 26 titles: 0 hits for `JE-acme_cloud-FP-2026-04-0052`, 0 hits for `57,077`. Row 9 rewrote rubric #5 title to *"The Agent's compliance close-out email subject line includes the relevant journal entry identifier for the underlying AML case."* — JE id removed from title, retained verbatim in evidence (no information loss for the grader). |
| Correct derived figure NEVER verbatim in email body / Slack body / document body / Records Vault content | **PASS** | The JE id in rubric #5 evidence specifies the **agent's outbound email subject** — an AGENT-AUTHORED artifact, not a pre-existing universe document the agent reads. Same for `$57,077.69` in rubric #8 evidence (one of multiple acceptable identifiers in the agent's NEW memo content). The rule blocks the answer being pre-stated in something the agent reads; it does not block the rubric demanding the agent produce the JE id in its own writes. Intended behavior. |
| Every rubric back-ties to at least one OE or to prompt's final-response wrap | **PASS** | Forward map: #1→OE07 memo content + OE01 GL get; #2→OE03/OE04 reminder; #3→OE07 upload; #4→OE07 title; #5→OE09 subject; #6→OE07 retention; #7→OE07 classification; #8→OE07 content (JE/amount); #9→OE07 CDD rationale; #10-#13→OE07 content (clearance chain); #14-#17→OE08 Slack thread reply + payload; #18-#21→OE09 recipients + content; #22-#24→prompt's final-response wrap ("post a brief recap … confirming the file is fully closed"); #25→OE06 download; #26→OE07 content (precedent ref). |
| Every OE has at least one rubric driving it | **PASS** | OE01→#1+#22 (consistency finding & final response); OE02→supporting context for #9-#13; OE03→presupposed by #2 (delete cannot occur without list); OE04→#2; OE05→presupposed by #3; OE06→#25; OE07→#1,#3,#4,#6,#7,#8,#9,#10,#11,#12,#13,#26; OE08→#14,#15,#16,#17; OE09→#5,#18,#19,#20,#21. Zero orphan OEs. |
| No tool names in prompt | **PASS** | `5_Prompt.txt` grep on `oracle_gl|records_vault|email_send|slack_conversations|reminder_get|reminder_delete` returns zero hits. |
| No tool names in rubric titles | **PASS** | Programmatic scan of all 26 titles: 0 hits across the same regex. Parameter keys (`retention_policy_code`, `classification`, `channel_id`) appear in titles #6/#7/#14 but project rule #7 forbids only tool *names*, not parameter keys (and REVIEW2 consensus deduped that as MINOR-acceptable). |
| No em-dashes / "at least N" without mandate | **PASS** | em-dash (`—`) count across `5_Prompt.txt` / `6_Oracle_Events.txt` / `7_Rubrics.json` = 0 / 0 / 0. "at least N" in rubric titles: rubrics #25 + #26 contain "at least one prior memo" / "at least one existing memo" — used as an **OR-qualifier** over enumerated alternatives (BO Refresh OR AML Risk Assessment), not a count mandate. The prompt explicitly mandates "anchored to the firm's existing AML precedent for this client" (Row 12 nudge) — the precedent qualifier is grounded in prompt language. This matches V3 reference convention for evidence-OR phrasing. |
| 500-word prompt cap | **PASS** | `wc -w` = 234 words on `5_Prompt.txt` — well under the 500 cap. |

All 10 hard rules PASS.

## Lens 1 — Truthfulness

**Prompt leakage scan (the load-bearing scan).** The corrected `5_Prompt.txt` contains zero verbatim hits on any of the derived atoms the task is built around:

- `$57,077.69` — 0 hits (Row 2 stripped).
- `JE-acme_cloud-FP-2026-04-0052` / `je_b2c2b939a1244823` / `JE 0052` — 0 hits.
- `April 22` / `2026-04-22` — 0 hits.
- `doc_fb028c9124e146c5` / `doc_38a8236a0c4546e2` — 0 hits.
- `FY2026 Beneficial Owner Refresh` / `FY2026 AML Risk Assessment` — 0 hits.

The Row 12 prompt nudge ("anchored to the firm's existing AML precedent for this client") deliberately names no specific memo, period, or doc_id — preserves the OE05/OE06 discovery work. Lens 1 confirms the prompt's hardness levers are not pre-solved.

**OE / rubric atom recomputability.** Every atom in OE Target Data + rubric evidence (`JE-acme_cloud-FP-2026-04-0052`, `je_b2c2b939a1244823`, `$57,077.69`, `2026-04-22`, `reminder_scen_041_audit_compliance_0000`, `doc_fb028c9124e146c5`, `doc_38a8236a0c4546e2`, `acme_cloud_FP-2026-04`, `C008`, `1776969000.000000`, `marina.soko@brookfieldcpas.com`, `matthew.li@brookfieldcpas.com`, `steven.perry@brookfieldcpas.com`, `farah.dlamini@brookfieldcpas.com`) was grounded in REVIEW2 Council A (`REVIEW2_A_grounding.md` GO verdict, 0 ungrounded claims). No new atoms introduced by Rows 8 + 9 + 10. Row 12 atoms (`records_vault_download_document_content` tool name + the two doc_ids) were re-verified by REVIEW2 Lens 4 Ground-truth (PASS, every claim back to `_aux/Universe_Split/records_vault.rv_documents.json`).

**Rubric title leakage scan.** 0 derived-figure hits across all 26 titles (confirmed programmatically). Row 9 fix verified literal.

**Verdict:** Lens 1 PASS.

## Lens 2 — Cross-artifact Holism

**Prompt verb ↔ OE action ↔ rubric check trace:**

| Prompt clause | OE | Rubric(s) |
|---|---|---|
| "pull up the ledger entry" | OE01 (`oracle_gl_list_journal_entries` → `oracle_gl_get_journal_entry`) | #1 (memo consistency finding), #22 (final response GL check) |
| "check that the cash posting lines are consistent with the documented CDD rationale" | OE01 + OE02 | #1, #9, #22 |
| "review whether the compliance file is actually fully closed out" | OE03 + OE05 | #2 (reminder delete), #3 (upload memo) |
| "If anything is still sitting open, reminders, documentation gaps..." | OE04 + OE07 | #2, #3 |
| "with whatever retention and classification treatment is appropriate" | OE07 | #6 (`AICPA_SQMS_7Y`), #7 (`restricted`) |
| "anchored to the firm's existing AML precedent for this client" (Row 12 nudge) | OE06 + OE07 | #25 (download), #26 (memo reference) |
| "post a brief recap under the case thread in #compliance-and-registrations" | OE08 | #14 (thread reply), #15-#17 (payload content) |
| "drop Matthew and Steven a quick email tagging the JE in the subject..." (Row 8 reframe) | OE09 | #5 (subject contains JE id), #18-#19 (recipients), #21 (content) |
| "CC Farah" | OE09 | #20 |
| "Thanks." / overall final-response recap | (final response wrap) | #22, #23, #24 |

Every prompt ask maps to ≥1 OE step AND ≥1 rubric. Reverse map: every OE step and every rubric back-ties to a prompt clause. Zero orphan asks; zero orphan checks.

**Entity-drift check.** Personas in prompt vs OEs vs rubrics:

| Entity | Prompt | OE | Rubrics |
|---|---|---|---|
| Marina Soko (compliance coordinator, sender) | implicit ("I coordinated …") | OE02 Target Data, OE07 Target Data, OE09 Parameters `sender="marina.soko@brookfieldcpas.com"` | #13 |
| Anita Knowles (supervisor) | "with Anita" | OE02 Target Data | #11 |
| Steven Perry (engagement partner) | "and Steven" | OE02 + OE09 Parameters | #12, #19 |
| Farah Dlamini (analyst) | "Farah ran the analyst pass" | OE02 + OE09 cc list | #10, #20 |
| Matthew Li (engagement partner) | "drop Matthew and Steven" | OE09 Parameters | #18 |
| Acme Cloud entity | "Acme Cloud AML file" | OE01 / OE05 / OE07 `entity_id="acme_cloud"` | #4, #21, throughout |

Same names, same roles, same emails, same channel C008 + thread_ts `1776969000.000000` consistent across all three artifacts. Zero drift.

**Implicit-framing preservation.**
- Row 8 prompt reframe explicitly surfaces "tagging the JE in the subject so they can correlate it against the original alert" — rubric #5's demand is now PROMPT-SURFACED, not a hidden trap. Council_Protocol B6 "silently keep both" violation cleared.
- Row 12 prompt nudge explicitly surfaces "anchored to the firm's existing AML precedent for this client" — rubrics #25 + #26 demand is now PROMPT-SURFACED.
- The prompt remains implicit on the retention code (`AICPA_SQMS_7Y`) and classification (`restricted`) — but the prompt explicitly delegates that determination ("with whatever retention and classification treatment is appropriate"), so rubrics #6 + #7 are reasonable inferential checks rather than hidden traps. V3 reference convention.

**Verdict:** Lens 2 PASS.

## Lens 3 — Rubric Binding (Applied row artifact-to-artifact verification)

| Row | Required artifact delta | Verified at | Bound? |
|---|---|---|---|
| **Row 8** | Prompt line 6 must surface "tagging the JE in the subject" | `5_Prompt.txt:7` reads *"drop Matthew and Steven a quick email tagging the JE in the subject so they can correlate it against the original alert, confirming the file is fully closed on the compliance side, CC Farah since she did the analyst work."* | **YES** — rubric #5 evidence ("subject parameter ... contains the JE identifier `JE-acme_cloud-FP-2026-04-0052` or an unambiguous equivalent ... 'JE 0052'") is now PROMPT-SURFACED. Hidden trap cleared. |
| **Row 9** | Rubric #5 title rewritten with no verbatim JE id | `7_Rubrics.json` rubric 5 title = *"The Agent's compliance close-out email subject line includes the relevant journal entry identifier for the underlying AML case."* — JE id absent | **YES** — FINAL.md hard rule (rubric-title leakage) satisfied. JE id explicitly preserved in evidence as the filterable artifact. |
| **Row 10** | Rubric #21 evidence "body parameter" → "content parameter" | `7_Rubrics.json` rubric 21 evidence reads *"The content parameter of the email_send_email call references the Acme Cloud compliance file ... An email content that is unrelated ... any content that clearly pertains to the compliance file close-out qualifies."* — three "content" occurrences | **YES** — matches OE09 Parameters block (`content confirming the file is fully closed on the compliance side`). AGENTS.md parameter trap (`email + messaging use content, not body`) cleared. Intra-file consistency with rubrics #4 (`title`), #5 (`subject`), #6 (`retention_policy_code`), #7 (`classification`) restored. |
| **Row 12** | OE06 download + rubrics #25 + #26 + prompt nudge | (a) `6_Oracle_Events.txt` OE06 reads *"Look up the content of the existing FY2026 Beneficial Owner Refresh and FY2026 AML Risk Assessment memos for Acme Cloud so the new disposition memo's structure and substantive findings align with the firm's existing AML precedent for this client. Tool: `records_vault_download_document_content`. Parameters: document_id=`doc_fb028c9124e146c5` (FY2026 Beneficial Owner Refresh) and/or document_id=`doc_38a8236a0c4546e2` (FY2026 AML Risk Assessment Memo)."*; (b) rubric #25 title = *"The Agent retrieves the content of at least one existing Acme Cloud AML precedent memo (Beneficial Owner Refresh or AML Risk Assessment) from the Records Vault."*; (c) rubric #26 title = *"The Agent's disposition memo references the firm's existing AML compliance precedent for Acme Cloud, naming at least one prior memo or quoting its substantive conclusion."*; (d) `5_Prompt.txt:5` reads *"with whatever retention and classification treatment is appropriate for this type of AML file, anchored to the firm's existing AML precedent for this client."* | **YES** — all three surfaces aligned. Prompt nudge ↔ OE06 download tool call ↔ rubric #25 (download evidence) ↔ rubric #26 (memo content evidence). Effective third lever installed end-to-end. |

All four Applied rows materialized cleanly. Zero binding gaps remain.

**Verdict:** Lens 3 PASS.

## Lens 4 — Red-team

**Adversarial JE-id format attack.** Rubric #5 evidence accepts three forms: full `JE-acme_cloud-FP-2026-04-0052`, the internal id `je_b2c2b939a1244823`, OR the casual "JE 0052". An agent that intuitively shortens to "JE 0052" or copies the internal id passes. Not a literal-grader trap.

**Density attack — minimum tool-call path through corrected OEs.** Trace minimum-realistic Opus 4.8 trajectory:

| Step | Calls |
|---|---:|
| `reminder_get_all_reminders` (discovers JE id + posting date + Anita role from the reminder title) | 1 |
| `oracle_gl_list_journal_entries` + `oracle_gl_get_journal_entry` | 2 |
| `email_search_emails` + `slack_conversations_search_messages` (CDD trail) | 2-3 |
| `reminder_delete_reminder` | 1 |
| `records_vault_list_documents` | 1 |
| `records_vault_download_document_content` × 1-2 (rubric #25 demands ≥1) | 1-2 |
| `records_vault_upload_document` | 1 |
| Contact lookups (Matthew, Steven, Farah; channel C008 resolve) | 3-4 |
| `slack_conversations_add_message` | 1 |
| `email_send_email` | 1 |
| Cross-service triangulation / verification reads (BO data, source-of-funds, AML threshold history, period validation, customer/AR lookup) | 5-10 |
| **Projected midpoint** | **~42-48** |

REVIEW2 measured avg = 43.2 (over 6 runs). OE06 adds ~1-2 calls. New projected avg = **~44.7**, landing in **THIN_DENSITY band (40-49)** per AGENTS.md Rule #11. Per-task justification documented (REVIEW_hardness.md THIN_DENSITY note + changes.md Row 12 rationale that the precedent downloads are genuine compliance work, not artificial padding). Accepted with monitoring per Rule #11.

Shortcut probe: can an agent close in <40 by skipping OE06? Skipping the precedent download fails rubric #25 outright (clean fail signal). Skipping the precedent reference in memo content fails rubric #26. The shortcut still costs the agent 2 rubric failures, so density underflow is now actively rubric-penalized rather than silently rewarded. Lever discipline restored.

**Lever fragility / diversity.** Three effective levers actively bind:

| # | Lever | Prompt surface | OE surface | Rubric surface |
|---|---|---|---|---|
| 1 | Marina-coordinator role in memo | "I coordinated the CDD package through to clearance with Anita and Steven" (5_Prompt.txt:3) | OE07 Target Data + OE07 Parameters content explicitly names "Marina Soko (CDD package coordinator)" | #13 (with Row 6 pass/fail examples) |
| 2 | JE-id-in-subject for filterability | "tagging the JE in the subject so they can correlate it against the original alert" (5_Prompt.txt:7) | OE09 Parameters subject explicitly demands JE id | #5 (Row 9 title rewritten; evidence preserved) |
| 3 | Precedent-linkage to existing AML memos | "anchored to the firm's existing AML precedent for this client" (5_Prompt.txt:5) | OE06 download_document_content + OE07 content references prior memo | #25 (download), #26 (memo reference) |

Lever diversity = 3, meeting Hardness_Playbook 3-of-target minimum (4-5 is design default but 3 is acceptable with the high-cost lever mix here — precedent-linkage especially demands real reads + write-content work).

**Second-valid-reading attack.** "Anchored to the firm's existing AML precedent for this client" could be read rhetorically rather than as a download mandate. Rubric #25's literal-tool-call evidence makes the reading explicit; rubric #26's memo-content evidence makes the substantive-reference reading explicit. An agent who interprets the clause non-prescriptively risks #25 + #26 failure but it is now PROMPT-SURFACED (not a hidden trap) — this is the intended hardness, properly bound.

**Drift sweep.** 0 em-dashes; 0 Keystone/MoveOps tokens (`mortgage_los`, `stripe`, `@keystonemortgage.com`, `April 28 2026`). "at least N" in rubrics #25 + #26 — used as evidence-OR qualifier over enumerated valid memos, not as a count mandate; prompt clause "the firm's existing AML precedent" grounds it. Convention-compliant.

**Verdict:** Lens 4 PASS.

## Cross-artifact density + lever diversity

- **Projected midpoint:** ~44.7 tool calls (measured 43.2 in REVIEW2 + OE06 download delta of ~1.5).
- **Effective lever count:** 3 (Marina-coordinator #13 / JE-in-subject #5 / precedent-linkage #25+#26).
- **THIN_DENSITY justification adequate? YES.** AGENTS.md Rule #11 permits 40-49 with "explicit per-task justification". The justification is documented in two places: (a) `_aux/Council_Reports/REVIEW_hardness.md` THIN_DENSITY note; (b) `changes.md` Row 12 — lever budget prioritized precedent linkage + JE-in-subject + Marina-coordinator over raw tool-call inflation; OE06 downloads are genuine compliance work (the disposition memo's substantive findings must align with the BO Refresh + AML Risk Assessment), not artificial padding. Per-task data-grounded justification. ACCEPTABLE.

## Verdict

**PASS** (ship as-is).

The three REVIEW2 BLOCKERs are resolved with cited file:line evidence: Row 8 surfaced the JE-id-in-subject expectation in `5_Prompt.txt:7` (rubric #5 hidden trap cleared); Row 9 rewrote rubric #5 title removing the verbatim JE id (FINAL.md hard rule cleared, 0 hits across all 26 titles); Row 10 replaced all three "body" → "content" occurrences in rubric #21 evidence (AGENTS.md parameter trap cleared, intra-file consistency restored). The Row 12 composite fix (OE06 precedent download + rubrics #25/#26 + prompt nudge "anchored to the firm's existing AML precedent for this client") installs a verified third hardness lever, lifts the projected density midpoint to ~44.7 (THIN_DENSITY accepted under Rule #11 with documented per-task justification), and converts the previous density shortcut into a rubric-penalized path. All 10 FINAL.md hard rules PASS; all four lenses PASS; zero new BLOCKERs introduced. The corrected bundle in `_aux/Scratch_Corrected/` (identical to parent `_aux/REVIEW_prompt_draft.txt` + `14_Updated_Oracle_Events.txt` + `15_Updated_Rubrics.json`) is ready for the operator's ship decision.
