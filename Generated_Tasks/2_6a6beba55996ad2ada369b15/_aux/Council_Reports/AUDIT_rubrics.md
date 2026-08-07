# AUDIT (STRICT VETERAN) - Rubric Set `2_6a6beba55996ad2ada369b15`

Universe **harmonygames** (confirmed `_aux/Universe.txt` = `harmonygames`; framework `hg`, single-model, model under test **Claude Opus 4.7**) · persona **Robert**, Co-Founder & Creative Director, Executive · universe today **2026-02-28** America/Chicago · deliverable `7_Rubrics.json`, **25 criteria** (Outcome 1.1=3, Outcome 1.2=18, Outcome 2.1=3, Process=1).

Read in full: `7_Rubrics.json`, `5_Prompt.txt`, `6_Oracle_Events.txt` (OE 20 decompose read untruncated), `PersonaBrief.txt`, `_aux/Hardness_Plan.md`, `_aux/Reasoning/OE_solvability.md`, `_aux/Reasoning/Rubric_Coverage_Matrix.md`, both S3 council reports, `Docs_harmonygames/7_QC_Spec_Doc1.json`, `Docs_harmonygames/9_Common_Error.md`, `Docs_harmonygames/14_Persona_ACL.md`, `Evals_harmonygames/3_Rubrics_Eval.md`. Every load-bearing atom re-derived from `_aux/Universe_Split/` myself, not taken from Council A. Severity ordering used is the HarmonyGames one: **Overly Broad = Moderate, Overly Specific = Minor**; an over-specification that would false-fail a correct agent is **Incorrect (Major)** per Eval 3 Phase 2.7 and Doc1 "Specificity, Accuracy, and Acceptance".

**Memory discipline (rule 33):** `snowflake.snowflake.tables.json` (159 MB) streamed via `_aux/stream_sf.py`; my `audit_verify.py` run peaked at **231.0 MiB** RSS, under the 384 MiB ceiling. No `json.load()` of the blob.

## Deterministic floor (settled, cited, not re-argued)

`validate.py --phase rubrics` PASS (0 fails, 0 warns, 6 notes; outcome=24 process=1) · `check_rubric_antipatterns.py` OK (0/25x3) · `check_ordering_coverage.py` OK (1 construction, 1 Process carrier) · `check_oe_rubric_sync.py` OK · `check_qc_binary.py` 6/6 measurable PASS · `test_regression_anchors.py` 89/89. `check_criterion_dependencies.py` and `check_rubric_signal.py` both SKIP (no verifier export at S3): **unmeasurable until S4, not passed** - carry both to S4 before classifying any all-failing criterion or trimming on signal.

---

## LENS 1 - Strict QC scoring (every applicable Rubric sub-dim, `7_QC_Spec_Doc1.json`)

Defect class sought: any sub-dim below a clean 5 under the maximally-literal reading.

| Rubric sub-dimension | Binary | Score | One-line reason | What prior council missed |
|---|---|---|---|---|
| Four-Field JSON Schema / Blank | Yes | **5** | All 25 carry non-blank title/category/justification/evidence; all four category values legal | nothing |
| Overall Rubric Quality | No | **5** | 0 Major, 0 Moderate, 0 Minor after independent re-triage of all 25 (see LENS 5); <5% Minor holds vacuously | nothing |
| Self-Containment & Verifiability | No | **5** | Title-only deletion test clears on all 25; placeholder pre-scan (`states a specific`, `the correct value`, open range hedge) zero hits; R23 over-lists rather than under-defines | nothing |
| Atomicity | Yes | **5** | No title bundles independently-failing actions/records; R14 recipient-pair and the per-artifact figure repeats are inside the documented bundling / per-deliverable exceptions | nothing |
| Requirement Coverage & Destination | Yes | **5** | Forward + reverse maps complete; each fact graded on the artifact the prompt placed it on; no OE-only requirement | nothing |
| Specificity, Accuracy & Acceptance | Yes | **5** | Every embedded value re-grounded EXACT (table below); reworded R23 no longer over-specifies; no Overly-Broad admits a plausible wrong answer on its own dimension | nothing |
| Duplicate & Vague Rubrics | Yes | **5** | Three coverage-verdict and three 8,452.64 criteria sit on distinct prompt-specified artifacts (Phase 3.3 explicitly distinct); zero `such as`/`e.g.`/`for example` across all four fields x25 | nothing |
| All-Failing Rubrics | No | **5 (N/A at S3)** | No verifier export; auto-pass. 0 predicted AF: every target writable, every value reachable through an unscoped/authored path | re-assess at S4 |
| Rubric Category Balance | Yes | **5** | Outcome present (24/25); Process 1/25 = 4.0% <= 40% cap; zero-Process would also be valid | nothing |
| Process Rubrics | No | **5** | Exactly one Process (R25), passes all three conditions (LENS 5); no tool named; no write graded as Process | nothing |
| Agent-Centric Affirmative Phrasing | No | **5** | Documented possessive tension adjudicated to 5 (see below); no tool name, no prohibition-only syntax, Agent is actor on all 25 | tension surfaced, not a fail |
| Negative Criteria | Yes | **5** | Pre-scan hits R11 "exceeds", R12/R16/R24 "fall short" all affirmative actor+verb naming a reported factual state; reworded R23 carries no negation token | nothing |

