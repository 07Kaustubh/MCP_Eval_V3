# Council B — Adversarial QC · S2 Oracle Events · **ROUND 3**

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** `starpm` (V4, dual-model) · **Universe today:** **2026-07-01 America/Chicago** (`_aux/Universe_Index/today_horizon.json`)
**Deliverable:** `6_Oracle_Events.txt` re-read from disk after the post-GO edits — **38 OE steps**, 0 em-dashes, 0 en-dashes, 0 non-ASCII, 0 "at least N"
**Density scheme:** StarPM V4 per `AGENTS.md` hard rule 11 — **midpoint >= 40 = PASS · 15-39 = THIN · < 15 = INSUFFICIENT, per model.** V3-family 50/40 bands not applied.
**Breadth gate (codified, `Reference/Sessions/HARDNESS.md:151`):** ">= 4 distinct services with each >= 5% of total = PASS; 3 distinct services with the dominant one < 60% = ACCEPTABLE; <= 2 distinct services OR **dominant > 60% = THIN_BREADTH**." The two clauses are independent and either can fire.

---

## 0. Concession — my round-2 B3 was wrong, and the AUDIT identified the mechanism correctly

The AUDIT's MAJOR against my round-2 work is **upheld in full**. I have re-derived it and the error is arithmetic, not interpretive:

> Round 2 I reported an Opus profile of **linear 28 / 52 total = 53.8%** with "6.2 points of headroom".

The Linear call count the round-2 OE text **itself prescribed** was: reads `list_teams` 1 + `list_issue_statuses` 1 + `list_projects` 1 + `list_issues` 1 + `get_issue` OPS-87 1 + OE 13 pair 2 + OE 14 pair 2 + OE 15 two `get_issue` 2 + OE 16 `list_issues` 1 + OE 17 pair 2 + OE 18 pair 2 + OE 19 pair 2 + OE 20 two `get_issue` 2 + OE 21 five `get_issue` 5 = **25**; writes `save_issue` x5 + `save_comment` x3 = **8**. **Floor = 33.**

**I reported 28 against a prescribed floor of 33.** A minimising reading cannot land below the floor, so my figure was not a minimising reading at all — it was a thorough-agent estimate with Linear silently discounted and the non-Linear optional steps counted at full weight. The AUDIT's phrase "not reconciled with its own component table" is exactly right. Under the round-2 text the honest minimising share was **33 / 50 = 66%**, which is the coordinator's independently-derived figure, and **THIN_BREADTH fired then and I did not report it.**

Everything below is re-derived from the current file with the floor computed first and the reading stated before the number.

---

## B3 — Density and breadth, three readings side by side

Reading definitions, fixed before counting:

- **(A) OE-faithful minimising** — every step the OE prescribes as *expected*, each collapsed to the cheapest call count that satisfies it. No pagination credit, no retries, no optional steps.
- **(B) Maximally-skeptical minimising** — (A) minus every non-Linear call a determined minimal agent could skip without failing a required write. Linear is held at its floor because every Linear read feeds a required determination and all eight Linear writes are mandated. **This is the governing reading for the >60% disqualifier.**
- **(C) Thorough-agent expansive** — what a careful agent plausibly does: per-issue iteration, paginated reads, extra thread opens, redundant list calls.

### Per-service counts and percentages

| Service | **(A) OE-faithful min.** | % | **(B) Max-skeptical min.** | % | **(C) Thorough expansive** | % |
|---|---:|---:|---:|---:|---:|---:|
| **linear** | **30** | **56.6%** | **30** | **63.8%** | **36** | **56.3%** |
| slack | 7 | 13.2% | 6 | 12.8% | 9 | 14.1% |
| airtable | 7 | 13.2% | 5 | 10.6% | 8 | 12.5% |
| gcalendar | 5 | 9.4% | 4 | 8.5% | 5 | 7.8% |
| contacts | 2 | 3.8% | 1 | 2.1% | 4 | 6.3% |
| gmail | 2 | 3.8% | 1 | 2.1% | 2 | 3.1% |
| quickbooks | 0 | 0.0% | 0 | 0.0% | 0 | 0.0% |
| hubspot | 0 | 0.0% | 0 | 0.0% | 0 | 0.0% |
| **TOTAL** | **53** | | **47** | | **64** | |
| **Services >= 5%** | **4** | | **4** | | **5** | |
| **Dominant > 60%?** | no | | **YES** | | no | |

