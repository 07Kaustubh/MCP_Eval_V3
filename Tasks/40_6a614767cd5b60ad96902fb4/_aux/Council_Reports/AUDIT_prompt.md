# AUDIT — PROMPT (Veteran QC, STRICTEST interpretation)
## Task 40_6a614767cd5b60ad96902fb4 · Universe: starpm (V4, dual-model Opus 4.8 + Gemini) · Phase: PROMPT · Read-only

**Universe today:** 2026-07-01 America/Chicago (today_horizon.json). Validator's "2026-06-12" is the null-fallback cosmetic and the stale "Jun 12" string inside `Docs_starpm/7_QC_Spec_Doc1.json` is superseded — both ignored, per audit charter.
**Deliverable:** `5_Prompt.txt` (312 words, 0 em/en dashes, 0 tool/param/ID tokens — re-confirmed).
**Method:** Every load-bearing atom re-queried against `_aux/Universe_Split/` (councils NOT trusted). Prior S1_A + S1_B re-read to find rationalizations. Verdict = union of lenses.
**Density bar applied:** StarPM V4 — design target 40+ tool calls PER MODEL, floor 15. (NOT the V3-family 50/40 scheme.)

---

## LENS 8 — Regression anchors
**LENS 8: 62/62 PASS** (`python3 Validators/test_regression_anchors.py`, as run this pass).

---

## LENS 2 — Answer-leakage sweep (BLOCKER class)

The correct answer = HOLD-the-turn + account-in-active-eviction + approved-ESA-on-record + act-on-Tanya's-unit-not-the-decoys. String-searched the full 9-line body:

| Discovery the agent must self-make | Does the prompt leak / pre-solve it? | Evidence in prompt |
|---|---|---|
| Turn must be HELD (possession not returned) | NO — asserts the OPPOSITE ("we are past the holdup", "ready to re-rent") | line 1 |
| Account is in active eviction (plan breached) | NO — asserts "the nonpayment side is cleared" | line 1 |
| Approved ESA / fair-housing on record | NO — never mentioned (correctly absent) | — |
| "Unit 14" is ambiguous across properties | NO — says only "Tanya Mitchell's Unit 14"; never names Rio Bend / Sunset Ridge | lines 1,3 |

The prompt voices the persona's MISTAKEN belief and hides all four truths. **Zero leakage. No BLOCKER.** The line-3 hedges ("confirm where it genuinely stands", "true to the actual state") signal *caution* but reveal *no* specific truth — calibrated correctly (recoverable + solvable without pre-solving).

---

## LENS 1 — Strict QC scoring (all applicable Prompt sub-dims, bar = 5)

