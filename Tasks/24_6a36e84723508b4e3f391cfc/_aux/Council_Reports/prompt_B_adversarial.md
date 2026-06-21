# Council B — Adversarial QC + Density + Hardness Preservation (S1 / Prompt)

Task: `24_6a36e84723508b4e3f391cfc`
Deliverable: `5_Prompt.txt` (478 words)
Universe today: 2026-06-12 (US/Eastern)
Persona: Lena Park (Procurement Officer) — TRIAGES, defers approval/routing to Daniel Jones + Steven Perry.

Five role lenses applied (Architect / Implementer / Red-team / Ground-truth / Integration), combined into B1-B5.

---

## [B1] QC Sub-Dim Scoring (prompt-phase, `Docs/7_QC_Spec_Doc1.json`)

| Sub-dim | Score | One-line reason |
|---|---:|---|
| Unique Ground Truth | 5 | Single end-state: 4 specified writes (payables-channel post, Linear comment on the existing orphan-approver ticket, email Daniel cc Steven, 7-day reminder) + compound-ranked vendor summary + per-vendor root-cause classification — no second reading yields a different write set or universe state. |
| Feasibility | 5 | All required surfaces (SAP subledger, Records Vault, Linear, email, Slack, reminders) are in the standard service inventory; nothing impractical for a single response. |
| Persona fit | 5 | Lena Park's procurement-triage voice, explicit "I am not approving or routing anything myself; Daniel and Steven own that call" — matches PersonaBrief authority pattern exactly. |
| Business-function fit | 5 | AP / Vendor Operations — pending-approval queue triage across 3 entities is dead-center for the assigned function. |
| Coherence | 5 | One cohesive situation: vendor complaints → queue triage → root-cause read → escalation evidence. Removing any sentence breaks the chain. |
| Contrived language | 5 | Narrative tone, no step-by-step command list, no artificial constraint stacking; compound-rank framing is naturally motivated ("long-aged mid-dollar item is not hidden behind something newer but bigger"). |
| Investigation pre-solved | 5 | Root-cause categories (orphan / disputed / missing credit memo) are options to classify per vendor, not the answer. Agent must diagnose. |
| Single-service tool use | 5 | Requires 6 services: SAP, Records Vault, Linear, email, Slack, reminders. |
| Maximalism | 5 | 4 writes × 3 entities × 3-5 vendor chain × 2-entity scope × prior-conversation cross-check. Density midpoint 47. (Prior candidate scored 1 here — explicit fix.) |
| Word count / format | 5 | 478 words ≤ 500. Three paragraphs. No em-dashes / en-dashes (`grep -P '[—–]'` returns 0). |
| Strict-language conventions | 4 | Two "at least" usages found: "at least two or three" (conversational vendor count — acceptable) and "at least one change order" (universe-grounded floor — the universe has exactly one change_order doc). Neither violates the linter rule (which targets rubric titles) and both are intentional, but flagging as a 4 with explicit awareness; see B5 watch-out. (Prior candidate scored 2; this is materially improved.) |
| Tool/system name leakage | 5 | No tool function names, no MCP server references, no internal IDs (apinv_*, doc_*, issue_*, VEN-*, exc_*, BL-*, C010, C005, C008). `grep` confirms NONE. |
| Truthfulness / lever fit | 5 | Every claim atom-anchored: Daniel Jones (Accounts Manager) + Steven Perry (Managing Partner) exist as contacts; payables channel resolves uniquely to C010; AP-routing orphan-approver ticket exists (`issue_378874ffeb8f4cb0b0417021f2d3d647`); Acme addendum + change_order exist; Northstar engagement_letter exists; 210000/219000 account split is accurate. (Prior candidate scored 3 because of the impossible Acme `engagement_letter` ask; that trap is gone.) |

All applicable sub-dims ≥ 4, eleven of twelve at 5. The single 4 (Strict-language) is justified above and does not warrant a BLOCK.

---

## [B2] Adversarial Alt-Path / Second-Reading

Four readings probed; none produce divergent write actions or universe states.

**Reading 1 — "post a summary" channel resolution.** Prompt says "post a vendor-by-vendor summary in the payables channel." The only payables channel is C010 `#vendor-bills-and-ap`. C005 `#monthly-close-coordination` is close discipline (not payables); C008 `#compliance-and-registrations` is compliance. The qualifier "payables" rules out both. **Unique → C010.**

**Reading 2 — "email to Daniel with Steven on copy" recipient resolution.** Universe contacts: Daniel Jones is the Accounts Manager (the only Daniel in AP authority); Steven Perry is the Managing Partner (the only Steven in partner authority). Persona narrative pre-anchors both names with role context ("Daniel and Steven own that call"). Cross-checked `entities_personas.md` — no Daniel/Steven collision. **Unique → Daniel Jones + Steven Perry cc.**

