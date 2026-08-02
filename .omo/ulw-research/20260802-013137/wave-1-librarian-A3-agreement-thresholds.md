# Wave 1 / A3 — Inter-rater agreement thresholds + the kappa paradox

## Sources
[S11] Krippendorff, "Computing Krippendorff's Alpha-Reliability", UPenn repository (2011).
[S12] Wikipedia "Krippendorff's alpha" (restates the canonical bands + the q failure-probability).
[S13] Artstein & Poesio, "Inter-Coder Agreement for Computational Linguistics", CL 34(4) 2008
      (J08-4004) — the canonical CL survey.
[S14] Wong, Paritosh, Aroyo, "An Empirical Approach to Interpreting Inter-rater Reliability",
      ACL 2021 long #548 — the xRR framework. 4M human judgements released.
[S15] "Observer agreement paradoxes in 2x2 tables: comparison of agreement measures",
      BMC Med Res Methodol, PMC4236536.
[S16] "Kappa and Beyond: Is There Agreement?", Global Spine J, SAGE 10.1177/2192568220911648.
[S17] "High Agreement and High Prevalence: The Paradox of Cohen's Kappa", Open Nursing J 11:211 (2017).
[S18] "Gwet's AC1 is not a substitute for Cohen's kappa - A comparison of basic properties",
      PMID 37234937 (2023). <-- COUNTER-SOURCE.
[S19] Gwet, "Computing inter-rater reliability and its variance in the presence of high agreement",
      Br J Math Stat Psychol (origin of AC1).
[S20] Braylan et al., "Measuring Annotator Agreement Generally across Complex Structured,
      Multi-object, and Free-text Annotation Tasks", arXiv:2212.09503.

## The canonical bands (report these verbatim)
KRIPPENDORFF'S ALPHA [S11][S12] — the stricter, and the one Krippendorff himself set:
  alpha >= 0.800            -> rely on it; firm conclusions.
  0.667 <= alpha < 0.800    -> TENTATIVE conclusions only.
  alpha <  0.667            -> discard; Krippendorff calls 0.667 the "lowest conceivable limit".
LANDIS & KOCH (1977) KAPPA — the looser, and the one most cited:
  0.21-0.40 fair · 0.41-0.60 moderate · 0.61-0.80 substantial · >0.80 almost perfect.
  Convention: "above 0.6" is the publishable floor.
Krippendorff also defines q = P(alpha fails to reach a chosen alpha_min), bootstrapped
(10,000 samples typical). Worked example [S11]: ordinal alpha .7598, CI [.7078,.8078] ->
q(alpha_min=.80) = 0.9473 (i.e. almost certainly below .80) but q(alpha_min=.70) = 0.0125.
=> Report the failure probability against YOUR chosen minimum, not just the point estimate.

## Which coefficient (decision rule) 
Cohen's kappa: EXACTLY 2 raters, no missing cells, nominal/weighted-ordinal. Allows the two
  raters to have DIFFERENT marginals (Cohen believed raters are not interchangeable).
Fleiss' kappa: 3+ raters, nominal only, complete balanced data. (Actually generalises Scott's pi.)
Krippendorff's alpha: any number of raters, any measurement level, MISSING DATA NATIVELY.
  Reduces to Scott's pi (2 raters nominal), Spearman rho (2 raters ordinal, no ties),
  and the intraclass correlation (2 raters interval). Default to alpha when in doubt.
Note [S13]: choosing kappa-style (individual marginals) vs pi/alpha-style (pooled) "can lead to
reliability values falling on different sides of the accepted 0.67 threshold" -> report both.

## THE KAPPA PARADOX — the decisive finding for this project
Paradox 1: LOW kappa despite HIGH observed agreement, under symmetrically imbalanced marginals.
Paradox 2: HIGHER kappa for ASYMMETRICALLY imbalanced marginals (backwards from what is wanted).
Trigger threshold [S17]: the paradox "begins to be evident for values of prevalence higher
than 60%" — at equal sensitivity/specificity of raters, in the simple 2-rater 2-outcome case.
Worked example [S16]: Po = 68% observed agreement with a "quite low" kappa.

Fixes on offer:
 - PABAK (Byrt et al.) = 2*Po - 1. Prevalence- and bias-adjusted. Purely a function of Po,
   so it does NOT move with prevalence or bias at all.
 - Byrt et al. also say: when reporting kappa, ALSO report the Bias Index (BI) and
   Prevalence Index (PI). BI = 0 iff the marginals are equal; PI in [-1,+1], 0 iff categories
   equiprobable.
 - Gwet's AC1 [S19]: same shape as kappa but Pe uses the AVERAGE of marginal probabilities;
   formally the conditional probability that two random raters agree GIVEN agreement is not by
   chance. Robust to paradox 1.
 - Bangdiwala's B-statistic: [S15] concludes B "came closest to resolving both paradoxes than
   any of the other indices" and recommends B + the agreement chart for 2x2.

## CONTRADICTION (unresolved in the literature, must be reported as such)
[S17] concludes "it would always be appropriate to adopt the AC1 statistic".
[S18] (2023) rebuts: AC1 and kappa use different comparators — kappa compares to expected
AGREEMENT, AC1 to expected DISAGREEMENT. Therefore for a FIXED agreement rate, AC1 INCREASES as
prevalence departs from 0.5 while kappa DECREASES. AC1 can be positive OR negative when there is
NO association between raters, where kappa is exactly 0. Conclusion: "Gwet's AC1 should not be
seen as a substitute for Cohen's kappa. In particular, the verbal classification of kappa values
by Landis & Koch should not be applied to Gwet's AC1."
=> RESOLUTION FOR PRACTICE: AC1 is not a drop-in replacement and must NOT be read against
Landis-Koch bands. The defensible move is to report Po + PI + BI + kappa TOGETHER (Byrt),
which is exactly what every source agrees on, and to treat a large PI as the explanation for a
low kappa rather than silently swapping in a friendlier coefficient.

## The threshold-is-contextual counter-position [S14]
ACL 2021 argues absolute Landis-Koch thresholds are "too rigid and too stringent" for modern
data-from-the-wild, with measured real-world IRR: toxicity judgement 0.2-0.4; facial emotion
>80% of values BELOW 0.6; A/B user-preference testing typically 0.3-0.5. Proposes xRR
(cross-replication reliability): benchmark IRR against a REPLICATION of the same corpus rather
than an absolute constant. Also notes SQuAD, ImageNet and Freebase never reported IRR at all.
[S20] independently: alpha's "threshold for acceptable agreement varies greatly by task and
distance function", making a fixed cut-off unusable for complex/structured annotation.

## EXPAND
- LEAD: xRR replication-baseline framing — WHY: the user HAS replications (two independent
  regradings of byte-identical trajectories) so xRR is computable today — ANGLE: fetch ACL 2021
  paper for the xRR definition/formula.
- LEAD: Bangdiwala B-statistic + agreement chart — WHY: best paradox resistance per [S15] —
  ANGLE: get the formula; check stdlib implementability.
- DEAD END: searching for a single universally accepted numeric threshold. There is none; the
  literature actively rejects one. The defensible artifact is the BAND + the failure probability
  q + the paradox diagnostics.
