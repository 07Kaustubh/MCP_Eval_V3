# Rubric Coverage Matrix — Tasks/27_6a39fd19048f9213281ec7b

**AUDIT verdict:** PASS (STRICT)
**Council A verdict:** GO
**Council B verdict:** GO
**Validator:** PASS (0 fails, 7 warns documentary on Fact_Ledger sign convention)
**Rubric count:** 24 outcome / 0 process
**Density projection (B3):** PASS (centroid ~43 against >=40 floor; observed avg-53 trajectory)
**Hardness lever coverage (B4):** 6/6 PASS (P1, P2, P7, P8, P9, L9 overlay)

---

## Rubric ordering (positional indices used below)

The 24 rubrics in `7_Rubrics.json`, in file order:

| # | Surface | Sub-type | Title cue |
|---|---|---|---|
| 1 | Vault | 1.1 | Vault upload metadata (kind / retention / classification / related recon / uploader) |
| 2 | Vault | 1.2 | Actual recent precedent: exc_d8fc13aa2cc742 in FP-2025-12 |
| 3 | Vault | 1.2 | FP-2025-11 BL-8DCA6908E272 variance $3.42 refutation [NEW, AUDIT F2] |
| 4 | Vault | 1.2 | First attachment mismatch (evid_6cbb5c1605904b -> doc_01b7c6e1cbe94529 Marketing/BD) |
| 5 | Vault | 1.2 | Second attachment mismatch (evid_6969ca2fd0a345 -> doc_b3633a2899a04e9e AICPA dues) |
| 6 | Vault | 1.2 | 102000 is USD Cash - Payroll, FX cannot apply [NEW, AUDIT F1] |
| 7 | Slack | 1.1 | Thread reply on C005 thread_ts 1780147500.000000 |
| 8 | Slack | 1.2 | Thread reply references exc_aade06f6129e43 + BL-333FF9956BC6 + records-check summary |
| 9 | Email | 1.1 | Email from ben.arinzo to george.mcadam |
| 10 | Email | 1.2 | Actual recent precedent: exc_d8fc13aa2cc742 in FP-2025-12 |
| 11 | Email | 1.2 | FP-2025-11 BL-8DCA6908E272 variance $3.42 refutation |
| 12 | Email | 1.2 | First attachment mismatch |
| 13 | Email | 1.2 | Second attachment mismatch |
| 14 | Email | 1.2 | 102000 is USD Cash - Payroll, FX cannot apply |
| 15 | Reminder | 1.1 | Reminder for chase-before-FP-2026-05-certifies |
| 16 | Reminder | 1.2 | Reminder framed distinctly from reminder_scen_009_orphan_exception_0000 and _0008 |
| 17 | Final | 2.1 | Actual precedent period: FP-2025-12 (not FP-2025-11) |
| 18 | Final | 2.1 | Actual precedent figure: $617.63 (not $42) |
| 19 | Final | 2.1 | Actual precedent cause label: unrecorded_invoice (not subledger_feed_drop) |
| 20 | Final | 2.1 | Actual precedent close-out: corrective JE posted on BL-782A2EC69343 (not accept-timing) |
| 21 | Final | 2.1 | FP-2025-11 BL-8DCA6908E272 variance $3.42 refutation |
| 22 | Final | 2.1 | First attachment mismatch (evid_6cbb5c1605904b -> Marketing/BD doc) |
| 23 | Final | 2.1 | Second attachment mismatch (evid_6969ca2fd0a345 -> AICPA dues doc) |
| 24 | Final | 2.1 | 102000 is USD Cash - Payroll, FX cannot apply |

---

## Prompt sentence -> OE step(s) -> rubric(s)

