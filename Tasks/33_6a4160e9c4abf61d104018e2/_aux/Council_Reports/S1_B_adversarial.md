# Council B — Adversarial QC + Density + Hardness Preservation (S1 / prompt phase)

**Task:** 33_6a4160e9c4abf61d104018e2
**Phase:** prompt (S1)
**Deliverable:** `Tasks/33_6a4160e9c4abf61d104018e2/5_Prompt.txt`
**Persona:** Carlos Rivera (Loan Officer, FHA + Conventional)
**Universe:** keystone — today 2026-06-12
**Reviewer:** Council B (adversarial QC, density, hardness preservation)

## Ground-truth atoms verified against `3_UniverseDataForThisTask.json`

| Atom | Value | Source |
|---|---|---|
| Carlos staff id | `los_staff_a7fa5b29babd` | mortgage_los.staff (Carlos Rivera) |
| LN-2026-00009 | status=`conditional_approval`, assigned_lo=`los_staff_a7fa5b29babd` (Carlos), updated 2026-03-01 | mortgage_los.loans |
| LN-2026-00211 | status=`withdrawn`, assigned_lo=`los_staff_6d606f7506a7` (Brian Mitchell), updated 2026-03-28 | mortgage_los.loans |
| LN-2026-00622 | status=`processing`, assigned_lo=`los_staff_0375f7c91014` (Todd Jennings), updated 2026-03-28 | mortgage_los.loans |
| LN-2026-00009 outstanding conditions | 3 (`los_cond_d7fdad61f9fa` 2026-02-27, `los_cond_739ecac87a02` 2026-03-02, `los_cond_74d7f24385f5` 2026-03-03) | mortgage_los.conditions |
| LN-2026-00211 outstanding conditions | **0** | mortgage_los.conditions |
| LN-2026-00622 outstanding conditions | **0** | mortgage_los.conditions |
| Doc-checklist trio | 00009: 12 items (4 reviewed / 4 approved / 3 received / 1 required); 00211: 14 (12 received / 2 required); 00622: 14 (9 received / 4 required / 1 approved) | mortgage_los.document_checklist_items |
| Grace ↔ Carlos Slack | `D_grace_yamamoto` (mpim w/ Carlos + Grace + Sofia + Robert) — Carlos IS in members | slack.slack_channels |
| `D_grace_robert` | 2-person IM Grace ↔ Robert; **Carlos NOT a member** | slack.slack_channels |
| C002 #loan-processing | 334 msgs | slack.slack_messages |

The “longest-overdue outstanding item” is unambiguous **iff** “outstanding item” = condition: only LN-2026-00009 has any outstanding conditions, oldest `los_cond_d7fdad61f9fa` issued 2026-02-27 (≈ 105 days overdue at 2026-06-12).

---

## [B1] QC Sub-dim Scoring

| Sub-dim | Score | One-line reason |
|---|---:|---|
| Unique Ground Truth (1/3/5) | **4** | All trio facts resolve uniquely; `every outstanding item` phrasing is condition-anchored by paragraph 2 + `condition follow-up` close, but reading-2 doc-checklist scope adds 30+ peripheral rows. Justified 4 not 5: not a flipped write but a scope soft-edge. |
| Feasibility (1/3/5) | **5** | All required services available; 4 writes are all valid tool surfaces. |
| Explicit Tool Mention (1/5) | **5** | Zero tool names in body. |
| Clarity & Specificity (1/3/5) | **4** | Conversational + tight. Soft-edge on `outstanding item` scope (see B2); `longest-overdue` is unique only under condition-table reading. Justified 4 not 5 per per-task universe (no other ambiguity carrier). |
| Contrived / Unnatural (1/3/5) | **5** | LO running pipeline review for Director of Ops is a textbook Loan Operations beat for Carlos given the 60-day closing drought scenario_d8b2b048. |
| Alignment with Today's Date (1/3/5) | **5** | `tomorrow afternoon` → 2026-06-13, `today` → 2026-06-12; both resolve to in-window universe data. |
| Truthfulness (1/3/5) | **5** | Prompt is Carlos's voice; Grace's quoted reassurance is plausible-but-wrong (L9 design carrier, not an unverifiable claim). |
| Tool Use & Cross-service (1/5) | **5** | Forces slack + mortgage_los + crm + email + contacts (5 services min). |
| Investigation + Action (1/5) | **5** | Read trio + conditions + chatter; write email + slack + 3× CRM + 1× condition. |
| Coherence / Bolt-on (1/5) | **5** | All four writes flow from the discovery; no bolt-on. |
| Persona (1/3/5) | **5** | Carlos voice: `look`, `buried this month`, `the channel has been wrong before`, `Grace is going to check` — matches over-promising / informal LO brief. |
| Business Function (3/5) | **5** | Loan Operations: pipeline review, condition mgmt, CRM hygiene, channel reconciliation. |

