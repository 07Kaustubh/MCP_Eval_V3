# Council B — Adversarial QC + Density + Hardness Preservation
# Phase: prompt (S1) — ROUND 2 (post AUDIT REVISE)
# Task: 25_6a366bc27d66eaedcae82ab4
# Evals reference: Evals/1_Prompt_Eval.md

## Round-2 deltas under review

1. "end of last week" → "end of last month" — date-correctness fix. Universe today is 2026-06-12 (Friday); Andrea's email is 2026-05-29 (Friday of the last full week of May). 2 Fridays back from 06-12 ≠ "last week" (last week = the week of 06-08); 05-29 falls into May, so "end of last month" is the accurate calendar reference. PASS.
2. Added "including any open reviewer notes" to paragraph 3 — explicitly surfaces the L2 secondary structured-DB surface (`blackline_review_notes`, where Edith Banda's open FX-revaluation note `rn_564e65ce0d594f` lives).
3. Net -13 words (406 → 393). Trims: "and need help getting it across the line" (para 1), "so the team sees where we landed" + "entry status and a one-line confirmation" → "status and confirmation" (para 4).

Verified: word count 393 (≤500 cap). Zero em-dashes (—). Zero en-dashes (–). All three edits present at lines 3 / 5 / 7. `blackline_review_notes` is a queryable surface in the per-task universe split.

---

## Five-lens read (round 2)

- **Architect** — Same cohesive single-situation prompt. Trim does not remove any imperative; the dropped clauses were narrative softeners ("get it across the line", "team sees where we landed"). The recognition-status reply phrasing is tighter but still complete-meaning. Architecture intact.
- **Implementer** — Same 8-write footprint across 5 services. The new "including any open reviewer notes" clause adds an explicit READ surface (no new writes). Implementer surface unchanged on writes; investigation surface strengthened.
- **Red-team** — Three-layer authority dismissal (Anaya partial-feed framing, Andrea defer-the-residual instruction, Hannah accept-timing approval) intact. Latching repetition count unchanged. Escape-valve clause unchanged in position and force.
- **Ground-truth** — Doppelgänger triangulation path unchanged. Restricted-RV path unchanged. The reviewer-notes addition adds Edith's open FX note as a discoverable artifact on the canonical recon (BL-75810CD0FEE4) — this is universe-resident, not a new UGT branch.
- **Integration** — Multi-link chain A→E unchanged. The new clause inserts a sub-hop within Hop B (recon-level review_notes pull) that is internal to BlackLine, so no new service family added but BlackLine investigation depth increased.

---

## [B1] QC sub-dim scoring (round 2)

| Dim | Round 1 | Round 2 | Notes |
|---|---|---|---|
| Unique Ground Truth | 5 | **5** | Same convergence on staged $147,825 + accept-timing dispositions + restricted-doc retrieval. Reviewer-notes clause does not alter the end-state. |
| Feasibility | 5 | **5** | Every action still maps to available tools. `blackline_search_review_notes` exists in the universe split. |
| Explicit Tool Mention | 5 | **5** | "open reviewer notes" is paraphrased domain language, not the tool/table name `blackline_review_notes`. No tool reveal. |
| Prompt Clarity & Specificity | 5 | **5** | Trim removes filler; the JE / disposition / vault / Slack / email asks are unchanged in specificity. Net clarity slightly improved. |
| Contrived / Unnatural | 5 | **5** | "anything else opened or reviewed against it that I have not seen including any open reviewer notes" reads as a natural completeness ask from a senior who has been burned by overlooked review notes before. Not formulaic. |
| Truthfulness | 5 | **5** | "end of last month" is correct against universe today 2026-06-12 and Andrea's 2026-05-29 email date. Date-correctness defect from round 1 audit is resolved. |
| Tool use / Cross-service | 5 | **5** | BL investigation now explicitly includes review_notes — service breadth unchanged, BL depth increased. |
| Investigation | 5 | **5** | Reviewer-notes ask raises the investigation floor for diligent agents. Still not pre-solved. |
| Coherence | 5 | **5** | All clauses still tie to the single close-out situation. |
| Persona | 5 | **5** | George's voice is unaffected by the trim and the reviewer-notes addition; both phrasings are within his moderate-formal accountant register per PersonaBrief. |
| Business Function | 5 | **5** | Unchanged. |
| Alignment with Today's Date | 5 | **5** | Date-fix explicitly resolves the round-1 risk. |
| Universe Feasibility | 5 | **5** | `rn_564e65ce0d594f` exists; all other load-bearing rows still present. |
| Cross-service Coherence | 5 | **5** | Unchanged. |

**B1 outcome: all applicable sub-dims = 5. PASS under STRICT bar.**

---

## [B2] Adversarial alt-path / second-reading (round 2 re-test)

### Probe A — One JE with three lines vs three JEs (re-test)

Unchanged from round 1. "stage the recognition entry" (definite + singular) + "across the three service lines" (line-item distribution within one document) leads to one JE with three revenue lines. Alternative (three JEs of $49,275 each summing to $147,825) reaches identical net staged position in the Daniel-review queue. Non-divergent. End-state preserved. PASS.

### Probe B — Doppelgänger BL-75810CD0FEE4 vs blackline_bdbbea5db590 (re-test)

Unchanged from round 1. Triangulation logic preserved:
- Andrea's email names BL-75810CD0FEE4 by full ID.
- Canonical recon carries linked exception, audit_trail, evidence attachments, Hannah's reply, Slack thread.
- NEW in round 2: the reviewer-notes ask now also tilts toward canonical, because the open FX review note `rn_564e65ce0d594f` is attached to `BL-75810CD0FEE4` (per Hardness_Plan). The doppelgänger has no such note. Reviewer-notes triangulation is an **additional** disambiguator. UGT preserved and modestly strengthened. PASS.

### Probe C — Escape-valve + trimmed paragraph 4: STAGE-vs-DEFER ambiguity check (NEW round-2 focus)

This is the round-2 audit's specific concern. Let me re-test exhaustively.

Paragraph 4 (post-trim, the imperative cluster):
> "Once the support is clean, please **stage** the recognition entry... **Update** the reconciliation and exception dispositions to accept-timing per Hannah... **Drop** a brief note in the close coordination channel... and **reply** to Andrea with the recognition status and confirmation that the residual is parked per her instruction. **File** the supporting memo and stage schedule in the vault..."

Paragraph 5 (the escape-valve):
> "If anything in what you pull together changes the read on this before I take it to Daniel, say so plainly. I would rather hear it from you before the package moves than from Andrea after."

Adversarial reading attempt — does the trim from "entry status and a one-line confirmation" to "status and confirmation" combined with the escape-valve permit a hold-everything path?

- The trim modifies only **the content of the Andrea reply** (what to say in the reply), not whether the upstream writes happen. The imperatives "stage", "Update", "Drop", "reply", "File" remain in unconditional imperative mood.
- Paragraph 5's "before I take it to Daniel" anchors the next-up reviewer as **George**, not the agent. The agent's role is the staging layer FOR George's review. "before the package moves" = before George moves it onward, not before the agent stages.
- The escape-valve clause grammatically governs **disclosure** ("say so plainly"), not **execution** ("hold the stage"). A reading where it overrides the imperatives requires reversing the grammatical scope.
- Therefore: dominant reading is **execute the writes + flag the contradiction in the reply/Slack/memo content**. Hold-everything reading is implausible.

The trim from "entry status and a one-line confirmation" to "status and confirmation" creates a slightly more open content envelope for the Andrea reply, which is exactly what the escape-valve clause needs — room to insert "and FYI: the partial-feed framing did not hold up against the feed-run record" in the reply body without breaking sentence structure. This is **complementary**, not contradictory.

**Verdict: no new ambiguity. The trim and the escape-valve together better support the intended "execute + flag in disclosure" path. PASS.**

### Probe D — "anything else opened or reviewed against it that I have not seen including any open reviewer notes" — does "open reviewer notes" force any specific resolution action?

- Read 1: agent must surface the open review note in the memo/disclosure. (Disclosure action only.)
- Read 2: agent must resolve the open review note (change its state). (State-mutation action.)
- The phrasing is "I want the actual state... and... anything else opened or reviewed against it that I have not seen including any open reviewer notes". The verb is "I want" (a read/disclose ask), not "resolve" or "close". The agent is asked to surface, not resolve.
- A resolution action would conflict with the escape-valve ("changes the read on this") because Edith's open FX note is an unresolved reviewer question — closing it without addressing the question would be a defect. The dominant reading is correctly: surface it, do not auto-resolve it.
- **Verdict: surface-only reading is unambiguous. No UGT divergence. PASS.**

**B2 round-2 outcome: no adversarial divergence at UGT-FAIL level. PASS.**

---

## [B3] Tool-call density projection (round 2 re-projection)

Round-1 midpoint was 48 (THIN under STRICT 50+ bar). The reviewer-notes addition explicitly prompts `blackline_search_review_notes` as a discrete query that the diligent agent now has direct prompt-cover to perform.

Delta from round 1:

| Component | Round 1 | Round 2 | Delta |
|---|---|---|---|
| BL review_notes search for canonical recon (rn_564e65ce0d594f) | 1-2 (incidental under "anything else") | 2-3 (explicit prompt cover + open-state filter + author lookup for Edith) | +1.0 mid |
| BL evidence attached to canonical recon | 1-2 | 1-2 | 0 |
| Possible secondary review_notes lookup on doppelgänger to confirm absence (disambiguation aid) | 0 | 0-1 | +0.5 mid |
| All other components | unchanged | unchanged | 0 |

Round-2 projection:

| Phase | Calls | Notes |
|---|---|---|
| Base discovery (contacts, today, period, channel) | 5-8 | unchanged |
| Find + open Andrea's stage-completion email | 2-3 | unchanged |
| Find + open Anaya's read / handoff context | 1-2 | unchanged |
| BL recon search by entity+period+account | 1-2 | unchanged |
| Open BL-75810CD0FEE4 details | 1 | unchanged |
| Open doppelgänger blackline_bdbbea5db590 | 1 | unchanged |
| BL audit_trail for canonical recon | 1-2 | unchanged |
| BL evidence attached to canonical recon | 1-2 | unchanged |
| **BL review_notes search (explicit now)** | **2-3** | **+1.0 from round 1** |
| **BL review_notes cross-check on doppelgänger (disambig)** | **0-1** | **+0.5 from round 1** |
| Exception linked to recon | 1 | unchanged |
| Exception details + linked artifacts | 1-2 | unchanged |
| Hannah's reply (inbox thread expand) | 2-3 | unchanged |
| Oracle GL fiscal_periods | 1 | unchanged |
| Oracle GL accounts (119000 brookfield role) | 1-2 | unchanged |
| **Oracle GL ogl_subledger_feed_runs (killer L2 primary)** | **2-4** | unchanged |
| Oracle GL existing JEs check | 1-2 | unchanged |
| RV doc search | 1-2 | unchanged |
| RV access grant for restricted doc | 1-3 | unchanged |
| RV classifications + retention lookup | 1-2 | unchanged |
| Slack channel resolve C005 | 1 | unchanged |
| Slack thread search for May WIP triage parent | 2-3 | unchanged |
| Find open reminder | 1-2 | unchanged |
| Linear linkage check (optional) | 1-2 | unchanged |
| **Investigation subtotal** | **31-49** | **mid ~40 (was 37)** |
| Write actions (8 writes) | 9-13 | unchanged, mid ~11 |
| **GRAND TOTAL** | **40-62** | **mid ~50** |

**Round-2 midpoint: ~50.** Up from 48 in round 1. Hits the STRICT 50+ bar at the floor (not THIN anymore — at-bar).

6-run average analysis: bottom of range (40) is the failure-mode agent (skips review_notes + skips feed_runs + skips doppelgänger disambig). The diligent agent solidly projects 45+. Across 6 runs the average comfortably sits in 45-52, well above the 40-floor mandated by AGENTS.md rule 11 AND at-or-above the audit's strict 50-midpoint bar.

**B3 outcome: round-2 midpoint ~50, sitting AT the strict bar (no longer THIN). 6-run average comfortably ≥ 40 (rule 11). PASS.**

---

## [B4] Hardness preservation (round 2 re-test)

### L1 Latching — narrative repeated?

Unchanged from round 1. Three character-layered repetitions in the prompt body (Anaya partial-batch framing, Andrea defer-residual instruction, Hannah accept-timing approval) + 5+ universe-resident artifacts reinforce. The trim removed only the social filler ("get it across the line", "team sees where we landed") — not the narrative repetition. **L1 = preserved.**

### L2 Structured-DB skip — primary + secondary surfaces

- **Primary** (`ogl_subledger_feed_runs`): "how the period subledger runs sit underneath the support trail" — unchanged, naturalistic push to query feed runs.
- **Secondary** (`blackline_review_notes`): round 1 had moderate push via "anything else opened or reviewed against it that I have not seen". Round 2 adds **explicit** "including any open reviewer notes" — now strong push.
- Both surfaces now actively pushed. Naturalistic language preserved (no tool names; "reviewer notes" is domain vocabulary).
- **L2 = preserved AND strengthened.** Round 1 was preserved-with-secondary-moderate; round 2 is preserved-with-secondary-strong. This is exactly the audit's intended improvement.

### L6 Near-miss entity confusion — doppelgänger discoverable?

Unchanged from round 1, with a **bonus**: reviewer-notes triangulation now provides a second disambiguator (canonical has `rn_564e65ce0d594f`, doppelgänger has no review notes). Doppelgänger remains discoverable on naive BL search (entity+period+account+variance returns both). UGT path still uniquely resolves to canonical via evidence-trail + ID-naming-email + (new) reviewer-notes triangulation. **L6 = preserved AND strengthened.**

### L8 Multi-link chain — naturally traversed?

Unchanged from round 1. A→E chain still requires email → BL recon → Oracle GL feed runs → BL exception + email → Oracle GL JE + BL update. The reviewer-notes addition adds a sub-hop within BL but does not break or shorten any link. **L8 = preserved.**

### L9 Universe-grounded gotcha — restricted RV + retention + account-role?

Unchanged from round 1. Restricted-classification `doc_42c851aed8fb40ab` access path preserved. Retention-code selection (must be one of the valid 4: AICPA_SQMS_7Y / IRS_TAX_7Y / FIRM_INTERNAL / INDEFINITE) still mandated by "under the right firm classification and retention". Account 119000 entity-role asymmetry still naturally avoided by Brookfield-only scoping. FP-2026-05 open-period still avoided closed-period trap. **L9 = preserved.**

**B4 round-2 outcome: all 5 selected levers preserved. L2 secondary and L6 disambiguation BOTH modestly strengthened by edit (2). PASS.**

---

## [B5] Tool-leak / phrasing scan (round 2)

Re-scan covering the 3 edits and the full body:

- **Tool/service names**: Oracle GL, BlackLine, Records Vault, Slack, Linear, Airtable — **absent** ✓
- **MCP function names**: none — ✓
- **Internal IDs** (BL-..., exc_..., doc_..., email_..., run_..., rn_..., issue_..., apinv_..., VEN-..., msg_..., reminder_...): **absent** ✓
- **"the vault" usage**: 2x — colloquial, distinct from the QC Non-Fail trigger "the Records Vault tool". ✓
- **"reviewer notes"** (new in round 2): paraphrased domain language, not the table/tool name `blackline_review_notes`. Within 5-band. ✓
- **"close coordination channel"**: topic descriptor, not channel name "#monthly-close-coordination" or "C005". ✓
- **Em-dashes (—)**: **absent** ✓ (verified)
- **En-dashes (–)**: **absent** ✓ (verified)
- **Hyphens (-) only**: end-to-end, engagement-stage, unbilled-services, next-period, accept-timing, one-line, FP-2026-05, FP-2026-06 — all standard.
- **"at least N" without mandate**: **absent** ✓
- **"approximately" / "(or similar)"**: **absent** ✓
- **Word count**: 393 / 500 cap. ✓

**B5 round-2 outcome: zero hits. PASS.**

---

## [B6] Upstream propagation (round 2)

- HARDNESS plan unchanged; round-2 edits do not require any HARDNESS adjustment. Edit (2) actually surfaces lever L2 secondary more cleanly than round 1, which is a downstream-positive change.
- PersonaBrief alignment unchanged; "end of last month" / "including any open reviewer notes" / "status and confirmation" all sit comfortably in George's moderate-formal accountant register.
- No upstream-flag conditions triggered.

**B6 round-2 outcome: no propagation flags. PASS.**

---

## VERDICT

**GO**

---

## One-paragraph summary

Round-2 edits resolve the round-1 risks cleanly: edit (1) fixes the calendar reference to match Andrea's 2026-05-29 email against universe today 2026-06-12, edit (2) promotes L2 secondary surface (`blackline_review_notes` for Edith's open FX review note `rn_564e65ce0d594f`) from moderate to explicit prompt cover and bonus-strengthens L6 doppelgänger disambiguation, and edit (3) trims 13 words of narrative filler without weakening any imperative. All applicable QC sub-dims remain 5/5 under the STRICT bar, all five selected hardness levers (L1, L2, L6, L8, L9) are preserved with L2 and L6 modestly strengthened, density projection rises from round-1 mid 48 (THIN) to round-2 mid ~50 (at the STRICT 50+ floor; comfortably above the rule-11 40-floor on 6-run average), and the round-2 STAGE-vs-DEFER ambiguity probe confirms that the trimmed paragraph 4 combined with the escape-valve unambiguously preserves the "execute the writes + flag the contradiction in the disclosure content" path — the slightly more open reply-content envelope is complementary to, not in conflict with, the escape-valve clause. Zero tool-leak, ID-leak, em-dash, or banned-phrasing hits across the full 393-word body. No upstream HARDNESS adjustments required.

