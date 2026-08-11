# AUDIT — S2 Oracle Events (strictest interpretation) — round 2 — 6_Oracle_Events.txt

Task `2_6a6beba55996ad2ada369b15` · universe **harmonygames** (`hg`, single-model) · model under test **Claude Opus 4.7** · persona **Robert** (Executive) · today **2026-02-28** America/Chicago
Deliverable: `6_Oracle_Events.txt` (**25 OE steps**). READ-ONLY. Every figure, timestamp and channel below re-derived by me from `_aux/Universe_Split/` this pass (snowflake streamed memory-bounded via `stream_sf.py`; slack Feb+Jan shards re-parsed). Prior councils and my own round-1 report re-read as CLAIMS, not evidence (AGENTS.md rules 18/19).

## Deterministic floor (cited, not re-argued)
- `validate.py --phase oe`: PASS, 0 fails, 0 warns, 25 steps (per handoff; not re-run — green).
- `check_persona_acl.py`: 0 findings. `verify_universe_atoms.py`: PASS.
- `check_oe_rubric_sync.py`: SKIP (no 7_Rubrics.json at S2 — expected).

## Request 1 — every new/changed figure, re-derived from source

| Figure (OE) | Source re-read | Value found | Verdict |
|---|---|---|---|
| R&D credit **24,275** | slack ts 1770765262.985999 #executives | "Federal Research and Development (R&D) Tax Credit of **$24,275**" | MATCH |
| Payroll-liability supersession | ts 1770767188.858539 "4 dollars of payroll"; ts 1770780604.709459 provider "cannot apply the R&D payroll tax credit during those quarters … any unused credit carrying forward"; ts 1770780769.446499 Robert "it's a credit, not a rebate then" | all verbatim | MATCH — non-cash carryforward |
| Sunset wind down **~15,000** | ts 1770850852.708789 | "cost of Sunset is about **~$15K** … data will likely cover our costs without … liquifying the laptops/assets" | MATCH |
| four-to-six weeks | ts 1770851973.264019 "**4-6 weeks**"; ts 1770852126.205579 "this is with the tax help" | verbatim | MATCH |
| Singular **18,750** | ts 1770765511.243329 | "Singular (**$18750**)" | MATCH |
| Unity formula **~2.348*9**, carried ~21,000 | ts 1770765511.243329 | "Unity (**~2.348*9 months**)" | MATCH; 2.348×9=21.132 → ~21,000. Unit unstated; siblings are $150×N (Helpshift) and lump $18,750 (Singular), so $2,348/mo is the only sane read for a Unity Pro licence. OE flags it approximate → defensible |
| Helpshift **1,200** supersedes **1,500** | ts 1770765511 "Helpshift ($150*8 months)"=1,200; ts 1770673467.186629 "$150*10 = $1500" | both verbatim | MATCH |
| Available **13,300** | 10,800 net + 2,500 cash | 13,300 | MATCH |
| Aggregate **~56,000** | 15,000+18,750+21,000+1,200 | 55,950 | MATCH (OE: "on the order of 56,000 before SVB") |
| **23.8%** coverage | 13,300 / 55,950 | 0.2377 | MATCH; "well under a quarter" defensible — SVB adds to denominator, pushing ratio below 23.8% |
| **15,000 > 10,800** | arithmetic | true | MATCH (narrow finding holds) |
| **78%** | 8,452.64 / 10,800 | 0.7826 | MATCH |
| net **10,800** | 22,500 − 11,700 (ts 1770911000.728559) | 10,800; absent from universe as a token (L6-clean) | MATCH |

**Zero figure mismatches.** All snowflake figures (DAU 72/36/peak 801/845/55,101; revenue 0.00; IAP 0 rows; V2 marts 1,636/4,313 combo=0; ad spend 7,483.42; post-02-09 8,452.64; 02-28 346.00/combo 160.88; cash 2,500/burn 22,500/runway 0.1) re-confirmed EXACT this pass.

