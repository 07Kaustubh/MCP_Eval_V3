# Wave 1 / A4 — Criteria drift in rubric-based LLM evaluation

## Source
[S9] Shankar, Zamfirescu-Pereira, Hartmann, Parameswaran, Arawjo,
"Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human
Preferences", UIST 2024, arXiv:2404.12272, DOI 10.1145/3654777.3676450. n=9 industry practitioners.
[S10] Arawjo, "EvalGen: Helping Developers Create LLM Evals Aligned to Their Preferences",
Medium 2025-05-14 (retrospective, names downstream adopters: LangSmith, Autoblocks, Chroma).

## The finding, verbatim
CRITERIA DRIFT: "users need criteria to grade outputs, but grading outputs helps users define
criteria" — a catch-22. Consequence stated by the authors: "it is impossible to completely
determine evaluation criteria prior to human judging of LLM outputs." Even participants who
graded FIRST still refined criteria on further grading, and went back to CHANGE PREVIOUS GRADES.

Two distinct drift types:
 1. ADDITIVE drift — new criteria wanted once a new *type* of bad output is observed (5/9 users).
 2. REINTERPRETIVE drift — the definition of an EXISTING criterion silently changes (5/9 users).
    Canonical example: a "proper noun" criterion initially meant ALL extracted entities must be
    proper nouns; after seeing outputs, users wanted MOST. Same criterion text, different rule.

Also observed: P8 graded an output BAD "not because they believed the output was bad, but
because they wanted to be consistent with previous grades" — consistency pressure corrupting
the label. Authors: good labeling practice, "but not good for alignment."

## Why this is fatal to a settled-criteria pipeline
Authors explicitly name AutoCalibrate as the contrast case: methods that "require large
expert-labelled datasets with settled (i.e., established upfront) criteria". Their finding is
that criteria are DEPENDENT on the specific outputs observed, not independent. Therefore any
change to the pipeline (new model version, prompt edit, upstream change) can itself cause
criteria drift. Recommendation: criteria refinement and grading must happen IN TANDEM, with
interfaces supporting rapid simultaneous iteration over criteria AND implementations.

## Design lessons EvalGen shipped after the study [S10]
- Grade PER-CRITERION, not overall thumbs up/down.
- Allow free navigation backwards to edit criteria at any point.
- FORCE a few free-text feedback responses BEFORE criteria definition — a cognitive forcing
  function that helps users externalise what matters.
- Known limit: EvalGen emits assertions (true/false) only, not numeric/categorical scorers.

## EXPAND
- LEAD: the "proper noun ALL vs MOST" drift is nearly identical to a rule in the user's own repo
  (recent commit: "proper noun detection excludes sentence-initial capitalization") — WHY: strong
  evidence the user has independently rediscovered reinterpretive drift — ANGLE: codebase axis.
- LEAD: downstream productionisation (LangSmith, Chroma generative benchmarking) — WHY: shows what
  the industry actually shipped in response — ANGLE: search those features.
- LEAD: SPADE (assertion generation from prompt revision history) — WHY: auto-derives assertions
  from *diff history*, which the user has (git) — ANGLE: search SPADE Shankar.
