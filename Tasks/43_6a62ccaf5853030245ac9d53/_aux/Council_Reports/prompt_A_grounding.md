# Council A — Grounding & Convention — Prompt Phase

**Task:** `Tasks/43_6a62ccaf5853030245ac9d53`
**Deliverable:** `5_Prompt.txt`  ·  **Universe:** starpm  ·  **Today:** 2026-07-01 (America/Chicago)
**Iteration:** 1  ·  **Date:** 2026-07-25  ·  **Verdict: GO**

Every claim below was verified directly against `_aux/Universe_Split/*.json` (parsed `row_data`), not from any upstream summary.

## Deterministic floor
`python3 Validators/verify_universe_atoms.py --task Tasks/43_6a62ccaf5853030245ac9d53 --verbose`
-> `[PASS] 0 fails, 0 warns, 0 atoms checked`. Report: `_aux/Council_Reports/verify_universe_atoms.md`.
NOTE: the atom checker declared 0 atoms, so it is a vacuous PASS. All grounding below was therefore performed manually against the per-task universe split.

---

## A1 — Grounding sweep

| # | Claim in prompt | File : record locator | Verdict |
|---|---|---|---|
| 1 | Persona Carlos Mendez (Onsite PM) | `PersonaBrief.txt`; `gmail.gmail_messages.json` id `5101c5a41dffa90a` from_address `carlos.mendez@starpm.com`; QB bill PrivateNotes name "Carlos Mendez" (`quickbooks` id `991582431419`, `546359391323`) | GROUNDED |
| 2 | "Mesa Vista 4C" unit | `quickbooks.quickbooks_entities.json` id `445653930748` line descriptions "Mesa Vista Unit 4C"; `airtable.airtable_records.json` `recbd087a4abd605b` / `recc8534b3fd13954` fldUnit "Mesa Vista 4C"; ticket `reca424761ae15355` | GROUNDED |
| 3 | Owner "Linda Castillo" | `contacts.contacts.json` contact_id `b47044b4ec775b318bac813d5fb1bf5d`, job "Property Owner", `linda.castillo@gmail.com`; AR invoice `445653930748` CustomerRef name "Linda Castillo" (value `proj-4ae920b7c9e8`) | GROUNDED — **A1(a) CONFIRMED: Linda is CustomerRef on 2026-534** |
| 4 | Prior cost summary / "summary calling it done" sent to Linda | `gmail.gmail_messages.json` id `5101c5a41dffa90a`, to `linda.castillo@gmail.com`, subj "Mesa Vista 4C Make-Ready Complete. Cost Summary for Your Records", 2026-06-02; AR invoice `445653930748` CustomerMemo to "Linda" | GROUNDED — **A1(b) CONFIRMED** |
| 5 | Post-move-out deep clean | AR line 1 $387 (`445653930748`); AP bill `195089456477` (Sunshine, Doc 2026-SC-4C) $387 | GROUNDED — **A1(d)+(e)** |
| 6 | Full interior repaint | AR line 2 $1,140 (`445653930748`); AP bill `696089964235` (Permian / Pete Donovan, Doc PD-2026-09) $1,340 | GROUNDED — **A1(d)+(e)** |
| 7 | Closet trim touch-up | AR line 3 $95 (`445653930748`); AP bill `546359391323` (Permian, Doc 2026-519) $85 | GROUNDED — **A1(d)+(e)** |
| 8 | Make-ready record for 4C | `airtable.airtable_records.json` tblMakeReady `recc8534b3fd13954` (selReady) + `recbd087a4abd605b` (selProg); tblMaintenanceTickets `reca424761ae15355` (market-ready) | GROUNDED — **A1(c) CONFIRMED** |
| 9 | Costs are a pass-through to the owner | AR PrivateNote "Owner cost pass-through invoice…"; AP PrivateNotes "Pass-through to owner" (`195089456477`, `546359391323`, `696089964235`) | GROUNDED |

**A1 result: 0 ungrounded concrete claims.** Every named entity, amount-bearing item, and state artifact in the prompt resolves to a materialized universe row. The Pete-Donovan owner cue is a decoy (`contacts` job "Exterior Painter") and the prompt does **not** leak it.

---

## A2 — Convention sweep

