# Hardness Plan — Task 43_6a62ccaf5853030245ac9d53

**Framework:** StarPM V4 (dual-model: 6 runs Opus 4.8 + 6 runs Gemini). No-injection task (levers must be grounded in the per-task universe already present; base-universe edits forbidden). Density gate is StarPM per-model: midpoint >= 40 = PASS, 15-39 = THIN, < 15 = INSUFFICIENT.

## Persona and Business Function
- **Carlos Mendez** (Onsite Property Manager, `carlos.mendez@starpm.com`, `p_009`).
- **Business Function:** Property Operations (StarPM BF1).

## Recommended spine (fresh; avoids Task 39 Las Palmas 8D + Tasks 40/41 Tanya Unit 14 + Task 38 water-heater/412-Mesquite chain)
**Mesa Vista 4C make-ready owner cost pass-through reconciliation.** Carlos believes the 4C turn is fully wrapped and the owner has been billed. The persona-believed (WRONG) figure is on record: AR invoice **2026-534** (`quickbooks.quickbooks_entities.json` id `445653930748`, customer **Linda Castillo**, **$1,622** = deep clean $387 + repaint **$1,140** + closet trim **$95**, Balance 1622). Carlos's own email to Linda (`gmail.gmail_messages.json` id `5101c5a41dffa90a`, subj "Mesa Vista 4C Make-Ready Complete. Cost Summary for Your Records") reinforces "fully wrapped up / market-ready."

The **authoritative (DERIVED) truth lives only in the QuickBooks AP bills**, never stated as a total anywhere:
- Deep clean **$387** — bill `195089456477` (Sunshine, Doc 2026-SC-4C, "Mesa Vista Unit 4C"). Matches the AR line.
- Interior repaint **$1,340** — bill `696089964235` (Permian Make-Ready Crew / Pete Donovan Painting, Doc PD-2026-09, "Interior repaint, full unit - Mesa Vista Apartments Unit 4C"). AR line shows **$1,140 → understated $200**. **Load-bearing.**
- Closet trim touch-up **$85** — bill `546359391323` (Permian, Doc 2026-519, "Bedroom closet trim paint touch-up, Mesa Vista Unit 4C"). AR line shows **$95 → overstated $10**.
- **Correct owner pass-through = 387 + 1340 + 85 = $1,812** (vs believed **$1,622**).
- **Over-inclusion decoy:** bill `991582431419` (Alamo HVAC, Doc 2026-481-566, "$85 Unit condition inspection and punch list … Mesa Vista Unit 4C", note "Internal labor charge for Carlos Mendez's make-ready walk", NOT on the AR invoice) → adding it yields the **$1,897** decoy. Excluded.
- **Under-inclusion decoy:** treating the closet $85 as "internal" and dropping it yields the **$1,727** decoy.

**Owner-identity note (design risk, NOT a load-bearing lever):** the AR invoice + belief email both address **Linda Castillo** — treat Linda as the 4C owner. Several AP-bill notes say the receivable pairs to "Pete Donovan," but Pete Donovan is the *painter* (npc, Exterior Painter) — this is a near-miss decoy, not the owner. S1/S2 should keep the owner as Linda (per the AR invoice) or make the owner reference agnostic; do NOT build a load-bearing owner-recipient rubric on the Pete/Linda tangle.