**Linear floor derivation (identical in A and B), from the current text:** `list_teams` 1 · `list_issue_statuses` 1 · `list_projects` 1 · OE 11 `list_issues` 1 · OE 12 `get_issue` 1 · OE 13 pair 2 · OE 14 pair 2 · **OE 15 single `list_issues(state:"Done")` 1** · OE 16 `list_issues` 1 · OE 17 pair 2 · OE 18 pair 2 · OE 19 pair 2 · OE 20 two `get_issue` 2 · **OE 21 two `get_issue` + one `list_issues` 3** = **22 reads**; `save_issue` x5 + `save_comment` x3 = **8 writes**. **Total 30.** The two rebalancing edits are real: OE 21 is −2 and OE 15 is −1 against the round-2 text, taking the floor from 33 to 30.

**What (B) strips from (A), and why each is genuinely skippable:** OE 7's second `slack_search_public` query (one query can satisfy a lazy sweep); OE 25's second `search_records` pass and the `list_records_for_table` page (one keyword sweep is enough to conclude "no push ticket"); OE 22's `list_calendars` (the calendar id is inferable from the persona's own email); OE 26 beyond the single Brooke lookup (Brooke is a defensible owner on four of the five tracking items, so one lookup can carry the recipient plus four owners); OE 27 entirely (no prompt sentence cues a mailbox sweep).

### Direct answer on the 60% question

**No. Under the governing minimising reading (B), `linear` is at 63.8% — above 60%. THIN_BREADTH FIRES.**

I am not reaching for reading (A) or (C) to clear it. (A) puts Linear at 56.6% only by crediting five non-Linear calls that a minimal agent skips, which is the identical move that made my round-2 number wrong. The AUDIT's stated band was 61-65%; my independent figure of 63.8% sits inside it and **corroborates the AUDIT rather than rebutting it.**

**Can it be brought under 60% without padding? No.** At Linear 30, clearing 60% needs a total of >= 50, i.e. **three more non-Linear calls that a minimal agent would still make**. The only candidates are precisely the five that (B) strips, and each is genuinely optional for a minimal agent. Adding them back is padding by definition.

The one non-padding lever that exists is on the Linear side and I recommend against it: OE 13/17/18/19 and OE 14 each pair `get_issue` with `list_comments`, ten calls in total. `get_issue` exposes `includeRelations: boolean`; if the server returns comments under that flag, the floor drops to Linear 25 / total 42 / **59.5%** — under the line. But that depends on unverified server behaviour, and it would also cut five calls of real density. **Do not rely on it.**

### `## THIN breadth acceptance` — the structural reason

This is a **prompt-and-universe property, not an OE defect, and no OE edit can fix it.**

1. **The load-bearing determination resolves in a single Linear column.** Lever 2 is the symmetric backbone: the whole "is the QC actually closed" question turns on `state_id` across OPS-87 / OPS-96 / OPS-98, decoded via `list_issue_statuses`. No other service mirrors that column — a 103-pattern leakage sweep found zero prose statement of it anywhere in the universe.
2. **Eight of the twelve required write calls are Linear writes** — five `save_issue` tracking items (mandated by "Anything still open gets its own tracking item raised") plus three `save_comment` notes (mandated by "a short note left on each one"). Both are explicit prompt asks. The remaining four writes are spread one each across airtable, gcalendar, slack and gmail, which is already the maximum diversification the prompt supports.
3. **The non-Linear read surface is genuinely shallow.** The Airtable table has four fields and 50 rows; the calendar has ten relevant events; contacts is a flat 61-row lookup; Gmail contains zero push content (verified: zero threads of 156 match "Preventive Maintenance Push" or "cluster"); QuickBooks and HubSpot are correctly at zero and were deliberately excluded at HARDNESS with three documented reasons.
4. **The >= 4-services clause still PASSES under every reading** — 4 services at >= 5% in (A) and (B), 5 in (C). The task is not the single-service-stack false positive the gate was written to catch: the chain genuinely forces cross-correlation across Linear structured state, Linear prose, Slack top-level posts, Slack thread replies and Calendar agendas. It fails only the dominance sub-clause, and it fails it because the answer lives in Linear and the user asked for Linear writes.

