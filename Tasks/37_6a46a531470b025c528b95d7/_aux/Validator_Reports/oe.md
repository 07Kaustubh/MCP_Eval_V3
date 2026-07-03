# Validator report: oe

**Status:** PASS  
**Fails:** 0 · **Warns:** 1 · **Notes:** 3

## WARN
- OE step 10 (X3 service-mapping): step text references `loans` (expected service `mortgage_los` per keystone oe_service_map) but tool call(s) target service(s) ['crm']. Verify the right service is being used for this data type. WARN-only observation period.

## NOTE
- universe: keystone
- OE step count: 26
- no closed fiscal periods in Fact_Ledger.lifecycle.closed_periods — skipping lifecycle precondition check
