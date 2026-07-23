# HARDNESS Cross-Source Verification — 39_6a602c895d0b0ab6551a3a86 (REDO)

**REDO note:** This file supersedes the previous Verification_hardness.md from the failed HARDNESS run (5 levers, midpoint 50.5, which produced Opus avg 37.5 / Gemini avg 35.5 actual tool calls — both below the 40-call floor). This REDO adds L6 (HubSpot near-miss entity) and raises the midpoint to 60.5 per the L31 calibrated gate (≥55 required for REDO on QC closeout scenarios).

---

## Sources consulted

### Per-task data
- `_aux/Universe_Split/airtable.airtable_records.json` :: confirmed rec291f423370e2a2db (Las Vistas 3C, fldTurnStatus=selReady); L25 anchor preserved — NO-OP injection (R1).
- `_aux/Universe_Split/linear.linear_issues.json` + `linear.linear_comments.json` :: confirmed OPS-224, OPS-225, OPS-226 as Las Vistas 3C rework tickets. Injection Plan (R2-R4) resets to state="In Review" + plants James Bennett rework-complete comments.
- `_aux/Universe_Split/gmail.gmail_messages.json` + `gmail.gmail_threads.json` :: confirmed no existing Las Vistas 3C closeout thread from Brooke; no existing Brooke→Jaime "activate showings" message. Injection R8/R9 creates both decoy (6/16 Jaime→Carlos fail) and canonical (6/18 Brooke→Jaime closeout-request with Denise leasing-activation ask).
- `_aux/Universe_Split/slack.slack_messages.json` + `slack.slack_channels.json` :: confirmed C004 = #make-ready (147 messages in base); no Las Vistas 3C closeout thread present. Injection R5-R7 plants decoy fail-post (6/16) and canonical closeout-request (6/18).
- `_aux/Universe_Split/hubspot.hubspot_objects.json` :: confirmed no "Las Vistas 3C" or "Las Vistas 9D" deals in base universe; existing deals are Mesa Vista, Starview Commons, Marcus Delgado 2BR. Injection R10-R11 creates the canonical 3C deal + the 9D decoy for L6.
- `_aux/Universe_Split/quickbooks.quickbooks_entities.json` :: verified "Unit 3C" bills exist only at Elmwood, Pineview, 4712 Redwood — not Las Vistas. QuickBooks excluded (no grounding for Las Vistas 3C cost action in persona scope).
- `_aux/Universe_Index/entities_personas.md` :: confirmed Jaime + Brooke + Carlos + James Bennett + Denise Morales all present as base contacts.
- `_aux/Universe_Index/service_inventory.md` :: HubSpot 187 objects, QuickBooks 625, Airtable 2 tables, Linear 230 issues, Slack 583 messages.
- `_aux/Universe_Index/key_facts.md` :: Slack C004=147; Linear 230; used for density projection.
- `_aux/Fact_Ledger.json` :: 206 emails, 403 amounts, 192 dates, 61 personas — confirmed all injected contact emails resolve to existing personas.
- `_aux/Candidate_Originals/5_Prompt.txt` :: Previous prompt confirmed no HubSpot action; HubSpot is net-new write surface in REDO.
- `_aux/REDO_reason.md` :: Root cause documented: 7 write actions / 5 services → Opus 37.5 / Gemini 35.5 avg. L6 + HubSpot add 6th service + 1 write + 5-8 disambiguation reads.

