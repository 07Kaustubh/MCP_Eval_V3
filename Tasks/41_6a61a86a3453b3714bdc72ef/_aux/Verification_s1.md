# Cross-Source Verification — S1 (prompt) — Tasks/41_6a61a86a3453b3714bdc72ef

## Sources consulted
- Per-task data :: _aux/Universe_Split/ :: grounded Lisa Smith (contacts, lisa.smith@starpm.com/p_002), Tanya Mitchell (contacts + QB CustomerRef proj-2e48c594aab7), the owner Linda Castillo (airtable rec922b9a2d1b9451 / EVF-2026-014), current eviction SoR (airtable recc83c05d889b354, JP coordination / make-ready cannot begin), arrears records (QB AR invoice 283231782926 = DocNumber 7214 Balance $0 decoy; AP bill 232176553533 = QR-2026-0441 Balance $2,132, VendorRef Alamo HVAC, no CustomerRef), stale latching framing (linear OPS-32/38/54 + gcalendar Harris hearing), Rio Bend Unit 14 near-miss (airtable rec94e86a3007dd5e), Slack #make-ready C004.
- Per-task data :: _aux/Fact_Ledger.json :: confirmed prompt asserts NO dollar figures and NO internal IDs verbatim; correct arrears ($2,132 / $1,832 net / $1,982 charges-only) never appears; net figure not stored anywhere in QuickBooks (must be derived).
- Per-task data :: _aux/Hardness_Plan.md :: all 5 selected levers (L2 flagship, L10, L1, L11, L31) preserved in prompt framing; density projection matched by councils.
- Eval spec :: Evals_starpm/1_Prompt_Eval.md :: sub-dims 1.1-1.12 scored (per-sub-dim detail in the "Eval spec sub-dims" section below).
- QC spec :: Docs_starpm/7_QC_Spec_Doc1.json (Prompt dimension) :: all applicable Prompt sub-dims 5/5 (detail in the "QC spec sub-dims" section below).

## Eval spec sub-dims (Evals_starpm/1_Prompt_Eval.md) verified
- 1.1 Unique Ground Truth :: PASS — "Tanya Mitchell" anchor uniquely disambiguates the cross-property Unit 14 near-miss; every ask resolves to a single end-state (Council A A7, Council B B2, AUDIT L1/L5).
- 1.2 Feasibility :: PASS — full dependency chain materialized in Universe_Split; no impossible-future ask (today 2026-07-01; all records present).
- 1.3 Explicit Tool Mention :: PASS — no tool/function/MCP-server names; "QuickBooks / make-ready channel / email" are natural product references permitted by the format card.
- 1.4 Prompt Clarity and Specificity :: PASS — persona intent recoverable from the prompt alone; no MAJOR clarity gap (Council A A7).
- 1.5 Contrived / Unnatural Prompts :: PASS — mid-thought, first-person, warm-professional; stale beliefs hedged as recollection; no artificial precision or format constraints.
- 1.6 Truthfulness :: PASS — every claim grounded; stale beliefs framed as hedged recollection grounded in real (superseded) records, not asserted current fact (Council A A3, AUDIT per-atom table).
- 1.7 Tool use and Cross-service requirement :: PASS — spans QuickBooks + Airtable + Linear + Slack + Gmail; 8 services in projected trajectory (7 at >=5%).
- 1.8 Investigation :: PASS — broad investigative asks ("figure out what she owes", "find out where the eviction really stands") plus action; both phases present.
- 1.9 Coherence :: PASS — one situation (the owner brief); sentence-removal test clean, no bolt-ons.
- 1.10 Persona :: PASS — Lisa Smith (Onsite PM) leads the Tanya scenario; voice matches PersonaBrief; scope in-bounds (Council A A6).
- 1.11 Business Function :: PASS — Property Operations (BF1) match=true (Council A A10).
- 1.12 Alignment with Today's Date :: PASS — relative phrasing ("a few weeks stale", "a while ago", "right now", "today") coherent with 2026-07-01; resolved windows contain universe records. (Validator NOTE shows stale 2026-06-12 V3 default — tooling artifact; the authoritative anchor is 2026-07-01.)

## QC spec sub-dims (Docs_starpm/7_QC_Spec_Doc1.json — Prompt dimension) verified
- All applicable Prompt sub-dims scored 1/3/5 per the scheme map in Reference/Council_Protocol.md: Council B = 14/14 at 5/5; AUDIT strict = 14/14 at 5/5 (NON-FAIL middle bands not invoked).

## Reference docs consulted
- Reference/Prompt_Format.md :: voice, anti-patterns, 500-word cap re-checked; 399 words, no em/en dashes, no headings/bullets, closing write cluster on-convention.

## Verification statements
- [x] Validator (validate.py --phase prompt) exit 0. (0 fails, 0 warns, 5 notes)
- [x] Council A grounding + convention clean (zero ungrounded claims, zero convention drift).
- [x] Council B QC scoring shows every applicable sub-dim >= 5 (14/14 at 5/5; no bands invoked).
- [x] Similarity gate (calc_similarity.py) composite < 40. (max 30.6; < 35 near-pivot threshold)
- [x] AUDIT verdict = PASS (STRICT). (_aux/Council_Reports/AUDIT_prompt.md)
- [x] Regression-anchor suite executed: 62/62 PASS. Atom verifier: 0 fails / 0 warns.

## Discrepancies surfaced (if any)
- None blocking. Two non-blocking items routed forward to S2 (OE phase): (1) pin the canonical "eviction ticket" note surface (Linear issue OPS-32 vs Airtable EVF-2026-014 — identical content either way); (2) the validator's relative-date NOTE prints a stale 2026-06-12 V3 default while the authoritative per-task anchor is 2026-07-01 (tooling artifact; the prompt itself is correctly date-aligned).

## Verdict
- PASS — every box checked; no blocking discrepancy. S1 prompt cleared through validator + Council A + Council B + similarity + strict AUDIT.
