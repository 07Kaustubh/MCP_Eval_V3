# Verification — HARDNESS — Tasks/40_6a614767cd5b60ad96902fb4

## Sources consulted

| Source category | File / Query | What was verified |
|---|---|---|
| Per-task data | `_aux/Universe_Split/airtable.airtable_records.json`, `hubspot.hubspot_objects.json`, `_aux/Fact_Ledger.json`, `_aux/Universe_Index/graph_report.md` | 8 Airtable spine record ids present; OPEN ESA accommodation ticket_8faab56c663352cfb8d61c994b2bae88 present; atom surface (emails 206, amounts 403, dates 192); density signals (Brooke 740, Lisa 73, Tanya 28). Full per-source breakdown in the detailed section below. |
| Eval spec | `Evals_starpm/` trajectory Tool Call Count dimension | Density midpoint projection 48 per model, classified on the StarPM V4 scale (>= 40 = PASS; NOT the V3-family 50/40 scheme). |
| QC spec | `Docs_starpm/7_QC_Spec_Doc1.json` trajectory T1 (Tool Call Count) | Projected midpoint 48, band PASS (StarPM >= 40). |
| Reference cards | `Reference/Hardness_Playbook.md`, `Tasks/_meta/Learnings.md` (L1-L31) | 11-lever catalog + StarPM per-model density note; 5 levers selected (L31, L8/L13, L10, L4, L9), each citing a Learnings entry. |
| Prior phase verification | `_aux/Verification_s0.md`, `_aux/Universe.txt` | Universe = starpm; today 2026-07-01 America/Chicago; 8 services confirmed. |

## Data sources consulted
- _aux/Universe_Split/airtable.airtable_records.json :: verified all 8 spine record ids present (recc0ecc885e9645e, rec769c9f03f0b85f, rec8005502043b755, rec91517a5acab558, rec922b9a2d1b9451, recc83c05d889b354, rec94e86a3007dd5e, reca8230a8fd9ff51) via grep.
- _aux/Universe_Split/hubspot.hubspot_objects.json :: verified OPEN ESA accommodation ticket_8faab56c663352cfb8d61c994b2bae88 present.
- _aux/Universe_Split/ (all) :: phrase counts — "reasonable accommodation" 60, "emotional support" 50, "payment plan" 78, "possession…returned" 2, "Ready to File" 2, "Rio Bend" 146, "Sunset Ridge" 48; ".pdf" tokens = 0 (near-dup PDF decoy lever confirmed ABSENT and excluded).
- _aux/Fact_Ledger.json :: atom surface (emails 206, amounts 403, dates 192, ids for airtable/linear/hubspot/slack) consulted for lever feasibility; entities/fiscal_periods = 0 (property-mgmt, no GL trap — expected).
- _aux/Universe_Index/graph_report.md :: density signals — Lisa 73, Brooke Phillips 740 (authority), Tanya 28; make-ready 120 / maintenance 50; slack C004=144 / C003=127.
- _aux/Universe_Index/{service_inventory,key_facts,today_horizon,entities_personas,accounts_per_entity}.md :: services (8), today 2026-07-01 America/Chicago, volumes.

