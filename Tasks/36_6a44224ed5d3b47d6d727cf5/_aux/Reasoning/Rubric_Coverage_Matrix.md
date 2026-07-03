# Rubric Coverage Matrix — Task 36

**AUDIT verdict:** `PASS (STRICT)` (see `_aux/Council_Reports/AUDIT_rubrics.md`)
**Councils:** Council A grounding = GO, Council B adversarial = GO (5/5 all sub-dims), density midpoint 51 ≥ 50 design target
**Validator:** PASS (0 fails, 5 informational WARNs)
**Rubric count:** 34 outcome, 0 process (all 4 V3 references have 0 process → baseline preserved)

## Forward map — prompt sentence → OE step(s) → rubric(s)

| # | Prompt sentence / ask | OE step(s) | Rubric(s) |
|---|---|---|---|
| 1 | "Email her back, cc Mina" (Simone) | OE 18 | R1 (1.1 send) |
| 2 | Simone needs a real answer today, not another 'reviewing your file' note | OE 18 | R2 (1.2 mismatch confirmed with UrbanNest) |
| 3 | Simone recovery reflects escalation-in-flight | OE 18 | R3 (1.2 escalation to Carmen with same-day response) |
| 4 | "figure out whether a same-unit-type transfer is available and what the swing on our account is" | OE 4, OE 5, OE 18 | R4 (1.2 transfer availability + swing pending Carmen) |
| 5 | "If she still owes us one, escalate plainly by email, do not just send another gentle nudge" | OE 19 | R5 (1.1 escalation send) |
| 6 | Restate the six specific questions | OE 4, OE 19 | R6 (1.2 six questions restated) |
| 7 | Escalation posture + same-day response | OE 19 | R7 (1.2 same-day requirement + escalation framing) |
| 8 | "update her Airtable placement record so anyone reading it can see this is live and not resolved" | OE 20 | R8 (1.1 record update), R9 (1.2 Status In Progress preserved), R10 (1.2 Special Requirements content) |
| 9 | "email him a concrete next checkpoint, cc Mina" (Marcus) | OE 21 | R11 (1.1 send) |
| 10 | Current position (Indianapolis stall + April 11 driver called off) | OE 8, OE 21 | R12 (1.2 Indianapolis + April 11 stall) |
| 11 | Concrete next checkpoint (April 18 to April 20 window) | OE 8, OE 21 | R13 (1.2 revised window) |
| 12 | "If the carrier still cannot give a hard delivery date, say that. Do not soften it." | OE 21 | R14 (1.2 no-hard-date + driver reassignment, no softening) |
| 13 | "reflect the actual state on his Airtable placement record" (Marcus) | OE 22 | R15 (1.1 record update), R16 (1.2 Status In Progress preserved), R17 (1.2 Special Requirements content) |
| 14 | "put the Slack status update on the audit thread Mina raised Thursday, not in a fresh post" | OE 12, OE 13, OE 23 | R18 (1.1 canonical thread_ts 1776997200.000000 on #customer-engagement / C002) |
| 15 | Slack payload covers Simone recovery state | OE 23 | R19 (1.2 Simone Slack content) |
| 16 | Slack payload covers Marcus recovery state | OE 23 | R20 (1.2 Marcus Slack content) |
| 17 | "Add a Linear comment on the BrightLoop operational issue that captures where each employee stands" | OE 14, OE 24 | R21 (1.1 comment on linear_issue_f85be674c9b8), R22 (1.2 Simone stands), R23 (1.2 Marcus stands) |
| 18 | "what the money impact looks like on the batch" | OE 11, OE 24 | R24 (1.2 INV-2026-0308 total ~$11,350) |
| 19 | Per-employee finance breakout ("finance side of these two moves is not something I can answer with feelings") | OE 11, OE 24 | R25 (1.2 line-item breakout $4,500 base + $750 rush + $4,500 base + $1,100 vehicle) |
| 20 | "Update the BrightLoop engagement on our CRM so it stops reading like the April cohort is basically done" | OE 16, OE 25 | R26 (1.1 create new NOTE engagement) |
| 21 | CRM correction — cohort not closed | OE 25 | R27 (1.2 April cohort not closed) |
| 22 | CRM correction — Simone in wrong unit awaiting UrbanNest | OE 25 | R28 (1.2 Simone still in wrong unit) |
| 23 | CRM correction — Marcus stalled at Indianapolis | OE 25 | R29 (1.2 Marcus stalled + window + no hard date) |
| 24 | "Hold thirty minutes on my calendar late Tuesday to recheck Simone's housing outcome" | OE 26 | R30 (1.1 30-min April 28 hold with Julian attendee) |
| 25 | "send Mina a short internal email pulling the whole position together in one place" | OE 27 | R31 (1.1 send internal email) |
| 26 | Internal email covers Simone position | OE 27 | R32 (1.2 Simone internal summary) |
| 27 | Internal email covers Marcus position | OE 27 | R33 (1.2 Marcus internal summary) |
| 28 | Internal email covers internal-actions bundle (Slack + Linear + CRM + calendar) | OE 27 | R34 (1.2 internal actions summary with $11,350 impact) |

**Forward map coverage:** 28/28 prompt asks map to at least one rubric. No gaps.

## Reverse map — rubric → prompt sentence

Every one of the 34 rubrics traces back to a prompt sentence via the forward map above. No surplus. Verified by Council B Sweep 2 (34/34 clean) and AUDIT Lens 7 (34/34 clean).

## Hardness lever coverage — Council B B4 / AUDIT Lens 3

| Lever | Mechanism | Covering rubric(s) |
|---|---|---|
| L25 — Existing-output anchor trap | Julian's 4/23 apology+promise is not the answer; rubric requires factual delivery, not paraphrase | R2 (factually confirmed with UrbanNest), R6 (restates the six questions), R12/R13/R14 (specific vehicle-state facts, not the 4/23 promise) |
| L9 — Authority self-anchor dismissal | Airtable Special Requirements silent on unit type; rubric forces the mismatch to surface in the record | R10 (Simone Special Requirements text with mismatch), R17 (Marcus Special Requirements text with stall), R24/R25 (Linear finance impact from QB invoice, not from feelings) |
| L26 — Decoy parent thread | Rubric locks to canonical thread_ts 1776997200.000000; Julian's C007 orphan (1777011000) + C002 "Drafted and sent" (1777012200) are decoys | R18 (canonical thread_ts exact-match, fresh post rejected) |
| L2 — Airtable-silence + QB-invoice skip | Simone unit-type claim lives only in email/Slack chatter; QB invoice is off-domain for Customer Support | R10 (Simone Airtable Special Requirements), R17 (Marcus Airtable Special Requirements), R24 (INV-2026-0308 $11,350), R25 (line-item math from invoice) |
| L8 — Three-service emergent (Airtable + email + QB) | Truthful answer requires cross-service triangulation | R2 (email evidence) + R10 (Airtable) + R25 (QB invoice) stack forms the 3-service triangulation the levers demand |

**Lever coverage:** 5/5. Every lever traversed by at least one Outcome rubric whose pass/fail depends on the lever mechanism.

## Persona attribution triple-lock — AUDIT Lens 9

| Persona | Correct binding (positive-locked) | Wrong bindings (implicitly rejected) |
|---|---|---|
| Simone Richter | simone.richter@brightloopanalytics.com (R1) | simone.richter@stormcloud.io |
| Marcus Webb | marcus.webb@brightloopanalytics.com (R11) | m.webb@ironcladsec.com, marcus.webb.lab@gmail.com, marcus.thorne@moveops.com |
| Carmen Reyes | carmen.reyes@urbannestsolutions.com (R5) | carmen.delgado-reyes@palmettofoundation.org |
| Julian Brooks | julian.brooks@moveops.com (R1/R5/R11/R31 sender + R30 attendee) | n/a |
| Mina Hashimoto | mina.hashimoto@moveops.com (R1/R5/R11 CC + R31 recipient) | n/a |

Bonus 9th disambiguation surfaced by AUDIT: 5th Marcus Webb (Canopy Health Lab Research Associate, name-only, no email) — auto-rejected by exact-email positive lock; no rubric change needed.

## Density projection — Council B B3 / AUDIT Lens 8

| Component | Count |
|---|---:|
| Base discovery (contacts, initial reads) | 6-8 |
| Email chain reads (Julian's 3× 4/23 outbounds + Simone parent + Marcus originals + Road Runner delay) | 6-8 |
| Airtable reads (2 records) | 2 |
| Airtable base list | 1 |
| QuickBooks invoice read | 1 |
| Slack multi-probe enumeration + parent verify | 4-6 |
| Linear reads (ops-gaps + sister audit) | 2 |
| CRM engagement + contact lookups | 3-5 |
| **10 write actions** | 10 |
| Cross-service verification buffer | 5-7 |
| **Total range** | **40-56** |
| **Realistic midpoint** | **51** |

**Verdict:** PASS (>= 50 design target). Council B: 51. Hardness_Plan: 50. AUDIT: 52. Convergent.

## Exit criteria checklist

- [x] `7_Rubrics.json` exists, 34 outcome rubrics, 0 process, all agent-centric titles
- [x] Validator PASS (0 fails)
- [x] Council A GO (all 9 grounding perspectives clean)
- [x] Council B GO (5/5 all sub-dims, zero adversarial hits)
- [x] Council B-B3 density midpoint 51 ≥ 50 design target
- [x] Council B-B4 all 5 hardness levers covered by ≥ 1 Outcome rubric
- [x] AUDIT PASS (STRICT) — 9-lens sweep clean, no PROPAGATE flags
- [x] Coverage matrix (this file)
