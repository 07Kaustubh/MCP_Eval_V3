# Reads — S1

Every spec doc / reference card / eval consulted this phase, one line each.

## QC spec + framework docs
- `Docs_starpm/9_Common_Error.md` :: Part 1 prompt-writing errors read BEFORE drafting per S1 runbook. Confirmed the 7 error classes: over-specificity, sequential command lists, tool/parameter names, pre-solving, bolted-on asks, every-task-ends-in-email, too-short prompts. Draft checked against each.
- `Docs_starpm/6_Prompt_Relative_Time_Updates.md` :: DATE SSOT. Universe today = 2026-07-01 (Wednesday). Confirms relative-time phrasing is permitted and that "it is now July" resolves correctly. Also confirms Jul 1 is the Q3/H2 boundary, which is coherent with a missed end-of-June deadline.
- `Docs_starpm/7_QC_Spec_Doc1.json` :: Prompt-dimension sub-dims + which are BINARY (Tool use & Cross-service, Investigation, Coherence, Alignment with Today's Date). Delegated per-sub-dim scoring to Council B-B1.

## Reference cards
- `Reference/Sessions/S1.md` :: phase contract, 9-step procedure, exit criteria, conditional AUDIT auto-fire (Track F v21).
- `Reference/Prompt_Format.md` :: hard rules (500-word cap, no em-dash, no tool names, no MCP-server names, no internal IDs, no pre-solving, first person, one coherent situation), voice principles (mid-thought entry, asymmetric knowledge), 3-movement structure (Trigger / Context / Asks), anti-pattern list.
- `Reference/Council_Protocol.md` :: Council A perspectives A1-A13 (A5/A8/A9/A12 retired), Council B B1-B11, role-lens anchoring, sub-dimension scoring scheme map, unified JSON verdict format. Confirmed StarPM density is per-model 40+/15, NOT the V3-family 50/40.

## Eval specs
- `Evals_starpm/1_Prompt_Eval.md` :: routed to Council B as the phase eval; 12 prompt sub-dims scored there.

## Reference corpus (voice / structure)
- `QC_Tasks/V4_Tasks/QC_Passed/Task1..Task4/5_Prompt.txt` :: 4 QC-passed V4 prompts read end to end. Extracted pattern: name the deliverable surfaces explicitly, leave the investigation surfaces implicit; generic write licenses ("anything that needs fixing", "whatever reminders we need") rather than named defects; mid-thought entry; persona states what they already believe.

## Per-task inputs
- `Tasks/46_.../1_Business_Function.txt` :: Property Operations.
- `Tasks/46_.../2_Persona.txt` + `PersonaBrief.txt` :: Lisa Smith, Onsite Property Manager, p_002, warm-professional / thorough / calm, formality 0.60 verbosity 0.55.
- `Tasks/46_.../_aux/Hardness_Plan.md` :: 5 selected levers (L2, L10, L11, L1, L7), the L36 withholding table (governing constraint), single-target uniqueness exclusions, per-model density projection (Opus 63.5 / Gemini 66.0).
- `Tasks/46_.../_aux/Universe_Index/today_horizon.json` :: universe_today 2026-07-01, America/Chicago.
- `Tasks/46_.../_aux/Universe_Split/*` :: grounded every named atom (see Verification_s1.md).

## Validator source read (to resolve a FAIL correctly rather than by guessing)
- `Validators/validate.py:87 SERVICE_KEYWORDS` :: read the actual detection map to satisfy the cross-service gate from DELIVERABLE surfaces only, preserving lever L2. Confirmed `gcalendar` matches only the literal "Google Calendar", so plain "calendar" never counted.
- `Validators/validate.py:546-561` :: bolt-on detector. Confirmed the WARN was a regex artifact (consecutive-capital tokenization made "The Harris" != "Harry Harris"), fixed structurally rather than suppressed.
- `Validators/validate.py:472` :: **DEFECT FOUND** — hardcoded Brookfield fallback `"2026-06-12"` when `Fact_Ledger.lifecycle.today` is null. Surfaced, not patched (touches frozen regression hashes).
