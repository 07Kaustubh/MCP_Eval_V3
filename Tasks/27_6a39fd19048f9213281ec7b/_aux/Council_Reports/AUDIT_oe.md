# AUDIT_oe.md — Strict Veteran Audit (OE phase)

**Task:** `27_6a39fd19048f9213281ec7b` (REDO after fabricated discriminator `brookfield_6000001115`)
**Deliverable under audit:** `6_Oracle_Events.txt` (24 numbered OEs)
**Prior councils:** `S2_A_grounding.md` PASS, `S2_B_adversarial.md` PASS (after two correction rounds: OE 15 `blackline_show_data` clarification; OE 22 messaging fallback removed, email only).
**Audit lens:** Strictest possible interpretation per `AGENTS.md` rule 12 (5/5 only; "should" = "must"; density bar 50+ midpoint; any prompt or agent-readable-source leakage on the derived figure = BLOCKER).

---

## LENS 1 — Strict QC scoring

Per `Docs/7_QC_Spec_Doc1.json`, OE has two scorable sub-dims. Under strictest interpretation:

### OE Completeness — **5/5**

**Reason:** The OE list covers the full critical path: persona/recipient identification (OE 1, 19), period status (OE 2), the open recon and exception (OE 3, 5), grounding gate for the persona's own variance explanation (OE 4, P9 lever), the three-service conversational latch surface (OE 6–9, P1 lever), all four refutation legs of George's precedent claim (OE 10 prior-period record, OE 11 close-out path, OE 12 actual-precedent discovery, OE 13 + 14 actual-precedent body + recon), the structured-DB skip on evidence + RV chase (OE 15–17, P2 lever), L25 anchor-trap surfacing (OE 18), and all four required writes plus the final user-facing reply (OE 20–24, P7 lever). Every prompt ask traces to one or more OEs.

| Prompt ask | OE(s) | Coverage |
|---|---|---|
| Take precedent claim from where raised; extract period / figure / cause / close-out | OE 6, 7 | Full |
| Refute on all four legs: same account, period, cause, close-out | OE 10, 11, 12, 13, 14 | Full |
| Closer-fit prior-period record on this account | OE 12, 13, 14 | Full |
| Read evidence labels, open underlying docs, say plainly if they don't back the cause | OE 15, 16, 17 | Full |
| Drop write-up into vault under close-cycle file | OE 20 | Full |
| Drop short note into the channel the precedent was raised in | OE 21 | Full |
| Send George a direct line | OE 22 | Full |
| Set reminder to chase before period certifies | OE 23 | Full |
| Tell what found and where left | OE 24 | Full |

**What the prior council could have missed:** Nothing material on completeness. `S2_A` already flagged write-action coverage; `S2_B` re-checked critical-path closure on the corrected version.

### OE Accuracy — **5/5**

**Reason:** All 22 tool references (`contacts_search_contacts`, `oracle_gl_get_fiscal_period`, `blackline_get_reconciliation`, `oracle_gl_get_account`, `blackline_get_exception`, `slack_conversations_search_messages`, `slack_conversations_replies`, `email_search_emails`, `email_get_email_by_id`, `messaging_search_conversations`, `messaging_get_conversation`, `blackline_list_reconciliations`, `oracle_gl_list_subledger_feed_runs`, `oracle_gl_get_subledger_feed_run`, `blackline_list_exceptions`, `blackline_show_data`, `records_vault_get_document`, `reminder_get_all_reminders`, `records_vault_upload_document`, `slack_conversations_add_message`, `email_send_email`, `reminder_add_reminder`) are real tools per `8_Server_Tools_Details.json`. Parameter traps are explicitly called out: OE 21 names `payload` (not `text`), OE 22 names `content` (not `body`), OE 23 implies `due_datetime` (not `due_date`). Every cited record id, dollar amount, status, persona email, and timestamp matches the Hardness_Plan anchor table that was itself grep-verified against `_aux/Universe_Split/`. OE 15's clarification on `blackline_show_data` (no parameters; the call dumps full BlackLine state and is the only surface exposing the evidence table) is the corrected wording from the prior block-and-fix cycle and is consistent with the tool def. OE 22's collapse to `email_send_email` only (no messaging fallback) is the corrected wording from the prior block-and-fix cycle. The `retention_policy_code "AICPA_SQMS_7Y"` on OE 20 is on the valid list per `AGENTS.md` (not `SOX_7Y` / `SEC_PERMANENT`).

