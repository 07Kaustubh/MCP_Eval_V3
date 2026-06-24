# REVIEW — Final Council (Cross-Artifact)

Per `Reference/Sessions/FINAL.md`: four lenses — Truthfulness, Cross-artifact Holism, Rubric Binding, Red-team.

## Lens 1: Truthfulness (answer leakage + factual claims)

| Check | Finding |
|---|---|
| Does the prompt leak the answer? | NO. Prompt names no JE id, doc id, account number, dollar amount, or stakeholder email. The contested item is anchored only as "one of the items that moved during the close." |
| Do the OEs leak the answer in a way agents could lift verbatim? | NO. OEs name IDs (which is expected and required), but agents must call the tools to confirm. The verifier-fails confirm agents had to investigate to identify the JE. |
| Do the rubrics state the answer? | The rubrics name the JE id and supporting IDs as the verification anchors. This is the standard pattern — rubrics are graded against the final response, so they CAN name the answer they're checking for. Verifier-fails confirm agents did not lift these IDs from the rubrics (they're graded after-the-fact, not visible to the agent during the task). |
| Persona-truth check | "Andrea is wrapping up her certification" aligned with persona briefs and scen_028 yaml. No false premise. |
| Acme-vs-Northstar persona alignment | Matthew is Northstar-weighted but has explicit Acme engagement authority (scen_041 AML, AP > $50K). Partner peer-review on a single judgment item is plausible. |

**Verdict:** PASS — no leakage. Premise grounded in universe truth.

## Lens 2: Cross-artifact Holism

| Check | Finding |
|---|---|
| Prompt → OE coverage | Every prompt clause maps to ≥1 OE. Investigation (4 prompt clauses) ↔ OEs 1-6. Documentation (1 clause) ↔ OE 7. Communication (1 clause) ↔ OE 8. |
| OE → Rubric backing | Every Outcome rubric has ≥1 OE backing. R5 + R10 are graded against the final response, so OE backing is via the synthesis-feeding OEs (OE 3, OE 6). |
| Rubric → Prompt traceability | Every rubric criterion traces back to a clause in the prompt. R10 (isolated-vs-recurring) ↔ prompt "whether the matter is part of a broader pattern". |
| Identifier consistency | The JE id, doc id, period id, and stakeholder emails appear consistently formatted across all three artifacts. |
| Method-agnostic flexibility preserved | OE 7 / R6 both list three valid write paths (Records Vault memo, MAP version-add, BlackLine review note). OE 8 / R8 both list three valid comm channels (email, messaging, Slack). |

**Verdict:** PASS — full holistic coherence.

## Lens 3: Rubric Binding

| Check | Finding |
|---|---|
| Does every rubric have a unique, verifiable answer in the per-task universe? | YES. R1 ↔ JE 0044. R4 ↔ JE-FP-2025-09-0041. R6 ↔ Records Vault or BlackLine write. R8 ↔ three named stakeholders. |
| Could a judge grade each rubric without re-reading the prompt? | YES — every rubric is self-contained. |
| Are the rubric evidence fields specific enough to verify? | YES — they name specific tool calls, specific document IDs, specific stakeholder emails. |
| Process rubric verifiable from trajectory alone? | YES — R11 is graded by checking tool-call order. |
| Are bundled-attribute rubrics graded atomically by the grader? | The verifier-fails show graders treat R7 / R9 as PASS-only-if-all-elements-present. Behavior matches V3 intent. |

**Verdict:** PASS — every rubric is unambiguously verifiable.

## Lens 4: Red-team (exploit attempts)

Tried to find shortcuts an agent could exploit:

| Exploit | Result |
|---|---|
| "I'll just ask Andrea what the contested item is" — single-tool shortcut via email_send_email | Would fail R6 (no write to system of record), R7 (no artifact). Caught. |
| Skip the write action, narrate the recommendation in chat | 5 of 6 verifier-fail runs did exactly this. Failed R6/R7/R8/R9. Caught. |
| Send comm without investigating | Would fail R11 (process). Caught. |
| Cite the FY25 cumulative without checking SAP subledger | Possible but R3/R10 require evidence-grounding. R3 graders flagged missing AP subledger tie-out across runs. Caught. |
| Treat all three competing explanations as equally valid (avoid taking a stance) | Would fail R2 (clear conclusion). Caught. |
| Reuse the embedded MAP SAB 99 memo as the "review record" | Would fail R6 — the MAP isn't a partner-review record, it's the close package being reviewed. The OEs and rubrics distinguish a NEW write from re-pointing at an existing doc. Caught. |

**Verdict:** PASS — no exploit path survives the rubric set.

## Final Council verdict: PASS

All four lenses clear. Task is shippable.

### Lever inventory (the deliberate Opus 4.8 stumping mechanisms preserved through the materialization)

| Lever | Mechanism | Confirmed in trajectory |
|---|---|---|
| Partner-voice mandate ambiguity | "make sure the rationale is documented clearly" reads as advisory; Opus 4.8 frequently treats this as chat-conversation rather than systems-of-record write | 6/6 runs failed R6 |
| Stakeholder comm deference | "make sure relevant stakeholders have a consistent understanding" reads as advisory; Opus 4.8 frequently defers ("If you'd like I can draft") | 5/6 runs failed R8 |
| Brenda Abbas role ambiguity | JE approver of record is also listed as "Vendor account manager" in contacts | Multiple runs flagged this as a documentation gap (good — they investigated rather than ignored it) |
| Cumulative-vs-period framing | $28.4K (one period) vs ~$340K (FY25 cumulative) competing narratives | All runs surfaced this competing-narrative dynamic |
| Comparability break | Go-forward-only treatment vs FP-2025-09 precedent that pushed corrective JE | Multiple runs caught the comparability inconsistency |
| Embedded-stub memo | SAB 99 memo embedded in MAP doc with restricted-classification but stub content | Multiple runs caught the documentation gap |
