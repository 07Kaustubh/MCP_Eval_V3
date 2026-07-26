# Council B — Adversarial QC + Density + Hardness Preservation

**Deliverable:** `Tasks/41_6a61a86a3453b3714bdc72ef/5_Prompt.txt` (S1 prompt phase)
**Universe:** StarPM V4 (dual-model: Opus 4.8 + Gemini) · Universe today = 2026-07-01 (America/Chicago)
**Persona:** Lisa Smith, Onsite Property Manager (Property Operations, BF1)
**Lenses applied (union verdict):** Architect · Implementer · Red-team · Ground-truth · Integration

All load-bearing universe records were re-queried directly from `_aux/Universe_Split/` (not trusted from the Hardness_Plan). Confirmed live:
- AP bill `232176553533` / DocNumber `QR-2026-0441`: `VendorRef` "Alamo HVAC Services" (value 200), **no CustomerRef**, `Balance`/`TotalAmt` **2132.0**; lines 847 + 925 + 210 + **150 ("Partial payment plan credit applied", stored as a POSITIVE Amount that ADDS)**. PrivateNote: "Consolidated rent ledger compiled by Teresa Wood for Tanya Mitchell eviction filing package." → three readings 2132 (stored) / 1982 (charges) / **1832 (net)**. L2 + L11 confirmed live.
- AR invoice `283231782926` / DocNumber `7214`: `Balance` **0.0**, CustomerRef Tanya Mitchell, TotalAmt 8173.44 with a 5885.94 "credit" pad; zeroed by payment `952690463873` (8173.44, LinkedTxn→7214, UnappliedAmt 0). The paid decoy confirmed.
- Airtable `recc83c05d889b354` (tblMakeReady, Unit 14, mod **2026-07-01 11:18**): "Eviction petition … being coordinated with the Justice of the Peace — make-ready work on this unit cannot begin until the legal process concludes and possession is formally returned." L10 + L31 confirmed.
- Airtable `rec922b9a2d1b9451` (EVF-2026-014, mod 2026-06-30): "Owner authorization received from Linda Castillo … Owner Approved - Ready to File." Supersession + true owner confirmed.
- Airtable `receee45491536859` ("awaiting owner sign-off") and `rec769c9f03f0b85f` ("active payment plan") = superseded reassuring frames. Confirmed.
- Airtable `rec94e86a3007dd5e` = "Rio Bend - Unit 14", `selReady` (rent-ready) — the near-miss unit (L6). Confirmed.
- Linear: "Eviction Hearing - Mitchell, **Harris Property**" + "Mitchell eviction hearing prep - checklist complete, status advancing" = the latching decoy (L1). Contact `linda.castillo@gmail.com` (Property Owner) confirmed; "Harry Harris" appears only in the Linear framing (mis-attribution trap).
- Gmail `74cc50c7d2ffb7dc` (2026-07-01, "Eviction Filing Procedures and Hearing Availability") + `a559caf010645abe` ("Re: Eviction Filing Authorization"); gcalendar "JP Court Eviction Filing Appointment" 2026-07-01 16:30 vs older "Mitchell Eviction Court Hearing" 2026-05-13. Petition-not-yet-filed current state confirmed.

Prompt leak scan (grep): **0** em/en/figure dashes, **0** dollar figures / multi-digit numbers, **0** tool/function/MCP/ID tokens, **0** "at least N" / "approximately". Word count 399.

---

## [B1] QC sub-dimension scoring (bar = 5)