## Request 2 — the false-absence class, independently swept

**Method:** I re-derived Robert's reachable channel set myself (authorship over Jan+Feb shards, the correct denominator per Reads_s2.md line 53), NOT the council's claim. Reachable = 20 channels incl. the high-volume DMs D07H86MV4DN (235 Feb / 557 Jan), D04UP2L3E3S (103/335), D077ALC9VK3 (131 Jan). I then grep-swept all 20 for every money/obligation-bearing message (49 hits in Feb) and read each.

**Figure-omission class: CLOSED.** Every reachable figure bearing on inbound funds, wind-down costs, obligations, cash or the still-running ad spend is either carried by the OE or correctly out of scope. The two non-carried figure hits are both correctly excluded: the "$3,000/$4,000 per playable" negotiation (ts 1770082578, #executives) is a **pre-shutdown** creative-buy negotiation dated 02-03, never referenced as a standing wind-down item after the 02-09 stop; and the two out-of-scope figures (Helpshift 300 #admin_foundersonly; 12K fiduciary DM) sit outside Robert's read scope, correctly named as such. No fourth instance of "a reachable FIGURE the OE denies/omits." The REBUILD-triggering repeat did **not** occur.

**One residual, NOT a figure omission — see F1-R2.** My sweep surfaced a reachable **unquantified** obligation the OE's absolute qualifier misses.

## Findings

### F1-R2 [MINOR — OE precision / exhaustiveness qualifier]
OE 16 states: *"SVB is the only named obligation that no reachable record quantifies."* My sweep found a second one. ts **1770836625.652859** in #executives (C07C2866011, Robert-reachable): a draft to a fundraising advisor — *"we are unable to move forward with the fundraising plan … We would like to settle for the work performed."* This is a reachable, **named, unquantified** payable (settlement for work performed, no figure anywhere). The word **"only"** is therefore strictly false.

**Severity is MINOR, not a repeat of round-1 F1, for three reasons:** (a) it carries **no figure**, so it is not the figure-omission class that triggers REBUILD; (b) it does **not** corrupt any figure or the coverage-verdict direction — like SVB it only widens the shortfall, and per Hardness_Plan risk #5 a full total-liabilities reconciliation is deliberately kept off the load-bearing path; (c) the claim lives in **OE-internal justification prose**, not in any `S3 must decompose` element, so it will not seed a brittle rubric. But under strictest reading an absolute contradicted by a reachable message is a precision defect — and it is exactly the lesson Reads_s2.md line 53 records ("an 'X is stated nowhere' assertion is only as good as the channel set it was tested against").

**FIX (in place, one clause):** in OE 16 drop the absolute — e.g. "SVB is the only *vendor* obligation in the coverage stack that no reachable record quantifies," or acknowledge the advisor settlement as a second unquantified, non-load-bearing item that likewise cannot flip the coverage direction. No figure, no other OE, and no decompose element changes.

### NOTE (non-blocking) — S3 negative-criterion trap on the 24,275
OE 16a's correct conclusion ("does not belong in the funds available … leaves the figure out of the coverage arithmetic") could tempt S3 to author *"the agent does NOT include the $24,275."* That is a negatively-framed criterion — HG QC dim 23 FAIL, since this prompt mandates no prohibition. The trap is already well-mitigated: OE 20 element 8/9 frame the target **affirmatively** (10,800 net + 2,500 cash = 13,300 available). Carry one explicit line into S3: grade the affirmative 13,300, never the exclusion. Latent, not a current defect.

## Request 3 — is OE 16a overclaiming in the other direction?
**No.** I read the R&D thread to its end. It is a payroll-tax credit applied quarterly against payroll (Fondo, ts 1770765242); with ~$0 payroll (ts 1770767188) a dissolving company cannot apply it in 2026 and it carries forward only on resumed payroll (provider ts 1770780604), which a dissolution will not do, and Robert himself closes it as "a credit, not a rebate" (ts 1770780769). A competent agent that treats 24,275 as inbound cash has read the thread **shallowly** (stopping at the "This $25K is great" line, ts 1770765443). The full-thread read supports **exclusion** from funds available. OE 16a is correct and is a genuine supersession lever, not an overclaim. An agent may still mention the credit exists as a non-cash carryforward and reach the identical coverage verdict — so no UGT break in either direction.

## Request 4 — authority rank 6 (decompose directives)
All four directives (OE 20/21/22/23) trace element-by-element to a prompt sentence. OE 20's 11 elements: page created + window + 0.00 revenue + 7,483.42 spend + retention/engagement peak (prompt L3 "how it genuinely performed and what we paid"); 8,452.64 + Leonard-as-owner (L5 "naming with a figure … and an owner"); 10,800 + 2,500 + **~15,000 wind-down service** + coverage verdict (L7 "whether that genuinely covers shutting down in an orderly way … be precise"). Element 10 (~15,000) is the **cost of orderly shutdown itself**, squarely inside L7's "shutting down in an orderly way" — not an OE-only demand. No element the prompt never asks for. Negative-criterion push: none in any decompose directive (see NOTE for the one latent risk, already affirmatively framed).

## Request 5 — density (25 steps, HG bands ≥40 PASS / 15–39 THIN / <15 INSUFF)
My own sketch, strict reading: necessary calls per step ≈ OE1(1) OE2(2) OE3(4) OE4-6(3) OE7(2) OE8(1) OE10-11(2) OE12(2) OE13(2) OE14(1) OE15(2) OE16(2) OE16a(2) OE16b(1) OE17(1) OE19(1) OE20(2) OE21(1) OE22(1) ≈ **~35 necessary**, total with realistic list/describe/paging/retry inflation **~40–48, midpoint ~43**. Distinct services on the necessary path: **slack, snowflake, confluence(or gdocs), linear(or trello), contacts = 5**. Prompt-eval hard gate (>15 necessary, ≥2 services, multiple meaningful writes, information friction) cleared with wide margin. **Density → PASS** (~43 ≥ 40; far above the 15 floor). The F1-R2 fix adds no calls.

## Request 6 — hardness (five levers)
- **L11 net-vs-gross — SHARPENED.** ~15,000 now sits strictly between net 10,800 and gross 22,500. OE 16b + OE 18 narrow finding ("the wind down service alone … exceeds the 10,800 … survives only against the 22,500 gross") turn the net/gross gap into a discriminating wedge. Confirmed.
- **L10 supersession — carried in THREE places:** deal structure sale→licence (OE 15), vendor keep/cancel state (OE 13), and the R&D credit→carryforward (OE 16a). Confirmed independently.
- **L2 Snowflake FINANCE skip** (OE 17), **L8 multi-link chain** (gross→net→cash→obligations→wind-down cost, now longer), **L7 multi-write** — all present.
- **Plan-vs-prompt delta (expected, not a defect):** the plan targets **4 writes/4 services** (incl. a GSheet tracker) on the pure wind-down spine; the shipped prompt asks for **3 writes** (write-up, post, tracking item) and the OE faithfully delivers 3 (Confluence/gdocs, Slack, Linear/Trello). Prompt > plan; density still ~43 and breadth still 5 services. The plan's density/breadth tables describe the superseded spine, as the handoff notes — no lever lost.

## Request 7 — coverage both directions + OE 18 ordering
Forward (every prompt sentence → OE): performance/spend → OE 4–8; still-running+owner → OE 9–12; money/coverage → OE 14–18; write-up → OE 20; post → OE 21; tracking item → OE 22; lead figures → OE 23. Reverse (no OE beyond prompt): holds; OE 16a establishes what is *not* available, which is part of "where that leaves us." **OE 18 ordering refs resolve:** "Compute … from OE 14, OE 16, OE 16a, OE 16b and OE 17" — all five exist and precede OE 18 after the 16a/16b insertion. Global ordering clause (OE 20 < 21/22, OE 23 last, discovery before writes) intact.

## Lens status (rule-20, one line each)
- **Figures:** all new/changed values EXACT; zero mismatches (table above).
- **False-absence FIGURE class:** CLOSED across all 20 reachable channels, verified by my own authorship-derived sweep. No REBUILD repeat.
- **Residual:** F1-R2 — one reachable *unquantified* obligation falsifies OE 16's word "only"; MINOR, prose-only, ground truth intact.
- **OE 16a direction:** correct; full-thread read supports exclusion; not an overclaim.
- **Authority rank 6:** all 4 decompose directives trace to prompt; no beyond-prompt element; one latent negative-criterion trap for S3 flagged (NOTE), already affirmatively mitigated.
- **Density:** ~43 midpoint, 5 services → PASS.
- **Hardness:** five levers trace; L11 sharpened, L10 in three places; plan-vs-prompt write delta expected.
- **Coverage/ordering:** both directions hold; OE 18 refs resolve.
- **Rule-20 self-check:** F1-R2 catches a defect no deterministic gate reaches (cross-channel reachability sweep + semantic falsification of an absolute qualifier). NOTE catches an HG-dim-23 seed a mechanical scan cannot see pre-S3. No lens padded.

## Verdict rationale
The figure-omission class that surfaced three times is genuinely CLOSED — I re-derived the reachable channel set and swept all 20 channels myself, and every figure bearing on inbound/costs/obligations/cash/ad-spend is carried or correctly out of scope. All new figures match exactly, OE 16a is correct rather than overclaiming, levers/density/coverage/ordering all hold. This is **not** REBUILD. But my sweep found one reachable, named, unquantified obligation (fundraising-advisor settlement, ts 1770836625) that makes OE 16's absolute "the only named obligation that no reachable record quantifies" strictly false. Under the strictest reading that is a sub-5 precision defect on OE Accuracy — fix-in-place, one clause, no figure or downstream artifact affected.

VERDICT: REVISE

---

## Round-2 resolution (F1-R2 fix verified from disk)

Re-read `6_Oracle_Events.txt` OE 16 from disk after the operator's one-clause fix. The fix is exactly as reported and touches OE 16 alone.

- **F1-R2 RETIRED.** The absolute is now scoped to "named **vendor** obligation" — a closed set {Singular, Unity, Helpshift, SVB}. From the Feb sweep already completed: Singular 18,750, Unity ~2.348*9, Helpshift 150*8 all quantified at ts 1770765511.243329 (Helpshift also at ts 1770673467.186629); SVB quantified nowhere (ts 1770860000.975869 / 1770911000.728559 / 1770927223.969899, no amount). The narrowed "only" is TRUE as written.
- **No fresh false-absence claim.** The added sentence "One further unquantified payable sits outside the vendor stack" is existential, not exhaustive — it cannot be falsified the way the old "only" was. The advisor settlement (ts 1770836625.652859) is unquantified in the one message that references it; nothing in the 49-hit sweep attaches a figure.
- **Stays out of S3.** Clause is OE-internal justification prose, self-labelled "corroboration rather than a load-bearing figure … carries no criterion." No rubric carrier; affirmatively framed, so no HG dim-23 negative-criterion push.
- **No knock-on.** Advisor settlement is unquantified, cannot enter OE 18 arithmetic. Available 13,300, stack ~55,950, coverage 23.8%, both findings unchanged. OE 20's 11 decompose elements unaffected.

Deterministic floor re-confirmed by operator: `validate.py --phase oe` PASS 0/0 at 25 steps; `check_persona_acl.py` 0 findings.

The three-times-recurring figure-omission class is CLOSED (round-2 sweep of all 20 reachable channels). The residual precision defect is now retired with no new defect introduced. Under the strictest reading the deliverable holds 5/5 on OE Accuracy.

VERDICT: PASS (STRICT)
