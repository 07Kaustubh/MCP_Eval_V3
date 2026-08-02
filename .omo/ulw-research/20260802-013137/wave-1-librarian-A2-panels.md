# Wave 1 / A2 — Panel / jury of judges (PoLL)

## Source
[S8] Verga, Hofstatter, Althammer, Su, Piktus, Arkhangorodsky et al. (Cohere),
"Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models",
arXiv:2404.18796 (2024-04-29). 3 judge settings, 6 datasets.

## Hard numbers + mechanism
- PoLL = Command R (Cohere) + Claude 3 Haiku (Anthropic) + GPT-3.5 (OpenAI).
  DELIBERATELY three DISJOINT model families, and deliberately the SMALLER model of each family.
- Correlates BETTER with human judgement than a single GPT-4 judge.
- Cost: PoLL $1.25/M in + $4.25/M out vs GPT-4 Turbo $10/M in + $30/M out => 7-8x cheaper.
- Variance: PoLL score spread std dev 2.2 vs GPT-3.5 alone 6.1 (delta vs human annotators).
- Voting function f: MAX voting for binary [correct/incorrect]; AVERAGE POOLING for 1-5 scales
  (a 3-judge panel often yields no clear majority on a 5-point scale). Max-voting-with-average-
  fallback gave identical overall ranking.
- Intra-model bias made visible: "the highest positive delta for each individual model being
  scored occurs when it is judged by itself". GPT-4 judge ranked a GPT-4 variant at position 2
  when its true Arena-ELO position was 4.
- "There is not a single 'best' judge across all settings" — judge choice does not transfer.
- GPT-4 as judge shows HIGH VARIANCE to minor prompt changes (Section 4.3).

## The load-bearing caveat for this project
The ENTIRE benefit is decorrelation across DISJOINT FAMILIES. Pooling N judges from the SAME
family/model does not decorrelate anything — [S6] "familial patterns" shows same-series judges
agree 70-85%+, i.e. a same-model panel is close to one judge run N times. Authors also restrict
the claim to factoid QA + preference ranking and explicitly flag math/reasoning as UNVERIFIED.
Panel selection is left to future work.

## EXPAND
- LEAD: "panel selection" is an open problem — WHY: user must choose panel members — ANGLE:
  search post-2024 work on judge/panel selection, judge diversity metrics.
- LEAD: Does a panel of same-model-different-prompt personas buy anything? — WHY: that is exactly
  the user's council design (Council A / Council B, same Opus) — ANGLE: search multi-agent debate
  / self-consistency vs true model diversity; look for negative results.