SUB-DIM Unique Ground Truth -> SCORE 5/5 (1/3/5) -> REASON single end-state per ask; balance uniquely = net-of-applied-credit ("real outstanding figure … not double-counting any credit that got applied" → 1832), eviction status uniquely = owner-approved/JP-coordination/not-filed, unit uniquely = hold; no file-now-vs-defer (prompt asks to REPORT whether filed, never to file).
SUB-DIM Feasibility -> SCORE 5/5 (1/3/5) -> REASON every ask actionable with StarPM tools (QB read/derive, Airtable read+write, Gmail read+draft-only, Slack read+post, Linear read+note); no conflicting or impossible instruction; "draft me an email … so I can look it over" matches gmail draft-only.
SUB-DIM Explicit Tool Mention -> SCORE 5/5 (1/5 binary) -> REASON no function/MCP names; "QuickBooks", "make-ready channel", "email" are permitted natural product/channel references.
SUB-DIM Prompt Clarity & Specificity -> SCORE 5/5 (1/3/5) -> REASON four writes all determinate (update make-ready record, note eviction ticket, post make-ready channel, draft owner email); no write-vs-no-write / act-vs-defer ambiguity; only minor OE-phase pin needed on which surface = "the eviction ticket" (identical note content either way — non-blocking, see B2).
SUB-DIM Contrived / Unnatural -> SCORE 5/5 (1/3/5) -> REASON natural warm-professional owner-brief message; no step list, no exact-timestamp/format constraints; difficulty is organic (stale memory, scattered/conflicting systems).
SUB-DIM Truthfulness -> SCORE 5/5 (1/3/5) -> REASON the "mostly squared away" / "about at the hearing stage" beliefs are explicitly HEDGED recollections to verify ("last I tracked", "if anything I've assumed is off, tell me plainly"), not asserted facts; no tight-identifier claims; persona/tenant/unit/owner all grounded.
SUB-DIM Tool Use & Cross-service -> SCORE 5/5 (1/5 binary) -> REASON facts scattered across QuickBooks + Airtable + Gmail + Slack + Linear + gcalendar + hubspot + contacts and must be reconciled; far beyond a single service.
SUB-DIM Investigation + Action -> SCORE 5/5 (1/5 binary) -> REASON investigation (balance / eviction status / unit disposition) feeds four writes (Airtable update, ticket note, Slack post, Gmail draft).
SUB-DIM Coherence (Bolt-on) -> SCORE 5/5 (1/5 binary) -> REASON every ask funnels into one situation (the Tanya Mitchell owner brief); removing any sentence leaves the brief incomplete; no unrelated staple.
SUB-DIM Persona -> SCORE 5/5 (1/3/5) -> REASON Lisa Smith (Onsite PM) leads the Tanya Mitchell / accommodation scenario, drives make-ready, is the tenant↔owner connective tissue; prepping an owner brief on delinquency/eviction/unit-turn is squarely in scope; warm-professional voice matches.
SUB-DIM Business Function -> SCORE 5/5 (3/5) -> REASON tenant delinquency + eviction status + make-ready/unit-turn disposition + owner brief is core Property Operations (BF1); unambiguous match.
SUB-DIM Alignment with Today's Date -> SCORE 5/5 (1/3/5) -> REASON current state (owner approval 06-30, JP filing appt 07-01, make-ready record mod 07-01) aligns to universe today 2026-07-01; relative phrasing ("today", "a few weeks stale", "last I tracked") resolves cleanly; no future-event ask.
SUB-DIM Universe Data Exists -> SCORE 5/5 (1/5 binary) -> REASON every load-bearing record re-queried and present (AP bill, AR invoice, payment, make-ready supersession chain, EVF-2026-014, Linear Harris decoy, Gmail auth/filing threads, gcalendar events, contacts).
SUB-DIM Universe Cross-service Coherence -> SCORE 5/5 (1/5 binary) -> REASON the Harris-vs-Castillo / hearing-vs-JP / $0-vs-$2,132 conflicts are DESIGNED hardness with a determinable truth (freshest Airtable SoR + semantic note-dates + AP filing-package ledger + Gmail 07-01), not [Fail - Task Relies on Misaligned Data] — a unique ground truth exists.

**All applicable sub-dims = 5.**

---

## [B2] Adversarial second-reading attack

