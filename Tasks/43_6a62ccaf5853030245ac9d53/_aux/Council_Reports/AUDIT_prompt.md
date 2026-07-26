# AUDIT — Veteran QC Re-Verification (STRICT) — Prompt Phase

**Task:** `Tasks/43_6a62ccaf5853030245ac9d53`
**Deliverable:** `5_Prompt.txt` · **Universe:** starpm · **Framework:** StarPM V4 (dual-model)
**Today:** 2026-07-01 (America/Chicago) — the "Jun 12 US/Eastern" string in `7_QC_Spec_Doc1.json` is SUPERSEDED.
**Iteration:** 1 · **Date:** 2026-07-25 · **Prior councils:** A=GO, B=GO (re-read; NOT trusted — every claim re-verified against `_aux/Universe_Split/*.json`).

**VERDICT: PASS (STRICT)**

Zero BLOCKER hits · zero Lens-1 sub-dims < 5 · 4/4 levers surfaced · neither model INSUFFICIENT (Opus PASS, Gemini THIN-accepted).

---

## Deterministic floors (re-run this pass)

| Floor | Result |
|---|---|
| `validate.py --phase prompt` | **PASS** — 0 fails, 1 WARN (bolt-on heuristic), 4 notes. Re-run confirmed. |
| `test_regression_anchors.py` | **62/62 PASS** (Lens 8). Re-run confirmed. |
| `verify_universe_atoms.py` | PASS (0 atoms — prompt carries no tight identifiers by design; vacuous pass, grounding done manually below). |
| `calc_similarity.py` | max composite 27.4 (< 40) — clear. |

---

## LENS 1 — Strict QC sub-dimension scoring (per `7_QC_Spec_Doc1.json`)

Scale: strictest interpretation, 5 is the only pass. All applicable Prompt + Universe sub-dims scored.

| Sub-dim | Score | One-line reason | What prior council missed |
|---|:--:|---|---|
| Unique Ground Truth | **5** | Single end-state: correct existing AR 2026-534 to $1,812 (387+1340+85), update 4C selReady make-ready Notes (cost + closed), draft email Linda, Slack post. Every alternative ($1,622 / $1,727 / $1,897 / new invoice / Pete) is a trapped model error, not a valid reading. | Nothing material. Confirmed the two-4C-row split does NOT create a second valid end-state — selReady is corroborated-current; selProg is a trapped stale latch. |
| Feasibility | **5** | All 4 writes tool-supported. Airtable `tblMakeReady` has NO cost field and NO "Closed" status (only Scheduled/In Progress/Ready), but `fldNotes2` (multilineText) absorbs both "final owner cost" + "fully closed" — fully actionable, no conflict. | Neither council examined the Airtable schema. Verified: the missing cost/closed fields do NOT break feasibility (Notes field carries it). Watch-item for OE only. |
| Explicit Tool Mention | **5** | "get our 4C make-ready record in Airtable updated" = locative system-of-record reference. NON-FAIL band triggers only on "use the Airtable **tool**" / "Airtable **MCP server**" — prompt does neither. Format Card whitelists product names ("Slack"). | Confirmed against exact NON-FAIL band text; "in Airtable" is not in that band. |
| Prompt Clarity & Specificity | **5** | Asks are explicit and ordered by intent; "Correct the invoice she is holding… I do not want a second bill created" fixes create-vs-correct; recipient (Linda) and act-now are pinned. | The two residual openings (which channel / which 4C row) do NOT diverge write actions — hard exclusion cited (Lens 5). |
| Contrived / Unnatural | **5** | Natural first-person Carlos voice; mid-thought entry; no command list, no arbitrary format/timestamp constraint; difficulty is organic reconciliation. | — |
| Truthfulness | **5** | Every concrete claim grounded (per-atom table below); prompt states ZERO dollar figures → no numeric error possible. | — |
| Tool Use & Cross-service | **5** | Requires QuickBooks (AP+AR) + Airtable (4C row) + Gmail (belief email + draft) + Slack + Contacts; answer scattered, must be reconciled. | — |
| Investigation + Action | **5** | Deep derive-$1,812-from-AP-bills investigation feeds 4 writes; not pre-solved (no figure/root-cause disclosed). | — |
| Coherence / Bolt-on | **5** | Validator WARN is a heuristic FALSE POSITIVE — flagged sentence FAILS the remove-test (orphans downstream "where it landed" / "corrected number") → load-bearing → not a bolt-on. | Re-ran remove-test independently; confirmed. |
| Persona | **5** | Carlos Mendez, Onsite PM, leads the Mesa Vista 4C make-ready (signature scenario); voice matches. | — |
| Business Function | **5** | Property Operations, Cat 1.1 Unit Turnover Coordination — squarely the assigned flagship function; no ambiguity with another function. | — |
| Alignment with Today's Date | **5** | Today 2026-07-01; "back in the spring" → May 2026 (AR TxnDate 2026-05-01), belief email 2026-06-02, all past; close-out now is coherent; no future-facing ask. | Two-row date inconsistency (move-out 06-01 vs 06-15) is the intended latch with a corroborated correct answer, not a today-misalignment. |
| Universe: Data Exists | **5** | All bills/invoice/records/email/channels/contact verified present & tool-retrievable (see evidence table). | — |
| Universe: Cross-service Coherence | **5** | Closet "Internal labor (Tony)" note is out-corroborated by external Permian VendorRef + "Owner Reserve (Trust)" acct + "Pass-through to owner" + already-on-AR + prompt's "outside vendor work belongs on her side" rule → include-closet is the supported truth. QC carve-out ("sufficient supporting evidence") applies. | Confirmed the misaligned-data carve-out applies; NOT a [Fail-Misaligned Data]. S2/S3 must ground the rationale (watch-item). |