**Agent-Centric possessive tension, adjudicated (not waved).** 18 of 25 titles use "The Agent's written account states..." / "The Agent's #winddown message states...". Doc1's Non-Fail(3/4) row literally names "a valid possessive... construction". A maximally-literal reader could dock to 4. I decline the dock, grounded in a re-read of two authority documents, not internal precedent: (1) Doc1's own Authority Order sub-dimension states "Evals/*.md supplies the current evaluation procedure and repository-level policy overrides"; (2) `Evals_harmonygames/3_Rubrics_Eval.md` line 767 "Possessive Agent forms... are agent-centric and valid, do NOT fail them", line 782 table verdict "(no fix needed; valid)", line 788 "at worst NON-FAIL (3-4), never a fail (06/09)". The 06/09 override reclassifies the possessive out of the "nonstandard" 3/4 bucket into clean-valid. Score **5**.

### PER-ATOM EVIDENCE TABLE (self-derived, `stream_sf.py`, 231 MiB peak)

| Atom asserted in a criterion | Universe query I ran | Row excerpt returned | Verdict |
|---|---|---|---|
| measured life 2026-01-05 to 2026-02-09 (R2) | DAILY_ACTIVE_USERS game_id=combo_fighter min/max(date) | 72 rows, 36 distinct dates, min 2026-01-05, max 2026-02-09 | MATCH |
| 0.00 lifetime revenue (R3) | REVENUE_DAILY combo sum(iap+ad+total); REVENUE_DAILY_V2 combo rows | 72 rows, total=0.0 iap=0.0 ad=0.0; V2 combo rows=0 | MATCH |
| 7,483.42 lifetime acquisition spend (R4) | AD_SPEND_DAILY combo sum(spend_usd) | 330 rows, 7483.42 | MATCH |
| 801 peak DAU / 845 new / 55,101 sessions / 44.0 D1 (R5) | DAILY_ACTIVE_USERS combo | per-day platform-sum peak 801 (02-07; single-row max 426), new_users 845, sessions 55101, d1 simple mean 44.0 (n=72; new-user-weighted 43.78) | MATCH |
| 8,452.64 charged since 2026-02-09 (R6/R17/R20) | AD_SPEND_DAILY all game_ids date>2026-02-09 | 280 rows, 8452.64 (domino 5569.66, combo 2444.08, zombie 438.90); incl 02-09 = 8922.12; combo-only after = 2444.08 | MATCH |
| Leonard Hayes controls ad accounts (R7/R21) | slack.2026-01/02 campaign-control ts sweep | Leonard starts/stops/pauses campaigns (ts 1770404487, 1767475598, 1768166121, 1770844112); Arthur advises only; Robert voices concern only | MATCH |
| 10,800 net proceeds (R8) | Slack C0ADGSZKR3R ts 1770911000.728559 + derive; literal sweep for `10800` | "cash offer of $22500 for our data. They charge us $11700"; 22500-11700=10800; no `10,800` dollar literal anywhere in universe | MATCH (derivation) |
| 2,500 cash on hand (R9) | CASH_BALANCE month_end_date=2026-02-28 | {cash_usd:2500, monthly_net_burn:22500, runway_months:0.1, headcount:6, notes:"Company wind-down initiated"} | MATCH |
| approximately 15,000 wind-down (R10/R11) | Slack C07C2866011 ts 1770850852.708789 | "the cost of Sunset is about ~$15K, the data will likely cover our costs" | MATCH |

