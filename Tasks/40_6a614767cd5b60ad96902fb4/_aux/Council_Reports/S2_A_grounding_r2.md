# Council A — Grounding and Convention · S2 Oracle Events · RE-REVIEW (r2, post-REVISE)

**Task:** 40_6a614767cd5b60ad96902fb4 · **Universe:** starpm (V4) · **Deliverable:** 6_Oracle_Events.txt (19 OEs)
**Scope:** DELTA-ONLY. Two OEs changed after a strict AUDIT: OE 14 (co-valid write target) + OE 9 (wording nit). Prior pass = GO (S2_A_grounding.md, all 19 grounded).
**Method:** independent parse of `_aux/Universe_Split/airtable.airtable_records.json` + `quickbooks.quickbooks_entities.json`; full-file dash scan. Values confirmed in data, not from the OE's assertions.

## Delta 1 — OE 14: reca8230a8fd9ff51 blessed as co-valid write target [A1] GROUNDED

Re-verified all three records directly in airtable_records.json (parsed `row_data`):

| Record | fldUnit | fldTurnStatus | last_modified | Role | Verdict |
|---|---|---|---|---|---|
| reca8230a8fd9ff51 | `Sunset Ridge Unit 14` (literal) | selSched | 2026-06-07 13:03:56 | identity anchor, Tanya notes | **legitimate co-valid target** |
| recc83c05d889b354 | `Unit 14` | selSched | 2026-07-01 11:18:57 | latest, possession-hold note | **same Sunset Ridge turn (latest)** |
| rec94e86a3007dd5e | `Rio Bend - Unit 14` | selReady | 2026-05-24 | carpet done, rent-ready | **DIFFERENT property, correctly excluded** |

- reca8230a8fd9ff51: `fldUnit` is literally "Sunset Ridge Unit 14", `fldTurnStatus` selSched, table tblMakeReady, `fldNotes2` names Tanya Mitchell (June late-rent notice). It IS the same tenant + same property turn -> co-valid target confirmed.
- recc83c05d889b354: `fldUnit` "Unit 14", selSched, mod 2026-07-01 11:18:57 (latest), notes = "Eviction petition for Tanya Mitchell ... coordinated with the Justice of the Peace - make-ready work ... cannot begin until ... possession is formally returned". Same Sunset Ridge Unit 14 turn. Confirmed.
- rec94e86a3007dd5e: `fldUnit` "Rio Bend - Unit 14", selReady, notes = carpet replacement complete / unit inspected. Different property, already rent-ready. The OE 14 clause "The Rio Bend Unit 14 record rec94e86a3007dd5e must never be the target" is correct and the exclusion is preserved.

Relaxation is sound: OE 14 UPDATES fldNotes2 with the possession-hold content, so the target's prior note is overwritten. Both blessed records are correct-tenant (Tanya Mitchell) + correct-property (Sunset Ridge Unit 14) + tblMakeReady/selSched; either lands the identical correct outcome. Grading "on the hold content plus correct-tenant and correct-property record, not the exact record id" is grounded and removes a false-fail path (an agent that writes to the record literally spelling "Sunset Ridge Unit 14" was previously penalized). Real trap (Rio Bend) stays locked. No new atom introduced.

## Delta 2 — OE 9: "Balance 0.00 (the invoice nets to zero)" [A1/A2] GROUNDED + TRUTHFUL

Invoice id 283231782926 re-verified in quickbooks_entities.json (`properties`):
- DocNumber = **7214** · TotalAmt = **8173.44** · Balance = **0.0** · CustomerRef = Tanya Mitchell (proj-2e48c594aab7).
- PrivateNote: "Consolidated rent ledger ... **Net balance reflects all charges and credits** through the June 29 cure deadline; Mitchell account rem[ains delinquent] ...".

"nets to zero" is a faithful paraphrase of the invoice's OWN PrivateNote ("Net balance reflects all charges and credits") and of Balance 0.00. The revised gloss no longer asserts a specific "payment of 8173.44 applied" mechanism — a strict improvement. It is also independently defensible: a discrete payment atom of TotalAmt 8173.44 (id 952690463873) exists in the universe, but OE 9 no longer needs it. The unchanged clause "the zero balance must NOT be read as resolved" remains supported by the delinquent PrivateNote.

## Convention — dash scan [A2] CLEAN

Full-file scan for U+2012/U+2013/U+2014/U+2015/U+2212/U+2E3A/U+2E3B: **zero hits**. Only ASCII hyphen U+002D (98x, all in " - " glosses / status labels). No em-dash or en-dash introduced. Delta strings confirmed present; old causal "a payment of 8173.44 is applied" fully removed.

## Regression — 17 unchanged OEs [A3/A4/A11] NO REGRESSION

Both deltas operate entirely on atoms already grounded in the GO pass (S2_A_grounding.md lines 12-14 for the three make-ready records; line 21 for invoice 7214 / 8173.44 / Balance 0.00). No new entities, ids, amounts, or dates were introduced. OE 9's surrounding text (bills QR-2026-0441 Balance 2132.00, 2026-EV-047 Balance 185.00; PrivateNote-vs-books conflict) and OE 14's surrounding text (keep selSched, do not advance) are unchanged and were grounded previously. Nothing else can have regressed.

## Non-blocking note
- reca8230a8fd9ff51's own fldNotes2 carries the earlier (superseded) "committed to a payment timeline" state, while recc83c05d889b354 carries the current possession-hold note. Immaterial to correctness: OE 14 overwrites fldNotes2 with the correct hold content regardless of which co-valid record is targeted, and both are the same tenant/property.

## VERDICT: GO
Both deltas grounded (A1), convention-clean with no em-dash/en-dash (A2), and no regression on the 17 unchanged OEs (A3/A4/A11). reca8230a8fd9ff51 is a legitimate co-valid write target; recc83c05d889b354 is the same latest turn; rec94e86a3007dd5e (Rio Bend) is correctly excluded. Invoice 7214 "nets to zero" is truthful against Balance 0.00 and the invoice's own PrivateNote.