| Prompt sentence (abridged) | OE steps | Rubric indices |
|---|---|---|
| "I prepared the cash-payroll recon for the May close and the exception on it is now lined up for accept-timing on a precedent someone cited in the channel and on the supporting evidence stapled to the recon." | OE 1-5 (persona lookup, period status, recon retrieval, account check, exception retrieval) | Context only; no rubric. Drives the discovery flow that backs every downstream rubric. |
| "The read going around does not match how the records sat when I put the recon together, so I want to re-check both pieces against what is actually there before this gets locked in." | Framing across all OEs | All 24 rubrics (frames the records-check mandate). |
| "Take the precedent claim from where it was raised. Tell me what period it points to, the figure, the cause it is citing, and how it was closed out." | OE 6, 7 (Slack thread + George reply retrieval) | Implicit in 17 / 18 / 19 / 20 (the four-pillar contrast format embeds the claim). |
| "Then take it apart on all four: same account, same period, same cause label, same close-out path." | OE 10 (FP-2025-11 recon), OE 11 (FP-2025-11 feed run), OE 12 (precedent search), OE 13 (precedent retrieval), OE 14 (precedent recon retrieval) | 17, 18, 19, 20, 21 (final response), 10, 11 (email), 2, 3 (vault). |
| "Pull the record for the period that was named and lay it next to the claim." | OE 10 (BL-8DCA6908E272 retrieval) | 21 (final), 11 (email), 3 (vault) [NEW]. |
| "If that period is not the closest fit for what we are actually seeing on this account, tell me which recent prior-period record on this account is the closer fit, and what that one shows on the same four." | OE 12, 13, 14 (find + read actual precedent) | 17, 18, 19, 20 (final, four pillars), 10 (email), 2 (vault). |
| "I want the real prior-period shape on this account, not the framing in the thread." | Reinforcement | Same as above (no additional rubric). |
| "Do the same on the supporting evidence the recon is leaning on. Read what each piece is labelled as." | OE 15 (blackline_evidence dump for BL-333FF9956BC6) | 22, 23 (final), 12, 13 (email), 4, 5 (vault). |
| "Then open the underlying documents and see what they cover." | OE 16, 17 (records_vault_get_document on doc_01b7c6e1cbe94529 and doc_b3633a2899a04e9e) | 22, 23 (final), 12, 13 (email), 4, 5 (vault). |
| "If the contents do not back the cause the recon is asserting, say so plainly." | OE 4 (USD-cash account confirmation), OE 24 (final response synthesis) | 24 (final), 14 (email), 6 (vault) [NEW] — the structural disproof that FX cannot apply, plus the evidence-mismatch rubrics that show the cause is not backed by the attachments either. |
| "When you have the picture, drop a write-up of what you saw on the prior-period record and the documents into the vault under the close-cycle file so it is on hand for George." | OE 20 (records_vault_upload_document) | 1, 2, 3, 4, 5, 6 (vault block). |
| "Drop a short note into the channel the precedent was raised in so the thread sees something was checked against the records." | OE 21 (slack_conversations_add_message thread reply on C005 thread_ts 1780147500.000000) | 7, 8 (Slack block). |
| "And send George a direct line letting him know what the records actually show on each piece, so he has it before he takes the disposition." | OE 19 (contacts_search_contacts for George), OE 22 (email_send_email to George) | 9, 10, 11, 12, 13, 14 (email block). |
| "Set me a reminder to chase this with George before the period certifies." | OE 18 (reminder_get_all_reminders for existing context), OE 23 (reminder_add_reminder for the new chase) | 15, 16 (reminder block). |
| "Tell me what you found and where you left it." | OE 24 (final response synthesis) | 17, 18, 19, 20, 21, 22, 23, 24 (final response block). |

---

## OE step -> rubric reverse-coverage

