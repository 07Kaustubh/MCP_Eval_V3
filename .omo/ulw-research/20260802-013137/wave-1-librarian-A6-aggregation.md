# Wave 1 / A6 — Does "aggregate by MIN" have a principled basis?

## ANSWER: yes, it is a named model. MIN across dimensions == the STRICTEST CONJUNCTIVE rule.

## Sources
[S21] Haladyna & Hess, "An Evaluation of Conjunctive and Compensatory Standard-Setting Strategies
      for Test Decisions", Educational Assessment 6(2):129-153 (1999). DOI 10.1207/s15326977ea0602_03.
      THE canonical reference; everything downstream cites it.
[S22] Meyers, "Scoring models in competency-based educational assessment", J Competency-Based
      Education (2018). DOI 10.1002/cbe2.1173.
[S23] Homer & Russell, "Conjunctive standards in OSCEs: the why and the how of number of stations
      passed", White Rose eprint 168283.
[S24] Arnold et al., "Systematic Comparison of Decision Accuracy of Complex Compensatory Decision
      Rules Combining Multiple Tests in a Higher Education Context", EM:IP, DOI 10.1111/emip.12186.
[S25] "Combining Scores in Multiple-Criteria Assessment Systems: The Impact of Combination Rule",
      Gifted Child Quarterly, DOI 10.1177/0016986213513794 — names all three rules explicitly.

## The taxonomy (use these words)
- COMPENSATORY ("mean"): strength in one dimension offsets weakness in another; one cut score on
  the total. Competence is defined as a GLOBAL TRAIT.
- CONJUNCTIVE ("and"): must meet the standard on EVERY dimension (or a stated proportion).
  Competence is defined as a CHECKLIST of specific traits. TAKING THE MIN AND COMPARING TO A
  THRESHOLD IS EXACTLY THIS RULE, in its most extreme "all dimensions" form.
- DISJUNCTIVE / COMPLEMENTARY ("or"): any one dimension clearing the bar suffices.
[S22] states the consequence plainly: "the model selected implicitly defines competence."

## Hard numbers
- [S22]: switching a real university programme from compensatory to conjunctive would FAIL between
  33% and 70% of the students who passed under compensatory, depending on which conjunctive
  variant. Effect grows with the NUMBER of dimensions ("the more hurdles ... the lower the
  likelihood he or she will pass").
- [S24]: the error profile inverts. Conjunctive => LOWER false-positive, HIGHER false-negative.
  Compensatory => LOWER false-negative, HIGHER false-positive. Which is more accurate depends on
  average test reliability, average inter-test correlation, and number of re-examinations.

## Named intermediate variants [S22] — the menu between mean and min
  Model 1 Uniform Cut Score: the overall cut applied to EVERY dimension.
  Model 2 Norm-Referenced Cut: cut per dimension = avg of dimension scores among past passers.
  Model 3 "allow one failure": pass if at most ONE dimension is below cut.
  Model 4 "75% rule": pass if >= 75% of dimensions clear cut.
=> There is a principled ladder between MEAN (fully compensatory) and MIN (fully conjunctive).
   MIN is one end of it, not the only option, and not the default.

## The direct criticism of a MIN rule
[S23] on the OSCE "killer station" (a single station that must be passed, i.e. a MIN rule on one
dimension): "hard to defend psychometrically since a single station-level decision lacks
reliability". And: dichotomising a continuous score into a pass/fail decision "provides a less
reliable measure of performance". Clauser et al. (1996) criterion, quoted approvingly: a
conjunctive hurdle should only be used if it is "of sufficient reliability to ADD INFORMATION to
the resulting decision."
[S23] verdict on the field: conjunctive minimum-number-of-stations standards are "not
sufficiently evidence-based, and is under-theorised ... a lack of underpinning theoretical
argument or justification".
[S23] scope rule: the need for a conjunctive standard is STRONGER when the assessed traits are
clearly MULTI-DIMENSIONAL, and WEAKER when the dimensions are narrowly defined and closely
related (because then total score and per-dimension pass counts correlate strongly anyway).

## Application note for a MIN-of-per-dimension-score extractor
MIN inherits the reliability of its WEAKEST dimension, and it is maximally sensitive to a single
mis-extracted cell: one spurious low score sets the whole verdict. Under [S24] that is precisely
the high-false-negative corner. If the dimensions are genuinely independent hurdles (a real
checklist definition of competence) MIN is defensible and named; if they are correlated facets of
one construct, MEAN or the 75% rule is the better-supported choice.

## EXPAND
- LEAD: "worst-of-CRITICAL-dimensions" is the hybrid [S24] calls a complex decision rule
  (conjunctive minimum + compensatory average TOGETHER) — WHY: user explicitly asked about it,
  and it is the best-supported design — ANGLE: fetch EM:IP 12186 for the exact rule form.
- LEAD: binary QC sub-dimensions in the user's own spec are already a conjunctive standard —
  WHY: their 10 binary sub-dims ARE "killer stations" — ANGLE: codebase axis.