**What the prior council could have missed (NOT blocking, see Issues below):** Two minor stylistic / date items — OE 10 + OE 13 narrative conclusions use "about three dollars" / "about six hundred and eighteen dollars" *after* citing the exact figures (-3.42 / -617.63) in the same OE. The exact figures are present so this is not "approximately near amounts" in the format-card sense; it's narrative paraphrase. OE 23's *example* due_datetime "2026-06-11T09:00:00-04:00" sits one day before universe today (2026-06-12) — a future-of-today example would have been cleaner, but the OE wording "earlier than the typical close-day cadence so the chase happens before the period locks" makes the intent clear and the prior councils correctly read it as a non-blocking example, not a mandate.

**Score:** OE Completeness **5/5**, OE Accuracy **5/5**. Both at the strictest bar.

---

## LENS 2 — Answer-leakage sweep

The "correct/derived answer" carried by this task: **`exc_d8fc13aa2cc742`** (brookfield_FP-2025-12, type `unrecorded_invoice`, financial_impact `-617.63`, resolution_summary "Corrective JE posted; variance cleared in subsequent recon refresh", related_reconciliation_id `BL-782A2EC69343`).

**Search targets:** `617.63`, `617`, `$617`, `exc_d8fc13aa2cc742`, `FP-2025-12`, `Corrective JE`, `BL-782A2EC69343`, `unrecorded_invoice`, plus arithmetic neighbors and competing-precedent token `feed_drop`.

| Surface | Searched for answer tokens | Hit? |
|---|---|---|
| `5_Prompt.txt` (prompt body) | all of the above | **No hits.** Prompt is ID-free, period-ID-free, amount-free except for the implicit cash-payroll context. Persona narrative only names "the cash-payroll recon for the May close" and "the exception on it" in descriptive prose. |
| Slack thread `1780147500.000000` (per OE 6, 7) | per OE quote: George's reply names "FP-2025-11", "$42", "feed-drop residual", "accepted as timing because the next-period retry picked it up clean" | **No leakage.** The thread states the WRONG four pillars; agent must disprove and replace. |
| Daniel approval email `email_scen_009_orphan_exception_0007` | per OE 8 quote: "Approved. Accept-timing for FP-2026-05 is fine based on the 29 dropped rows, Ryan's note, George's precedent, and Hannah's downstream review." | **No leakage.** Disposition narrative only; no mention of FP-2025-12 / -617.63 / unrecorded_invoice / corrective JE. The "29 dropped rows" loosely mirrors the open exception's |-28.59| but does not name the precedent. |
| Blue↔Daniel email `email_scen_009_orphan_exception_0006` | per OE 8 description | **No leakage.** Same content domain. |
| Blue↔Ryan messaging `conversation_scen_009_orphan_exception_0001` | per OE 9 | **No leakage.** Ryan recommends accept-timing, loops George and Hannah; no precedent body. |
| Records Vault doc `doc_01b7c6e1cbe94529` | per OE 16 | **No leakage.** Content is "Supporting documentation for Marketing / business development" JE support, unrelated. |
| Records Vault doc `doc_b3633a2899a04e9e` | per OE 17 | **No leakage.** Content is "Supporting documentation for AICPA / state society dues" JE support, unrelated. |

**Synthesis check:** No single tool call surfaces `exc_d8fc13aa2cc742` / FP-2025-12 / -617.63 / corrective-JE. The agent must (a) recognize George's claim does not survive contact with the FP-2025-11 record (OE 10 + OE 11), (b) run `blackline_list_exceptions` filtered to brookfield/102000/closed and inspect by type to surface the precedent (OE 12), then (c) fetch its body to read `resolution_summary` (OE 13). That is **three structured-DB hops minimum** to land the answer.