### Eval spec and reference docs
- `Reference/Hardness_Playbook.md` :: All 11 levers reviewed. L1, L6, L8, L9, L25, L26 selected. StarPM adaptation section confirmed: gmail draft-only, slack uses `message`, hubspot uses `manage_crm_objects`.
- `Reference/Sessions/HARDNESS.md` :: Phase runbook — 3-lever floor, tiered density gate (≥50 PASS / 40-49 THIN / <40 STOP), L31 REDO override (≥55 for QC closeout scenarios), service-breadth gate (≥4 distinct services each ≥5%), StarPM V4 Injection Plan schema.
- `Tasks/_meta/Learnings.md` :: L25 (existing-output anchor trap, 100% failure rate), L26 (decoy parent thread, 80%+ failure rate), L31 (THIS task's REDO record — calibrated realization 74% Opus / 70% Gemini; midpoint ≥55 required).
- `AGENTS.md` :: StarPM section — parameter traps, timezone America/Chicago, services list, HubSpot `manage_crm_objects` confirmed.

---

## Eval spec sub-dims verified

| Sub-Dim | Gate | Result |
|---|---|---|
| Trajectory Tool Call Count (T1) | Midpoint ≥55 (L31 REDO gate; standard gate is ≥50) | **PASS — midpoint 60.5** |
| Service Breadth | ≥4 distinct services each ≥5% of projected tool calls | **PASS — 7 services** |
| Lever Count | ≥3 Opus-4.8 stumping levers with Learnings citations | **PASS — 6 levers** |
| Difficulty Preservation | Existing 0% pass@1 difficulty levers (L25+L26) retained | **PASS — unchanged** |
| Injection Plan (StarPM V4) | Full plan with reachability + decoy annotation per HARDNESS.md schema | **PASS — 15 records R1-R11** |
| REDO Delta | Net-new service + lever vs failed plan | **PASS — L6 + HubSpot added** |

---

## Verification checkboxes

- [x] All 11 levers from Hardness_Playbook.md reviewed against universe data before selection
- [x] 6 levers selected (L1, L6, L8, L9, L25, L26); each grounded in specific universe records
- [x] Learnings L25, L26, L31 explicitly cited in Hardness_Plan.md
- [x] Density midpoint 60.5 ≥ 55 (L31 REDO gate) → PASS
- [x] Density midpoint 60.5 × 74% = 44.8 (Opus expected avg) > 40 floor → PASS
- [x] Density midpoint 60.5 × 70% = 42.4 (Gemini expected avg) > 40 floor → PASS
- [x] Service breadth: 7 services each ≥5% (airtable 13%, contacts 5%, gcalendar 5%, gmail 17%, hubspot 13%, linear 25%, slack 17%) — dominant Linear 25% well below 60% ceiling → PASS
- [x] HubSpot confirmed absent from base universe (no Las Vistas deals) — injection R10+R11 required and sufficient
- [x] Las Vistas 9D decoy (R11): newer hs_lastmodifieddate (2026-06-20 vs 3C 2026-06-11), no QC hold mentioned, appears first in recency-sorted search — exploitable trap
- [x] Las Vistas 3C canonical deal (R10): description explicitly states "Once QC clears, advance to appointment-scheduled" — resolves only after Airtable/Linear closeout confirmed
- [x] L25 anchor (rec291f423370e2a2db, fldTurnStatus=selReady) in base Airtable — NO injection needed; R1 is NO-OP
- [x] L26 decoy thread (Jaime 6/16 fail-post R5 + Bennett reply R6) vs canonical (Brooke 6/18 closeout-request R7) — 2-day date gap is unambiguous; canonical identifiable
- [x] Gmail canonical (R9): Brooke→Jaime 6/18 contains "Denise is asking whether leasing can activate showings" — motivates HubSpot deal update naturally
- [x] All injected IDs schema-valid; no collision with base universe IDs confirmed by grep
- [x] StarPM parameter traps (Slack `message`, Gmail `body` + draft-only, HubSpot `manage_crm_objects`, Airtable camelCase, Linear `team` + `save_comment(issueId, body)`) documented in L9 gotcha lever
- [x] Oracle sub-agent skip justified: REDO is density-only; direction unambiguous from REDO_reason.md; previous plan already executed full 11-lever scan
- [x] Injection Plan R1-R11: service, table, operation, fields, foreign keys, cross-service refs, reachability, decoy mechanism all populated
- [x] No edits to non-injected base universe records
- [x] Read-only PDF constraint respected — L12 skipped; no Files/ writes in injection plan
- [x] L6 hard rule respected — no correct HubSpot deal state stated verbatim in injected artifacts; correct deal-stage advancement must be derived from prompt intent + R10 description

## Discrepancies surfaced

- Universe_Index reports timezone `America/New_York`; AGENTS.md canonical StarPM tz is `America/Chicago`. Injection Plan uses `America/Chicago` per AGENTS.md rule. Non-blocker; flagged for S2/S3 awareness.
- OPS-99/OPS-108 (L10 duplicate East cluster HVAC tickets) remain available in the universe and were not selected — Jaime's 3C anchor scenario is stronger and HubSpot breadth was the better density fix. Documented for future task use.
- Previous Verification_hardness.md (midpoint 50.5, 5 levers) is fully superseded by this file.

---

## Verdict

**PASS (REDO)** — 6 levers selected (L1, L6, L8, L9, L25, L26), density midpoint 60.5 ≥ 55 (L31 REDO gate), service breadth 7 distinct services, Injection Plan complete (15 records R1-R11) per StarPM V4 schema. Ready for INJECTION.
