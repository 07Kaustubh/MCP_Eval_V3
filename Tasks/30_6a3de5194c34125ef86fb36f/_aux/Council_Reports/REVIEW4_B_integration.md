# REVIEW4 Integration seat report (B4)

LENS: Integration
SEAT: B4 (Council_Protocol.md §"Opt-in: True multi-model Council B")
SCOPE: Cross-artifact integration of `_aux/REVIEW_prompt_draft.txt` + `14_Updated_Oracle_Events.txt` + `15_Updated_Rubrics.json` + `_aux/REVIEW_persona_draft.txt`.

## Seat verdict

**PASS**

No BLOCKER, MAJOR, or MINOR integration defect remains after Rows 1-13 of `changes.md` are applied to the materialized artifacts. Rubric #5 hidden-trap fix (Row 8), rubric #5 derived-figure-in-title fix (Row 9), rubric #21 body→content parameter fix (Row 10), and rubric #25/#26 over-specificity fix (Row 12 + Row 13) are all present and intra-file consistent. One INFORMATIONAL note on records-vault content parameter naming convention is logged but does not warrant REVISE under Council_Protocol B2.

## Rubric → OE → Prompt traceability matrix

| Rubric # | Title (truncated) | Backing OE | Motivating prompt phrase | Status |
|---|---|---|---|---|
| 1 | Memo documents GL/CDD consistency finding | OE07 (upload memo) + OE01 (JE lookup feeds the finding) | "check that the cash posting lines are consistent with the documented CDD rationale" | **OK** |
| 2 | Delete overdue AML monitoring reminder | OE04 (delete) + OE03 (discovery) | "If anything is still sitting open, reminders…please take care of it" | **OK** |
| 3 | Upload new AML clearance disposition memo | OE07 + OE05 (gap discovery) | "documentation gaps, anything that hasn't been properly put to bed, please take care of it" | **OK** |
| 4 | Memo title names client (Acme Cloud) + AML/compliance subject | OE07 (`title` param) | "this type of AML file" + "the Acme Cloud AML file" + "fully closed out" (filing-craft inference, justification grounded in audit-retrievability — not a hidden trap; B2-OK) | **OK** |
| 5 | Email subject includes JE identifier | OE09 (`subject` param) | "drop Matthew and Steven a quick email **tagging the JE in the subject** so they can correlate it against the original alert" | **OK — Row 8 fix verified present in prompt line 6** |
| 6 | `retention_policy_code` = `AICPA_SQMS_7Y` | OE07 (`retention_policy_code` param) | "whatever retention and classification treatment is appropriate for this type of AML file, **anchored to the firm's existing AML precedent for this client**" — telegraphed via OE06 precedent download; precedent memos (BO Refresh / AML Risk Assessment) carry `AICPA_SQMS_7Y`, agent replicates the enum value via OE06→OE07 chain | **OK (B2-acceptable: prompt delegates + precedent anchor telegraphs the enum)** |
| 7 | `classification` = `restricted` | OE07 (`classification` param) | Same precedent-anchor phrase as #6; AML files with beneficial-ownership data are `restricted` per firm-standard pattern surfaced by OE06 download of the AML Risk Assessment Memo | **OK (B2-acceptable: same telegraph mechanism as #6)** |
| 8 | Memo references verified ledger entry ($57,077.69 / April 2026 / Acme Cloud / JE id) | OE07 (memo content) + OE01 (provides the JE data) | "pull up the ledger entry" | **OK** |
| 9 | Memo includes CDD clearance rationale | OE07 (memo content) + OE02 (clearance trail provides the rationale text) | "documented CDD rationale" | **OK** |
| 10 | Memo identifies analyst stage (Farah) | OE07 (memo content) + OE02 (clearance trail) | "Farah ran the analyst pass" | **OK** |
| 11 | Memo identifies supervisory stage (Anita Knowles) | OE07 (memo content) + OE02 | "I coordinated the CDD package through to clearance with Anita and Steven" | **OK** |
| 12 | Memo identifies partner clearance (Steven Perry) | OE07 (memo content) + OE02 | "with Anita and Steven" + Steven's partner role grounded via persona scope | **OK** |
| 13 | Memo identifies CDD coordination stage (Marina Soko) | OE07 (memo content) + OE02 | "I coordinated the CDD package through to clearance" (Marina = persona "I") | **OK — Lever 1 preserved; persona's "I" maps to Marina via 2_Persona** |
| 14 | Slack threaded reply in C008 with thread_ts 1776969000.000000 | OE08 (`channel_id`, `thread_ts` params) | "post a brief recap **under the case thread** in **#compliance-and-registrations**" (C008 = #compliance-and-registrations per AGENTS.md universe constants) | **OK** |
| 15 | Slack post confirms positive GL verification outcome | OE08 (`payload`) | "covering **what you found**" | **OK** |
| 16 | Slack post references reminder dismissal | OE08 (`payload`) | "covering what you found and **what was actioned**" | **OK** |
| 17 | Slack post references memo filing | OE08 (`payload`) | "what was actioned" | **OK** |
| 18 | Email to Matthew Li (matthew.li@brookfieldcpas.com) | OE09 (`recipients`) | "drop **Matthew** and Steven a quick email" | **OK** |
| 19 | Email to Steven Perry (steven.perry@brookfieldcpas.com) | OE09 (`recipients`) | "drop Matthew and **Steven** a quick email" | **OK** |
| 20 | Email CC Farah Dlamini (farah.dlamini@brookfieldcpas.com) | OE09 (`cc`) | "**CC Farah** since she did the analyst work" | **OK** |
| 21 | Email content addresses Acme Cloud compliance close-out | OE09 (`content` param) | "confirming the file is **fully closed on the compliance side**" | **OK — Row 10 fix verified: title says "body of the email" (natural English), evidence says "content parameter" (matches tool sig); zero residual "body" references in evidence field** |
| 22 | Final response confirms GL/CDD consistency | (response rubric; OE01 + OE07 source the finding) | "covering **what you found**" | **OK** |
| 23 | Final response confirms reminder dismissed | (response rubric; OE04 source) | "what was actioned" | **OK** |
| 24 | Final response confirms memo filed | (response rubric; OE07 source) | "what was actioned" | **OK** |
| 25 | Agent retrieves content of existing Acme Cloud AML precedent memo | OE06 (`records_vault_download_document_content`) | "anchored to the firm's existing AML precedent for this client" | **OK — Row 12 prompt nudge + OE06 + Row 13 title-rewrite all verified present** |
| 26 | Memo references existing AML precedent (names prior memo or quotes substantive conclusion) | OE07 (memo content) + OE06 (provides the precedent text) | "anchored to the firm's existing AML precedent for this client" | **OK — Row 13 title-rewrite "naming a prior memo or quoting its substantive conclusion" present, no "at least N"** |

**No orphan rubrics. Every rubric traces to a prompt phrase (verbatim or directly inferential) and is exercised by at least one OE step.**

## OE → Rubric forward coverage

| OE # | Action | Backs rubrics | Status |
|---|---|---|---|
| OE01 | Look up the Acme Cloud JE | #8 (memo references ledger entry), #1 (GL/CDD consistency finding), #22 (final response GL confirmation) | **OK** |
| OE02 | Search emails/Slack for clearance trail | #9 (CDD rationale), #10 (Farah), #11 (Anita), #12 (Steven), #13 (Marina) — provides the source data for every clearance-chain rubric in OE07 | **OK** |
| OE03 | List active reminders | #2 (reminder delete) — provides the `reminder_id` for OE04; without OE03 the agent cannot satisfy #2 | **OK (discovery → write chain)** |
| OE04 | Delete the stale reminder | #2 (`reminder_delete_reminder` with exact `reminder_id`), #16 (Slack reminder-dismissal recap), #23 (final response reminder confirmation) | **OK** |
| OE05 | List Records Vault docs | #3 (upload memo) — establishes the documentation gap that motivates the upload; #25 (precedent retrieval) — surfaces the two precedent doc_ids; #26 (memo references precedent) — agent must know precedent docs exist before referencing them | **OK (discovery → write chain)** |
| OE06 | Download precedent memo content | #25 (records_vault_download_document_content with target doc_id), #26 (memo references precedent — provides the text the memo will cite), #6 (retention enum — agent reads the precedent's `AICPA_SQMS_7Y` and replicates), #7 (classification enum — agent reads `restricted` and replicates) | **OK** |
| OE07 | Upload disposition memo | #1, #3, #4, #6, #7, #8, #9, #10, #11, #12, #13, #26 (12 rubrics) — the heaviest-loaded OE; covers consistency finding, write action, title, retention, classification, ledger reference, CDD rationale, four clearance-chain identifications, precedent linkage | **OK** |
| OE08 | Slack threaded recap | #14 (channel + thread_ts), #15 (GL verification recap), #16 (reminder-dismissal recap), #17 (memo-filing recap) | **OK** |
| OE09 | Send close-out email | #5 (subject contains JE id), #18 (Matthew), #19 (Steven), #20 (Farah CC), #21 (content addresses close-out), #24 (final response memo confirmation indirectly) | **OK** |

**No orphan OEs. Every OE either directly satisfies a rubric or is a required discovery step in a chain ending at a write-action rubric.**

## Parameter / tool consistency check

| Rubric # | Named parameter / tool | OE-stated parameter / tool | 8_Server_Tools_Details.json (per AGENTS.md universe constants) | Match |
|---|---|---|---|---|
| 2 | `reminder_delete_reminder` + `reminder_id=reminder_scen_041_audit_compliance_0000` | OE04: `reminder_delete_reminder`, `reminder_id="reminder_scen_041_audit_compliance_0000"` | tool exists; param `reminder_id` is the documented sig | **MATCH** |
| 4 | `records_vault_upload_document` + `title` param | OE07: `records_vault_upload_document`, `title=...` | tool exists; `title` is the documented sig | **MATCH** |
| 5 | `email_send_email` + `subject` param | OE09: `email_send_email`, `subject` | tool exists; `subject` is documented sig | **MATCH** |
| 6 | `records_vault_upload_document` + `retention_policy_code=AICPA_SQMS_7Y` | OE07: `retention_policy_code="AICPA_SQMS_7Y"` | tool + param exist; enum value `AICPA_SQMS_7Y` is in the AGENTS.md valid list ("`AICPA_SQMS_7Y`, `IRS_TAX_7Y`, `FIRM_INTERNAL`, `INDEFINITE`") | **MATCH** |
| 7 | `records_vault_upload_document` + `classification=restricted` | OE07: `classification="restricted"` | tool + param exist; enum value `restricted` is in the AGENTS.md valid list ("`internal`, `restricted`, `public`") | **MATCH** |
| 14 | `slack_conversations_add_message` + `channel_id=C008` + `thread_ts=1776969000.000000` | OE08: same | tool + params exist; payload uses `payload` (not `text`) per AGENTS.md trap, and rubric #15/#16/#17 evidence correctly says "payload parameter" | **MATCH** |
| 15-17 | `slack_conversations_add_message` `payload` param | OE08: `payload` | AGENTS.md: "Slack uses `payload` (not `text`)" — correct | **MATCH** |
| 18-20 | `email_send_email` `recipients` / `cc` | OE09: same | tool + params exist; emails are valid sender/recipient/cc strings | **MATCH** |
| 21 | `email_send_email` `content` param (evidence field, post-Row-10 fix) | OE09: `content` | AGENTS.md: "email + messaging use `content` (not `body`)" — correct | **MATCH (Row 10 fix verified; no residual "body" reference in rubric #21 evidence; no other rubric reuses "body" for email content)** |
| 25 | `records_vault_download_document_content` + `document_id` (doc_fb028c9124e146c5 or doc_38a8236a0c4546e2) | OE06: `records_vault_download_document_content`, `document_id="doc_fb028c9124e146c5"` and/or `document_id="doc_38a8236a0c4546e2"` | tool name exact match per Row 12 verification footnote ("NOT records_vault_get_document_content — does not exist") | **MATCH** |
| 1, 3, 8, 9, 10, 11, 12, 13, 26 | `records_vault_upload_document` "content parameter" (evidence) | OE07: `content_b64` (tool sig per OE Parameters block) | Tool sig is `content_b64` (base64-encoded body). Rubrics use the natural-English phrase "content parameter" referring to the decoded content data, not the literal parameter token. | **INFORMATIONAL** — see Findings |

**No tool-name drift. No parameter-name drift on email / slack / reminder / records-vault-list / records-vault-download / records-vault-upload tool/param/enum fields tested by rubrics. The only `content` vs `content_b64` artifact is the conventional naming-shorthand on the upload-memo content rubrics — see INFORMATIONAL note below.**

## Persona-prompt-OE-rubric alignment on Marina's role

| Artifact | Marina's role |
|---|---|
| `_aux/REVIEW_persona_draft.txt` (Row 7 extension) | "Marina Soko, Compliance Officer, marina.soko@brookfieldcpas.com, Supervisor: Anita Knowles, Scope: AML monitoring, CDD case management, retention/classification of compliance records" |
| `_aux/REVIEW_prompt_draft.txt` | "Farah ran the analyst pass and **I coordinated the CDD package through to clearance with Anita and Steven**" (Marina = persona "I") |
| `14_Updated_Oracle_Events.txt` OE07 | "the full clearance chain identifying Farah Dlamini (AML analyst), **Marina Soko (CDD package coordinator)**, Anita Knowles (supervisory officer), and Steven Perry (engagement partner)" |
| `15_Updated_Rubrics.json` rubric #13 | "identifies the CDD package coordination stage of the AML clearance, specifically **Marina Soko's assembly and routing of the clearance package**, or an equivalent description of the coordinating officer role" |

**Aligned across all four artifacts.** The persona is fully consistent with the prompt's first-person voice, OE07's clearance chain reconstruction, and rubric #13's grader requirement. Marina = persona = "I" = CDD coordinator = clearance chain position between analyst (Farah) and supervisory (Anita). The Row 6 evidence tightening with pass/fail examples ("Pass: 'Marina Soko (CDD coordinator)'... Fail: 'Prepared by Marina Soko'...") freezes the grader semantics against permissive drift.

## Findings

- **BLOCKER**: none.
- **MAJOR**: none.
- **MINOR**: none.
- **INFORMATIONAL**:
  - **Records-vault upload memo "content" naming convention.** Nine rubrics (#1, #3, #8, #9, #10, #11, #12, #13, #26) refer to "the content parameter of the records_vault_upload_document call". The tool's actual parameter name per `8_Server_Tools_Details.json` and OE07's Parameters block is `content_b64` (base64-encoded). This is **not** the same defect class as Row 10's email body→content fix: in Row 10 the verifier needed to match against the literal `content` parameter token because `email_send_email` uses `content` (and the rubric incorrectly said "body"). Here, no rubric is asserting a literal parameter-name match; the evidence reads naturally as "the content [that the agent passes] to the upload call". A reasonable verifier base64-decodes `content_b64` and checks the decoded text against the evidence criteria. This convention is consistent with V3 reference tasks (Task11-14 use the same "content parameter" shorthand for `records_vault_upload_document` rubric evidence). No action required. If a future strict-literal verifier is introduced, the rubric could be tightened to "the decoded `content_b64` payload of the records_vault_upload_document call" — but doing so now would diverge from V3 convention without an upstream rule-change to motivate it. Cited rule: Council_Protocol B2 over-specificity threshold ("rubric is over-specific OR the prompt has a second valid reading") is not crossed; the rubrics describe the substantive content requirement, not the parameter-name literal.

## Reasoning

### 1. Rubric #5 hidden-trap re-verification (Row 8 BLOCKER fix)

REVIEW2 flagged rubric #5 (email subject contains JE id) as a hidden trap because the original prompt's email instruction was "drop Matthew and Steven a quick email confirming the file is fully closed on the compliance side, CC Farah". Row 8 re-framed the prompt to: "drop Matthew and Steven a quick email **tagging the JE in the subject so they can correlate it against the original alert**, confirming the file is fully closed on the compliance side, CC Farah since she did the analyst work."

Verifying against `_aux/REVIEW_prompt_draft.txt` line 6 in the materialized draft: the phrase "tagging the JE in the subject so they can correlate it against the original alert" is present verbatim. The agent is now explicitly directed to put the JE id in the subject line; the rubric's evidence requirement ("subject parameter ... contains the JE identifier JE-acme_cloud-FP-2026-04-0052 or an unambiguous equivalent") is no longer a hidden trap — it is a direct fulfillment of the prompt's "tagging the JE in the subject" instruction. **Row 8 fix verified.** Council_Protocol B6 propagation requirement ("fix the issue at the phase where the root cause lives, then re-run downstream phases") satisfied: the root-cause re-frame happened in the prompt, not as a silent rubric edit.

### 2. Rubrics #6 and #7 B2 over-specificity test

Both rubrics hardwire specific enum values (`retention_policy_code=AICPA_SQMS_7Y`, `classification=restricted`) against a prompt that delegates the choice ("whatever retention and classification treatment is appropriate for this type of AML file"). Under a naive B2 read this would be over-specific. However:

- The prompt's full clause is "appropriate for this type of AML file, **anchored to the firm's existing AML precedent for this client**" — the Row 12 nudge added the precedent-anchoring instruction explicitly.
- OE06 directs the agent to download the FY2026 BO Refresh and FY2026 AML Risk Assessment Memo. Both precedent memos are stored with `retention_policy_code=AICPA_SQMS_7Y` and `classification=restricted` (the AML-pattern firm-standard).
- The agent therefore arrives at the correct enum values by replicating the precedent's metadata, which the prompt explicitly instructs.
- Council_Protocol B2 over-specificity test fails only if a valid agent path exists that satisfies the prompt's intent (precedent-anchored choice) but produces a different enum value. No such path exists when the precedent metadata is `AICPA_SQMS_7Y` / `restricted`.

**Rubrics #6 and #7 pass B2 because the precedent-anchor clause is the telegraph mechanism, not a hidden trap.** The agent does not need to guess; it reads OE06's precedent metadata.

### 3. Rubric #21 body→content re-verification (Row 10 BLOCKER fix)

Row 10 directed: "Replace all three 'body' occurrences in rubric #21 evidence with 'content'". Verifying the materialized `15_Updated_Rubrics.json` rubric #21:

- Title: "The Agent addresses the Acme Cloud compliance close-out **in the body of the email** sent to the engagement partners…" — "body of the email" is natural-English usage, not a literal parameter-name claim. Acceptable per Row 10's note ("title unchanged — 'body of the email' as natural English is correct").
- Evidence: "The **content parameter** of the email_send_email call references the Acme Cloud compliance file and conveys a close-out or confirmation message. An email **content** that is unrelated to the Acme Cloud compliance matter does not pass. Exact wording is not required; any **content** that clearly pertains to the compliance file close-out qualifies."

All three evidence occurrences of "body" have been replaced with "content" per AGENTS.md's parameter-trap rule ("email + messaging use `content` (not `body`)"). I additionally grepped the full rubric file for residual "body" references against email_send_email — zero hits. The Row 10 fix is fully applied and intra-file consistent.

### 4. Rubric #25 / #26 "at least N" re-verification (Row 13 BLOCKER fix)

Row 13 directed: rubric #25 title rewrite from "retrieves the content of **at least one** existing Acme Cloud AML precedent memo" to "retrieves the content of **an existing** Acme Cloud AML precedent memo (either the Beneficial Owner Refresh or the AML Risk Assessment)" — and rubric #26 title rewrite from "**naming at least one prior memo**" to "**naming a prior memo**".

Verifying the materialized `15_Updated_Rubrics.json`:

- Rubric #25 title: "The Agent retrieves the content of **an existing** Acme Cloud AML precedent memo (either the Beneficial Owner Refresh or the AML Risk Assessment) from the Records Vault." ✓ No "at least N".
- Rubric #26 title: "The Agent's disposition memo references the firm's existing AML compliance precedent for Acme Cloud, **naming a prior memo or quoting its substantive conclusion**." ✓ No "at least N".

AGENTS.md hard rule #6 satisfied. Evidence fields on both rubrics still name both precedent docs (BO Refresh + AML Risk Assessment) as acceptable targets, preserving the disjunction without the title-level "at least N" violation.

### 5. Hardness lever count and end-to-end preservation

Hardness_Plan / changes.md Row 11 documents three levers post-Row-12:
- **Lever 1**: Marina-coordinator-role in memo content (rubric #13).
- **Lever 2**: JE-id in email subject line (rubric #5).
- **Lever 3**: Precedent-linkage in memo content + precedent-content retrieval (rubrics #25 + #26).

Each lever is end-to-end traceable through prompt → OE → rubric:

- **Lever 1**: prompt's "I coordinated the CDD package through to clearance" → OE02 (clearance trail) + OE07 (memo must identify Marina by name + coordinator role) → rubric #13 (with Row 6 pass/fail examples freezing the grader).
- **Lever 2**: prompt's "tagging the JE in the subject" (Row 8) → OE09 (subject references JE id) → rubric #5 (Row 9 title-rewrite to satisfy FINAL.md no-derived-figure-in-title rule).
- **Lever 3**: prompt's "anchored to the firm's existing AML precedent for this client" (Row 12 nudge) → OE06 (download precedent content) + OE07 (memo references precedent) → rubrics #25 + #26 (Row 13 title-rewrite).

All three levers preserved end-to-end. Council_Protocol B4 hardness preservation: PASS.

### 6. Channel + thread_ts + email recipient + precedent doc_id consistency

All four are pin-checked against the corresponding OE Parameters block AND the AGENTS.md universe-constants table where applicable:

- **C008 / #compliance-and-registrations**: AGENTS.md universe constants line "C008 #compliance-and-registrations" ✓; OE08 `channel_id="C008"` ✓; prompt "#compliance-and-registrations" ✓; rubric #14 `channel_id=C008` ✓.
- **thread_ts 1776969000.000000**: OE08 `thread_ts="1776969000.000000"` ✓; rubric #14 same ✓. (Prompt does not name the timestamp by design — agent discovers via OE02 clearance-trail search.)
- **Email recipients**: prompt "Matthew and Steven … CC Farah" ✓; OE09 recipients=[matthew.li, steven.perry], cc=[farah.dlamini] ✓; rubrics #18 / #19 / #20 each name one of the three with correct email address ✓.
- **Precedent doc_ids**: OE06 `document_id="doc_fb028c9124e146c5"` (BO Refresh) and `document_id="doc_38a8236a0c4546e2"` (AML Risk Assessment) ✓; rubric #25 evidence names both with identical doc_ids ✓. The doc_ids are verified present in `_aux/Universe_Split/records_vault.rv_documents.json` per Row 12's verification footnote.

### 7. Persona-prompt-OE-rubric quadruple alignment

Persona draft says Marina is Compliance Officer with email marina.soko@brookfieldcpas.com and supervisor Anita Knowles. The prompt is written in first-person voice ("I coordinated the CDD package through to clearance with Anita and Steven"), so "I" = Marina = compliance officer. OE07 identifies Marina explicitly as "CDD package coordinator", which matches the persona's CDD-case-management scope and the prompt's first-person coordination claim. Rubric #13 grades on Marina being identified by name OR role description ("CDD coordinator", "coordinating officer") in memo body — consistent with the prompt's narrative and OE07's expectation. The Row 6 evidence pass/fail examples freeze the grader against permissive drift on this lever.

Anita Knowles appears in: persona ("Supervisor: Anita Knowles"), prompt ("clearance with Anita and Steven"), OE02 (Anita's supervisory sign-off in the clearance trail), OE07 (Anita Knowles in clearance chain), rubric #11 (supervisory stage identifies Anita Knowles). Fully consistent.

Steven Perry appears in: prompt ("with Anita and Steven"), OE02 (Steven's partner sign-off), OE07 (Steven Perry as engagement partner), OE09 (steven.perry@brookfieldcpas.com as email recipient), rubrics #12 (partner stage) and #19 (email recipient). Fully consistent.

Farah Dlamini appears in: prompt ("Farah ran the analyst pass" + "CC Farah"), OE02 (Farah's analyst findings), OE07 (Farah Dlamini as AML analyst in clearance chain), OE09 (farah.dlamini@brookfieldcpas.com on cc), rubrics #10 (analyst stage) and #20 (cc recipient). Fully consistent.

Matthew Li appears in: prompt ("drop Matthew and Steven a quick email"), OE09 (matthew.li@brookfieldcpas.com on recipients), rubric #18 (email recipient). Persona does not need to mention Matthew because he is a downstream recipient, not part of Marina's named workflow. No drift.

### 8. AGENTS.md universe-constants compliance

Spot-check of universe-constants AGENTS.md exposes:
- **Account-number trap**: account 101000 ("Cash - Operating") in OE01 — this is Brookfield-firm cash, but here it's described as Acme Cloud's Cash - Operating. Acme Cloud is a client entity (SaaS), and per AGENTS.md the cash account-number trap warns about `105000` having different roles per entity. Account 101000 is not in the trap list, so no per-entity drift. The JE id format `JE-acme_cloud-FP-2026-04-0052` follows V3 convention ✓. Period id `acme_cloud_FP-2026-04` follows convention ✓.
- **JE lifecycle**: OE01 retrieves a "posted" JE — no closed-period write requested, no `late_post_authorization_id` invoked. Compliant.
- **Retention codes**: `AICPA_SQMS_7Y` is in the valid set per AGENTS.md ("`AICPA_SQMS_7Y`, `IRS_TAX_7Y`, `FIRM_INTERNAL`, `INDEFINITE`"). Compliant.
- **Classifications**: `restricted` is in the valid set ("`internal`, `restricted`, `public`"). Compliant.
- **Slack channel**: C008 = `#compliance-and-registrations` ✓.
- **Parameter traps**: email uses `content` (rubric #21 post-Row-10), slack uses `payload` (rubrics #15/#16/#17 evidence). Compliant.

### 9. Today vs horizon check

Universe today is 2026-06-12 (per AGENTS.md "Universe today: 2026-06-12"). Reminder due 2026-05-02 is overdue (~6 weeks past today) — consistent with the prompt's "still sitting open" language and OE03's "overdue" framing. JE posted 2026-04-22 is ~7 weeks in the past — consistent with prompt's "earlier this quarter" framing. No date drift. Universe-current date (today's 2026-06-27 per session context) does not affect this task — the per-task universe today (2026-06-12) is the SSOT per AGENTS.md hard rule #2.

### 10. Final integration verdict

Every rubric traces to a backing OE step AND a motivating prompt phrase (verbatim or directly inferential). Every OE either directly satisfies a rubric or is a required discovery step in a chain ending at a write-action rubric. All parameter names match the tool inventory (with one V3-conventional naming-shorthand on records_vault upload "content parameter" that is consistent with reference tasks and below B2 over-specificity threshold). Persona, prompt, OE, and rubric are aligned on Marina's role and the full clearance chain. Channel + thread_ts + email recipients + precedent doc_ids are pin-consistent across all three artifacts. Hardness levers 1-3 are preserved end-to-end with no regression. Rows 8, 9, 10, 12, 13 fixes are all applied and intra-file consistent.

**Seat verdict: PASS.**

## Cited rules engaged

- **Council_Protocol.md B2 (Adversarial alt-path / over-specificity)** — applied to rubrics #6, #7 (B2 telegraph test via precedent anchor) and to the records_vault "content parameter" shorthand (B2 over-specificity threshold not crossed).
- **Council_Protocol.md B6 (Upstream propagation)** — applied to verify Row 8's prompt re-frame fixed rubric #5 at the prompt root cause (not silently patched downstream).
- **Council_Protocol.md B4 (Hardness preservation)** — applied to verify all three levers (Marina-coordinator / JE-id-in-subject / precedent-linkage) are still end-to-end triggered.
- **Council_Protocol.md Integration lens** — applied across all 26 rubrics + 9 OEs for cross-artifact consistency.
- **AGENTS.md hard rule #6** — applied to rubrics #25, #26 to verify Row 13 title rewrite eliminated "at least N".
- **AGENTS.md hard rule #7** — applied to verify no tool names appear in rubric titles (rubrics referencing `records_vault_upload_document`, `email_send_email`, etc. mention tools only in evidence/justification fields).
- **AGENTS.md parameter-trap rules** — applied to verify email `content` (rubric #21), slack `payload` (rubrics #15/#16/#17), reminder `reminder_id` (rubric #2), and records-vault enum values.
- **AGENTS.md universe-constants table** — applied to channel C008 mapping, retention enum set, classification enum set, JE lifecycle, period id format.
- **Reference/Sessions/FINAL.md hard-rules table** — applied to verify rubric #5 title rewrite (Row 9) eliminated the verbatim derived figure (JE id stays in evidence, not title).

---

**End of REVIEW4 Integration seat report.**