**Reading 3 — "open AP-routing orphan-approver ticket" comment vs. create.** Prompt phrases it as "the open AP-routing orphan-approver ticket" (definite article + "open" presupposes an existing item) and "Add a comment on" (explicit comment verb, not create). Universe has exactly one matching Linear issue: `issue_378874ffeb8f4cb0b0417021f2d3d647` "Fix AP routing rule for departed approvers and sweep orphaned pending approvals." A literal reader cannot reasonably justify creating a new ticket given the definite-article framing. **Unique → comment on existing issue.**

**Reading 4 — "scope verification on the engagement" Acme trap.** This is the critical fix from the prior candidate. The prompt explicitly says: "For Acme, the original engagement evolved through an addendum and at least one change order, so we have multiple documents to check, not a single letter." A literal-reader who searches `kind=engagement_letter` on Acme and reports "not found" directly contradicts the prompt language. The prompt itself anchors the agent to `engagement_letter_addendum` + `engagement_change_order` for Acme and to `engagement_letter` for Northstar. **Unique → addendum + change_order on Acme; engagement_letter on Northstar.**

**No divergence found.** No tightening recommended.

---

## [B3] Tool-Call Density Projection

Sketched trajectory for a competent Opus 4.8 agent on the deliverable as written:

| Component | Low | High | Mid | Notes |
|---|---:|---:|---:|---|
| Base discovery (channel lookup, Daniel/Steven/Margaret contacts, fiscal period boundary, vendor master sweep) | 5 | 8 | 6.5 | C010 channel resolution + 2-3 contact lookups + 1 period lookup + 1-2 vendor master pulls. |
| Pending AP queue sweep across 3 entities | 4 | 6 | 5.0 | One pull per entity at minimum; thorough agent paginates or re-filters by age/dollar. |
| Compound-rank computation (age × dollars) | 1 | 2 | 1.5 | Either 1 combined query or 2 calls (sort by age, sort by amount, reconcile). |
| Per-vendor 3-link chain (SAP detail + Linear issue + email escalation) for top 3-5 | 9 | 15 | 12.0 | 3 vendors × 3 surfaces = 9; 5 vendors × 3 = 15. Prompt says "three to five worst offenders." |
| Records Vault scope verification (2 entities × 3 doc kinds + access-grant check) | 5 | 7 | 6.0 | Acme: `engagement_letter_addendum` + `engagement_change_order` + access-grant check on restricted docs. Northstar: `engagement_letter` + access-grant check. |
| 4 write actions (Slack post + Linear comment + email draft + reminder) | 4 | 4 | 4.0 | Floor: one tool call per write. |
| Cross-service buffer (refetches, BlackLine exception cross-check, Airtable AP Workflow Exceptions sweep, prior-conversation Slack/email history sweep) | 5 | 8 | 6.5 | Prompt explicitly mandates "check whether this orphan-approver story has come up before" — drives extra reads. |
| Restricted-doc access-grant resolution | 2 | 3 | 2.5 | Lena likely needs a grant on at least one restricted doc; the access check is a separate read per failed access. |
| **PROJECTED TOTAL** | **35** | **53** | **44.0** | |

Adjusted against Hardness_Plan's projection (37 / 47 / 57): my low-end is slightly tighter (35 vs 37) because a fast agent may collapse the rank step; my high-end is tighter (53 vs 57) because I didn't double-count the per-vendor 3-link inside the cross-service buffer. **Midpoint 44 ≥ 40 floor → PASS with +4 margin.** Low-end 35 is below the 40 floor but is a fast-agent edge case; the explicit "three to five worst offenders" + "compound view of age in days against outstanding dollars" + 4-write mandate makes the low-path harder to justify than the prior candidate's 32.5 average.

Risk note: the low-end 35 is uncomfortably close to the floor. If a single thorough run lands at 50+ and balances the average, we're fine; if all 6 runs collapse to the fast path, average could brush 35-38. Mitigated by OE pressure on per-vendor drill and 4 distinct writes (B3 cannot dictate OE design, but flagging for S2).

---

## [B4] Hardness Preservation (vs `Hardness_Plan.md` levers)

