# Linter Decision — Task 45 (Mesa Vista 4C prompt)

- Date: 2026-07-27
- Block class: B (similarity)
- Linter complaint: prompt flagged critical, too similar to an existing make-ready QC prompt on Mesa Vista 205B (platform corpus, NOT in the local task set — which is why the local similarity gate at S1 never scored against it).

## Resolution: INVALIDATE (justification pushback)

Ran the multi-dimensional scorer against the 205B text with matching persona + business function (context multiplier 1.0, all constants align, universe unknown so untouched). Composite = 31.5 (< 40). Per-dimension: word-bigram 7.1 (very low — the two prompts phrase the same situation in genuinely different words), unigram 30.8, word-count similarity 81.8. Per the two-band Class B flow (composite < 40 -> INVALIDATE), a justification pushback is defensible rather than a full pivot.

- Justification: `_aux/Linter_Justifications.md` (check_justification.py clean, 0 hits).
- `5_Prompt.txt` UNCHANGED. Justification-only resolution, so per S1.5 no re-run of validator / Council A / Council B / AUDIT is required.

## Honest caveats (operator-internal, NOT for the reviewer)
- The low composite is driven by phrasing. The scenario archetype (QC inspector kicks back a make-ready unit marked done) IS shared, and is inherent to the QC & Field Services function.
- Local Task 43 is the SAME unit (Mesa Vista 4C) make-ready, authored under a different persona/business function (composite 10.1 after the 0.36 multiplier). Not what the platform flagged, but a saturation signal: this function slot is dense (Tasks 39/40/43/44/45 are all make-ready or maintenance QC close-outs).
- Fallback if the reviewer rejects the pushback: scenario pivot. Most distinct option = the HVAC field-service QC scenario (maintenance_hvac_elias), which would need a fresh HARDNESS pass + full redraft + re-run of councils + AUDIT.

## Gate weakness surfaced (worth a fix)
calc_similarity is lexical + local-only. It cannot see a platform-corpus prompt (205B), and it underweights semantic/structural duplication (bigram 7.1 despite the same scenario). A semantic or cross-corpus similarity check would have caught this at S1.
