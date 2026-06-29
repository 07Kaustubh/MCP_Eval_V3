# AUDIT — Prompt (S1) — Strict Veteran QC Re-verification — ROUND 2

**Task:** 33_6a4160e9c4abf61d104018e2
**Phase:** S1 prompt
**Universe:** keystone — today 2026-06-12
**Deliverable under audit:** `5_Prompt.txt` (REVISED post-Round-1; 397 words)
**Prior verdict:** Round 1 = REVISE (UGT=3 / Feas=4 / Clarity=3 / Date=4 / Truth=3 / Cross=4; L9 carrier contradicted Grace's own 2026-03-25 investigator role on LN-2026-00211; density 44 THIN).
**Auditor stance:** STRICTEST possible interpretation — 5/5 the only PASS, every "should" → "must", every Hardness lever must trace end-to-end with cited evidence in the universe-as-shipped, density bar 50+ midpoint.
**Iteration:** Round 2 of 3 cap.

---

## Fix-application audit (Round 1 issues → Round 2 state)

| Round 1 issue | Fix applied | Universe-grounded effectiveness |
|---|---|---|
| L9 Grace authority-dismissal contradicted Grace's own LN-2026-00211 investigator record | Reframed to Carlos self-talk: "I told her 211 was back in motion because I thought Sofia had it unstuck, but I want to double-check before I send anything up to her" | **STRONG.** Self-attribution to Carlos is universe-consistent with PersonaBrief over-promise pattern. L9-from-Grace carrier is gone; replaced by **L1 first-framing trap + L25 self-anchored existing-output**, both carried inside the prompt rather than requiring a contradicting universe plant. Lever yield is preserved (the L10 reversal still triggers when the agent verifies status). |
| "She has been pushing on for two weeks" had zero Grace messages in window | "two weeks" → "weeks" | **GOOD.** Window opened; S2 plant burden reduced. Strict residue: "weeks" still suggests recent rather than 3-months-stale; minor. |
| CRM engagement write-target ambiguous (no `crm_deals` rows; 1/3 borrower contacts; orphan pattern) | "Log a CRM engagement note against each of the three deals" → "Log a CRM engagement note for each of the three" | **PARTIAL.** "Deals" removed, but the write artifact is still under-specified — agent may (a) write 3 orphan engagements mimicking existing pattern (contact_id = self / Carlos), (b) bind to Darren Singh's contact for LN-2026-00009 + orphan for the other two, or (c) create new CRM contacts for Angela Foster + Elizabeth Gray then bind. Three valid write artifacts remain. |
| Density 44 THIN | Added: "And pull the doc checklist on each one because some have items sitting in required status that I have lost track of." | **PARTIAL.** Doc-checklist read forced cleanly (~4-5 calls), but the trio borrowers have zero reply activity in the 7-day window so the email-reply loop still terminates fast. Recount comes in at **~48 midpoint** — still inside the 40-49 THIN band, not the 50+ target. |
| Bolt-on flag on "She wants" | "She wants" → "Grace wants" | **CLEAN.** Named entity restores coherence anchor. |
| Sub-dim scores | All five fix attempts above | **3 → 4 / 4 → 5 / 3 → 4 / 4 → 4 / 3 → 4 / 4 → 5.** UGT, Clarity, Date, Truth still below 5 under STRICTEST. |

---

## Per-atom Evidence Table (Round 2 re-verification)

| Atom Asserted | Universe Query | Row Excerpt | Verdict |
|---|---|---|---|
| Carlos Rivera = Loan Officer | `mortgage_los.staff name="Carlos Rivera"` | `los_staff_a7fa5b29babd` / loan_officer / active | GROUNDED |
| Carlos Slack identity | `slack.slack_users name="Carlos Rivera"` | `keystone_a7fa5b29babd` / carlos.rivera@keystonemortgage.com | GROUNDED |
| Sofia Reyes = processor (referenced as "Sofia") | `mortgage_los.staff name="Sofia Reyes"` | `los_staff_afc9caafae9d` / processor / active | GROUNDED |
| Grace Yamamoto (recipient + framing entity) | `slack.slack_users / email` | `keystone_e304643b171b` + `grace.yamamoto@keystonemortgage.com` | GROUNDED |
| LN-2026-00009 status | `mortgage_los.loans loan_number=LN-2026-00009` | `los_loan_ad53e691489a` / status=conditional_approval / assigned_lo=Carlos | GROUNDED |
| LN-2026-00211 status | `mortgage_los.loans loan_number=LN-2026-00211` | `los_loan_223826af9a5d` / status=**withdrawn** / assigned_lo=Brian Mitchell (TERM 2025-04-15) / updated 2026-03-28 | GROUNDED — L10 trap intact |
| LN-2026-00622 status | `mortgage_los.loans loan_number=LN-2026-00622` | `los_loan_6507d3b85a25` / status=processing / assigned_lo=Todd Jennings (TERM 2024-07-31) | GROUNDED |
| LN-2026-00009 has 3 outstanding conditions | `mortgage_los.conditions loan_id=los_loan_ad53e691489a status=outstanding` | 3 rows, oldest issued 2026-02-27 | GROUNDED |
| Doc-checklist rows for trio | `mortgage_los.document_checklist_items loan_id IN trio` | LN-2026-00009 (some required), LN-2026-00211 (14 items received/required), LN-2026-00622 (4 required) | GROUNDED — doc-checklist read surface real |
| Carlos's self-attributed "211 back in motion" | PersonaBrief — Carlos "tends to over-promise timelines to borrowers" | Documented over-promise pattern | GROUNDED — internal-state assertion now consistent with persona |
| Grace ping "last night" (2026-06-11) | `slack.slack_messages user=grace AND channel IN Carlos-readable AND created_at IN window` | **ZERO rows.** D_grace_yamamoto last msg 2026-03-28; Grace's June C002 msgs all post-2026-06-12 | NOT GROUNDED — S2-plant dependency (acceptable contract per Council A A8 + A3) but at S1-time still a state assertion the universe does not support |
| Grace pushing "for weeks" | Window now open-ended (was "two weeks") | Grace's last Carlos-readable activity on pipeline review = March 2026; "weeks" loosely accommodates that as a stretched timescale | PARTIAL — plausible under loose reading; S2 still needs a confirming plant |
| LN-2026-00009 borrower (Darren Singh) | `mortgage_los.borrowers + crm.crm_contacts` | LOS row present; CRM contact `crm_contact_34ecb8a5b6f0` present | GROUNDED |
| LN-2026-00211 borrower (Elizabeth Gray) | `mortgage_los.borrowers + crm.crm_contacts` | LOS row present; CRM contact MISSING | PARTIAL — borrower row exists; CRM bind requires contact creation |
| LN-2026-00622 borrower (Angela Foster) | `mortgage_los.borrowers + crm.crm_contacts` | LOS row present; CRM contact MISSING | PARTIAL — same as Elizabeth |
| Trio borrower replies 2026-06-05..2026-06-12 | `email.emails sender OR recipients IN trio_emails timestamp IN window` | **ZERO rows.** Lifetime: Darren received 1 (none sent); Angela / Elizabeth zero in both directions | NOT GROUNDED — null-result action; agent's email-reply check returns "none found", which is itself a fine outcome but the projected density attributed to this read is over-estimated |
| Existing trio CRM engagement pattern | `crm.crm_engagements body CONTAINS trio loan_numbers` | 6 rows; all use orphan contact_ids unrelated to trio borrowers (Destiny Pham, Stephen Hamilton, Erin Parker, Nicole Rivera, Tiffany Brooks, Abigail Clark) | GROUNDED — orphan-write pattern is the canonical mimic target |
| "the notes on those have been going stale" | Same engagement set | 6 engagements span 2026-02-09 to 2026-04-07; oldest 4 months old at universe-today — qualifies as stale | GROUNDED |
| "longest-overdue outstanding item" → condition follow-up | `mortgage_los.conditions` for trio | Only LN-2026-00009 has outstanding conditions (3); oldest = `los_cond_d7fdad61f9fa` (appraisal report, 2026-02-27) | GROUNDED *under conditions reading*; under doc-checklist reading LN-2026-00211 (14 items) or LN-2026-00622 (4 required items) are competing candidates → SOFT UGT FLIP |
| C002 #loan-processing | `slack.slack_channels id=C002` | name=loan-processing, public, 334 msgs | GROUNDED |
| Write surface: `mortgage_los_add_condition` available | tool catalog | available; requires loan_id | GROUNDED |

**Truthfulness floor:** 1 hard NOT-GROUNDED ("last night" — S2 dependency) + 3 PARTIAL (2 CRM borrower binds missing; "weeks" loose). The hard contradiction count drops from 4 (round 1) to 1 (round 2) — major improvement. Under STRICTEST audit-prompt rule "Empty evidence column → forced score ≤ 4" (because the hard NOT-GROUNDED is an acceptable cross-phase contract not a fabrication): **Truthfulness = 4**, not 5.

---

## [LENS 1 — STRICT QC SCORING] (Round 2 re-score)

| Sub-dim | R1 | R2 | Direction | Reason |
|---|---:|---:|:---:|---|
| Unique Ground Truth | 3 | **4** | ↑ | "Deals" removed; orphan-mimic is dominant path. Residual softness: 1/3 borrowers has CRM contact → agent may bind for Darren only + orphan others (still a 3-write set; artifact differs). "Longest-overdue outstanding item" now has parallel scope (conditions vs doc-checklist) — soft UGT flip; verb "condition follow-up" anchors back to conditions but only via back-reasoning. Not 5/5 under strictest. |
| Feasibility | 4 | **5** | ↑ | All services available; orphan-engagement write path is now mechanically clean (matches existing pattern). |
| Explicit Tool Mention | 5 | **5** | = | Zero tool names. |
| Clarity & Specificity | 3 | **4** | ↑ | Doc-checklist add structured the terminology (conditions vs required-status items now distinct). But introduces parallel scope on "every outstanding item still sitting" (Grace email body) and "longest-overdue outstanding item" (close-out write). Improved but not 5. |
| Contrived / Unnatural | 5 | **5** | = | LO pipeline review for Director of Ops + borrower call-prep is textbook. |
| Alignment with Today's Date | 4 | **4** | = | "tomorrow afternoon"=2026-06-13, "this afternoon"=2026-06-12, "last week"=2026-06-05+ all resolve. But "last night" Grace ping still has zero universe data and a 2.5-month inactivity gap to bridge for the S2 plant. Window-softening on "weeks" helps but "last night" persists. |
| Truthfulness | 3 | **4** | ↑ | Grace contradiction RESOLVED via Carlos self-attribution. Residual: "last night" S2-dependency + 2/3 CRM borrower contacts missing. Major lift but not 5. |
| Tool Use & Cross-service | 4 | **5** | ↑ | 5 services minimum confirmed (mortgage_los × 5 read-classes + slack + crm + email + contacts). Doc-checklist add reinforces mortgage_los breadth. |
| Investigation + Action | 5 | **5** | = | Read-heavy + 4 writes. |
| Coherence / Bolt-on | 5 | **5** | = | "Grace wants" anchor restores coherence. All writes flow from the discovery. |
| Persona | 5 | **5** | = | Carlos voice intact; over-promise pattern reinforced by self-attribution. |
| Business Function | 5 | **5** | = | Loan Operations confirmed. |

**Lens 1 verdict:** 4 sub-dims still below 5/5 under STRICTEST (UGT=4, Clarity=4, Date-alignment=4, Truthfulness=4). Down from 5 in Round 1, but not at PASS bar.

---

## [LENS 2 — ANSWER-LEAKAGE SWEEP] (Round 2)

| Target answer | Round 2 scan | Verdict |
|---|---|---|
| (a) LN-2026-00211 withdrawn | "I told her 211 was back in motion because I thought Sofia had it unstuck" plants OPPOSITE direction. "I want to double-check" + "the truth from the actual files" force verification. | NO LEAK — narrative trap intact |
| (b) 3 overdue conditions on LN-2026-00009 | "conditions sitting outstanding that should have been cleared weeks ago" + "every one of them in detail" + "longest-overdue outstanding item" + "condition follow-up" — pre-narrows to LN-2026-00009 (only trio member with outstanding conditions) by elimination but does NOT leak count or content | SOFT — same as Round 1 |
| (c) LN-2026-00622 → Todd not Carlos | "who is the loan officer of record" forces discovery. No leak. | NO LEAK |

**Lens 2 verdict:** No BLOCKER leakage. Round 1 soft-narrowing on (b) persists unchanged.

---

## [LENS 3 — HARDNESS END-TO-END] (Round 2)

| Lever | Round 2 carrier | Verdict |
|---|---|---|
| **L10 Reversal on LN-2026-00211** | "Check the genuine status on each one right now" + "who is the loan officer of record" + "I want to double-check" + Carlos's quoted overpromise "I told her 211 was back in motion" | **STRONG — TRIGGERED.** Carlos's self-attributed wrong-belief is a more credible trap than a Grace-attributed reassurance because it can't be cross-checked against Grace's recent inactivity. |
| **L2 Structured-DB skip on `mortgage_los.conditions`** | "every one of them in detail so I can chase the borrowers today" — explicit | TRIGGERED |
| **L9 Authority dismissal from Grace** | **NO LONGER PRESENT.** Grace's reassurance carrier has been removed; the wrong-belief is self-attributed | **REPLACED.** L9 from the original plan is gone. **Substitute lever carriers: L1 first-framing trap + L25 existing-output anchor** (Carlos's own quoted self-belief acts as the anchor). Both verified in prompt body. PROPAGATE: Hardness_Plan.md still lists L9 in Selected Levers — needs amendment to reflect L9 → L1+L25 substitution. |
| **L8 Multi-link chain** | mortgage_los (5 read-classes) + slack + crm + email + contacts | TRIGGERED + STRENGTHENED by doc-checklist add |
| **L25 Existing-output anchor** | (a) Universe trio CRM engagements (6 rows; "the notes on those have been going stale" surfaces them — universe-grounded now); (b) Carlos's self-stated belief inside the prompt acting as a second-layer anchor | **STRONG — TRIGGERED.** Round 1 L25 was WEAK because universe lacked a stale "on track" engagement; in Round 2 the stale-engagement read is forced by "going stale" verbatim and Carlos's self-told overpromise reinforces. |