- **Word count: 364** (cap 500) — PASS.
- **Em-dash / en-dash: 0 of each** (U+2014, U+2013) — PASS.
- **No pre-solving of the number:** `1,812 / 1812 / 1,727 / 1,897` all absent — PASS. Correct total never appears verbatim (matches Hardness_Plan L15/L16 requirement).
- **No internal IDs / DocNumbers / leaked amounts:** none of `2026-534`, `2026-SC-4C`, `PD-2026-09`, `2026-519`, `2026-481-566`, entity IDs, or the stale line amounts (`1140`, `1622`, `$95`, `$85`, `$387`) appear — PASS.
- **No tool / MCP-server names:** none. The word "Airtable" appears once ("our 4C make-ready record in Airtable"). Per `3_StarPM_TASK CATEGORIES.md` line 93 the "no tool names" rule targets function-style names (`airtable_mock_update_record`), and the Format Card explicitly whitelists the product name "Slack" as a natural reference — so naming the system "Airtable" is **not** a hard-rule violation. NON-BLOCKING (optional softening to "our make-ready tracker").
- **First-person natural voice / mid-thought entry:** PASS — opens mid-situation ("I'm going back through the make-ready items I still have open…"), asymmetric knowledge, no "Hi, I need" opener, no checklist tone.
- **One coherent situation (sentence-removal):** PASS — every sentence advances the single 4C owner-cost closeout; no bolt-ons.

**A2 result: 0 drift on Major fields.**

---

## A3 — Narrative State Consistency

| State claim (quote) | Record : locator | Verdict |
|---|---|---|
| "the make-ready items … the ones that are actually finished" / 4C treated as done | airtable `recc8534b3fd13954` selReady "Unit confirmed ready for leasing"; ticket `reca424761ae15355` "market-ready"; slack `ef33c545…` "4C is market-ready" | CONSISTENT (belief-on-its-face, intended) |
| "back in the spring I billed her" | AR invoice `445653930748` TxnDate 2026-05-01 (spring) | CONSISTENT |
| "sent her a summary calling it done" | gmail `5101c5a41dffa90a` to Linda, 2026-06-02, "fully wrapped up" — before today 2026-07-01 | CONSISTENT |
| "that summary is the record she keeps" | AR invoice + belief email both exist and were issued to Linda | CONSISTENT |
| "what she was actually charged" (implying a live, holdable invoice) | AR `445653930748` Balance 1622, active=true, not voided | CONSISTENT |

**Belief/truth gap is intact and INTENDED:** the face records (selReady row, market-ready ticket, "fully wrapped up" email, $1,622 AR) support Carlos's belief, while the contradicting truth ($1,340 repaint / $85 closet) lives only in the AP bills (`696089964235`, `546359391323`). This is the flagship L2/L10 lever, not a contradiction to block on. **0 blocking contradictions.**

---

## A4 — Action-vs-Universe-Prescription

- Prompt asks: reconcile AR against AP, **correct the existing invoice** (explicitly "I do not want a second bill created next to the one she already has. Correct the invoice she is holding"), update the Airtable 4C record, email Linda, post to a channel.
- Scanned `linear_issues` (0 4C hits), `linear_comments` (0), `slack_messages` (5 4C hits — all reinforce "done/market-ready", none prescribe an alternative), `gmail` (5 4C hits — all belief-supporting). **No universe record prescribes a different resolution, a second invoice, or a different owner total.**
- Authority: `2_StarPM_PERSONA BRIEFS.md` + `3_StarPM_TASK CATEGORIES.md` — Carlos anchors Mesa Vista; `makeready_turn_carlos` (Mesa Vista 4C) is his 9-action signature scenario; Cat 1 primary systems include QuickBooks (invoicing), Airtable, Slack, Gmail (owner comms). He has authority for every asked action.
- The prompt's explicit "correct, do not duplicate" language pre-empts Stump Hypothesis 4 (duplicate-invoice failure) — correct framing.

**A4 result: 0 action-divergence, 0 authority gap.**

---

## A6 — Persona Scope

Possessives ("my open items", "our make-ready record", "our channel", "her account") all fall inside Carlos's assignment scope: he anchors Mesa Vista (persona brief) and Linda Castillo is listed as a Category 1 property-owner NPC he services. **0 scope drift.**

---

## A7 — Clarity & Specificity (cold read)

