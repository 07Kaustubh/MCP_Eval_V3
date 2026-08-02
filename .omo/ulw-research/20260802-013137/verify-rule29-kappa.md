VERIFICATION: AGENTS.md rule 29 headline number
====================================================================================================
Rule 29 asserts: '90% raw agreement on a mostly-Fail grid is kappa 0.23, which is fair
and far below the 0.60 conventionally treated as acceptable.'

Reported Task 44 Opus per-run PASS counts out of 60 criteria:
  pass-3 export: [28, 33, 43, 31, 32, 37] -> 204 / 360 = 56.7% Pass
  pass-4 export: [32, 32, 44, 32, 36, 46] -> 222 / 360 = 61.7% Pass
  => grid is 57-62 percent PASS. It is NOT a 'mostly-Fail' grid.

Cross-regrading 2x2 at the reported cell movement:
  cells moved   = 31 (8.6%)  net drift = +18 toward Pass
  2x2           = both-Pass 197 | Pass->Fail 7 | Fail->Pass 24 | both-Fail 132
  Po            = 0.914
  Pe            = 0.515
  Cohen kappa   = +0.822  -> Landis-Koch: ALMOST PERFECT
  Gwet AC1      = +0.833
  PABAK         = +0.828
  PrevalenceIdx = +0.181  (small |PI| => kappa paradox NOT triggered)

What prevalence would make rule 29's number true at 90% agreement?
  kappa=0.23 requires Pass prevalence ~= 2.1% (kappa=0.226)
  i.e. ~98 percent of all decision cells would have to be Fail.

====================================================================================================
VERDICT: REFUTED (as stated). The observed grid yields kappa = +0.822 (almost perfect),
not 0.23 (fair). The kappa paradox is real but is NOT the active failure mode on this
near-balanced grid. Rule 29's DIRECTION -- report chance-corrected agreement rather than
raw percent -- remains CORRECT and is independently supported by arXiv:2606.19544's
finding of universal 33.8-41.3pp kappa deflation across 21 judges. Only the number and
the 'mostly-Fail' premise are wrong.
====================================================================================================
