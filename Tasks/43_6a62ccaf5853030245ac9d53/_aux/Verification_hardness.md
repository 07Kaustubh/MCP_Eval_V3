# Cross-Source Verification — HARDNESS (Task 43_6a62ccaf5853030245ac9d53)

## Sources consulted
- Per-task data :: `_aux/Universe_Split/quickbooks.quickbooks_entities.json` — verified AR invoice 2026-534 (id 445653930748, Linda Castillo, $1,622 = 387/1140/95) and the three 4C AP bills (Sunshine 195089456477 $387; Permian repaint 696089964235 $1,340 PD-2026-09; Permian closet 546359391323 $85) + Alamo inspection decoy 991582431419 $85 + the 10-bill $1,340 cluster (6 vendors). All grepped and confirmed real.
- Per-task data :: `_aux/Universe_Split/airtable.airtable_records.json` — verified two Mesa Vista 4C tblMakeReady rows (recbd087a4abd605b selProg / recc8534b3fd13954 selReady) + ticket reca424761ae15355 (MR-4C-2026-08 "market-ready"); Rio Bend carpet near-miss rows; water-heater chain MT-2026-1211/1256.
- Per-task data :: `_aux/Universe_Split/gmail.gmail_messages.json` — verified belief-anchor email 5101c5a41dffa90a (Carlos -> Linda, "Mesa Vista 4C Make-Ready Complete. Cost Summary for Your Records").
- Per-task data :: `_aux/Universe_Split/linear.linear_issues.json` + linear_comments — OPS-39 (In Review) vs OPS-93 ("Approved and Closed" title, state Todo) budget-recon supersession context.
- Per-task data :: `_aux/Fact_Ledger.json` — amounts 403 / emails 206 / invoice-ids 504 / airtable-ids 170 confirm lever feasibility (dollar + ledger surface is dense).
- Per-task data :: `_aux/Universe_Index/graph_report.md` + `service_inventory.md` — density signals: 8 services, quickbooks 625 entities (155 invoice / 117 credit_memo / 113 bill), airtable SoR, 8 Slack channels; Carlos rank-5 by artifact density (525 mentions).
- Eval spec :: `Evals_starpm/` trajectory Tool Call Count dim (>= 15 floor; StarPM 40+ design target per model) — projected Opus 43.5 (PASS band) / Gemini ~34 (THIN band).
- QC spec :: `Docs_starpm/1_Project_Instructions_Overall.md` + `7_QC_Spec_Doc1.json` — difficulty target average 40+ tool calls per model, pass@1 <= 40% (<= 2 of 6 pass), 3+ services; dual-model (Opus + Gemini).

## Reference docs consulted
- `Reference/Hardness_Playbook.md` :: all 11 levers considered; selected L2 (structured-DB skip, flagship), L10 (supersession), L6 (near-miss), L11 (net-vs-gross) + L1 reserve. Costs reconciled against the FIXED cost table (Task 38 calibration lesson) — no widened ranges.
- `Tasks/_meta/Learnings.md` :: cited L2/L10 (structured-store-skip symmetric), L4/L13 (near-miss paired with structure / first-framing), L6/L7/L15/L16 (HARD: answer derived not stated, wrong-looking data on record, implicit prompt, persona believes wrong number), L11/L14 (net-vs-gross / correct-observation-wrong-conclusion), L31 (Gemini negative-directive — noted NOT available on this spine).
- `Tasks/_meta/Hardness_Patterns_Log.md` + `Stump_Hypotheses.md` :: StarPM dual-model recipe (Tasks 39/40/41) — 1 symmetric + 2 complementary asymmetric; robustness ranking; per-model density spread (Gemini ~9-10 fewer calls).

## Eval spec sub-dims relevant to this phase
- Trajectory dim Tool Call Count (>= 15 floor; StarPM 40+ design target, PER MODEL) :: projected Opus 43.5 (PASS), Gemini ~34 (THIN).

## QC spec sub-dims relevant to this phase
- Trajectory T1 Tool Call Count (Docs_starpm/1: average 40+ per model) :: Opus PASS band, Gemini THIN band — documented acceptance + OE-lift plan in Hardness_Plan.md.

## Verification statements
- [x] At least 3 levers selected; each cites a Learnings.md entry. (4 selected + 1 reserve; L2/L10/L6/L11 each cited.)
- [x] Density midpoint projection classified per model into {PASS >= 40, THIN 15-39, INSUFFICIENT < 15}. (Opus 43.5 PASS; Gemini ~34 THIN.)
- [x] Service breadth table populated (v11 G1). (6 distinct services; dominant quickbooks ~42% < 60% -> PASS.)
- [x] Every load-bearing sub-agent claim independently re-grepped; the one unverified claim (mis-cited doc# "2026-537") was found absent (0 hits) and dropped.
- [x] Answer-leakage clean: derived $1,812 and decoys $1,727 / $1,897 have 0 comma-formatted hits; bare-number hits are all timestamps (L7 satisfied — only wrong-looking figures $1,622/$1,140/$95 are on record).

## Discrepancies surfaced
- **Sub-agent overreach (caught + corrected):** the lever-scan sub-agent cited a "mis-cited doc# 2026-537" as an L6 near-miss anchor. `grep 2026-537` = 0 hits — the detail is fabricated. Dropped from the plan; L6 stands on the verified 10-bill cluster + amount/owner near-misses.
- **Owner-identity tangle (design risk, flagged not blocking):** AP-bill notes pair the 4C receivable to "Pete Donovan" while the AR invoice + belief email address Linda Castillo. Pete is the painter (npc), not an owner — treat as a near-miss decoy; keep the owner as Linda. Not a load-bearing lever.
- **Gemini-selective leg is the weak point (flagged):** no data-grounded negative-directive available on the 4C-ready spine (no-injection). Acceptable because the symmetric flagship sweeps Gemini on its own (0/12 twice historically); mitigation + REDO contingency documented in Hardness_Plan.md.

## Verdict
PASS (levers 4/5, Opus density PASS, breadth PASS) with THIN_DENSITY on the Gemini model accepted per the documented OE-lift plan. Ready for `PIPELINE S1`.
