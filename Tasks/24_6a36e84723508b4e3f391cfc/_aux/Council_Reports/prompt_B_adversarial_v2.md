# Council B v2 — Adversarial QC + Density + Hardness Preservation (S1.5 revised prompt)

Task: `24_6a36e84723508b4e3f391cfc`
Deliverable: `5_Prompt.txt` (revised after linter SoD pushback)
Universe today: 2026-06-12 (US/Eastern)
Persona: Lena Park (Procurement Officer) — **procurement-seat triage hand-off**, never owns AP disposition.
Pass against: prior `prompt_B_adversarial.md` (v1).

Five role lenses applied (Architect / Implementer / Red-team / Ground-truth / Integration), combined into B1-B5. All delta-from-v1 changes flagged inline.

---

## Linter delta the revision is supposed to fix

v1 framed Lena as owning AP-queue triage (the cross-entity pending-approval sweep was the spine of her requested action). Persona brief reserves AP-queue triage for Priya Khatri (AP Coordinator) and explicitly carves Lena off from AP per segregation-of-duties; Daniel Jones is her escalation for AP-disposition crossings; vault SOWs are her Recent Activity. v1's QC sub-dim **Persona fit** therefore reads as 4 once the linter is taken at face value.

The v2 reframe:
- Inbound is procurement-rooted ("They reach me because procurement owns the relationship") — the call source matches Lena's seat.
- The AP-queue snapshot is explicitly NOT her decision surface ("the queue itself is on the AP side and that is not my call").
- Her purpose is to FILTER what procurement can answer cleanly (SOW currency / change-order / vault scope) so she does not "add noise" to Priya's backlog.
- The 4 writes are framed as CROSS-TEAM HANDOFF, not AP-owned action: payables-channel summary FOR Priya, Linear comment WITH procurement-side evidence (not opening a procurement-owned ticket), email to Daniel cc Steven, self-reminder.
- Closing: "I am not approving or routing; Priya, Daniel, and Steven own that call."

This is structurally the procurement-seat triage hand-off pattern the persona brief sanctions.

---

## [B1] QC Sub-Dim Re-Scoring

Only re-scoring the five sub-dims the prompt called out; for all others, flagging only changes from v1.