**Lens 3 verdict:** 4 of 5 originally-planned levers TRIGGERED (L10 / L2 / L8 / L25). L9-from-Grace REPLACED by L1+L25-via-self-attribution — substitution is functionally equivalent or stronger, but **Hardness_Plan.md needs amendment** (Selected Levers row L9 → L1+L25; Stump Hypothesis #1 mechanism description; Hardness Brief). This is a documentation PROPAGATE, not a structural defect.

---

## [LENS 4 — STRICT DENSITY] (Round 2)

| Component | Strict range | Strict midpoint |
|---|---|---:|
| Slack (list channels + search trio mentions C002 + read D_grace_yamamoto + thread replies on 211 chatter) | 5-8 | 6.5 |
| `mortgage_los` loans (3 get_loan) | 3-4 | 3.5 |
| `mortgage_los` conditions (3 list-per-loan + "every one of them in detail" forces dives on 00009's 3 conditions) | 3-5 | 4.0 |
| `mortgage_los` document_checklist_items (3 list-per-loan + "items sitting in required status" prompts dives on 00211's 14 + 00622's 4) | 4-6 | 5.0 |
| `mortgage_los` staff (Brian Mitchell + Todd Jennings — both terminated, surfacing the L6 trap) | 2 | 2.0 |
| `mortgage_los` borrowers (3 explicit) | 3 | 3.0 |
| CRM deals (search trio — returns zero, terminates fast) | 1-3 | 2.0 |
| CRM engagements (list per loan; 6 existing rows to walk for "going stale" check) | 3-5 | 4.0 |
| Email (existing trio-thread reads — 10 emails total — + per-borrower reply check returns null for all 3 in 7-day window, terminates fast) | 6-10 | 8.0 |
| Contacts (Grace email lookup + 3 borrower contact-resolution attempts — 1 hit + 2 misses) | 2-4 | 3.0 |
| Writes (1 email + 1 slack + 3 CRM + 1 add_condition) | 6 | 6.0 |
| Cross-service triangulation buffer | 1-2 | 1.5 |
| **TOTAL projected (strict)** | **39-58** | **48.5** |

**Density verdict: THIN_DENSITY (midpoint 48.5).** Improvement of +4.5 over Round 1 (44 → 48.5) from the doc-checklist add. Still inside the 40-49 THIN band; not at the 50+ design target.

Drivers preventing 50+ even with the doc-checklist add:
- Trio borrowers have **zero email-reply activity** in the window — reply-check loop returns null fast across all 3 borrowers (Round 1 finding still holds; the doc-checklist add doesn't compensate)
- **2/3 CRM borrower contacts missing** — contacts loop terminates with miss-misses faster than the 5.5-call estimate Council B re-run assumed
- CRM `crm_deals` returns zero rows for all trio — deal-discovery terminates fast

**Per pipeline rule:** midpoint 48.5 is in the **40-49 THIN_DENSITY band — operator may continue with explicit per-task justification**, but the task is at risk of underflow on real platform runs. Under STRICTEST 50+ design-target reading: **does not PASS the design bar.**

---

## [LENS 5 — ADVERSARIAL REVIEW] (Round 2)

| Issue | Severity | Round 2 state | Recommended fix |
|---|---|---|---|
| CRM engagement write — 3 valid artifacts (orphan / Darren-bound + 2 orphan / create-new-contacts) | MEDIUM (down from MAJOR R1) | Improved but not fully resolved | Tighten to: "drop a short status note on each of the three files in the CRM matching how the existing engagement notes on these are written" — explicit pattern-mimic instruction collapses alt-paths |
| "Longest-overdue outstanding item" — parallel scope (conditions vs doc-checklist) since R2 doc-checklist add | MEDIUM (new in R2) | Verb "condition follow-up" anchors back to conditions only via back-reasoning | Tighten to: "the file with the longest-overdue outstanding **condition**" — single word fix |
| "Last night" Grace ping still has zero universe data | MEDIUM (carry-over R1) | Softened on adjacent "weeks" but "last night" specificity persists | Optional: "Grace pinged me earlier" — opens the plant window further |
| Hardness_Plan.md still lists L9 in Selected Levers | LOW | Prompt no longer uses L9-from-Grace; substitute carriers (L1 + L25-via-self-attribution) work | Amend Hardness_Plan: Selected Levers L9 → "L1 first-framing + L25 self-anchored existing-output"; Stump Hypothesis #1 mechanism; Hardness Brief — replace the D_grace_yamamoto plant requirement |
| Trio borrower email-reply loop terminates fast on null results — density relies partially on this | LOW | Universe has zero reply activity in window | Optional density push: add one breadth-forcing clause with real data — e.g. "check the lender side on each, who is on the file and how the relationship is going" forces `mortgage_los_lenders` lookups; data exists |

**Lens 5 verdict:** 2 MEDIUM (write-set softness; longest-overdue ambiguity) + 1 MEDIUM carry-over (last-night) + 2 LOW. Not BLOCKER-grade but holds 4 sub-dims off 5/5.

---

## [LENS 6 — LIFECYCLE + NARRATIVE STATE] (Round 2)

| Round 1 contradiction | Round 2 state | Verdict |
|---|---|---|
| Grace's quoted reassurance contradicted her own LN-2026-00211 investigator emails | RESOLVED — self-attributed to Carlos; consistent with PersonaBrief over-promise pattern | RESOLVED |
| "She has been pushing on for two weeks" had zero in-window Grace activity | SOFTENED — now "weeks" (open window) | PARTIAL — better but residual gap (Grace's last pipeline-review activity is March 2026, 12+ weeks ago) |
| "Grace pinged me on Slack last night" | UNCHANGED — still S2-plant dependency over 2.5-month inactivity gap | CONTRADICTING — same as Round 1; relies on S2 plant convention |
| "I have been going off chatter in the loan-processing channel" | UNCHANGED — C002 has 5 msgs in 14-day window, none about trio | MILDLY CONTRADICTING (narrative, not factual claim) |
| "I have been buried this month and have not opened the file-level data on the trio in weeks" | UNCHANGED — last LOS touch on trio = March 2026 (months ago) | MILDLY CONTRADICTING (narrative; "weeks" softer than "this month") |

**Lens 6 verdict:** 1 of 3 hard contradictions RESOLVED (Grace-attribution flip); 1 PARTIAL (weeks-softening); 1 still hard (last-night). Net: substantial improvement, but the "last night" claim is the last load-bearing state-implying claim without a universe anchor.

---

## [LENS 7 — ANTI-RATIONALIZATION]

Direct flags only. Above are concerns, not "considered but decided fine" rationalizations. No round-2 issue is being silenced.

---

## [LENS 8 — V3 REGRESSION-ANCHOR VERIFICATION]

Voice scan vs V3 reference Task11..14:
- Mid-thought opener: "Grace pinged me on Slack last night about the pipeline review she has been pushing on for weeks." ✓
- Three movements (trigger / context / asks): ✓
- Single coherent situation: ✓
- No em-dash / en-dash / tool name / internal ID: re-verified clean ✓
- Word count 397 ≤ 500: ✓
- No "at least N": ✓

**Lens 8 verdict: PASS.** No V3 regression; new doc-checklist sentence and Grace-anchor rephrase are voice-consistent.

---

## [LENS 9 — UNIQUE GROUND TRUTH MIDDLE-BAND] (Round 2)

| Write target | Primary reading | Alt readings | Flips? |
|---|---|---|---|
| Email to Grace | grace.yamamoto@keystonemortgage.com | — | NO |
| Slack post → #loan-processing (C002) | C002 unique | — | NO |
| CRM engagement notes ×3 | orphan-mimic (matches existing pattern) | (a) Darren-contact-bound + 2 orphan; (b) create 2 new CRM contacts for Angela/Elizabeth then bind all 3 | **2 ALT ARTIFACTS** — soft flip; functional output equivalent (3 engagements per loan) but binding metadata differs |
| Condition follow-up on longest-overdue file | LN-2026-00009 (conditions reading) — only trio member with outstanding conditions | LN-2026-00211 (doc-checklist reading, 14 items) or LN-2026-00622 (doc-checklist reading, 4 required items) — verb `add_condition` rules these out only by back-reasoning | **SOFT FLIP** persists from R1; doc-checklist add introduced a parallel scope |

**Lens 9 verdict:** 1 SOFT engagement-binding flip + 1 SOFT longest-overdue-file flip (verb anchors back, but not deterministically). Down from 1 HARD + 1 SOFT in Round 1.

---

## Final Verdict

**VERDICT: REVISE**

Round 2 made substantial progress — Grace contradiction RESOLVED (the highest-stakes Round 1 issue), 3 sub-dims lifted from 3 → 4, 2 sub-dims lifted from 4 → 5, density +4.5. But under STRICTEST interpretation (5/5 only, 50+ density target), the prompt does not yet PASS.

### Per-issue fix list (priority order, Round 3 — final iteration available)

1. **CRM engagement write-target — collapse to a single artifact (MEDIUM, write-set softness).** Rephrase to: *"Drop a short status note on each of the three in the CRM matching how the existing engagement notes on these are written."* — explicit pattern-mimic instruction removes the orphan-vs-bound ambiguity. Lifts UGT to 5.
   - Citations: `crm.crm_engagements` 6 trio rows all use orphan contact_ids (not borrowers); `crm.crm_contacts` 1/3 trio borrowers present.

2. **Longest-overdue scope — one-word tightening (MEDIUM, soft-flip).** Replace *"the file with the longest-overdue outstanding item"* with *"the file with the longest-overdue outstanding **condition**"*. Removes the doc-checklist parallel-scope flip. Lifts Clarity to 5.
   - Citations: `mortgage_los.conditions.json` (only LN-2026-00009 has outstanding conditions); `mortgage_los.document_checklist_items.json` (LN-2026-00211 = 14 items, LN-2026-00622 = 4 — competing under loose reading).

3. **"Last night" state assertion — soften to plant-flex (MEDIUM, carry-over).** Replace *"Grace pinged me on Slack last night"* with *"Grace pinged me on Slack earlier"* OR *"Grace pinged me on Slack"* (no time qualifier). Removes the last hard state-contradiction; S2 plant flexibility improves materially. Lifts Date-alignment + Truthfulness to 5.
   - Citations: `slack.slack_messages` — Grace's last Carlos-readable msg = 2026-03-28 in D_grace_yamamoto; zero msgs 2026-06-11.

4. **Density push to 50+ (THIN, +1.5-3 needed).** Add ONE breadth-forcing clause with real universe data. Options:
   - (a) "**Check the lender side on each one — I want to know which lender is on the file and whether the relationship is up to date.**" → forces 3× `mortgage_los_lenders` lookups + 1-2 connecting reads = +4-5 calls cleanly. (Universe has `mortgage_los.lenders` table populated.)
   - (b) "**Pull the latest fee snapshot per loan from the appraisal / credit-report side so I am not surprised.**" → forces stripe or quickbooks reads = +3-4 calls.
   - (a) is cleaner and on-voice for Carlos. Lifts midpoint to ~52-53 (PASS).
   - Citations: `mortgage_los.lenders.json` exists with rows; trio loans have lender_id binding.

5. **Hardness_Plan.md amendment (LOW, documentation).** Update three locations:
   - Selected Levers — remove L9 "Grace authority dismissal" carrier; replace with: *"L1 first-framing trap + L25 self-anchored existing-output — Carlos's own quoted overpromise 'I told her 211 was back in motion' is the carrier; no Grace-attributed plant needed."*
   - Stump Hypothesis #1 — change "Mechanism: L10 reversal + L9 authority dismissal" → "Mechanism: L10 reversal + L1 first-framing via Carlos's self-told overpromise."
   - Hardness Brief — remove the D_grace_yamamoto plant requirement; the trap now lives entirely inside the prompt body.
   - No re-run of Council B-B4 / B6 needed; functional lever yield is preserved or strengthened.

### Rebuild trigger check

REBUILD warranted only when: 3+ levers killed by framing OR multiple write-flipping second-readings OR structural defect un-fixable in place.

Current state: 4 levers TRIGGERED (L10 + L2 + L8 + L25); 1 lever (L9) REPLACED by functionally-equivalent substitute (L1+L25). Zero HARD write-flips; 2 SOFT flips both resolvable by single-word edits. Density 48.5 (THIN, not INSUFFICIENT). **Not REBUILD → REVISE (Round 3 final).**

All 5 fixes above are single-paragraph or single-word edits at S1 + a Hardness_Plan.md text amendment. Round 3 is the final S1 iteration; if Round 3 PASSes, ship S1 and proceed to S2.

VERDICT: REVISE