**OE-body leakage of the answer is EXPECTED and allowed** per `AGENTS.md` rule 7 ("No tool names in prompts. No tool names in rubric titles. Allowed only in OE bodies and in rubric evidence / justification fields."); the same convention covers ID leakage. OE 13, OE 14, OE 20, OE 22, OE 24 all name the precedent IDs in OE body — correct.

**Verdict:** **No leakage blocker.** Prompt is clean; agent-readable sources are clean; synthesis requires 3+ hops.

---

## LENS 3 — Hardness end-to-end trace

Per `_aux/Hardness_Plan.md` "Selected Levers" table — six levers (P1, P2, P7, P8, P9, L9-overlay).

| Lever | Prompt sentence (verbatim) | OE step(s) exercising | Fact_Ledger atom(s) | Rubric (S3) |
|---|---|---|---|---|
| **P1 Latching** | "the exception on it is now lined up for accept-timing on a precedent someone cited in the channel and on the supporting evidence stapled to the recon" | OE 5 (`exc_aade06f6129e43`), OE 6 + OE 7 (Slack thread `1780147500.000000` and George reply `1780152480.000000`), OE 8 (emails `_0006` + `_0007`), OE 9 (`conversation_scen_009_orphan_exception_0001`) | slack ts × 3, email_id × 2, conversation_id × 1, exc_aade06f6129e43, daniel.jones / ryan.delgado / george.mcadam / hannah.grant / blue.evans | **deferred to S3 AUDIT** |
| **P2 Structured-DB skip** | "Do the same on the supporting evidence the recon is leaning on. Read what each piece is labelled as. Then open the underlying documents and see what they cover. If the contents do not back the cause the recon is asserting, say so plainly." | OE 15 (`blackline_show_data` → filter evidence rows for `BL-333FF9956BC6`), OE 16 (`doc_01b7c6e1cbe94529`), OE 17 (`doc_b3633a2899a04e9e`) | evid_6cbb5c1605904b (kind `fx_rate_workbook`), evid_6969ca2fd0a345 (kind `subledger_export`), doc_01b7c6e1cbe94529 ("Marketing / business development" JE support), doc_b3633a2899a04e9e ("AICPA / state society dues" JE support) | **deferred to S3 AUDIT** |
| **P7 Multi-write diversification** | "drop a write-up… into the vault" + "Drop a short note into the channel the precedent was raised in" + "send George a direct line" + "Set me a reminder to chase this with George before the period certifies" | OE 20 (RV upload), OE 21 (Slack post C005 thread), OE 22 (email to George), OE 23 (reminder add) | RV `records_vault_upload_document` kind `reconciliation_support`; Slack `C005` thread `1780147500.000000`; email sender ben.arinzo, recipient george.mcadam; reminder_add_reminder | **deferred to S3 AUDIT** |
| **P8 Multi-link chain (precedent dig — LOAD-BEARING)** | "If that period is not the closest fit for what we are actually seeing on this account, tell me which recent prior-period record on this account is the closer fit, and what that one shows on the same four." | OE 10 (`BL-8DCA6908E272` FP-2025-11 recon — refutes "$42" claim, variance -3.42), OE 11 (`run_9e4afe5f93d549` — refutes "retry picked it up clean", status `retried`), OE 12 (`blackline_list_exceptions` × 2 filtered to brookfield/102000), OE 13 (`exc_d8fc13aa2cc742` body), OE 14 (`BL-782A2EC69343` recon) | exc_d8fc13aa2cc742 (FP-2025-12, unrecorded_invoice, -617.63, "Corrective JE posted"), BL-782A2EC69343, BL-8DCA6908E272 (variance -3.42, attachments []), run_9e4afe5f93d549 (status `retried`, retried_from_run_id null) | **deferred to S3 AUDIT** |
| **P9 Universe-grounded gotcha (USD-cash → no FX)** | "The read going around does not match how the records sat when I put the recon together, so I want to re-check both pieces against what is actually there before this gets locked in." (implicit; the recon's own variance_explanation is the persona's own and the agent must recognize it as anti-grounded) | OE 4 (`oracle_gl_get_account` 102000 brookfield → confirms USD Cash - Payroll, no FX surface), OE 3 (surfaces the persona-authored "FX revaluation rates refreshed" variance explanation) | account 102000 = "Cash - Payroll" USD on brookfield (per `_aux/Universe_Index/accounts_per_entity.md`); variance_explanations.attributed_to = ben.arinzo@brookfieldcpas.com on BL-333FF9956BC6 | **deferred to S3 AUDIT** |
| **L9 authority-dismissal overlay** | "the exception on it is now lined up for accept-timing" + the persona's own variance_explanation is the override target | OE 3 (persona's own variance_explanation), OE 7 (George precedent), OE 8 (Daniel approval + Hannah downstream review), OE 9 (Ryan recommendation), OE 5 (Blue Evans assignment) | Five-way authority alignment: ryan.delgado (recommends) + george.mcadam (precedent) + hannah.grant (payroll-tax-downstream) + daniel.jones (approves) + blue.evans (executes); plus ben.arinzo's own anti-grounded explanation | **deferred to S3 AUDIT** |