| Sub-dim | v1 | v2 | Delta justification |
|---|---:|---:|---|
| **Persona fit** | 4 | **5** | v1 had Lena owning AP-queue triage (SoD overreach). v2 reframes inbound as procurement-rooted, the queue snapshot as a non-decisional information pull ("not my call"), the four writes as cross-team handoff (FOR Priya / WITH procurement evidence / TO Daniel cc Steven / reminder for self). Persona brief's authority pattern — "TRIAGES and ESCALATES, NOT approves, routes, or posts" — is now explicit in the closing sentence. Daniel-as-escalation and vault-SOWs-as-Recent-Activity both surface naturally in the request. **Improved over v1.** |
| **Business-function fit** | 5 | **5** | Vendor-Operations / procurement-AP interface remains dead-center; the AP queue is still pulled across 3 entities, scope verification is still mandated on Acme + Northstar. The function did not narrow — it widened to procurement-AP HANDOFF, which is still on the spec's "AP / Vendor Operations" axis. **No regression.** |
| **Maximalism** | 5 | **5** | All five Hardness levers still surface naturally (B4 below). No write dropped (still 4 across 4 services). No entity dropped (still 3 entities in the queue pull). No doc-kind dropped (still addendum + change_order + engagement_letter). The procurement-angle framing does not reduce surface area; it relabels OWNERSHIP without dropping any read or write. **No regression.** |
| **Single-service tool use** | 5 | **5** | 6 services still required: SAP subledger (queue pull + per-vendor detail), Records Vault (Acme addendum + change_order + Northstar engagement_letter + access grants), Linear (existing orphan-approver ticket + per-vendor void-and-rebill / escalation issues), email (per-vendor Owen / Daniel threads + Daniel-cc-Steven draft), Slack (C010 history sweep + new summary post), reminders (7-day follow-up). The procurement-angle framing does not collapse any service. **No regression.** |
| **Truthfulness / lever fit** | 5 | **5** | Every claim still atom-anchored: Priya Khatri (AP Coordinator), Daniel Jones (Accounts Manager, Lena's named escalation per persona brief), Steven Perry (Managing Partner), Owen Mercer (AP Specialist) all exist as contacts; payables channel resolves uniquely to C010 (`#vendor-bills-and-ap`); orphan-approver ticket exists (`issue_378874ffeb8f4cb0b0417021f2d3d647`); Acme has no `engagement_letter` but has both `engagement_letter_addendum` (`doc_eb7cb30c59bd4f03`) and `engagement_change_order` (`doc_2d85ac5a698745c5`); Northstar has `engagement_letter` (`doc_0036f5b991574808`); 210000 / 219000 GL split is accurate; all three named scope docs are `classification = restricted`. **No regression.** |
| **Investigation pre-solved** | 5 | **5** | The new "first three are procurement's problem, last two are AP's" sentence is a **cause-CATEGORY ownership map** ("first three" = stale SOW / missing change order / out-of-scope line are scope issues procurement owns; "last two" = missing credit memo / orphan approval chain are AP issues), NOT a per-vendor classification. The agent still must DIAGNOSE which category each of the 3-5 worst offenders falls into by cross-referencing SAP + Linear + email. The category-ownership map tells the agent how to ROUTE the diagnosis in the writes (procurement-side evidence → Linear comment for AP; partner sign-off → email Daniel cc Steven), not what the diagnosis IS. **Not pre-classifying.** |

All other sub-dims unchanged from v1:

| Sub-dim | v1 | v2 | Note |
|---|---:|---:|---|
| Unique Ground Truth | 5 | 5 | Same end-state (4 writes + ranked vendor read + per-vendor diagnosis + scope reads). |
| Feasibility | 5 | 5 | Same service inventory. |
| Coherence | 5 | 5 | Procurement-seat-triage framing is internally cohesive end-to-end. |
| Contrived language | 5 | 5 | Narrative voice held; the SoD acknowledgement reads natural in a Procurement Officer's voice. |
| Word count / format | 5 | 5 | 478 → ~485 words by my count, still ≤ 500. Three paragraphs. |
| Strict-language conventions | 4 | 4 | Same two "at least" usages held over from v1 ("at least two or three" conversational, "at least one change order" universe-grounded floor). No new violations introduced. **No regression.** |
| Tool/system name leakage | 5 | 5 | No new tool / MCP / internal-ID surface. |

**Eleven of twelve sub-dims at 5; one (Strict-language) at 4 with explicit justification carried over from v1. Persona fit specifically improved from 4 to 5.**

---

## [B2] Adversarial Alt-Path / Second-Reading (four targeted readings)

### Reading 1 — Could the AP-queue snapshot be skipped because "AP is not my call" makes it feel out of scope?

**Test:** Does the SoD-acknowledgement framing ("that is not my call") give an agent license to skip the queue pull?

**Verdict: NO.** The exact prompt mandate is:

> "Pull a snapshot of the pending-approval AP queue across Brookfield, Northstar Legal, and Acme Cloud so we can see who is stuck and how long."

This is an unambiguous imperative ("Pull a snapshot"), with explicit cross-entity scope ("across Brookfield, Northstar Legal, and Acme Cloud"), purpose-bound to information ("so we can see who is stuck and how long"). The "not my call" framing applies to **disposition / routing**, not to **information-gathering** — and the prompt explicitly distinguishes these by saying "Before I push this to Priya or Daniel, I want to know what procurement can answer cleanly." The wanting-to-know is mandated; the pushing is deferred. No reasonable agent would interpret the imperative as optional.

**Density risk: none.** SAP queue pull stays in the trajectory.

### Reading 2 — Could "post a summary in the payables channel for Priya and the AP folks" be read as a DM to Priya?

**Test:** Does the "for Priya and the AP folks" qualifier introduce DM ambiguity?

**Verdict: NO.** The exact phrasing is:

> "post a summary in the payables channel for Priya and the AP folks with the per-vendor read and which side owns each one."

The locative preposition is "**in the payables channel**" — that is a channel POST, syntactically. "for Priya and the AP folks" is the AUDIENCE adjunct (who the post is FOR), not the destination. If the intent were DM, the prompt would read "DM Priya" or "send Priya". The construction "post … in the channel … for …" is the natural way to address a channel post to a sub-audience and only resolves as a channel post.

Cross-check: there is only one payables channel (C010 `#vendor-bills-and-ap`); both Priya Khatri and the AP team are members.

**Unique → Slack channel post to C010.** Not a DM.

### Reading 3 — Could "Drop a comment on the open AP-routing orphan-approver ticket" be read as creating a NEW procurement-side ticket?

**Test:** Does the procurement-seat framing tempt the agent to open a procurement-owned Linear ticket alongside or instead of commenting on the AP-owned ticket?

**Verdict: NO.** Three textual cues lock this unambiguously:
1. **Definite article** ("**the** open AP-routing orphan-approver ticket") presupposes a unique existing referent.
2. **"open"** as a state-qualifier reinforces the referent is an existing ticket already in the open state.
3. **"Drop a comment on"** is an explicit comment verb. "Open" / "create" / "file" would be the create verbs and are absent.

The universe has exactly one matching Linear issue (`issue_378874ffeb8f4cb0b0417021f2d3d647` "Fix AP routing rule for departed approvers and sweep orphaned pending approvals"). Furthermore, the prompt explicitly says "**with the procurement-side evidence so the AP team has it when they work the ticket**" — the procurement evidence is the COMMENT BODY, supplied INTO the AP-owned ticket, not the payload of a new procurement ticket.

**Unique → comment on existing `issue_378874ffeb8f4cb0b0417021f2d3d647`.** Not a new ticket.

### Reading 4 — Could the per-vendor root-cause read be skipped on vendors the agent assumes are "AP's problem"?

**Test:** Does the "first three are procurement's problem, last two are AP's" framing license skipping the L8 multi-link chain on AP-owned vendors?

**Verdict: NO**, but with a watch-out for S2 to reinforce.

The exact prompt mandate is:

> "For the three to five worst offenders, give me a per-vendor read from the procurement angle. **For each**, tell me whether the holdup looks like a stale or superseded SOW, a missing change order, an out-of-scope line, an active vendor dispute, a missing credit memo, or simply an approval chain with no owner on the AP side."

"**For each**" universally quantifies — the per-vendor diagnosis applies to ALL 3-5 worst offenders, whether they end up classified as procurement-side or AP-side. The category-ownership map ("first three are procurement's problem, last two are AP's") describes how to ROUTE the diagnostic finding into the writes, not whether to do the diagnosis.

Three structural backstops force the agent to do the L8 chain even on AP-owned vendors:

1. The agent cannot CLASSIFY a vendor as "approval chain with no owner on AP side" without checking SAP (approver=null) AND Linear (no existing void-and-rebill or escalation issue) AND email (no partner sign-off thread). The classification ITSELF requires the 3-link chain.
2. The Linear comment write requires "**the procurement-side evidence**" attached to the AP ticket — for AP-side vendors, the agent must still pull SAP + email evidence FROM the procurement angle to deposit on the ticket.
3. The email to Daniel needs "vendors that need partner sign-off for release" — identifying which 80+ day vendors need partner sign-off requires reading the email escalation history per vendor, which is the third link in the chain.

**Watch-out for S2:** OEs should explicitly score the per-vendor SAP/Linear/email triangulation for ALL classified vendors, not just procurement-owned ones, to fully close the low-end density gap. Flagging for downstream.

**No adversarial divergence found across all four readings.**

---

## [B3] Tool-Call Density Re-Projection

The structural drivers of density did not change from v1 — only the framing of OWNERSHIP changed. The 4 writes, the per-vendor 3-link chain, the 2-entity × 3-doc-kind scope verification, the base discovery, the prior-conversation cross-check all remain mandated.

| Component | Low | High | Mid | Delta from v1 | Notes |
|---|---:|---:|---:|---|---|
| Base discovery (channel lookup, Daniel/Steven/Priya/Margaret contacts, fiscal period, vendor master) | 5 | 8 | 6.5 | +0 | One extra contact lookup (Priya) is offset by no new other deltas. |
| Pending AP queue sweep across 3 entities | 4 | 6 | 5.0 | +0 | Still 3 entities, still age-banded. |
| Compound rank (age × dollars) | 1 | 2 | 1.5 | +0 | Unchanged. |
| Per-vendor 3-link chain (SAP detail + Linear + email) for top 3-5 | 9 | 15 | 12.0 | +0 | Reading 4 confirmed chain still mandated for all classified vendors. |
| RV scope verification (2 entities × 3 doc kinds + access-grant check) | 5 | 7 | 6.0 | +0 | Unchanged. |
| 4 write actions (Slack + Linear comment + email + reminder) | 4 | 4 | 4.0 | +0 | Unchanged (writes are the same 4, just reframed as handoff). |
| Cross-service buffer (refetches, BlackLine exception cross-check, Airtable AP Workflow Exceptions sweep, prior-conversation Slack/email sweep) | 5 | 8 | 6.5 | +0 | Daniel-Jones "routing-fixed" dismissal sweep still mandated explicitly. |
| Restricted-doc access-grant resolution | 2 | 3 | 2.5 | +0 | Unchanged. |
| **PROJECTED TOTAL** | **35** | **53** | **44.0** | **+0** | Identical to v1 midpoint. |

**Midpoint 44 ≥ 40 floor → PASS with +4 margin.**

Critical risk the user flagged: *does the procurement-angle framing risk an agent dropping the SAP detail call because they think "I shouldn't read the AP queue deeply"?*

**Answer: NO.** The prompt explicitly mandates the queue pull AND the per-vendor diagnosis. The "AP is not my call" framing applies to DISPOSITION ("approving or routing"), not to information-gathering. SAP detail per vendor is structurally required to:
- Identify whether `approver = null` (orphan signal),
- Read `invoice_date` to compare against Daniel's "fixed last sprint" claim (the L1 reconciliation),
- Pull amount + age for the compound-rank classification.

None of these are achievable without per-vendor SAP detail reads. **SAP detail stays in the trajectory.**

**No `INSUFFICIENT_DENSITY` flag.**

---

## [B4] Hardness Preservation (vs. `Hardness_Plan.md` levers)

| Lever | v1 status | v2 status | v2 prompt language that surfaces it |
|---|---|---|---|
| **L1 Latching** (Daniel-Jones routing dismissal + dollar-bias counter-anchor) | ✓ | ✓ PRESERVED | "Daniel posted in the payables channel a couple of weeks back that the routing rule for departed approvers was patched last sprint. The procurement picture won't tell me whether that held, but if the invoices we are still sitting on were dated after that patch, the routing issue is alive on the AP side and Priya needs that signal." Dollar-bias counter: "I want the lens to be age against outstanding dollars together rather than top-dollar alone, because a long-aged mid-dollar invoice can drift past us." Both anchors explicit. **Reconciliation pressure preserved.** |
| **L2 Structured-DB skip** (RV scope on 2 entities, 3 doc kinds, restricted + access grants) | ✓ | ✓ PRESERVED | "For any 80-plus-day item touching Acme Cloud or Northstar Legal, I need scope confirmation before anything routes. For Acme, the original engagement evolved through an addendum and at least one change order, so we have multiple documents to check, not a single letter. For Northstar the engagement letter itself should be cleaner. If a record is marked restricted and you can't get to it without an access grant, say so plainly, don't call it missing." All three lever facets (multi-entity, multi-doc-kind, restricted/access-grant) present. |
| **L7 Multi-write diversification** (4 writes across 4 services) | ✓ | ✓ PRESERVED — STILL 4 | (a) "post a summary in the payables channel for Priya and the AP folks", (b) "Drop a comment on the open AP-routing orphan-approver ticket with the procurement-side evidence", (c) "Draft an email to Daniel with Steven on copy on the vendors that need partner sign-off for release", (d) "set me a reminder to re-check in seven days so this doesn't drift". **Exactly 4 writes, each on a distinct surface. Count held.** |
| **L8 Multi-link chain** (per-vendor SAP → Linear → email) | ✓ | ✓ PRESERVED | "Cross-check the active engagement records in the vault, the open AP exception ticket on the issues board, and any partner sign-off or void-and-rebill threads in email from Owen or Daniel." Three surfaces mandated per vendor; the categorization options ("stale or superseded SOW, missing change order, out-of-scope line, active vendor dispute, missing credit memo, or simply an approval chain with no owner on the AP side") cannot be distinguished without all three. Reading 4 above confirms the chain applies to ALL classified vendors. |
| **L9 Universe-grounded gotcha** (restricted docs + access grants + 210000 vs 219000 split) | ✓ | ✓ PRESERVED | Restricted/access-grant covered under L2 phrasing. Account split: "Stay on external-vendor activity; employee reimbursements run through a different account family and are not ours." Both facets explicit. |

**All 5 levers naturally surfaced in the revised voice. No `HARDNESS_REGRESSION`.**

Persona-fit improvement is the ONLY material change; the lever surface area is structurally preserved.

---

## [B5] Phrasing Scan (revised text)

| Check | Result | Delta from v1 |
|---|---|---|
| Tool function names | NONE | +0 |
| MCP server names | NONE | +0 |
| Internal IDs (VEN-*, apinv_*, doc_*, issue_*, exc_*, BL-*) | NONE | +0 |
| Channel codes (C010, C005, C008) | NONE — only natural-language ("payables channel") | +0 |
| Em-dashes / en-dashes (`[—–]`) | NONE | +0 |
| "at least N" without prompt mandate | Two instances, both held from v1: "at least two or three" (conversational vendor count) and "at least one change order" (universe-grounded floor — exactly 1 change_order doc exists for Acme). No new instances. Neither violates the rubric-title rule. **No new violation.** | +0 |
| "approximately" before IDs/dates | NONE | +0 |
| "(or similar)" near exact values | NONE | +0 |
| Mass-produced tonality ("loop in", "CC our CEO", "circle back", "sync up", "reach out", "let's touch base") | NONE | +0 |

**Watch-out carried from v1 for S3:** prefer exact-anchor formulations over "at least 1 change order" in rubric titles; the prompt mandate exists as backstop, but exact phrasing is cleaner.

---

## Delta-from-v1 summary by perspective

| Perspective | v1 verdict | v2 delta |
|---|---|---|
| B1 (QC sub-dims) | 11×5 + 1×4 | **Persona fit 4 → 5** (linter SoD fix lands); all other sub-dims unchanged. Investigation-pre-solved verified 5 against the new "first three are procurement's problem" framing — confirmed cause-category ownership map, not per-vendor pre-classification. |
| B2 (alt-path / second-reading) | No divergence on 4 readings | **No new divergence introduced.** All four newly-targeted readings (queue skip / channel-vs-DM / comment-vs-create / per-vendor drill on AP-owned vendors) close cleanly. One watch-out flagged for S2 OEs (per-vendor chain coverage on AP-owned vendors). |
| B3 (density) | Midpoint 44, low 35, high 53 | **Identical projection.** No structural change — same 4 writes, same per-vendor 3-link chain, same 2-entity × 3-doc-kind scope, same prior-conversation cross-check. Procurement-angle reframe is OWNERSHIP relabeling, not surface reduction. |
| B4 (hardness preservation) | All 5 levers present | **All 5 levers still present** — L1 reconciliation, L2 multi-doc-kind + restricted, L7 four-write × four-service, L8 SAP-Linear-email per vendor, L9 restricted-access + account split. No regression. |
| B5 (phrasing scan) | Clean, two intentional "at least" usages | **Clean.** No new tool/MCP/ID/em-dash/tonality surface introduced. The two "at least" usages were carried over verbatim. |

---

## Verdict

**GO.**

- Every applicable QC sub-dim ≥ 4 (eleven at 5, one at 4 with explicit justification). **Persona fit improved 4 → 5 — the specific linter blocker is resolved.**
- No adversarial divergence across four targeted second-readings (queue-skip / DM-vs-channel / comment-vs-create / AP-owned-vendor drill).
- Projected density midpoint 44 ≥ 40 floor (no change from v1; procurement-angle reframe does not collapse any read or write).
- All 5 Hardness levers (L1, L2, L7, L8, L9) still naturally surfaced in the revised voice.
- Zero new phrasing hits; no new tool names, MCP names, internal IDs, em-dashes, or mass-produced tonality.
- The v1 v2 delta is strictly a persona-fit improvement; no other dimension regressed.

**Notes for downstream phases:**

1. **(S2) OEs must score the per-vendor 3-link chain (SAP detail + Linear cross-check + email cross-check) for ALL 3-5 classified vendors, regardless of whether the agent classifies them as procurement-owned or AP-owned.** The new "first three procurement, last two AP" framing must not become a license for the agent to skip the L8 chain on AP-side vendors. The classification ITSELF requires the chain — reinforce this in OE scoring.
2. **(S2) OE for the Linear comment write should explicitly require procurement-side evidence atoms (vault scope status + per-vendor SAP / email cross-reference) IN the comment body**, not just the act of commenting. This closes the L8-on-AP-owned gap from the other side.
3. **(S3) Prefer exact-anchor rubric titles over "at least 1" formulations.** "References the Acme change order doc" > "references at least 1 change order". Prompt mandate ("at least one change order") exists as backstop but exact phrasing is cleaner against the linter.
4. **(S3) Daniel-Jones thread-reply reconciliation rubric** should target the agent's reconciliation conclusion (post-fix-date invoices still carry null approver → the routing issue is alive) and the resulting Priya-signal in the Slack post, not the act of reading the reply. Anchor on Lena's closing sentence: "if the invoices we are still sitting on were dated after that patch, the routing issue is alive on the AP side and Priya needs that signal."