**Recommendation: carry THIN_BREADTH forward as a documented acceptance, do not manufacture breadth.** Any OE edit that adds non-Linear calls purely to move this number is padding and would be a worse defect than the finding.

### Density band per model, under the minimising reading

Reading (B)'s 47 is a floor, not a midpoint. Per-model figures built on it:

| Model | Floor | **Midpoint** | Range | **Band** |
|---|---:|---:|---|---|
| **Opus 4.8** | 45 | **50** | 44-58 | **PASS** (>= 40) |
| **Gemini** | 38 | **42** | 36-50 | **PASS** (>= 40) |
| **Combined** | 42 | **46** | 40-54 | **PASS** |

**Confirmed: the band is still PASS on both models after the −3 Linear calls.** The twelve-call write floor is incompressible and the Linear read floor is 22, so even a maximally-minimal Opus run clears 40 with margin. **Gemini's floor of 38 is the only soft spot** and sits just under the line; the midpoint of 42 clears, and per prior StarPM calibration (Task 41 Gemini 47/45/37/38/33/40) individual sub-40 Gemini runs are expected and are not a defect.

Movement against round 2, on like-for-like methodology (round 2 re-scored under reading B): Opus 52 -> 50, Gemini 44 -> 42, `linear` 66% -> **63.8%**. **The edits moved the share 2.2 points in the right direction and cost ~2 calls per model. They did not clear the gate and were never going to.**

---

## B1 — QC spec scoring (re-run against the current text)

Bands verbatim from `Docs_starpm/7_QC_Spec_Doc1.json`.

### OE Completeness — **5 / 5**

> **Pass (5):** "OEs describe the full critical path: key discovery steps + dependency chain(s) + required write action(s)."

No step was removed by the edits. OE 21 folds three `get_issue` calls into one `list_issues` pass but still covers OPS-16/17/18 discovery; OE 15 permits a single Done sweep but still covers the overclaim bound. All six write classes and twelve write calls remain. All prerequisite lookups remain and remain correctly ordered (`list_teams` -> `list_issue_statuses`; `list_calendars` -> `list_events` -> `create_event`; schema walk -> create; existing-ticket sweep -> create; forward-event sweep -> create; contacts -> draft; channel resolution -> post). Two steps were *promoted* from optional to expected (OE 23 Brooke sweep, OE 25 paging), which strictly increases coverage. Re-swept all 20 prompt asks; no new gap. **5/5.**

### OE Accuracy — **5 / 5**

> **Pass (5):** "All OEs are factually accurate. Tools, services, parameters, and expected data match the universe. Following the OEs literally would produce a correct trajectory."

**Every new or changed factual claim re-derived from source this pass:**

| Claim | Verification | Verdict |
|---|---|---|
| OE 16: a "North cluster" query "returns ten issues (seven on titles alone)" | Full-record match = **10**; title-only match = **7** (OPS-40, -44, -56, -66, -81, -87, -98); title-or-description union = **10** | **EXACT** |
| OE 25: 18 HVAC rows; Building C 9 incl. unit 304 and the lobby; Palomar 4 incl. unit 312; single rows Pinecrest 12 / Elmwood / Riverside; "four of the 18 name no property at all (two Unit 204 rows, a compressor-belt follow-up and a budget-review summary)"; "two standup rows name more than one site" | 18 / 9 / 4 / 1 / 1 / 1 all exact. The four property-less rows are MT-2026-043 and MT-2026-1257 (Unit 204), MT-2026-082 (compressor belt), MT-2026-1320 (budget review) — **exact**. The two multi-site standup rows are MT-2026-062 (Palomar + Riverside) and MT-2026-1219 (Pinecrest + Elmwood) — **exact**. Removing "unit 204" from the Building C parenthetical was correct. | **EXACT** |
| OE 27: "a 'Preventive Maintenance Push' query and a 'cluster' query each return zero threads across all 156" | `gmail_threads` = **156** rows; "preventive maintenance push" = **0**; "cluster" = **0** | **EXACT** |
| OE 21: `list_issues(team:"OPS", query:"Summer HVAC preventive service")` picks up the three scope issues | All three titles contain the string case-insensitively: OPS-16 "Summer HVAC Preventive Service - All Property Clusters", OPS-17 "Summer HVAC preventive service - cluster scope assignments", OPS-18 "Summer HVAC preventive service - all property clusters" | **EXACT** |
| OE 9: `team: "OPS", or "team_001" as returned by OE 8` | Round-2 MINOR 4 discharged | **FIXED** |
| OE 28: `fldPriority` option-id note (`selHigh`/`selMedium`/`selLow`, either form accepted, no criterion may grade it) | Matches the schema exactly; `typecast` exists | **FIXED** |
| OE 5: "the two replies a plain channel read **may not** surface" (was "do not appear in") | Correctly hedges the server-behaviour assumption I recorded as an unverifiable NOTE in round 1 | **IMPROVED** |
| OE 18: new sentence distinguishing OPS-56's access-pending pair from Jaime's walked-and-deficient pair | Verified distinct: OPS-56 created 2026-05-18 (never entered, tenant scheduling); Jaime's note 2026-05-23 (walked, deficient) | **CORRECT** |

