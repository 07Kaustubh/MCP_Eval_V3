# Council B - Adversarial QC + Density + Hardness Preservation (RE-PASS)

**Phase:** OE (S2)
**Deliverable:** `Tasks/27_6a39fd19048f9213281ec7b/6_Oracle_Events.txt` (24 OEs, corrected)
**Pass context:** RE-PASS after prior Council B BLOCK. Deltas:
1. OE 15 corrected: `blackline_show_data` now described as no-parameter dump with client-side filter on `target_kind="reconciliation"` / `target_id="BL-333FF9956BC6"`.
2. OE 22 corrected: messaging fallback removed; email is sole tool.
3. Prior B6 PROPAGATE concern re-evaluated against the ACTUAL prompt text (the prior pass had quoted a sentence that does not exist in `5_Prompt.txt`).

---

## [B1] QC Sub-Dim Scoring (OE sub-dims)

Per `Docs/7_QC_Spec_Doc1.json` the OE dimension has two sub-dims. Re-scoring after the corrections, with the two prior accuracy concerns re-checked against ground truth.

### OE Completeness: 5

Full critical path covered by 24 OEs:
- Persona self-lookup (OE 1) + period status (OE 2) + open recon (OE 3) + USD-cash grounding (OE 4) + open exception (OE 5).
- Three-service latching: Slack thread (OE 6, 7) + email disposition pair (OE 8) + Blue<->Ryan messaging (OE 9).
- Four-pillar precedent refutation: FP-2025-11 recon (OE 10) + FP-2025-11 feed run status="retried" (OE 11).
- Real-precedent discovery: `blackline_list_exceptions` filtered to brookfield/102000 (OE 12) + exc_d8fc13aa2cc742 read (OE 13) + BL-782A2EC69343 read (OE 14).
- Evidence-chase chain: `blackline_show_data` dump filtered to BL-333FF9956BC6 (OE 15) + both RV docs (OE 16, OE 17).
- Anti-L25 reminder pre-check (OE 18) + George contact resolution (OE 19).
- All four write actions: vault upload (OE 20) + Slack thread post on the precedent-raising message (OE 21) + email direct line to George (OE 22) + chase-before-certify reminder (OE 23).
- Final user-facing response (OE 24).

Every actionable sentence in the prompt has at least one OE step (see B6 FORWARD for line-by-line map). No requirement is uncovered.

### OE Accuracy: 5

Two prior concerns re-checked against ground truth:

**(1) `blackline_show_data` tool name (OE 15)** - VERIFIED. `Brookfield_Base_Universe/8_Server_Tools_Details.json` defines the tool as:
```
{
  "name": "blackline_show_data",
  "description": "Dump all BlackLine state - for debugging.",
  "parameters": []
}
```
Empty parameter list confirmed. OE 15's "no parameters; the call dumps the full BlackLine state, and it is the only surface that exposes the blackline_evidence table since there is no list_evidence tool" is accurate against the tool def. Client-side filtering on `target_kind="reconciliation"` / `target_id="BL-333FF9956BC6"` is the only path to the per-recon evidence rows given the recon's own `attachments=[]` field. P2 chain is reachable.

**(2) OE 22 messaging fallback** - VERIFIED REMOVED. OE 22 now reads "Send George a direct line using email_send_email with sender 'ben.arinzo@brookfieldcpas.com' and recipients 'george.mcadam@brookfieldcpas.com'." No `messaging_send_message` alternative. No display-name-as-identifier shape. Parameter shape (`content`, not `body`) explicitly noted.

All other tool names, parameter names, and record IDs cross-checked against `_aux/Universe_Split/*.json` per the verified table in `Hardness_Plan.md`:

