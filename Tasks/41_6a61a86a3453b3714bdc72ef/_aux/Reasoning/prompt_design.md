# S1 Prompt Design Record — Tasks/41_6a61a86a3453b3714bdc72ef

**Persona:** Patricia Nguyen, Onsite Property Manager (p_010, patricia.nguyen@starpm.com) · **Business Function:** Property Operations (BF1) · **Universe:** StarPM V4 (dual-model Opus 4.8 + Gemini) · **Universe today:** 2026-07-01.

> **S1.5 persona reassignment.** Originally authored for Lisa Smith (p_002). The platform persona linter flagged scope drift, and re-check confirmed it: the rent/eviction lifecycle, QuickBooks delinquency ledger, filing package, and owner-authorization confirmation are Patricia Nguyen's anchored territory (she leads all five rent/eviction scenarios); Lisa's only Tanya Mitchell scenario is the ESA accommodation, which is legally independent of the delinquency. Reassigned to Patricia — same Business Function (BF1 Onsite PM), all five levers preserved and now landing on the persona who owns the workstream. See `_aux/Linter_Decision.md`.

## Situation engineered
Patricia is closing out the filing package on the Tanya Mitchell (Unit 14) delinquency/eviction — the balance and case status that go into the court file and in front of the owner. She carries a STALE, reassuring picture (back rent "mostly squared away" after the payment plan she herself set up; eviction "about at the hearing stage") and asks the agent to verify and correct it before it moves, then execute the record/ticket/channel/owner-draft writes. Her mistaken beliefs are hedged as uncertain recollections ("last I tracked it", "I was under the impression", "I don't trust my own memory"), each grounded in a real but superseded universe record, so the traps fire without a truthfulness violation and without pre-solving.

## Levers engineered into the prompt (5 selected)
- **L2 Structured-DB skip (flagship).** "what Tanya genuinely owes us right now ... checked against what is actually in QuickBooks ... the real outstanding figure for the filing package." Findable AR invoice 7214 (Balance $0, paid decoy via payment 952690463873) says "current"; authoritative arrears live in vendor-linked AP bill 232176553533 / QR-2026-0441 (no CustomerRef, invisible to a customer/invoice query).
- **L10 Reversal/supersession.** "where the eviction really stands today ... the current picture" + "update the make-ready record to the real current state, not the stale note." Forces the current Airtable SoR (recc83c05d889b354: JP coordination, petition not filed) over the reassuring superseded states (active payment plan / awaiting sign-off).
- **L1 Latching.** "last I tracked it we were about at the hearing stage" seeds the older, more-findable Linear/calendar "hearing set / favorable ruling / Harris property" framing; "whether we have truly filed yet" + "confirm we have the owner's authorization on file" forces the true state (petition not filed) and the correct owner (Linda Castillo EVF-2026-014, not Harry Harris).
- **L11 Net-vs-gross / sign.** "walk it back to the underlying charges so I know it is the clean number and we are not double-counting any credit or adjustment" forces correct handling of the $150 "credit applied" line stored as a positive ($2,132 stored vs $1,832 net).
- **L31 Negative-directive omission (Gemini differentiator).** "whether we are clear to get her unit back into make-ready ... or whether it has to hold" + "whether we can touch the unit yet" forces the deliverable to state the make-ready must NOT begin / not market because possession is not returned.

Stacked/supporting: L6 near-miss (Rio Bend Unit 14 rec94e86a3007dd5e rent-ready decoy; catch-all customer proj-2e48c594aab7; dual owner) disambiguated by anchoring on the tenant "Tanya Mitchell"; L7 multi-write density (Airtable record + Linear ticket note + Slack make-ready channel post + Gmail owner draft = 4 writes across 4 services); L3/L5 missing-reply/thread-reply (owner authorization sits in a reply).

## Expected stump targets
Symmetric (both models): arrears reported as "current/$0" or wrong number (L2); eviction reported "at hearing / owner=Harris" instead of "owner-approved, JP coordination, petition not filed" (L1/L10); $2,132 gross vs $1,832 net (L11). Gemini-asymmetric: omission of the explicit "do not begin make-ready / do not market" prohibition (L31).