**Every lever traces to a prompt anchor, OE step(s), and Fact_Ledger atom(s).** No "probably triggered" / "implied without evidence" levers.

**Verdict:** **No hardness regression.** Six-of-six levers carry end-to-end.

---

## LENS 4 — Strict density projection

**Strict bar:** 50+ midpoint. 40–49 = THIN. <40 = BLOCKER.

**Strictest reading (single call per OE step, no pagination beyond minimum):**

| OE | Min calls (strict) | Realistic calls (per trajectory shape) |
|---|---|---|
| OE 1 contacts_search ben | 1 | 1 |
| OE 2 get_fiscal_period | 1 | 1 |
| OE 3 get_reconciliation BL-333... | 1 | 1 |
| OE 4 get_account 102000 | 1 | 1 |
| OE 5 get_exception exc_aade06... | 1 | 1 |
| OE 6 slack search | 1 | 1–2 |
| OE 7 slack replies | 1 | 1 |
| OE 8 email search + 2 gets | 3 | 3 |
| OE 9 messaging search + get | 2 | 2 |
| OE 10 list_reconciliations + get BL-8DCA... | 2 | 2–3 |
| OE 11 list_subledger_feed_runs (paginated) + get run_9e4afe... | 2 | 3–5 |
| OE 12 list_exceptions × 2 (paginated, both types) | 4 | 6–10 |
| OE 13 get_exception exc_d8fc13... | 1 | 1 |
| OE 14 get_reconciliation BL-782A... | 1 | 1 |
| OE 15 blackline_show_data | 1 | 1 |
| OE 16 get_document doc_01b7c... | 1 | 1 |
| OE 17 get_document doc_b3633... | 1 | 1 |
| OE 18 get_all_reminders | 1 | 1 |
| OE 19 contacts_search george | 1 | 1 |
| OE 20 upload_document | 1 | 1 |
| OE 21 slack_add_message | 1 | 1 |
| OE 22 send_email | 1 | 1 |
| OE 23 add_reminder | 1 | 1 |
| Supporting (slack_list_channels for C005, contact disambiguation, retries) | 2–4 | 4–8 |
| **TOTAL** | **31–34** | **45–55** |

**Cross-check against observed candidate trajectory:** `Tasks/27_6a39fd19048f9213281ec7b/_aux/Trajectory_Stats.json` reports avg **53** / min **30** / max **69** on the same OE shape.

**Verdict on strict bar:** observed avg **53 ≥ 50 = PASS**. Strict-min reading lands at **31–34** which would be BLOCKER on the absolute floor, but two facts neutralize it: (a) OE 11 and OE 12 explicitly mandate pagination ("paginate via offset and limit") which trajectory data confirms agents actually execute, pushing realistic count to 45–55; (b) the observed avg-53 trajectory exists, demonstrating the shape supports the strict bar. **Density PASS.**

