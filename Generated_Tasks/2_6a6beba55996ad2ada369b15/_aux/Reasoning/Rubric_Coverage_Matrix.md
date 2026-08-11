# Rubric Coverage Matrix — S3 (`2_6a6beba55996ad2ada369b15`)

Universe **harmonygames** (framework `hg`) · persona **Robert** · today **2026-02-28** America/Chicago · model under test **Claude Opus 4.7**

| Gate | Result |
|---|---|
| `validate.py --phase rubrics` | PASS, 0 fails, 0 warns |
| `check_rubric_antipatterns.py` | OK |
| `check_ordering_coverage.py` | OK, 1 ordering construction, 1 Process carrier |
| `check_oe_rubric_sync.py` | OK |
| `check_qc_binary.py` | 6/6 measurable binary sub-dims PASS |
| `test_regression_anchors.py` | 89/89 |
| Council A (grounding) | GO |
| Council B (adversarial) | GO on round 2, after one Major fixed in place |
| AUDIT (strictest) | **PASS (STRICT)** on the first round. All twelve applicable Rubric sub-dims at 5, zero BLOCKER, all five hardness levers trace end-to-end, density midpoint 40 to 43 across 5 services on the HarmonyGames bands. |

Set shape: 25 criteria. Outcome 1.1 = 3, Outcome 1.2 = 18, Outcome 2.1 = 3, Process = 1. Process share 4 percent against the HarmonyGames flat cap of 40 percent. 25 of the 60-criterion project ceiling.

## Forward map: every prompt ask reaches a criterion

