# Council B — Adversarial QC + Density + Hardness Preservation (S1 / prompt phase) — RE-RUN

**Task:** 33_6a4160e9c4abf61d104018e2
**Phase:** prompt (S1) — RE-RUN against REVISED `5_Prompt.txt` and UPDATED `Hardness_Plan.md` (v2)
**Persona:** Carlos Rivera (Loan Officer, FHA + Conventional)
**Universe:** keystone — today 2026-06-12
**Reviewer:** Council B (adversarial QC, density, hardness preservation)
**Prior verdict:** BLOCK on B3 (THIN_DENSITY midpoint ~41.5 vs 50.5 plan) + B6 (PROPAGATE: L9 plant `D_grace_robert` → `D_grace_yamamoto`).

---

## What changed since prior run

1. **Prompt revision (5_Prompt.txt):** one new paragraph added between the "real state from the system" paragraph and the closing write block:
   > *"While you are walking the files, pull each borrower's current contact details and check whether any have replied to outstanding-item emails in the last week. I am calling them this afternoon and do not want to be working off stale information or covering ground Sofia has already covered."*
2. **Hardness_Plan.md v2:** L9 plant location moved from `D_grace_robert` → `D_grace_yamamoto` in three locations:
   - Levers Available table, row 9 (now reads "CORRECTED v2: Grace plant must live in `D-grace-yamamoto` MPIM ... `D-grace-robert` is Grace+Robert only, Carlos has no read access there.").
   - Selected Levers L9 bullet (now reads "Grace Yamamoto plants a plausible-but-wrong Slack message in `D-grace-yamamoto` MPIM (Grace + Carlos + Sofia + 1 other; Carlos has read access)...").
   - Hardness Brief for the Prompt Writer (now reads "CORRECTED v2: original plan named `D-grace-robert` for the plant but Carlos is not a member there; the plant must live in `D-grace-yamamoto`...").

---

## [B3] Tool-Call Density Projection — RE-RUN (PRIMARY FOCUS)

Recompute the realistic competent-Opus-4.8 trajectory under the revised prompt. The new paragraph forces three additional read-classes:

| Δ-driver from new paragraph | Mechanism | Per-task universe basis |
|---|---|---|
| 3× `mortgage_los.borrowers` lookup | "pull each borrower's current contact details" — borrower row is canonical for legal name + phone + email | `mortgage_los.borrowers` carries `legal_name`, `phone`, `email` per row; one row per loan |
| 3-4× `contacts.contacts` resolution attempts | Borrowers may or may not have CRM contact rows; competent agent tries `contacts_search_contacts` per borrower email after pulling LOS row | `contacts.contacts` is the universe's contact directory; not all borrowers materialised here |
| 3-6× email reply check | "check whether any have replied to outstanding-item emails in the last week" — agent must `email_list_emails`/`email_list_threads` filtered to last-week window per borrower, and may need to fetch one or two threads to confirm reply state | 1-week window from 2026-06-12 = 2026-06-05+ |

Full re-tally:

| Component | Range | Midpoint |
|---|---|---:|
| Slack (list_channels + search trio mentions C002 + read `D_grace_yamamoto` + thread replies on 211 chatter) | 6-9 | 7.5 |
| `mortgage_los` loans (3 get_loan + optional list for context) | 3-4 | 3.5 |
| `mortgage_los` conditions (3 list-per-loan; `every one of them in detail` forces per-loan) | 3-4 | 3.5 |
| `mortgage_los` document_checklist_items (3 list-per-loan; `every outstanding item still sitting` pulls these too) | 3 | 3.0 |
| `mortgage_los` staff (lookup of Brian Mitchell + Todd Jennings as LOs of record on 211/622) | 1-2 | 1.5 |
| **`mortgage_los` borrowers (3 explicit per the new paragraph)** | **3** | **3.0** |
| CRM deals (locate 3 deals by loan_number) | 3-4 | 3.5 |
| CRM engagements (list per deal; staleness check) | 3-4 | 3.5 |
| **Email (existing trio-thread reads + NEW per-borrower reply check in last-week window)** | **7-12** | **9.5** |
| **Contacts (Grace email lookup + 3 borrower-contact resolution attempts as fallback path)** | **4-7** | **5.5** |
| Writes (1 email + 1 slack + 3 CRM + 1 add_condition) | 6 | 6.0 |
| Cross-service triangulation buffer | 1-3 | 2.0 |
| **TOTAL projected** | **43-62** | **52.0** |

**Δ vs prior B3 run:** +10.5 calls at midpoint (41.5 → 52.0). Drivers:
- borrowers: 1.5 → 3.0 (now explicit, not "0-3")
- contacts: 1.0 → 5.5 (Grace + 3 borrower fallbacks)
- email: 5.0 → 9.5 (existing trio-thread context + 3-6 reply-check queries in 1-week window)
- All other rows unchanged.