| OE | Step | Rubric(s) checking this |
|---|---|---|
| OE 1 | Persona contact lookup | 9 (email sender = ben.arinzo) |
| OE 2 | FP-2026-05 period status | 15 (reminder due before period certifies) |
| OE 3 | BL-333FF9956BC6 retrieval | 1 (vault related_resource), 8 (Slack content), 15 (reminder content) |
| OE 4 | 102000 account confirmation (USD Cash - Payroll) | 6 (vault), 14 (email), 24 (final) |
| OE 5 | exc_aade06f6129e43 retrieval | 8 (Slack content), 15 (reminder content), 16 (reminder framing distinct) |
| OE 6 | Slack thread search | 7 (Slack thread reply target) |
| OE 7 | Slack thread replies retrieval (George's claim) | 17, 18, 19, 20 (final response contrasts the claim) |
| OE 8 | Email disposition thread | Context only (informs L9 authority overlay) |
| OE 9 | Messaging conversation | Context only (informs L9 authority overlay) |
| OE 10 | BL-8DCA6908E272 retrieval (FP-2025-11 102000 recon) | 3 (vault), 11 (email), 21 (final) |
| OE 11 | FP-2025-11 feed run retrieval | Context only (informs Slack note + final response framing) |
| OE 12 | blackline_list_exceptions filter to brookfield/102000 | 2 (vault), 10 (email), 17 (final) - all depend on finding exc_d8fc13aa2cc742 |
| OE 13 | exc_d8fc13aa2cc742 retrieval | 2 (vault), 10 (email), 17, 18, 19, 20 (final four pillars) |
| OE 14 | BL-782A2EC69343 retrieval (corrective-JE recon) | 2 (vault), 10 (email), 20 (final close-out) |
| OE 15 | blackline_evidence dump for BL-333FF9956BC6 | 4, 5 (vault), 12, 13 (email), 22, 23 (final) |
| OE 16 | doc_01b7c6e1cbe94529 retrieval (Marketing/BD) | 4 (vault), 12 (email), 22 (final) |
| OE 17 | doc_b3633a2899a04e9e retrieval (AICPA dues) | 5 (vault), 13 (email), 23 (final) |
| OE 18 | Reminder list (existing two reminders) | 16 (reminder framed distinctly) |
| OE 19 | George contact lookup | 9 (email recipient) |
| OE 20 | Records Vault upload | 1, 2, 3, 4, 5, 6 |
| OE 21 | Slack thread reply on C005 | 7, 8 |
| OE 22 | Email to George | 9, 10, 11, 12, 13, 14 |
| OE 23 | Reminder add | 15, 16 |
| OE 24 | Final response | 17, 18, 19, 20, 21, 22, 23, 24 |

---

## Hardness lever -> rubric coverage (B4)

| Lever | Prompt surface | OE step(s) | Rubric(s) | Fact_Ledger atoms touched |
|---|---|---|---|---|
| **P1 latching** (Slack triage thread + 2 disposition emails + 1 messaging convo all agree on accept-timing) | "precedent someone cited in the channel and on the supporting evidence stapled to the recon" + "The read going around does not match how the records sat" | OE 6, 7, 8, 9 | 7, 8 (Slack reply confirms records check happened, does not endorse the thread); contrasts in 17-20 prove the agent rejected the latched narrative | slack ts 1780147500.000000 / 1780152480.000000 / 1780323420.000000; emails email_scen_009_orphan_exception_0006 / _0007; conversation_scen_009_orphan_exception_0001 |
| **P2 structured-DB skip** (blackline_evidence -> RV doc) | "the supporting evidence stapled to the recon ... Read what each piece is labelled as. Then open the underlying documents and see what they cover" | OE 15, 16, 17 | 4, 5 (vault), 12, 13 (email), 22, 23 (final) — 6 rubrics requiring the chase through blackline_evidence then records_vault | evid_6cbb5c1605904b, evid_6969ca2fd0a345, doc_01b7c6e1cbe94529, doc_b3633a2899a04e9e |
| **P7 multi-write diversification** (vault + Slack + email + reminder = 4 writes across 3 services) | "drop a write-up ... into the vault" + "Drop a short note into the channel" + "send George a direct line" + "Set me a reminder" | OE 20, 21, 22, 23 | 1 (vault), 7 (Slack), 9 (email), 15 (reminder) — one 1.1 per write surface | records_vault, slack, email, reminder write events |
| **P8 multi-link chain** (George's claim -> blackline_list_exceptions filtered to brookfield/102000 -> exc_d8fc13aa2cc742 -> resolution_summary -> derive corrective-JE remediation) | "tell me which recent prior-period record on this account is the closer fit, and what that one shows on the same four" | OE 12, 13, 14 | 2 (vault), 10 (email), 17, 18, 19, 20 (final four pillars), and 3 (vault), 11 (email), 21 (final) for the FP-2025-11 contrast — 9 rubrics total anchored on the precedent dig | exc_d8fc13aa2cc742 (all fields), BL-782A2EC69343, BL-8DCA6908E272 |
| **P9 universe-grounded gotcha** (102000 is USD Cash - Payroll on brookfield so FX revaluation cannot create variance) | "If the contents do not back the cause the recon is asserting, say so plainly" | OE 4 (account confirmation) + OE 20(c), OE 22, OE 24 (write surface delivery) | 6 (vault) [NEW], 14 (email), 24 (final) — 3 rubrics across all 3 write surfaces | oracle_gl.ogl_accounts.json (102000 / brookfield / Cash - Payroll) |
| **L9 authority-dismissal overlay** (Ryan recommends, George cites, Hannah signs, Daniel approves, Blue executes - all five align on the wrong call) | The whole "re-check both pieces against what is actually there before this gets locked in" framing | OE 6, 7, 8, 9 (read the five-way alignment) | Implicit in every rubric that requires the agent to override the disposition cluster's consensus by surfacing the records | All conversational anchors above |

All 6 levers trace prompt sentence -> OE step -> rubric -> Fact_Ledger atom end-to-end.

---

## Coverage gap check

- **Every prompt ask covered?** Yes. 14 explicit prompt sentences map to at least one rubric (excluding pure framing). The four-pillar comparison, the evidence chase, and all four writes have dedicated rubric coverage.
- **Every rubric tied to a prompt ask?** Yes. The reverse table above shows every rubric (1-24) anchors to a specific prompt sentence + OE step + Fact_Ledger atom.
- **No process rubrics smuggled as outcomes?** Confirmed - 24/0 split. All rubrics are write-action or fact-reporting, none describe execution traces.

## Soft caveats carried forward (non-blocking)

- **F-AUDIT3-trade** — Stripping `approximately` from `$617.63` / `$3.42` / `$42` introduces rounding-rigidity risk per `Always_Failing_Rubrics.md` Example 3. Bounded by `(or similar)` on every affected rubric. Risk LOW-MEDIUM on $617.63; LOW on $3.42 and $42. If verifier trajectories show systematic rounding fails, re-add `approximately` on R11 (email FP-2025-11) and R21 (final FP-2025-11) first.
- **USD derivation** — Account currency for 102000 derives via `entity_id: brookfield` (US-domiciled firm per universe constants) rather than an explicit `currency` field on the account record. Per universe convention, not blocking.

---

**Coverage matrix complete. Producer phase (S3) closed. Awaiting `PIPELINE FINAL — Tasks/27_6a39fd19048f9213281ec7b` in a fresh chat.**
