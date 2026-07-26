# Rubric Coverage Matrix - Tasks/39_6a602c8886ebb06f12354d77 (StarPM / V4)

Deliverable: 7_Rubrics.json - 15 Outcome, 0 Process.
Gates: validator PASS (0 fail / 0 warn); Council A GO (grounding); Council B GO (all sub-dims 5/5, density ~47, 5 levers covered).
AUDIT verdict: PASS (STRICT) - all 10 rubric sub-dims 5/5, zero BLOCKER, 5 levers trace end-to-end, density ~47 (StarPM 40+ PASS), regression anchors 62/62, validator exit 0 (2 MINOR half-applied-tweak evidence defects raised and fixed in place, then re-verified).

## Prompt sentence -> OE step(s) -> rubric(s) -> lever

| Prompt clause | OE step(s) | Rubric(s) | Hardness lever |
|---|---|---|---|
| "can you figure out where 8D really stands" | OE1-7 (discovery) | R12 (2.1 not ready) | L10 supersession + L1 latching |
| "confirm where each piece actually landed instead of going off what someone said in passing" | OE2, OE3, OE4, OE5, OE7 | R13 (disposal blocker), R14 (MT-2026-1271 open in Airtable SoR), R15 (rest complete) | L2 SoR skip + L4 eviction + L3 missing-reply |
| "if something's still open, run down whatever it's waiting on and get it moving so it can genuinely close" | OE6, OE7, OE8 | R1 (advance blocker), R13 (identify what it waits on) | L3 missing-reply |
| "square up what we've got logged so it matches where the unit really is right now" | OE9 | R2 (update record receb057b02f20052), R3 (status ready -> in progress), R4 (notes: disposal seized/awaiting replacement) | L10 supersession |
| "Post an update in the make-ready channel so the crew isn't working off old info" | OE10, OE11 | R5 (post to #make-ready C004), R6 (8D not ready / not to be shown), R7 (seized disposal named as the open item) | L1 latching |
| "draft John an email laying out where 8D stands, what's still outstanding if anything, and what it'll take to finish" | OE10, OE12 | R8 (draft to john.smith@starpm.com), R9 (where it stands = not ready to close), R10 (outstanding = seized disposal), R11 (what it takes = approve/order + install + final walk or closeout) | - |
| "I'd much rather catch whatever's still hanging now than after I've already told him it's ready" | framing (motivates the reconciliation) | R12, R13 (the not-ready finding + its cause) | L10 + L1 |

## OE -> rubric cross-reference (write + key-discovery)

| OE | Type | Covering rubric(s) |
|---|---|---|
| OE8 advance disposal blocker | Write | R1 (1.1, method-agnostic) |
| OE9 correct tblMakeReady receb057b02f20052 | Write | R2 (1.1) + R3 (1.2 status) + R4 (1.2 notes) |
| OE11 post to #make-ready C004 | Write | R5 (1.1) + R6 (1.2) + R7 (1.2) |
| OE12 draft email to john.smith@starpm.com | Write | R8 (1.1) + R9/R10/R11 (1.2) |
| OE1-7 discovery (status conflict, open ticket, seized disposal, done chatter) | Read (user-asked) | R12/R13/R14/R15 (2.1 findings) |
| OE10 contacts lookup john.smith | Read (intermediate) | supports R8 recipient; no standalone rubric needed |

## Gap check (every explicit + implicit ask has a rubric)

- figure out where 8D really stands -> R12. COVERED
- confirm each piece landed (open piece) -> R13, R14. COVERED
- confirm each piece landed (done pieces) -> R15. COVERED
- advance whatever is still open -> R1. COVERED
- square up the logged record -> R2, R3, R4. COVERED
- post an update in the make-ready channel -> R5, R6, R7. COVERED
- draft John an email (stands / outstanding / what-it-takes) -> R8 / R9 / R10 / R11. COVERED (compound ask decomposed per part)

No gap. Final-response coverage gate satisfied: every user-asked finding has a 2.1 (R12/R13/R14/R15).

## Surplus check (every rubric ties to a prompt ask)

R1..R15 each map to a prompt clause in the table above. No beyond-prompt / surplus rubric.

## Hardness lever coverage (each covered by >=1 Outcome whose value depends on traversal)

| Lever | Covering rubric(s) | Dependency |
|---|---|---|
| L10 temporal supersession | R12, R2, R3 | correctness requires recognizing the 2026-05-01 selReady row is superseded by the live June selProg work |
| L2 Airtable-is-SoR skip | R14 | requires grounding "turn not complete" in the Airtable SoR (open MT-2026-1271 / in-progress record), not the Linear/Slack done chatter |
| L1 latching | R12, R6, R7 | requires overriding the "8D done / cleared" Slack chatter |
| L4 search-cap eviction | R2, R14 | id-forced: an agent evicted to the 204B swarm cannot produce receb057b02f20052 / MT-2026-1271 |
| L3 missing-reply | R13, R1, R10 | the "full replacement / pending parts approval" facts live only in the chased OPS-227 comment |

All 5 levers covered.

## Near-miss / decoy handling

No dedicated exclusion rubric required (the task is a status reconciliation, not a "list all X" filter). Every rubric requires 8D-specific ids/facts, so an agent misled by the 204B swarm or the Rio Bend 214 / MT-2026-1325 twin fails R2/R12/R14 rather than passing a wrong-unit report. Council A confirmed no rubric title references Rio Bend, 214, or MT-2026-1325.