**Two residual imprecisions, neither reaching the 4-band:**

- **A-1 (OE 15, MINOR).** *"using a single list_issues (team: "OPS", state: "Done") pass or get_issue on each, which returns [the two titles] both in state Done."* That pass returns **36** Done issues, not two; OPS-40 and OPS-91 are the two push-relevant ones among them. Accurate under the `get_issue` branch of the disjunction, loose under the `list_issues` branch.
- **A-2 (OE 10, MINOR).** *"proj_003 holds 60 issues of which roughly half are unrelated mass-email campaign items."* A broad mass-email keyword sweep over proj_003 returns **25 of 60 = 42%**; a title-only sweep returns **10 of 60 = 17%**. "Roughly half" is defensible against 42% and is an improvement on the round-1/2 text ("most", which was wrong), but it is generous.

Neither changes what any call returns in a way that breaks the trajectory, and no OE names a wrong tool, wrong service, wrong parameter, non-existent record or absent entity. **5/5.**

---

## B2 — Forward + reverse coverage (re-run)

**Forward: 20 of 20 asks fully covered.** No ask lost coverage in the edits. The three promotions strengthen two implicit asks: OE 23's Brooke sweep now firmly covers "confirm nothing already scheduled covers the re-inspection" at portfolio scope, and OE 25's paging now firmly covers "confirm no existing ticket covers the field items" against keyword-eviction.

**Reverse: 38 of 38 steps trace. Zero scope creep.** I re-attacked the three promoted/expanded steps specifically, since they were introduced partly for rebalancing and are therefore the most exposed to a padding charge:

- **OE 25 `list_records_for_table`** — carries a stated substantive reason ("to confirm the keyword sweeps did not evict a push-linked row"). Lever 4 in the Hardness Plan is search-result-cap eviction and the table holds 50 rows against a keyword sweep returning 18, so the eviction risk is real. **Legitimate, not padding.**
- **OE 23 Brooke forward sweep** — required to discharge Hardness Plan constraint 3 (F9 watch items: the 2026-07-15 Mesa Vista 4C QC inspection must not be contradicted). Jaime's own calendar is empty forward, so the only way to see the nine forward events is another attendee's calendar, and Brooke is verifiably an attendee on all nine. **Legitimate.**
- **OE 26 / OE 7 per-call notes** — these add no new step; they state the true arity of tools already in the OE (`contacts_search_contacts` takes one `query`; `slack_search_public` takes one `query`). Both are correct against the catalog. **Legitimate — they correct a prior undercount rather than inventing work.**

---

## B5 — Solvability (re-run against the current text)

All 38 steps run. Two new calls verified against the catalog and the data:

- `list_issues(team: "OPS", state: "Done")` — `state` is a real `list_issues` parameter (`string | null`). Returns 36 rows including OPS-40 and OPS-91. **Runs.**
- `list_issues(team: "OPS", query: "Summer HVAC preventive service")` — `query` is real; all three scope-issue titles match. **Runs, and this is a better step than the three `get_issue` calls it replaced** because it also models how an agent would actually find them.

Round-2 residuals both discharged: OE 9 now hedges the team key; OE 28 now states the priority option-id form. **No step fails at runtime.** The only remaining runtime-adjacent assumption is Lever 5's dependence on `slack_read_channel` not returning thread replies, which OE 5 now correctly hedges rather than asserting.