**Minor note (non-blocking):** The Hardness_Plan P9 projection lists three density-padding calls under "universe-grounded gotcha" (`oracle_gl_get_account`, `oracle_gl_list_journal_entries period=FP-2026-05 account=102000`, `oracle_gl_get_account_balance (102000 / FP-2026-05)`). Only the first is in the OE (OE 4). Including the other two as explicit cross-checks would tighten the strict-min floor by 2 calls but is not critical-path required.

---

## LENS 5 — Adversarial veteran review

Pattern-recognition pass against 200+ prior task defects:

| Check | Status | Evidence |
|---|---|---|
| Implicit-prompt framing preserved (persona is recanting own variance_explanation, not contradiction-hunting) | **PASS** | Prompt voice: first-person ownership ("I prepared the cash-payroll recon", "the read going around does not match how the records sat when I put the recon together"). OE 24 voice explicitly: "The voice is the persona recanting his own variance_explanation against the records, not a contradiction-hunt or a disposition decision." |
| Entity-drift seams (102000 = Cash-Payroll on brookfield vs IOLTA on northstar_legal vs Short-term Investments on acme_cloud) | **PASS** | OE 3 + OE 4 + OE 12 + OE 14 all carry explicit `entity_id "brookfield"` and `account_name "Cash - Payroll"`. OE 12 specifically filters `entity_id "brookfield" AND related_account_id "102000"`. |
| Tool name leaks in PROMPT | **PASS** | Prompt body uses descriptive prose ("the cash-payroll recon", "the channel the precedent was raised in", "the vault under the close-cycle file"). No `verb_noun_subject` tokens. |
| Em-dashes (— or –) | **PASS** | Neither prompt body nor OE list contains em-dash or en-dash; only hyphens in compound terms ("cash-payroll", "accept-timing", "next-period"). |
| "at least N" without prompt mandate | **PASS** | Neither prompt nor OE list uses "at least N". |
| Internal IDs in the prompt | **PASS** | Prompt is ID-free. OEs carry IDs (allowed per `AGENTS.md`). |
| OE meta-tags (write/read arrows) | **PASS** | Natural prose ("Call…", "Confirm…", "Conclude…"). No tag syntax. |
| Single-channel lock-in where prompt named goal ("send George a direct line" → OE 22 email_send_email only) | **MINOR NOTE** | The prior block-and-fix cycle deliberately collapsed OE 22 to email-only after the messaging fallback was flagged. "Direct line" reads naturally as email for a disposition-grade reference. This is the corrected behavior and the rubric should treat the channel choice as evidence of intent rather than method-locking. Acceptable. |
| "Approximately" near IDs / dates / account numbers / dollar amounts | **MINOR NOTE** | OE 10 ("variance was about three dollars rather than forty-two") and OE 13 ("carried about six hundred and eighteen dollars, not forty-two") use narrative paraphrase AFTER citing the exact figures (-3.42 / -617.63) in the same OE. Not "approximately near amounts" in the format-card sense (exact figures are present); narrative tone for the conclusion sentence only. Not blocker. |
| "(or similar)" near values that must be exact | **PASS** | Only used on search-query alternatives (OE 6, OE 8, OE 9), which is the format-card allowed pattern, never on exact values like recon IDs / account numbers / dollar amounts. |
| L25 anchor trap (two existing reminders on the exception — does OE 18 + OE 23 keep new reminder distinct?) | **PASS** | OE 18 explicitly lists both pre-existing reminders (`_0000` triage breadcrumb + `_0008` post-retry recheck) and notes "The persona's new reminder must be framed as the distinct period-certifies chase against George with the precedent and evidence findings, not a duplicate of the retry-recheck cadence." OE 23 mirrors: "The framing must be distinct from the two existing reminders on `exc_aade06f6129e43`… so it does not collapse into the L25 no-op." Both halves are present. |
| L9 authority dismissal preserved as verification, not crusade | **PASS** | OE 22 framing: "what the records actually show on each piece, so he has it before he takes the disposition" — gives George information, not orders. OE 24 voice: "not a contradiction-hunt or a disposition decision." Persona does not direct anyone to reverse the call. |
| L24 soft verbs on writes | **PASS** | OE 20 "Drop the close-cycle write-up", OE 21 "Drop a short note", OE 22 "Send George a direct line", OE 23 "Set the persona's chase-before-certify reminder", OE 24 "summarizes what the records show". No "Daniel was wrong", "reverse the disposition", "tell Daniel he made a mistake" verbs. |
| L29 escape valves in user-facing reply | **PASS** | OE 24 description is descriptive only ("walk the four-pillar refutation… state that the recon's two evidence attachments are kind-mislabelled… name where the write-up was dropped… confirm the chase-before-certify reminder was set"). No invitations to expand scope, surface other contradictions, or chase further unrelated issues. |
| L6 answer-naming in persona-authored artifact bodies | **PASS** | Prompt body (the only persona-authored artifact pre-existing in this task) does NOT name `exc_d8fc13aa2cc742` / `FP-2025-12` / `-617.63` / "Corrective JE" / `unrecorded_invoice`. The agent-authored vault upload (OE 20) and direct-line email (OE 22) do name the answer — these are agent reports of investigation findings, not persona-authored artifacts, so L6 is preserved. |
| OE 23 date-consistency on example due_datetime | **MINOR NOTE** | The OE-suggested example "2026-06-11T09:00:00-04:00" sits one day before universe today (2026-06-12). The wording frames it as one possible value ("for example"), and the intent ("ahead of FP-2026-05 certification, earlier than the typical close-day cadence so the chase happens before the period locks") is unambiguous. An agent might set a slightly future date instead, which the rubric should treat as equally valid. Not a blocker because the OE example is illustrative rather than mandatory, and the prior councils correctly read it as such. |

