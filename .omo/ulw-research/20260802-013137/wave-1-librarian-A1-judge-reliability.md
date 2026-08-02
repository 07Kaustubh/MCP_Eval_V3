# Wave 1 / A1 — LLM-judge reliability vs humans + bias catalogue

## Sources
- [S1] "Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge
  Models Across Agreement, Consistency, and Bias" arXiv:2606.19544 (2026).
  21 judges / 9 providers, MT-Bench + JudgeBench + RewardBench, 118 runs, ~541,000 judgments.
- [S2] Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" arXiv:2306.05685v4
  (NeurIPS 2023 D&B). The origin of the position/verbosity/self-enhancement triad.
- [S3] "A survey on LLM-as-a-judge", ScienceDirect S2666675825004564 (2025).
- [S4] "Validating LLM-as-a-Judge Systems under Rating Indeterminacy", NeurIPS 2025 proceedings.
- [S5] "Beyond the Surface: Measuring Self-Preference in LLM Judgments", EMNLP 2025 main #86.
- [S6] "A Systematic Study of Position Bias in LLM-as-a-Judge", IJCNLP 2025 long #18.
- [S7] "Explaining Length Bias in LLM-Based Preference Evaluations", Findings EMNLP 2025 #358.

## Hard numbers
- KAPPA DEFLATION [S1]: raw exact-match agreement overstates chance-corrected agreement by
  33.8-41.3 percentage points on MT-Bench, in ALL 21 judges evaluated. Universal, not model-specific.
- [S2] GPT-4 vs human expert agreement 85% (tie-excluded) vs human-human 81% -> "80%+ agreement,
  same level as humans". THIS IS THE RAW-AGREEMENT NUMBER THAT [S1] SHOWS IS INFLATED.
- Position bias [S1] = |P(A wins) - 0.5| over paired AB+BA. Best Gemini 2.5 Pro 0.002;
  worst Qwen3-8B 0.192. Gemini 2.5 Pro vs 2.5 Flash differ by 70x WITHIN the same family.
  Only 1 of 3 "thinking" judges fell below 0.05.
- Position flip rate literature range 25%-50% [S1 citing Wang 2024, Shi 2025].
  Position-swap debiasing raises within-judge consistency ~60% -> ~85% [Li 2024b].
- Verbosity bias [S1]: ALL 21 judges < 0.011 Pearson (len-diff vs verdict); 17/21 < 0.005.
  An order of magnitude smaller than 2023-era 20-40% variance claims. => verbosity bias has
  LARGELY DECAYED as a practical concern for modern judges (scope caveat: single pairwise rubric).
- Judge rankings NON-TRANSFERABLE: a model shifts up to 14 positions between benchmarks [S1].
- JudgeBench discriminates 4.5x more sharply than MT-Bench (60.4pp vs 13.5pp kappa spread) [S1].
- CONSISTENCY-BIAS PARADOX [S1]: test-retest > 0.95 coexisting with position bias > 0.10 in two
  production judges (Qwen3-8B 0.992/0.192; Gemini 2.5 Flash 0.988/0.125). High stability with
  high bias is a FAILURE MODE, not a strength.
- Self-preference [S2]: GPT-4 +10% own-win-rate, Claude-v1 +25%. [S5] shows the naive delta
  CONFLATES bias with real quality; proposes DBG score = judge score - gold judgment.
  Larger models show LESS self-preference; reasoning models are NOT immune.
- [S4] forced-choice elicitation under rating indeterminacy selects judge systems up to 31% worse
  than response-set (multi-label) elicitation.

## Minimum Viable Validation Protocol (MVVP) [S1] - directly applicable
1. Chance-correct: report Cohen's kappa / Krippendorff alpha as the HEADLINE, not exact match.
2. Swap positions: paired AB+BA, report |P(A wins)-0.5|.
3. Replicate: >=3 independent runs, temperature 0, caching disabled -> test-retest.
4. Cross-validate on >=2 benchmarks with contrasting label structure.
5. Audit the paradox: if test-retest > 0.95, VERIFY position bias < 0.10 before claiming reliability.

## EXPAND
- LEAD: [S4] rating indeterminacy / response-set elicitation — WHY: my councils force a single
  verdict per sub-dimension where multiple are defensible; 31% regret is enormous — ANGLE: fetch
  the NeurIPS 2025 paper, get the exact recommendation ladder (i)-(iv).
- LEAD: JudgeBench vs MT-Bench discriminative spread — WHY: suggests my rubric set's own
  discriminative power is measurable — ANGLE: search JudgeBench construction.
- LEAD: [S1] is arXiv-only (2606.19544) — WHY: needs primary-source verification, not secondary —
  ANGLE: fetch the HTML directly, confirm the numbers and the MVVP text.
- LEAD: "familial patterns" in judge agreement [S6] — WHY: my councils are all the same model
  family, so their mutual agreement is structurally inflated — ANGLE: search intra-family judge
  correlation / judge diversity.
