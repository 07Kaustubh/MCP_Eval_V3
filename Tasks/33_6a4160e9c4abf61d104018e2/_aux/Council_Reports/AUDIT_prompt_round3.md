# AUDIT — Prompt (S1) — Strict Veteran QC Re-verification — ROUND 3 (FINAL)

**Task:** 33_6a4160e9c4abf61d104018e2
**Phase:** S1 prompt
**Universe:** keystone — today 2026-06-12
**Deliverable under audit:** `5_Prompt.txt` (REVISED R3; 397 words; em-dash/en-dash/tool-name clean re-verified)
**Prior verdict:** R1 REVISE → R2 REVISE
**Auditor stance:** STRICTEST interpretation — 5/5 only PASS, every "should" → "must", levers traced end-to-end with cited universe rows, density bar 50+ midpoint, per-atom evidence for every state assertion.
**Iteration:** Round 3 of 3 cap (FINAL allowed).

---

## R2 → R3 fix-application audit

| R2 residue | R3 fix applied | Universe-grounded effectiveness |
|---|---|---|
| "Grace pinged me on Slack last night" — zero Grace activity 2026-06-11 in Carlos-readable channels | Dropped "last night" entirely; now reads "Grace pinged me on Slack about the pipeline review she has been pushing on for weeks." | **STRONG.** Hard "last night" state-claim removed. The remaining ping is undated and absorbs a single S2 plant anywhere Carlos can read. |
| CRM engagement orphan-vs-Darren-bound ambiguity (1/3 borrowers has CRM contact; orphan-mimic pattern in universe) | NO prompt fix. Operator-documented decision: defer artifact-binding scoring to S3-rubric layer; rubric scores on engagement COUNT (3 created) regardless of binding metadata. | **PARTIAL.** R3 fix narrative explicitly states "NOT a S1 prompt fix". Single-phrase pattern-mimic instruction was available (R2 §1 recommendation) and not applied. Operator deferral, not universe-unachievable. |
| "Longest-overdue outstanding item" — parallel scope conditions vs doc-checklist | "outstanding item" → "outstanding **condition**" (single-word add) | **STRONG.** Noun anchors directly to `mortgage_los.conditions`. Verb "condition follow-up" + noun "outstanding condition" both align. Doc-checklist alt-path eliminated. |
| Density 48.5 — THIN | Added: "And tell me where each of the rate locks sits because I cannot remember the expirations." | **STRONG.** Field verified present in `mortgage_los.loans` (column 7 of 26); all three trio rows populated with EXPIRED dates (2026-04-09 / 2026-04-15 / 2026-04-26 — all 47-64 days past universe today). Forces 3× loan reads (already counted) + 3× distinct lender lookups (distinct lender_ids verified per loan) + 1-2 lender-relationship reads. Net density add: +3 to +5 calls. New projected midpoint: **51.5** (PASS at 50+ target). Hardness bonus: all three rate locks expired is a layered Grace-email finding the agent must surface. |
| Hardness_Plan L9 → L1+L25 | Plan v3 amended: Selected Levers row replaced with "L1 First-framing + L25 Existing-output anchor (Carlos's own quoted over-promise)"; Hardness Brief paragraph also updated v3 with corrected rationale | **CLEAN.** Plan now matches prompt carrier. L9 row replaced; Hardness Brief reflects v3 reasoning that Grace cannot voice the authority-dismissal given her March 2026 investigative record on LN-2026-00211. |
| "Weeks" loose temporal anchor for Grace pushing | NO prompt fix. Operator-documented: "weeks" intentionally vague to absorb S2 plant; one Grace message sometime "recently" satisfies. | **PARTIAL.** Universe shows Grace's last Carlos-readable activity on pipeline review = D_grace_yamamoto MPIM. S2 plant convention is the path. Operator deferral, not universe-unachievable. |

---

## Per-atom Evidence Table (R3 — full re-verification of every state-implying claim)