**Lens-1 result: 14/14 sub-dims = 5. No REVISE.**

---

## LENS 1 — Per-atom evidence table (Truthfulness 5/5 proof)

Every excerpt pulled directly from `_aux/Universe_Split/*.json` (row_data parsed).

| Atom asserted in prompt | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| Persona Carlos Mendez | gmail 5101c5a41dffa90a; qb 991582431419 PrivateNote | `from_address: carlos.mendez@starpm.com`; "Internal labor charge for **Carlos Mendez's** make-ready walk" | GROUNDED |
| "Mesa Vista 4C" unit | airtable tblMakeReady; qb 445653930748 | recc8534b3fd13954 `fldUnit: "Mesa Vista 4C"`; AR lines "Mesa Vista Unit 4C" | GROUNDED |
| "Linda Castillo owns that unit" | contacts; qb 445653930748 CustomerRef | contacts `linda.castillo@gmail.com`, "Property Owner"; AR `CustomerRef.name: "Linda Castillo"` (value `proj-4ae920b7c9e8`) | GROUNDED — Linda IS CustomerRef on 2026-534 |
| "back in the spring I billed her" | qb 445653930748 | `DocNumber: 2026-534`, `TxnDate: 2026-05-01`, `TotalAmt: 1622`, `Balance: 1622` | GROUNDED |
| "sent her a summary calling it done" | gmail 5101c5a41dffa90a | from Carlos → to linda.castillo@gmail.com, subj "Mesa Vista 4C Make-Ready Complete. Cost Summary for Your Records", body "…is **fully wrapped up**", 2026-06-02 | GROUNDED |
| "post-move-out deep clean" | qb 195089456477 | Sunshine Cleaning, `TotalAmt: 387`, Doc 2026-SC-4C, "Post-move-out deep clean … Mesa Vista Unit 4C" | GROUNDED (matches AR line 1 $387) |
| "full interior repaint" | qb 696089964235 | Permian Make-Ready Crew, `TotalAmt: 1340`, Doc PD-2026-09, "Interior repaint, full unit - Mesa Vista Apartments Unit 4C" | GROUNDED (AR line 2 = $1,140 → understated $200) |
| "closet trim touch-up" | qb 546359391323 | Permian, `TotalAmt: 85`, Doc 2026-519, acct "Owner Reserve (Trust)", "Pass-through to owner" | GROUNDED (AR line 3 = $95 → overstated $10) |
| "internal walk / condition check handled in house" (exclude) | qb 991582431419 | Alamo HVAC, `TotalAmt: 85`, "Unit condition inspection and punch list … Mesa Vista Unit 4C", "Internal labor charge for Carlos Mendez's make-ready walk"; NOT on AR | GROUNDED (Alamo = the excludable internal walk) |
| "our 4C make-ready record in Airtable" | airtable tblMakeReady | recc8534b3fd13954 (selReady, "Unit confirmed ready") + recbd087a4abd605b (selProg, "still tracking") | GROUNDED (dual-row latch present) |
| "our channel for the crew and front office" | slack_channels | #make-ready (C004), #vendors (C005), #owner-relations (C006), #general (C003) | GROUNDED (channels exist) |
| "costs are a straight pass-through to Linda" | qb AR PrivateNote / AP PrivateNotes | AR: "Owner cost pass-through invoice…"; AP: "Pass-through to owner" | GROUNDED |
| Pete Donovan owner decoy AVOIDED | qb customer proj-f6f9edfeae5c | "Pete Donovan" is a QB customer + painter; AR customer is Linda, not Pete; prompt never names Pete | DECOY CORRECTLY AVOIDED |

