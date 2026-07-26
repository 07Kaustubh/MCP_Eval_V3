# AUDIT — S3 RUBRICS (RE-AUDIT after REVISE) — Task 41_6a61a86a3453b3714bdc72ef

**Universe:** StarPM v4 (dual-model Opus 4.8 + Gemini) · **Persona:** Patricia Nguyen (Onsite PM) · **Mode:** READ-ONLY, STRICTEST interpretation.
**Prior audit:** REVISE with ONE finding — non-atomic bundling of "owner-approved" (EVF-2026-014/Gmail) + "petition-not-filed/JP coordination" (Airtable SoR/Slack) on array #8, #10, #15.
**Operator fix applied:** make-ready-note narrowed to possession-hold only; eviction-ticket note SPLIT (petition-not-filed + owner-approved); owner-email eviction-status SPLIT (petition-not-filed + owner-approved). Set is now **18 rubrics** (was 16).

**VERDICT: PASS (STRICT).** Zero BLOCKER · zero sub-dim < 5 · atomicity finding RESOLVED · all 5 levers trace end-to-end · density PASS (both models). No fix-in-place items; no rebuild.

---

## Rubric inventory (18, 0-based array idx → my label)
R0 net ~$1,832 (2.1) · R1 charges ~$1,982 walk-back (2.1) · R2 petition-not-filed/JP (2.1) · R3 owner-auth-on-file Linda Castillo (2.1) · R4 unit must hold (2.1) · R5 update Sunset Ridge U14 record (1.1) · R6 update keeps turn held/not-advanced (1.2) · **R7 update states possession-hold reason — NARROWED (1.2)** · R8 note on eviction ticket (1.1) · **R9 note: petition-not-filed — NEW SPLIT-a (1.2)** · **R10 note: owner-approved — NEW SPLIT-b (1.2)** · R11 post to #make-ready (1.1) · R12 channel msg no-mobilize/no-market (1.2) · R13 draft to Linda Castillo (1.1) · R14 draft ~$1,832 net (1.2) · **R15 draft: petition-not-filed — NEW SPLIT-a (1.2)** · **R16 draft: owner-approved — NEW SPLIT-b (1.2)** · R17 draft: unit cannot be touched/marketed (1.2).
**Counts: 18 Outcome / 0 Process.**

---

## LENS 1 — Strict QC scoring of the 5 Rubric sub-dimensions

### Atomicity finding — RESOLVED (independently re-verified)
The prior REVISE targeted the "owner-approved AND petition-not-filed" bundle (two independently-verifiable, differently-sourced facts). Every surface that carried the bundle is now split:
- **Final response** — already split (R2 not-filed / R3 owner-auth).
- **Eviction ticket note** — now R9 (not-filed) + R10 (owner-approved).
- **Owner email** — now R15 (not-filed) + R16 (owner-approved).
- **Make-ready note (R7)** — narrowed to the possession-hold reason ONLY; the eviction-status clause was removed.

Each of R7/R9/R10/R15/R16 tests exactly one claim that can pass/fail independently. **No "owner-approved + not-filed" bundle survives anywhere in the 18-set.**

Directly consistent with `Tasks/_meta/Learnings.md` #5/#7/#8: this exact split (owner-approved ⟂ JP-coordination) + demotion of the "(EVF-2026-014)" parenthetical from a graded token to optional grounding was platform-re-verified on BOTH models (Opus 8a and Gemini 8b: each split half 6/6 consistent, pass@1 unchanged at 0%). I confirmed the id-demotion is honored: in R3/R10/R16 the string EVF-2026-014 appears only as "traceable to…"/justification context and **never inside a gradable FAIL clause** — so it is not graded as a token.

### Per-atom evidence table — newly-split / narrowed rubrics
| Rubric | Single graded claim | Source (independently verified) | Atomic |
|---|---|---|---|
| **R7** (make-ready note, narrowed) | make-ready cannot begin until possession is formally returned | Airtable `recc83c05d889b354` fldNotes2: "make-ready work on this unit cannot begin until the legal process concludes and possession is formally returned" | ✅ one fact |
| **R9** (eviction note, split-a) | petition not yet filed / JP coordination | `recc83c05d889b354` fldNotes2 (JP coordination) + Slack C003 "JP coordination is underway … before the petition goes in" | ✅ one fact |
| **R10** (eviction note, split-b) | filing owner-approved / authorization on file | Airtable `rec922b9a2d1b9451` (EVF-2026-014): "authorization received from Linda Castillo … Owner Approved - Ready to File" + Slack C003 "she's authorized the filing. I updated the Airtable record to Owner Approved" + Gmail thread `621640f9e7aa6d46` (subject "Eviction Filing Authorization. Tanya Mitchell. Unit 14", Linda reply) | ✅ one fact |
| **R15** (owner draft, split-a) | petition not yet filed / JP coordination | same as R9 | ✅ one fact |
| **R16** (owner draft, split-b) | filing owner-approved / authorization on file | same as R10 | ✅ one fact |