| Atom asserted in R3 prompt | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| Carlos Rivera = LO at Keystone | `mortgage_los.staff name="Carlos Rivera"` | `los_staff_a7fa5b29babd` / role=loan_officer / status=active | GROUNDED |
| Carlos Slack identity | `slack.slack_users name="Carlos Rivera"` | `keystone_a7fa5b29babd` / carlos.rivera@keystonemortgage.com | GROUNDED |
| Sofia (hallway / Slack reference) | `mortgage_los.staff name="Sofia Reyes"` | `los_staff_afc9caafae9d` / processor / active | GROUNDED |
| Grace (email recipient + framing entity) | `slack.slack_users name="Grace Yamamoto"` / `email` surface | `keystone_e304643b171b` + `grace.yamamoto@keystonemortgage.com` | GROUNDED |
| LN-2026-00009 status = `conditional_approval`, assigned_lo = Carlos | `mortgage_los.loans` | `los_loan_ad53e691489a` / status=conditional_approval / assigned_lo=`los_staff_a7fa5b29babd` (Carlos) / rate_lock_exp=2026-04-15 (EXPIRED) | GROUNDED |
| LN-2026-00211 status = **withdrawn**, assigned_lo ≠ Carlos | `mortgage_los.loans` | `los_loan_223826af9a5d` / status=withdrawn / assigned_lo=`los_staff_6d606f7506a7` (Brian Mitchell; terminated 2025-04-15) / rate_lock_exp=2026-04-09 (EXPIRED) | GROUNDED — L10 trap intact |
| LN-2026-00622 status = `processing`, assigned_lo ≠ Carlos | `mortgage_los.loans` | `los_loan_6507d3b85a25` / status=processing / assigned_lo=`los_staff_0375f7c91014` (Todd Jennings; terminated 2024-07-31) / rate_lock_exp=2026-04-26 (EXPIRED) | GROUNDED |
| Trio has rate locks Carlos has "lost track of expirations" on | `mortgage_los.loans` rate_lock_expiration field | All three: 2026-04-09 / 2026-04-15 / 2026-04-26 — all 47-64 days past universe today | GROUNDED — naturally consistent with persona ("buried this month"); hardness bonus surface for Grace email |
| 3 distinct lenders on trio (forces 3 lender lookups) | `mortgage_los.loans` lender_id field | `los_lender_345751ed726c` / `los_lender_b962d0e22e0f` / `los_lender_533a73fed6b6` — distinct per loan | GROUNDED — density add lands cleanly |
| LN-2026-00009 has outstanding conditions | `mortgage_los.conditions loan_id=los_loan_ad53e691489a status=outstanding` | 3 rows; oldest = `los_cond_d7fdad61f9fa` issued 2026-02-27 (~105 days overdue) | GROUNDED |
| "Longest-overdue outstanding CONDITION" anchors to single file | `mortgage_los.conditions status=outstanding` filtered to trio | Only LN-2026-00009 has outstanding conditions → unique anchor to `los_loan_ad53e691489a` | GROUNDED — UGT flip eliminated by R3 single-word fix |
| Doc-checklist rows for trio | `mortgage_los.document_checklist_items loan_id IN trio` | Real rows for all three (per R2 audit table) | GROUNDED |
| Carlos self-attributed "211 back in motion because I thought Sofia had it unstuck" | PersonaBrief — "He tends to over-promise timelines to borrowers" | Documented over-promise pattern | GROUNDED — internal self-talk consistent with persona |
| Trio borrower contacts (Darren Singh / Elizabeth Gray / Angela Foster) | `mortgage_los.borrowers` + `crm.crm_contacts` | LOS rows present for all 3; CRM contact present for Darren only (`crm_contact_34ecb8a5b6f0`); Elizabeth + Angela missing from CRM | PARTIAL — borrower rows exist; CRM-bind requires contact creation for 2/3 |
| Existing trio CRM engagement pattern (orphan-bound) | `crm.crm_engagements body CONTAINS trio loan_numbers` | 6 rows; all use orphan contact_ids (no link to trio borrowers) | GROUNDED — orphan-mimic is the canonical pattern; agent following pattern produces orphan engagements |
| Trio CRM engagement notes "going stale" | Same engagement set | 6 engagements span 2026-02-09 to 2026-04-07; oldest 4+ months at universe-today | GROUNDED |
| Trio borrower reply activity in 7-day window | `email.emails sender OR recipients IN trio_emails AND timestamp 2026-06-05..2026-06-12` | Zero rows | GROUNDED null-result; agent's check terminates fast — does not break truthfulness, but compresses density estimate |
| C002 #loan-processing as Slack post target | `slack.slack_channels id=C002` | name=loan-processing / public / 334 msgs | GROUNDED |
| Email send-target for Grace | `contacts` + Grace's Slack user record | grace.yamamoto@keystonemortgage.com | GROUNDED |
| Write surface `mortgage_los_add_condition` | tool catalog (`8_Server_Tools_Details.json`-equivalent for keystone) | Available; requires loan_id | GROUNDED |
| **Grace pinged Carlos "about the pipeline review she has been pushing on for weeks"** | `slack.slack_messages` Grace activity in Carlos-readable channels last N weeks | No 2026-06 ping yet; last Grace D_grace_yamamoto activity 2026-03-28 (~11 weeks before universe-today) | **NOT GROUNDED at S1-time — S2-plant-flex.** Operator-documented cross-phase contract: S2 must plant ONE Grace ping. Strictest residue: "for weeks" present-perfect implies sustained activity; single plant satisfies "pinged" but is loose against "pushing on for weeks". |

