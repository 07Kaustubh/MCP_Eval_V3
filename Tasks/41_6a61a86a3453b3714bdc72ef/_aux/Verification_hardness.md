# Cross-Source Verification — HARDNESS — Tasks/41_6a61a86a3453b3714bdc72ef

## Sources consulted
- Per-task data :: _aux/Universe_Split/airtable.airtable_records.json — tblMakeReady (120) + tblMaintenanceTickets (50): Tanya contradictory records (payment-plan vs breach vs 3-day-notice vs eviction-filing), Las Vistas 9D turn, Rio Bend Unit-14 near-miss (`rec94e86a3007dd5e`).
- Per-task data :: _aux/Universe_Split/quickbooks.quickbooks_entities.json — AP bill `232176553533`/QR-2026-0441 (Balance $2,132, VendorRef Alamo HVAC, no CustomerRef), AR invoice `283231782926`/7214 (Balance $0, zeroed by payment `952690463873` $8,173.44), credit memos, 13-entity catch-all customer `proj-2e48c594aab7` ($13,208.75).
- Per-task data :: _aux/Universe_Split/gmail.gmail_messages.json — accommodation thread (Tanya ESA request 05-15 -> Lisa approves 05-23) + eviction-auth thread (Linda Castillo authorization 06-30); base64 payload.body.data.
- Per-task data :: _aux/Universe_Split/linear.linear_issues.json — OPS-32/38/54 "Eviction Hearing - Mitchell, Harris Property" (hearing set, owner Harry Harris) = latching decoy vs Airtable SoR.
- Per-task data :: _aux/Universe_Index/graph_report.md + _aux/Fact_Ledger.json — density signals (Tanya 28 mentions; Airtable SoR 170; amounts 403, emails 206) confirmed sufficient for lever feasibility.
- Reference doc :: Reference/Hardness_Playbook.md — all 11 levers considered; selected L2/L10/L1/L11 (+ StarPM L31); per-lever cost ranges used in the density projection.
- Reference doc :: Tasks/_meta/Learnings.md — cited L2/L10 (structured-DB skip), L13/L26 (latching/first-framing anchor), L22 (net-vs-gross/sign), L31 (Gemini negative-directive omission), 2026-07-23 #3 (arrears-as-AP-bill single most robust stump); L15/L16 (implicit prompt) noted for S1.
- Eval spec :: Docs_starpm/1 density hard gate ("AVERAGE TOOL CALL COUNT OF ALL AGENT RUNS MUST BE 40+") — StarPM v4 per-model bar (design 40 / floor 15) applied; projected midpoint ~50 Opus / ~43 Gemini.
- QC spec :: Trajectory T1 Tool Call Count — projected midpoint ~50 Opus / ~43 Gemini, both in the PASS band (>=40).

## Verification statements
- [x] At least 3 levers selected; 5 selected (L2, L10, L1, L11, L31), each cites a Learnings entry.
- [x] Density midpoint projection stated per-model (StarPM v4 bar): Opus ~50 PASS, Gemini ~43 PASS. V3 50/40 scheme deliberately NOT applied.
- [x] Service breadth table populated (v11 G1): 8 distinct services, 7 at >=5% -> PASS.
- [x] Load-bearing record ids independently re-verified against Universe_Split: AP bill 232176553533/QR-2026-0441 Balance $2,132 VendorRef Alamo HVAC no CustomerRef; AR invoice 283231782926/7214 Balance $0 zeroed by payment 952690463873; EVF-2026-014 rec922b9a2d1b9451 owner Linda Castillo; Linear OPS-32/38/54 Harris framing; Rio Bend Unit 14 rec94e86a3007dd5e selReady; freshest eviction record recc83c05d889b354 (2026-07-01).

## Discrepancies surfaced
- Arrears authoritative figure is NOT a single settled "$1,982": the AP bill stored Balance is $2,132 ($150 "credit applied" line stored as a POSITIVE), net-of-credit $1,832. Promoted to lever L11 (net-vs-gross/sign) rather than treated as a fixed number. S1 must set the rubric-correct figure explicitly.
- Credit memos CM2026-089 (Unit 5B) and CM-2026-044 (770 Sagebrush) do NOT apply to Unit 14 rent — near-miss distractors, not genuine reductions.
- Las Vistas 9D genuinely reached Rent Ready in May (no open May blocker); the real anomaly is a 2026-07-02 make-ready re-kickoff post-dating that status + triplicate selReady records. 9D is a secondary lever source, not the flagship.
- Two eviction OWNERS coexist (Harry Harris in Linear/May framing vs Linda Castillo in Airtable SoR/current) — this IS the latching lever (L1), flagged for S1 to exploit, not a data error.
- Airtable created_time is a batch-load artifact (records stamped 2026-05-01 08:43 describe June-29 events); timeline must be read from semantic note-dates, not created_time. Flagged for S1/S2.
- DocNumber QR-2026-0441 and invoice 7214 coincide with Task-40 Learnings notes; confirmed by direct read that both are genuinely present in THIS task's Universe_Split (not a conflation).

## Verdict
- PASS — 5/5 hardness, 10 of 11 levers available, density midpoint ~50 Opus / ~43 Gemini (both PASS the StarPM v4 >=40 bar), breadth 8 services / 7 at >=5% PASS. No STOP gate fired. Proceed to S1.