| ID / field | OE step | Verified against |
|---|---|---|
| `BL-333FF9956BC6` (open recon, ben.arinzo preparer, variance -28.59) | OE 3 | `blackline.blackline_reconciliations.json` (Hardness_Plan anchor) |
| `exc_aade06f6129e43` (open exception, type=subledger_feed_drop, state=logged, financial_impact=-28.59) | OE 5 | `blackline.blackline_exceptions.json` |
| `1780147500.000000` / `1780152480.000000` / `1780323420.000000` ts values | OE 6-7 | `slack.slack_messages.json` |
| `email_scen_009_orphan_exception_0006` / `_0007` | OE 8 | `email.emails.json` |
| `conversation_scen_009_orphan_exception_0001` + msg_3a5d2103e25b + msg_3c287e39ef3f | OE 9 | `messaging.messages.json` |
| `BL-8DCA6908E272` (FP-2025-11 cert, variance -3.42, variance_explanations=[], attachments=[]) | OE 10 | `blackline.blackline_reconciliations.json` |
| `run_9e4afe5f93d549` (status="retried", 119/119/0, period=FP-2025-11) | OE 11 | `oracle_gl.ogl_subledger_feed_runs.json` |
| `exc_d8fc13aa2cc742` (FP-2025-12, unrecorded_invoice, -617.63, "Corrective JE posted; variance cleared in subsequent recon refresh") | OE 13 | `blackline.blackline_exceptions.json` |
| `BL-782A2EC69343` (FP-2025-12 cert, variance -617.63, certifier john.bartlett, variance_explanations with intercompany clearing) | OE 14 | `blackline.blackline_reconciliations.json` |
| `evid_6cbb5c1605904b` (kind="fx_rate_workbook", document_id=doc_01b7c6e1cbe94529) + `evid_6969ca2fd0a345` (kind="subledger_export", document_id=doc_b3633a2899a04e9e) | OE 15 | `blackline.blackline_evidence.json` |
| `doc_01b7c6e1cbe94529` (Marketing/business development JE support, je_368371d2b5424fdd) | OE 16 | `records_vault.rv_documents.json` |
| `doc_b3633a2899a04e9e` (AICPA/state society dues JE support, je_092d3a619f7f4bc5) | OE 17 | `records_vault.rv_documents.json` |
| `reminder_scen_009_orphan_exception_0000` + `_0008` | OE 18 | `reminder.reminders.json` |
| Slack parameter `payload` (not `text`/`content`) | OE 21 | AGENTS.md parameter-trap catalog |
| Email parameter `content` (not `body`) | OE 22 | AGENTS.md parameter-trap catalog |
| Retention code `AICPA_SQMS_7Y` + classification `internal` | OE 20 | AGENTS.md whitelist |

All accuracy spot-checks clean.

| Sub-Dim | Score |
|---|---:|
| OE Completeness | **5** |
| OE Accuracy | **5** |

---

## [B2] Adversarial Alt-Path

**NO ALT-PATH MISS.** Re-evaluated against the ACTUAL prompt text (not the misquoted version from the prior pass).

The actual prompt directs comparison broadly. Verbatim from `5_Prompt.txt`:

> "Take the precedent claim from where it was raised. Tell me what period it points to, the figure, the cause it is citing, and how it was closed out. Then take it apart on all four: same account, same period, same cause label, same close-out path. Pull the record for the period that was named and lay it next to the claim. **If that period is not the closest fit for what we are actually seeing on this account, tell me which recent prior-period record on this account is the closer fit, and what that one shows on the same four. I want the real prior-period shape on this account, not the framing in the thread.**"

The bolded sentences are explicit. The prompt itself instructs the agent:
- "If that period is not the closest fit for what we are actually seeing on this account" - conditional that the named period (FP-2025-11) may not be the right comparator;
- "tell me which recent prior-period record on this account is the closer fit" - explicit directive to search cross-period for the actual recent precedent on the same account;
- "what that one shows on the same four" - apply the four-pillar comparison to the discovered record, not the named record;
- "I want the real prior-period shape on this account, not the framing in the thread" - the prompt's closing line eliminates the narrow reading.

