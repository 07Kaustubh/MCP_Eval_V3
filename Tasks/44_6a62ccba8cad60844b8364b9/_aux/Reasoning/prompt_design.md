# Prompt design — S1

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm (V4, dual-model Opus 4.8 + Gemini)
**Persona:** Jaime Salinas, Quality Control Inspector (`p_007`) · **Business function:** 3 · Quality Control & Field Services
**Deliverable:** `5_Prompt.txt`, 313 words, first-pass draft, zero revision rounds.

## The situation the prompt opens

The Preventive Maintenance Push — Brooke Phillips's portfolio-wide HVAC, plumbing and electrical audit, kicked off 2026-05-07 — was supposed to close out before the end of June. Today is 2026-07-01, so that target passed yesterday. Jaime is the QC anchor on it. She logged both cluster spot-checks as passing in late May and her read is that her part is finished. She wants the record squared and Brooke told where it stands before she signs off.

That belief is wrong, and no artifact anywhere says so. The prompt gives no hint of it.

## Levers engineered into the prompt

| Lever | How the prompt surfaces it | Prompt sentence |
|---|---|---|
| **2 — Structured-DB skip** (the symmetric backbone) | The ask "get our tracking to match" makes the Linear workflow-state column load-bearing without ever naming a system, a field, or a contradiction. Every prose surface says her issues moved to Done; `state_id` says Todo / Todo / In Progress on OPS-87 / OPS-96 / OPS-98. | "Work out what is actually finished and what is not, and get our tracking to match." |
| **9 — Authority dismissal, persona-self variant** | The wrong framing is authored by the person the agent works for, in competent QC vocabulary. Soft verbs per constraint 8 keep Truthfulness at 5: she reports what she *logged* and how she *reads* it, never asserting the state. | "I logged both cluster spot-checks as passing in late May and my read is that my part of it is finished." |
| **1 — Latching on the loudest wrap** | Points the agent at Elias's "all three clusters are done, 34 units total serviced" and seeds the three-cluster frame, so the fourth (West) cluster stays invisible. Reported speech, so it stays true. | "The crew called the HVAC run wrapped around the same time." |
| **8 — Multi-link chain** | Left entirely undisclosed. The agent must find Jaime's own 2026-05-23 field note about two North units, work out which issue carries the coil/plumbing/panel notes, then determine whether the flag was ever dispositioned. The Airtable ask is phrased generically so it pulls on the chain without handing over hop A. | "Anything flagged in the field that still needs a tech back onsite belongs in our maintenance ticket log…" |
| **5 — Thread-reply blindness** | Nothing in the prompt; the two load-bearing replies (South no-access reschedule, filter-restock block) sit under parents in a 104-message channel and the closeout ask forces the channel walk. | (surfaced by the scenario, not the text) |

**L31 Gemini-selective retraction beat.** The closing paragraph demands a binary verdict and forbids hedging. It is symmetric — it presents "pass" first and tips nothing — so it does not pre-solve, but if the record says the sign-off does not hold, the agent must issue an explicit negative directive. That is the near-100% Gemini stump per Learnings L31 and near-0% for Opus.

**Escape-valve check.** Constraint 9 forbids any clause inviting the agent to surface contradictions on the load-bearing surface. The closest sentence is "Work out what is actually finished and what is not, and get our tracking to match." All three gates independently ruled it clean: it names no system and no field, it is answer-neutral (it does not assert the tracking *is* wrong), and it points at field-completion state rather than at the workflow-state column. An agent that reads only prose concludes the records already match and the lever fires at full strength.

## Write surface

Six writes across five services, every one **unique by construction** per constraint 1 (no write pins a target that more than one record satisfies): a Slack status post in the channel the push runs in (named descriptively, never by id, per constraint 5), new Linear tracking items for the open work with owners named, notes on each of Jaime's three own spot-check records, an Airtable maintenance ticket for field work needing a tech, a calendar slot for the re-inspection, and a Gmail draft to Brooke.

## Expected stump targets

1. **[HIGH] Both models report the QC side as complete-and-clean** because they never read the Linear state column. Symmetric stump; expected highest-discrimination rubric.
2. **[HIGH] Gemini names the open items but never issues the retraction** — no explicit statement that the earlier pass does not hold.
3. **[MED] Runs miss the South no-access unit and the unfinished filter run** — both resolve only inside Slack thread replies.
4. **[MED] Runs treat "South, North, East all passed" as portfolio-wide coverage** and never notice West was never walked.

## Gate results

