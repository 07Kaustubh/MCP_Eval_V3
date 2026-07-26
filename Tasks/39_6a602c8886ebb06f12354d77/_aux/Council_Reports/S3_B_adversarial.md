# Council B (Adversarial QC) - S3 Rubrics Exit Gate

Task: 39_6a602c8886ebb06f12354d77 (StarPM / V4)
Deliverable: 7_Rubrics.json - 15 Outcome, 0 Process
Scope: Las Palmas 8D make-ready reconciliation (stale "ready" row vs live seized-disposal blocker)
VERDICT: GO

Note on indexing: this report uses R1..R15 for array positions 1..15. The task brief used 0-based indices; its "index 9" = R10 (email outstanding-item bundle) and "index 14" = R15 (rest-complete list). Both were scrutinized hardest per the brief.

---

## 1. Rubric inventory + sub-category map

| R | Sub-cat | One-line | Artifact |
|---|---|---|---|
| R1 | 1.1 | follows up on OPS-227 requesting parts approval (method-agnostic) | Linear comment OR Slack OR email |
| R2 | 1.1 | updates receb057b02f20052 so it no longer shows ready | Airtable make-ready |
| R3 | 1.2 | status ready -> in progress on receb057b02f20052 | Airtable make-ready |
| R4 | 1.2 | notes: disposal seized/awaiting replacement, not ready to show | Airtable make-ready |
| R5 | 1.1 | posts an update in #make-ready (C004) re 8D | Slack C004 |
| R6 | 1.2 | channel msg: 8D not ready, should not be marketed/shown | Slack C004 |
| R7 | 1.2 | channel msg: names seized disposal as the open item | Slack C004 |
| R8 | 1.1 | drafts email to john.smith@starpm.com re 8D standing | Gmail draft |
| R9 | 1.2 | email: 8D not yet ready to close | Gmail draft |
| R10 | 1.2 | email: seized disposal (full replacement + pending approval) = outstanding item | Gmail draft |
| R11 | 1.2 | email: what it takes (approve/order, install, final walk to close) | Gmail draft |
| R12 | 2.1 | identifies 8D not ready despite logged status + cleared chatter | Final response |
| R13 | 2.1 | identifies seized disposal blocker (full replacement, pending approval) | Final response |
| R14 | 2.1 | identifies MT-2026-1271 open in Airtable SoR (turn not complete) | Final response / trajectory |
| R15 | 2.1 | reports the rest (repairs, carpet, deep clean, punch-list, fridge swap) complete | Final response |

Structure read: for EACH of the three commissioned deliverables (channel post, email, report-to-user) the set carries the not-ready verdict plus the disposal cause, then the email adds the finish path (R11) and the final response adds the SoR ticket (R14) and the rest-complete contrast (R15), on top of the record-correction trio (R2/R3/R4) and the blocker-advance (R1). Clean per-deliverable coverage, not redundancy (same fact across different required artifacts is independently failable).

---

## 2. QC sub-dimension scores