---

## B9 — Anti-pattern sweep (re-run)

| # | Check | Finding |
|---|---|---|
| 1 | Pure-reasoning OE with no tool call | **PASS.** OE 3 and OE 4 name `slack_read_channel`. OE 15 still opens with "Compare the three records..." before reaching its tool call in the second sentence — carries a tool call, so Phase 1.2 is satisfied; style residual only. |
| 2 | OE stating a count that does not match the universe | **PASS.** Every count re-derived: 10 / 7 North-cluster matches (exact), 18 / 9 / 4 / 1 / 1 / 1 Airtable (exact), 156 threads with 0 push hits (exact), 16 OPS-34 comments, 104 C001 messages, 230 issues, 48 comments, 5 states, 3 projects, 60 proj_003, 3 Jaime-assigned, 50 tickets, 4 fields, 20 calendars, 10 Jaime events, 9 forward events. Two hedged looseness items recorded as A-1 and A-2; no wrong number. |
| 3 | Tool that does not exist or belongs to a different service | **PASS.** 25 references, unchanged set, all previously verified name-, service- and parameter-correct. |
| 4 | Missing write-action OE | **PASS.** Six write classes, twelve write calls, all covered. |
| 5 | Act-vs-defer conflict | **PASS.** Unchanged: 580 Slack + 484 Gmail messages swept; six defer hits, all on the mass-email campaign; the only push timing decision runs the other way (Brooke, 2026-06-19). |

---

## Item 3 — F8 decomposition guard verification, per step

Standard applied: the guard must (i) say **must**, (ii) enumerate **one criterion per content element actually present in that step's description**, (iii) require a **separate owner criterion**, (iv) close with "never one criterion enumerating them", and (v) carry an accept-band wherever the step itself blesses an alternative form or location.

| OE | Content elements in the description | Guard enumerates | Owner criterion | "never one criterion" | Accept-band needed? | Verdict |
|---|---|---|---|---|---|---|
| **29** West | 2 — no QC record covers West; OPS-186 2026-06-17 records work still underway | **2, both** | yes | yes | no | **CORRECT** |
| **30** filter run | **3** — John's 2026-05-23 restock block; **Brooke's unanswered stock-count and bulk-order ask to Elias**; no record shows the run completed | **2** — restock block, and "that no record shows the run completed" | yes | yes | no | **DEFECTIVE — see MAJOR-1** |
| **31** access | 2 — South no-access unit; two North access-pending units | **2, both** | yes | yes | **YES** — the step blesses "splitting this into two separate tracking items, one per cluster" | **INCOMPLETE — see MODERATE-1** |
| **32** plumbing | 4 — OPS-97 state-vs-prose mismatch; two water heater replacements; hose bib repairs; 2026-06-02 budget escalation | **4, all** | yes | yes | **YES** — the step blesses routing the water heaters to Airtable instead | **INCOMPLETE — see MODERATE-2** |
| **33** East | 3 — identical title in opposing states; neither in a completed state; both assigned to Elias rather than Jaime | **2** (omits the assignee element, which is arguably absorbed by the owner criterion) | yes | yes | **YES, and it is PRESENT** — "the S3 criterion must accept either location or a correct agent false-fails" | **CORRECT** (one minor omission, MINOR-1) |

**Consistency with the pre-existing guards on OE 35 / 37 / 38:** OE 37 and OE 38 both use "S3 must decompose... never one criterion enumerating them" and match the new phrasing exactly. **OE 35 is the outlier — it says "S3 *should* grade them as three atomic criteria"** where all seven other guards say "must". Recorded as MINOR-2.

**Summary: 2 of 5 fully correct (29, 33); 1 defective (30); 2 incomplete on the accept-band (31, 32).** The AUDIT's second MAJOR is therefore **partially discharged** — the guards exist and three of five are sound, but one instructs S3 to author a criterion the pipeline forbids.

---

## Final scoring table