**Gate verdict:** midpoint 52.0 ≥ 50 → **PASS.** Comfortably above the 50+ design target with a 43-62 range (low end 43 still ≥ 40 floor).

**Service breadth recount (v11 G1):**

| Service | Projected calls | % of 52.0 |
|---|---:|---:|
| `mortgage_los` (loans, conditions, document_checklist_items, staff, borrowers) | 14.5 | 28% |
| `slack` | 7.5 | 14% |
| `email` | 9.5 | 18% |
| `crm` (deals + engagements) | 7.0 | 13% |
| `contacts` | 5.5 | 11% |
| Writes spread across email/slack/crm/mortgage_los | (already counted) | — |
| Triangulation buffer | 2.0 | 4% |
| **Distinct services** | **5** | — |

Dominant share 28% (well under 60%). 5 distinct services each ≥ 11% (except triangulation buffer which is not a service). **Breadth gate: PASS.**

---

## [B6] Upstream Propagation — RE-RUN (PRIMARY FOCUS)

| Prior flag | Resolution check |
|---|---|
| L9 plant location: Hardness_Plan.md must move from `D_grace_robert` → `D_grace_yamamoto` | **RESOLVED.** Verified in three locations of `Tasks/33_6a4160e9c4abf61d104018e2/_aux/Hardness_Plan.md`: (1) Levers Available row 9 carries "CORRECTED v2" and explicitly names `D-grace-yamamoto` while flagging that `D-grace-robert` excludes Carlos; (2) Selected Levers L9 bullet specifies the plant in `D-grace-yamamoto` MPIM; (3) Hardness Brief retains the corrected wording. No residual reference to `D_grace_robert` as the plant location remains; the surviving mentions only document the v2 correction rationale. |
| Density projection over-count (50.5 vs realistic ~41.5) | **RESOLVED VIA PROMPT REVISION** (option b from prior B6 recommendation): the new borrower-contact + email-reply paragraph closes the gap to 52.0 midpoint — no Hardness_Plan.md re-baseline is required because the realistic recount now matches the original 50.5 target within rounding. Recommend the operator either (i) leave the Hardness_Plan at 50.5 since the realistic count now matches, or (ii) update the projection to 52.0 to reflect the revised prompt. Neither is blocking. |

**B6 verdict:** Both prior PROPAGATE flags RESOLVED. No new propagation raised.

**Sanity check on the L9 plant carrier under the corrected location:** `slack.slack_channels` shows `D_grace_yamamoto` membership includes Carlos (`keystone_a7fa5b29babd`) per the universe data — the planted Grace message will be readable by Carlos's agent at S2 OE time. Robert Calloway remains a member of `mortgage_los.staff` (los_staff_e85bc913c756) and a legitimate NPC in `D_denise_robert`, but he is NOT the L9 carrier and the prompt does not claim he is.

---

## [B1] QC Sub-dim Scoring — light re-check

The base structure is unchanged; the new paragraph adds one read-class (borrower-contact + email-reply check) without introducing new entities, tools, or write surfaces. Re-scoring:

| Sub-dim | Score | Δ vs prior run | One-line reason |
|---|---:|---:|---|
| Unique Ground Truth | **4** | 0 | Same as prior; trio facts still uniquely resolve. New paragraph adds borrower-record uniqueness, no new ambiguity. |
| Feasibility | **5** | 0 | All required services (incl. contacts, borrowers) available in universe. |
| Explicit Tool Mention | **5** | 0 | New paragraph contains zero tool names. Re-checked: "pull", "contact details", "replied", "outstanding-item emails" — all natural English. |
| Clarity & Specificity | **4** | 0 | Same scope soft-edge on "outstanding item" carries; new paragraph is unambiguous. |
| Contrived / Unnatural | **5** | 0 | "I am calling them this afternoon" is textbook LO behaviour pre-pipeline-review call session. |
| Alignment with Today's Date | **5** | 0 | "this afternoon" → 2026-06-12 PM; "last week" → 2026-06-05+; both in-window. |
| Truthfulness | **5** | 0 | New paragraph is Carlos's voice; no unverifiable claims. |
| Tool Use & Cross-service | **5** | 0 | Now forces 5 services minimum (mortgage_los + slack + crm + email + contacts). |
| Investigation + Action | **5** | 0 | Read surface expanded by ~10 calls; writes unchanged. |
| Coherence / Bolt-on | **5** | 0 | New paragraph flows from `I am calling them this afternoon` motivation — not bolted on. |
| Persona | **5** | 0 | "covering ground Sofia has already covered" is on-voice for Carlos's relationship with his processor. |
| Business Function | **5** | 0 | Loan Operations: borrower-side communications hygiene fits the function. |

**B1 verdict: no FAILs, no score drops. Two 4-scores hold from prior run (both justified).**

---

