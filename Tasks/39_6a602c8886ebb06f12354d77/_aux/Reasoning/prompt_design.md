# S1 Prompt Design + Verdict Record - Task 39_6a602c8886ebb06f12354d77

**Universe:** StarPM (V4), today 2026-07-01. **Persona:** James Bennett (p_006), Assistant Maintenance Technician (junior, formality 0.35). **Business Function:** Maintenance & Repairs.
**Deliverable:** `5_Prompt.txt` (233 words). **Scenario:** the Las Palmas 8D make-ready turn close-out.

## The situation engineered
James believes 8D is basically done (the punch-list and carpet chatter he has "picked up") and told his Lead John he would have it closed out today. Before reporting up, he asks his assistant to make sure it is actually buttoned up, get anything still open moving, reconcile the records, tell the crew, and draft John the rundown. The framing is diligence, not suspicion: it forces a genuine cross-system verification without telegraphing that the record is wrong. James's belief that the unit is "about there" is preserved throughout.

## Levers engineered (all 5 preserved end-to-end; verified by Council B + AUDIT)
- **L10 reversal / supersession**: "dragging since May" plus "I'd bet some of it is stale by now" push the agent past the stale 5/1 "ready/closed out" row (receb057b02f20052) to the live 5/14 and 6/25 rows.
- **L2 structured-DB (Airtable-SoR) skip**: "square up what we've got logged" plus "confirm where each piece actually landed" drive the agent to the Airtable source of record (team_001 declares it; MT-2026-1271 is OPEN there) rather than the Linear mirror or Slack chatter. Airtable is deliberately NOT named.
- **L1 latching**: the prompt echoes the "punch-list knocked out / carpet's in" chatter (grounded in Slack C004) AND challenges it ("instead of going off what someone said in passing").
- **L4 search-result-cap eviction**: centering on "Las Palmas 8D" forces the 8D-specific dig under the 61-row "204B" decoy swarm (~10:1).
- **L3 missing reply**: "run down whatever it's waiting on" pushes the agent into the OPS-227 reply where the disposal disposition ("parts approval before I swap it") lives. The disposal is deliberately NOT named.

Four writes across four services woven into the ask (Airtable record correction, Linear comment advancing OPS-227, Slack #make-ready post, Gmail draft to John) carry density and write-breadth.

## Stump hypothesis (expected failure)
Both models trust the loud "done / cleared / ready" chatter plus the stale 5/1 row and report 8D READY. Correct end-state: 8D NOT ready. Garbage-disposal replacement + parts approval outstanding, ticket MT-2026-1271 OPEN in the Airtable SoR, the 6/25 fridge swap unconfirmed at today 7/1.

## Verdicts
- **validate.py --phase prompt:** PASS (0 fails, 0 warns). Revised once: the first draft failed the validator's cross-service + investigation/action keyword gates because it was too oblique; fixed by naming the two write-target systems (email, make-ready channel) while keeping the trap services (Airtable, Linear) unnamed.
- **Council A (grounding):** GO. Zero ungrounded claims; latching trap real and intentional; conventions clean; business function MATCH.
- **Council B (adversarial QC):** GO. Every sub-dim 5/5; unique end-state confirmed; density ~47/model PASS; 5 levers preserved.
- **Similarity:** max composite 26.7 < 40. Top match QC_Tasks/V3_Tasks/Task13 (raw_lex 26.7 vs the V3 reference corpus); nearest prior live task <= 10.2 after contextual weighting. Clear of the ceiling.
- **Strict AUDIT:** PASS (STRICT). All 14 sub-dims 5/5 under the strictest reading; density ~46/model on the V4 40+ per-model bar; 5 levers traced with cited atoms; regression anchors 62/62.

## Carry-forward (downstream)
- BEFORE S2: fix Fact_Ledger.lifecycle.today (null, should be 2026-07-01) so Council A A3 narrative-state checks resolve correctly. Correct the S0 report's injection claim.
- S2/S3 design constraint: full credit must require demonstrated cross-source synthesis plus the 4-write workflow, because James's own 6/22 #maintenance messages corroborate "8D still open" (universe-resident, not in the prompt-directed channel, does not defeat the stump). Optional authority-injection re-hardens.