No empty evidence cell → Truthfulness stands at 5.

---

## LENS 2 — Answer-leakage sweep

Derived answer **$1,812**; neighbors $1,897 / $1,727 / $1,622 / $1,340 / $1,140 / $95 / $85 / $387 / $200 / $10.

| Check | Result |
|---|---|
| Any `$` sign in prompt | **NONE** |
| Any dollar figure (1812/1727/1897/1622/1340/1140/95/85/387/200, comma or plain) | **ZERO hits** |
| Any digit at all | Only "**4C**" (unit designator) — no numeric quantity anywhere |
| Internal IDs (2026-534, PD-2026-09, 2026-519, 2026-481-566, 2026-SC-4C, rec…, proj-…) | **NONE** |
| Em-dash (U+2014) / En-dash (U+2013) | **NONE / NONE** |
| "at least N" / artificial precision | **NONE** |
| Pete Donovan (entity-drift decoy) | **NOT mentioned** (correct) |

**LENS 2 result: CLEAN. Zero leakage. No BLOCKER.**

---

## LENS 3 — Hardness lever → prompt-sentence map (prompt-phase scope)

| Lever | Surfacing prompt sentence | Fact_Ledger atom(s) the agent must touch | Status |
|---|---|---|---|
| **L2 Structured-DB skip (flagship)** | "every dollar on her bill has to line up with what we actually paid out on that unit, to the dollar, no more and no less. Go back to what each vendor charged us for the 4C work and set it against the line items I sent her." | AP bills 696089964235 ($1,340), 546359391323 ($85), 195089456477 ($387) — actuals live ONLY in AP, not AR/email | **SURFACED** |
| **L10 Reversal / supersession** | "Before I log 4C as truly closed I want to be sure what she was actually charged holds up, because that summary is the record she keeps" + "so she is not sitting on a summary that no longer matches." | AR 445653930748 ($1,622 stale) superseded by AP bills | **SURFACED** |
| **L6 Near-miss entity** | "Go back to what each vendor charged us for the 4C work and set it against the line items I sent her." + "Linda Castillo owns that unit." | 10-bill $1,340 cluster (only 696089964235 is 4C); $1,140-vs-$1,340; $95-vs-$85; twin $85 (546359391323 vs 991582431419); Linda-vs-Pete owner | **SURFACED** |
| **L11 Net-vs-gross** | "Only outside vendor work belongs on her side. Anything that was our own time on the unit, an internal walk or a condition check we handled in house, stays off her bill entirely." | 991582431419 (Alamo, exclude → $1,897 decoy); 546359391323 (closet, include; drop → $1,727 decoy) | **SURFACED** |

**Levers surfaced: 4/4. No HARDNESS_REGRESSION.** L2 preservation confirmed per empirical note — the trap survives even though the prompt says "what each vendor charged us"; it does not name QuickBooks, and a sibling StarPM task naming QuickBooks still stumped 0/12. OE-step and rubric-criterion legs are **S2/S3 = PENDING** (not regressions).

---