| Dimension | Sub-dimension | R1 | R2 | **R3** | Justification |
|---|---|---:|---:|---:|---|
| Oracle Event | **OE Completeness** | 4 | 5 | **5 / 5** | Full critical path preserved through the rebalancing edits: no step removed, two promoted from optional to expected, all six write classes and twelve write calls intact, every prerequisite lookup present and correctly ordered, 20 of 20 prompt asks covered. |
| Oracle Event | **OE Accuracy** | 4 | 5 | **5 / 5** | Every new and changed claim re-derived exact against source (10/7 North-cluster matches, the full 18-row Airtable tally with its stated non-partition caveat, 156 threads with zero push hits, the OPS-16/17/18 query match); two hedged wording imprecisions (OE 15's "which returns" against a 36-row Done sweep, OE 10's "roughly half" against 42%) change no outcome. |

**Note on the verdict-vs-score relationship:** the QC spec's OE dimension has only these two sub-dimensions, and neither captures a *grading instruction* that will produce a defective rubric downstream. MAJOR-1 below is exactly that. Per `Evals_starpm/2_OE_Eval.md` ("OE issues... directly impact rubric quality and accuracy"), I treat it as verdict-bearing even though it moves neither score.

---

## Issue table

| # | Sev | Where | Issue | Concrete fix |
|---|---|---|---|---|
| — | **BLOCKER** | — | **NONE.** | — |
| **MAJOR-1** | **MAJOR** | OE 30 | **The new F8 guard instructs S3 to author an absence-grounded criterion, and omits one of three content elements.** The guard reads: *"S3 must decompose this into one criterion per content element (the 2026-05-23 restock block, and that no record shows the run completed) plus a separate criterion for the named owner."* (a) *"that no record shows the run completed"* is an **absence**. Hardness Plan constraint 7 and Learnings L7 forbid building a rubric on one outright, and this is the identical defect I raised against OE 16 in round 1 and which was correctly fixed there by demoting the absence to corroboration — the guard reintroduces it in a different step. (b) The description carries **three** elements; the guard enumerates two, omitting **Brooke's unanswered stock-count and bulk-order ask to Elias at ts `1779569323.000012`** — which is the positive, verifiable element that should be graded in the absence's place. | Replace the guard sentence with: *"S3 must decompose this into one criterion per content element (John Smith's 2026-05-23 restock block at ts `1779567943.000011`, and Brooke's unanswered stock-count and bulk-order ask to Elias at ts `1779569323.000012`) plus a separate criterion for the named owner, never one criterion enumerating them. That no record shows the run completed is corroboration and must not itself be a graded criterion."* |
| MODERATE-1 | MODERATE | OE 31 | **Guard lacks the either-form accept-band the step itself requires.** OE 31 blesses "splitting this into two separate tracking items, one per cluster", but the guard does not tell S3 the criteria must pass under both the one-item and the two-item form. A 1.1 criterion pinned to "a tracking item" (singular) would false-fail the agent that splits. OE 33 handles the analogous case explicitly; this one does not. | Append: *"Because splitting into two items is equally acceptable, each criterion must be phrased to pass whether the content sits in one tracking item or two."* |
| MODERATE-2 | MODERATE | OE 32 | **Same shape.** OE 32 blesses routing the water heater replacements to the Airtable ticket log instead, but the guard's "two water heater replacements" criterion carries no either-location accept-band, so an agent that took the blessed alternative false-fails that criterion. | Append: *"Because routing the water heater replacements to the Airtable ticket log is equally acceptable, the criterion covering them must accept either location."* |
| MINOR-1 | MINOR | OE 33 | Guard enumerates two of three description elements, omitting *"both are assigned to Elias Navarro rather than to Jaime"*. Arguably absorbed by the owner criterion, but the omission is unstated. | Either add it as a third element or state that it is covered by the owner criterion. |
| MINOR-2 | MINOR | OE 35 | Phrasing outlier: *"S3 **should** grade them as three atomic criteria"* where the seven other guards (29-33, 37, 38) say **must**. | Change "should" to "must" for consistency. |
| MINOR-3 | MINOR | OE 15 | *"a single list_issues (team: "OPS", state: "Done") pass ... which returns [the two titles]"* — that pass returns **36** Done issues; OPS-40 and OPS-91 are the two push-relevant ones among them. Accurate under the `get_issue` branch, loose under the `list_issues` branch. | Reword to *"...which surfaces, among the 36 issues in state Done, 'Preventive Maintenance Push - North Cluster Properties' (OPS-40) and 'HVAC condenser cleaning and filter replacements - West Cluster' (OPS-91)."* |
| MINOR-4 | MINOR | OE 10 | *"roughly half are unrelated mass-email campaign items"* — a broad keyword sweep gives **25 of 60 (42%)**; title-only gives 10 of 60 (17%). Defensible but generous. | Change to *"of which a large share, roughly forty per cent, are unrelated mass-email campaign items."* |
| NOTE-1 | NOTE | Breadth | **THIN_BREADTH fires** under the governing minimising reading: `linear` 63.8% against the >60% disqualifier at `Reference/Sessions/HARDNESS.md:151`. The >= 4-services clause passes (4 services at >= 5%). Not OE-fixable; structural to the prompt. | Carry forward as a documented `## THIN breadth acceptance` with the four structural reasons in B3. **Do not manufacture breadth.** |
| NOTE-2 | NOTE | OE 15 | Still opens with a comparison before reaching its tool call. Phase 1.2 satisfied; style only. | Optional. |
| NOTE-3 | NOTE | Density | Gemini's maximally-minimal floor is **38**, just under 40. Midpoint 42 clears. Per Task 41 calibration, individual sub-40 Gemini runs are expected. | Record for S4; do not treat a single sub-40 run as a defect. |
| NOTE-4 | NOTE | `_aux/Reads_s2.md`, `AUDIT_prompt.md` | Still carry "23 HVAC tickets" and "18 OPS-34 comments" against verified 18 and 16. | Housekeeping; correct before S3 / FINAL. |