**Verdict:** No structural defects. Three MINOR notes (single-channel lock-in on OE 22, narrative "about" in OE 10 + OE 13 conclusions, OE 23 example date is past-today) all already cleared by prior council cycles or are non-blocking on strict reading.

---

## VERDICT SYNTHESIS

| Lens | Result |
|---|---|
| LENS 1 — Strict QC (OE Completeness + Accuracy at strictest bar) | **5/5 + 5/5** |
| LENS 2 — Answer-leakage sweep (prompt + agent-readable sources) | **No leakage** |
| LENS 3 — Hardness end-to-end trace (P1 + P2 + P7 + P8 + P9 + L9-overlay) | **All 6 levers trace** |
| LENS 4 — Strict density projection (50+ midpoint) | **PASS** (observed avg 53; realistic 45–55; strict-min 31–34 padded by mandated pagination on OE 11 + OE 12) |
| LENS 5 — Adversarial veteran review | **No structural defects; 3 minor notes already cleared or non-blocking** |

**Blocker hits:** 0
**Lens-1 sub-dims below 5:** 0
**Untraced levers:** 0
**Density below strict bar:** No (avg 53 ≥ 50)

This deliverable was REDONE after a fabricated discriminator was caught at FINAL on the prior attempt. The new OE list is data-first, anchored on grep-verified records, and every load-bearing claim (`exc_d8fc13aa2cc742` precedent, evidence-label-vs-content mismatch on the two RV docs, USD-cash-no-FX grounding, three-service latch surface, two-existing-reminder L25 trap) traces cleanly. The prior block-and-fix cycle on OE 15 (`blackline_show_data` parameter clarity) and OE 22 (messaging fallback removed) are both reflected in the current deliverable correctly. The prior `Council_B_S1.5` PROPAGATE-to-S1 finding that referenced a prompt quote not present in the actual prompt has been correctly read as a council-side false positive; the current prompt body is clean.

**VERDICT: PASS (STRICT)**