| Sub-dimension | Score | Basis |
|---|---|---|
| Overall Rubric Quality | 5 | 0 Major, 0 Moderate, 0 counted Minor. All soft notes are robustness recommendations, not scored defects (see Section 10). |
| All-Failing Rubrics | 5 (N/A at S3) | Every target grounded in the per-task universe (receb057b02f20052, MT-2026-1271 blank completion, OPS-227 + comment_16a0a0c53f, C004, john.smith@starpm.com via OE10). No always-fail predicted. Re-assess at verifier stage. |
| Rubric Category Balance | 5 | 15 Outcome > 0 Process. |
| Process Rubrics | 5 | Zero is correct. No needed behavior uncovered: SoR verification is folded into R14 (Outcome-first); no ordering precondition among the 4 writes. |
| Agent-Centric Phrasing | 5 | All criteria are "The Agent .." / "The Agent's .."; possessive forms valid (06/09). No tool name in any criterion. Data ids (record/ticket/channel) are not tool names. |
| Atomicity (per-set) | 5 | No cross-action / cross-service bundling. Same-artifact coupled content and the R15 aggregate are acceptable (see Section 6). |
| Self-Containment (per-set) | 5 | All expected values embedded (emails, record id, ticket #, channel, enum gloss). No catch-all trap ("or another record / or similar entity"). |
| Completeness (prompt-ask coverage) | 5 | All 5 asks + the email's 3 sub-asks covered; no gap (Section 5). |
| Flexibility (EM vs fuzzy) | 5 | EM for ids/emails/channel/ticket; agent-generated content reads as Required-Elements / paraphrase-tolerant. One flexibility recommendation on R11. |
| Accuracy (per-set) | 5 | Literals consistent across Hardness_Plan spot-checks + OEs + rubrics; no discrepancy. Contingent on Council A/S2 confirming john.smith@starpm.com and the selReady/selProg enum form, which S2 grounded. |

Lowest sub-dimension: none below 5.

---

## 3. Adversarial alt-path pass (attempt to break each rubric)

For each rubric I constructed the strongest valid trajectory that could still fail it. Result column: SURVIVES = no valid path breaks it; RESIDUAL = a low-probability path exists, logged with a fix.

| R | Break attempt (valid trajectory that could fail it) | Result |
|---|---|---|
| R1 | Agent advances blocker but only posts "8D still pending" without requesting approval | SURVIVES. R1 requires "requests parts approval", which is the advancing action the prompt asked ("get it moving"). Vague update correctly fails. Method-agnostic (comment/Slack/email) so no channel lock-in. Micro-note: a #maintenance channel post tagging John should count as "Slack message to John". |
| R2 | Agent de-readies via a different means than a status write | SURVIVES. receb057b02f20052 is the only 8D row reading ready (the other two 8D rows are already selProg); pinning it is a structured one-correct-value, not over-specific. |
| R3 | Agent sets a not-ready status other than "in progress" | SURVIVES in practice. selProg is GT (OE9) and both sibling 8D rows use selProg; no rival not-ready enum is evidenced. Criterion states "ready -> in progress" (natural language); the selProg id lives only in evidence as a gloss, so an option-name write still grades. |
| R4 | Agent writes "disposal seized" but omits "not ready to show" | SURVIVES (acceptable coupling). Same notes field, blocker + consequence; the tail is redundant with R3's status flip so it cannot reject a correct correction. |
| R5 | Agent posts to a different channel | SURVIVES. Prompt explicitly named the make-ready channel; #make-ready(C004) matches prompt specificity. Not channel lock-in. |
| R6 | Agent posts "8D still in progress" without the explicit "don't market/show" | SURVIVES (acceptable). "Don't show" is the core correction (the old chatter said "cleared, available to show"), so it is prompt-grounded, not a surplus second item. |
| R7 | Agent names a wrong blocker | SURVIVES. Requires the seized disposal, the sole GT blocker. |
| R8 | Agent uses a different address, or sends instead of drafts | SURVIVES. john.smith@starpm.com is EM (OE10). Gmail is draft-only; "drafts" matches the universe gotcha. |
| R9 | Agent's email is upbeat but hedged | SURVIVES. Requires the explicit "not ready to close" verdict. |
| R10 | Agent's email names the disposal but omits "pending parts approval" | RESIDUAL (low). Bundles one blocker's attributes from the single OPS-227 comment; acceptable coupling, but see Section 6 option to split. |
| R11 | Agent lists approve + install + "close it out" without the literal "final walk" | RESIDUAL (low). "to close the turn" reframes the step as the closeout; a competent judge accepts "close out". Fix: add "(or a closeout step)". |
| R12 | Agent reports not-ready only inside the email, terse final response | SURVIVES. Prompt asks James directly ("can you figure out where 8D really stands") so a 2.1 final-response verdict is the requested artifact. |
| R13 | Agent identifies not-ready via the 6/25 in-progress row, never reads OPS-227 comment | SURVIVES. The "pending parts approval / full replacement" facts exist only in the OPS-227 comment; an agent that skips it cannot produce R13's content, which is the intended L3 signal. |
| R14 | Agent solves correctly via OPS-227 + make-ready rows, never queries tblMaintenanceTickets | RESIDUAL (top watch-item). See dedicated analysis below. Held VALID at S3. |
| R15 | Agent says "8D fully ready" (wrong) - does it pass R15? | SURVIVES. R15 tests only "is the rest complete", which is true; the disposal error is caught by R12/R13/R14 (which that wrong response fails). R15 is not overly broad on its own subject. |

### R14 dedicated analysis (most contestable rubric)
The only construct that fails R14 while reaching the right answer is an agent that confirms 8D-not-ready from OPS-227 (a Linear comment) plus the in-progress make-ready rows, without opening tblMaintenanceTickets. Two facts hold R14 VALID at S3:
1. The prompt explicitly says "confirm where each piece actually landed instead of going off what someone said in passing." OPS-227 is a Linear comment (someone said it); team_001 charter names Airtable the system of record and Linear secondary. Requiring the SoR-ticket confirmation is therefore prompt-aligned, not method lock-in (R14 pins a finding, not a channel).
2. Evidence already allows "final response OR trajectory", so any agent that queried the ticket passes without prose; and MT-2026-1271 specificity is protective against the near-miss MT-2026-1325 (Rio Bend 214, completed 6/25).
Residual-risk recommendation (non-blocking): consider broadening R14 evidence to also accept the make-ready record's own in-progress / blank-completion state as an equivalent Airtable-SoR signal, since both tables live in the SoR. If S4 shows a run that did every write and reached the correct verdict yet failed only R14 for skipping the ticket table, broaden then. Do NOT drop R14: it is the Outcome that lets the set carry zero Process (Section 7) and is the sole L2 cover (Section 9).

No adversarial attempt yielded a path that a Major/Moderate would attach to.

---

## 4. Reverse-coverage (rubric -> prompt sentence)

| R | Ties to prompt clause | Surplus? |
|---|---|---|
| R1 | "if something's still open, run down whatever it's waiting on and get it moving so it can genuinely close" | No |
| R2/R3/R4 | "square up what we've got logged so it matches where the unit really is right now" | No |
| R5/R6/R7 | "Post an update in the make-ready channel so the crew isn't working off old info" | No |
| R8 | "draft John an email" | No |
| R9 | "laying out where 8D stands" | No |
| R10 | "what's still outstanding if anything" | No |
| R11 | "what it'll take to finish" | No |
| R12 | "figure out where 8D really stands" | No |
| R13 | "run down whatever it's waiting on" | No |
| R14 | "confirm where each piece actually landed instead of going off what someone said in passing" | No |
| R15 | "confirm where each piece actually landed" (the done pieces) | No |

No beyond-prompt / surplus rubric. Every rubric has a prompt anchor.

---

## 5. Forward-coverage (prompt ask -> covering rubric)

| Prompt ask (explicit + implicit) | Covering rubric(s) | Covered |
|---|---|---|
| figure out where 8D really stands | R12 | Yes |
| confirm each piece landed (done pieces) | R15 | Yes |
| confirm each piece landed (open piece + SoR) | R13, R14 | Yes |
| advance whatever is still open | R1 | Yes |
| square up the logged record | R2, R3, R4 | Yes |
| post an update in the make-ready channel | R5, R6, R7 | Yes |
| email: draft it | R8 | Yes |
| email sub-ask: where it stands | R9 | Yes |
| email sub-ask: what is outstanding | R10 | Yes |
| email sub-ask: what it takes to finish | R11 | Yes |

No forward-coverage gap. The compound email ask (stands / outstanding / what-it-takes) is decomposed into R9/R10/R11 (each part covered). Decoy handling (204B swarm, Rio Bend 214, MT-2026-1325) is implicitly enforced: every rubric requires 8D-specific ids/facts, so a decoy-fooled agent fails R2/R12/R14 rather than passing a wrong-unit report; no dedicated exclusion rubric is required because the task is not a "list all X" filter where a decoy could be wrongly included.

---

## 6. Atomicity pass (brief-flagged R10 and R15 hardest)

Decision frame: cross-action / cross-service claims are always split (Major). Multiple content facts of a single artifact are acceptable when they are one thing's attributes or a cause/consequence pair from one data point. No rubric bundles across actions or services.

- R10 (brief index 9): "seized + full replacement + pending parts approval, as the one outstanding item." All attributes of ONE blocker sourced from the single OPS-227 comment. Acceptable coupling. Optional split: (i) email names the seized disposal as the outstanding item; (ii) email states it needs a full replacement and is pending parts approval. Not required; low failure-independence risk.
- R15 (brief index 14): aggregates 5 completion items (repairs, carpet, deep clean, punch-list, fridge swap). VALID by direct precedent: the V3 guidelines' own Task-2 example ships a single 2.1 "Agent reports the status of each relocation" rubric covering 5 items. A single 2.1 aggregate status report is a blessed pattern, not a "split completely" violation. No change needed.
- R4: "disposal seized/awaiting replacement" + "not ready to show" - one notes field, blocker + consequence. Acceptable; the tail is redundant with R3 and could be trimmed.
- R6: "not ready" + "should not be marketed/shown" - one message, status + crew-actionable implication. Acceptable; optional two-way split for purity.
- R11: "approve/order + install + final walk" - one finish-path answer to a single ask. Acceptable Required-Elements; add closeout flexibility.

No Major/Moderate atomicity hit.

---

## 7. Process check (confirm zero Process is correct)

Two candidate behaviors that an Outcome might miss:
1. Ordering between the 4 writes. None of (advance disposal, correct record, post channel, draft email) is a precondition for another; the prompt states no order. No ordering Process rubric needed.
2. Authoritative-source verification (Airtable SoR over Slack/Linear chatter). This is the L2 lever. Three-condition test: condition 2 fails because a stricter Outcome CAN capture it, and does - R14 ("identifies MT-2026-1271 open in Airtable, the system of record"). Outcome-first rule: fold into the Outcome, do not add Process.

Zero Process is the correct design. No necessary behavior is left uncovered. No PROPAGATE flag.

---

## 8. Density projection (B3, StarPM V4 bands: 40 design / 15 floor)

The rubric set forces the full discovery-plus-write path (every OE is required to ground a rubric): Airtable base + table listing + two make-ready record pulls + maintenance-ticket pull (R2/R14), Slack #make-ready + #maintenance reads (R6/R7/R15 + disposal), Linear issue + comment thread + optional team charter (R13/R14 grounding), contacts lookup (R8), then 4 writes (R1 comment, R2 record update, R5 channel post, R8 draft). Add L4 eviction refinements (204B swarm forces query narrowing) and L6 near-miss verification (Rio Bend 214 / MT-2026-1325).

- Hard minimum (aggressive batching): ~15-18 discrete calls across 4+ services. Clears the 15 floor with margin.
- Realistic compliant midpoint: ~44-48 (consistent with Hardness_Plan component sum 38-59, midpoint 48.5). Point estimate ~47.

Midpoint ~47 >= 40 StarPM V4 design target. Applied per model (Opus and Gemini separately). B3: PASS (not THIN, not INSUFFICIENT).

---

## 9. Hardness levers (B4) - each covered by >=1 Outcome whose value depends on traversal

| Lever | Covering rubric | Dependency |
|---|---|---|
| L10 temporal supersession (stale 5/1 ready row vs live June work) | R12 (+ R2/R3) | R12 requires the not-ready verdict "despite the logged make-ready status"; producing it requires recognizing the 5/1 row is superseded. R2/R3 require correcting that exact stale row. |
| L2 Airtable-is-SoR skip (open MT-2026-1271) | R14 | Correctness requires traversing tblMaintenanceTickets (the SoR) and reading the blank completion date. Sole cover; do not drop. |
| L1 latching (Slack "8D done" chatter) | R12 (+ R6/R7) | R12 requires overriding "earlier channel messages indicating it was cleared"; R6/R7 require correcting that chatter. |
| L4 search-cap eviction (real 8D rows under 204B decoys) | R2 + R14 (indirect) | R2 pins receb057b02f20052 and R14 pins MT-2026-1271; an evicted agent that only surfaces 204B cannot produce these exact ids, so both fail. Coverage is id-forced, not decoy-named, but load-bearing. |
| L3 missing reply (disposition in OPS-227 comment / parts-approval reply) | R13 (+ R1/R10) | The "full replacement / pending parts approval" facts live only in comment_16a0a0c53f (chased, not the first-found issue description). R13/R1/R10 cannot be satisfied without reading that reply. |

All 5 levers covered. No uncovered lever.

---

## 10. Findings + recommendations (all NON-BLOCKING)

No Major and no Moderate. The following are robustness recommendations at the operator's discretion; none reject a clearly-valid path at a plausible probability, so none block the gate.

1. R14 (watch): broaden evidence to accept the make-ready record's in-progress / blank-completion state as an equivalent Airtable-SoR signal alongside the ticket. Re-check at S4; keep R14 (sole L2 cover, and it lets the set stay zero-Process).
2. R11 (minor flexibility): phrase the closeout element as "complete a final walk (or a closeout step) to close the turn" so an agent who says "close it out" is not pinned to the literal "final walk".
3. R10 (optional split): separate "names the seized disposal as the outstanding item" from "states it needs a full replacement and is pending parts approval" if maximal atomicity purity is wanted.
4. R6 (optional split): separate "8D is not ready" from "should not be marketed or shown".
5. R4 (optional trim): the "so the unit is not yet ready to show" tail is redundant with R3's status flip and may be dropped.
6. R1 (micro-note): confirm the judge treats a #maintenance channel post tagging John, requesting parts approval, as satisfying "a Slack message to John Smith".
7. R2/R3 (no change): acceptable 1.1 + 1.2 layering on the same record correction.

Dependency for Accuracy=5: Council A / S2 must have confirmed john.smith@starpm.com and the selReady/selProg enum form against 7_Server_Tools_Details.json and contacts (standard division of labor). No discrepancy found in this pass.

---

## Final scoring table

| Sub-dimension | Score |
|---|---|
| Overall Rubric Quality | 5 |
| All-Failing Rubrics | 5 (N/A at S3) |
| Rubric Category Balance | 5 |
| Process Rubrics | 5 |
| Agent-Centric Phrasing | 5 |
| Atomicity | 5 |
| Self-Containment | 5 |
| Completeness | 5 |
| Flexibility | 5 |
| Accuracy | 5 |

Density midpoint ~47 (PASS, >= 40). All 5 levers covered. Zero surviving adversarial hits at Major/Moderate. Zero Process is correct; no PROPAGATE.

COUNCIL B: GO