Every embedded value re-derived EXACT. The 22,500 collision (gross offer == CASH_BALANCE.monthly_net_burn) is handled correctly: no criterion grades the bare 22,500; only the derived net 10,800 (R8) is graded, so the collision cannot mis-grade.

**LENS 1 verdict: all twelve applicable Rubric sub-dims score 5.**

---

## LENS 2 - Answer-leakage sweep

Defect class sought: a load-bearing derived figure readable from a single tool call, or present verbatim in what the agent reads.

Grep of `5_Prompt.txt` for `10800`, `10,800`, `13300`, `13,300`, `8452`/`8,452`, `7483`/`7,483`, `22500`/`22,500`, `11700`/`11,700`, `2500`/`2,500`, `15000`/`15,000`: **0 hits on every token.** The agent's target figures appear nowhere in the prompt. The primary derived figure **10,800** is confirmed absent as a dollar literal from the entire February Slack shard and the Snowflake tables (only substring hits are inside unix timestamps, e.g. `1768510800`); it is producible only by the two-source synthesis 22,500 (Slack) minus 11,700 (Slack). Cash (2,500) lives only in Snowflake FINANCE, the offer only in Slack, the wind-down cost only in a separate Slack channel: no single call reveals the coverage verdict. The five OE-body hits on `10,800` are in `6_Oracle_Events.txt`, which the agent never reads. **No BLOCKER. PASS.**

---

## LENS 3 - Hardness end-to-end trace (four-part, every selected lever)

Defect class sought: a lever missing prompt-surface, OE-exercise, rubric-carrier, or Fact_Ledger atom (= HARDNESS_REGRESSION).

| Lever | Prompt sentence | OE step | Rubric carrier | Atom | Trace |
|---|---|---|---|---|---|
| L11 net-vs-gross | "I know roughly what we are getting for the data... be precise" | OE 14 (22,500/11,700/10,800), OE 16b (15K vs net) | R8 (10,800), R11 (wind-down > net) | Slack ts 1770911000.728559 | ✓ |
| L2 Snowflake FINANCE skip | "Tell me where that actually leaves us and be precise" | OE 17 (CASH_BALANCE) | R9 (2,500 cash) | FINANCE.EXPENSES.CASH_BALANCE 2026-02-28 cash_usd=2500 | ✓ |
| L8 multi-link chain | "whether that genuinely covers shutting down in an orderly way" | OE 18 (reconciliation) | R12, R24 (funds fall short) | 10,800 net + 2,500 cash vs ~15,000 + named vendor stack | ✓ |
| L7 multi-write | "Write it up... post it... file a tracking item" | OE 20/21/22 | R1 (page/doc), R13 (Slack), R18 (tracker) | write surfaces in `6_Server_Tools_Details.json` | ✓ |
| L10 supersession | (no direct ask - investigation friction) | OE 15 (quote rises, cash unchanged) | R8's exact 10,800 catches the quote-rise-as-cash-rise misread | Slack ts 1770924424.711879 / 1770924465.624129 | ✓ |

**L10 adjudicated independently (not adopted from Council B).** Council B judged L10 to have no covering criterion and called that correct because the prompt never asks for deal structure and the licence leaves cash unchanged. I concur on the conclusion but sharpen the reasoning, which strengthens it: L10 has a numeric failure mode and a structural one, and they are treated differently. The **structural** distinction (outright sale vs IP-retaining licence) changes no figure and the prompt never asks it, so grading it would be a beyond-prompt Incorrect (Major); correctly ungraded. The **numeric** failure mode is an agent that reads "the quote is gonna go slightly higher" (ts 1770924465.624129) as the cash consideration rising, and reports net proceeds above 10,800. That misread is caught by R8's exact 10,800. So L10's discriminating effect DOES reach a criterion (R8), while its non-numeric aspect is correctly left as pure friction. This is not a HARDNESS_REGRESSION. All five levers trace end-to-end.