A competent Opus 4.8 agent reading this language has no path to satisfy the prompt without:
1. Pulling FP-2025-11 102000 record (BL-8DCA6908E272) and comparing the four pillars - the named-period sweep. **OE 10, OE 11.**
2. Concluding FP-2025-11 is not the closest fit (variance -3.42 vs claimed $42, no variance_explanations, no feed-drop exception, feed run status="retried" not "success"). **OE 10, OE 11 outcomes.**
3. Searching for the actual recent prior-period record on account 102000 (brookfield) that IS the closer fit. **OE 12.**
4. Reading that record's four pillars (period, figure, cause label, close-out path) - i.e., reading `exc_d8fc13aa2cc742` (FP-2025-12, unrecorded_invoice, -617.63, "Corrective JE posted") + its related recon `BL-782A2EC69343`. **OE 13, OE 14.**

The prior pass's alt-path concern was built on a misquote. The actual prompt forces the broad reading. **Alt-path: CLOSED.**

Density on this required cross-period chain is the floor of P8 (the load-bearing lever). Without OE 12-14 the agent fails the prompt's literal "tell me which recent prior-period record on this account is the closer fit" directive.

---

## [B3] Tool-Call Density Projection

Realistic trajectory a competent Opus 4.8 agent would take, with paginations / list-then-get pairs / handle resolution / retries factored in.

| OE | Tool call(s) | Min count |
|---|---|---:|
| 1 | contacts_search_contacts (Ben) | 1 |
| 2 | oracle_gl_get_fiscal_period brookfield_FP-2026-05 | 1 |
| 3 | blackline_get_reconciliation BL-333FF9956BC6 | 1 |
| 4 | oracle_gl_get_account 102000 brookfield | 1 |
| 5 | blackline_get_exception exc_aade06f6129e43 | 1 |
| 6 | slack_conversations_search_messages (+ likely slack_list_channels for C005 if not pre-cached) | 1-2 |
| 7 | slack_conversations_replies C005 1780147500.000000 | 1 |
| 8 | email_search_emails + email_get_email_by_id x 2 | 3 |
| 9 | messaging_search_conversations + messaging_get_conversation | 2 |
| 10 | blackline_list_reconciliations (FP-2025-11/102000) + blackline_get_reconciliation BL-8DCA6908E272 | 2 |
| 11 | oracle_gl_list_subledger_feed_runs (paginated, 1-2 pages) + oracle_gl_get_subledger_feed_run run_9e4afe5f93d549 | 2-3 |
| 12 | blackline_list_exceptions x 2 (unrecorded_invoice closed + subledger_feed_drop closed), paginated | 2-4 |
| 13 | blackline_get_exception exc_d8fc13aa2cc742 | 1 |
| 14 | blackline_get_reconciliation BL-782A2EC69343 | 1 |
| 15 | blackline_show_data (parameterless dump) | 1 |
| 16 | records_vault_get_document doc_01b7c6e1cbe94529 | 1 |
| 17 | records_vault_get_document doc_b3633a2899a04e9e | 1 |
| 18 | reminder_get_all_reminders | 1 |
| 19 | contacts_search_contacts (George) | 1 |
| 20 | records_vault_upload_document | 1 |
| 21 | slack_conversations_add_message | 1 |
| 22 | email_send_email | 1 |
| 23 | reminder_add_reminder | 1 |

**Min floor (no overhead):** ~29 calls.
**Realistic midpoint** (paginations on OE 11 + OE 12, list+get re-pairs, channel/handle resolution, occasional retry, base discovery scaffolding): **42-47 calls.**

Hardness_Plan.md projected midpoint **44**. Candidate's pre-rebuild trajectory on essentially the same shape hit avg **53**. The OE list as written holds the **40 floor** and lands at the **44 midpoint**.

OE 11 (pagination across feed-run history) and OE 12 (double list_exceptions across type/state filters) are the two density-load-bearing pagination steps. Both are required by the OE blueprint and ride directly on prompt language ("how it was closed out" = needs feed-run read; "which recent prior-period record on this account is the closer fit" = needs the list_exceptions cross-period search). Density floor is durably held.

**Density: PASS** (>= 40 floor).

---

## [B4] Hardness Preservation

Mix from `Hardness_Plan.md` Selected Levers table: **P1 + P2 + P7 + P8 + P9 + L9-overlay.**

