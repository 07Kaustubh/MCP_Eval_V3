# S4 Rubric Fixes (Pass 2)

Two Bucket-1 defects on `7_Rubrics.json` (sha `b29c850...`, 28 criteria). Both are rubric-side; neither requires prompt or OE changes.

Applying both edits drops the All-Failing Rubrics sub-dim from **3/5 NON-FAIL** to **5/5 PASS** and loses no hardness lever coverage.

---

## Fix 1 — R1: Broaden ART tracker accept set

### Before

```json
{
    "title": "The Agent creates a Linear comment on the ART-team VFX tracking issue (either ART-770 as the most-recently-updated ART VFX ticket, or the top-level ART-252 'ART: VFX' tracker; either is acceptable).",
    "category": "Outcome 1.1",
    "justification": "The prompt requires a reconciliation comment on the ART tracking ticket. OE 24's fallback deterministically resolves the ART tracking ticket to ART-770 because zero fresh unresolved ART VFX tickets exist as of 2026-02-28.",
    "evidence": "Inspect Linear write actions. FAIL if no linear_create_comment call is made on either ART-770 or ART-252, and FAIL if a linear_create_comment call is made but its issueId is neither 'ART-770' nor 'ART-252'."
}
```

### After

```json
{
    "title": "The Agent creates a Linear comment on the ART-team VFX tracking issue (ART-770 as the most-recently-updated ART VFX ticket, ART-252 as the top-level 'ART: VFX' tracker, or ART-760 as the next-most-recent ART VFX ticket; any of the three is acceptable).",
    "category": "Outcome 1.1",
    "justification": "The prompt requires a reconciliation comment on the ART tracking ticket without naming a specific issue id. Three ART VFX Linear issues are plausible reconciliation homes given the universe state on 2026-02-28: ART-770 (most-recently-updated), ART-252 (top-level tracker), and ART-760 (next-most-recent).",
    "evidence": "Inspect Linear write actions. FAIL if no linear_create_comment call is made on any of ART-770, ART-252, or ART-760. FAIL if a linear_create_comment call is made but its issueId is none of these three. FAIL if the agent creates a new Linear issue and comments on the new issue rather than on one of the three existing ART VFX trackers."
}
```

### Trajectory citations

- Run 1: `linear_create_comment(issueId='ZOM-247')` — Zombie Match roadmap ticket, not ART VFX.
- Run 2: `linear_create_comment(issueId='ART-760')` — legitimate ART VFX ticket, would pass under new accept set.
- Run 3: agent called `linear_create_issue` to create ART-2438 then commented there — creating a new issue is not commenting on an existing tracker; still fails.
- Run 4: `linear_create_comment(issueId='ART-760')` — would pass under new accept set.
- Run 5: `linear_create_comment(issueId='ZOM-247')` — same as Run 1.
- Run 6: `linear_create_comment(issueId='ZOM-521')` — Zombie Match, not ART VFX.

### Projected pass rate after fix

R1 becomes 2/6 pass (Runs 2, 4) — a partial fail rather than AF, appropriately hard, no lever lost.

### Rationale

The prompt says only "the ART tracking ticket in Linear" without naming an id. Agents that landed on ART-760 followed correct reasoning (searched ART-*, filtered for VFX, picked a plausible tracker). The current accept set is over-tight for what the prompt asks. Broadening from two ids to three preserves the discrimination against agents that pick ZOM-* tickets or create new issues, while accepting the two runs that reached a valid ART tracker by legitimate navigation.

The rubric evidence stays fully mechanical (an id must be one of three strings). No judge discretion introduced.

---

## Fix 2 — R3: Retitle to remove hardcoded ticket id

### Before

```json
{
    "title": "The Agent's ART-770 comment identifies Combo-Fighters PR #36 as merged on 2026-02-11.",
    ...
}
```

### After

```json
{
    "title": "The Agent's ART-team VFX tracker comment identifies Combo-Fighters PR #36 as merged on 2026-02-11.",
    ...
}
```

Category, justification, evidence unchanged.

### Rationale

R2, R4, R5, R6 all begin `The Agent's ART-team VFX tracker comment identifies...`. Only R3 hardcodes `ART-770 comment` in its title. The evidence field already references "the ART-team VFX tracker comment body (on either ART-770 or ART-252)" (and after Fix 1, also ART-760), so the title is inconsistent with its own evidence and with its four siblings.

Per rule 16, a title that reliably induces the same judge misreading is a rubric defect. All six verifier judgments on R3 begin with "No comment was made on ART-770" (or equivalent) before considering content — the title is causing the judge to check ticket id first and skip the content check, exactly the failure mode rule 16 describes.

### Trajectory citations

- All six runs: judge decision begins with a target-mismatch statement before considering PR #36 content. Retitling to match siblings removes the mechanical target-check bias and lets the content check run on its own merits.

### Projected pass rate after fix

R3 stays 0/6 pass (no run named PR #36 with the 2026-02-11 date in its ART tracker comment — including the two runs that produced ART-760 comments). But it reclassifies from Bucket 1 to Bucket 3 (legit AF, symmetric with R4). AF sub-dim ratio drops from 2/8 to 0/6 = 0% (5/5 PASS).

---

## Post-fix gate re-run

After applying both edits, run:

```
python Validators/validate.py Generated_Tasks/3_6a797ca9aaeb231749d71fc3 --phase rubrics
python Validators/check_criterion_dependencies.py Generated_Tasks/3_6a797ca9aaeb231749d71fc3
python Validators/check_oe_rubric_sync.py Generated_Tasks/3_6a797ca9aaeb231749d71fc3
python Validators/check_rubric_antipatterns.py Generated_Tasks/3_6a797ca9aaeb231749d71fc3
python Validators/check_export_freshness.py Generated_Tasks/3_6a797ca9aaeb231749d71fc3 --pin
```

Expected: all exit 0. Pin re-created against the edited rubric bytes.
