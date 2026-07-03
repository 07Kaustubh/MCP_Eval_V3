# AUDIT prompt (STRICTEST interpretation) — Task 37 ORIGINAL

**Scope:** Candidate's `5_Prompt.txt` — read strictly, every "should" as "must".

## Programmatic floor
- `verify_universe_atoms.py`: **PASS** (0 fails, 39 atoms checked) — persona `Sofia Reyes / sofia.reyes@keystonemortgage.com`, 26 active pipeline loans, terminated LO landmines, and compliance-recipient emails all grounded.
- `validate.py --phase prompt`: **PASS** (0 fails, 3 warns, 6 notes)
  - Word count 343 (within 500 cap; within sweet spot)
  - No em-dashes
  - No tool names in prompt body

## Strict lens checks

### 1. Answer leakage / pre-solving (Prompt Eval 1.3)
- Counts hidden: no "26", no "5 terminated-LO loans", no lender names, no document counts.
- Loan IDs hidden: no `LN-YYYY-NNNNN` strings in prompt.
- Named entities: Grace (boss), Camille (locks), Carlos/Derek/Keisha (LOs), Elena/Denise (compliance escalation). Sofia knows all of these — natural for a Processor persona.
- **Verdict: PASS strict.**

### 2. Bolt-on sentence check (WARN-flagged 3 candidates)
Applied remove-sentence test to each WARN:

**Sentence A** — "Check what's been going on with each of these loans, look at any recent email threads or Slack discussions about them, and figure out exactly what's blocking progress on each one."
- Coherent with the surrounding investigation ask (per-loan blocker discovery). Removing it would gut the discovery lever ("look at recent email threads or Slack") that drives ~40% of the tool budget. **NOT a bolt-on.**

**Sentence B** — "Reach out to Carlos, Derek, Keisha, and any other LO with active files in my queue..."
- Directly introduces the LO-notification deliverable that dominates the OE + rubric set. Removing it leaves Grace and Camille as the only outreach targets — the LO-notification lever collapses. **NOT a bolt-on.**

**Sentence C** — "If anything you find looks like it could be a compliance concern, flag it separately for Elena and Denise with specifics."
- Introduces the compliance-escalation lever tied to the phishing/TRID/terminated-LO scenarios. Conditional escalation is a defensible pattern (the prompt implicitly permits "if no concerns, don't send"). Removing it eliminates a discoverable hardness lever. **NOT a bolt-on.**

- **Verdict: PASS strict — all 3 WARNs are false positives.**

### 3. Contrived / command-list smell
- Prompt uses natural boss-panic register ("Grace just told me... 3 pm today... Camille flagged me this morning... putting out fires").
- No numbered list, no "run tool X then tool Y" language.
- **Verdict: PASS strict.**

### 4. Feasibility (single context window, cross-service)
- Requires: LOS pipeline + per-loan detail + conditions + docs + staff + emails + Slack + CRM + contacts + email send ×8+ + Slack post + activity notes + CRM engagements.
- 6/6 measured runs completed the pipeline (no timeouts).
- **Verdict: PASS strict.**

### 5. Unique ground-truth end-state
- 26 loans (unique count from pipeline query).
- 8 LO recipients (each mandated by rubric).
- Every write action is method-agnostic where prompt uses "reach out"/"give"/"make sure Camille gets"; method-locked only where prompt names channel ("processing channel").
- **Verdict: PASS strict.**

### 6. Tool-service breadth (Council B-B1)
- Distinct services referenced by OE/rubric: mortgage_los, email, slack, crm, contacts. **5 distinct services** (above the 3+ threshold).
- **Verdict: PASS strict.**

### 7. Persona coherence
- Sofia (processor) writing to Grace (branch manager / boss), Camille (lock desk), Elena/Denise (compliance), and 8 LOs. All entities exist in staff/contacts. Denise's `is_active=false` LOS-record absence is compensated by explicit Slack-C004 compliance authority.
- **Verdict: PASS strict** — see AUDIT rubrics for the one minor Elena attribution flag.

### 8. Date alignment
- Universe today = **2026-04-28** (from `today_horizon.json`); prompt says "today" and "this morning". Both resolve inside the universe window.
- **Verdict: PASS strict.**

## AUDIT verdict — PROMPT: **PASS (STRICT)**

No REVISE, no REBUILD triggered.

Minor observation (not a defect):
- Word count 343 could be tightened toward 300, but the sweet-spot ceiling is not breached. No action required.
