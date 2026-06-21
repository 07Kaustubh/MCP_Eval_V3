# Public (stale-to-task pre-baked split)

> Per-task data lives in `Tasks/<TASK_DIR>/_aux/Universe_Split/_changelog.json` (when present). Do not use these files for per-task work.

## Service role

Universe changelog. Records actions taken during scenario construction (engagement letters filed, audits completed, scenarios anchored, etc.). Empty in many task universes; populated only when the universe was built with scripted scenarios.

## Tables (inner shapes)

| File | Key fields |
|---|---|
| `_changelog.json` | `id` (`act_*`), `ts`, `actor` (email or scenario id), `details` (kind-specific map), `action_type` |

## Notes

- Changelog records have a different shape than other Universe_Split files: they DO have top-level `ts` and `actor`, and a nested `details` object — not `row_data`.
- When present, the changelog is the cheapest way to discover which scripted scenarios ran in this task's universe build.

## Discovery patterns

- Search for `action_type` patterns like `ENGAGEMENT_LETTER_ADDENDUM_FILED`, `JE_POSTED`, `RECONCILIATION_CERTIFIED` to find scenario anchor points.
- Cross-reference `details.scenario_id` with the 52 scripted scenarios documented in `Brookfield_Base_Universe/4_Scenario_Storylines.md`.

## MCP tool notes

No direct MCP tools — the changelog is read-only metadata about how the universe was built. Use it for orientation only.