Intra-artifact independence holds: on the eviction note an agent can state not-filed and omit owner-approved (R9 pass / R10 fail) or vice-versa; identical for the owner email (R15 vs R16). Removing either changes scoring ⇒ neither is redundant.

### Sub-dimension scores
| Sub-dimension | Score | Basis |
|---|---|---|
| **Overall Rubric Quality** | **5** | 0 Major / 0 Moderate / 0 Minor. All 18 atomic; all values self-contained and verified (see LENS 2/grounding); no channel/structured-value lock-in (R5 accepts either record id; R8 accepts OPS-32 OR EVF-2026-014; R11 accepts channel name OR C004); "approximately" used only on the derived $ figures. |
| **All-Failing Rubrics** | **5** | Rubric-phase audit — no completed agent runs to fail. Projected AF set (the L31 explicit-prohibition rubrics R4/R6/R7/R12/R17) are valid, grounded, in-scope real behaviors → an intended asymmetric Gemini gap, not invalid AF. <2 invalid AF predicted. |
| **Rubric Category Balance** | **5** | 18 Outcome > 0 Process. Binary PASS. |
| **Process Rubrics** | **5** | Zero Process rubrics ⇒ zero invalid Process rubrics. |
| **Agent-Centric Phrasing** | **5** | All 18 criteria open with "The Agent"/"The Agent's"; zero tool names in any criterion (deliverables named as make-ready record / eviction ticket / #make-ready / owner draft / final response). |

**Overall Rubric Quality is 5 (zero Major AND zero Moderate). No sub-dim < 5.**

---

## LENS 2 — Answer-leakage sweep ($1,832 / $1,982 and neighbors) — **PASS, no BLOCKER**
Swept prompt + every readable universe source (`_aux/Universe_Split/*` gmail/slack/airtable/quickbooks, `Universe_complete_data.json`) and `Fact_Ledger.json`.
- Exact amount forms `1,832` / `1832.00` / `$1832` — **0 hits.** Exact forms `1,982` / `1982.00` / `$1982` — **0 hits.**
- Raw substring "1832" hits are timestamp/hash tokens only (`1781018320000`, `55e8d318324f56f6`); "1982" hits are ID/timestamp fragments (`311198205235`, `…02.051982`). None is a dollar amount.
- Fact_Ledger `amounts[]` contains neither 1832.00 nor 1982.00 (confirms both are correctly DERIVED-only). Stored decoy `2132.00` IS present verbatim (as intended — it is the double-counted stored Balance the FAIL clauses reference).
Derived figures on R0/R1/R14 never appear verbatim in any agent-readable surface → no answer-leakage on a derived figure. **No BLOCKER.**

---

## LENS 3 — Hardness end-to-end trace (L2/L10/L1/L11/L31) — all 5 trace; split reinforces L1/L10
| Lever | Prompt sentence | OE | Rubric | Fact_Ledger / record atom |
|---|---|---|---|---|
| **L2** structured-DB skip | "walk it back to the underlying charges … clean number" | OE 4/5 (vendor-linked AP bill QR-2026-0441, no CustomerRef) | R0/R1 | bill `232176553533` lines 847/925/210/(−150), Balance 2132 |
| **L10** reversal/supersession | "last I tracked … about at the hearing stage" | OE 9/12 (JP coordination supersedes active-plan / awaiting-sign-off) | R2/R4 (**+R9/R15**) | `recc83c05d889b354` fldNotes2 |
| **L1** latching | "confirm we have the owner's authorization on file" | OE 10/11/13 (EVF-2026-014 Linda Castillo vs Linear OPS-32 "Harris Property hearing") | R3 (**+R10/R16**) | `rec922b9a2d1b9451`, contacts Linda vs Harry/John |
| **L11** net-vs-gross/sign | "not double-counting any credit or adjustment" | OE 5 ($150 credit stored as positive → 2132 vs 1832) | R0 | bill line4 150.00 credit |
| **L31** negative-directive | "I don't want the crew mobilizing … or us marketing something we can't deliver" | OE 14/16/17 (explicit prohibitions) | R4/R6/R7/R12/R17 | possession-hold note |

No lever orphaned by the split. The split **reinforces L1** (owner=Linda now graded on note R10 + email R16, rejecting the Harris latch) **and L10** (not-filed now graded on note R9 + email R15). ✅

---

## LENS 4 — Density projection (StarPM v4 per-model ≥40) — **PASS**
Rubric count does not change trajectory density — the split grades additional *facets* of writes the agent already performs (no new tool calls). Hardness Plan projection stands: **Opus ~50 midpoint / Gemini ~43 midpoint, both ≥40.** Breadth 8 distinct services, 7 at ≥5% of a ~50-call trajectory. Both models clear the v4 PASS band. (Operator-run trajectory tool-call counts on the split re-verify were 47/45/37/38/33/40 per Learnings #8 — unchanged from pre-split, corroborating density is undisturbed.)

---

## LENS 5 — Adversarial veteran review
- **Atomicity (all 18):** each tests one claim. R1 bundles $1,982 + three components — acceptable (same tool output; prompt demands "walk it back"). R4/R12/R17 bundle make-ready+market — acceptable: one hold disposition from one fact; they would fail on the *same single error* ("unit clear to release"), so splitting them would MANUFACTURE redundancy. The owner-approved/not-filed pair fails on *different* errors, so it correctly IS split. Asymmetry is coherent, not arbitrary.
- **New overlap/redundancy from the split:** none. owner-approved and petition-not-filed each live on 3 artifacts (final response / eviction note / owner email) = per-deliverable coverage across distinct write actions (blessed, not redundant). Intra-artifact pairs pass/fail independently on different errors.
- **Beyond-prompt (owner-approved note/email):** grounded in OE 15 ("owner-approved by Linda Castillo (EVF-2026-014)") and OE 17 ("owner's authorization is on file"), and prompt-grounded ("confirm we have the owner's authorization on file"; email covers "the eviction status"). Not beyond-prompt.
- **Coverage gap from narrowing R7:** none. Make-ready-record deliverable still covered by R5 (write) + R6 (status held) + R7 (possession-hold reason); eviction-status facts covered on R9/R10, R15/R16, R2/R3. OE-to-rubric xref closes.
- **Entity drift:** Linda Castillo (Property Owner, linda.castillo@gmail.com) correctly distinguished from decoys John Castillo (Water Delivery Rep) and Harry Harris ("Harris Property"); Sunset Ridge Unit 14 vs Rio Bend Unit 14 (`rec94e86a3007dd5e`, selReady). All decoys sit in FAIL clauses. Verified against contacts + airtable.
- **Channel lock-in:** none — R11 accepts #make-ready OR C004; R8 accepts OPS-32 OR EVF-2026-014; R5 accepts either valid record id. Deliverables are all prompt-named ("our channel", "the eviction ticket", "make-ready record", "email to the owner").
- **Tool-name / em-dash / at-least-N / "(or similar)" misuse / silent process rubrics:** none found.

---

## LENS 7 — Anti-rationalization sweep
No "considered flagging but decided fine" defect-waving in the file or councils. The dispositions that keep R4/R12/R17 bundled correctly apply the spec's acceptable-bundling rule (same-source, single-error facts) — splitting them would create redundancy the spec explicitly warns against — so there is nothing to promote to REVISE. Verified independently, not accepted on trust.

---

## LENS 8 — Regression anchors
**62/62 PASS** (operator-run; recorded, not re-run in this read-only audit). Validator re-run recorded PASS 0 fails / 18 warns (decoy-in-evidence FAIL clauses per Task3 precedent; derived $1,832/$1,982 not in ledger; X2 observation-period notes) — all warns are expected/adjudicated, none escalate.

---

## FINAL DISPOSITION
**PASS (STRICT).**
- Sub-dims: Overall Rubric Quality **5** · All-Failing **5** · Category Balance **5** · Process **5** · Agent-Centric **5**.
- Prior atomicity finding: **RESOLVED** — bundle split on all three surfaces; R7 narrowed; EVF-id demoted to non-graded grounding (matches the both-model-validated Learnings #7/#8 remedy).
- Leakage: **none** ($1,832/$1,982 absent verbatim everywhere; no derived-figure leak).
- Levers: **L2/L10/L1/L11/L31 all trace end-to-end**; split reinforces L1/L10; no orphan.
- Density: **PASS** (Opus ~50 / Gemini ~43, both ≥40; 8 services / 7 ≥5%).
- Remaining findings: **none.** No fix-in-place; no rebuild.
