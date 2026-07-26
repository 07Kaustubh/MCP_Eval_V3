# OE Solvability + Coverage Report — S2 — Tasks/41_6a61a86a3453b3714bdc72ef

**Universe:** StarPM V4 · **Persona:** Patricia Nguyen (Onsite Property Manager) · **Today:** 2026-07-01.
**Deliverable:** 6_Oracle_Events.txt (18 OEs) · **Gate stack:** validator PASS · atom-verifier PASS · Council A GO · Council B GO · AUDIT PASS (STRICT).

## OE-to-prompt coverage map (forward: every prompt ask -> OE)

| Prompt ask | OE(s) | Type |
|---|---|---|
| "what Tanya genuinely owes us right now ... checked against what is actually in QuickBooks" | OE 2, OE 3, OE 4 | Discovery (customer -> paid-invoice decoy -> authoritative AP bill) |
| "walk it back to the underlying charges ... the clean number ... not double-counting any credit or adjustment" | OE 5 | Discovery + derivation (net 1832 = 1982 charges - 150 credit; reject 2132 gross / 0 paid) |
| "where the eviction really stands today ... the current picture" | OE 6, 7, 8, 9, 10, 12, 13 | Discovery (Airtable SoR + supersession chain + tickets + Slack current-status + Linear ticket) |
| "whether we have truly filed the petition yet or are still short of that" | OE 8, OE 12 | Discovery (SoR note + Slack: JP coordination, petition NOT filed) |
| "confirm we have the owner's authorization on file the way we should" | OE 10, OE 11 | Discovery (EVF-2026-014 owner-approved + Gmail owner-auth reply, Linda Castillo) |
| "whether we are clear to release her unit back for make-ready, or whether it has to hold" | OE 8, OE 14 | Discovery + write (HOLD: possession not returned) |
| "get our make-ready record for the unit updated to the real current state" | OE 14 | WRITE 1 (Airtable update_records_for_table recc83c05d889b354) |
| "Leave a short note on the eviction ticket so the trail is current" | OE 15 | WRITE 2 (Linear save_comment OPS-32; EVF-2026-014 alt) |
| "Drop the make-ready team a heads-up in our channel" | OE 16 | WRITE 3 (Slack slack_send_message C004 #make-ready) |
| "draft me an email to the owner covering the balance, the eviction status, and whether we can touch the unit yet" | OE 17 | WRITE 4 (Gmail create_draft -> linda.castillo@gmail.com, draft-only) |
| "If anything I've assumed here turns out to be off, tell me plainly" | OE 18 | Final response (corrects stale beliefs: not "squared away"; not "at hearing stage") |

Reverse coverage: every OE maps to a real prompt ask. OE 1 (identity resolution) supports the owner draft + grounding. No OE goes beyond the prompt. ESA/reasonable-accommodation is EXCLUDED (out of Patricia's rent/eviction lane; the prompt never raises it) — confirmed non-scope-creep by Council B + AUDIT.

## OE-to-rubric mapping preview (drives S3)

| OE | Becomes | Rationale |
|---|---|---|
| OE 14 (Airtable make-ready update) | Outcome 1.1 + 1.2 | Write result + content (held at Scheduled, not advanced; possession-not-returned note; correct Sunset Ridge record, not Rio Bend) |
| OE 15 (Linear eviction-ticket note) | Outcome 1.1 + 1.2 | Write result + content (current status: delinquent/breached, net owed, owner-approved but petition not filed, hold) |
| OE 16 (Slack #make-ready post) | Outcome 1.1 + 1.2 | Write result + content (active eviction, HOLD, do-not-mobilize / do-not-market) |
| OE 17 (Gmail owner draft) | Outcome 1.1 + 1.2 | Draft-created to linda.castillo@gmail.com + content (balance 1832 net, eviction status, unit-touchability) |
| OE 5 net figure ($1,832) | Outcome 2.1 | "what Tanya genuinely owes" — the clean derived number reported to the persona |
| Eviction current state (petition not filed; owner auth on file, Linda Castillo) | Outcome 2.1 | "where the eviction really stands" + "confirm the owner's authorization" |
| Make-ready release decision (must HOLD) | Outcome 2.1 | "whether we are clear to release ... or hold" + explicit do-not-begin / do-not-market (L31 negative directive) |
| Corrected stale assumptions | Outcome 2.1 | "if anything I've assumed is off, tell me plainly" |
| OE 1-13 (reads/lookups) | Usually NO rubric | Downstream Outcomes prove the reads happened; no ordering-Process rubric warranted (three-condition test fails — the tightened Outcomes capture the requirement) |

**S3 carry (from AUDIT, forward NOTE — not an OE defect):** OE 15/17/18 bundle "owner-approved (EVF-2026-014)" and "petition-not-filed / JP-coordination" — facts sourced from DIFFERENT records. At S3, split these into separate Outcome 1.2 / 2.1 criteria and demote the EVF-2026-014 id to optional grounding (atomic-rubric guidance, Learnings 5/7/8). Also: OE 14/15/17/18 carry the L31 negative-directive ("do NOT begin make-ready / do NOT market") — S3 must include a rubric that FAILS if the deliverable omits the explicit prohibition (the Gemini differentiator).

## Hardness lever end-to-end preservation (Council B-B4 + AUDIT Lens 3)

| Lever | Prompt sentence | OE exercising it | Atom the agent must touch |
|---|---|---|---|
| L2 structured-DB skip (flagship) | "what Tanya genuinely owes ... in QuickBooks" | OE 3 (invoice decoy) + OE 4 (AP bill) | AP bill 232176553533 (VendorRef Alamo HVAC, no CustomerRef) vs invoice 7214 Balance 0 |
| L10 supersession | "where the eviction really stands today ... real current state, not the stale note" | OE 8 + OE 9 + OE 12 | recc83c05d889b354 (JP coordination) over rec769c9f03f0b85f (active plan) |
| L1 latching | "last I tracked it we were about at the hearing stage" | OE 12 + OE 13 | OPS-32 "Harris Property / hearing" + Slack court-stage decoys vs SoR |
| L11 net-vs-gross / sign | "not double-counting any credit or adjustment" | OE 5 | bill line 4 (150 credit) sign; 1832 net vs 2132 stored |
| L31 negative-directive omission | "whether we are clear to release ... or whether it has to hold ... whether we can touch the unit yet" | OE 14/16/17/18 | recc83c05d889b354 note "cannot begin until possession formally returned" |
| L6 near-miss (stacked) | "the Tanya Mitchell ... Unit 14" | OE 1 + OE 7 | Rio Bend Unit 14 rec94e86a3007dd5e / owner Castillo-vs-Harris / catch-all customer proj-2e48c594aab7 |

## Density + solvability

- Per-model density (StarPM v4 bar, midpoint >=40 PASS): Opus ~47-48 PASS · Gemini ~42-43 PASS. Both clear the >=40 floor; the V3 50/40 scheme deliberately not applied.
- Service breadth: 6 distinct services actually exercised (airtable, quickbooks, slack, gmail, linear, contacts), each >=5% -> PASS. (Hardness_Plan's 8-service projection over-counted hubspot + gcalendar, which the OE chain does not touch. Non-blocking; reconcile at FINAL.)
- End-to-end solvable: every dependency-chain source row is materialized in _aux/Universe_Split/ (Council A A11 + AUDIT).

## AUDIT verdict

**PASS (STRICT)** — `_aux/Council_Reports/AUDIT_oe.md`. OE Completeness 5/5, OE Accuracy 5/5 (per-atom evidence table, zero discrepancies); answer-leakage sweep clean (net 1832 in no universe record); all 5 levers + L6 trace prompt -> OE -> atom; regression 62/62; validator 0/0. No PROPAGATE-to-S1. One forward carry to S3 (content-rubric split), recorded above.