## [B2] Adversarial Alt-Path / Second Reading — light re-check

New paragraph's two clauses re-tested for second-reading ambiguity:

| New clause | Second reading attempted | Flips a write? |
|---|---|---|
| "pull each borrower's current contact details" | (a) `mortgage_los.borrowers` only; (b) `mortgage_los.borrowers` + `contacts.contacts` cross-check; (c) `contacts.contacts` first then fallback | All three readings produce the same Grace email body content (borrower name + phone + email per loan). **No write flip.** Reading (a) under-counts density slightly; reading (b) is the modal competent-agent path. |
| "check whether any have replied to outstanding-item emails in the last week" | (a) any reply by any borrower in last week; (b) only replies on threads explicitly about outstanding conditions/items | Both readings produce the same observable: "borrower X replied / did not reply". The Grace email body would carry the same status note either way. **No write flip.** |
| "covering ground Sofia has already covered" | Narrative — Carlos's reason; not an action requirement | **No action divergence.** |

**B2 verdict: PASS.** Zero divergence in write set introduced by the new paragraph. The pre-existing soft-edges on `outstanding item` scope and `longest-overdue file` carry forward unchanged (both reconverge on LN-2026-00009 per prior B2).

---

## [B4] Hardness Preservation — light re-check

| Lever | Status post-revision | Note |
|---|---|---|
| **L10 Reversal on LN-2026-00211** | **PRESERVED** | `genuine status... right now` + `loan officer of record` + (new) `pull each borrower's current contact details` still forces `mortgage_los_get_loan` on 211, surfacing `status=withdrawn`. |
| **L2 Structured-DB skip on `mortgage_los.conditions`** | **PRESERVED** | `every one of them in detail` is unchanged; new paragraph references "outstanding-item emails" which does NOT pre-solve the conditions read (emails are reply-check surface, not the canonical condition list). |
| **L9 Authority dismissal from Grace** | **PRESERVED** | Grace's quoted reassurance `211 is back in motion because Sofia got it unstuck` is intact in the prompt body. The corroborating Slack plant now lives in `D_grace_yamamoto` per Hardness_Plan v2 — Carlos-readable. |
| **L8 Multi-link chain** | **PRESERVED + ENHANCED** | Was 4 services (mortgage_los + slack + crm + email). Now 5 services with `contacts` explicitly forced. Three reductions still hold (Slack chatter → LOS truth; LOS conditions → email reply state; CRM engagement → LOS reconciliation). |
| **L25 Existing-output anchor** | **PRESERVED** | `the notes on those have been going stale` is intact; the borrower-reply check adds a SECOND existing-output anchor candidate (email threads) — the agent that anchors to "no recent reply" without checking the LOS status flip still misses the 211 withdrawal. |

**B4 verdict: All 5 selected levers preserved; L8 hardness arguably strengthened by the contacts-service add.**

---

## [B5] Tool-leak / Phrasing Scan — light re-check

New paragraph text scanned:

| Check | Result on new paragraph |
|---|---|
| Tool names (`email_send_email`, `mortgage_los_get_borrower`, `contacts_search_contacts`, `email_list_emails`, etc.) | **0 hits.** "pull each borrower's current contact details" and "check whether any have replied to outstanding-item emails" are natural English. |
| Internal IDs | **0 hits.** |
| Em-dashes (—) | **0 hits.** |
| En-dashes (–) | **0 hits.** |
| `at least N` without explicit mandate | **0 hits.** |
| `approximately` before IDs/dates | **0 hits.** |
| Generic-urgency clichés | **0 hits.** |
| Hyphenated compound check | "outstanding-item emails" — hyphen, not en/em-dash. ✓ |

Whole-document re-scan also clean (prior B5 0-hit count holds).

**B5 verdict: clean.**

---

## Summary of resolutions

| Prior issue | Status |
|---|---|
| B3 THIN_DENSITY (midpoint ~41.5) | **RESOLVED.** Revised prompt drives midpoint to 52.0 (range 43-62). |
| B6 PROPAGATE (L9 plant `D_grace_robert` → `D_grace_yamamoto`) | **RESOLVED.** Hardness_Plan.md v2 verified in three locations. |
| B1 / B2 / B4 / B5 (clean from prior run) | **STILL CLEAN.** No regressions introduced by the new paragraph. |

---

## Final verdict

VERDICT: GO -- B3 PASS (midpoint 52.0 ≥ 50, range 43-62; service breadth 5 services with healthy spread), B6 RESOLVED (Hardness_Plan v2 places L9 plant in D_grace_yamamoto where Carlos has read access; prior D_grace_robert reference removed except as v2-correction documentation), B1/B2/B4/B5 still clean (no FAILs, no write-flip second reading, all 5 levers L10+L2+L9+L8+L25 preserved with L8 enhanced, zero tool-name/em-dash/internal-ID leaks).
