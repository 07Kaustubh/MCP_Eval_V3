# AUDIT prompt — REVIEW3 corrected bundle

Subject: `Tasks/30_6a3de5194c34125ef86fb36f/_aux/Scratch_Corrected/5_Prompt.txt` (mirror of `_aux/REVIEW_prompt_draft.txt`)
Audit policy: STRICTEST interpretation; 5/5 bar; "should" = "must".
Re-audit driver: REVIEW2 OVERTURNED the prior `AUDIT_prompt.md` PASS (STRICT) verdict on the basis that rubric #5 hidden trap (JE-in-subject) was not surfaced by the prompt (Council_Protocol B6 propagation). Operator applied Row 8 (prompt re-frame) + Row 12 (precedent nudge). This audit re-scores the re-framed prompt under strictest interpretation.

## Per-sub-dim scoresheet

| Sub-dim | Score (1-5) | Citation | One-line reason |
|---|---:|---|---|
| P1 Feasibility (every ask lands on a real tool family) | 5 | `Scratch_Corrected/5_Prompt.txt:1-7` vs `Brookfield_Base_Universe/8_Server_Tools_Details.json` Records Vault + email + slack + reminder + oracle_gl servers | All asks resolve to real tool families: ledger lookup, reminder lookup, Records Vault upload, Slack thread post, email send. |
| P2 Unique ground truth end-state | 5 | `Scratch_Corrected/6_Oracle_Events.txt` OE01-OE09 | Deterministic close-out trajectory: read JE-acme_cloud-FP-2026-04-0052, delete reminder_scen_041_audit_compliance_0000, retrieve precedent memo content, upload one disposition memo with AICPA_SQMS_7Y / restricted, threaded reply on ts 1776969000.000000, email Matthew + Steven cc Farah. |
| P3 Persona-business-function fit | 5 | `Scratch_Corrected/2_Persona.txt` + `_aux/Universe_Split/email.emails.json` (marina.soko@brookfieldcpas.com) | Marina Soko (Compliance Officer) operating in Compliance & Internal Controls; AML housekeeping ahead of partner review is canonical for the role. |
| P4 Coherence (single situation) | 5 | `Scratch_Corrected/5_Prompt.txt:1-7` | Single AML close-out narrative; no bolt-on sub-asks; Row 3 withdrawal kept the prompt focused. |
| P5 Not contrived | 5 | `Scratch_Corrected/5_Prompt.txt:1` ("I'm doing a sweep ... ahead of the partner review") | Pre-partner-review compliance sweep is a routine real-world scenario in Marina's voice. |
| P6 Investigation pre-solved | 5 | `Scratch_Corrected/5_Prompt.txt:2` (Row 2 applied: no $57,077.69, no "late April") + Row 12 OE6 precedent-discovery work | Agent must use the reminder OR period search to locate the JE; agent must download precedent memo content to anchor the new memo. Both raise the discovery cost vs pre-fix prompt. |
| P7 Tool / internal-ID hygiene | 5 | `Scratch_Corrected/5_Prompt.txt` — `grep -nE "oracle_gl\|email_send\|email_search\|slack_conversations\|records_vault\|reminder_\|linear_\|airtable_\|sap_subledger\|blackline_\|messaging_"` → 0 hits; `grep "JE-acme_cloud-FP-2026-04-0052"` → 0 hits | No tool names, no internal IDs, no JE id, no reminder id, no doc id. Natural systems-naming only ("the ledger entry", "the compliance file", "the case thread in #compliance-and-registrations", "the vault"). |
| P8 Truthfulness | 5 | `_aux/Fact_Ledger.json` indexing; `_aux/Universe_Split/email.emails.json` confirms Matthew Li / Steven Perry / Farah Dlamini emails; `_aux/Universe_Split/slack.conversations.json` confirms C008 thread 1776969000.000000 | Every fact in the prompt grounded in `_aux/Universe_Split/`. Row 3's FY26 lever was correctly dismissed because the calibration event is on 2026-06-03 (past universe today 2026-06-12) and the meeting's pre-reads already include the closed monitoring file. |
| P9 Cross-service tool use | 5 | OE coverage spans oracle_gl + email + slack + reminder + records_vault | Five services exercised. Cross-service breadth confirmed. |
| P10 Hardness lever density (P12 in legacy) | 5 | `Scratch_Corrected/5_Prompt.txt:3,6` + `_aux/Council_Reports/REVIEW2_B_consensus.md` Disagreement 1 resolution + Row 8 + Row 12 | THREE independent levers post-iteration: (a) Marina-coordinator-role rubric content (prompt line 3 "I coordinated the CDD package through to clearance with Anita and Steven"); (b) JE-id-in-subject (prompt line 6 "tagging the JE in the subject so they can correlate it against the original alert" — Row 8 fix now adequately surfaces rubric #5); (c) precedent-linkage (prompt line 4 "anchored to the firm's existing AML precedent for this client" — Row 12 nudge surfaces rubrics #25 + #26). Each lever is on a mechanically distinct artifact (memo body / email subject / precedent retrieval), so Hardness_Playbook 3-of-target is met without inventing a fictitious obligation. |
| P11 Em-dash absence + word cap | 5 | `grep -c "—"` → 0; `grep -c "–"` → 0; `wc -w` → 234 | 0 em-dashes, 0 en-dashes, 234 words (well under 500-word cap). |
| P12 Universe data presence | 5 | `_aux/Universe_Split/` cross-checks | All implicit entities (Acme Cloud entity, JE for the April wire, reminder_scen_041, C008 thread, three partner emails, Farah analyst email, Marina sender email) verified present. |

## Findings

- **BLOCKER:** none.
- **MAJOR:** none.
- **MINOR:** none.
- **INFORMATIONAL:**
  - Row 12 precedent-nudge ("anchored to the firm's existing AML precedent for this client") is binding-by-implication for rubrics #25 + #26 (which demand actual download of precedent memo content). A competent Opus-4.8 agent reading "anchored to the firm's existing AML precedent" should naturally retrieve precedent content to write a properly anchored memo. This is materially different from the Row 8 rubric #5 hidden trap (where the rubric demanded a specific subject-line element no prompt language hinted at). Under strictest interpretation the prompt language here is acceptable, but operator should monitor a fresh trajectory run: if 2+ runs satisfy the precedent-reference rubric (#26) without calling `records_vault_download_document_content`, rubric #25 would be ungrounded against the prompt's actual incentive surface and a follow-up prompt sharpening would be warranted (e.g., "review the firm's existing AML precedent for this client before writing").
  - Validator action-verb whitelist convention drift on the OE phase is non-blocking for the prompt audit; surfaced here only for cross-phase awareness.

## Verdict

**PASS (STRICT)**

The Row 8 prompt re-frame ("tagging the JE in the subject so they can correlate it against the original alert") fully discharges the REVIEW2 BLOCKER overturn — rubric #5 (JE-id-in-subject) is now adequately surfaced by the prompt language. The Row 12 precedent nudge surfaces the precedent-anchor expectation that binds rubrics #25 + #26 with reasonable (if implicit) force. All hard-rule gates pass: 500-word cap, em-dash absence, tool-name absence, internal-ID absence, truthfulness sweep, three-lever diversity. Every QC sub-dim scores 5/5 under strictest interpretation. The prompt ships.