| Prompt line | Ask | OE step(s) | Criteria |
|---|---|---|---|
| 1 | Context. Leonard's angel calls, Robert's ownership of the design, "somebody should write down what the data actually said" | OE 1, OE 2 | none required (framing, no independent ask) |
| 3 | "the whole life of that game, from its first day with players to the last day there is anything to look at" | OE 3, OE 4, OE 9 | 2 |
| 3 | "work out how it genuinely performed" | OE 4, OE 5, OE 6 | 3, 5 |
| 3 | "and what we paid to put players in front of it" | OE 8 | 4 |
| 3 | "Some of that will read better than I expect and some worse, so don't smooth it out" | OE 4, OE 5 | 3 and 5 jointly. The bad side is graded by requiring 0.00, the good side by requiring an engagement figure. Graded as figures the account states, never as a criterion about what the agent refrains from doing, which would be a negatively framed criterion under HG QC dimension 23. |
| 5 | "find out whether anything is still quietly running on our side" | OE 9, OE 10, OE 11 | 6 |
| 5 | "that list got put together fast and nobody has been back over it properly" | OE 13 | 19 (the tracking item's subject must be the paid acquisition, not an item already on the wind down list) |
| 5 | "Whatever is still taking money from us needs naming with a figure against it" | OE 10, OE 11 | 6, 17, 20 |
| 5 | "and an owner" | OE 12 | 7, 21 |
| 7 | "I know roughly what we are getting for the data" | OE 14, OE 15 | 8 |
| 7 | "and I know who we still owe" | OE 16 | 12 (the verdict is graded against the named obligation stack; no criterion demands a closed total, because SVB is unquantified and Unity is stated as an unlabelled rate) |
| 7 | "whether that genuinely covers shutting down in an orderly way" | OE 16b, OE 17, OE 18 | 9, 10, 11, 12 |
| 7 | "Tell me where that actually leaves us and be precise about it" | OE 18 | 24 |
| 9 | "Write it up as one honest account ... somewhere it will outlast our accounts going dark" | OE 20 | 1 |
| 9 | "Then post it to him and Arthur in the wind down channel" | OE 19, OE 21 | 13, 14, 15, 16, 17 |
| 9 | "Then post it" (the ordering the word Then creates) | OE ordering clause | 25 |
| 9 | "and file a tracking item for whatever is still costing us so it does not get lost between the three of us" | OE 22 | 18, 19, 20, 21 |
| 11 | "Then tell me the two or three figures you would lead with" | OE 23 | 22, 23 |

## Reverse map: every criterion traces to a prompt ask

| # | Category | Criterion, short | Authorizing prompt language |
|---|---|---|---|
| 1 | Outcome 1.1 | standalone page or document created | "Write it up as one honest account ... somewhere it will outlast our accounts going dark" |
| 2 | Outcome 1.2 | window 2026-01-05 to 2026-02-09 | "from its first day with players to the last day there is anything to look at" |
| 3 | Outcome 1.2 | 0.00 lifetime revenue | "work out how it genuinely performed", "don't smooth it out" |
| 4 | Outcome 1.2 | 7,483.42 lifetime acquisition spend | "what we paid to put players in front of it" |
| 5 | Outcome 1.2 | one engagement figure from a closed set | "how it genuinely performed", "some of that will read better than I expect" |
| 6 | Outcome 1.2 | 8,452.64 charged since 2026-02-09 | "whether anything is still quietly running", "needs naming with a figure against it" |
| 7 | Outcome 1.2 | Leonard Hayes controls the ad accounts | "and an owner" |
| 8 | Outcome 1.2 | 10,800 net proceeds | "I know roughly what we are getting for the data", "be precise about it" |
| 9 | Outcome 1.2 | 2,500 cash on hand | "Tell me where that actually leaves us and be precise about it" |
| 10 | Outcome 1.2 | approximately 15,000 wind-down service | "whether that genuinely covers shutting down in an orderly way" |
| 11 | Outcome 1.2 | wind-down cost alone exceeds net proceeds | same sentence. This is the sharpest discriminator in the set: Leonard's own "the data will likely cover our costs" is true against the 22,500 gross and false against the 10,800 net. |
| 12 | Outcome 1.2 | account concludes funds fall short | "I don't have a straight answer on whether that genuinely covers shutting down in an orderly way" |
| 13 | Outcome 1.1 | posts in #winddown | "Then post it to him and Arthur in the wind down channel" |
| 14 | Outcome 1.2 | addresses Leonard Hayes and Arthur Blake | "to him and Arthur" |
| 15 | Outcome 1.2 | points to the written account | "post **it**", where it is the account of the previous clause |
| 16 | Outcome 1.2 | message states funds fall short | "post it", read as delivering the account's substance to the founders who need it for the calls |
| 17 | Outcome 1.2 | message states 8,452.64 | "Leonard, Arthur and I are personally on the hook here", the exposure the post exists to surface |
| 18 | Outcome 1.1 | files a tracking item | "file a tracking item for whatever is still costing us" |
| 19 | Outcome 1.2 | subject is the still-running paid acquisition | "for whatever is still costing us", resolved by the records to paid user acquisition |
| 20 | Outcome 1.2 | tracking item carries 8,452.64 | "needs naming with a figure against it" |
| 21 | Outcome 1.2 | tracking item names Leonard Hayes as owner | "and an owner", "so it does not get lost between the three of us" |
| 22 | Outcome 2.1 | two or three lead figures given | "tell me the two or three figures you would lead with" |
| 23 | Outcome 2.1 | each lead figure drawn from the records | same sentence. Stated as an objective open semantic rule rather than a closed list, so an agent leading with a grounded engagement figure is not false-failed. |
| 24 | Outcome 2.1 | final response reports funds fall short | "Tell me where that actually leaves us and be precise about it" |
| 25 | Process | account completed before the post | "Write it up ... **Then** post it" |

No criterion grades a requirement that exists only in the Oracle Events. No prompt ask is left ungraded.

## Same fact on different artifacts: coverage, not duplication

Two facts are deliberately graded three times each, on three different deliverables. `Evals_harmonygames/3_Rubrics_Eval.md` Phase 3.1 is explicit that a fact required inside one deliverable is not covered by a criterion on a different deliverable, and that such a pair is not redundant because the actions differ.

| Fact | Written account | #winddown post | Final response |
|---|---|---|---|
| Funds fall short of the named costs | 12 | 16 | 24 |
| 8,452.64 still running | 6 | 17 | 20 (tracking item) |
| Leonard Hayes as owner | 7 | — | 21 (tracking item) |

## Nesting check (project rule 17)

Criteria 2 to 12 are bound to "The Agent's written account", which criterion 1 creates. Criteria 14 to 17 are bound to "The Agent's #winddown message", which criterion 13 creates. Criteria 19 to 21 are bound to "The Agent's tracking item", which criterion 18 creates. Each dependent names its subject artifact by content, so a run that fails the antecedent cannot pass the dependent, and the binding survives renumbering. The account criteria and the post criteria are unnested: no single agent act satisfies one from each group, which is directive 6 from `_aux/Reasoning/OE_solvability.md`.

Deterministic confirmation of this is unavailable until S4: `check_criterion_dependencies.py` needs a verifier export and currently SKIPs. Re-run it at S4 before classifying any all-failing criterion.

## Signal check deferred

`check_rubric_signal.py` also SKIPs with no verifier export. The set is at 25 of the 60 ceiling with no trim pending, so nothing had to be cut on signal grounds at this phase. Run it at S4 to identify zero-discrimination criteria before any future trim, per project rule 28.