## LENS 4 — Strict per-model density (StarPM per-model gate)

Trajectory sketched under the reading that MINIMIZES inferred exploration.

| Segment | Calls |
|---|---|
| Contacts: resolve Linda's email | 1–2 |
| Airtable: find + disambiguate 2× 4C make-ready rows + ticket | 3–4 |
| QuickBooks: find/read AR 2026-534 | 2–3 |
| QuickBooks: search AP bills + read deep-clean/repaint/closet/Alamo + disambiguate 10-bill $1,340 cluster | 8–12 |
| Gmail: read belief email | 1–2 |
| Slack: context read | 1–2 |
| Writes (4): correct AR (+read-back) · update Airtable 4C Notes · draft email Linda · Slack post | 4–6 |
| Post-write verification | 2–4 |

| Model | Range | Midpoint | Band |
|---|---|:--:|---|
| **Opus 4.8** | ~34–50 | **~43** | **PASS (≥ 40)** |
| **Gemini** (empirical −9.5) | ~26–41 | **~34** | **THIN (15–39, documented-accept)** |

Matches Hardness_Plan (Opus 43.5 / Gemini ~34). **Density is REAL, not inflated:** 4 genuine writes (QB AR correction, Airtable 4C Notes, Gmail draft, Slack post) across 5 services exercised (QuickBooks, Airtable, Gmail, Slack, Contacts; Linear optional 6th); the 10-bill $1,340 cluster forces genuine disambiguation reads on both models. **Neither model INSUFFICIENT (<15).** Gemini THIN is a pre-accepted operator decision (Hardness_Plan `## THIN density acceptance`). **Does NOT block.**

---

## LENS 5 — Adversarial veteran review

- **(a) Implicit framing / fix-and-execute intent:** PASS. Prompt uses implicit L15/L16 framing — Carlos believes the ~$1,622 bill is right and asks to "square it away." No "flag the discrepancy" rubric-mismatch. Consistent with fix-and-execute.
- **(b) Entity-drift seam (Linda vs Pete):** PASS. Prompt anchors **Linda Castillo** (para 1) and keeps her throughout ("email Linda", "her bill", "her account"); Pete Donovan (QB customer `proj-f6f9edfeae5c` / painter) is NEVER named — the decoy is left in the data for the agent to trip on, not leaked into the prompt.
- **(c) Leak scan:** no tool-function names, no MCP-server phrasing, no em-dash, no "at least N", no internal IDs, no artificial precision, no contrived format. Only "Airtable" as a natural product reference (adjudicated 5).
- **(d) Single-channel lock-in:** N/A — prompt names a goal ("drop a line in our channel for the crew and front office"), not a locked channel; method-agnostic, correct.
- **(e) Write-Action Divergence + Delegation Clarity HARD GATES:** PASS. Create-vs-correct pinned ("I do not want a second bill created… Correct the invoice she is holding"); recipient pinned (Linda); act-now pinned ("I would sooner square this myself now"); assistant does the work (no ambiguous "I'll" self-action hand-off).