**B1 verdict:** No FAILs. Two 4-scores both justified; bar held.

---

## [B2] Adversarial Alt-Path / Second Reading

| Surface | Second reading attempted | Flips a write? |
|---|---|---|
| Email recipient | Could `tight email summarizing... for her` admit Sofia as CC? | No. The prompt explicitly says `send Grace a tight email` — singular `her`. C002 channel post covers Sofia. **No divergence.** |
| Channel | `the loan-processing channel` → C002 (#loan-processing) per universe constants; C003 #closings, C006 #sales-pipeline are not loan-processing. **No divergence.** |
| Outstanding item scope | `outstanding items` → conditions (the load-bearing reading, anchored by `conditions sitting outstanding` mid-prompt + `condition follow-up` at end) vs doc-checklist items | **Soft divergence.** Email body length changes (3 items vs 40+); CRM engagement bodies change; but the final write SET does not flip — Grace still gets one email, C002 still gets one post, 3 deals still get 1 engagement each, and the condition follow-up still targets LN-2026-00009 (the only trio loan with any condition row). **Same write recipients + same target loan.** |
| Longest-overdue file | Conditions reading → LN-2026-00009 (3 outstanding, oldest 2026-02-27). Doc-checklist reading → ambiguous (LN-2026-00622 has 4 required, oldest unknown; LN-2026-00211 has 2 required but is withdrawn). | The `condition follow-up` close-out anchors to LN-2026-00009 under both readings: doc-checklist reading on LN-2026-00622 has no condition row to follow up on, so a `mortgage_los_add_condition` there is incoherent. **Convergent on LN-2026-00009.** |
| LO of record on trio | LN-2026-00009 = Carlos; LN-2026-00211 = Brian Mitchell; LN-2026-00622 = Todd Jennings. Prompt's `my three flagged files` first-frames them as Carlos's — but the request explicitly asks for `loan officer of record on each`, which forces the agent to read assigned_lo. **Hardness lever L6 preserved without ambiguity in the write set.** |
| CRM engagement type | `engagement note` → NOTE (the existing per-deal pattern). **No divergence.** |

**B2 verdict:** Zero adversarial divergence on writes. Two scope soft-edges noted (outstanding-item scope, longest-overdue file) but both reconverge on the same target loan + recipients. **PASS** with note: tightening `every outstanding item` → `every outstanding condition` would close the soft-edge cleanly; current phrasing is acceptable because `condition follow-up` anchors the close-out.

---

## [B3] Tool-Call Density Projection

Realistic competent-Opus-4.8 trajectory walk (counting necessary + prompt-implied calls):

| Component | Range | Midpoint |
|---|---|---:|
| Slack (list_channels + search trio mentions C002 + read D_grace_yamamoto + thread replies on 211 chatter) | 6-9 | 7.5 |
| `mortgage_los` loans (3 get_loan + optional list for context) | 3-4 | 3.5 |
| `mortgage_los` conditions (3 list-per-loan; the `every one in detail` line forces per-loan) | 3-4 | 3.5 |
| `mortgage_los` document_checklist_items (3 list-per-loan; `every outstanding item still sitting` pulls these too) | 3 | 3.0 |
| `mortgage_los` staff (lookup of Brian Mitchell + Todd Jennings as LOs of record on 211/622) | 1-2 | 1.5 |
| `mortgage_los` borrowers (3 borrower-name reads for email body) | 0-3 | 1.5 |
| CRM deals (locate 3 deals by loan_number) | 3-4 | 3.5 |
| CRM engagements (list per deal; `notes have been going stale` forces staleness check) | 3-4 | 3.5 |
| Email (search threads on each trio loan + read 211 withdrawal trail — `channel has been wrong before` forces it) | 4-6 | 5.0 |
| Contacts (Grace email lookup) | 1 | 1.0 |
| Writes (1 email + 1 slack + 3 CRM + 1 add_condition) | 6 | 6.0 |
| Cross-service triangulation buffer | 1-3 | 2.0 |
| **TOTAL projected** | **34-49** | **41.5** |

**Density verdict: THIN_DENSITY (midpoint ≈ 41.5 in the 40-49 band).** The Hardness Plan projected 50.5 — the realistic count is below the 50+ design target.

Drivers of the gap vs Hardness Plan:
- The plan padded with `quickbooks` + `stripe` + `filesystem` (~6.5) that the prompt does not naturally force — pipeline-review framing doesn't pull AP / fees / PDFs.
- The plan's `cross-service triangulation buffer = 6.5` over-counted; my buffer is 2.
- The `tight email`, `short status note` phrasings ALSO trim the agent's natural breadth: a verbose prompt would pull more email reads, but Carlos's `tight` cues a shorter compose phase.

**Per gating rule, midpoint 40-49 = THIN_DENSITY. The S1→GO criterion requires B3 ≥ 50.** Recommend operator decide between (a) accepting THIN with explicit per-task justification appended to Hardness_Plan.md, or (b) tightening prompt to force one more service (e.g., adding `pull the credit-report fee history off the trio` to force `stripe` reads → +3, or `check the appraisal file on 211` to force `filesystem` → +2). Option (b) preserves the 50+ design target; option (a) accepts THIN risk.

---

## [B4] Hardness Preservation

| Lever | Status | Note |
|---|---|---|
| **L10 Reversal on LN-2026-00211** | **PRESERVED** | `I want the real picture before I send anything up to her` + the request for `genuine status... right now` + `who is the loan officer of record` actively forces an `mortgage_los_get_loan` call on 211, which surfaces `status=withdrawn`. Grace's quoted reassurance counter-anchors but does not pre-solve. |
| **L2 Structured-DB skip on `mortgage_los.conditions`** | **PRESERVED** | `conditions sitting outstanding that should have been cleared weeks ago, I need every one of them in detail` is an explicit pull on the conditions table. An agent that paraphrases from Slack/email chatter alone will miss the 3 outstanding rows on LN-2026-00009. |
| **L9 Authority dismissal from Grace** | **PRESERVED (with B6 caveat)** | Grace's quote `211 is back in motion because Sofia got it unstuck` is in the prompt body — that IS the dismissal carrier. **BUT** the Hardness Plan's planned corroborating Slack DM location (`D_grace_robert`) is unreachable by Carlos — Carlos is not a member. The S2 OEs must plant the message in `D_grace_yamamoto` (Carlos IS in that mpim) or a Grace→C002 thread. Flag forwarded to B6. |
| **L8 Multi-link chain** | **PRESERVED** | Forces slack (Grace ping + C002 reconcile) → LOS (loan + condition lookups) → CRM (deal + engagement reads + write) → email (Grace recipient + back-context) → contacts (Grace email resolution). Five services minimum, three reductions. |
| **L25 Existing-output anchor** | **PRESERVED** | `the notes on those have been going stale` forces the agent to read existing CRM engagements on each of the three deals before writing the new ones. The stale-note plant becomes the anchor candidate. |
| **L6 Near-miss entity / first-framing trap (bonus)** | **PRESERVED** | `my three flagged files` first-frames the trio as Carlos's, but `loan officer of record on each` forces the assigned_lo check — surfacing Brian (211) and Todd (622) as the actual LOs, not Carlos. |

**B4 verdict: All five primary levers preserved at the prompt level**, with one downstream caveat (L9 plant location) propagated to B6.

---

## [B5] Tool-leak / Phrasing Scan

| Check | Result |
|---|---|
| Tool names in body (`email_send_email`, `mortgage_los_*`, `slack_post_message`, `crm_create_engagement`, etc.) | **0 hits** |
| Internal IDs (`los_loan_*`, `los_cond_*`, `los_staff_*`, `keystone_*`, `crm_deal_*`, `crm_engagement_*`) | **0 hits** |
| Em-dashes (—) | **0 hits** |
| En-dashes (–) | **0 hits** |
| `at least N` without explicit mandate | **0 hits** |
| `approximately` before IDs or dates | **0 hits** |
| `(or similar)` near exact values | **0 hits** |
| Generic-urgency clichés (`before it blows up`, `keeping me up at night`, `something changed in the last few days`, `go through everything that has come my way`, `loop in`) | **0 hits** |

**B5 verdict: clean.** Note: the prompt does use the natural informal opener `Look,` — that is not on the cliché ban-list and reads as authentic Carlos voice.

---

## [B6] Upstream Propagation

**PROPAGATE TO HARDNESS (1):** L9 plant location mismatch
- Root cause: Hardness_Plan.md row for L9 specifies `Plant Grace Slack DM: "LN-2026-00211 is back in motion — Sofia got it un-stuck"` in `D_grace_robert`.
- Upstream file:location: `Tasks/33_6a4160e9c4abf61d104018e2/_aux/Hardness_Plan.md` — Levers Available table row 9, and the Selected Levers L9 bullet.
- Verified: per `slack.slack_channels`, `D_grace_robert` membership is `["keystone_e304643b171b", "keystone_e85bc913c756"]` (Grace + Robert only); Carlos `keystone_a7fa5b29babd` is **not** a member. Carlos's agent cannot read that DM.
- Recommended upstream fix: change L9 plant location to **`D_grace_yamamoto`** (mpim with Carlos + Grace + Sofia + Robert per universe membership) for the corroborating message Carlos's agent can read. Update Hardness_Plan.md L9 row and Selected Levers L9 bullet. S2 OEs must reflect the corrected channel.

**PROPAGATE TO HARDNESS (2):** Density projection over-count
- Root cause: Hardness_Plan.md projects midpoint 50.5 with non-trivial contributions from QuickBooks (3), Stripe (2.5), Filesystem (3) and a `cross-service triangulation buffer` of 6.5 — totalling ~15 calls whose surface the pipeline-review prompt does not naturally force.
- Upstream file:location: `Tasks/33_6a4160e9c4abf61d104018e2/_aux/Hardness_Plan.md` — Tool-Call Density Projection table.
- Realistic recount under as-written prompt: **midpoint ~41.5 (range 34-49)** → THIN_DENSITY.
- Recommended upstream fix: either (a) re-baseline Hardness Plan to ~42 midpoint and add an explicit `THIN justification` clause documenting why this task tolerates 42, or (b) revise the prompt at S1 to add one breadth-forcing clause that pulls a 6th service (e.g., `pull the credit-report fee history off the trio` → stripe +3, or `dig the appraisal PDF on 211 out of the file` → filesystem +2). Option (b) is the cheaper restoration of the 50+ design target.

---

## Final verdict

VERDICT: BLOCK -- B3 THIN_DENSITY (midpoint ~41.5 vs 50.5 plan; fix by adding one breadth-forcing service-pull clause OR justify THIN in Hardness_Plan.md); B6 PROPAGATE TO HARDNESS (L9 corroborating Slack plant must move from D_grace_robert to D_grace_yamamoto because Carlos is not a member of D_grace_robert).
