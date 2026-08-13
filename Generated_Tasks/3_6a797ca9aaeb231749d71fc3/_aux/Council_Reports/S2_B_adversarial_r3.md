# Council B — Adversarial QC, R3 (delta-focused)

**Task:** `Generated_Tasks/3_6a797ca9aaeb231749d71fc3` (HarmonyGames, framework `hg`)
**Round:** R3 (delta-only)
**Scope of changes since R2:** OE 22, OE 23, OE 24. R2 verdict was GO. All other OEs unchanged.
**Sources read:** `6_Oracle_Events.txt` (R3); mental-application of OE 24 predicate against `HarmonyGames_Base_Universe/Services_Data/linear/data.json` (`team_ART` + title contains `VFX` = 55 rows).

---

## 1. OE 24 predicate — determinism + resolved identifier

**Predicate as authored:**
> the ART-team issue whose title binds VFX tracking or vendor-art scope broadly (title contains "VFX" and either references a general tracking role or the most recent live-state ART VFX work), tie-broken by the most recent updated_at
>
> Fallback: If the search returns no live-state (unresolved) ART VFX tracker (all rows Done or stale by more than six months relative to universe today 2026-02-28), still select the most recently updated ART VFX ticket as the reconciliation home.

**Mental application against `linear.issues WHERE team_id="team_ART" AND title CONTAINS "VFX"` (55 rows):**

| Candidate | id | title | state_id | updated_at | note |
|---|---|---|---|---|---|
| "general tracking role" match | ART-252 | `ART: VFX` | Canceled | 2024-04-05 | canceled ~23 months ago |
| "most recent live-state" match | ART-585 | `VFX For Character Unlock Animations` | Todo | 2024-07-04 | only live-state row, stale ~19 months vs today 2026-02-28 |
| "most recently updated ART VFX ticket" | **ART-770** | `River Rush VFXs and Animations` | Done | 2025-05-12 | fallback winner |

Six-month freshness cutoff (relative to universe today 2026-02-28) = 2025-08-28. Every one of the 55 rows is either Done/Canceled OR updated before that cutoff. The one live-state row (ART-585) is stale ~19 months → **fallback trigger fires**.

Fallback rule: "select the most recently updated ART VFX ticket". `updated_at` values are unique across the 55 rows (no ties on the top row), so the fallback yields exactly one identifier.

**Resolved identifier: `ART-770` ("River Rush VFXs and Animations", updated 2025-05-12T09:11:57Z).**

Determinism status: **PASS**. Every reader running the same predicate on the same universe reaches ART-770. The tie-breaker is not needed at the top row because updated_at is strict.

Side note (not blocking): OE 24 correctly instructs OE 25's comment body to "note the stale-tracker reality itself" so the downstream write records that ART Linear is not currently the live source of truth for vendor art work. That mitigates the awkwardness of writing onto a Done ticket.

---

## 2. F1 AMBIGUOUS_TARGET (from R1) — closure check

R1 flagged AMBIGUOUS_TARGET because the ART tracker was named by identifier in prompt language without a resolution path.

R3 OE 24: "The evidence identifier is used only for the downstream write; the OE does not pin a specific ART number in prompt language." Target is named by a predicate + tie-breaker + fallback that yields a single row. No prompt-language identifier appears.

**F1 closure status: CLOSED.**

---

## 3. F2-r2 LOOSE-ATOM (from R2) — closure check on OE 22

R2 flagged OE 22 for asserting `badges.checkItems == 0` on the two sibling cards as an atomic expectation (loose atom, not verified through evidence).

R3 OE 22 rewrite: "From the OE 17 card listing, read the badges.checkItems field on card X and Y; if either shows badges.checkItems > 0, fall through to trello_get_card and trello_get_checklists_on_board post-filtered by idCard for that sibling and descend into its check_items. If both siblings' badges.checkItems values are 0 (post-filtering the OE 19 board-level checklist result set for either sibling idCard also yields zero rows in that case), conclude that…"

The value is now (a) read from OE 17's already-gathered payload, (b) conditionally branched — no numeric assertion is made; (c) cross-verified against the OE 19 board-level checklist post-filter when the zero-branch is taken. No naked atom.

**F2-r2 closure status: CLOSED.**

---

## 4. B3 density projection (R3)

OE-mandated tool-call inventory (conservative; no agent-overhead multiplier):

| OE | Calls | Notes |
|---|---|---|
| 1, 2, 3, 4, 5, 6, 7, 8, 9 | 9 × 1 = 9 | fixed |
| 10 | 10 PRs × 2 (get_pr + get_reviews) = 20 | Marcus-authored PR sweep |
| 11, 12, 13 | 3 × 1 = 3 | user/contacts/linear lookups |
| 14 | 5 / 6 / 7 | contacts×2 + gdrive×1 + github_list×1 + get_pr on 1–3 Leapblock-tied PRs |
| 15, 16, 17, 18, 19, 20, 21 | 7 × 1 = 7 | Trello board/list/card/checklist sweep |
| 22 | 0 / 1 / 2 | conditional; two siblings; 0 if both badges.checkItems == 0 |
| 23, 24 | 2 × 1 = 2 | linear_list_issues + linear_get_issue |
| 25, 26, 27, 28, 29 | 5 × 1 = 5 | 5 writes |
| 30 | 0 | narrative reply, HG has no gmail send tool |
| **Total (OE-mandated)** | **51 / 53 / 55** | **{low, mid, high}** |

Add typical agent exploration overhead (~0–2 calls: at-most 1 retry, 1 extra list expansion). Realistic projected trajectory density:

**{low: 51, midpoint: 53, high: 57}**

Midpoint 53 ≥ 50 → **B3 PASS**. Consistent with R2's 54–56 midpoint (within noise).

---

## 5. Lever preservation (end-to-end)

| Lever | Where preserved in R3 | Status |
|---|---|---|
| L1 latching (Trello check_items drift from git reality) | OE 20 shows both check_items "incomplete" despite PR #36 having shipped Marcus's VFX; OE 26 toggles only "Marcus to create VFX" and leaves "Engineer to implement" open with reason. | PRESERVED |
| L2 structured-DB skip, variant A (PR body / CodeRabbit summary hides substantive review pushback) | OE 4/8/9 explicitly require the deeper reviews + inline comments endpoints and call out that the top-level counts hide the CHANGES_REQUESTED and inline pushbacks. | PRESERVED |
| L2 structured-DB skip, variant B (Linear ART tracker no longer live source of truth) | OE 24 fallback + OE 25 note-to-reader that ART Linear is stale, so the tracker's identifier alone would mislead. | PRESERVED |
| L6 Marcus disambiguation | OE 11–13 enumerate three harmonygames.co Marcuses vs GitHub-only PERSON_0396; OE 25 and OE 30 both call out per-piece attribution. | PRESERVED |
| L9 authority dismissal (Leonard's "already covered") | OE 30 supports parking PR #1 but explicitly rejects the broader "already covered" framing on the basis of PR #37's unresolved CHANGES_REQUESTED and the still-open "Engineer to implement" line-item. | PRESERVED |
| L10 reversal/supersession (PR #1 draft superseded by PR #36 + PR #16) | OE 2 fixes PR #1 as draft/+0/no reviews; OE 5/6 fix PR #36 and PR #16 as the substantive merged imports; OE 25/28/30 reconcile the supersession explicitly. | PRESERVED |

All 5 (in effect 6, counting L2's two variants) levers intact through R3.

---

## Council B verdict: GO