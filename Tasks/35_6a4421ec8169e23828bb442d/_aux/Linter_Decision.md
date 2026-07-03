# Linter Decision — Task 35_6a4421ec8169e23828bb442d

**Date:** 2026-07-01
**Mode:** CB
**Prompt file:** `5_Prompt.txt` (unchanged; 397 words; AUDIT v2 PASS_STRICT already on file at `_aux/Council_Reports/AUDIT_prompt_v2.md`)

## What the linter blocked

Platform linter fired one Class A block: Business Function pattern-fit mismatch. The linter reported the prompt as "not consistent with the Executive & Risk Oversight function" and cited the following gaps: no Brookfield personas (expected Steven Perry / Matthew Li / Andrea Phil / William White), no Brookfield systems (expected BlackLine / Oracle GL / SAP / Records Vault / Airtable / Linear), no Brookfield retention codes (AICPA_SQMS_7Y etc.), incorrect legal counsel routing (expected Linda Burns), incorrect SAR framing (expected Cat 4.1-4.2 AML anchored to Marina Soko), no match to Executive sub-patterns 9.1-9.4. The linter's own summary characterizes this as "wrong universe entirely" and recommends invalidation as uncorrectable.

## Skeptical-first reasoning

Every single linter flag traces to a single categorical mistake by the linter itself: it ran the **Brookfield** rulebook against a **KeyStone Mortgage Partners** universe task.

- `_aux/Universe.txt` was written by `Validators/detect_universe.py` at S0 and returns `keystone`.
- Persona `Robert Calloway` (Owner / Licensed Mortgage Broker) is a KeyStone authoring persona per `Mortgage_Base_Universe/3_Persona_Briefs.md`.
- Business Function `Executive` is a KeyStone Function per `Mortgage_Base_Universe/5_Task_Categories_Business_Functions.md` (10% target for KeyStone).
- Anchoring scenario `scenario_14b3ffde` (ransomware pay-vs-restore) is a KeyStone-native scenario.
- All referenced systems (LOS, email, Slack, CRM, filesystem, contacts) are KeyStone-native services per `Mortgage_Base_Universe/6_Server_Tools_Details.json`.
- Outside cyber counsel `Megan Sloane at wardbarrettlaw.com` is a real KeyStone contact seeded in `contacts.contacts.json`; the Bennett-* variants are Hardness Plan §L4 near-miss decoys, not the intended recipient.
- Suspicious-activity filing (SAR) language references FinCEN SAR obligations under BSA that apply to mortgage originators, which the KeyStone universe encodes via Denise Holloway's 3/20 privileged emails (grounded verbatim in `email.emails.json :: email_email_fc27f9914e8b`).
- All three of my pre-linter gates (Council A v2 GO, Council B v2 GO with 12/12 sub-dims at 5/5, AUDIT v2 PASS_STRICT) evaluated the prompt against the KeyStone rulebook and confirmed alignment.

The linter is clearly wrong on the categorical claim. Every downstream gap it lists is a consequence of the initial universe-detection error, not a defect in the prompt.

## Action taken

**INVALIDATE with justification** (Class A, per S1.5 skeptical-first decision flow — clearly-wrong disposition).

- Justification written to `_aux/Linter_Justifications.md` (4 sentences, first-person Robert voice, cites persona / date / concrete counsel contact, no em-dashes).
- `Validators/check_justification.py` exit 0 — zero hits on any forbidden-term category.
- Cross-task log appended at `Tasks/_meta/Linter_Justifications.md` with the linter excerpt + root-cause diagnosis + reviewer-response placeholder.
- No edit to `5_Prompt.txt`. The prompt remains at 397 words with all prior gates cleared (Validator PASS, Council A v2 GO, Council B v2 GO 12/12 at 5/5, similarity max 28.4, AUDIT v2 PASS_STRICT).
- AUDIT not re-run this pass (justification-only resolution, no prompt artifact changed).

## Final state

- `5_Prompt.txt` unchanged.
- Justification ready for platform submission.
- If the platform re-check clears, invoke `PIPELINE S2 — Tasks/35_6a4421ec8169e23828bb442d` in a fresh chat.
- If the platform re-check blocks again (either same flag or new), invoke `PIPELINE S1.5 — Tasks/35_6a4421ec8169e23828bb442d` in a fresh chat and paste the new linter output.
