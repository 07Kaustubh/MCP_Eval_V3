# Council B — Adversarial QC + Density + Hardness Preservation

**Deliverable:** `Tasks/26_6a390e724c34487b95645dcc/5_Prompt.txt`
**Phase:** S1 prompt
**Persona:** Tom Chang (Tax Associate)
**Universe today:** 2026-06-12 (US/Eastern)
**Reviewer:** Council B (5-lens overlay: Architect, Implementer, Red-team, Ground-truth, Integration)

---

## Lens-by-lens read

| Lens | Verdict | Notes |
|---|---|---|
| Architect | GO | Three-movement structure (trigger → context → asks). Single coherent situation = morning queue cleanup before client signature returns. Multi-write diversity natural to the persona. |
| Implementer | GO | Every recipient resolves (Hannah, William, Daniel, Jones via persona references), the "tax channel" is `#tax-prep-and-filings` (C006), the "December period for Northstar" resolves uniquely to `northstar_legal_FP-2025-12` (closed 2026-01-05 — requires `late_post_authorization_id`). The vault retention referent ("our long tax-return retention" → `IRS_TAX_7Y`) and classification ("restricted") resolve. |
| Red-team | GO with note | Two reasonable readings exist on the exc_652 timing-recon item (dismiss-under-materiality vs reclass-via-4-eyes). This is the L9 trap working as designed, not a UGT defect at S1 phase. See B2 below. |
| Ground-truth | GO | Every concrete claim verified against per-task `_aux/Universe_Split/`. See B1 grounding column. No phantom tight identifiers (because no tight identifiers appear in the prompt). |
| Integration | GO | All 5 selected Hardness levers (L1, L2, L8, L9, L10) preserved end-to-end. No PROPAGATE-TO-HARDNESS flag. |

---

## [B1] QC sub-dim scoring