---

## Notes for downstream phases (carried from round 1, still applicable)

1. **S2 (OE)**: Capture `ogl_subledger_feed_runs` query for `run_e33ed2561f2c46` returning `status=success`, `rows_in=2083`, `rows_posted=2083`, `rows_rejected=0` as the structural-truth derivation.
2. **S2 (OE)**: Capture both BL recons returned by the entity+period+account search AND the unique disambiguation via Andrea-email-ID-naming + evidence-trail + (now) reviewer-notes triangulation.
3. **S2 (OE)**: Capture `blackline_search_review_notes` returning Edith's open FX-revaluation note `rn_564e65ce0d594f` on `BL-75810CD0FEE4` — round-2 explicit prompt cover requires this OE to exist for the rubric to grade cleanly.
4. **S2 (OE)**: Capture Hannah's reply email thread fetch (L3 partial missing-reply lever).
5. **S3 (Rubrics)**: Recognition-JE outcome rubric should accept either one-JE-three-lines or three-JEs-one-line-each as long as net staged recognition = $147,825 across the three service lines.
6. **S3 (Rubrics)**: "Agent flags partial-feed contradiction" rubric should fire on Andrea reply text OR Slack post text OR vault memo body — multiple disclosure surfaces are valid.
7. **S3 (Rubrics)**: "Agent surfaces Edith's open FX review note" rubric should be a disclosure/acknowledgment grader, NOT a resolution-state grader (the prompt asks for surfacing, not closing).
8. **S3 (Rubrics)**: Restricted-RV doc retrieval — grade on doc access OR skip-and-cite, multiple valid paths.