**(a) Wrong "Unit 14" (Rio Bend `rec94e86a3007dd5e`).** The entire prompt is bound to "Tanya Mitchell's situation" / "her unit" / "Tanya genuinely owes". Rio Bend - Unit 14 (`selReady`, Victor Rios carpet job) carries **no Tanya linkage** — updating its make-ready record satisfies none of the Tanya-bound asks (balance, eviction, owner auth). "Tanya Mitchell" is a strong, repeated disambiguator; Rio Bend is a designed near-miss (L6) the agent must avoid, not a legitimately valid second reading. The correct end-state (Tanya's Sunset Ridge / 1402 Rimrock Unit 14, eviction hold) is unique. **No divergence.**

**(b) Paid-invoice "$0 / current" reading.** The prompt explicitly rejects it: "I was under the impression the back rent had mostly been squared away, but I am not putting a number in front of the owner that I haven't checked … Whatever the real outstanding figure is for the filing package, walk it back to the underlying charges … not double-counting any credit or adjustment that got applied." Invoice 7214's $0 balance is the decoy; "for the filing package" points at the AP bill whose PrivateNote is literally the filing-package ledger, and "walk it back to the underlying charges" forbids accepting a stored balance. Reporting "$0/current" as the final answer is **not** a permitted reading. **No divergence.**

**(c) "confirm we have the owner's authorization on file."** Unique answer: EVF-2026-014 — Linda Castillo authorization received 06-30, "Owner Approved - Ready to File." The only trap is mis-attribution to Harry Harris (Linear framing); the true owner-of-record is Linda Castillo. Single correct answer (yes, on file, from Linda Castillo, 06-30). **No divergence.**

**Minor (non-blocking) observation for S2:** "Leave a short note on the eviction ticket" leaves the surface (Linear eviction issue vs Airtable EVF-2026-014) slightly open. This does NOT flip a write recipient or the final universe state — the note content (documenting current JP-coordination/not-filed state) is identical either way, so it is immaterial per the UGT precision guardrail (identical deliverable) and the Clarity same-action-different-surface band. The OE phase should pin the canonical target (Hardness_Plan projects Linear `save_comment` on the eviction issue); not a prompt-phase block.

**B2 result: no adversarial divergence found.**

---

## [B3] Tool-call density projection — PER MODEL (StarPM v4 bands: >=40 PASS / 15-39 THIN / <15 INSUFFICIENT)

**Opus 4.8 trajectory sketch (midpoint ~49):**
- contacts: resolve Tanya Mitchell + Linda Castillo (owner) [+ Court Clerk] — ~2-3
- quickbooks: customer search (13-entity catch-all) → invoice 7214 → payment 952690463873 → bill search → AP bill QR-2026-0441 → inspect lines → credit memos CM2026-089/CM-2026-044 → net derivation — ~8-10
- airtable: list Tanya/Unit 14 make-ready records → traverse supersession chain (plan → breach → 3-day → did-not-cure → awaiting sign-off → JP coordination) → EVF-2026-014 → Rio Bend near-miss check → **WRITE** current-state update — ~10-12
- gmail: eviction-auth thread (Brooke request → Linda Castillo reply) → 07-01 filing-procedures thread → accommodation thread (avoid conflation) → **WRITE** owner draft — ~7-9
- slack: #general/#make-ready parents + thread replies (plan/breach/escalation) → **WRITE** #make-ready post — ~6-7
- linear: OPS-32/38/54 Harris-hearing decoy reads → **WRITE** note on eviction issue — ~4-5
- gcalendar: Harris hearing 05-13 / 3-day deadline / JP filing 07-01 — ~3
- hubspot: ESA accommodation tickets/addendum (avoid conflation) — ~2-3

Opus total ≈ 42-56, **midpoint ~49 → PASS** (>=40).

**Gemini trajectory (~0.85x leaner on lever traversal; Task 40 empirical 33-47):** projected ~36-48, **midpoint ~42 → PASS** (>=40). Marginal (just above the floor) but within band; the four independent levers (L2 discovery / L11 disposition / L1 anchor / L10 supersession) plus four cross-service writes keep even the lean run above 40.

**Service breadth (distinct services >=5% of a ~50-call trajectory):** airtable ~22%, quickbooks ~18%, gmail ~17%, slack ~13%, gcalendar ~6%, hubspot ~5%, linear ~9%, contacts ~4%. **8 distinct services, 7 at >=5% → breadth PASS**; no single service dominates (max ~22%).

**B3 result:** Opus midpoint **~49 PASS**, Gemini midpoint **~42 PASS**. Both models clear the v4 >=40 bar. (V3 50/40 scheme correctly NOT applied.)

---

## [B4] Hardness preservation (5 selected levers)

- **L2 Structured-DB skip** — TRIGGERED. "checked against what is actually in QuickBooks myself … the real outstanding figure for the filing package, walk it back to the underlying charges." The "mostly squared away" belief + "for the filing package" march the agent straight into the $0 invoice decoy and demand it not stop there; authoritative arrears live in the vendor-linked AP bill (no CustomerRef).
- **L10 Reversal / supersession** — TRIGGERED. "where the eviction really stands today … last I tracked we were about at the hearing stage … whether we have truly filed yet or are still short of that." Forces the current SoR state (owner-approved, JP coordination, NOT filed) over the superseded "active payment plan" / "awaiting sign-off" frames.
- **L1 Latching** — TRIGGERED. Stale "about at the hearing stage" recollection + "confirm we have the owner's authorization on file" surface the older Linear "hearing set / favorable ruling / Harris property" framing the agent must not anchor on, and force owner = Linda Castillo (not Harry Harris).
- **L11 Net-vs-gross / sign** — TRIGGERED. "the clean number and we are not double-counting any credit or adjustment that got applied" is the explicit disposition directive that separates net 1832 from stored-gross 2132 (the $150 "credit" stored as a positive).
- **L31 Negative-directive omission (Gemini differentiator)** — TRIGGERED. "whether we are clear to get her unit back into make-ready … or whether it has to hold. I don't want the crew mobilizing on a unit they can't touch yet, or us marketing something we can't actually deliver" + "reflect the real current state" + owner email covering "whether we can touch the unit yet" force the explicit prohibition (do NOT begin make-ready / do NOT market — possession not returned) that Gemini characteristically omits.

**All 5 levers still triggered. No HARDNESS_REGRESSION.**

---

## [B5] Tool-leak / phrasing scan

No function/tool names, no MCP-server names, no internal record/doc/ticket IDs, no em/en/figure dashes, no "at least N" without mandate, no "approximately", and **no exact arrears figure** (the correct net is derived, never printed). "QuickBooks", "make-ready channel", "email", "re-lease" are permitted natural references per the format card. **No hits.**

---

## [B6] Upstream propagation

- Hardness_Plan lever selection: all 5 levers grounded in re-verified records; independence (discovery/disposition/anchor/supersession) holds. No flag.
- Universe data: designed-conflict-with-determinable-truth; no incoherent-that-breaks-solvability edit. No flag.
- **Non-blocking observation (not a PROPAGATE):** `_aux/Validator_Reports/prompt.md` NOTE resolves relative dates against a stale `2026-06-12` (generic V3 default), while the authoritative per-task anchor is `2026-07-01` (`_aux/Universe_Index/today_horizon.json`, task brief, V4 eval). The prompt itself is correctly aligned to 07-01 (the task is only solvable under 07-01 — owner approval 06-30 and JP filing 07-01 must be past), so this is a validator-note tooling artifact, not a prompt/universe defect. It does not require re-running S1.

**No upstream propagation flags.**

---

## VERDICT: GO

Every applicable QC sub-dim = 5. No adversarial divergence (the Rio Bend unit, $0 invoice, and Harris owner are designed traps with a unique correct end-state, not valid second readings). Per-model density both PASS the StarPM v4 bar (Opus ~49, Gemini ~42; breadth 8 services / 7 at >=5%). All 5 selected levers still surfaced by the prompt's framing. No phrasing/leak hits. No blocking upstream flags (one non-blocking note on a stale validator date default). One minor, non-blocking pin for S2: canonicalize the "eviction ticket" note surface.

```json
{
  "phase": "prompt",
  "council": "B",
  "task_dir": "Tasks/41_6a61a86a3453b3714bdc72ef",
  "verdict": "GO",
  "perspectives": {
    "B1": {
      "status": "PASS",
      "findings": []
    },
    "B2": {
      "status": "PASS",
      "findings": [
        {
          "severity": "MINOR",
          "location": "prompt:para5 'Leave a short note on the eviction ticket'",
          "issue": "Note surface (Linear eviction issue vs Airtable EVF-2026-014) slightly open; note content identical either way (immaterial per UGT precision guardrail).",
          "fix": "Pin the canonical eviction-ticket target in the OE phase (Hardness_Plan projects Linear save_comment on the eviction issue).",
          "propagate_to": null
        }
      ]
    },
    "B3": {
      "status": "PASS",
      "findings": []
    },
    "B4": {
      "status": "PASS",
      "findings": []
    },
    "B6": {
      "status": "PASS",
      "findings": [
        {
          "severity": "NOTE",
          "location": "_aux/Validator_Reports/prompt.md NOTE (relative-date anchor)",
          "issue": "Validator note resolves dates against stale 2026-06-12 (V3 default); authoritative per-task universe today is 2026-07-01. Prompt itself is correctly aligned to 07-01.",
          "fix": "Tooling-only: correct the validator's date-anchor default for V4 StarPM tasks; no prompt change and no S1 re-run required.",
          "propagate_to": null
        }
      ]
    }
  },
  "scores": {
    "unique_ground_truth": { "score": 5, "scheme": "1/3/5", "reason": "single end-state per ask; balance=net-of-applied-credit, eviction=owner-approved/JP-coordination/not-filed, unit=hold; no file-vs-defer" },
    "feasibility": { "score": 5, "scheme": "1/3/5", "reason": "all asks actionable with StarPM tools; gmail draft-only matches 'draft me an email … before it goes'" },
    "explicit_tool_mention": { "score": 5, "scheme": "1/5", "reason": "no function/MCP names; only natural product/channel references" },
    "clarity_specificity": { "score": 5, "scheme": "1/3/5", "reason": "four determinate writes; no write-vs-no-write ambiguity" },
    "contrived_unnatural": { "score": 5, "scheme": "1/3/5", "reason": "natural owner-brief message; organic difficulty" },
    "truthfulness": { "score": 5, "scheme": "1/3/5", "reason": "stale beliefs are hedged recollections to verify, not asserted facts; all entities grounded" },
    "tool_use_cross_service": { "score": 5, "scheme": "1/5", "reason": "facts scattered across 8 services, must be reconciled" },
    "investigation_action": { "score": 5, "scheme": "1/5", "reason": "investigation feeds four writes" },
    "coherence_bolt_on": { "score": 5, "scheme": "1/5", "reason": "all asks tie to the single owner-brief situation" },
    "persona": { "score": 5, "scheme": "1/3/5", "reason": "Lisa Smith Onsite PM owns the Tanya scenario + make-ready; voice matches" },
    "business_function": { "score": 5, "scheme": "3/5", "reason": "core Property Operations (BF1): delinquency/eviction/unit-turn owner brief" },
    "alignment_with_date": { "score": 5, "scheme": "1/3/5", "reason": "current state aligns to universe today 2026-07-01; relative phrasing resolves cleanly" },
    "universe_data_exists": { "score": 5, "scheme": "1/5", "reason": "every load-bearing record re-queried and present" },
    "universe_cross_service_coherence": { "score": 5, "scheme": "1/5", "reason": "designed conflicts with a determinable ground truth; not misaligned-data fail" }
  },
  "density_projection": {
    "midpoint": 49,
    "band": "PASS",
    "opus_midpoint": 49,
    "opus_band": "PASS",
    "gemini_midpoint": 42,
    "gemini_band": "PASS",
    "breadth_services": 8,
    "breadth_band": "PASS"
  },
  "lever_preservation": {
    "expected": 5,
    "preserved": 5,
    "missing": []
  },
  "bucket_1_risk_pct": null,
  "iteration": 1,
  "timestamp": "2026-07-24T12:05:00-05:00"
}
```