## Levers Available
| # | Lever | Status | Evidence (`file` :: id) | Cost range |
|---|---|---|---|---:|
| 1 | Latching | yes | `airtable_records` recbd087a4abd605b (4C selProg "still tracking") vs recc8534b3fd13954 (4C selReady "confirmed ready") + ticket reca424761ae15355 "market-ready"; belief email 5101c5a41dffa90a | 5-8 |
| 2 | **Structured-DB skip** | **yes (flagship)** | `quickbooks` 696089964235 ($1,340 repaint) + 546359391323 ($85 closet) — actual amounts exist ONLY in AP bills, not in the AR draft, email, or Slack | 4-7 |
| 3 | Missing reply | no | no buried reply flips the total | — |
| 4 | Search-cap eviction | partial | `quickbooks` — **10 distinct bills at exactly $1,340** across 6 vendors (102111031436, 103013736254, 170950667066, 177091955583, 258920406326, 274398891317, 315183662554, 686894936323, **696089964235**, 968953468344); a search-by-amount buries the 4C repaint bill | 3-5 |
| 5 | Thread-reply blindness | no | resolution not in a Slack thread reply | — |
| 6 | **Near-miss entity** | **yes** | repaint $1,140 (AR) vs $1,340 (bill); closet $95 (AR) vs $85 (bill); twin $85 charges (Permian closet 546359391323 vs Alamo inspection 991582431419, same amount, one billable one internal); owner Linda vs Pete decoy; 10-bill $1,340 cluster | 3-5 |
| 7 | Multi-write diversification | yes (OE-dependent) | reissue/correct QB AR invoice 2026-534 + update Airtable 4C row + Slack #vendors/#owner-relations post + owner email (+ optional Linear OPS-39 budget comment) | 9-12 |
| 8 | Multi-link chain | partial | Airtable 4C row -> QB AP bills -> AR invoice 2026-534 -> owner; mostly inside QB, so counted as discovery not a separate lever | 6-9 |
| 9 | Universe-grounded gotcha | yes | AR invoice 445653930748 looks complete/authoritative but its line amounts contradict the AP bills; the $85 Alamo inspection looks passable but is internal (exclude) | 3-5 |
| 10 | **Reversal / supersession** | **yes** | AR draft 445653930748 ($1,622, stale amounts) is superseded by the actual AP bills; agent uses the stale gross AR line | 4-6 |
| 11 | Net-vs-gross | yes | net billable $1,812 vs $1,897 (incl. internal inspection) vs $1,727 (drop closet) — which lines/adjustments are owner-billable | 4-7 |

## Selected Levers (4 + 1 reserve)
Realizes the StarPM dual-model recipe: **one symmetric flagship + Opus-asymmetric near-miss + a (weaker) Gemini-leaning net-vs-gross.**

- **L2 — Structured-DB skip (SYMMETRIC flagship)** — the $1,340 repaint / $85 closet actuals live only in QB AP bills; both models trust the visible $1,622 AR draft + Carlos's "complete" email and never re-derive. Expected to stump **BOTH** models (~0/12, mirrors Task 40 R10 / Task 41 arrears, both 0/12). Justifies via **L2/L10 + L6/L15** (answer derived, never stated). Projected cost **6** (mid of 4-7).
- **L10 — Reversal / supersession (symmetric support)** — the AR invoice is the stale mirror; correct figures supersede it in the AP bills. Reinforces L2 on both models. Cost **5** (mid of 4-6).
- **L6 — Near-miss entity (OPUS-asymmetric)** — 10-bill $1,340 cluster + $1,140/$1,340 + $95/$85 + twin $85 + Linda/Pete owner decoy; Opus latches on the first-seen figure/record. Expected **Opus-selective** (mirrors Task 40 R1 / Task 41 owner-latch, both Opus-only). Justifies via **L4 (paired with structure, never alone) + L13 first-framing**. Cost **4** (mid of 3-5).
- **L11 / L9 — Net-vs-gross + universe-grounded gotcha (GEMINI-leaning, weaker)** — exclude the internal $85 Alamo inspection, keep the closet $85 -> $1,812; the $1,897 / $1,727 decoys punish mis-scoping. Justifies via **L11 + L14 correct-observation/wrong-conclusion**. Cost **5** (mid of 4-7).
- **L1 — Latching (reserve, Opus support)** — 4C "complete/market-ready" framing across email + ticket + selReady row. Available if the near-miss margin needs deepening; NOT summed into density.

## Tool-Call Density Projection (per model — StarPM gate applied separately)
Components use the **fixed** Playbook ranges; selected-lever costs are the midpoints above (sum = L2 6 + L10 5 + L6 4 + L11 5 = **20**).

| Component | Range | Midpoint |
|---|---|---:|
| Base discovery | 5-8 | 6.5 |
| L2 Structured-DB skip | 4-7 | 6 |
| L10 Reversal/supersession | 4-6 | 5 |
| L6 Near-miss entity | 3-5 | 4 |
| L11 Net-vs-gross | 4-7 | 5 |
| Write actions (3-4 writes) | 9-12 | 10.5 |
| Cross-service buffer | 5-8 | 6.5 |
| **TOTAL projected (Opus)** | **34-53** | **43.5** |

**Per-model spread (empirical, Tasks 39/41): Gemini runs ~9-10 fewer calls than Opus on the same task.** Applying −9.5:

| Model | Range | Midpoint | Band |
|---|---|---:|---|
| **Opus 4.8** | 34-53 | **43.5** | **PASS (>= 40)** |
| **Gemini** | ~26-43 | **~34** | **THIN (15-39)** |