---

## LENS 4 - Strict density projection (HarmonyGames bands, NOT the V3-family 50/40)

Defect class sought: density that clears only under a generous exploration assumption.

Trajectory sketched under the reading that MINIMIZES inferred exploration: identity/channel resolution ~3-4; Snowflake enumerate (list dbs/schemas/tables) + query DAU/REVENUE/AD_SPEND/CASH_BALANCE ~6-8; Slack searches for offer/owner/obligations/wind-down cost ~5-7; four writes (account, post, tracker) plus ~3 supporting reads ~10; recipient resolve ~2. **Minimized floor ~28 calls; midpoint ~40-43. Distinct services on the necessary path: 5** (slack, snowflake, confluence/gdocs, linear/trello, contacts).

HarmonyGames bands: authoring target 40+ calls AND 3+ services -> midpoint 40-43 with 5 services **PASS**; prompt-eval hard gate >15 necessary calls AND 2+ services with multiple meaningful writes and friction -> ~28 necessary **PASS**; trajectory floor >=15 average **PASS** with wide margin. `set_acting_user`, ACL-denied reads and inaccessible retries excluded from every count. The rubric set *forces* this density: R9 forces the Snowflake FINANCE read, R8 forces the Slack offer read plus derivation, R1/R13/R18 force three writes across three distinct services. Even the minimized floor clears every gate. **Density: PASS on HG bands.**

---

## LENS 5 - Adversarial veteran review (200+ tasks)

Per-defect-class, what I looked for and found:

- **Implicit framing preserved across all three artifacts:** yes. Account (R1-R12), post (R13-R17), tracker (R18-R21), final response (R22-R24) all carry the wind-down/coverage spine; no artifact drifts into an unrelated ask.
- **Entity drift (Leonard Hayes / leonard.hayes@harmonygames.co / "Leonard"):** none. Titles use full "Leonard Hayes" (R7, R14, R21) and "Arthur Blake" (R14) consistently; no email needed in titles (person is named, Slack resolves by identity). Council A bound Leonard = EMPLOYEE_0038, Arthur = EMPLOYEE_0025.
- **Silent Process-as-Outcome or converse:** none. R25 is genuinely non-write ordering (correctly Process); all writes are 1.1/1.2; all final-response facts are 2.1. R1/R13/R18 are creation writes correctly at 1.1.
- **Tool-name leaks / em-dashes / "at least N" without mandate:** grep of all 25 titles returned none on each. R22 "two or three figures" mirrors the prompt's exact "two or three", not a reward-hackable "at least N".
- **"approximately" near an ID/date/count:** the only "approximately" is R10 "approximately 15,000", a calculated/rounded cost stated "~$15K" in-universe, which is the correct flexibility treatment. Not near an ID/date/count.
- **Nested accept-sets (rule 17):** R2-R12 evidence pins "the created page or document"; R14-R17 pin "the posted message"; R19-R21 pin "the created tracking item". A run that fails the antecedent write (R1/R13/R18) fails its dependents. Account-content and post-content criteria are unnested (no single act satisfies one from each group). Deterministic confirmation deferred to S4 (`check_criterion_dependencies.py` SKIP).
- **Per-deliverable coverage (fact required in one artifact graded on another):** clean. The coverage verdict is graded on the account (R12), the post (R16) and the final response (R24) separately; 8,452.64 on the account (R6), post (R17) and tracker (R20) separately. Phase 3.3 and Common Error "the same fact required in two different deliverables is also distinct" bless this as coverage, not duplication.
- **Single-surface lock-in where the prompt named only a goal:** confirmed correct. R1 "standalone written page or document" does not pin Confluence vs GDocs vs GDrive (honours durability-relative-to-Slack directive 5); R18 "issue tracker or task board" does not pin Linear vs Trello. Neither goes so loose it stops discriminating: R1 excludes a Slack message (a Slack post is neither a page nor a document, and Slack is ruled out by the free-tier drop at ts 1770839825.928989), R18 excludes a non-tracking write. R13 pins #winddown, which is the prompt's explicit named destination ("the wind down channel"), not lock-in.

