# S1 Prompt Design Record — Tasks/42_6a62ccac9492f2a60e456c1c

**Universe:** starpm (V4, dual-model Opus 4.8 + Gemini) · **Persona:** Brooke Phillips (Apartment Property Supervisor, p_000) · **BF:** Portfolio Coordination & Owner Relations (#2) · **Spine:** `owner_capex_approval_roof` — close out the Ridgeview roof-section CapEx pass-through to owner Robert Finley and get the vendor payment coordinated.

## Levers engineered into the prompt
| Lever | How the prompt surfaces it (no leak) |
|---|---|
| **L2 Structured-DB skip (FLAGSHIP, symmetric)** | "Go into the books, figure out what the payable for that roof job actually is." Forces the agent into the QuickBooks AP store, where the vendor of record is Big Bend Restoration, not the conversational "Pete Donovan / Donovan Roofing." |
| **L10 Duplicate / reversal (Opus-selective)** | "get it set up correctly and queued, and make sure the amount we pass back to the owner is the right one." Two identical $8,400 Big Bend bills exist; correct payable is $8,400, not $16,800. Not stated in the prompt. |
| **L31 Negative-directive / HOLD (Gemini-selective)** | "Before any money leaves... done by the book... If anything about it does not line up... do not just push it through. Bring it back to me first with what you found and what still has to happen before we can release." Surfaces the retract-into-HOLD without prescribing the reserve-confirmation condition. |
| **L1 Latching (Opus-selective support)** | "Pete Donovan's crew is confirmed for the work... so the crew can be paid." The persona's mistaken belief anchors the wrong vendor. |
| **L6 Near-miss entity** | Names "Ridgeview" precisely (3x); the Ridge-* / doc-number decoys live in the data. |

## Answer-leak discipline
$8,400 is leaked verbatim across the universe, so the prompt states NONE of the derived facts: no dollar figure, no "Big Bend", no "Donovan Roofing", no "duplicate", no "$16,800", no doc numbers, no explicit hold-condition. Only "Pete Donovan" appears — the intended latch (persona belief), which is the OPPOSITE of the answer (Donovan is not the payable vendor). Council A + Council B + AUDIT Lens 2 all confirmed zero derived-fact leakage.

## Write set (4 writes + reminder — to hold Gemini density >= 40)
1. QuickBooks bill flag/queue (payable set up but held) + 2. owner email to Finley (pass-through close-out) + 3. Slack post to #owner-relations + 4. Linear comment on the owner-report issue (OPS-100) + calendar reminder to confirm release.

## Expected stump targets (per Hardness Plan Stump Hypothesis)
1. [HIGH] Both models release/queue payment WITHOUT the explicit HOLD (Gemini near-100%, echoes "we're good to go"). Mechanism: L31.
2. [HIGH] Both misroute vendor as "Pete Donovan / Donovan Roofing" instead of Big Bend (never open the AP store). Mechanism: L2 symmetric + L1.
3. [MED-HIGH] Opus double-counts to $16,800 / misses PD-2026-084 as duplicate; Gemini misses it by never opening the store. Mechanism: L10 (Opus) + L2 (Gemini).
4. [MED] Near-miss confusion pulls a Ridge-* / PD-2026-09 decoy. Mechanism: L6.

## Validator
`validate.py --phase prompt` → PASS, 0 fails, 0 warns, 4 notes (word count 319, distinct-services 2 by the keyword heuristic; true breadth 7). `verify_universe_atoms.py` → PASS (0 atoms to ground; prompt carries no IDs/amounts by design).

## Council verdicts
- **Council A (Grounding):** GO. Zero ungrounded claims; every entity resolved to Universe_Split (Brooke, Finley, Pete Donovan=painter/customer, Ridgeview roof rec8b679d92f30753, Owner Reserve Trust account 64, OPS-100, C006 #owner-relations, two Big Bend bills). Narrative-state clean (Finley approval genuinely granted; premature-Slack defect is by-design, not a prompt contradiction). Authority OK. BF match true. Solvable end-to-end.
- **Council B (Adversarial QC):** GO. All 12 Prompt sub-dims 5/5. Unique Ground Truth holds (queue-vs-hold resolves to prepare-but-hold; end-state co-determined by universe duplicate + unconfirmed reserve). Density: Opus ~48 PASS / Gemini ~40 PASS (at floor). All 5 levers preserved. No leak, no upstream propagation. 3 non-blocking NOTES carried to S3: (a) anchor Linear rubric to OPS-100 not OPS-10; (b) reward duplicate-catch without hard-pinning which doc survives; (c) confirm Gemini density on first platform run (sits at 40 floor).

## Similarity gate
`calc_similarity.py` → **max composite 27.1** (< 40 ceiling, < 35 near-pivot band) → PASS. Top match: QC_Tasks/V3_Tasks/Task13 at 27.1 (raw-lex, cross-universe Brookfield reference; contextual multiplier 1.0 only because refs are unweighted). Nearest live Tasks/ prompt: Task 40 at composite 12.0 (raw 33.2 × 0.36 persona/BF/universe multiplier). Genuinely distinct; no pivot required.

## AUDIT (strict veteran)
**PASS (STRICT).** Zero BLOCKER hits; zero Lens-1 sub-dims below 5 (all 12 Prompt sub-dims 5/5, plus Universe Data-Exists + Cross-service Coherence 5/5 under strictest interpretation). All 5 levers trace from explicit prompt sentences to independently re-verified atoms (L2 Big Bend vendor 203 / no Donovan Roofing vendor / Pete Donovan = customer proj-f6f9edfeae5c; L10 two identical unpaid $8,400 bills 2026-481 + PD-2026-084; L31 reserve-confirmation HOLD notes on both bills; L1 Donovan latch; L6 Ridge* decoys). Answer-leakage sweep clean on every derived figure (the two "hold"/"reserve" hits are natural funding references, not the derived HOLD answer). Density Opus ~48 PASS / Gemini ~40 PASS. Regression 62/62. Similarity 27.1 (<35). Single material caveat: Gemini sits exactly on the 40 floor → carried as a MINOR watch-item to confirm on the first S4 platform run (not a REVISE — projected midpoint meets the >=40 StarPM gate and the 5-write mandate is verified present and maxed). Two non-blocking S3 anchoring notes carried forward (anchor Linear rubric to OPS-100 not OPS-10; reward duplicate-catch / single-$8,400-payable without hard-pinning which doc survives).

## Final verdict — S1 COMPLETE
All exit criteria met: validator PASS · Council A GO · Council B GO (12/12 sub-dims 5/5, density both models >=40, 5/5 levers preserved) · similarity 27.1 < 40 · AUDIT PASS (STRICT). Prompt is ready for the platform linter. Next: user pastes linter response (→ S1.5) or confirms linter-clean (→ S2 Oracle Events).
