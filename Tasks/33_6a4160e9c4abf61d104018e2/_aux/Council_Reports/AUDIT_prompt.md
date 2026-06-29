# AUDIT — Prompt (S1) — Strict Veteran QC Re-verification

**Task:** 33_6a4160e9c4abf61d104018e2
**Phase:** S1 prompt
**Universe:** keystone — today 2026-06-12
**Deliverable under audit:** `5_Prompt.txt` (345 words, revised post-Council-B-rerun)
**Prior verdicts:** Council A GO; Council B initial BLOCK → re-run GO after revision.
**Auditor stance:** STRICTEST possible interpretation — 5/5 the only PASS, every "should" → "must", every Hardness lever must trace end-to-end with cited evidence in the universe-as-shipped (not assumed S2 plant artifacts).

---

## Per-atom Evidence Table (mandatory before any Truthfulness 5/5)

| Atom Asserted | Universe Query | Row Excerpt | Verdict |
|---|---|---|---|
| Carlos Rivera = Loan Officer | `mortgage_los.staff name="Carlos Rivera"` | `los_staff_a7fa5b29babd` / loan_officer / FHA, Conventional / active | GROUNDED |
| Carlos Slack identity | `slack.slack_users name="Carlos Rivera"` | `keystone_a7fa5b29babd` / carlos.rivera@keystonemortgage.com | GROUNDED |
| Sofia Reyes = processor | `mortgage_los.staff name="Sofia Reyes"` | `los_staff_afc9caafae9d` / processor / active | GROUNDED |
| Grace Yamamoto in slack | `slack.slack_users name="Grace Yamamoto"` | `keystone_e304643b171b` / Grace Yamamoto / not bot | GROUNDED (slack-only; not in mortgage_los.staff — operations role) |
| Grace Yamamoto email | `email` search "grace.yamamoto" | `grace.yamamoto@keystonemortgage.com` confirmed sender | GROUNDED |
| LN-2026-00009 status | `mortgage_los.loans loan_number=LN-2026-00009` | `los_loan_ad53e691489a` / status=conditional_approval / assigned_lo=los_staff_a7fa5b29babd (Carlos) / borrower=los_borrower_34ecb8a5b6f0 (Darren Singh) | GROUNDED |
| LN-2026-00211 status | `mortgage_los.loans loan_number=LN-2026-00211` | `los_loan_223826af9a5d` / status=**withdrawn** / assigned_lo=los_staff_6d606f7506a7 (Brian Mitchell, TERMINATED 2025-04-15) / assigned_processor=los_staff_afc9caafae9d (Sofia) / updated_at=2026-03-28 | GROUNDED |
| LN-2026-00622 status | `mortgage_los.loans loan_number=LN-2026-00622` | `los_loan_6507d3b85a25` / status=processing / assigned_lo=los_staff_0375f7c91014 (Todd Jennings, TERMINATED 2024-07-31) | GROUNDED |
| LN-2026-00009 has 3 outstanding conditions | `mortgage_los.conditions loan_id=los_loan_ad53e691489a status=outstanding` | `los_cond_d7fdad61f9fa` issued 2026-02-27 (appraisal report); `los_cond_739ecac87a02` issued 2026-03-02 (pay stub); `los_cond_74d7f24385f5` issued 2026-03-03 (bank statements) | GROUNDED — oldest 2026-02-27 ≈ 105 days overdue |
| LN-2026-00211 outstanding conditions | `mortgage_los.conditions loan_id=los_loan_223826af9a5d status=outstanding` | **ZERO rows** | GROUNDED (0) |
| LN-2026-00622 outstanding conditions | `mortgage_los.conditions loan_id=los_loan_6507d3b85a25 status=outstanding` | **ZERO rows** | GROUNDED (0) |
| Trio borrowers contact info | `mortgage_los.borrowers id IN trio` | Darren Singh ph=(980)889-1647 em=darren.singh@gmail.com; Angela Foster ph=(704)974-9167 em=angela.foster.622@gmail.com; Elizabeth Gray ph=(704)372-3526 em=elizabeth.gray.211@gmail.com | GROUNDED |
| Trio borrower CRM contacts | `crm.crm_contacts email IN trio_borrower_emails` | **Only Darren Singh found** (crm_contact_34ecb8a5b6f0); Angela Foster + Elizabeth Gray = NOT FOUND | PARTIAL — 1/3 grounded |
| CRM deals for trio | `crm.crm_deals body/name CONTAINS trio loan numbers` | **ZERO rows** | NOT GROUNDED (no deals exist for any trio loan) |
| CRM engagements for trio | `crm.crm_engagements body CONTAINS trio loan numbers` | 6 rows: 2 on LN-2026-00009 (Marcus-Webb investigation context + "borrower wants file moved to Marcus"); 3 on LN-2026-00211 (Marcus-Webb spouse-conflict investigation context); 0 on LN-2026-00622. contact_ids bind to UNRELATED people (Destiny Pham, Stephen Hamilton, Erin Parker, Nicole Rivera, Tiffany Brooks, Abigail Clark) — NOT to the trio borrowers | GROUNDED but pattern is orphan-style |
| D_grace_yamamoto channel | `slack.slack_channels id=D_grace_yamamoto` | is_mpim=True; 5 historical msgs; senders confirm membership = Grace + Carlos + Sofia + Denise Holloway (NOT Robert as Council B claimed) | GROUNDED — Carlos IS a member |
| D_grace_robert channel | `slack.slack_channels id=D_grace_robert` | is_im=True; 21 msgs; senders = Grace + Robert only | GROUNDED — Carlos NOT a member (prior Hardness Plan v1 error correctly fixed in v2) |
| C002 #loan-processing | `slack.slack_channels id=C002` | name=loan-processing / public / 334 historical msgs | GROUNDED |
| Grace ping "last night" in any Carlos-readable channel (2026-06-11 to 2026-06-12) | `slack.slack_messages user_id=keystone_e304643b171b channel_id IN (D_grace_yamamoto, C002) created_at IN window` | **ZERO rows.** D_grace_yamamoto last msg = 2026-03-28 (Carlos, not Grace); C002 last Grace msg = pre-2026-05-29; the 2 Grace C002 msgs flagged as "in window" are actually dated 2026-06-25 and 2026-08-04 — BEYOND universe today | NOT GROUNDED |
| Grace "pushing on for two weeks" (Grace activity 2026-05-29 to 2026-06-12) | `slack.slack_messages user_id=keystone_e304643b171b created_at IN window` | **ZERO Grace msgs in window in any Carlos-readable channel.** | NOT GROUNDED |
| Grace's documented position on LN-2026-00211 | `slack.slack_messages + email.emails sender/text CONTAINS 00211` | Grace's only 00211 activity is March 2026: (a) 2026-03-08 C002 msg "had one come into main inbox on LN-2026-00211. Similar issue: hard to reach, typo-heavy emails"; (b) 2026-03-25 C002 msg "Just sent Marcus an email asking for written disclosure/explanation on LN-2026-00629, LN-2026-00211, and LN-2026-00227"; (c) 2026-03-25 email subject "Marcus Webb conflict review and disclosure policy risk" — Grace IS the lead investigator on LN-2026-00211's fraud-conflict review; the loan was withdrawn 3 days later (2026-03-28) | GROUNDED — and DIRECTLY CONTRADICTS the L9 plant "Sofia got it unstuck, just hold the line on the new appraisal" |
| Trio borrower email activity 2026-06-05 to 2026-06-12 (new paragraph's "outstanding-item email replies in the last week") | `email.emails sender OR recipients_json IN trio_borrower_emails timestamp IN window` | **ZERO emails** sent or received by ANY trio borrower in the window. In ALL TIME: Darren Singh received 1 email (none sent); Angela Foster zero in either direction; Elizabeth Gray zero in either direction | NOT GROUNDED — the new paragraph's email-reply-check loop has nothing to check |
| Sofia recent activity on LN-2026-00211 | `slack.slack_messages user_id=keystone_afc9caafae9d created_at >= 2026-05-29` | **ZERO Sofia msgs in window.** Sofia's last Slack activity on LN-2026-00211 is 2026-03-05 ("I've got LN-2026-00211 in the same bucket. No clean notes, no doc chase logged, lock clock is getting tight.") — a flag, not an "unstuck" | NOT GROUNDED — Sofia has not "got it unstuck" in any recent universe activity |
| L25 stale "on track / lock extended" engagement on trio | `crm.crm_engagements body LIKE %on track% OR %lock extend% AND body CONTAINS trio` | **ZERO trio-tagged stale-anchor engagements.** Existing trio engagements are all Marcus-Webb-investigation context. The one "keep closing on track" hit is on a basement-permit issue, unrelated. | NOT GROUNDED — L25 anchor artifact does not exist in universe |

**Truthfulness floor consequence:** 4 atoms NOT GROUNDED + 1 PARTIAL. Per audit-prompt rule "Empty evidence column → forced score ≤ 3." Truthfulness sub-dim forced to ≤ 3 under strict reading.

---

## [LENS 1 — STRICT QC SCORING]

| Sub-dim | STRICT SCORE | One-line reason | What prior council missed |
|---|---:|---|---|
| Unique Ground Truth | **3** | "Log a CRM engagement note against each of the three deals" — no `crm_deals` exist for any trio loan; existing engagement pattern uses orphan contact_ids unrelated to borrowers; only 1/3 trio borrowers (Darren Singh) has a CRM contact. Agent has at least 4 valid write paths (search-deals-fail/orphan-create/contact-attach-1-of-3/create-new-contacts) that produce different write artifacts. | Council A scored A7 as "MINOR — within envelope" but the mitigation ("contact_ids fallback") only works for 1/3 borrowers. Council B reported "engagements still 3 deals get 1 engagement each" without verifying the existing pattern's contact_id bindings. |
| Feasibility | **4** | All services available; write surfaces exist; but the CRM engagement write is mechanically open only via orphan creation since 2/3 borrower contacts are missing — fragile path. | Council B-B1 scored 5/5 without checking whether the borrowers actually have CRM contact rows. |
| Explicit Tool Mention | **5** | Zero tool names. | (Confirmed clean.) |
| Clarity & Specificity | **3** | "outstanding items" mid-text vs "outstanding-item emails" (new para) vs "longest-overdue outstanding item" vs "condition follow-up" — terminology drifts across conditions / doc-checklist / generic readings; "the three deals" doesn't ground (no deals exist). | Both councils noted scope soft-edge on "outstanding item" but called it within envelope. Strict reading: 4 different terms over 1 page is more than soft-edge. |
| Contrived / Unnatural | **5** | LO pipeline-review for Director of Ops is textbook Loan Operations. | (Confirmed natural.) |
| Alignment with Today's Date | **4** | "tomorrow afternoon" → 2026-06-13 OK; "this afternoon" → 2026-06-12 OK; "last night" + "last week" + "two weeks" have ZERO universe-grounded activity in the time windows asserted (per evidence table). The dates resolve mechanically but the data the prompt claims to be reading isn't there. | Both councils treated these as S2-plant dependencies and passed them. Strict reading: at S1-time, the prompt asserts states the universe does not contain — that is a date-alignment fail, not deferrable to S2. |
| Truthfulness | **3** | Per evidence table: 4 atoms NOT GROUNDED (Grace ping last night, Grace pushing two weeks, trio borrower replies last week, L25 stale anchor) + 1 PARTIAL (CRM contacts) + L9 carrier directly CONTRADICTED by Grace's own documented March-2026 role as LN-2026-00211 fraud investigator. Audit-prompt rule forces ≤ 3. | Council A A8 scored "0 MAJOR / 2 S2-dependency MINORs (intentional contract)" — but the contract still requires the universe to be plant-able WITHOUT contradicting existing universe records. Grace cannot plausibly Slack "Sofia got it unstuck" on a loan she herself sent to Marcus-conflict review 3 months ago. Council B-B4 marked L9 as "PRESERVED" without checking Grace's email/slack history on LN-2026-00211. |
| Tool Use & Cross-service | **4** | Forces 5 services in theory; in practice the contacts + email paths terminate quickly because trio borrowers have ~zero email activity and 2/3 have no CRM contact. Realistic breadth is closer to 4 active services. | Council B-B3 re-run treats email check as 9.5 calls midpoint and contacts as 5.5; strict recount with the actual data is 3-4 (email) + 1-3 (contacts) since the data isn't there. |
| Investigation + Action | **5** | Read-heavy + 4 writes. | (Confirmed.) |
| Coherence / Bolt-on | **5** | All writes flow from the discovery. | (Confirmed.) |
| Persona | **5** | Carlos voice matches PersonaBrief and V3 reference voice. | (Confirmed.) |
| Business Function | **5** | Loan Operations: pipeline review, conditions, CRM hygiene. | (Confirmed.) |

**Lens 1 verdict:** 5 sub-dims fall below 5/5 under strict reading. UGT=3, Feasibility=4, Clarity=3, Date-alignment=4, Truthfulness=3, Cross-service=4. **Under STRICTEST: REVISE.**

---

## [LENS 2 — ANSWER-LEAKAGE SWEEP]

Expected agent outputs: (a) LN-2026-00211 flagged withdrawn-not-active; (b) 3 overdue conditions on LN-2026-00009 surfaced; (c) LN-2026-00622 attributed to Todd Jennings.

| Target answer | Prompt scan | Verdict |
|---|---|---|
| (a) LN-2026-00211 withdrawn | No "withdrawn" / "closed" / "terminated" phrasing tied to 00211. Grace's "back in motion because Sofia got it unstuck" plants the OPPOSITE direction. | NO LEAK |
| (b) 3 overdue conditions on LN-2026-00009 | "conditions sitting outstanding that should have been cleared weeks ago" + "every one of them in detail" + "longest-overdue outstanding item" + "condition follow-up" together heavily *signal* that LN-2026-00009 (the only trio member with outstanding conditions) is the target. Does NOT leak the 3-count or the descriptions, but pre-narrows the file selection to LN-2026-00009 by elimination. | SOFT LEAK — file-selection only, not the count or content. Under strictest reading: borderline pre-solving on the "which file" axis. Not a BLOCKER but worth tightening. |
| (c) LN-2026-00622 attributed to Todd | Prompt frames "my three flagged files" and asks "who is the loan officer of record." Does not leak Todd's name or that Carlos is wrong. | NO LEAK |

**Lens 2 verdict:** No BLOCKER leakage. One SOFT pre-narrowing on (b)'s file selection.

---

## [LENS 3 — HARDNESS END-TO-END]

| Lever | Cited evidence in prompt | Verdict |
|---|---|---|
| **L10 Reversal on LN-2026-00211** | "I want the real picture before I send anything up to her" + "Check the genuine status on each one right now" + "who is the loan officer of record" forces `mortgage_los_get_loan(LN-2026-00211)` which surfaces `status=withdrawn`. Universe atom verified. | TRIGGERED |
| **L2 Structured-DB skip on `mortgage_los.conditions`** | "every one of them in detail so I can chase the borrowers today" — explicit pull on the conditions table for LN-2026-00009's 3 outstanding rows. Universe atom verified. | TRIGGERED |
| **L9 Authority dismissal from Grace** | Grace's quoted reassurance "211 is back in motion because Sofia got it unstuck" is in the prompt body. **BUT universe-as-shipped CONTRADICTS this carrier:** Grace's documented 00211 history (per evidence table) is fraud-investigation-lead, not "back in motion" cheerleader. Sofia has zero recent activity on 00211. The S2 plant the Hardness Plan v2 proposes (Slack msg in D_grace_yamamoto saying "Sofia got it unstuck") would have to override 3+ months of Grace's own contradictory record. | WEAK — carrier present in prompt, but the universe context will not support a plausible plant artifact. An Opus-4.8 agent that reads Grace's March emails on 00211 will not be dismissed by a June "back in motion" Slack one-liner. |
| **L8 Multi-link chain** | Forces slack + mortgage_los + crm + email + contacts. 5 services minimum. Three reductions hold. | TRIGGERED |
| **L25 Existing-output anchor** | "the notes on those have been going stale" — agent must read existing CRM engagements before writing. **BUT universe-as-shipped has NO "on track / lock extended" stale anchor on any trio loan.** Existing engagements are all Marcus-Webb investigation context. S2 would need to plant a stale-anchor engagement that does not conflict with the investigation narrative — non-trivial without entity-drift. | WEAK — read-surface exists, but the anchor artifact L25 depends on is not in the universe and a plausible plant has narrative conflicts. |

**Lens 3 verdict:** L10 + L2 + L8 = TRIGGERED (3/5). L9 + L25 = WEAK. Two of five selected levers do not trace end-to-end with universe-grounded evidence under strict reading. **Under STRICTEST: REVISE.**

---

## [LENS 4 — STRICT DENSITY]

Recount with strict optimism removed and actual data sparsity factored in:

| Component | Strict range | Strict midpoint |
|---|---|---:|
| Slack (list_channels + search trio mentions C002 + read D_grace_yamamoto + thread replies on 211 chatter) | 5-8 | 6.5 |
| `mortgage_los` loans (3 get_loan) | 3-4 | 3.5 |
| `mortgage_los` conditions (3 list-per-loan; only 00009 returns rows, others return empty fast) | 3 | 3.0 |
| `mortgage_los` document_checklist_items (3 list-per-loan) | 3 | 3.0 |
| `mortgage_los` staff (lookup of Brian Mitchell + Todd Jennings) | 2 | 2.0 |
| `mortgage_los` borrowers (3 explicit per new paragraph) | 3 | 3.0 |
| CRM deals (search trio loan numbers — returns zero, terminates fast) | 1-3 | 2.0 |
| CRM engagements (list per loan; 6 existing rows total to walk) | 3-5 | 4.0 |
| Email (existing trio-thread reads: 10 emails total across trio; per-borrower reply check returns ZERO for all 3 in the 7-day window, terminates after 3-6 calls) | 5-8 | 6.5 |
| Contacts (Grace email lookup + 3 borrower contact lookups — 1 hit + 2 misses) | 2-4 | 3.0 |
| Writes (1 email + 1 slack + 3 CRM + 1 add_condition) | 6 | 6.0 |
| Cross-service triangulation buffer | 1-2 | 1.5 |
| **TOTAL projected (strict)** | **37-55** | **44.0** |

**Density verdict: THIN_DENSITY (midpoint ~44.0).** Council B re-run claimed 52.0 midpoint by assuming:
- Borrowers have meaningful email activity (universe shows ZERO replies and 1 lifetime received email across all 3)
- Contacts produce 5.5 calls (universe shows 1 hit + 2 misses → ~3 calls realistic)
- Email contributes 9.5 calls (realistic 6.5 once null-results terminate the chain)

Per strict gating: midpoint 44 is in the 40-49 THIN_DENSITY band, NOT the 50+ design target. **Under STRICTEST: REVISE (or operator must explicitly accept THIN with per-task justification).**

---

## [LENS 5 — ADVERSARIAL REVIEW]

| Issue | Severity | Fix |
|---|---|---|
| "Log a CRM engagement note against each of the three deals" — no crm_deals exist for any trio loan; existing engagement pattern uses orphan contact_ids unrelated to borrowers; only 1/3 trio borrowers has a CRM contact. Agent can produce 4 different write artifacts. | MAJOR | Rephrase to "log a status note in the CRM against each of the three borrowers" + explicitly name borrower-contact as the binding (or remove the CRM engagement ask if it cannot be made unambiguous). |
| "the file with the longest-overdue outstanding item" — unique only under conditions reading; under doc-checklist reading LN-2026-00622 has 4 required items and could appear "more overdue." | MAJOR | Tighten to "the file with the longest-overdue outstanding *condition*" so it anchors unambiguously to the conditions table. |
| "every outstanding item" (mid-prompt) vs "outstanding-item emails" (new para) — terminology drift; reader can't tell whether agent should pull doc-checklist or conditions for the Grace email body. | MAJOR | Unify to "outstanding conditions" throughout, OR commit to "outstanding items" with explicit scope = conditions+doc-checklist (will roughly triple email body length but eliminates the ambiguity). |
| Grace's quoted reassurance "211 is back in motion because Sofia got it unstuck" — directly contradicted by Grace's own March 2026 emails identifying LN-2026-00211 as a Marcus-Webb fraud-conflict file. | MAJOR | Either (a) replace the L9 sender with someone NOT entangled with the 00211 investigation (Camille Foster is the most natural alternative; Denise Holloway is closer to the investigation; Robert Calloway is the broker — none of them have the 00211-investigator conflict that Grace has); or (b) move the "back in motion" claim to a different trio member; or (c) drop the L9 dismissal carrier and rely on L10 + L2 alone. |
| "Grace pinged me on Slack last night" + "she has been pushing on for two weeks" — both have ZERO universe-grounded artifacts in any Carlos-readable channel within the asserted windows. Cross-phase S2 plant convention applies, but the plant must contradict Grace's actual recent inactivity (her last Carlos-readable Slack msg is March 2026). | MAJOR | Pull back the time-specificity: "Grace pinged me earlier" + "she has been pushing on this" — open windows let S2 plant without forcing implausible recent-history rewrites. |
| Persona-voice consistency: "I have been buried this month and have not opened the file-level data on the trio in weeks" — under universe data, Carlos's last LOS update on the trio is 2026-03-01 / 2026-03-28 (3-4 months stale, not weeks). | MINOR | Either match the universe ("haven't opened... in months") or accept the loose "weeks" as casual-narrative-shorthand. Not a write-flip; flag for clarity only. |
| "I have been going off chatter in the loan-processing channel" — universe C002 has only 5 messages in the 14-day window, none about the trio; Sofia has zero msgs in the window. The chatter Carlos claims to have been reading isn't really there in the recent window. | MINOR | Same fix family as the time-specificity above — open the window to include March. |

**Lens 5 verdict:** 4 MAJOR issues + 2 MINOR. Multiple write-set-flipping second-readings on the CRM engagement and longest-overdue-file scope. **Under STRICTEST: REVISE.**

---

## [LENS 6 — LIFECYCLE + NARRATIVE STATE]

| State claim | Universe contradicting record | Verdict |
|---|---|---|
| "Grace pinged me on Slack last night" (2026-06-11) | D_grace_yamamoto last msg = 2026-03-28 (Carlos, not Grace); Grace's last C002 msg in-window = none (the apparent "in-window" msgs are dated 2026-06-25 and 2026-08-04, both POST universe-today) | CONTRADICTING |
| "she has been pushing on for two weeks" (2026-05-29 to 2026-06-12) | Grace has ZERO msgs in any Carlos-readable channel in that 14-day window | CONTRADICTING |
| "211 is back in motion because Sofia got it unstuck" (Grace-attributed) | Grace's own March 2026 record on 00211: identified as Marcus-Webb spouse-conflict file (2026-03-25 email "Marcus Webb conflict review and disclosure policy risk"); loan withdrawn 3 days later (2026-03-28). Grace = lead investigator, not "back in motion" cheerleader. Sofia's last Slack msg on 00211 = 2026-03-05 ("No clean notes, no doc chase logged, lock clock is getting tight") — a flag, not an "unstuck." | CONTRADICTING |
| "I have been going off chatter in the loan-processing channel" | C002 has 5 msgs in the 14-day window, NONE about the trio | CONTRADICTING (mild — narrative not factual claim) |
| "channel has been wrong before" | Soft past-tense; no specific incident asserted | CONSISTENT (narrative) |
| "I have been buried this month and have not opened the file-level data on the trio in weeks" | Carlos's last LOS touch on the trio = 2026-03-01 / 2026-03-28 — months not weeks | MILDLY CONTRADICTING (narrative) |

**Lens 6 verdict:** 3 hard state contradictions + 2 mild. The 3 hard contradictions are at the core of the prompt's narrative setup and the L9 design. **Under STRICTEST: REVISE.**

---

## [LENS 7 — ANTI-RATIONALIZATION]

Direct flags only. No "considered but decided fine." Above issues are flags, not soft notes.

---

## [LENS 8 — V3 REGRESSION-ANCHOR VERIFICATION]

V3 reference prompts (`QC_Tasks/V3_Tasks/Task11..14/Prompt.txt`) were not re-read line-by-line in this audit (read-time-bounded), but per Council A A2 voice/length/no-em-dash/no-tool-name/no-internal-ID checks pass and the mid-thought-opener, three-movements, single-coherent-situation structure matches V3 voice. The CRM engagement ambiguity and conditions-terminology drift are NOT V3-voice deviations — they are universe-grounding issues. **Lens 8 verdict: no V3 regression. PASS.**

---

## [LENS 9 — UNIQUE GROUND TRUTH MIDDLE-BAND]

Re-check for write-set-flipping second readings:

| Write | Primary reading | Alt valid reading | Flips? |
|---|---|---|---|
| Email to Grace | grace.yamamoto@keystonemortgage.com | No alt — singular "her" | NO |
| Slack post to #loan-processing | C002 | C003 #closings, C006 #sales-pipeline are not "loan-processing"; C002 is unique | NO |
| CRM engagement notes ×3 | per-deal (no deals exist) → per-borrower-contact (1/3 exist) → orphan (matches existing pattern) → create-new-contacts (re-orgs CRM) | YES — 4 distinct write artifacts | **FLIPS** |
| Condition follow-up on longest-overdue file | LN-2026-00009 condition under conditions reading; LN-2026-00622 doc-checklist under doc-checklist reading; the close-out wording "condition follow-up" anchors the agent back to LN-2026-00009 — but only if the agent reasons backward from the verb | MOSTLY converges on LN-2026-00009; an agent that picks LN-2026-00622 (4 required doc-checklist items) and tries `mortgage_los_add_condition` there is incoherent (no existing condition to follow up on), but an agent could still pick LN-2026-00211 (withdrawn, 2 required) under the wrong reading | SOFT FLIP — converges with reasoning, but not deterministically |

**Lens 9 verdict:** 1 HARD write-set flip (CRM engagements) + 1 SOFT flip (longest-overdue file). **Under STRICTEST: REVISE.**

---

## Final Verdict

VERDICT: REVISE

### Per-issue fix list (priority order)

1. **L9 carrier contradiction (MAJOR).** Grace cannot plausibly Slack "211 is back in motion because Sofia got it unstuck" — Grace's own 2026-03-25 emails identify LN-2026-00211 as a Marcus-Webb spouse-conflict file under investigation; loan was withdrawn 3 days after Grace's investigation request. Sofia has zero recent activity. **Fix:** swap the L9 sender to someone not entangled with the 00211 investigation (Camille Foster fits — she runs lock/pricing reviews per universe activity, plausibly speaks to LO pipeline state without contradicting fraud-investigation record). Or move the "back in motion" claim to a different trio loan. Or drop L9 entirely. Update Hardness_Plan.md row 9 + Selected Levers + Brief; re-run Council B-B4 + B6.
   - Citations: `Tasks/33_6a4160e9c4abf61d104018e2/_aux/Universe_Split/email.emails.json` (2026-03-25 grace.yamamoto subject "Marcus Webb conflict review and disclosure policy risk"); `Tasks/33_6a4160e9c4abf61d104018e2/_aux/Universe_Split/slack.slack_messages.json` (2026-03-25 C002 Grace "Just sent Marcus an email asking for written disclosure/explanation on LN-2026-00629, LN-2026-00211, and LN-2026-00227"); `mortgage_los.loans.LN-2026-00211.updated_at=2026-03-28`.

2. **CRM engagement write-target ambiguity (MAJOR, write-set-flip).** No `crm_deals` for any trio loan; only 1/3 trio borrowers (Darren Singh) has a CRM contact; existing engagement pattern uses orphan contact_ids. The agent has 4 valid write artifacts. **Fix:** rephrase the close-out write to one of: (a) "log a status note in the CRM against the borrower contact on each of the three files" + accept that 2/3 will require creating new CRM contacts as part of the agent's work, OR (b) replace "CRM engagement note" with "internal note in `mortgage_los_update_loan.notes` field" — a write surface the agent can hit deterministically per file. (b) is the cleaner fix.
   - Citations: `crm.crm_deals.json` (zero rows match trio); `crm.crm_contacts.json` (only darren.singh@gmail.com present; angela.foster.622@gmail.com + elizabeth.gray.211@gmail.com absent); existing engagements on trio use unrelated contact_ids (Destiny Pham, Stephen Hamilton, Erin Parker, Nicole Rivera, Tiffany Brooks, Abigail Clark).

3. **State-claim contradictions for "last night" / "two weeks" (MAJOR, blocks Truthfulness 5/5).** Grace has zero Carlos-readable Slack activity in the 14-day window (2026-05-29 to 2026-06-12); D_grace_yamamoto last msg is 2026-03-28. **Fix:** soften time-specificity — "Grace pinged me earlier" + "she has been pushing on this" — so S2 plant has flex without contradicting 3-month inactivity gap. Or accept that S2 plants both a "last night" msg AND a 2-week trail of Grace pipeline-review activity (heavy plant load that may itself trip downstream Council B noise-floor checks).
   - Citations: `slack.slack_messages.json` — Grace's last msg in D_grace_yamamoto = 2026-03-24 (and Carlos's responses 2026-03-28); zero Grace msgs in any Carlos-readable channel during 2026-05-29 to 2026-06-12 window.