No Major, Moderate or Minor survives the per-criterion isolation test. Zero findings.

---

## LENS 7 - Anti-rationalization (each "considered but fine" promoted and grounded)

Per rule 19 I may not decline a validated finding on internal-precedent grounds; each decline below quotes a fact re-read from the universe or the artifact.

1. **Agent-Centric possessive tension.** Declined, grounded in Doc1 Authority Order ("Evals/*.md supplies... repository-level policy overrides") + Eval 3 lines 767/782/788 ("possessive... valid, do NOT fail them"). Not internal precedent; authority-document text.
2. **R23 breadth / low signal.** Declined. Re-read of the artifact: R23 grades provenance (each lead figure is drawn from one of five named record domains). Within its own dimension a wrong response (a fabricated figure, or the 24,275 R&D credit which traces to none of the five domains) fails it. Net-vs-gross is a different dimension graded by R8/R11. Eval 3 Overly-Broad precision guardrail (a): a strict companion (R8 net 10,800, R11 wind-down > net) independently locks the verdict, so the content-coverage criterion legitimately checks only that the lead set is grounded. Cleared.
3. **R5 branches 801 (cross-platform sum) and 44.0 (simple vs new-user-weighted mean = 43.78) carry mild derivation ambiguity.** Declined as a finding. Re-read of the table: R5 is any-one-of-four and its other two branches, 845 (single-column sum of new_users) and 55,101 (single-column sum of total_sessions), are unambiguous exact values, so the criterion is satisfiable on a clean branch and does not false-fail a correct agent. Logged as a watch-item for S4 signal review, not a REVISE.
4. **R6/R17/R20 "since 2026-02-09" paired with the strict-after value 8,452.64 (vs inclusive 8,922.12).** Declined. Re-read of the prompt: "the last day there is anything to look at" is 2026-02-09 (the last measured DAU/REVENUE date, verified min/max above), so "still running" money is money past that measured boundary, i.e. strictly after 02-09 = 8,452.64. The value is embedded exactly and disambiguates; 8,922.12 (including the endpoint) is a boundary error, not a co-equal reading. Cleared.
5. **R14 "addresses both Leonard Hayes and Arthur Blake" bundles two recipients.** Declined. The two founders are the single named audience of one Slack post; recipients of one write are coupled fields of that write under the explicit acceptable-bundling rule ("multiple required fields of the same write action... may share one Outcome rubric"; the canonical good example bundles three content items of one message). Atomic.
6. **R23/R12 "the named wind-down costs and vendor obligations" is mildly self-referential.** Declined. The domain is identifiable from the universe (wind-down service ~15,000, Singular 18,750, Unity ~21,000, Helpshift 1,200), and the title's five-domain disjunction remains decidable from the trajectory alone. Cleared.

No promoted item survives as a REVISE.

---

## LENS 8 - Regression anchors

`test_regression_anchors.py` 89 passed / 0 failed of 89. PASS.

---

## SPECIFIC ADJUDICATIONS (all six)

1. **R23 reword (retires the Council B Major).** New title: "The Agent draws each figure in its final response lead set from the Combo Fighter performance record, its acquisition spend, the data agreement, the cash position, or the named wind-down costs and vendor obligations." **Self-contained under title-only deletion:** yes, it names a closed five-domain disjunction the judge can decide by tracing each figure to a record; no acceptance-bearing fact sits only in justification/evidence. **Still discriminates against a wrong lead:** yes, on two hard cases re-derived from the universe, (a) the 24,275 R&D tax credit, which is not the data agreement, not the 2,500 cash, not acquisition spend, not a wind-down/vendor figure, and not in the GAME_EVENTS performance record, so it traces to none of the five domains and fails; (b) any fabricated number. It correctly does NOT fail a lead of 22,500 (genuinely drawn from the data agreement); the net-vs-gross verdict is R8/R11's job. Adjudication: the objective open semantic rule is valid; the Major is genuinely retired.