**Council-A "MINOR" ambiguities re-adjudicated under STRICT (do they flip a write action?):**
1. **"our channel"** — Candidate channels (#make-ready / #vendors / #owner-relations / #general) all deliver ONE coordination post to the SAME audience ("crew and front office"). **Write action, audience, and content are identical across readings.** QC Clarity HARD GATE explicitly excludes "channel-to-the-same-recipient differences that converge on the same action." → **Does NOT flip a write action. Non-blocking.** (OE must pin the exact channel — S2/S3, PENDING.)
2. **"our 4C make-ready record"** (two rows) — recc8534b3fd13954 (selReady/"confirmed ready", newer) is corroborated-current by belief email + market-ready ticket + Slack; recbd087a4abd605b (selProg/"still tracking", older) is the stale snapshot. Updating the stale row is a **trapped model error (intended L1 latch)**, not a defensible second reading; the end-state converges (4C make-ready reflects $1,812 + closed). QC coherence carve-out ("sufficient supporting evidence") applies. → **Does NOT flip the intended write action. Non-blocking.** (OE must pin recc8534b3fd13954 / grade on content — S2/S3, PENDING.)

---

## LENS 7 — Anti-Rationalization self-scan

Each "I considered flagging X but decided it's fine" promoted UNLESS it cites a hard exclusion:

| Considered flag | Hard exclusion cited | Promote to REVISE? |
|---|---|---|
| "our channel" not named | QC Clarity HARD GATE: channel-to-same-recipient convergence is explicitly NOT a fail; audience fixed | **No** |
| "our 4C make-ready record" (2 rows) | QC coherence carve-out (corroborated truth) + intended L1 latch → stale-row update is a trapped error, not a valid reading | **No** |
| "Airtable" named | QC Explicit-Tool NON-FAIL band triggers only on "use the X tool"/"MCP server"; Format Card whitelists product names | **No** |
| No cost field / no "Closed" status in Airtable | `fldNotes2` multilineText absorbs cost + closure; fully actionable, no conflict | **No** |
| Closet "Internal labor (Tony)" vs external vendor | QC misaligned-data carve-out: 4 corroborating cues + prompt's "outside vendor work" rule establish include-closet as supported truth | **No** |

All five cite genuine hard exclusions grounded in QC-spec text (not "probably meant"). None promote. **Every watch-item is an S2/S3 (OE/rubric) grounding requirement, PENDING and out of prompt-phase scope.**

---

## LENS 8 — Regression anchors

`test_regression_anchors.py` → **62 passed, 0 failed out of 62.** Recorded.

---

## Bolt-on WARN adjudication (validator heuristic)

Flagged sentence: "Correct the invoice she is holding so it carries the right figure, and get our 4C make-ready record in Airtable updated so it shows the final owner cost and the unit fully closed."
- **Remove-sentence test:** deleting it orphans the downstream asks — "email Linda… where **it** landed" and "so whoever else touches her account is working off **the corrected number**" lose their antecedent, and the entire corrective action vanishes. Rest does NOT make sense → **FAILS remove-test → load-bearing → NOT a bolt-on.**
- **Heuristic error:** the validator claims the sentence "shares no named entities"; in fact it shares the invoice, Linda ("she"), 4C, the make-ready record, and the owner cost via pronoun/description references the heuristic cannot resolve. **Confirmed false positive. Coherence = 5.**

---

## Final verdict

**VERDICT: PASS (STRICT)**

Zero BLOCKER hits · zero Lens-1 sub-dims < 5 (14/14 = 5) · 4/4 levers surfaced with cited prompt sentences · Opus density PASS (~43), Gemini THIN (~34, documented-accept), neither INSUFFICIENT · answer-leakage CLEAN · bolt-on WARN is a confirmed heuristic false positive · regression anchors 62/62.

**Carry-forward watch-items for S2/S3 (NOT prompt-phase defects):**
1. OE must pin the exact Slack channel for the coordination post.
2. OE must pin the exact 4C make-ready row (recc8534b3fd13954) or grade on content, not row-id.
3. OE must specify the Airtable write mechanism (final owner cost + "fully closed" recorded in `fldNotes2`, since no cost field / "Closed" status exists).
4. Rubric must ground the include-closet / exclude-Alamo rationale (external Permian pass-through on-AR w/ Owner-Reserve acct vs internal make-ready walk) so the $1,727 path grades as a genuine model failure, not a rubric artifact.

```json
{"phase":"audit_prompt","council":"AUDIT","task_dir":"Tasks/43_6a62ccaf5853030245ac9d53","verdict":"PASS_STRICT","scores":{"unique_ground_truth":5,"feasibility":5,"explicit_tool_mention":5,"clarity_specificity":5,"contrived_unnatural":5,"truthfulness":5,"tool_use_cross_service":5,"investigation_action":5,"coherence_bolton":5,"persona":5,"business_function":5,"alignment_today":5,"universe_data_exists":5,"universe_cross_service_coherence":5},"density_projection":{"midpoint":43,"band":"PASS","gemini_midpoint":34,"gemini_band":"THIN"},"levers":{"expected":4,"surfaced":4,"missing":[]},"leakage_hits":0,"regression_anchors":"62/62","iteration":1,"timestamp":"2026-07-25"}
```
