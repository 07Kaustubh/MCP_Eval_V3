# Validator report: oe

**Status:** PASS  
**Fails:** 0 · **Warns:** 1 · **Notes:** 3

## WARN
- OE step 3 (X3 service-mapping): step text references `budget` (expected service `quickbooks` per starpm oe_service_map) but tool call(s) target service(s) ['slack']. Verify the right service is being used for this data type. WARN-only observation period.

## NOTE
- universe: starpm
- OE step count: 19
- no closed fiscal periods in Fact_Ledger.lifecycle.closed_periods — skipping lifecycle precondition check
