# OE Solvability — S2 (Task 36)

## AUDIT verdict
- **Round 1:** REVISE (2 BLOCKER-STRICT defects — OE 7 folder mismatch + density 37 midpoint STRICT under floor)
- **Round 2:** **PASS (STRICT)** after 5 in-place fixes (`_aux/Council_Reports/AUDIT_oe_round2.md`)

## Density
- STRICT no-buffer midpoint: 44 (clears 40 floor)
- Realistic-buffer midpoint: ~51 (clears 50 design target)

## OE→Prompt coverage map

| Prompt ask | OE(s) |
|---|---|
| Close BrightLoop recovery before Tessa's Monday weekly | Full chain (OE 1-27) |
| Send Simone + Marcus real updates promised Thursday | OE 18 (Simone), OE 21 (Marcus) |
| Pull booking-vs-delivered picture from email for Simone | OE 2, OE 3, OE 4 |
| Figure out same-unit-type transfer availability + $ swing | OE 4 (six-question basis), OE 5 (verify no reply), OE 11 (credit-math base), OE 19 (escalation) |
| Check if Carmen still owes an answer | OE 5 |
| Escalate plainly by email (not gentle nudge) | OE 19 |
| Email Simone back, cc Mina | OE 18 |
| Update Simone's Airtable placement record | OE 20 |
| Get Marcus current position from Road Runner | OE 8 |
| Email Marcus concrete next checkpoint, cc Mina | OE 21 |
| Do not soften absence of hard delivery date | OE 21 (explicit) |
| Reflect Marcus state on Airtable placement record | OE 22 |
| Slack status update on Mina's audit thread (not fresh post) | OE 12, OE 13, OE 23 |
| Linear comment on BrightLoop operational issue | OE 14, OE 24 |
| Capture where each employee stands + money impact on batch | OE 11, OE 24 |
| Update BrightLoop CRM engagement | OE 16, OE 25 |
| Hold thirty minutes late Tuesday to recheck Simone housing | OE 26 |
| Internal email to Mina pulling whole position together | OE 27 |

## OE→Rubric preview (forward map to S3)

| OE | Type | Rubric class | Notes |
|---|---|---|---|
| 1 | Read (contact anchor) | none | Downstream cc verification lands via Outcome 1.2 on write OEs |
| 2 | Read (Julian outbound anchor) | none | Anti-template signal for S3 |
| 3 | Read (Simone parent thread) | none | Anti-template signal |
| 4 | Read (Carmen outbound + 6-question anchor) | none | Establishes rubric-testable question set |
| 5 | Read + Conclude (no Carmen reply) | none | Discovery gate for OE 19 escalation choice |
| 6 | Read (Julian Marcus outbound anchor) | none | Anti-template |
| 7 | Read (Marcus parent + 2nd follow-up) | none | Silence chain |
| 8 | Read + Conclude (Road Runner state) | none | Discovery gate for OE 21 factual content |
| 9 | Read + Conclude (Airtable Special Requirements silent) | none | L2 anchor |
| 10 | Read + Conclude (Marcus Airtable state) | none | L2 anchor |
| 11 | Read + Conclude (QB $11,350 credit math) | none | Financial-impact anchor |
| 12 | Read + Reject decoys | none | L26 anchor |
| 13 | Read (thread reply state) | none | Verifies OE 23 attach point |
| 14 | Read (Chloe BrightLoop issue) | none | Verifies OE 24 target |
| 15 | Read (Mina audit issue context) | none | Context only |
| 16 | Read + Conclude (CRM create-only) | none | Design constraint |
| 17 | Read + Reject 5 near-miss identities | none | Persona-attribution anchor |
| **18** | **Write — email Simone** | **Outcome 1.1 + 1.2** | 1.2 must gate: cc Mina, factual not apology, UrbanNest escalation state, no verbatim answer |
| **19** | **Write — plain escalation to Carmen** | **Outcome 1.1 + 1.2** | 1.2: 6 questions restated, same-day request, cc Mina |
| **20** | **Write — update Simone Airtable** | **Outcome 1.1 + 1.2** | 1.2: Status stays In Progress, Special Requirements updated to live state |
| **21** | **Write — email Marcus** | **Outcome 1.1 + 1.2** | 1.2: cc Mina, Indianapolis hub, April 18-20 window, no hard-date softening |
| **22** | **Write — update Marcus Airtable** | **Outcome 1.1 + 1.2** | 1.2: Status stays In Progress, Special Requirements updated |
| **23** | **Write — Slack post on audit thread** | **Outcome 1.1 + 1.2** | 1.2 MUST hard-bind `thread_ts = "1776997200.000000"` + `channel_id = "C002"` (L26 canonical) |
| **24** | **Write — Linear comment on Chloe issue** | **Outcome 1.1 + 1.2** | 1.2: issueId `linear_issue_f85be674c9b8`, per-employee + $11,350 batch impact |
| **25** | **Write — create new BrightLoop CRM engagement** | **Outcome 1.1 + 1.2** | 1.2: engagement_type NOTE, body reflects cohort-not-closed |
| **26** | **Write — calendar hold late Tuesday** | **Outcome 1.1 + 1.2** | 1.2: 2026-04-28 late-day window, 30 min duration |
| **27** | **Write — internal email to Mina** | **Outcome 1.1 + 1.2** | 1.2: single-source position summary |

