# REVIEW — Council Report: Prompt (`5_Prompt.txt`)

## Council A — Grounding sweep

Verified every load-bearing claim against the per-task universe.

| Claim | Verified |
|---|---|
| Andrea is the certifying partner for the May Acme close | YES — `2_Persona_Briefs.md` Andrea Phil entry: "She certifies four monthly close packages: ... scen_028 (Acme May with the Datadog reclass from account 500000 to 521000)." Cross-checked against scen_028 close-package semantics. |
| Acme May close is in progress (not finalized) | YES — `_aux/Universe_Index/key_facts.md` fiscal-period table: `acme_cloud_FP-2026-05` status `open`, BD3 lock 2026-06-03, `locked_at = null`. Universe today = 2026-06-12. |
| There is a contested judgment item with conflicting explanations | YES — `oracle_gl.ogl_journal_entries.json` shows `je_1ce7247752034cbc` (the only Datadog-mentioning JE in the universe), $28,400, DR 521000 / CR 500000. The competing $28.4K-vs-$340K narratives surface in emails/Slack per the trajectory traces in `8_Verifier_Fails.txt`. |
| Prior-period precedent exists for KPI-sensitive reclasses | YES — `JE-acme_cloud-FP-2025-09-0041` (`Cloud infrastructure spend` reclass, `entry_type = reclassification`) confirmed via direct JSON query. |
| Matthew can plausibly partner-review on Acme | YES — `2_Persona_Briefs.md` Matthew Li entry: engagement-side authority on Acme (scen_041 AML wire-flag review, AP > $50K threshold approval). |

## Council B — 5 perspectives × 5 lenses

### Perspective 1: Strict Veteran QC Reviewer

| Lens | Finding |
|---|---|
| Truthfulness | No factual claims that conflict with universe. The premise is genuine. |
| Self-containment | Prompt does not lean on out-of-prompt context to make sense. Reads cleanly cold. |
| Anti-patterns | No em-dashes, no "at least N", no tool names. No "please confirm" / "tell me whether" binary framing that would collapse difficulty. |
| Persona fit | Matthew's voice is partner-formal, commercially aware, decision-oriented. The prompt matches all three. |
| Business function | Accounting Operations — partner sign-off on a close package is canonical Cat 1.1 work. |

**Verdict:** PASS.

### Perspective 2: Red-Team Adversary

Looking for ways to game / collapse / cheat.

| Lens | Finding |
|---|---|
| Single-source shortcut | NO — the contested item, the two explanations, and the precedent are all on different services (Oracle GL, Slack, email, Records Vault). Single-service shortcut yields incomplete answer. |
| Stated-answer leakage | NO — the prompt names no JE ID, no doc ID, no dollar amount, no account number. Agent must discover everything. |
| Pre-solving | NO — "one of the items that moved during the close" is a generic anchor; agent must investigate to find which one. |
| Tool-name leakage | NO — descriptive intent only ("review the supporting materials, the discussion around the item"). |
| Process collapse | NO — the prompt explicitly requires both investigation AND a write-and-communicate cycle, but in partner-natural language so the model has to reason about what "make sure the rationale is documented" means in a CPA-firm context (this IS the deliberate Opus 4.8 lever per L1/L6/L7 in `_meta/Learnings.md`). |

**Verdict:** PASS — adversarial probing finds no shortcut.

### Perspective 3: Persona / Role Authenticity Check

| Lens | Finding |
|---|---|
| Voice consistency | Matthew's "I'm less concerned about the size of the adjustment than I am about the quality of the judgment behind it" is exactly the partner-voice register from his persona brief ("commercially minded, oriented toward decisions, quality, and client trust"). |
| Workflow plausibility | Asking a co-partner for an independent read on a judgment item is a defensible partner-level peer-review pattern. Not Matthew's most common scenario but plausible. |
| Authority alignment | Matthew has Acme engagement authority (AP > $50K, scen_041 AML lead). He's not stepping outside his lane. |
| Email/voice register | No casual register. No filler. No "thanks!" / "any thoughts?" patterns alien to partner voice. |
| Tone matches scene urgency | Pre-finalization window has the right partner urgency — measured but actionable. |

**Verdict:** PASS.

### Perspective 4: Verifier (How Will a Judge Score This?)

| Lens | Finding |
|---|---|
| What's verifiable from final response | Conclusion (supportable / not); the specific JE identified; the two explanations surfaced; precedent comparison; recommendation; isolated-vs-recurring classification. |
| What's verifiable from trajectory | Write action to Records Vault or BlackLine; outbound communication to Andrea / Jones / Brenda. |
| Atomicity per rubric | Each rubric covers one verifiable thing or one tightly-coupled set. |
| Cascading dependency | R7 cascades on R6 and R9 cascades on R8 — but that's a known and accepted pattern (an artifact's content can only be evaluated if the artifact was created). Not a defect. |
| Judge interpretation risk | Low — rubrics name JE IDs, doc IDs, stakeholder emails, account paths. No "appropriate", "sufficient", "enough" left for judge interpretation. |

**Verdict:** PASS.

### Perspective 5: Coherence / Across-Artifact

| Lens | Finding |
|---|---|
| Prompt → OE | Each prompt sentence maps to one or more OEs. Investigation drive ↔ OEs 1-6. Documentation drive ↔ OE 7. Communication drive ↔ OE 8. |
| Prompt → Rubrics | "Concise recommendation" → R5. "Make sure the rationale is documented clearly" → R6/R7. "Relevant stakeholders have a consistent understanding" → R8/R9. "Whether it's part of a broader pattern" → R10. |
| Internal contradictions | None. The prompt's emphasis on judgment-quality-over-dollar-amount is preserved across rubrics. |
| Length appropriateness | 251 words — well under 500 cap. |
| Cap on assumptions | One assumption (which judgment item is being reviewed) — resolved by investigation. Within acceptable single-assumption band. |

**Verdict:** PASS.

## Council verdict: PASS — Prompt score 5/5 every sub-dim.
