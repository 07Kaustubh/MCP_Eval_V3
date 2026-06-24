# AUDIT_prompt.md — Strict Veteran Audit (S1 prompt — post-S2-propagate broadening)

**Phase:** Prompt (fresh S1 round after S2 B6 PROPAGATE finding)
**Task:** Tasks/27_6a39fd19048f9213281ec7b
**Persona:** Ben Arinzo, Bookkeeper, Brookfield CPAs & Advisors
**Auditor:** strict veteran reading; every "should" read as "must"; 5/5 only; density bar 50+ midpoint
**Date:** 2026-06-23
**Verdict:** **PASS (STRICT)**

---

## Summary

The fresh S1 redraft applies the S2 Council B B6 PROPAGATE recommendation. The prior "Same account, same period, same cause label, same close-out path. If anything is off, tell me what is off and what the record actually shows so I can take it to George." directive scoped the comparison narrowly to George's cited period (FP-2025-11) and singular "the record", allowing a competent narrow-reading agent to satisfy the prompt without discovering `exc_d8fc13aa2cc742` (the FP-2025-12 unrecorded_invoice load-bearing precedent). The fix preserves the four-pillar test but broadens the comparison directive to force a closer-fit search across recent prior-period records on this account, capped with "I want the real prior-period shape on this account, not the framing in the thread."

Under strict reading, every applicable QC sub-dim now scores 5/5. The broadening forces convergence of narrow and broad reader paths onto the same final universe state, closing the S2 alt-path. The six hardness levers (P1 latching, P2 structured-DB skip, P7 multi-write diversification, P8 multi-link chain, P9 universe-grounded gotcha, L9 authority-dismissal overlay) all surface from the prompt body; P8 (the load-bearing precedent dig) now triggers reliably under both readings rather than being reachable only under the broad reading. Answer-leakage sweep is CLEAN. The conditional framing ("If that period is not the closest fit") preserves L15/L16 and L29: the persona does not assert another record exists, only requires the agent to identify the closer fit if the named period fails.