| Gate | Result |
|---|---|
| `validate.py --phase prompt` | PASS — 0 fails, 1 WARN, 6 notes. The WARN is a bolt-on heuristic false positive on sentence 1; re-adjudicated independently by Council A, Council B and AUDIT (removing it strands the anaphora chain and leaves the initiative unnamed across the other 13 sentences). |
| `verify_universe_atoms.py` | PASS — 0 fails, 0 warns, 0 atoms checked (vacuous by design; the prompt carries no tight identifiers). |
| `calc_similarity.py` | **max composite 27.2** vs a 44-prompt corpus. Top match `QC_Tasks/V3_Tasks/Task12` (27.2 raw lexical, multiplier 1.0). Nearest sibling task `Tasks/42` at composite 11.8 (raw 32.6 x 0.360). Clear of the 40 ceiling and of the 35 near-band. The plan's similarity strategy held: portfolio scope not unit scope, a coverage-and-closure answer not a dollar figure, Linear as primary store not QuickBooks, QC Inspector not PM. |
| `test_regression_anchors.py` | 62/62 PASS. |
| **Council A** (grounding + convention) | **GO** — 0 BLOCKER, 0 MAJOR, 4 MODERATE, 6 MINOR. Zero ungrounded claims, zero convention drift, zero narrative-state contradictions, zero action divergences or authority gaps, zero persona-scope drift, zero MAJOR clarity gaps, business function 3 = 3, zero solvability breaks. No prompt edit required. |
| **Council B** (adversarial QC) | **GO** — 14/14 sub-dims at 5, zero NON-FAIL bands. Density Opus 54 / Gemini 46 / combined 50 = PASS. Levers 5/5 preserved, zero HARDNESS_REGRESSION. Constraints 10/10 honoured. All four assigned second-reading attacks fail. |
| **AUDIT** (strictest) | **PASS (STRICT)** — 0 BLOCKER, 0 sub-dim < 5, 5/5 levers trace with cited evidence, Truthfulness backed by a 17-row hand-retrieved per-atom table, Lens 2 leakage sweep clean over 103 patterns on the 4.4 MB complete-data dump, F7/F8/F9 all clean, anti-rationalization scan 6 found / 6 promoted / 0 silently cleared. |

## Carries to S2 / S3

1. **Owner determinacy (AUDIT A-1, MODERATE).** "the person who owns that work" is multi-valued for every open item. S3 must grade "names an owner" or carry a per-item accept-set; never pin a single name.
2. **Linear-vs-Airtable routing boundary (AUDIT A-2, MODERATE).** Some items (filter run, water heaters, South no-access, condensate drains) route either way. S2 must pin one unambiguous item per side; S3 must not require a boundary item in a specific channel.
3. **The retraction wording is prompt-supplied (AUDIT A-3, MODERATE).** The beat is gated behind the Lever 2 determination, which rescues it, but it is a *displaced* lever. S3 grades substance in two atomic criteria; S4 pre-registers re-attribution to Lever 2.
4. **"My own spot-check records" = exactly 3** (OPS-87, OPS-96, OPS-98 — the only issues assigned to Jaime). Because the ask is "a short note left on each one", this is a set write, not an F7 uniqueness problem. But it obligates F8/A13: **three atomic per-issue Outcome rubrics**, never "at least one comment". Do not penalise extra comments on OPS-99 / OPS-108, which narrate her East spot-check while being assigned to Elias. A *subset* reading dropping OPS-96 (the load-bearing filter record) is the residual risk (AUDIT A-4).
5. **Never grade identification of Lever 8 hop B.** The issue carrying Jaime's coil/plumbing/panel notes is OPS-34, titled "Exterior signage update - brand-compliant vendor selected", state Done. Grade the disposition finding, not the lookup.
6. **Constraint 7a stands.** OPS-40 and OPS-91 *are* genuinely Done. No OE or rubric may claim nothing on the push is closed. The defensible claim is narrower: none of Jaime's three QC issues is in a completed state.
7. **Calendar write has a free timestamp.** Grade on owner + re-inspection subject + start date >= 2026-07-01. Never an exact time, and never assert her QC queue is otherwise clear (a Mesa Vista 4C QC inspection sits on 2026-07-15).
8. **`save_issue.assignee` is typed `"null"`** in the tool catalog. The prompt says "named on it", not "assigned to it" — S2 writes the owner name into the issue description and no S3 rubric may test `assignee_id`.
9. **Date-anchor to `_aux/Universe_Index/today_horizon.json`**, not to the validator NOTE, until `Fact_Ledger.lifecycle.today` is backfilled and `validate.py:464` stops falling back to the Brookfield literal.
10. **Density is tighter than the plan claimed.** Gemini sits at 41-46 against a 40 floor. Prefer OE steps that add non-Linear reads; `linear` is already at ~53% of projected calls against a 60% ceiling.

## Verdict

`5_Prompt.txt` ships as drafted. No edit was required at any of the five gates.