**Gate (StarPM per-model):** Opus **PASS**. Gemini **THIN_DENSITY** (above the 15 INSUFFICIENT floor; below the 40 design target). See `## THIN density acceptance` below.

## Service Breadth (v11 G1)
StarPM service set (`Validators/universes.py`): airtable, contacts, gcalendar, gmail, hubspot, linear, quickbooks, slack.

| Service | Calls | % of total |
|---|---:|---:|
| quickbooks | ~18-20 | ~42% |
| airtable | ~7 | ~16% |
| gmail | ~6 | ~14% |
| slack | ~6 | ~14% |
| contacts / hubspot | ~3 | ~7% |
| linear | ~3 | ~7% |
| **Distinct services** | **6** | — |

**Breadth gate: PASS.** 6 distinct services each >= 5%; dominant service (quickbooks ~42%) is < 60%. QuickBooks dominance is expected and in-bounds — the reconciliation legitimately lives in the AP/AR ledger, but the trajectory still forces cross-correlation into Airtable (readiness), Gmail (belief anchor), and Slack (coordination).

## Stump Hypothesis (4 predictions)
1. **[HIGH — BOTH models, symmetric flagship]** Agents report the owner pass-through as **$1,622** (trusting AR invoice 2026-534 + Carlos's "complete" email) instead of the derived **$1,812**, never reconciling the repaint line against AP bill PD-2026-09 ($1,140 vs $1,340) or the closet ($95 vs $85). Mechanism: L2 structured-store-skip + L10 supersession. Expected ~0/12 (mirrors Task 40 R10 and Task 41 arrears, both 0/12).
2. **[MED-HIGH — OPUS]** Opus grabs the **wrong $1,340 bill** from the 10-bill cluster (or a $1,340 A Plus/412-Mesquite bill from a different scenario), or anchors on the AR's first-seen $1,140, or bills **Pete Donovan** rather than Linda. Mechanism: L6 near-miss + L1/L13 first-framing. Opus-selective (mirrors Task 40 R1 / Task 41 owner-latch).
3. **[MED — GEMINI-leaning]** Agent mis-scopes billable lines: drops the closet $85 -> **$1,727**, or includes the internal Alamo $85 inspection -> **$1,897**. Mechanism: L11 net-vs-gross + L9/L14 correct-observation/wrong-conclusion. NOTE: this may be **masked by L2** (an agent that never opens the AP bills stops at $1,622 and never reaches the netting step — as happened to L11 in Task 41). Treat as a margin item, not the engine.
4. **[LOW-MED — BOTH]** Duplicate write: agent *creates a new* owner invoice instead of correcting the existing 2026-534, double-billing the owner. Mechanism: L9 universe-grounded gotcha. Candidate negative-guard rubric ("does NOT issue a second/duplicate owner invoice").

## Hardness Score
**4 / 5 selected levers — PASS (levers) · THIN_DENSITY (Gemini model).**
- Levers: >= 3 grounded, non-latching-variant, dual-model-shaped -> PASS.
- Density: Opus 43.5 PASS; Gemini ~34 THIN (not INSUFFICIENT). -> overall THIN on the Gemini model, acceptable with the OE-lift plan below.
- Breadth: 6 services, dominant < 60% -> PASS.

## THIN density acceptance (Gemini model)
Per HARDNESS gate, a THIN midpoint (Gemini ~34, band 15-39) is an operator decision, not a STOP. Accepting with these per-task justifications + mitigation:
1. **The symmetric flagship does the work regardless of Gemini's call count.** On the two prior StarPM dual-model tasks the structured-store-skip stump hit **0/12** on its own — Gemini fails the reconciliation whether it makes 34 calls or 44. Density THIN does not endanger the pass@1 <= 40% target here; it only risks the QC "40+ average tool calls" sub-dim on the Gemini side.
2. **The THIN is liftable to PASS via the OE, and writes are model-agnostic.** S1/S2 MUST lock a **4-write / 5-service OE** (correct QB AR invoice 2026-534 + update the Airtable 4C make-ready row + Slack post in #vendors or #owner-relations + owner email + optional Linear OPS-39 budget comment). Writes execute on BOTH models, and the 10-bill $1,340 cluster forces disambiguation reads on both. A write-heavy OE pulls the Gemini midpoint toward ~40 without widening any lever range. Do **not** vague-ify or inflate levers to force the number — build the density into real write actions.
3. **Watch-item for S4:** carry a per-model density spread, not one midpoint (Task 39/41 lesson). Flag the first Gemini run's tool-call count; if it lands < 30, the OE needs another grounded write before upload.

## Lever-selection risk (surfaced honestly)
The Gemini-selective **negative-directive** leg (L31, the cheapest reliable Gemini stump on Tasks 39/40/41) is **NOT data-supported on this spine** — the 4C universe uniformly reads as "ready" (selReady record + "market-ready" ticket + belief email), so a grounded "the unit is NOT ready / do not market" beat cannot be engineered without contradicting base data (a no-injection violation). This spine is therefore **symmetric-strong + Opus-strong, Gemini-softer**. The mitigation is (a) the symmetric flagship sweeps Gemini on its own (empirically 0/12 twice), and (b) an optional exclusion-directive beat ("do not pass through the internal inspection charge to the owner") gives a mild Gemini-leaning negative directive if more margin is wanted. If S4 shows Gemini sweeping (passing), the REDO lever delta should add a genuine Gemini negative-directive from a *different* Carlos scenario (e.g., a Mesa-Vista-pool-closed "do not tell tourers it is open" or a Rio-Bend "not rent-ready, do not list" beat) rather than stretching this one.

## Hardness Brief for the Prompt Writer (S1)
Write an **implicit** prompt in Carlos Mendez's voice that treats the Mesa Vista 4C make-ready as done and asks the agent to **finalize/close out the owner cost pass-through** for Linda Castillo — Carlos BELIEVES the owner has been billed correctly (~$1,622) and just wants it "squared away and the record updated." Do NOT hint any figure is wrong (L15/L16). The agent must self-discover, from the QuickBooks AP bills, that the actual vendor cost is **$1,812** (repaint understated $200, closet overstated $10) and correct the existing AR invoice 2026-534 — not create a new one, and not add the internal $85 Alamo inspection. Selected levers: **L2 structured-DB skip (symmetric flagship, the $1,340 repaint bill), L10 supersession (stale AR draft), L6 near-miss (10-bill $1,340 cluster + $1,140/$1,340 + twin $85 + Pete/Linda owner decoy), L11 net-vs-gross ($1,897 / $1,727 decoys).** Keep the owner as Linda (per the AR invoice); the Pete-Donovan-owner cue is a decoy. Target a **4-write / 5-service OE** (QB AR correction + Airtable 4C row + Slack + owner email + optional Linear budget comment) to hold Opus density ~43 (PASS) and lift Gemini from THIN ~34 toward ~40. The correct total **$1,812 must never appear verbatim** in any artifact (verified clean: comma-formatted `$1,812`/`$1,727`/`$1,897` = 0 hits; only wrong-looking figures $1,622/$1,140/$95 are on record, per L7).

---

## FINAL-council carry-forward (2026-07-25, appended at PIPELINE FINAL — do not re-plan, this is an S4 watch-item)

**MAJOR-1 from `_aux/Council_Reports/FINAL_council.md`: the L2 flagship's predicted yield is optimistic; re-weight the Stump Hypothesis before scoring S4.**

Prediction 1 above claims L2 structured-DB skip sweeps ~0/12 (mirroring Task 40 R10 / Task 41 arrears). The Final Council disputes the magnitude, not the lever. `5_Prompt.txt` sentence 3 ("Go back to what each vendor charged us for the 4C work and set it against the line items I sent her") points the agent directly at the AP side, which is the `Learnings.md` **L29 escape-valve** pattern that neutralized L2 on Task 25.

**No prompt change applied, and this is deliberate.** Removing or softening that sentence would leave the reconciliation ask unstated and cost the prompt on Feasibility/Clarity. The instruction is the task, not an optional escape valve.

**The lever is preserved** (verified at FINAL): `1340.00` as the 4C repaint cost exists ONLY on bill `696089964235`. It is absent from invoice 2026-534, absent from the summary email body, and the only `$1,340` money hits anywhere in Gmail are `4a20c7c433db278a` (a monthly rent rate) and `6f2669a41401485a` (a Reyes Plumbing total), neither about 4C. Slack carries none.

**Revised attribution for S4:** expect the sweep to come from **L6 near-miss** (the 10-bill `$1,340` cluster + the twin `$85` discrimination + the Linda/Pete owner decoy) and **L11 net-vs-gross** (the `$1,897` / `$1,727` decoys), with **L2/L10** contributing the *depth* of the read rather than an outright skip. If S4 shows agents reaching the AP bills but landing on `$1,897` or `$1,727`, that is L6/L11 firing as re-attributed here, NOT L2 failing. Score it that way in the calibration ledger.
