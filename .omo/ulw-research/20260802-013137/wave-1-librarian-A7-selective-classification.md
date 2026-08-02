# Wave 1 / A7 — Confidence, abstention, calibration for a routing classifier

## Sources
[S26] "Overcoming Common Flaws in the Evaluation of Selective Classification Systems",
      OpenReview 2TktDpGqNM (NeurIPS 2024). Proposes AUGRC. 6 datasets, 13 confidence scoring fns.
[S27] "Trusting the Untrustworthy: A Cautionary Tale on the Pitfalls of Training-based Rejection
      Option", OpenReview DvUEstfH0c.
[S28] Chidambaram & Ge et al., "How Flawed is ECE? An Analysis via Logit Smoothing",
      arXiv:2402.10046 (2024).
[S29] "Hierarchical Selective Classification", NeurIPS 2024 (paper c8b100b3...). >1000 ImageNet
      classifiers.
[S30] Garcia-Galindo et al., "Multi-class Classification with Reject Option and Performance
      Guarantees using Conformal Prediction", PMLR v230:295-314 (COPA 2024).
[S31] Cattelan & Silva, arXiv:2305.15508 — post-hoc confidence estimators, 84 ImageNet classifiers.

## The vocabulary (this is the named pattern the user hand-rolled around)
SELECTIVE CLASSIFICATION == REJECT OPTION == classification with abstention.
  Selection function g_theta(x) = 1[kappa(x, yhat) > theta] where kappa is a CONFIDENCE SCORE.
  COVERAGE phi = fraction of inputs NOT rejected.
  SELECTIVE RISK R = error rate computed ONLY over accepted inputs.
  RISK-COVERAGE (RC) CURVE = risk as a function of coverage. AURC = its area.
  SELECTIVE ACCURACY CONSTRAINT (SAC) [Galil 2023] = the MAXIMUM COVERAGE at which a model
    still meets a specified accuracy. <-- most directly usable single number for a router.
  AUGRC [S26] = 2024 replacement for AURC; range [0, 1/2], lower is better; satisfies five stated
    requirements AURC fails (monotonicity, ranking interpretability, error flexibility, ...).

## Hard findings
- [S31] Some SOTA ImageNet classifiers have EXCELLENT accuracy yet "appallingly poor performance
  at detecting their own mistakes". RC curves can be NON-MONOTONIC (risk rising as coverage
  falls). A simple post-hoc fix (p-norm normalisation of logits, then max-logit as confidence)
  removed the pathology: 2% error went from unreachable at ANY coverage to reachable at 55.3%.
  => Accuracy and confidence-ranking quality are SEPARATE properties. A classifier can be right
     often and still not know when it is wrong. This is the core argument against silent argmax.
- [S27]: temperature scaling significantly DECREASES ECE while AURC stays EQUIVALENT.
  => Calibrating the probabilities does NOT improve the rejection decision. Do not conflate them.
- [S27]: post-hoc rejection methods beat training-based ones and need no architecture change or
  retraining -- the cheap option is also the good option. Also: training-based selective methods
  perform poorly on classes "not necessarily the hardest to classify", and WHICH classes vary
  with random initialisation.
- [S28] on ECE's flaws: it is DISCONTINUOUS in the space of predictors (small prediction changes
  cause large ECE jumps), cannot be efficiently estimated from samples, and binned variants are
  SENSITIVE TO BIN WIDTH. Fixes: Logit-Smoothed ECE (LS-ECE), smECE (Blasiok & Nakkiran),
  splines, isotonic regression, Adaptive Calibration Error (equal-mass bins).
  BUT [S28]'s empirical conclusion: binned ECE closely tracks LS-ECE on CIFAR-10/100 and
  ImageNet, so "the theoretical pathologies of ECE may be avoidable in practice."
- [S30]: CONFORMAL PREDICTION gives a reject option with DISTRIBUTION-FREE guarantees on
  accuracy/recall at a chosen rejection rate, and works with ANY underlying score function --
  it does not require a probabilistic model. Beats both calibrated and uncalibrated probabilistic
  classifiers on 6 multi-class datasets.
- [S29]: when classes form a HIERARCHY, abstention need not be all-or-nothing: "climb" to a
  parent node until confidence clears theta. Reduces specificity instead of refusing.

## Applicability caveat (be honest)
ECE requires probability estimates. A rule-based argmax-over-regex-hit-counts emits NO
probability, so ECE is NOT directly computable and is the wrong first tool. What IS directly
computable on a rule-based scorer:
  - a MARGIN confidence score: kappa = (top1_score - top2_score), or top1/(sum of all scores);
  - an RC curve and SAC over that margin, using labelled fixtures as the eval set;
  - a conformal reject-option wrapper [S30], which needs only a score function and a calibration
    set, not calibrated probabilities.

## EXPAND
- LEAD: SAC (max coverage at target accuracy) as the single reportable number — WHY: gives the
  user one defensible threshold rather than a hand-tuned constant — ANGLE: Galil et al. 2023.
- DEAD END: chasing ECE for a non-probabilistic rule-based router. Wrong tool; margin + RC curve
  + conformal is the right family.
