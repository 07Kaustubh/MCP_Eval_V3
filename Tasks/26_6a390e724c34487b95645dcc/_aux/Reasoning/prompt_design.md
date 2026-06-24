# S1 Prompt Design Report — Task 26_6a390e724c34487b95645dcc

## Persona / Business Function

- Tom Chang, Tax Associate (approachable, fairly concise, moderately formal, straightforward working style focused on task completion).
- Tax: federal + multi-state returns, stale-SLA reminders, partnership / sales-tax cycles, BlackLine exception triage, Records Vault tax memos.

## Situation engineered into the prompt

The morning of 2026-06-12. Hannah Grant has just informed Tom that William White cleared the Northstar Legal FY2025 Step 3 partner package last night (email_scen_068_*_0008, reply to _0006), including authorization for a closed-period SALT late-post on northstar_legal_FP-2025-12. Tom wants the close put to bed before the partner signature lands. He has two other stale items parked on his queue: exc_652c0931bb2546 (his own June 1 dismissal-recommendation email to Daniel went past the June 2 SLA without reply) and exc_151b0bee7e374e (stale-SLA tickler still firing on a Brookfield item closed in August 2025; March partner-level dismissal authorization from James Randall + Matthew Li sits two replies deep).

## Levers engineered

| # | Lever | How surfaced in the prompt |
|---|---|---|
| L1 | Latching | Hannah messaged William cleared the package; "ready for the partner signature"; "e-file path shouldn't be sitting behind accrual housekeeping" — the persona's framing reads "close is done". |
| L2 | Structured-DB skip | "Before staging anything I want the shortfall traced back through our own records on the Northstar side so the number we book is one we can ourselves stand behind, not one we copied off the messaging trail." Forces GL query against account 230000 northstar + tax-reserve cash movement rather than lifting $4,820.30 from slack. |
| L8 | Multi-link chain (4 hops) | A: trace ledger figure; B: stage closed-period entry on Northstar December period; C: bind to William's reply as authorization basis; D: file restricted-classification, long tax-retention memo tied to the entry; then notify Hannah and William. |
| L9 | Universe-grounded gotcha | Persona says "Jones and I had landed on dismissing under materiality. I want that actually pushed through" — contradicts the BlackLine `proposed_resolution="Reclassify to the correct cost center via standard 4-eyes approval"` on exc_652c0931bb2546. Agent must independently query the BL record and override the persona. |
| L10 | Reversal / supersession via L25 anchor | Deliberate omission of any mention of `doc_8f821bbad10c4eb4` "Northstar Legal FY2025 Federal Form 1065 + State Returns - Signed/E-Filed" (107-byte stub uploaded 2026-06-12 09:30 by persona_027). Agent will encounter this during vault discovery and must recognize the underlying late-post JE has NOT yet been booked, then proceed to stage rather than defer. |

## Expected stump targets (from Hardness Plan)

1. **[HIGH]** Agent fails to stage the closed-period SALT late-post (DR 530000 / CR 230000, $4,820.30, `late_post_authorization_id` = `email_scen_068_northstar_annual_corp_tax_0008`) because doc_8f821bbad10c4eb4 reads as "filing complete". L25 mechanism.
2. **[HIGH]** Agent endorses dismissal of exc_652c0931bb2546 rather than executing the BlackLine `proposed_resolution=Reclassify`. L9 + L27 mechanism.
3. **[MED]** Agent lifts $4,820.30 from slack ts=1781119800 verbatim without GL triangulation. L13 + L11 mechanism.
4. **[MED]** Agent chases the orphan stale tickler for exc_151b0bee7e374e as still live despite the March 2026 dismissal trail buried two replies deep in scen_001. L13 + L4 mechanism.

## Council verdicts

| Gate | Verdict | Notes |
|---|---|---|
| Validator (validate.py --phase prompt) | PASS | 0 fails, 0 warns, 4 notes (398 words; "this morning" / "this week" relative dates resolve to universe today 2026-06-12) |
| Council A (Grounding + Convention) | GO | 12/12 concrete claims grounded; 0 convention drift; 0 IDs / em-dashes / tool names / pre-solving |
| Council B (Adversarial QC + Density + Hardness) | GO | Every applicable QC sub-dim 5/5; no adversarial alt-path divergence (dismiss-vs-reclass is the intended L9 trap, not a defect); projected ~54 tool calls; all 5 levers preserved; 0 phrasing hits; no PROPAGATE-TO-HARDNESS flag |

## Similarity gate

| Metric | Value |
|---|---|
| Top match | Tasks/11_6a2d0b401b5f42afec452859/5_Prompt.txt |
| Top score | 5.5 |
| Threshold band | < 30 PASS (well below 30 WARN, well below 40 ceiling) |

## Strict veteran AUDIT

| Lens | Result |
|---|---|
| LENS 1 Strict QC scoring | 13/13 sub-dims at 5 under strictest reading |
| LENS 2 Answer-leakage sweep | 0 BLOCKERs (no figure, no doc id, no "Reclassify", no account / period leaks) |
| LENS 3 Hardness end-to-end trace | All 5 levers surface with cited prompt sentences + Fact_Ledger atoms; 0 HARDNESS_REGRESSION |
| LENS 4 Strict density projection | Strict midpoint ~49-52, council midpoint 54, plan midpoint 52 — holds above 50 floor |
| LENS 5 Adversarial veteran review | Framing preserved, entity separation clean, no escape valve neutralizing L10, polling-bug Linear discoverable via scen_001 reply chain |

**AUDIT verdict: PASS (STRICT).**

## Density target

Hardness Plan midpoint 52; Council B projection 54; AUDIT strict midpoint 49-52. Comfortably above the 40-call maximalism floor.

## Write actions (6 across 6 services)

1. Oracle GL — closed-period JE staging on northstar_legal_FP-2025-12 with `late_post_authorization_id`.
2. Records Vault — restricted-classification, IRS_TAX_7Y retention support memo tied to the staged JE.
3. Email — audit-trail email to Hannah and William confirming booking is live + package can circulate.
4. BlackLine — exception update on exc_652c0931bb2546 (reclassification per `proposed_resolution`, not dismissal).
5. Reminder — clear the stale tickler on exc_151b0bee7e374e.
6. Slack — confirmation post in #tax-prep-and-filings (C006).
7. Linear — follow-up note on the polling-bug ops ticket per Matthew Li's escalation ask.

## Forward notes for downstream phases (non-blocking; flagged by Council B + AUDIT)

- S2/S3 encode `late_post_authorization_id` binding = `email_scen_068_northstar_annual_corp_tax_0008`.
- S2/S3 encode exc_652c0931bb2546 disposition = reclassify (per `proposed_resolution`), not dismiss (persona-stated).
- S2/S3 pair the $4,820.30 figure with GL evidence from 230000 northstar + 103000 cash tax reserve, not slack chatter.
- S2/S3 encode that doc_8f821bbad10c4eb4 is the L25 anchor — agent must proceed to stage the JE despite encountering this stub.
- S2/S3 allow find-or-create for the polling-bug Linear ticket (Matthew Li's email mentions the ops ticket but no exact issue id is named in the universe).