2. **OE 20 and OE 21 decompose lists mirrored to the rubric set (rule 14).** OE 20's twelve elements map 1:1 to R1-R12 (page/doc, window, 0.00, 7,483.42, one engagement figure, 8,452.64, Leonard owner, 10,800, 2,500, ~15,000, wind-down > net, funds fall short). OE 21's five map 1:1 to R13-R17 (post, both founders, link/reference, verdict, 8,452.64). **Both faithful, neither bent to a weaker rubric.** The OE 20 edit replaced a softening-framed engagement element with "one engagement figure stated affirmatively from [closed set]" (a negative-criterion fix, not a weakening); the OE 21 edit split a bundled "verdict and figure restated" into two atomic elements (an atomicity fix). No content element the account genuinely needs was dropped.

3. **Three coverage-verdict criteria (R12 account, R16 post, R24 final response) and three 8,452.64 criteria (R6 account, R17 post, R20 tracker).** Under Eval 3 Phase 3.3 and Phase 3.1 plus Common Error "the same fact required in two different deliverables is also distinct", these are **per-deliverable coverage, not duplicates**: each grades a different prompt-specified artifact, the actions differ, and removing any one would drop coverage of a distinct deliverable. Not redundant.

4. **`OE_solvability.md` directives 1-9, 11-13 (source skips 10):** each honoured. 1 -> R19/R20 (tracker bound to 8,452.64 still-running UA). 2 -> R3 (0.00 unproducible from V2). 3 -> no bare-22,500 criterion; only net 10,800 (R8). 4 -> R12/R16/R24 grade direction, no closed total. 5 -> R1 "page or document", no surface pin. 6 -> R2-R12 vs R14-R17 unnested. 7 -> no communications write dated 2026-02-28 ("since 2026-02-09" is a data window). 8 -> R25 ordering Process. 9 -> no burn-reconciliation criterion. 11 -> no criterion names the 24,275 credit. 12 -> R11 net-vs-gross. 13 -> no January campaign-pause criterion. All present directives carried.

5. **Persona ACL (Robert's read scope, `14_Persona_ACL.md`).** No criterion depends on evidence outside Robert's scope. Snowflake, Confluence, Linear, Trello, Contacts are the unscoped public-service group, so R3/R4/R5/R6/R8/R9 (Snowflake), R1 (Confluence path), R18-R21 (Linear/Trello) carry zero read-feasibility risk. The only scoped surface in play is Slack; R7/R13/R14/R16/R17 rest on #winddown (C0ADGSZKR3R, Robert authored 19-21 Feb messages) and #executives (C07C2866011, Robert authored 130+), both inside his authored scope. Writes are outside ACL entirely. The README's "Gmail, Slack, GCal, and Contacts only" line is stale and contradicted by the authoritative ACL doc and Doc1 (Contacts is unscoped); this does not touch any criterion. PASS.

6. **Gmail has no send/reply/compose/draft (LANDMINE).** No criterion is ungradeable for requiring one. R1 targets a page/document (Confluence/GDocs/GDrive), R13 a Slack post, R18 a Linear/Trello item, R22-R24 the final response. No rubric requires a Gmail write, and the OE explicitly emails no one. PASS.

---

## Watch-items carried to S4 (no severity, not findings)

- R5 branches 801 and 44.0 carry mild derivation ambiguity; any-one criterion is satisfiable on the clean 845 / 55,101 branches. Re-check under `check_rubric_signal.py` at S4.
- R23 is broad on its provenance dimension (low discrimination); confirm it is not a zero-signal cut candidate once a verifier export exists (rule 28).
- `check_criterion_dependencies.py` and `check_rubric_signal.py` SKIP at S3; both mandatory at S4 before classifying any all-failing criterion or trimming.

## Result

Zero BLOCKER. Zero Lens-1 sub-dim below 5. All five hardness levers trace end-to-end. Density clears the HarmonyGames 40+ authoring target, the >15 prompt gate and the >=15 trajectory floor with margin. Leakage sweep clean on the prompt. Both edited OE mirrors faithful; reworded R23 self-contained and still discriminating. Every present S2 directive honoured. No ACL or Gmail-capability defect. The set is clean at the REVISE-blocking level; the six declines in LENS 7 are each grounded in re-read universe or artifact facts, not internal precedent.

VERDICT: PASS (STRICT)