| Lever | Status | Prompt language that surfaces it |
|---|---|---|
| **L1 Latching** (Daniel-Jones routing dismissal + dollar-bias counter-anchor) | ✓ PRESERVED | "Daniel said in the payables channel a couple of weeks back that the routing rule for departed approvers was patched last sprint, but I'm not sure that fully cleared the backlog because some of the calls reference invoices that look recent to me" + closing paragraph "check whether this orphan-approver story has come up before. Daniel's earlier note suggested it was handled. If the invoices we are still sitting on were dated after that, the rule isn't holding." Counter-anchor: "ranking done on a compound view of age in days against outstanding dollars rather than top-dollar alone." Both anchors explicit. |
| **L2 Structured-DB skip** (RV scope across 2 entities, 3 doc kinds, restricted/access grant) | ✓ PRESERVED | "Check the vault for the executed engagement record. For Acme, the original engagement evolved through an addendum and at least one change order, so we have multiple documents to check, not a single letter. For Northstar the engagement letter itself should be cleaner. If a record is marked restricted and you can't get to it without an access grant, say so plainly, don't report it as missing." Three doc kinds + restricted/access mandate explicit. |
| **L7 Multi-write diversification** (4 writes across 4 services) | ✓ PRESERVED | "post a vendor-by-vendor summary in the payables channel … Add a comment on the open AP-routing orphan-approver ticket … Draft an email to Daniel with Steven on copy … set me a reminder to re-sweep this in seven days." Exactly 4 writes, each on a distinct surface. |
| **L8 Multi-link chain** (per-vendor SAP → Linear → email) | ✓ PRESERVED | "tell me whether it is an orphaned approval chain, a disputed deliverable, or a missing credit memo. The queue status field flattens all three of those into the same label, so don't stop at status alone. Cross-check what any open AP exception ticket says on the issues side, and look for an active partner sign-off thread or a void-and-rebill request sitting in email from Owen or Daniel." Three surfaces mandated explicitly per vendor (SAP status + Linear ticket + email thread). |
| **L9 Universe-grounded gotcha** (restricted docs + access grants + 210000 vs 219000 account split) | ✓ PRESERVED | Restricted/access-grant covered under L2. Account split: "Stay on the external-vendor side of the ledger, not the employee-reimbursement side, since those run through a different account family and should not sit in this count." Both elements explicit. |

**All 5 levers naturally surfaced.** No `HARDNESS_REGRESSION` flagged.

---

## [B5] Tool-Leak / Phrasing Scan

| Check | Result |
|---|---|
| Tool function names (`email_send_email`, `linear_create_issue`, `sap_subledger_*`, etc.) | NONE |
| MCP server names ("the Oracle GL MCP server", etc.) | NONE |
| Internal IDs (VEN-*, apinv_*, doc_*, issue_*, exc_*, BL-*) | NONE |
| Channel codes (C010, C005, C008) | NONE — only natural-language descriptors ("payables channel") |
| Em-dashes / en-dashes | NONE (`grep -P '[—–]'` returns 0) |
| "at least N" without prompt mandate | 2 instances, both intentional: "at least two or three" (conversational vendor count), "at least one change order" (universe-grounded floor, exactly 1 change_order doc exists). Neither violates the strict rule (which targets rubric titles) but flagging for S3 awareness: if rubric uses "at least 1 change order" in title, it must be backed by the prompt mandate, which it is. |
| "approximately" before IDs/dates | NONE |
| "(or similar)" near exact values | NONE |
| Mass-produced tonality phrases ("loop in", "CC our CEO", "keeping me up at night", "circle back", "sync up", "reach out") | NONE |

**One watch-out for S3:** the "at least one change order" phrasing in the prompt legitimizes "at least 1 change order" in rubrics — but rubric writers should still prefer an exact assertion ("references the change order doc") over a count-based one to avoid linter friction.

---

## Delta check vs. prior candidate (regression scan)

| Failure dim | Prior | Rebuild |
|---|---|---|
| Em-dashes / en-dashes | (would-be) 0 | 0 ✓ |
| Acme `engagement_letter` impossible-doc trap | PRESENT (broke R4 in 3/6 runs) | REMOVED — prompt explicitly says addendum + change_order, "not a single letter" ✓ |
| Multi-write surface | 1 write (Slack only) | 4 writes (Slack + Linear comment + email + reminder) ✓ |
| Maximalism score | 1 | 5 ✓ |
| Strict-language score | 2 | 4 ✓ |
| Truthfulness / lever fit | 3 | 5 ✓ |
| Density (avg tool calls) | 32.5 (FAIL) | midpoint 44, low 35, high 53 — PASS with +4 margin ✓ |

No regressions on any prior-failure dimension.

---

## Verdict

**GO.**

- Every applicable QC sub-dim ≥ 4 (eleven at 5, one at 4 with explicit justification).
- No adversarial divergence across 4 second-readings.
- Projected tool-call density midpoint 44 ≥ 40 floor (with +4 margin; low-end 35 is a fast-path edge case mitigated by the 4-write × 3-vendor-chain × 2-entity-scope mandate).
- All 5 hardness levers (L1, L2, L7, L8, L9) naturally surfaced in prompt language.
- Zero phrasing hits (no tool names, no MCP names, no internal IDs, no em-dashes, no tonality phrases).
- All three prior-failure traps (em-dashes, Acme impossible-doc, single-write surface) explicitly closed.

**Notes for downstream phases:**
1. (S2) OE must pressure the per-vendor drill (3 surfaces × 3-5 vendors) and the 4 distinct writes; the low-end density gap closes only if OEs explicitly score per-vendor SAP/Linear/email triangulation.
2. (S3) Avoid "at least N" in rubric titles where an exact-anchor formulation works ("references the change order doc" > "at least 1 change order doc"). The prompt mandate exists to backstop "at least 1" if needed, but exact phrasing is cleaner.
3. (S3) The Daniel-Jones thread-reply dismissal lives in Slack thread replies — rubric grading the reconciliation should target the agent's reconciliation conclusion (invoices dated after the supposed fix still carry null approver), not the act of reading the reply.