**Truthfulness floor:** 1 NOT GROUNDED (S2-plant-flex, operator deferral) + 2 PARTIAL (CRM borrower binds; "for weeks" looseness). Hard contradictions: 0 (R1=4, R2=1, R3=0). Major lift from R2.

---

## [LENS 1 — STRICT QC SCORING] R3 re-score

| Sub-dim | R1 | R2 | R3 | Notes |
|---|---:|---:|---:|---|
| Unique Ground Truth | 3 | 4 | **4** | "Longest-overdue outstanding **condition**" cleanly anchors → LN-2026-00009 unique. BUT CRM engagement write target retains orphan-vs-Darren-bound 2-artifact ambiguity (operator declined the single-phrase pattern-mimic fix). Single artifact achievable via prompt-side rephrase → 5/5 NOT mathematically unachievable; this is operator-deferral. |
| Feasibility | 4 | 5 | **5** | All services available; `rate_lock_expiration` field + `lender_id` foreign-key both verified. |
| Explicit Tool Mention | 5 | 5 | **5** | Zero tool names re-verified across the new rate-lock sentence. |
| Clarity & Specificity | 3 | 4 | **5** | "Outstanding condition" single-word fix kills the doc-checklist alt-path. Rate-lock sentence is informal but unambiguous (expiration-state per loan). No remaining parallel-scope phrases. |
| Contrived / Unnatural | 5 | 5 | **5** | LO pre-deadline pipeline-review packet + borrower call-prep + "lost track of expirations" all textbook Carlos. |
| Alignment with Today's Date | 4 | 4 | **4** | "Last night" REMOVED. Resolved relatives ("tomorrow afternoon"=2026-06-13, "this afternoon"=2026-06-12, "last week"=2026-06-05+) all clean. Residue: "she has been pushing on for weeks" — present-perfect over a window where Grace's last Carlos-readable pipeline-review activity is 11 weeks back. Single S2 plant satisfies "pinged" minimally but not "pushing on for weeks" with conviction. 5/5 achievable via prompt-side temporal trim ("a while" / remove duration) → operator-deferral, not universe-unachievable. |
| Truthfulness | 3 | 4 | **5** | All hard state assertions now grounded or single-S2-plant-flex. Rate-lock claim grounded (field present + populated). Self-attributed overpromise grounded via PersonaBrief. CRM-bind partial is artifact-shape, not factual lie (Truthfulness is about what the prompt CLAIMS; the prompt doesn't claim a specific binding). 0 hard contradictions. Lifts to 5. |
| Tool Use & Cross-service | 4 | 5 | **5** | 7 distinct services: mortgage_los (loans, conditions, document_checklist_items, lenders, staff, borrowers) + slack + crm + email + contacts. Rate-lock add reinforces mortgage_los breadth via distinct lender lookups. |
| Investigation + Action | 5 | 5 | **5** | Read-heavy + 4 writes (email Grace / Slack C002 / 3 CRM engagements / 1 add_condition). |
| Coherence / Bolt-on | 5 | 5 | **5** | Every ask flows from "Grace deadline + I have been buried + need real picture". Rate-lock sentence anchors to "I cannot remember the expirations" — natural fold-in. |
| Persona | 5 | 5 | **5** | Carlos voice: over-promise pattern (self-attributed 211 belief), over-extended ("buried this month"), informal LO speech ("lost track", "stale", "I cannot remember"). |
| Business Function | 5 | 5 | **5** | Loan Operations: pipeline review + outstanding-condition chase + rate-lock check + CRM hygiene + borrower call prep. |

**Lens 1 R3 verdict:** **10/12 at 5/5 + 2/12 at 4/5** (UGT and Date-alignment).

**Strictest-acceptable analysis of the two 4s:**
- **UGT (4):** 5/5 IS prompt-side-achievable via a single-phrase pattern-mimic rephrase (R2 §1 recommendation). Operator declined and deferred binding ambiguity to S3 count-based rubric scoring. Per audit instruction's exact language, this is "operator giving up", not "mathematically unachievable under per-task universe constraints". Does NOT qualify for strictest 5/5 justification.
- **Date-alignment (4):** 5/5 IS prompt-side-achievable via temporal-softening ("for a while" / remove "for weeks"). Operator declined and deferred to S2-plant convention. Same classification: operator-deferral, not universe-unachievable.

Both residues are documented cross-phase contracts (legitimate pipeline pattern per AGENTS.md Council A A8 + A3) BUT under STRICTEST audit reading per the instruction's exact language, they fall on the operator-deferral side of the line.

---

## [LENS 2 — ANSWER-LEAKAGE SWEEP] R3

| Target answer | R3 scan | Verdict |
|---|---|---|
| LN-2026-00211 withdrawn | "I told her 211 was back in motion because I thought Sofia had it unstuck" + "double-check before I send anything up" — OPPOSITE direction; L10 trap intact | NO LEAK |
| 3 overdue conditions on LN-2026-00009 | "every one of them in detail" + "longest-overdue outstanding condition" — pre-narrows to LN-2026-00009 by elimination (only trio member with outstanding conditions) but does NOT leak count or condition IDs | SOFT (carry-over from R1/R2; unchanged) |
| LN-2026-00622 → Todd not Carlos | "who is the loan officer of record" forces discovery | NO LEAK |
| Rate-lock expirations | "tell me where each of the rate locks sits" + "I cannot remember the expirations" — forces discovery; does NOT state that all three are expired | NO LEAK |

**Lens 2 R3 verdict:** No BLOCKER leakage. Soft narrowing on conditions unchanged.

---

## [LENS 3 — HARDNESS END-TO-END] R3

| Lever | R3 carrier | Verdict |
|---|---|---|
| **L10 Reversal on LN-2026-00211** | Carlos self-quoted overpromise + "double-check" instruction + "the channel has been wrong before" | TRIGGERED (stronger than R1 — no Grace-contradiction risk) |
| **L2 Structured-DB skip on `mortgage_los.conditions`** | "every one of them in detail" + "longest-overdue outstanding condition" + verb anchor `add_condition` | TRIGGERED |
| **L1 First-framing + L25 Existing-output anchor** (replaces L9-from-Grace per v3 Hardness Plan) | Carlos's quoted "I told her 211 was back in motion" — Carlos's own confident wrong premise the agent inherits; PersonaBrief over-promise pattern validates | TRIGGERED via prompt body alone (no S2 plant contradiction risk) |
| **L8 Multi-link chain** | mortgage_los (loans + conditions + document_checklist_items + lenders + staff + borrowers) + slack + crm + email + contacts = 5 service families; rate-lock add forces lender service inclusion | TRIGGERED + STRENGTHENED by rate-lock breadth |
| **L25 Existing-output anchor** (separate layer) | Carlos's self-stated belief + "the notes on those have been going stale" surfacing the 6 existing CRM engagement notes | TRIGGERED |

**Lens 3 R3 verdict:** 5/5 levers triggered. L9-replacement (L1+L25) cleanly carries the original yield. Hardness Plan v3 amendment correctly reflects this.

---

## [LENS 4 — STRICT DENSITY] R3

| Component | Strict range | Strict midpoint |
|---|---|---:|
| Slack (channel list + trio search C002 + D_grace_yamamoto read + thread replies on 211 chatter) | 5-8 | 6.5 |
| `mortgage_los_get_loan` (3 trio loans) | 3-4 | 3.5 |
| `mortgage_los_list_conditions` (3 list-per-loan + "every one of them in detail" forces dives on 00009's 3 outstanding) | 3-5 | 4.0 |
| `mortgage_los` document_checklist_items (3 list-per-loan + dives on required-status items) | 4-6 | 5.0 |
| `mortgage_los` staff (Brian Mitchell + Todd Jennings — both terminated; L6 trap surface) | 2 | 2.0 |
| `mortgage_los` borrowers (3 explicit) | 3 | 3.0 |
| **`mortgage_los` lenders — NEW R3** (3 distinct lender_ids on trio; rate-lock context requires lender lookup per loan) | 3-5 | 4.0 |
| CRM deals (trio search returns zero, terminates fast) | 1-3 | 2.0 |
| CRM engagements (list per loan; 6 trio-related rows for "going stale" check) | 3-5 | 4.0 |
| Email (trio-thread reads + 7-day reply check returns null, terminates fast) | 6-10 | 8.0 |
| Contacts (Grace lookup + 3 borrower lookups → 1 hit + 2 misses) | 2-4 | 3.0 |
| Writes (1 email + 1 slack + 3 CRM engagements + 1 add_condition) | 6 | 6.0 |
| Cross-service triangulation buffer | 1-2 | 1.5 |
| **TOTAL projected (strict)** | **42-63** | **52.5** |

**Density verdict: PASS at design target (midpoint 52.5 ≥ 50).** R3 rate-lock + lender add lifts midpoint from R2's 48.5 to 52.5 (+4.0). Range floor 42 above 40 INSUFFICIENT bar.

---

## [LENS 5 — ADVERSARIAL REVIEW] R3

| Issue | Severity | R3 state |
|---|---|---|
| CRM engagement orphan-vs-bound write artifact | MEDIUM (carry-over) | Operator deferral to S3; not prompt-fix. 5/5 prompt-side achievable but declined. |
| "For weeks" present-perfect on Grace pushing | LOW-MEDIUM (carry-over) | Operator deferral to S2 plant. 5/5 prompt-side achievable but declined. |
| "Where each of the rate locks sits" | NEW R3 — verified | No new ambiguity. Field exists, populated, all three expired. Forces lender lookups cleanly. |
| Hardness_Plan L9→L1+L25 | LOW (R2 doc residue) | RESOLVED — v3 plan amended. |

**Lens 5 R3 verdict:** 2 carry-over operator-deferrals; 0 new issues. No write-flipping second-readings remain. No BLOCKER-grade adversarial findings.

---

## [LENS 6 — LIFECYCLE + NARRATIVE STATE] R3

| State-implying claim | R3 grounding |
|---|---|
| "Grace pinged me on Slack [no time]" | S2-plant-flex (acceptable cross-phase contract) |
| "She has been pushing on for weeks" | Loose temporal; operator-deferred to S2 plant + historical Grace pipeline-review activity context |
| "I told her 211 was back in motion" (Carlos self-attribution) | Universe-consistent with PersonaBrief over-promise pattern |
| "I have been buried this month" | Narrative, soft; consistent with Carlos's last trio LOS touch being March 2026 |
| "Have not opened the file-level data in weeks" | Same — narrative, soft, consistent |
| "I cannot remember the expirations" | Universe-consistent — all 3 rate locks expired 47-64 days ago; persona is over-extended |
| "Conditions sitting outstanding that should have been cleared weeks ago" | Universe-grounded — LN-2026-00009 conditions ~105 days overdue |
| "Channel has been wrong before" | Implied narrative, no specific factual claim |
| "Sofia in the hall" | Informal narrative, no claim |

**Lens 6 R3 verdict:** All state-implying claims either universe-grounded, consistent with persona, or single-S2-plant-flex. **No hard contradiction with universe state.** Major improvement R2→R3.

---

## [LENS 7 — ANTI-RATIONALIZATION] R3

Direct flags only. The two remaining 4/5 sub-dims (UGT, Date-alignment) are **operator-deferred to downstream phases**, NOT auditor-silenced concerns. Both have prompt-side 5/5 paths that the operator explicitly declined. No "considered but decided fine" framing — these are flagged as not-strictest-PASS even though they meet pipeline policy.

The "for weeks" residue is NOT a state-claim about a specific universe atom (which would be Truthfulness-flagged); it is a temporal-anchor looseness that compresses the date-alignment headroom under STRICTEST.

---

## [LENS 8 — V3 REGRESSION-ANCHOR] R3

| Check | Result |
|---|---|
| Mid-thought opener | ✓ "Grace pinged me on Slack about the pipeline review…" |
| Three-movement structure (trigger / context / asks) | ✓ |
| Single coherent situation | ✓ pipeline-review packet to Grace |
| No em-dash / en-dash | ✓ re-verified |
| No tool name | ✓ re-verified across rate-lock sentence |
| No internal ID | ✓ |
| Word count ≤ 500 | ✓ 397 |
| No "at least N" | ✓ |
| Carlos voice consistent with V3 Task11..14 LO pattern | ✓ |

**Lens 8 R3 verdict: PASS.**

---

## [LENS 9 — UNIQUE GROUND TRUTH MIDDLE-BAND] R3

| Write target | Primary reading | Alt readings | Flips? |
|---|---|---|---|
| Email to Grace | grace.yamamoto@keystonemortgage.com | — | NO |
| Slack post → C002 | C002 unique by name match | — | NO |
| CRM engagement × 3 | orphan-mimic existing pattern | (a) Darren-bound + 2 orphan; (b) create 2 new contacts + bind all 3 | **SOFT — operator deferred to S3 count-based scoring** |
| Condition follow-up on longest-overdue file | LN-2026-00009 (only trio member with outstanding conditions; verb + noun both anchor to `conditions`) | NONE (doc-checklist alt-path killed by "condition" noun) | **NO** (R2 SOFT flip resolved by R3 single-word fix) |
| Rate-lock state per loan (read-only) | rate_lock_expiration per loan | — | NO |

**Lens 9 R3 verdict:** 1 SOFT engagement-binding flip (operator-deferred-to-S3). 0 HARD flips. 0 longest-overdue parallel scope (R2 residue resolved).

---

## Final Verdict

### Lens summary (R3)

| Lens | Verdict |
|---|---|
| 1 Strict QC | 10/12 at 5; 2/12 at 4 (UGT, Date-alignment) — operator-deferrals, not universe-unachievable |
| 2 Answer leakage | PASS (no BLOCKER leak) |
| 3 Hardness end-to-end | PASS (5/5 levers triggered) |
| 4 Density | PASS at 50+ design target (52.5 midpoint) |
| 5 Adversarial | PASS (no new findings; 2 carry-over operator-deferrals) |
| 6 Lifecycle + narrative state | PASS (no hard contradictions) |
| 7 Anti-rationalization | Two 4/5 residues flagged directly |
| 8 V3 regression-anchor | PASS |
| 9 UGT middle-band | 1 SOFT operator-deferred flip; 0 HARD |

### Strictest-reading vs operator-deferral framing

R3 made the major lifts that R2 demanded: hard "last night" contradiction killed, longest-overdue parallel scope killed, density lifted from 48.5 THIN to 52.5 PASS, Hardness Plan v3 amended to match prompt carrier, 0 hard universe contradictions.

The two remaining 4/5 sub-dims (UGT engagement binding; Date-alignment "for weeks") are **operator-documented cross-phase contracts** — both have prompt-side 5/5 paths that were explicitly declined in favor of downstream-phase handling (S3 rubric count-scoring for the binding; S2 plant for the temporal anchor). Per the audit instruction's exact language, "operator giving up" excludes these from the strictest 5/5 PASS justification — the bar is "mathematically unachievable under per-task universe constraints", which neither residue meets.

However, both deferrals are **legitimate pipeline patterns documented in AGENTS.md** (Council A A8 + A3 cross-phase contracts) and the operator has documented rationale for each in the R3 fix narrative. The residues are not BLOCKER-grade, not structural defects, and do not compromise lever yield or density.

### Verdict resolution

Under STRICTEST audit reading the verdict must be REVISE (iteration cap hit). The R3 deliverable substantively meets pipeline policy and is downstream-shippable, but does not clear the "every applicable sub-dim 5/5 OR mathematically-unachievable-justified" bar.

Operator action required: **escalate to user**. Two paths available:
1. **Operator applies the two single-phrase prompt-side fixes** (CRM pattern-mimic instruction; temporal softening on "for weeks") → would clear UGT + Date-alignment to 5/5 → 12/12 strict PASS achievable in one more iteration if user authorizes a Round 4 exception.
2. **User accepts the documented operator-deferrals as cross-phase contracts** → proceed to S2 with the residues documented in `_aux/Council_Reports/AUDIT_prompt_round3.md` and flagged for S2 plant satisfaction + S3 rubric scoring. This is a policy-compliant ship path.

Recommendation: path 1 (two single-phrase fixes; ~5 minutes operator effort) clears strict PASS; path 2 ships now with documented residues. Either is defensible. Default to path 1 only if user wants strict 5/5; default to path 2 if user wants to move to S2 now.

Not REBUILD: 5/5 levers triggered, 0 hard contradictions, density PASS, voice PASS, no structural defect.

---

VERDICT: REVISE