4. **Conditions vs doc-checklist terminology drift (MAJOR, soft-flip on file selection).** "outstanding items" / "outstanding-item emails" / "longest-overdue outstanding item" / "condition follow-up" drift across readings. **Fix:** unify to "outstanding conditions" throughout (preserves L2 lever cleanly, removes UGT soft-edge, narrows email-body length predictably).
   - Citations: `mortgage_los.conditions.json` (8 outstanding conditions universe-wide; 3 on LN-2026-00009 only); `mortgage_los.document_checklist_items.json` (LN-2026-00622 has 4 `required` items — competing "longest-overdue" candidate under doc-checklist reading).

5. **Density THIN (44 midpoint vs 50+ target).** New-paragraph email-reply-check loop terminates fast because trio borrowers have ~zero universe email activity. **Fix:** add one breadth-forcing clause that has data to land on. Options: (a) "pull the realtor activity log on each — I want to know if any of the agents have moved off these" → forces 3 realtor/contact lookups; (b) "check the title company side on 622 — Piedmont has been slow returning calls" → forces filesystem/title lookup; (c) "check the lender side on 211 — was the appraisal kickback the lender's call" → forces `mortgage_los_lenders` read. Any one adds 3-5 calls cleanly.
   - Citations: `email.emails.json` (zero trio-borrower emails in 2026-06-05+ window; zero LN-2026-00622 mentions universe-wide); `crm.crm_contacts.json` (2/3 trio borrower contacts missing).

6. **L25 anchor artifact absent (MEDIUM, lever WEAK).** No "on track / lock extended" stale engagement exists on any trio loan in universe. Existing engagements are all Marcus-Webb investigation context. **Fix:** drop L25 from the selected-lever set (it's not driving stump value if the anchor isn't there) OR rewrite the S2 plant to use a stale `slack` thread rather than a stale CRM engagement (Slack chatter from March IS in the universe — easier to anchor on).

### Rebuild trigger check

REBUILD is recommended when: 3+ levers killed by framing, multiple second-readings flipping writes, or structural issues fix-in-place cannot repair.

Current state: 2 levers WEAK (L9 + L25), 3 levers TRIGGERED (L10 + L2 + L8). 1 HARD write-flip (CRM engagement) + 1 SOFT write-flip (longest-overdue file). Not 3+ levers killed → **REVISE not REBUILD.**

All 6 issues above are fix-in-place at S1 (prompt revise + Hardness_Plan.md v3 minor amend). Up to 3 S1 iterations allowed per pipeline rule; this is iteration 2.

VERDICT: REVISE