- **Write-Action Divergence (HARD GATE):** RESOLVED in-prompt. "Correct the invoice she is holding," not create a new one — single, unambiguous write-action set. PASS.
- **Delegation clarity (HARD GATE):** PASS — assistant does the work directly; no ambiguous hand-off.
- **Conditional branch** ("if clean, log closed; if not, correct + update + email + post"): both branches fully specified; the universe determines the branch (discrepancy exists), which is intended investigation difficulty, not ambiguity. Not a clarity gap.
- **MINOR — channel target:** "our channel for the crew and front office" does not name a specific channel; `#make-ready`, `#vendors`, `#owner-relations` are all plausible. The write-**action** (one Slack coordination post carrying the corrected number) is identical across readings, so readings do **not** diverge in write-actions. MINOR, non-blocking (OE accepts #vendors or #owner-relations).
- **MINOR — two 4C make-ready rows** (selProg + selReady): "our 4C make-ready record" is nominally singular; updating the 4C make-ready record is still an unambiguous action, and the split is the intended latching lever. MINOR, non-blocking.

**A7 result: 0 MAJOR clarity gaps.**

---

## A10 — Business Function Match

- Assigned: **Property Operations (StarPM BF1)**.
- Prompt primary scenario: Mesa Vista 4C make-ready owner cost pass-through reconciliation + turnover closeout.
- `3_StarPM_TASK CATEGORIES.md` Category 1 → subcategory **1.1 Unit Turnover Coordination**, linked scenario `makeready_turn_carlos` (Carlos primary), Linda Castillo listed as a Cat 1 owner NPC. QuickBooks owner invoicing + Airtable make-ready + owner email are all named Cat 1 systems/artifacts.
- `BUSINESS_FUNCTION: assigned=Property Operations, prompt_primary=make-ready owner cost pass-through reconciliation, match=TRUE`.

---

## A11 — End-to-End Solvability

Every dependency-chain row is materialized in `_aux/Universe_Split/`:

| Chain step | Required row | Present? |
|---|---|---|
| Airtable 4C make-ready state | `recc8534b3fd13954` (selReady) + `recbd087a4abd605b` (selProg) + `reca424761ae15355` (ticket) | YES |
| AR invoice to Linda | `quickbooks` id `445653930748`, DocNumber 2026-534, CustomerRef Linda Castillo, TotalAmt 1622 | YES |
| AP deep clean $387 | `195089456477` (Sunshine) | YES |
| AP repaint $1,340 | `696089964235` (Permian / Pete Donovan) | YES |
| AP closet trim $85 | `546359391323` (Permian) | YES |
| Internal-inspection exclude decoy $85 | `991582431419` (Alamo HVAC, "Internal labor charge for Carlos Mendez's make-ready walk", not on AR) | YES |
| Linda Castillo contact | `contacts` `b47044b4ec775b318bac813d5fb1bf5d` | YES |
| Coordination channel | `slack_channels` `#make-ready` (C004), `#vendors` (C005), `#owner-relations` (C006) | YES |

Derivation: 387 + 1340 + 85 = **$1,812** (repaint understated $200, closet overstated $10 vs the $1,622 AR); Alamo $85 excluded as internal. Chain is complete. **0 solvability breaks.**

---

## Non-blocking observations
1. "Airtable" is named explicitly once — permitted (Slack precedent + task-cat line 93 scoping). Optional-only softening.
2. Two tblMakeReady 4C rows (selProg + selReady) — intended latch; "our 4C make-ready record" is fine as an action target.
3. "our channel" is channel-agnostic — write-action unchanged across readings; MINOR only.
4. Belief email is 2026-06-02 (early summer) while the prompt says "back in the spring"; invoice TxnDate is 2026-05-01 (spring). Colloquially natural; non-blocking.

---

```json
{"phase":"prompt","council":"A","task_dir":"Tasks/43_6a62ccaf5853030245ac9d53","verdict":"GO","perspectives":{"A1_grounding":"PASS — 0 ungrounded claims; all 9 claims resolve to universe rows; Linda=CustomerRef on 2026-534, belief email to Linda, Airtable 4C make-ready + AR lines + AP bills all present","A2_convention":"PASS — 364 words; 0 em/en dashes; no IDs/DocNumbers/leaked amounts; correct total 1812 absent; no tool/MCP names ('Airtable' is a permitted system reference)","A3_narrative_state":"PASS — belief/truth gap intact and intended; 0 blocking contradictions","A4_action_prescription":"PASS — corrects existing invoice (not a duplicate); no record prescribes a different action; Carlos has authority","A6_persona_scope":"PASS — Mesa Vista 4C + Linda within Carlos's scope","A7_clarity":"PASS — 0 MAJOR gaps; write-action divergence + delegation gates resolved; 2 MINOR (channel target, dual make-ready rows)","A10_business_function":"PASS — Property Operations, Cat 1.1 Unit Turnover Coordination, match=TRUE","A11_solvability":"PASS — all chain rows materialized; 0 solvability breaks"},"iteration":1,"timestamp":"2026-07-25"}
```
