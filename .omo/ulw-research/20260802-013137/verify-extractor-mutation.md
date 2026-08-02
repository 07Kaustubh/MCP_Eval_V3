MUTATION TEST OF THE Score:N/5 EXTRACTOR  (truth for every mutant below = 2)
================================================================================================================
BASELINE (canonical form)                                    -> 2   [truth 2]  OK

  trailing rationale on the low line       -> 4     WRONG (4)    [per-dimension n=2]
  em-dash rationale on the low line        -> 4     WRONG (4)    [per-dimension n=2]
  bold markdown around the low line        -> 4     WRONG (4)    [per-dimension n=2]
  markdown list bullet                     -> 4     WRONG (4)    [per-dimension n=2]
  table row form                           -> 4     WRONG (4)    [per-dimension n=2]
  space before slash                       -> 2     ok           [per-dimension n=3]
  'out of 5' spelled out                   -> 4     WRONG (4)    [per-dimension n=2]
  trailing CR (CRLF file)                  -> 2     ok           [per-dimension n=3]
  trailing whitespace                      -> 2     ok           [per-dimension n=3]
  lowercase 'score:'                       -> 4     WRONG (4)    [per-dimension n=2]
  'Score - 2/5'                            -> 4     WRONG (4)    [per-dimension n=2]
  nbsp after colon                         -> 2     ok           [per-dimension n=3]
  score of 0 (out of stated range)         -> 4     WRONG (4)    [per-dimension n=2]
  quoted example inside prose              -> 2     ok           [per-dimension n=3]

================================================================================================================
RESULT: 9/14 mutants mis-scored or silently skipped. Mutation score = 36%
================================================================================================================

Now: does the AGGREGATE guard hold, and does a PARTIAL match fail loudly?
  3 dimensions present, only 2 parseable, the LOWEST is the unparseable one:
    -> returns 4 via [per-dimension n=2]   TRUTH IS 2.
    The extractor reports a CONFIDENT 4 and never signals that a dimension was dropped.
    This is the silent mis-score the design was meant to avoid: MIN over a SUBSET is not MIN.