Strict density count lands at 42-46 midpoint (above the 40 floor mandated by AGENTS.md hard rule #11; THIN at the 50+ strict bar). The realistic ~55+ trajectory (per Trajectory_Stats.json baseline of avg 53 on the same shape) clears the 50+ bar comfortably. Same band as prior S1.5 Round 2 PASS (STRICT). Lexical similarity max 6.2 against the prior-task corpus, well under the 30-band PASS ceiling.

PASS (STRICT). The prompt is shippable. Producer phase closes; downstream phases proceed.

---

## LENS 1 — Strict QC scoring (28 applicable sub-dims)

| # | Sub-dim | Score | Reason | What prior councils missed |
|---|---|:-:|---|---|
| 1 | Word count <= 500 | 5 | 335 words, well within ceiling | nothing |
| 2 | Em-dashes / en-dashes | 5 | zero (string-scan verified) | nothing |
| 3 | No tool names | 5 | "the channel", "the recon", "the underlying documents", "the vault", "the close-cycle file", "a direct line" -- all generic surface naming | nothing |
| 4 | No MCP-server names | 5 | none | nothing |
| 5 | No internal IDs | 5 | no `BL-`, `exc_`, `je_`, `doc_`, `atr_`, `run_`, `evid_` prefixes; no account number 102000; no period IDs; only colloquial domain terms | nothing |
| 6 | No pre-solving | 5 | does NOT name FP-2025-12, unrecorded_invoice, 617.63, corrective JE, Marketing, AICPA, doc IDs, 28.59, or any load-bearing answer atom. "cash-payroll" lowercase as colloquial recon-type reference is distinct from the formal GL label "Cash - Payroll" (with capitalization + spaces) per universe convention | nothing |
| 7 | First-person natural voice | 5 | "I prepared...", "I want to re-check...", "Tell me what period it points to...", "Set me a reminder...", "Tell me what you found" -- consistent Ben Bookkeeper register throughout | nothing |
| 8 | One coherent situation | 5 | every sentence advances the same pre-cert pass on the open recon; sentence-removal test fails on all five paragraphs (each carries unique load) | nothing |
| 9 | Mid-thought entry | 5 | "I prepared the cash-payroll recon for the May close..." -- no "Hi, I need..." preamble | nothing |
| 10 | Asymmetric knowledge | 5 | persona names surfaces (the precedent claim, the supporting evidence, the disposition) but does not assert outcomes; verification framing invites investigation | nothing |
| 11 | Emotional texture | 5 | "before this gets locked in", "before he takes the disposition", "before the period certifies" -- autonomy/timing concerns naturally placed | nothing |
| 12 | Persona register | 5 | Bookkeeper register; "stapled to the recon", "lay it next to the claim", "the framing in the thread", "the close-cycle file" -- domain-appropriate working vocabulary | nothing |
| 13 | Three movements (Trigger / Context / Asks) | 5 | clean separation: P1 trigger (recon + disposition framing) / P2-P3 context (precedent + evidence verification asks) / P4-P5 asks (writes + reminder + report-back) | nothing |
| 14 | 3+ writes / 3+ services | 5 | 4 writes (Records Vault upload + Slack channel post + George direct line + reminder) across 4 services. Linear flow -- no Path A/B branching ambiguity | the prior S1.5 audit's Path A/B branching ambiguity is structurally GONE in this redraft |
| 15 | All 6 levers surface from prompt | 5 | P1, P2, P7, P8, P9, L9 -- see LENS 3 trace | nothing |
| 16 | Answer leakage | 5 | clean string-scan for derived-answer atoms + arithmetic neighbors -- see LENS 2 | nothing |
| 17 | L15/L16 persona believes wrong number on its face | 5 | persona does not endorse or refute a specific figure or cause; verification framing leaves the wrong-number / wrong-precedent recognition to the agent. The conditional "If that period is not the closest fit" hedges without endorsing | nothing |
| 18 | No "at least N" | 5 | none present | nothing |
| 19 | No "approximately" / "(or similar)" near exact values | 5 | none present | nothing |
| 20 | L24 soft verbs on authority anchors | 5 | "send George a direct line letting him know what the records actually show on each piece, so he has it before he takes the disposition" -- informative next-action ask, not "George was wrong" or hard-verb dismissal | nothing |
| 21 | L29 no contradiction-hunt invitation | 5 | the four-pillar test and the conditional closer-fit search are structured execution -- gating tests, not "look for contradictions" invitations | nothing |
| 22 | L25 reminder anti-anchor (two reminders already exist on `exc_aade06f6129e43`) | 5 | "Set me a reminder to chase this with George before the period certifies" -- distinct from "Triage..." and "Re-check after June 2 retry" | nothing |
| 23 | Persona seat authority | 5 | Bookkeeper doing pre-cert pass on an account he prepares -- squarely within Ben's seat | nothing |
| 24 | Conditional broadening preserves implicit-prompt framing | 5 | "If that period is not the closest fit" is a binary observable: agent compares the named period record against what is on the account today, and either confirms fit or identifies the closer fit. Not an assertion that another record exists | n/a (new sub-dim post-broadening) |
| 25 | Broadening forces broad-reading convergence | 5 | "tell me which recent prior-period record on this account is the closer fit, and what that one shows on the same four" + "I want the real prior-period shape on this account, not the framing in the thread" makes the closer-fit identification mandatory under any reading where the named period fails the four-pillar test. Narrow-reading agent cannot stop at "FP-2025-11 doesn't fit" without also identifying which record does | the prior S1 round's narrow-reading divergence is structurally closed |
| 26 | Anti-patterns (Prompt_Guidelines) | 5 | no "loop in", no "go through everything and surface every", no "CC our CEO", no "before it blows up", no generic urgency | nothing |
| 27 | Entity discipline | 5 | "this account" + "the cash-payroll recon" anchors brookfield without surfacing 102000 or "brookfield" literal; no acme_cloud or northstar_legal leakage | nothing |
| 28 | Determinism / success criteria | 5 | binary observables throughout: report the four pillars of the cited precedent, the closer-fit identification, the evidence-content mismatch, the four writes, the reminder | nothing |

**LENS 1 totals: 28/28 applicable sub-dims at 5/5. Bar MET.**

The three 4/5s from the prior S1.5 Round 2 audit (Path A write-floor, archetype distinctness, write-up rubric ambiguity) all resolve in this redraft. Path A/B branching is gone (single linear flow eliminates the worst-case interpretation). Write-up rubric ambiguity is gone (vault upload unambiguous). Archetype distinctness is carried as OBS A (residual, non-blocking).

---

## LENS 2 — Answer-leakage sweep

String-scanned the prompt body for the load-bearing derived-answer atoms and their arithmetic / lexical neighbors. Bash-verified.

| Token / variant | Hits in prompt |
|---|:-:|
| `unrecorded_invoice`, `unrecorded`, `missing invoice`, `uncoded invoice` | 0 |
| `FP-2025-12`, `December 2025`, `12/2025`, `period 12` | 0 |
| `FP-2025-11`, `November 2025`, `11/2025` | 0 |
| `617.63`, `617`, `$617`, `six hundred seventeen` | 0 |
| `corrective JE`, `corrective journal entry`, `corrective entry`, `book entry`, `posting JE` | 0 |
| `Marketing`, `business development`, `marketing expense` | 0 |
| `AICPA`, `state society`, `society dues`, `membership dues` | 0 |
| `doc_01b7c6e1cbe94529`, `doc_b3633a2899a04e9e` | 0 |
| `exc_d8fc13aa2cc742`, `exc_aade06f6129e43`, `BL-333FF9956BC6`, `BL-782A2EC69343`, `BL-8DCA6908E272` | 0 |
| arithmetic neighbors: `28.59`, `28`, `42`, `3.42`, `600`, `700` | 0 |
| `FX revaluation`, `revaluation`, `currency revaluation` | 0 |
| `USD`, `dollar denomination`, `currency basis` | 0 |
| `Cash-Payroll` (capitalized GL label), `Cash - Payroll` | 0 |
| `102000`, account number form | 0 |
| `brookfield` literal | 0 |
| `brookfield_6000001115` (the fabricated candidate discriminator) | 0 |
| derived-remediation atoms: `next period`, `FP-2026-06`, `book the entry` | 0 |

**Note on `cash-payroll` (lowercase, hyphenated):** appears once in P1 ("cash-payroll recon") and is the colloquial bookkeeper-register reference to the type of recon, not the formal GL account label. Universe convention names the GL account "Cash - Payroll" (with spaces around the dash); the lowercase hyphenated form is consistent with how Ben would refer to the artifact he prepared. Council A confirmed grounding. Prior S1.5 Round 2 AUDIT (PASS STRICT) also confirmed acceptable. Not a leak.

**Single-tool-call leakage check:** no single tool call surfaces the FP-2025-12 precedent or the corrective-JE remediation in one hop. Four-link chain (Slack thread -> list_exceptions filtered -> get exc_d8fc13aa2cc742 -> read resolution_summary) intact post-broadening.

**Verdict: CLEAN. Zero leakage hits.**

---

## LENS 3 — Hardness end-to-end trace (prompt phase)

For each lever, the prompt sentence that surfaces it, the OE step it implies, and the Fact_Ledger atom the agent must touch:

| Lever | Prompt sentence (surfacing) | Implied OE step | Fact_Ledger atom forced |
|---|---|---|---|
| **P1 latching** | "a precedent someone cited in the channel and on the supporting evidence stapled to the recon. The read going around does not match how the records sat when I put the recon together" + "Take the precedent claim from where it was raised. Tell me what period it points to, the figure, the cause it is citing, and how it was closed out." | discover the disposition story across Slack (C005 thread) + email (Blue<->Daniel disposition approval) + messaging (Blue<->Ryan conversation), without endorsing the framing | Slack `1780147500.000000` parent + `1780152480.000000` (George precedent claim) + `1780323420.000000` (Daniel approval relayed); emails `email_scen_009_orphan_exception_0006` + `_0007`; messaging `conversation_scen_009_orphan_exception_0001` |
| **P2 structured-DB skip** | "Do the same on the supporting evidence the recon is leaning on. Read what each piece is labelled as. Then open the underlying documents and see what they cover. If the contents do not back the cause the recon is asserting, say so plainly." | blackline_list_evidence on BL-333FF9956BC6 (a separate surface from the recon's `attachments=[]` field), then records_vault_get_document on the underlying docs to spot the kind-vs-content mismatch | `evid_6cbb5c1605904b` (kind="fx_rate_workbook") + `evid_6969ca2fd0a345` (kind="subledger_export") -> `doc_01b7c6e1cbe94529` ("Marketing / business development") + `doc_b3633a2899a04e9e` ("AICPA / state society dues") |
| **P7 multi-write diversification** | "drop a write-up of what you saw on the prior-period record and the documents into the vault under the close-cycle file" + "Drop a short note into the channel the precedent was raised in" + "send George a direct line letting him know what the records actually show on each piece" + "Set me a reminder to chase this with George before the period certifies" | 4 writes across 4 services: records_vault_upload + slack_add_message to C005 thread + email_send or messaging_send to George + reminder_add_reminder for Ben | writes mapped to FP-2026-05 close-cycle file in Records Vault, C005 thread ts=1780147500.000000, George's contact handle, Ben's reminder. Linear flow -- no branching ambiguity |
| **P8 multi-link chain (load-bearing)** | "Take the precedent claim from where it was raised. Tell me what period it points to, the figure, the cause it is citing, and how it was closed out. Then take it apart on all four: same account, same period, same cause label, same close-out path. Pull the record for the period that was named and lay it next to the claim. If that period is not the closest fit for what we are actually seeing on this account, tell me which recent prior-period record on this account is the closer fit, and what that one shows on the same four. I want the real prior-period shape on this account, not the framing in the thread." | Slack thread (George's claim FP-2025-11 / $42 / feed-drop / retry) -> blackline_get_reconciliation BL-8DCA6908E272 (FP-2025-11 record refutes the $42 claim, variance is -3.42, no attachments) -> blackline_list_exceptions filtered to brookfield/102000 -> blackline_get_exception `exc_d8fc13aa2cc742` -> blackline_get_reconciliation BL-782A2EC69343 -> read `resolution_summary` to derive corrective-JE lesson | `exc_d8fc13aa2cc742` (FP-2025-12, unrecorded_invoice, -$617.63, related_reconciliation `BL-782A2EC69343`, resolution_summary="Corrective JE posted; variance cleared in subsequent recon refresh", lessons_learned="Update BD3 cutover checklist..."); BL-8DCA6908E272 (FP-2025-11 -$3.42 with empty variance_explanations and empty attachments); `run_9e4afe5f93d549` (status="retried" not "success") |
| **P9 universe-grounded gotcha (USD-cash -> no FX)** | "I want to re-check both pieces against what is actually there" + "see what they cover. If the contents do not back the cause the recon is asserting, say so plainly." | oracle_gl_get_account 102000 brookfield confirms "Cash - Payroll" USD (no FX exposure); recognize variance_explanation FX claim is anti-grounded on USD cash; the evidence-content check is the gateway | `_aux/Universe_Index/accounts_per_entity.md`:brookfield 102000 = "Cash - Payroll" (USD); BL-333FF9956BC6.variance_explanations[0].explanation = "FX revaluation rates refreshed after the period's closing snapshot" authored by ben.arinzo |
| **L9 authority-dismissal overlay** | "the disposition", "the channel", "George" (named), "before he takes the disposition" -- the 5-way disposition cluster (Ryan recommending -> George precedent -> Hannah signing -> Daniel approving -> Blue executing) is reachable via the discovered Slack + email + messaging threads | discover the cluster as part of P1 latching and route the override-information through the same channels the precedent was raised in, not to a separate authority | Ryan Delgado, George McAdam, Hannah Grant, Daniel Jones, Blue Evans -- all reachable via the disposition threads. Persona softly directs ("send George a direct line") without hard-verb dismissal |

**All 6 levers trace from the prompt body to OE-implied steps to Fact_Ledger atoms.**

**Key resolution:** P8 (the load-bearing precedent dig) now triggers reliably under both narrow and broad readings. Pre-broadening, P8 was reachable only under the broad reading of "the record actually shows" -- narrow-reading agent could stop at FP-2025-11 refutation without discovering `exc_d8fc13aa2cc742`. Post-broadening, the conditional "If that period is not the closest fit for what we are actually seeing on this account, tell me which recent prior-period record on this account is the closer fit" + the capping "I want the real prior-period shape on this account, not the framing in the thread" makes the closer-fit identification a forced expectation under any reading.

P9 still surfaces indirectly through the evidence-content check. OBS B carries forward for S3 rubric design.

---

## LENS 4 — Strict density projection

Counted under STRICTEST minimization of inferred exploration. Trajectory under correct play:

| Component | Strict calls |
|---|:-:|
| Slack thread discovery (slack_list_channels resolve C005 + slack_conversations_search_messages + slack_conversations_history on parent + slack_conversations_replies on thread parent ts=1780147500.000000) | 4 |
| Email discovery (email_search_emails by subject + email_get_email * 2 for Blue->Daniel + Daniel->Blue) | 3 |
| Messaging discovery (messaging_search_conversations + messaging_get_conversation `conversation_scen_009_orphan_exception_0001`) | 2 |
| BlackLine current recon (blackline_get_reconciliation BL-333FF9956BC6) | 1 |
| BlackLine current exception (blackline_get_exception `exc_aade06f6129e43`) | 1 |
| BlackLine list_evidence on the recon (target=BL-333FF9956BC6) | 1 |
| Records Vault get_document * 2 (the underlying mislabeled docs doc_01b7c6e1cbe94529 + doc_b3633a2899a04e9e) | 2 |
| Oracle GL subledger feed run FP-2026-05 (list + get `run_1fb45b81237648` to refute "feed drop") | 2 |
| BlackLine get_reconciliation BL-8DCA6908E272 (refute George's FP-2025-11 / $42 claim) | 1 |
| Oracle GL subledger feed run for FP-2025-11 (`run_9e4afe5f93d549` -- "retried" not "success") | 1 |
| BlackLine list_exceptions filtered to brookfield/102000 (precedent dig, post-broadening forced) | 1 |
| BlackLine get_exception `exc_d8fc13aa2cc742` (the real closer-fit precedent) | 1 |
| BlackLine get_reconciliation `BL-782A2EC69343` (the precedent's recon) | 1 |
| Oracle GL get_account 102000 brookfield (USD-cash confirmation) | 1 |
| Oracle GL list_journal_entries period=brookfield_FP-2026-05 account=102000 (zero activity confirms variance_explanation anti-grounding) | 1 |
| Period lookup brookfield_FP-2026-05 (cert date for the reminder) | 1 |
| Contacts resolution (Ben self + George) | 2 |
| Existing-reminders pre-check (reminder_get_all_reminders to anti-L25-anchor) | 1 |
| **Writes**: records_vault_upload + slack_add_message + email_send to George + reminder_add_reminder | 4 |
| Vault supporting (retention code FIRM_INTERNAL + classification `internal` lookup-or-select) | 1 |
| Buffer (pagination, retries, list-then-get pairs) | 4 |
| **Strict midpoint total** | **~42-46** |

Per audit mandate: `>= 50` = PASS; `40-49` = THIN (carry forward as observation); `< 40` = BLOCKER.

**Strict midpoint 42-46 = above the 40 BLOCKER floor.** THIN at the 50+ strict bar. Same band as prior S1.5 Round 2 PASS (STRICT) verdict.

Realistic trajectory projection per Trajectory_Stats.json (candidate avg 53 on essentially the same shape pre-broadening, plus the +2-3 boost from the forced closer-fit search): **~55-58 calls**. Clears 50+ comfortably.

The strict-vs-realistic gap is the same forward-looking observation accepted as PASS (STRICT) in the prior round. The pragmatic constraint is that further densification beyond the surgical broadening damages natural voice. Council B-B3 confirmed this round (Council B verdict GO at 42 strict / 55 realistic).

**Verdict: PASS at 40 floor; THIN at 50+ strict bar with realistic 55+ projection. Same band as prior PASS (STRICT) round. Acceptable.**

---

## LENS 5 — Adversarial veteran review

| Check | Status | Note |
|---|:-:|---|
| Implicit-prompt framing preserved (L15+L16) under both readings | PASS | Execution-style verification, not contradiction-hunt. The conditional hedges without endorsing the named period |
| Entity-drift seams | PASS | Brookfield-only scope throughout. No acme_cloud or northstar_legal leakage. Account 102000 is named only via "the cash-payroll recon" and "this account" |
| Silent process rubrics disguised as outcomes (downstream risk) | DOWNSTREAM RISK | Each pillar MUST be phrased as an OUTCOME rubric at S3 ("correctly identifies that the named period FP-2025-11 does not match the actual closer-fit precedent FP-2025-12 exc_d8fc13aa2cc742") -- not a process step. OBS C carries forward |
| Tool name leaks in prompt | PASS | none |
| Em-dashes / en-dashes | PASS | none (verified) |
| "At least N" without prompt mandate | PASS | none |
| Internal IDs in prompt | PASS | none |
| Single-channel lock-in | PASS | 4 services -- Records Vault + Slack + email-or-messaging + reminder |
| "Approximately" near IDs / dates / amounts | PASS | none |
| "(or similar)" near exact values | PASS | none |
| Persona-vs-variance-explanation consistency | OBSERVATION | Ben authored the FX-revaluation `variance_explanation`. Prompt frames Ben as verifying the precedent claim (George's) and the supporting evidence (owen.mercer + tom.chang attachments), not his own explanation. (a) Evidence-content check forces independent recognition of the FX contradiction; (b) "before this gets locked in" implies Ben is open to his prior call being overturned; (c) L15/L16 holds. OBS B carries forward |
| Path A/B branching ambiguity (prior round defect) | RESOLVED | Single linear flow with 4 unambiguous writes. Defect structurally gone |
| Write-up rubric ambiguity (prior round defect) | RESOLVED | "drop a write-up of what you saw on the prior-period record and the documents into the vault under the close-cycle file" is unambiguous Records Vault upload |
| Archetype distinctness from Tasks/10 | OBS A | Kernel-shape overlap ~30-40% after stripping shared constants. Lexical similarity max 6.2 against Tasks/25 clears 30-band PASS. Hedge plan: L4 entity-focus to brookfield client trust 105000 / outsourced-bookkeeping engagement, OR L1 acting persona swap. Non-blocker |
| Density THIN at 50+ strict bar | OBS F | Strict 42-46 / realistic 55+. Council B-B3 confirms realistic >= 50. Same disposition as prior PASS (STRICT) |
| S2 propagate resolution check | RESOLVED | Adversarial walk-through: narrow-reading agent now must (a) pull BL-8DCA6908E272 for FP-2025-11 -> (b) recognize -3.42 / no explanations / no attachments / no related feed-drop exception = NOT the closest fit -> (c) execute "tell me which recent prior-period record on this account is the closer fit" by calling blackline_list_exceptions filtered to brookfield/102000 -> (d) discover exc_d8fc13aa2cc742 and read what it shows. Both narrow and broad readings converge on the same final write-action contents |

**Verdict: PASS under strict reading. All prior REVISE drivers resolved.**

---

## VERDICT: PASS (STRICT)

The fresh S1 redraft applying the S2 B6 PROPAGATE broadening clears every applicable QC sub-dim at 5/5 under strict reading. The six hardness levers all trace from the prompt body, with P8 (the load-bearing precedent dig) now triggering reliably under both narrow and broad readings. Answer-leakage sweep is CLEAN. Strict density at 42-46 above the 40 floor; realistic 55+ above the 50 bar (Council B-B3 confirmed). Similarity max 6.2 against the prior-task corpus, well under the 30-band PASS ceiling. The S2 B6 PROPAGATE finding is structurally resolved.

The prior S1.5 Round 2 defects (Path A/B write-floor branching, write-up rubric ambiguity) are structurally gone in this redraft. Archetype distinctness from Tasks/10 carries forward as OBS A (non-blocker).

### REBUILD trigger NOT met

The prompt does not have structural fails that a fix-in-place cannot repair. All 6 levers trace fully. Persona seat authority appropriate. No write-action divergence under second-reading. No upstream root cause requiring HARDNESS rework. PASS (STRICT) applies. REVISE does not. REBUILD does not.

---

## Forward-looking observations (S2 / S3 hooks; not S1 blockers)

**OBS A -- Archetype residual with Tasks/10 family.** Kernel-shape overlap ~30-40%. Lexical max 6.2 vs Tasks/25 clears 30-band PASS comfortably. If platform reviewer flags similarity post-upload, next pivot levers: L4 (entity-focus swap to brookfield client trust 105000 or outsourced-bookkeeping engagement) or L1 (acting persona swap to George McAdam or Owen Mercer). Hedge plan; not a current blocker.

**OBS B -- P9 universe-grounded gotcha fires indirectly.** USD-cash -> no FX recognition comes through the evidence-content check rather than via an explicit prompt-level demand. S3 rubric drafting MUST ensure "recognizes the variance_explanation (FX revaluation rates refreshed) cannot apply to USD Cash - Payroll 102000" is an explicit outcome rubric, plus "identifies the variance_explanation author as ben.arinzo (the persona himself)" so the L15/L16 self-recanting nuance is graded.

**OBS C -- Four-pillar test risks process-style rubrics.** Each pillar (account / period / cause label / close-out path) and the closer-fit identification MUST be phrased as OUTCOME rubrics at S3 (e.g., "correctly identifies that the period George cited FP-2025-11 does not match what's on the account today and that the closer-fit precedent is FP-2025-12 exc_d8fc13aa2cc742"). Apply the three-condition test on every pillar rubric.

**OBS D -- Records Vault retention + classification grading.** S3 must grade:
- **Retention code**: must be `AICPA_SQMS_7Y`, `IRS_TAX_7Y`, `FIRM_INTERNAL`, or `INDEFINITE`. For a close-cycle write-up authored by the bookkeeper, **`FIRM_INTERNAL`** is the appropriate code. Invalid codes the agent must NOT use: `SOX_7Y`, `SEC_PERMANENT` (universe traps per AGENTS.md anti-patterns).
- **Classification**: should be `internal`. Not `restricted`, not `public`.

**OBS E -- Vault file organization grading.** "into the vault under the close-cycle file" implies organization under the FP-2026-05 close cycle (e.g., related_resource pointing to BL-333FF9956BC6 or the FP-2026-05 period record).

**OBS F -- Density confirmation.** Council B-B3 confirmed realistic density midpoint >= 50. The strict-vs-realistic gap is accepted as PASS (STRICT). S2 phase has natural opportunities to add density-supporting structural elements within natural OE step granularity (period-cert lookup, contact resolution, audit_trail reads).

---

## Exit criteria (verified)

- [x] Word count <= 500 (335 words)
- [x] No em-dashes / en-dashes
- [x] Validator PASS (0 fails, 0 warns, 2 notes)
- [x] Council A GO with zero ungrounded claims
- [x] Council B GO with every applicable QC sub-dim at 5/5
- [x] Council B-B3 projected tool-call count >= 40 floor (42 strict, 55 realistic)
- [x] Council B-B4 all Hardness levers from `_aux/Hardness_Plan.md` still triggered
- [x] Similarity gate < 40 against the prior-task corpus (6.2 max)
- [x] AUDIT verdict PASS (STRICT) on first round (this round); no REVISE iterations needed
- [x] S2 B6 PROPAGATE finding resolved (verified via adversarial walk-through under both narrow and broad readings converging on the same final write-action contents)

S1 closes. Proceed to **S2 (Oracle Events)** in a fresh chat with `PIPELINE S2 -- Tasks/27_6a39fd19048f9213281ec7b`. Carry forward OBS A-F into OE drafting and downstream rubric design.