## Reference docs consulted
- Reference/Hardness_Playbook.md :: 11-lever catalog + tool-call costs; StarPM framework-scoped density note (40/15 per model, never 50/40). Levers considered = all 11; selected S1(#9+L31), S2(#1/#8/#10), S3(#2), S4(#6), S5(L9). #11 net-vs-gross dropped (QB figures unverified). PDF near-dup (#6-via-files) dropped (0 .pdf).
- Tasks/_meta/Learnings.md :: L1-L31 read end to end. Cited: L8/L13 (S2 latching/anchor), L10 (S3 structured-DB skip), L4 (S4 near-miss entity), L9 (S5 authority, prompt-side), L31 (S1 dual-model Gemini negative-directive differentiator), L15/L16 (implicit prompt / persona belief, brief). S4 combines the L4 near-miss with structural levers (never L4/L5 alone).

## Eval spec sub-dims relevant to this phase
- Trajectory dim Tool Call Count (StarPM floor 15, design 40+ per model) :: projected midpoint ≈ 48 → PASS per model.

## QC spec sub-dims relevant to this phase
- Trajectory T1 Tool Call Count :: projected midpoint 48, band PASS (StarPM ≥ 40).

## Verification statements
- [x] At least 3 levers selected; each cites a Learnings.md entry (5 selected: L31, L8/L13, L10, L4, L9).
- [x] Density midpoint projection classified on the StarPM V4 scale (48 ≥ 40 = PASS; NOT the 50/40 V3-family scheme).
- [x] Service breadth table populated — 8 distinct services, dominant airtable ≈ 26% (< 60%) → PASS.
- [x] Every cited record atom verified present in the Universe_Split (8 Airtable ids + HubSpot ticket + phrase counts).
- [x] Dual-model requirement met: ≥ 1 Gemini-specific stump (L31 negative-directive) + ≥ 1 Opus-specific stump (L10 HubSpot skip).

## Discrepancies surfaced (if any)
- Oracle's initial brief framing ("accommodation-vs-eviction contradiction") CONFIRMED and sharpened: it is a genuine dual live track (OPEN ESA ticket + in-progress eviction) on the SAME tenant, not a mislabel. No pivot needed.
- Near-dup PDF decoy landmine (from universe notes) does NOT exist in this task (0 .pdf tokens) — correctly excluded; near-miss lever repointed to Unit 14 cross-property (Rio Bend vs Sunset Ridge).
- Las Palmas 8D present ×96 as prose but was Task 39's spine → similarity risk flagged to S1 (avoid 8D make-ready shape).


## Post-audit (Oracle skeptical completeness review, 2026-07-23)
- **Oracle verdict: VERIFIED COMPLETE.** Independently ground-truthed all load-bearing records (possession-hold recc83c05d889b354, stale-plan rec769c9f03f0b85f, HubSpot ESA ticket_8faab56c663352cfb8d61c994b2bae88) with file:line snippets; recomputed density midpoint 48.5 (PASS ≥ 40 StarPM); all 9 checklist items pass; zero hallucinated ids; correct framework (no 50/40 Brookfield leak).
- **Fixed the one actionable defect Oracle flagged:** S4 near-miss lever cited Learnings L6 (correction-emails) — corrected to **L4** (near-miss entity) across Hardness_Plan.md, this file, and the two _meta appends (Hardness_Patterns_Log, Stump_Hypotheses). Prior-task _meta L6 entries left untouched (append-only).
- **Closed Oracle minor-note-2 (secondary anchors):** independently confirmed present — gmail threads 9f2b3cd66c907597 / cfabf41121992633 / 37a90450b4c2de2c (gmail.gmail_threads.json), slack ts 1779304892 / 1782673915 (slack.slack_messages.json); .pdf token count = 0 (near-dup PDF decoy confirmed absent, lever correctly excluded).
- **Oracle minor-note-3 (L10 = SAP-labeled):** accepted as-is — StarPM has no SAP; L10's structured-DB-skip principle is the canonical reading and is what S3 applies (HubSpot ESA ticket the eviction workflow never opens). No change needed.

## Verdict

PASS

- Every required source verified clean: 8 Airtable spine ids, HubSpot ESA ticket, and all secondary anchors (gmail threads 9f2b3cd66c907597 / cfabf41121992633 / 37a90450b4c2de2c; slack ts 1779304892 / 1782673915) confirmed present in the Universe_Split.
- Density midpoint 48.5 recomputed from atoms, PASS on the StarPM V4 scale (>= 40 per model).
- Oracle skeptical completeness review (2026-07-23) returned VERIFIED COMPLETE; the one actionable defect it flagged (S4 near-miss lever cite L6 to L4) was fixed across Hardness_Plan.md and this file.
- Zero unresolved discrepancies: accommodation-vs-eviction confirmed as a genuine dual live track; PDF near-dup decoy correctly excluded (0 .pdf tokens); Las Palmas 8D similarity risk flagged forward to S1.