| Lever | Exercising OE step(s) | Status |
|---|---|---|
| **P1 Latching** (3-service consistency on the disposition story) | OE 6-7 (Slack thread `1780147500.000000` + reply `1780152480.000000` + relay `1780323420.000000`); OE 8 (email pair `email_scen_009_orphan_exception_0006` + `_0007`); OE 9 (messaging conversation `conversation_scen_009_orphan_exception_0001`) | ✓ TRIGGERED |
| **P2 Structured-DB skip** (recon.attachments=[] is misleading; evidence lives on a separate surface; kind labels lie about doc content) | OE 15 (`blackline_show_data` dump + client-side filter on target=BL-333FF9956BC6 surfaces `evid_6cbb5c1605904b` and `evid_6969ca2fd0a345`); OE 16-17 (RV doc reads revealing Marketing / AICPA JE-support content) | ✓ TRIGGERED |
| **P7 Multi-write diversification** (4 writes across records_vault / slack / email / reminder >= 3-service floor) | OE 20 (vault), OE 21 (Slack C005 thread post), OE 22 (email to George), OE 23 (reminder) | ✓ TRIGGERED |
| **P8 Multi-link chain** (load-bearing: thread -> list_exceptions filtered -> exc_d8fc13aa2cc742 -> resolution_summary -> derive corrective-JE remediation) | OE 10 (FP-2025-11 recon comparison); OE 11 (FP-2025-11 feed run status="retried"); OE 12 (list_exceptions discovery filtered to brookfield/102000); OE 13 (exc_d8fc13aa2cc742 read); OE 14 (BL-782A2EC69343 read) | ✓ TRIGGERED, **and reachable from the actual prompt** ("tell me which recent prior-period record on this account is the closer fit") |
| **P9 Universe-grounded gotcha** (USD Cash-Payroll -> no FX revaluation surface) | OE 4 (oracle_gl_get_account confirms 102000=Cash-Payroll USD on brookfield); grounding propagates into OE 20(c), OE 22(4), OE 24(b) | ✓ TRIGGERED |
| **L9 Authority-dismissal overlay** (Ryan + George + Hannah + Daniel + Blue alignment on the wrong call) | OE 6-9 establish 5-way alignment; OE 13-14 ground the disagreement on real records | ✓ TRIGGERED |

**All six selected levers TRIGGERED.** P8 reachability from the prompt is confirmed via the verbatim "tell me which recent prior-period record on this account is the closer fit" directive (see B2 quote). The corrected OE list preserves every lever in `Hardness_Plan.md` without overshoot or drift.

**Hardness preservation: PASS.**

---

## [B5] Tool-Leak / Phrasing Scan

| Check | Result |
|---|---|
| em-dashes (`—`) | **CLEAN.** Compound modifiers use ASCII hyphens (`-`). |
| en-dashes (`–`) | **CLEAN.** |
| "approximately" before exact IDs/dates | **CLEAN.** No such phrasing. |
| "(or similar)" near exact dollar values | **CLEAN.** Exact amounts (`-28.59`, `-617.63`, `-3.42`, `-247.05`) carried verbatim. |
| "at least N" phrases | **CLEAN.** Not present. |
| Slack `payload` (not `text`/`body`) | **CORRECT.** OE 21 explicitly: "The payload (parameter name 'payload', not 'text' or 'content')." |
| Email `content` (not `body`) | **CORRECT.** OE 22 explicitly: "The content (parameter name 'content', not 'body')." |
| Messaging `content` (not `body`) | **N/A** (messaging fallback removed; no messaging write in the OE). The only messaging step is OE 9 read. |
| Retention codes whitelist (AICPA_SQMS_7Y / IRS_TAX_7Y / FIRM_INTERNAL / INDEFINITE) | **CORRECT.** OE 20 uses `AICPA_SQMS_7Y`. No invalid codes (no `SOX_7Y`, no `SEC_PERMANENT`). |
| Classifications whitelist (public / internal / restricted) | **CORRECT.** OE 20 uses `internal`. |
| IDs only in OE bodies (legal location) | **OK.** Exact IDs carried only in OE bodies (`exc_aade06f6129e43`, `BL-333FF9956BC6`, `BL-782A2EC69343`, `BL-8DCA6908E272`, `exc_d8fc13aa2cc742`, doc/evid/run/je/email/msg/reminder IDs). No tool names leaked into prompt-style guidance. |