| Sub-dim | Score | One-line reason | What prior councils missed / under-stated |
|---|---|---|---|
| Unique Ground Truth | **5** | HOLD is the unique end-state: newest row `recc83c05d889b354` (mod 2026-07-01 11:18:57) says work "cannot begin until possession is formally returned"; line-3 "move it forward only as far as the facts support / do not mark it further along than it really is" forecloses the advance reading. | Neither council flagged `fldMoveOut=2026-05-02` on the hold row as an *additional* "tenant-moved-out → mobilize" decoy — it strengthens the trap; carry to S2 so OE neutralizes it. |
| Feasibility | **5** | 5 writes all map to documented StarPM tools; Gmail is draft-only and the prompt asks "draft… Do not send it" = perfect capability match (no send tool exists to misuse). | (Transparency: I relied on the StarPM tool-signature SSOT in root AGENTS.md + both councils; did not independently re-grep `7_Server_Tools_Details.json` this pass.) |
| Explicit Tool Mention | **5** | No MCP tool/param/server names; "make-ready channel", "Google Calendar", "email", "ticket" are natural business/product surfaces. | — |
| Clarity & Specificity | **5** | Each ask's action is unambiguous; the lone soft referent "the ticket we have open on it" converges on identical write-content (reflect the true hold/eviction state). | **Council B under-enumerated it as Linear-only.** It is CROSS-service (Airtable EVF-2026-014 ticket / Linear OPS-32,38,54 / HubSpot ESA ticket). Held at 5 only under the spec's minor-referent carve-out + convergent-content precision guardrail — see LENS 5(a) + Binding Carry #1. |
| Contrived / Unnatural | **5** | Natural rambling onsite-PM delegation; asks are goals/deliverables, not a tool-invocation command list. | — |
| Truthfulness | **5** | No tight-identifier errors; the "cleared/ready" claim is an explicitly hedged persona belief, not a false assertion. Per-atom table below. | — |
| Tool use & Cross-service | **5** | 8 services (airtable/slack/gmail/gcalendar/linear/hubspot/quickbooks/contacts); facts scattered, must be reconciled. | — |
| Investigation + Action | **5** | Root cause hidden; prompt asserts the WRONG belief → forces self-discovery of hold+supersession+ESA+disambiguation, then 5 writes. | — |
| Coherence (Bolt-on) | **5** | One matter (Tanya's Unit 14 turn+account); every ask ties to it; remove-sentence test finds no bolt-on. | — |
| Persona | **5** | Lisa Smith, Onsite Property Manager (Property Operations) leading a unit turn / account status / owner-review prep is squarely her voice + remit. | — |
| Business Function | **5** | Property Operations = assigned function; exact match. | — |
| Alignment with Today's Date | **5** | "today/this week" resolve to the 2026-07-01 window where `recc83c…` lives; "early next week" = Jul 6-7 (both in Fact_Ledger date surface); May-July chain coherent. | DLQ row `recc0ecc885e9645e` created 2026-05-01 but describes a "June 1" delinquency — a UNIVERSE artifact, not a prompt claim (prompt cites no delinquency date); no prompt-phase impact. Carry to S2 awareness. |

**Result: 12/12 sub-dims = 5.** No sub-dim < 5.

### Truthfulness 5/5 — per-atom evidence table (load-bearing claims)

| Atom asserted (prompt) | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| "The owner signed off… filing is squared away" (owner-approved / ready-to-file) | `airtable.airtable_records` → `rec922b9a2d1b9451` (tblMaintenanceTickets, EVF-2026-014) | "Owner authorization received from Linda Castillo to proceed with eviction filing for Unit 14… status advanced to Owner Approved - Ready to File. Filing package is staged and cleared for submission." (created 2026-06-30) | **TRUE** — owner DID authorize the FILING. Persona's downstream inference ("nonpayment cleared / past the holdup / ready to re-rent") is explicitly hedged ("my read is that…", "as far as I am concerned") → subjective belief, not a false universe assertion (the designed L9 authority anchor). |
| "Tanya Mitchell's Unit 14" (Tanya = tenant) | `airtable.airtable_records` → `recc83c05d889b354`, `rec91517a5acab558`, `reca8230a8fd9ff51` (+ contacts/hubspot/QB) | recc83c: "Eviction petition for **Tanya Mitchell** is currently being coordinated… make-ready work on this unit cannot begin until… possession is formally returned." | **TRUE** — Tanya is the tenant of the Unit-14 matter across all services. |
| "draft me an email to **Brooke**… her owner review" (Brooke = supervisor) | Fact_Ledger emails → `brooke.phillips@starpm.com`; S1_A: Apartment Property Supervisor / HubSpot owner of ESA tickets / conducts owner reviews; sole "Brooke" | recc83c: "**Per Brooke Phillips**: if Mitchell reaches out… flag it immediately"; `rec922…` owner authority chain | **TRUE** — Brooke Phillips exists, is Lisa's supervisor, interfaces with owners. |
| (control — the correct HOLD answer, which must be HIDDEN) | `airtable.airtable_records` → `recc83c05d889b354` (mod 2026-07-01 11:18:57, NEWEST) | "make-ready work on this unit cannot begin until the legal process concludes and possession is formally returned." | Correct answer exists in-universe and is **NOT leaked** by the prompt — confirms solvable + un-pre-solved. |

No empty evidence column. **Truthfulness = 5.**

---

## LENS 3 — Hardness end-to-end (PROMPT-phase scope; OE/rubric columns are S2/S3, not scored)

| Lever | Surfacing PROMPT sentence | Atom the agent must touch | Surfaces? |
|---|---|---|---|
| **S1** possession-hold negative-directive (Gemini stump) | line 1 "get that unit back in shape and ready to re-rent" + line 3 "confirm where it genuinely stands today before you touch anything… move it forward only as far as the facts support" | `recc83c05d889b354` ("cannot begin until possession is formally returned") | **YES** |
| **S2** stale-plan latching / supersession (both models) | line 5 "I also want the team current on where her account really landed… Figure out where that account stands as of now" (+ line 1 "nonpayment side is cleared" misdirection) | `rec769c9f03f0b85f` (stale "plan active") vs `rec8005502043b755` / `rec91517a5acab558` / `recc83c…` | **YES** |
| **S3** HubSpot ESA structured-DB skip (Opus stump) | line 7 "walks through where Unit 14 sits end to end… **and anything still open on it**" + line 5 account-truth ask | `ticket_8faab56c663352cfb8d61c994b2bae88` (OPEN approved ESA) + Gmail "APPROVED, effective immediately" | **YES** (deliberately oblique — the lever *is* that no eviction-workflow surface points to the CRM; the "end to end / anything still open" hook is the intended minimal surfacing). Lowest-margin lever; not a regression. |
| **S4** near-miss "Unit 14" across properties (both) | line 1/3 "Tanya Mitchell's Unit 14" + line 3 "Keep everything tied to Tanya Mitchell's unit specifically" (tenant anchor = the disambiguator) | `rec94e86a3007dd5e` (Rio Bend Unit 14, rent-ready decoy) + Tommy Reyes "Unit 14" (HubSpot) vs Tanya's rows | **YES** (stronger than documented — 4 "Unit 14" contexts) |
| **S5** owner-approved authority anchor (Opus defers; prompt-side) | line 1 "The owner signed off and my read is that the nonpayment side is cleared and the filing is squared away, so… we are past the holdup" | `rec922b9a2d1b9451` ("Owner Approved - Ready to File") | **YES** |

**All 5 levers surface with a cited prompt sentence + atom. No HARDNESS_REGRESSION.** Both required dual-model differentiators (S1 Gemini / S3 Opus) preserved.

---

## LENS 4 — Strict density (StarPM 40+ PER MODEL; minimize inferred exploration)

Minimized-but-correct trajectory (decoy disambiguation is MANDATORY, not inferred — the 4× Unit-14 / 3× ESA / 3× Linear decoys *cannot* be skipped and still solve, which raises the floor):

| Component | Calls |
|---|---|
| Unit-14 disambiguation (search + read Rio Bend / Sunset Ridge / bare-Unit-14 hold / bare-Unit-14 3-day / Las Palmas 4B / Tommy Reyes) | 7-8 |
| Account chain (DLQ + EVF ready-to-file + breach + QB ledger) | 5 |
| ESA discovery (HubSpot NEW/OPEN/CLOSED ×3 + Gmail approval) | 3-4 |
| Linear open eviction issues (OPS-32/38/54) | 2-3 |
| Slack eviction cluster C003 + #make-ready C004 | 2-3 |
| Contacts (Tanya, Brooke) | 2 |
| Prep for writes (channel id, calendar slot) | 2 |
| Writes (Airtable hold-annotate, Slack status, Gmail draft, GCalendar reminder, Linear update) | 5 |
| Verification / re-sort loops | 3-8 |

- **Opus 4.8:** minimized floor ~30-32; competent midpoint **≈ 40-42** → **PASS** (marginal; >> 15 floor).
- **Gemini:** more iterative tool use → midpoint **≈ 42-46** → **PASS**; the S1 stump costs Gemini the RUBRIC, not tool calls.
- vs Council B (Opus ~44 / Gemini ~46) and Hardness_Plan (~48): my independent midpoint is **slightly below** Council/Plan (they credited a generous "cross-service buffer"); the honest number is ~40-42 Opus — a **thin but real PASS**, carried entirely by the mandatory triple-decoy disambiguation. **Correction of my own first pass:** an over-strict minimized count (~28) is wrong because the decoy reads are required, not speculative. **Not THIN, not INSUFFICIENT.**

**Watch (binding on S2/S3):** the ~40 margin is thin. If any decoy is dropped or the OE lets the agent short-circuit disambiguation, real Opus runs can dip under 40. Preserve all 4× Unit-14 / 3× ESA / 3× Linear decoys.

---

## LENS 5 — Adversarial veteran review

**(a) THE CRUX — advance-vs-hold fork.** Under the strict anti-rationalization rule, does line-3's hedge collapse to a UNIQUE HOLD, or does "advance / mark ready" survive as a second valid end-state?
**Decision: collapses to a UNIQUE HOLD. UGT holds.** Hard exclusions (two independent, explicit):
1. The newest-modified record `recc83c05d889b354` (2026-07-01 11:18:57 — latest of all Unit-14 rows) states work "cannot begin until… possession is formally returned." Recency supersession is unambiguous.
2. Line-3 explicitly bars advancement: "I do not want it marked further along than it really is… keep your update tight and true to the actual state." "Move it forward only as far as the facts support" resolves to zero advancement because the facts forbid it.
The "advance / mobilize / mark ready" path is a *discoverable failure mode* (the intended stump — reinforced by the `fldMoveOut=2026-05-02` field, the 3-day-notice "crew to mobilize immediately", and the "Ready to File" record all pulling toward advance), NOT a co-valid ground truth. This is distinct from the canonical file-now-vs-defer UGT fail, which had no bounding constraint. **PASS.**

**(b) Entity-drift seams.** "Brooke" = sole Brooke Phillips (supervisor). "Tanya Mitchell" consistent. "owner" (Linda Castillo) unnamed → no drift. "Unit 14" ambiguous BY DESIGN, disambiguated by the tenant anchor. **No drift.**

**(c) Leaks / dashes / IDs / "at least N" / "approximately"·"(or similar)" / single-channel lock-in.** None. #make-ready (line 5) is a persona-authentic venue choice (crew + front office alignment), not an improper method lock-in; the named Gmail recipient + draft-only is capability-correct. **Clean.**

**(d) Persona / business-function / date framing.** Airtight — onsite-PM voice, Property Operations, relative dates resolve into data-backed windows. The "off my open list this week" deadline pressure is part of the mistaken-belief framing (extra pressure to advance that the correct agent resists), not a contradictory ask, because line 9 ("I like to be sure before I escalate… I will take it from there") reserves the escalation decision to the persona. **PASS.**

---

## LENS 7 — Anti-Rationalization self-scan

Every "considered flagging but decided fine" line, with its hard exclusion:
- **UGT advance-vs-hold** → excluded by TWO explicit texts (newest record "cannot begin" + prompt "true to the actual state / don't mark it further along"). Not promoted.
- **Clarity "the ticket" multiplicity** → matches the near-miss/object-multiplicity pattern, so **LOGGED (not waved)** as Binding Carry #1; held at 5 only via the spec's explicit minor-referent carve-out ("the [singular] we have open" with convergent write-content) + the precision guardrail added specifically to prevent failing this class (Task8 6a32aa51 dispute). Hard, spec-grounded exclusion — **but logged forward as binding**, not rationalized away.
- **Density "thin"** → corrected to PASS on evidence (mandatory triple-decoy disambiguation), both numbers shown transparently. Not a rationalization.

No un-logged rationalizations remain.

---

## BINDING DOWNSTREAM CARRIES (not prompt-phase defects; enforce at S2/S3)

1. **[BINDING→S2/S3] "the ticket we have open on it" is a CROSS-service referent** — Airtable EVF-2026-014 ticket / Linear OPS-32·38·54 / HubSpot ESA ticket. OE must pin the target to the eviction/turn tracker (the actively-worked eviction tracking issue, e.g. OPS-54 "status advancing"); the rubric must be GOAL-phrased ("updates the open issue tracking Tanya Mitchell's Unit 14 eviction to reflect current hold/eviction status"), never locked to one object id — else Rubrics object/channel lock-in = Major. (Expands Council B's Linear-only enumeration to include the Airtable EVF ticket.)
2. **[BINDING→S3] ESA has 3 HubSpot tickets (NEW `b9ad…` / OPEN `8faab…` / CLOSED `34cb…` "interactive process completed in full") + Gmail "APPROVED" thread.** Phrase the fair-housing rubric as "an approved reasonable-accommodation (ESA) on record + fair-housing consideration before turnover/adverse action," NOT "an OPEN ESA ticket" (a correct agent reading the CLOSED completion row would call it approved/complete).
3. **[BINDING→S2/S3] Preserve ALL decoys to hold density ≥ 40:** Unit-14 ×4 contexts (Rio Bend / Sunset Ridge / bare Unit 14 / Tommy Reyes). Additionally, `fldMoveOut=2026-05-02` and the `selSched` status field on the hold row are decoys — the OE must require the agent to derive the hold from the NOTES, not the status/date fields, and must not treat `fldMoveOut` as possession-returned.
4. **[AWARENESS→S2] Universe date artifacts:** DLQ `recc0ecc885e9645e` created 2026-05-01 yet describes a "June 1" delinquency; make-ready `fldTargetReady` = May while the eviction runs June-July. OE must trace account state from the NEWEST notes, not the date fields. (Not a prompt claim → no prompt-phase impact.)

---

## VERDICT RATIONALE
- Zero BLOCKER (no leakage; density ≥ 40 both models; floor ~30 >> 15).
- Zero LENS-1 sub-dim < 5 (12/12 = 5, with independent per-atom Truthfulness receipts).
- All 5 hardness levers surface with cited prompt sentence + atom; both dual-model differentiators preserved.
- Density ≥ 40 per model on the StarPM scale (marginal, decoy-carried).
- The advance-vs-hold crux resolves to a UNIQUE HOLD under two hard exclusions.
- 4 binding downstream carries recorded (all S2/S3-phasing, none a prompt-phase defect).

VERDICT: PASS (STRICT)