| Sub-dim | Score | One-line reason |
|---|---:|---|
| Coherence (Bolt-on) | 5 | Three ask-clusters unify under "clear my morning queue before partner signature returns / before day ends". Sentence-removal test does not produce a freestanding bolt-on; the exc_651 paragraph and the exc_151 paragraph both ground in Tom's "parked on my queue" framing. |
| Clarity & Specificity | 5 | All asks unambiguous as work items. The exc_652 dismiss-vs-reclass tension is the intentional L9 trap, not Clarity-side ambiguity (the universe state, not the prompt wording, drives the resolution). |
| Truthfulness | 5 | All persona references (Hannah, William, Daniel, Jones, Matthew/partner), entity (Northstar Legal), period (December for Northstar = FP-2025-12), exception traits (May timing recon sent June 1, the older Brookfield intercompany variance from last summer closed in August, partner confirmation in March, polling-bug context) verify against universe. No tight identifiers leaked → phantom-grep gate trivially passes. |
| Unique Ground Truth | 5 | The L9 mechanism (persona-stated dismiss vs universe `proposed_resolution`="Reclassify") is the intentional stump, not multi-end-state divergence at the prompt level. Universe state is determinate (reclass per BlackLine record); persona framing is the trap. Rubric set will resolve to the universe-grounded action. |
| Difficulty / Adversariality | 5 | All 5 levers (Latching, Structured-DB skip, Multi-link chain, Universe-grounded gotcha, L25 existing-output anchor) preserved by the framing. Stump hypothesis intact — agent must override persona on exc_652 and reconcile the doc_8f821bbad10c4eb4 "Signed/E-Filed" stub against the absent SALT late-post JE. |
| Contrived / Unnatural | 5 | Reads like a real tax-associate morning queue cleanup. No artificial precision, no contrived format, no command list. |
| Explicit Tool Mention | 5 | Zero tool names, zero MCP-server names, zero parameter names. References to systems are natural ("our ledger" is implicit via "stage the closed-period entry", "the vault" via "File a short support memo to the vault", "the tax channel"). |
| Feasibility | 5 | Every ask maps to an available MCP write tool (closed-period JE staging via late_post_authorization_id, Records Vault memo upload, email send, BlackLine exception update, reminder dismissal, Linear comment, Slack post). All required reads grounded in universe. |
| Investigation + Action | 5 | Heavy investigation feeding multiple writes across 5+ services. |
| Tool Use & Cross-service | 5 | 6+ writes across 5+ services (Oracle GL, Records Vault, Email, BlackLine, Reminder, Linear, Slack). |
| Persona / Voice Fidelity | 5 | Tom Chang's brief style ("approachable, fairly concise, moderately formal") matches. Word count ≈ 415 (well under 500). |
| Alignment with Today's Date | 5 | "this morning", "before the day ends", "last night" (William's 2026-06-11 reply), "on June 1" (Tom's scen_012 email), "back in March" (Matthew Li / James Randall sign-offs 2026-03-16), "last summer" / "in August" (exc_151 closure 2025-08-06) all resolve cleanly against universe today 2026-06-12. |
| Business Function | 5 | Tax (federal + multi-state returns, stale-SLA reminders, BlackLine exception triage, Records Vault tax memos) — matches Tom Chang's portfolio in PersonaBrief. |

**Grounding spot-checks (sample of A-zone grounding evidence, repeated here for B1 confidence):**

| Claim in prompt | Universe ground |
|---|---|
| Hannah / Step 3 partner package / William cleared | `email.emails.json`:email_scen_068_northstar_annual_corp_tax_0006 (Hannah → William, "routing for Step 3 partner review and authorization") + email_scen_068_northstar_annual_corp_tax_0008 (William's reply, "treat this reply as my authorization of record for the closed-period late-post to northstar_legal FP-2…") |
| "trial balance we locked in our December period for Northstar" | `oracle_gl.ogl_fiscal_periods.json`:northstar_legal_FP-2025-12 closed 2026-01-05 |
| SALT shortfall surfaced in review | `slack.slack_messages.json`:ts=1781013600.100000 (Hannah, "FY2025 SALT looks understated… versus LLP-level state estimated payments already made. Let's carry that as a review point") + ts=1781119800.200000 (Tom, "a SALT accrual shortfall of $4,820.30 based on account 230000 versus year-end state estimated payments") |
| William's reply = authorization of record for closed-period booking | email_scen_068_…_0008 verbatim |
| "May timing recon I sent Daniel for sign-off on June 1" | `blackline.blackline_exceptions.json`:exc_652c0931bb2546 (timing_difference_over_sla, brookfield_FP-2026-05, SLA due 2026-06-02, $9.61 on 260000) + email_scen_012_orphan_exception_0006 (Tom → Daniel, "Approval request to dismiss exc_652c0931bb2546 under materiality", parent=None, naturally fits "June 1"). State=awaiting_approval ✓. |
| "Jones and I had landed on dismissing under materiality" | exc_652c0931bb2546.identified_by = jones.harrison@brookfieldcpas.com ✓ |
| Stale tickler / Brookfield intercompany variance / closed in August | exc_151b0bee7e374e (unrecorded_invoice on 110000 Brookfield, brookfield_FP-2025-07, state=closed, resolution_executed_at = 2025-08-…). Description: "Intercompany clearing journal didn't sweep on schedule." ✓ |
| Partner-level confirmation in March that reminder was fine to dismiss / polling-bug side note | email_scen_001_orphan_exception_0007 (Matthew Li → Tom, "You're fine to dismiss the reminder on exc_151b0bee7e374e. … What is not fine is seeing three stale ticklers in one quarter. Please push the polling-bug ops ticket up the priority list…"). Date in chain → 2026-03 ✓ |
| "tax channel" | `slack.slack_channels.json`:C006 #tax-prep-and-filings ✓ |
| L25 anchor (NOT mentioned in prompt — must remain undisclosed) | `records_vault.rv_documents.json`:doc_8f821bbad10c4eb4 "Northstar Legal FY2025 Federal Form 1065 + State Returns - Signed/E-Filed", uploaded 2026-06-12 09:30 by persona_027 (Tom). Prompt makes no reference to this document → L25 trap intact ✓ |
| "open ops ticket for that polling bug" | Multiple email references in scen_001 chain confirm the polling-bug is tracked as an ops issue across the firm (Matthew Li: "push the polling-bug ops ticket up the priority list"). Linear issue corpus does not contain an exact-title match for the polling-bug ticket — the prompt's loose descriptor "the open ops ticket for that polling bug" lets the agent either find a semantically-close Linear issue or create one via `linear_create_issue`. Either is feasible. Loose-descriptor, not tight-identifier — does NOT trigger a Major. Flagged for S3 rubric phase to accept both find-and-comment and create-new dispositions. |

---

## [B2] Adversarial alt-path

Two reasonable readings exist on the exc_652c0931bb2546 ask:

- **Reading A (literal-persona compliance):** Tom directs "I want that actually pushed through and the exception closed out this morning" with "Jones and I had landed on dismissing under materiality". Agent dismisses exc_652 with disposition=materiality, closes the exception.
- **Reading B (universe-grounded override):** BlackLine `proposed_resolution`="Reclassify to the correct cost center via standard 4-eyes approval". Agent overrides Tom's framing and routes to 4-eyes reclass. Daniel Jones is the named approver on the exception record.

These two readings produce different write actions (dismiss vs reclass-route) and different final exception states. **This IS the L9 trap selected by HARDNESS phase**. It is not a UGT defect at the S1 prompt phase; the V3 framework explicitly uses persona-vs-universe contradiction as a stump mechanism. The rubric set (S3) must give credit only for Reading B (the universe-grounded reclass disposition). Council B at S1 phase notes this for downstream S2/S3 to encode correctly:

**Note to S3 author:** Outcome rubric for the exc_652 disposition must reward reclass-via-4-eyes (or equivalent override that preserves the BlackLine `proposed_resolution`), not dismissal under materiality. The prompt's literal directive is the trap; the rubric is the corrective. Do not let any Outcome rubric reward Reading A.

No second-reading attack found that would flip a recipient or final universe state outside the lever framework. No B2 BLOCK.

---

## [B3] Tool-call density projection

Trajectory sketch for a competent Opus-4.8 agent following the prompt:

| Step | Tool calls | Cumulative |
|---|---:|---:|
| Base discovery — contacts lookup (Hannah, William, Daniel, Jones, Matthew), Slack channel resolution (#tax-prep-and-filings → C006), fiscal-period resolution (Northstar December), today/horizon checks | 6 | 6 |
| Lever 1 (Latching) — read Hannah's slack ts=1781013600, read William's email_scen_068_0008 + parent thread, read Tom's own slack ts=1781119800 for SALT context | 6 | 12 |
| Lever 2 (Structured-DB skip) — query `ogl_journal_entries` for northstar_legal_FP-2025-12 + filter account 230000 (confirms zero in-period activity, only opening JE), pull subledger Cash Tax Reserve / 103000 outflows for derivation, recompute SALT shortfall | 5 | 17 |
| Lever 8 (Multi-link chain) — derive figure → identify William's email_id for `late_post_authorization_id` binding → stage closed-period JE → upload Records Vault memo with the JE link → email Hannah+William | 7 | 24 |
| Lever 9 (Universe-grounded gotcha) — read exc_652c0931bb2546 + BL-1F548113B049 recon detail + audit trail to confirm `proposed_resolution`="Reclassify"; override persona dismissal framing; route reclass via 4-eyes (BlackLine update + approval routing) | 4 | 28 |
| Lever 10 (L25 anchor) — Records Vault scan/list for existing Northstar FY2025 return docs → discover doc_8f821bbad10c4eb4 "Signed/E-Filed" stub → reconcile against absent SALT JE → confirm the SALT late-post must still be booked | 5 | 33 |
| Stale-tickler trail (exc_151b0bee7e374e) — BlackLine exception read, email_scen_001 reply-chain traversal (0005, 0006, 0007 to confirm James + Matthew dismissal sign-off and polling-bug context), reminder list + dismissal | 5 | 38 |
| Write actions — (1) GL JE staging (DR 530000 / CR 230000 in northstar_legal_FP-2025-12 with `late_post_authorization_id` = William's email_id), (2) Records Vault memo upload (kind=memo, classification=restricted, retention=IRS_TAX_7Y, tied to JE), (3) email to Hannah + William confirming late-post is staged, (4) BlackLine exc_652 update for reclass-via-4-eyes disposition, (5) Reminder dismissal on exc_151 tickler, (6) Linear find-or-create + comment on polling-bug ops ticket, (7) Slack post in C006 confirming close moving + backlog clear | 10 | 48 |
| Cross-service triangulation buffer — recon audit-trail confirms after JE post, return-success checks on each write, retention/classification verifications | 6 | 54 |

**Projected midpoint: ~54 tool calls** vs Hardness Plan's 52 midpoint. Range comfortably above 40 floor.

**B3 verdict:** PASS. Density well above the 40 floor; matches Hardness Plan projection.

---

## [B4] Hardness preservation

| Lever | Selected by HARDNESS? | Triggered by prompt as written? | Evidence in prompt |
|---|---|---|---|
| Lever 1 (Latching) | Yes | YES | "William cleared the Step 3 partner package… last night, including the state-and-local accrual piece we had open" + "ready for client signature" + "the package can move to the client for signature" — three close-framing anchors. |
| Lever 2 (Structured-DB skip) | Yes | YES | "I want the shortfall traced back through our own records on the Northstar side so the number we book is one we can ourselves stand behind, not one we copied off the messaging trail" — direct order to query GL/subledger, not lift from chatter. |
| Lever 8 (Multi-link chain) | Yes | YES | "Once you have a figure the records support, stage the closed-period entry on the Northstar December period and bind it back to William's reply as the authorization basis. File a short support memo to the vault… tied to the entry so the audit trail is clean. Then ping Hannah and William so they know the booking is live" — 4 hops preserved (derive → stage with auth-id → file memo bound to JE → notify). |
| Lever 9 (Universe-grounded gotcha) | Yes | YES | "Jones and I had landed on dismissing under materiality. I want that actually pushed through and the exception closed out this morning" — persona dismissal framing contradicts BlackLine `proposed_resolution`="Reclassify". Trap intact. |
| Lever 10 (L25 reversal/supersession) | Yes | YES | The prompt makes NO mention of the "Signed/E-Filed" Records Vault stub (doc_8f821bbad10c4eb4) uploaded 2026-06-12 09:30. Lever 10's mechanism requires the agent to independently discover and reconcile this existing-output anchor — preserved by omission. |

**B4 verdict:** PASS. No HARDNESS_REGRESSION.

---

## [B5] Tool-leak / phrasing scan

| Check | Hit? | Detail |
|---|---|---|
| Tool name in prompt body | NO | No `email_send_email`, `oracle_gl_post_journal_entry`, `blackline_update_exception`, `linear_create_issue`, etc. |
| Internal IDs (exc_*, BL-*, doc_*, JE-*, email_id, persona_*) | NO | No exception ids, recon ids, JE ids, doc ids, email ids, persona ids leaked. |
| Em-dashes (—) | NO | All sentence breaks are periods, commas, "since…", or natural conjunctions. |
| En-dashes (–) | NO | None. |
| "At least N" without prompt mandate | NO | Not used. |
| "Approximately" before IDs/dates | NO | Not used. |
| "(Or similar)" near exact values | NO | Not used. |
| Account number leak (230000, 530000, 103000) | NO | Prompt says "accrual housekeeping" and "the shortfall" — no account numbers. |
| Period ID leak (FP-2025-12) | NO | Prompt says "our December period for Northstar" — paraphrased. |
| Exact SALT figure leak ($4,820.30) | NO | Prompt says "the SALT shortfall" — no number. |
| doc_8f821bbad10c4eb4 / "Signed/E-Filed" upload mentioned | NO | Prompt does not name or hint at the L25 anchor doc. |
| MCP-server names | NO | Natural references only ("the vault", "tax channel", "ops ticket"). |

**B5 verdict:** PASS. Zero phrasing hits.

---

## [B6] Upstream propagation

Hardness Plan is the only upstream artifact for S1. Reviewing Hardness_Plan.md against the prompt as written:

- Levers selected match what the prompt surfaces. No mismatch.
- Density projection in Hardness Plan (52 midpoint) matches B3 trajectory sketch (54 midpoint). No mismatch.
- Stump hypothesis (4 predictions) all addressable through the prompt's framing. No mismatch.
- No factual claim in the prompt traces to a defect in Hardness Plan that would require re-running PIPELINE HARDNESS.

**B6 verdict:** PASS. No `PROPAGATE TO HARDNESS` flag.

---

## Forward notes for downstream phases (S2 OE, S3 rubrics, FINAL)

These are NOT BLOCKs on S1. They are heads-up flags so downstream phases encode the prompt's traps correctly:

1. **exc_652c0931bb2546 disposition (L9):** Outcome rubric must reward reclass-via-4-eyes (universe `proposed_resolution`), not dismissal-under-materiality (persona framing). Atomic Outcome rubric for the BlackLine update, separate from the audit-trail content rubric.
2. **doc_8f821bbad10c4eb4 reconciliation (L10):** Outcome rubric must reward the agent for proceeding with the SALT late-post JE despite the existing "Signed/E-Filed" stub. Add an Outcome rubric checking the agent did NOT defer the JE on the basis of the stub.
3. **"open ops ticket for that polling bug":** No exact-title Linear issue found in the per-task corpus. Outcome rubric must accept either (a) `linear_create_comment` on a semantically-close existing issue (e.g., the AP-side stale items if the agent reasons broadly) OR (b) `linear_create_issue` for a fresh polling-bug record + a follow-up comment. Both must reflect "this week" status per the prompt.
4. **SALT figure verification:** Outcome rubric for the staged JE should accept $4,820.30 (matches Tom's slack) provided the agent demonstrates verification against GL/subledger (Lever 2 satisfied), since the persona explicitly directs "the number we book is one we can ourselves stand behind". Do not accept the figure if the agent skipped the GL/subledger triangulation step.
5. **`late_post_authorization_id` binding:** Outcome rubric must require the email_id of email_scen_068_northstar_annual_corp_tax_0008 (William's reply) in the `late_post_authorization_id` parameter of the staged JE. This is the lever-8 fourth hop.

---

## Verdict

- B1 QC sub-dims: all 5. PASS.
- B2 Adversarial alt-path: no defect-side divergence; the divergence found IS the intended L9 trap. PASS.
- B3 Density: projected 54 calls midpoint, above 40 floor. PASS.
- B4 Hardness preservation: all 5 selected levers triggered by the prompt. PASS.
- B5 Phrasing scan: zero hits. PASS.
- B6 Upstream propagation: no PROPAGATE-TO-HARDNESS flag. PASS.

VERDICT: GO
