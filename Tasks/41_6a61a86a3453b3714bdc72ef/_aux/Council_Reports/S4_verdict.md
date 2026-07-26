# Verifier Fails — S4 verdict (Tasks/41_6a61a86a3453b3714bdc72ef)

**Universe:** StarPM · **Framework:** V4 dual-model (Opus 4.8 + Gemini) · **Runs:** 6 per model, 0 errored.
**This is the post-fix re-grade.** The prior S4 pass found R6 (make-ready record) was an over-strict exact-ID rubric contradicting OE 14 (Bucket 1) and produced one judge over-credit (Bucket 2); the R6 fix + the $2,287.50 additions to R1/R16 fail-lists were applied to `7_Rubrics.json` (2026-07-24) and the platform re-ran trajectories. This verdict classifies that re-graded output (`8a`/`8b` dated 2026-07-24 22:41-42).

**Bottom line:** task is SOLID, difficulty-valid, and ship-clean. pass@1 = 0% both models, 0 errored, density OK. **R6 now passes 6/6 — the prior Bucket-1 defect is CLOSED.** Every remaining verifier-assigned FAIL is a legitimate model failure (Bucket 3). Zero Bucket 1, zero Bucket 2 in this run. All-Failing sub-dim 5/5. Ship the AF justifications; no further rubric fix required.

## Trajectory hard gates (run before classification)

### T3 — Error Rate
Erroneous runs: Opus 0/6, Gemini 0/6. **Verdict: PASS** (< 3 each). All 12 trajectories completed to an evaluable state (`parse_trajectories.py`: 12/12 ok).

### T2 — Agent Failure Rate (pass@1 <= 40%)
Runs passing ALL rubrics: Opus 0/6, Gemini 0/6. pass@1 = **0.0%** each. **Verdict: PASS** (<= 40%). Not "too easy"; no REDO route.

Density (from `_aux/Trajectory_Stats.json`): avg 43.4 total tool calls / 29.6 MCP; per-model Opus 48.0, Gemini 38.8. Both above the StarPM v4 fail-floor (15) and at/above the 40 design target (Gemini 38.8 ~1 under target, well clear of floor). No REBUILD candidate.

## Run matrix (rubric index 1-20 = 7_Rubrics.json order; P=pass F=fail)

### Opus (8a) — only rows with any fail shown; all other 12 rubrics passed 6/6
| # | Rubric (short) | r1 | r2 | r3 | r4 | r5 | r6 | Fails |
|---|---|---|---|---|---|---|---|---|
| 1 | clean net ~$1,832 | F | F | F | F | F | F | **6/6 AF** |
| 2 | charges ~$1,982 (847/925/210) | F | F | F | F | F | F | **6/6 AF** |
| 4 | owner auth = Linda Castillo | F | P | F | P | F | P | 3/6 (r1,3,5) |
| 11 | note: owner-approved / auth on file | P | P | F | P | F | P | 2/6 (r3,5) |
| 15 | draft to Linda Castillo | F | P | F | P | F | P | 3/6 (r1,3,5) |
| 16 | draft: balance ~$1,832 | F | F | F | F | F | F | **6/6 AF** |
| 18 | draft: owner-approved / auth on file | P | F | F | P | F | P | 3/6 (r2,3,5) |
| | **Passed / 20** | 15 | 16 | 13 | 17 | 13 | 17 | pass@1 0/6 |

Rubrics passing 6/6 on Opus: 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 17, 19, 20. **R6 = 6/6 PASS (was 3/6 fail pre-fix).**

### Gemini (8b) — only rows with any fail shown; all other 16 rubrics passed 6/6
| # | Rubric (short) | r1 | r2 | r3 | r4 | r5 | r6 | Fails |
|---|---|---|---|---|---|---|---|---|
| 1 | clean net ~$1,832 | F | F | F | F | F | F | **6/6 AF** |
| 2 | charges ~$1,982 (847/925/210) | F | F | F | F | F | F | **6/6 AF** |
| 14 | channel: no marketing | F | P | P | P | F | F | 3/6 (r1,5,6) |
| 16 | draft: balance ~$1,832 | F | F | F | F | F | F | **6/6 AF** |
| | **Passed / 20** | 16 | 17 | 17 | 17 | 16 | 16 | pass@1 0/6 |

AF-validity (eval Step 5): rubrics 1, 2, 16 failed ALL 6 completed runs on BOTH models → genuine all-fails. Every partial passed >= 1 completed run → not AF (correctly excluded from AF-justification requirement).

## Classifications

- **Bucket 1 (rubric invalid): 0.** The prior R6 exact-ID defect was reconciled with OE 14 (graded on tenant + property + hold content); the re-run confirms R6 now grades consistently and passes 6/6 (identical Tanya-Unit-14 writes that previously flip-flopped now all pass). No remaining hard-invalid or over-strict rubric. See `S4_fixes.md` (fix CONFIRMED effective).
- **Bucket 2 (judge error): 0.** The prior run's single inconsistency (R6 over-credit on identical writes) is resolved by the R6 fix. Re-spot-checked all 240 gradings in this run against the raw trajectories: every FAIL is corroborated by the run's own tool calls; no misread, no inconsistent verdict on equivalent writes. See `S4_judge_errors.md`.
- **Bucket 3 (legitimate model failure): all 8 failing rubrics.** See `S4_Bucket3.md` (per-model trajectory walks) + `S4_AF_justifications.md` (AF batch for rubrics 1/2/16).
  - AF (both models, 6/6): rubrics 1, 2, 16 — balance trap (invoice 7214 $2,287.50 vs bill QR-2026-0441 $1,982 charges / $1,832 net; $150 credit not disposed).
  - Opus partial: rubrics 4, 11, 15, 18 (owner latch Harris vs Castillo).
  - Gemini partial: rubric 14 (channel no-marketing omission, negative-directive).