**Counts: 0 BLOCKER · 1 MAJOR · 2 MODERATE · 4 MINOR · 4 NOTE.**

---

**Verdict: NO-GO**

Both QC sub-dimensions hold at 5/5 and I re-verified every changed fact against source. The NO-GO is driven by **MAJOR-1 alone**: OE 30's new F8 guard instructs S3 to author a criterion grounded on an absence, which Hardness Plan constraint 7 and Learnings L7 forbid, and which is the same defect this council raised against OE 16 in round 1 and saw correctly fixed there. Shipping it would push a known-bad rubric shape into S3 with an explicit instruction behind it. The fix is one sentence. MODERATE-1 and MODERATE-2 are the same one-sentence shape on OE 31 and OE 32 and should land in the same pass.

On the AUDIT's finding against my round-2 B3: **upheld, conceded, and corrected.** I reported Linear at 28 against a prescribed floor of 33. Under the governing minimising reading the current text sits at **`linear` 63.8%**, above the 60% disqualifier, and I am recording **THIN_BREADTH** rather than reaching for a reading that clears it. Density remains **PASS on both models** (Opus 50, Gemini 42). No finding in this round has a root cause in `5_Prompt.txt`, so there is **no `PROPAGATE TO S1`** and the phase iterates at S2.

```json
{
  "phase": "oe",
  "council": "B",
  "round": 3,
  "task_dir": "Tasks/44_6a62ccba8cad60844b8364b9",
  "verdict": "NO-GO",
  "verdict_driver": "MAJOR-1 (OE 30 F8 guard instructs an absence-grounded criterion, violating Hardness Plan constraint 7 / Learnings L7)",
  "scores": { "oe_completeness": 5, "oe_accuracy": 5 },
  "score_history": { "round_1": [4, 4], "round_2": [5, 5], "round_3": [5, 5] },
  "round_2_self_correction": {
    "conceded": true,
    "audit_finding": "linear share 61-65% under the minimising reading; Council B reported 53.8% not reconciled with its own component table",
    "mechanism": "reported linear 28 in a 52-call profile while the round-2 OE text prescribed a Linear floor of 33 (25 reads + 8 writes); a minimising reading cannot fall below the prescribed floor",
    "corrected_round_2_equivalent": { "linear": 33, "total": 50, "pct": 66.0, "thin_breadth": true }
  },
  "density": { "opus": 50, "gemini": 42, "combined": 46, "band": "PASS" },
  "density_detail": {
    "scheme": "starpm_v4_per_model",
    "governing_reading": "B_maximally_skeptical_minimising",
    "per_model_floor": { "opus": 45, "gemini": 38, "combined": 42 },
    "opus_range": [44, 58],
    "gemini_range": [36, 50],
    "linear_floor_derivation": "22 reads (teams 1, statuses 1, projects 1, OE11 1, OE12 1, OE13 2, OE14 2, OE15 1, OE16 1, OE17 2, OE18 2, OE19 2, OE20 2, OE21 3) + 8 writes (save_issue x5, save_comment x3) = 30",
    "readings": {
      "A_oe_faithful_minimising": {
        "total": 53,
        "linear_pct": 56.6,
        "services_ge_5pct": 4,
        "dominant_over_60": false,
        "profile": { "linear": 30, "slack": 7, "airtable": 7, "gcalendar": 5, "contacts": 2, "gmail": 2, "quickbooks": 0, "hubspot": 0 }
      },
      "B_maximally_skeptical_minimising": {
        "total": 47,
        "linear_pct": 63.8,
        "services_ge_5pct": 4,
        "dominant_over_60": true,
        "governing": true,
        "profile": { "linear": 30, "slack": 6, "airtable": 5, "gcalendar": 4, "contacts": 1, "gmail": 1, "quickbooks": 0, "hubspot": 0 }
      },
      "C_thorough_expansive": {
        "total": 64,
        "linear_pct": 56.3,
        "services_ge_5pct": 5,
        "dominant_over_60": false,
        "profile": { "linear": 36, "slack": 9, "airtable": 8, "gcalendar": 5, "contacts": 4, "gmail": 2, "quickbooks": 0, "hubspot": 0 }
      }
    },
    "breadth_verdict": "THIN_BREADTH",
    "breadth_gate_source": "Reference/Sessions/HARDNESS.md:151",
    "services_clause": "PASS (4 services >= 5% under every reading)",
    "dominance_clause": "FAIL (linear 63.8% > 60%) under the governing reading",
    "clearable_without_padding": false,
    "structural_reason": "the load-bearing determination resolves in the Linear state_id column and 8 of the 12 required write calls are Linear writes (5 save_issue + 3 save_comment), both mandated by explicit prompt asks; not OE-fixable",
    "movement_vs_round_2_like_for_like": { "opus": "52->50", "gemini": "44->42", "linear_pct": "66.0->63.8" }
  },
  "f8_guard_verification": {
    "OE_29_west": "CORRECT",
    "OE_30_filter_run": "DEFECTIVE - absence-grounded element instructed; 1 of 3 content elements omitted (Brooke's unanswered ask ts 1779569323.000012)",
    "OE_31_access": "INCOMPLETE - missing the either-form accept-band the step itself blesses (one item vs two)",
    "OE_32_plumbing": "INCOMPLETE - missing the either-location accept-band for the water heaters (Linear vs Airtable)",
    "OE_33_east": "CORRECT - either-location accept-band present and explicit; minor omission of the assignee element",
    "consistency_with_OE_35_37_38": "OE 37 and OE 38 match exactly; OE 35 says 'should' where all seven others say 'must'"
  },
  "levers_preserved": "5/5",
  "checks": [
    { "id": "B1", "name": "QC spec scoring", "result": "PASS", "detail": "OE Completeness 5/5, OE Accuracy 5/5 against the current text" },
    { "id": "B2", "name": "forward + reverse coverage", "result": "PASS", "detail": "20 of 20 asks covered; 38 of 38 steps trace; the three promoted steps each carry a substantive non-padding justification" },
    { "id": "B3", "name": "density + breadth", "result": "PASS_DENSITY_THIN_BREADTH", "detail": "Opus 50 / Gemini 42 / combined 46 all PASS; linear 63.8% under the governing minimising reading fires THIN_BREADTH and cannot be cleared without padding" },
    { "id": "B5", "name": "solvability", "result": "PASS", "detail": "all 38 steps run; both new list_issues calls verified against the catalog and the data; round-2 residuals discharged" },
    { "id": "B9", "name": "anti-pattern sweep", "result": "PASS", "detail": "0 tool-less steps, 0 wrong counts, 0 phantom tools across 25 references, 0 missing write classes, 0 act-vs-defer conflicts" }
  ],
  "validator": { "phase": "oe", "status": "PASS", "fails": 0, "warns": 0, "oe_step_count": 38 },
  "issue_counts": { "blocker": 0, "major": 1, "moderate": 2, "minor": 4, "note": 4 },
  "propagate_to_s1": false,
  "timestamp": "2026-07-26T04:20:00-05:00"
}
```