## Guardrails honored
No tool/function names, no MCP-server names, no internal IDs, no dollar figures (correct arrears never verbatim), no em/en dashes, first-person mid-thought voice, 397 words (Patricia's firm/factual register). Natural product references (QuickBooks / make-ready channel / email) used to satisfy cross-service floor per format card.

## Gate log

### Validator (validate.py --phase prompt)
PASS — 0 fails, 0 warns, 5 notes. Word count 399 (<= 500, within 300-400 sweet spot).

### Similarity gate (calc_similarity.py)
PASS — max composite **30.6** (< 40 ceiling; < 35 near-pivot threshold).
Top match: Tasks/40_6a614767cd5b60ad96902fb4/5_Prompt.txt (composite 30.6, raw_lex 30.6, mult 1.000) — sibling StarPM task, same universe, expected surface overlap; no structural collision. Next: V3 reference Task14 (29.8). No pivot required.

### Council A — Grounding
**GO** — zero blocking issues. All concrete claims grounded (A1); both stale-belief traps correctly framed as hedged recollection, true SoR state not leaked, zero narrative-state contradictions (A3); four writes within Lisa's authority and respecting the "make-ready cannot begin" prescription (A4); no persona-scope drift (A6); "Tanya Mitchell" anchor uniquely disambiguates the cross-property Unit 14 near-miss, no MAJOR clarity gap (A7); business function match=true (A10); full dependency chain materialized, no solvability break (A11); no convention drift, 0 dollar figures / 0 internal IDs / 0 em-dashes (A2). Report: `_aux/Council_Reports/S1_A_grounding.md`.

### Council B — Adversarial QC
**GO** — no blocking issues. All 14 applicable Prompt QC sub-dims scored 5/5 (re-verified against live Universe_Split records). No adversarial divergence: Rio Bend Unit 14, the $0 paid invoice, and the Harry Harris owner are designed near-miss traps with a unique correct end-state, not valid second readings; "the real outstanding figure for the filing package, walk it back to the underlying charges" forces the AP-bill net derivation, and "confirm we have the owner's authorization on file" resolves uniquely to Linda Castillo / EVF-2026-014. All 5 levers (L2/L10/L1/L11/L31) still surfaced. Leak scan clean. Density PER MODEL: **Opus 4.8 ~49 (PASS)**, **Gemini ~42 (PASS)** — both clear StarPM v4 >=40; breadth 8 services / 7 at >=5% (PASS). Two non-blocking notes for S2: pin canonical eviction-ticket note surface (Linear issue vs Airtable EVF-2026-014); validator relative-date note uses stale 2026-06-12 V3 default (tooling artifact; prompt is correctly aligned to 2026-07-01). Report: `_aux/Council_Reports/S1_B_adversarial.md`.

### Strict veteran AUDIT (--phase prompt)
**PASS (STRICT)** — no blocking issues. All 14 applicable prompt sub-dims 5/5 under strictest interpretation (NON-FAIL bands not invoked); all 5 levers trace to explicit prompt sentences; answer-leakage sweep clean (zero digits/figures/IDs in the prompt; net $1,832 and charges-only $1,982 stored nowhere in QuickBooks, so the figure must be derived across 2+ sources); Lens 8 regression anchors 62/62 PASS. Per-model density Opus ~49 / Gemini ~42 (both >= StarPM v4 40 floor). Two non-blocking items routed to S2 (eviction-ticket note surface; stale validator date default). Report: `_aux/Council_Reports/AUDIT_prompt.md`.

## Final verdict — S1 CLEARED

Levers engineered: L2 structured-DB skip (flagship), L10 reversal/supersession, L1 latching, L11 net-vs-gross/sign, L31 negative-directive omission (Gemini differentiator); stacked L6 near-miss + L7 multi-write + L3/L5 missing-reply.
Expected stump targets: arrears reported "current/$0" or wrong number (symmetric); eviction reported "at hearing / owner=Harris" vs "owner-approved / JP coordination / petition not filed" (symmetric); $2,132 gross vs $1,832 net (symmetric); omission of the explicit "do not begin make-ready / do not market" prohibition (Gemini-asymmetric).
Council verdicts: Validator PASS · Council A GO · Council B GO (14/14 5/5) · Similarity 30.6 PASS · AUDIT PASS (STRICT).
Final similarity: composite 30.6, top match Tasks/40 (sibling StarPM task, same universe). Density per model: Opus ~49 PASS / Gemini ~42 PASS. Breadth 8 services / 7 at >=5% PASS.
All S1 exit criteria met. STOP gate reached — next: platform linter (S1.5 if flagged) then S2 (Oracle Events).

> **Note:** the gate log above (Validator 399 · Council A/B GO "within Lisa's authority" · Similarity 30.6 · AUDIT) is the S1 sign-off for the **superseded Lisa Smith version**. The Council A "no persona-scope drift (A6)" verdict rested on a misread — see S1.5 below.

## S1.5 — Persona linter (Class A misalignment) → reassignment + gate re-run

Platform persona linter returned FALSE on the Lisa version (persona-scope drift: QuickBooks filing-package verification, eviction-lifecycle tracking, owner-authorization confirmation, and owner-email drafting fall outside an Onsite PM's turnover/tenant-coordination lane). Re-check **agreed** (Class A, linter right → revise): issues on QuickBooks/eviction/owner-brief are grounded in the persona briefs and scenario storylines; only the make-ready-record + `#make-ready` ping objection was invalid (those are in-lane) and is rendered moot by the fix. Root cause: Council A A6 quoted "PersonaBrief and Hardness_Plan both state Lisa leads the Tanya Mitchell scenario" — dropping the "ESA accommodation" qualifier; the eviction/delinquency lifecycle is Patricia Nguyen's anchored territory. **Resolution:** reassigned p_002 Lisa → p_010 Patricia (same BF1 Onsite PM), rewrote the prompt in Patricia's firm/factual voice grounding the stale belief in the payment plan she herself set up, all 5 levers preserved. See `_aux/Linter_Decision.md`.

**Post-reassignment gates (re-run):** `validate.py --phase prompt` PASS 0 fails / 0 warns / 5 notes · 397 words · 0 dashes / 0 dollar-figures / 0 internal-IDs · 3 service surface words (QuickBooks / make-ready channel / email). Similarity max composite **28.6** (< 40; top match V3 Task14) — sibling **Tasks/40 dropped 30.6 → 17.8** composite (persona reassignment reduced overlap). Regression anchors 62/62 PASS. All 11 lever/anchor phrases present. Data grounding unchanged (arrears AP-bill derivation, owner Linda Castillo EVF-2026-014, current SoR recc83c05d889b354 — all persona-independent). Councils A/B/AUDIT were not re-run on the Patricia version; the two S2 carries (eviction-ticket note surface; stale validator date default) still apply.