**B5 verdict: CLEAN.** No phrasing hits.

---

## [B6] Upstream Propagation (FORWARD + REVERSE)

### FORWARD (every actionable prompt sentence maps to >= 1 OE step)

Sentences enumerated against the verbatim `5_Prompt.txt`:

| # | Prompt sentence (verbatim or first words) | OE step(s) |
|---|---|---|
| P1 | "I prepared the cash-payroll recon for the May close and the exception on it is now lined up for accept-timing..." (framing, non-actionable) | OE 3, OE 5 (recon + exception read) |
| P2 | "The read going around does not match how the records sat when I put the recon together, so I want to re-check both pieces against what is actually there before this gets locked in." (framing) | OE 6-9 (re-check disposition story across services); OE 15-17 (re-check supporting evidence); OE 2 (period still open) |
| P3 | "Take the precedent claim from where it was raised." | OE 6, OE 7 |
| P4 | "Tell me what period it points to, the figure, the cause it is citing, and how it was closed out." | OE 7 (extract George's four pillars: FP-2025-11, $42, feed-drop residual, accept-timing/retry-clean) |
| P5 | "Then take it apart on all four: same account, same period, same cause label, same close-out path." | OE 10 (period/figure/cause comparison on BL-8DCA6908E272), OE 11 (close-out comparison via run_9e4afe5f93d549) |
| P6 | "Pull the record for the period that was named and lay it next to the claim." | OE 10 (open BL-8DCA6908E272) |
| P7 | **"If that period is not the closest fit for what we are actually seeing on this account, tell me which recent prior-period record on this account is the closer fit, and what that one shows on the same four."** | OE 12 (list_exceptions discovery filtered to brookfield/102000), OE 13 (exc_d8fc13aa2cc742 read), OE 14 (BL-782A2EC69343 read) |
| P8 | "I want the real prior-period shape on this account, not the framing in the thread." | OE 13 + OE 14 (the real shape on 102000) - reinforcing P7 |
| P9 | "Do the same on the supporting evidence the recon is leaning on." | OE 15 (enumerate evidence via blackline_show_data dump) |
| P10 | "Read what each piece is labelled as." | OE 15 (capture kind labels "fx_rate_workbook" / "subledger_export") |
| P11 | "Then open the underlying documents and see what they cover." | OE 16, OE 17 |
| P12 | "If the contents do not back the cause the recon is asserting, say so plainly." | OE 16, OE 17, OE 20(b), OE 22(3), OE 24(b) (kind-vs-content mismatch finding) |
| P13 | "When you have the picture, drop a write-up of what you saw on the prior-period record and the documents into the vault under the close-cycle file so it is on hand for George." | OE 20 (records_vault_upload_document on BL-333FF9956BC6, kind=reconciliation_support, related_resource=BL-333FF9956BC6) |
| P14 | "Drop a short note into the channel the precedent was raised in so the thread sees something was checked against the records." | OE 21 (slack_conversations_add_message C005 thread_ts=1780147500.000000) |
| P15 | "And send George a direct line letting him know what the records actually show on each piece, so he has it before he takes the disposition." | OE 22 (email_send_email to george.mcadam@brookfieldcpas.com) |
| P16 | "Set me a reminder to chase this with George before the period certifies." | OE 23 (reminder_add_reminder, due_datetime ahead of FP-2026-05 cert + distinct from existing _0000/_0008) |
| P17 | "Tell me what you found and where you left it." | OE 24 (final user-facing response) |

**FORWARD coverage: CLEAN.** Every actionable prompt sentence maps to >= 1 OE step. P7 ("tell me which recent prior-period record on this account is the closer fit") - the sentence the prior pass misquoted - is now correctly mapped to OE 12-14 and exercises the load-bearing P8 chain.

### REVERSE (every OE step maps to a real prompt ask)

| OE | Maps to | Notes |
|---|---|---|
| OE 1 | Base discovery (universal; persona self-lookup) | Implicit |
| OE 2 | P2 framing ("before this gets locked in") | Grounded - period still open |
| OE 3 | P1 (the recon) | Direct |
| OE 4 | P12 ("if the contents do not back the cause") - USD-cash grounding feeds the "FX cause cannot apply" finding | Direct |
| OE 5 | P1 (the exception) | Direct |
| OE 6 | P3 ("where it was raised") | Direct |
| OE 7 | P3, P4 (read claim + capture four pillars) | Direct |
| OE 8 | P2 ("re-check both pieces") + supports P15 (George's email visibility into the disposition pair Daniel approved) | Direct |
| OE 9 | P2 ("re-check both pieces") + Ryan recommend traced | Direct |
| OE 10 | P5, P6 (compare to named period) | Direct |
| OE 11 | P5 ("close-out path") | Direct - feed-run status verifies the "retry picked it up clean" claim |
| OE 12 | **P7 ("tell me which recent prior-period record on this account is the closer fit")** | Direct - discovery sweep |
| OE 13 | **P7 + P8 ("the real prior-period shape on this account")** | Direct - the closer-fit record |
| OE 14 | P7 + P8 (the closer-fit record's related recon) | Direct |
| OE 15 | P9, P10 (enumerate + read labels) | Direct |
| OE 16 | P11 (open underlying doc) | Direct |
| OE 17 | P11 (open underlying doc) | Direct |
| OE 18 | P16 (distinct reminder framing - anti-L25) | Indirect but defensible - required to avoid no-op |
| OE 19 | P15 prerequisite (George address resolution) | Direct |
| OE 20 | P13 (vault write-up under close-cycle file) | Direct |
| OE 21 | P14 (slack note in precedent channel) | Direct |
| OE 22 | P15 (direct line to George) | Direct |
| OE 23 | P16 (chase-before-certify reminder) | Direct |
| OE 24 | P17 (tell what found, where left it) | Direct |

**REVERSE coverage: CLEAN.** No OE step is orphaned. OE 18 is the only indirect map (anti-L25 setup), and it is operationally required so OE 23 can frame the reminder distinctly from the two existing reminders on `exc_aade06f6129e43`.

### PROPAGATE TO S1

**None.** The prior pass's PROPAGATE concern was built on a quote that does not exist in `5_Prompt.txt`. The actual prompt contains the explicit "If that period is not the closest fit for what we are actually seeing on this account, tell me which recent prior-period record on this account is the closer fit, and what that one shows on the same four. I want the real prior-period shape on this account, not the framing in the thread." language. This is a verbatim mandate for cross-period precedent search. The narrow-reading alt-path the prior pass surfaced is closed by the prompt itself - no S1 edit needed.

No other root-cause-in-prompt issues observed.

---

## Summary

| Sub-Dim | Score |
|---|---:|
| OE Completeness | **5** |
| OE Accuracy | **5** |
| Adversarial alt-path | **none (closed by prompt)** |
| Tool-call density | **~44 midpoint (PASS, >= 40)** |
| Hardness preservation | **all 6 levers triggered, all reachable** |
| Phrasing scan | **CLEAN** |
| FORWARD propagation | **CLEAN (17/17 actionable sentences mapped)** |
| REVERSE propagation | **CLEAN (24/24 OEs mapped)** |
| PROPAGATE TO S1 | **none (prior concern was misquoted prompt)** |

Both deltas are correct against ground truth: `blackline_show_data` is `parameters: []` in `8_Server_Tools_Details.json` (OE 15 fix verified) and OE 22's messaging fallback is removed (email-only, with `content` parameter explicitly noted). The load-bearing P8 chain is now both technically triggered in the OE list AND reachable from the actual prompt language.

VERDICT: GO