## All-Failing Rubrics sub-dim (v11 scoring)

Bucket 1 ratio = **0 / 3 AF rubrics = 0%** (also 0/8 = 0% counting all distinct failing rubrics).
0% < 25% → **All-Failing Rubrics sub-dim = 5/5 (PASS).** Every all-failing rubric is a genuine, universe-grounded model failure (the vendor-linked-bill balance trap), not invalid rubric design. The rubric set is sound.

## Ground truth re-confirmed (this run, raw universe — not just OE)

Read directly from `_aux/Universe_Split/`:
- **Bill QR-2026-0441 (id 232176553533):** lines $847 (May arrears) + $925 (June rent) + $210 (late fees) + $150 ("Partial payment plan credit applied"); Balance 2132.0; VendorRef "Alamo HVAC Services"; **no CustomerRef**. → charges $1,982, net-of-credit $1,832, stored Balance $2,132 (credit added as a positive). Matches R1/R2/R16 expected values exactly.
- **Invoice 7214 (id 283231782926):** lines $1,125 + $975 + $187.50 (+ $5,885.94 credit); Balance 0.0; TotalAmt 8173.44; CustomerRef "Tanya Mitchell". → the three charge lines sum to $2,287.50, the figure all 12 runs reported.
- **Owner:** contacts label BOTH `linda.castillo@gmail.com` AND `harry.harris@gmail.com` as "Property Owner"; `john.castillo@gmail.com` is a "Water Delivery Representative" decoy. Only EVF-2026-014 (`rec922b9a2d1b9451`: "Owner authorization received from Linda Castillo to proceed with eviction filing for Unit 14") + the Gmail 06-30 reply disambiguate to Linda Castillo. → R4/R11/R15/R18 expected owner correct; the Harris latch is a grounded near-miss.

## Hardness calibration (this run vs Hardness_Plan + prior S4)

Stump-hypothesis hit rate vs `_aux/Hardness_Plan.md` (5 predictions):
- **H1 [HIGH, arrears figure] — HIT (strong, symmetric).** 12/12 reported $2,287.50 from paid invoice 7214; none opened vendor-linked bill QR-2026-0441. Flagship lever L2 confirmed the single most robust StarPM stump (2nd task running, sibling Task 40 R10 also 0/12).
- **H2 [HIGH, eviction state + owner] — PARTIAL / asymmetry correction.** Eviction-state half (petition not filed / JP coordination) did NOT fail: rubrics 3/10/17 passed 12/12. Over-predicted. Owner half DID fail, Opus-only (runs 1/3/5), Gemini 0/6 — predicted symmetric, actually **Opus-asymmetric**.
- **H3 [MED, net-vs-gross $2,132] — displaced.** No run reported $2,132; failure occurred one hop earlier (agents never opened the bill), so the $150-credit disposition (L11) was never reached. L11 masked by L2.
- **H4 [MED, Gemini negative-directive omission] — HIT (exact).** Rubric 14 (channel no-marketing) failed Gemini 3/6 (runs 1/5/6), Opus 0/6. Lever L31 confirmed a clean Gemini differentiator (3rd StarPM confirmation, Tasks 39/40/41).
- **H5 [LOW-MED, near-miss unit confusion] — MISS (over-predicted).** No run conflated Rio Bend Unit 14 or summed the $13,208.75 catch-all.

**Post-fix correction to the prior calibration:** the prior entry logged an "L10 reversal/supersession make-ready-record pick" as an Opus 3/6 stump. That was NOT a legitimate stump — it was the invalid R6 exact-ID rubric false-failing correct writes (right tenant, right Unit 14, right hold content per OE 14). After the R6 fix those writes pass; R6 is 6/6 this run. The genuine load-bearing levers are: **L2 arrears (symmetric all-fail)**, **L1 owner-latch (Opus-selective)**, **L31 negative-directive (Gemini-selective)**. pass@1 stays 0/6 both models on these three alone.

Lessons for next task: L2 vendor-linked-bill remains the flagship symmetric stump — keep verbatim. Owner-latch (L1/L6c) is Opus-differentiating when both candidate owners share the "Property Owner" role and only a task-specific auth record disambiguates. Negative-directive omission (L31) is the reliable Gemini differentiator. To surface L11 (net-vs-gross) as its own observable fail, pair it with an easier bill-discovery path so agents actually reach the bill. Do NOT count a rubric-invalidity false-fail as a difficulty lever (the R6 lesson).

## Action items

- **Ship** the three AF justifications (rubrics 1/2/16) to the platform reviewer — `S4_AF_justifications.md`, voice gate clean (exit 0).
- **No rubric fix outstanding.** The one prior substantive fix (R6 vs OE 14) is applied and confirmed effective by this re-grade.
- **No judge appeals needed** — zero judge errors this run.
- Task passes both hard gates and the All-Failing sub-dim. No REDO, no further re-run required. Route: everything shipped clean → EXIT.