## Hardness lever preservation (final state)

| Lever | Exercised by | Preserved |
|---|---|---|
| L25 existing-output anchor | OE 2, OE 4, OE 6 (Julian's 3 4/23 outbounds re-read as anti-templates) | Yes |
| L9 authority self-anchor | Julian's own voice preserved through prompt framing; OE list forces Airtable read to override the self-anchor | Yes (via mechanism) |
| L26 decoy parent thread | OE 12 enumerates + explicitly rejects Julian C007 orphan `1777011000` + Julian C002 `1777012200`; OE 13 verifies canonical target; OE 23 attaches to canonical `1776997200` | Yes (strengthened round 2) |
| L2 Airtable-silence + QB-invoice skip | OE 9 (Simone Special Requirements silent) + OE 10 (Marcus record) + OE 11 (QB invoice INV-2026-0308 $11,350) | Yes |
| L8 emergent 3-service reduction | OE 4 (email UrbanNest 6-question) + OE 5 (no reply verify) + OE 9 (Airtable silent) + OE 11 (QB $11,350) | Yes (strengthened round 2) |

## Non-blocking advisories for S3

Forwarded to S3 rubric authoring:
1. OE 23 rubric MUST exact-match `thread_ts = "1776997200.000000"` (canonical) — L26 hardness lever hinges on this.
2. Persona-attribution rubric grounding must grep BOTH candidate emails per `persona_attribution_landmine.md` memory. OE 17 enumerates 5 near-miss rejects.
3. OE 19 escalation content must NOT include the derived answer (unit type, credit dollars, transfer availability) — per L6 guardrail.
4. OE 25 CRM engagement rubric must not check for a `crm_update_engagement` tool (does not exist in MoveOps catalog).
5. `email_email_ab2391d62ab1` sender-field anomaly — S3 rubric must select by content/recipients/subject, not sender field.
6. Density projection 44 STRICT no-buffer / ~51 realistic. All 10 write OEs must remain rubric-mandatory to hold density on real runs.
7. OE 8 verification probe expected-negative (no later carrier update) — S3 rubric should not penalize agent for the second search returning empty.
8. OE 12 decoy rejection is prose-only (not tool-observable). S3 must not create a rubric that checks the agent explicitly rejected decoys — check the affirmative attach `thread_ts` instead.
9. Fact_Ledger `today = 2026-06-12` stale from S0. Prompt anchored on 2026-04-26; no drift into OE. Fact_Ledger regen recommended before S3 date-alignment checks.
