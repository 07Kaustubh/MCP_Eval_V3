#!/usr/bin/env python3
"""
Universe registry — per-universe constants for multi-universe pipeline support.

Three universes:
- brookfield: CPAs & business advisory firm (current default)
- keystone: Residential mortgage brokerage (V3.1)
- moveops: B2B remote-work relocation services (V2.1)

Every validator + runbook + council prompt should read constants via
`get_universe_constants(detect_universe(task_dir))` rather than hardcoding
universe-specific values.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

UNIVERSES = {
    "brookfield": {
        "name": "Brookfield CPAs & Advisors",
        "framework_version": "v3",
        "domain": "Public accounting / business advisory",
        "base_path": "Brookfield_Base_Universe",
        "docs_path": "Docs",
        "evals_path": "Evals",
        "tool_catalog": "Brookfield_Base_Universe/8_Server_Tools_Details.json",
        "persona_briefs": "Brookfield_Base_Universe/2_Persona_Briefs.md",
        "business_function_doc": "Brookfield_Base_Universe/3_Task_Categories_Business_Functions.md",
        "universe_one_pager": "Brookfield_Base_Universe/7_Brookfield_Universe_One_pager.md",
        "qc_reference_path": "QC_Tasks/V3_Tasks",

        "today": "2026-06-12",
        "today_tz": "US/Eastern",
        "persona_email_domain": "brookfieldcpas.com",
        "business_functions": [
            "Accounting Operations", "Bookkeeping", "Tax", "Compliance & Internal Controls",
            "Audit", "AP / Vendor Operations", "BlackLine Close-Discipline & Variance",
            "Engagement Mgmt & Client Operations", "Executive / Partner Oversight",
            "HR & People Operations",
        ],
        "tight_identifiers": [
            "channel names", "doc IDs", "JE IDs", "vendor names", "company names",
            "account numbers", "dollar amounts", "dates", "fiscal periods", "ticket IDs",
        ],
        "oe_service_map": {
            "reconciliations": "blackline", "exceptions": "blackline", "variance": "blackline",
            "ap_invoices": "sap_subledger", "vendor_master": "sap_subledger",
            "journal_entries": "oracle_gl", "accounts": "oracle_gl", "fiscal_periods": "oracle_gl",
            "retention": "records_vault", "documents": "records_vault",
            "tickets": "linear", "issues": "linear",
            "hr_personnel": "airtable",
            "chat": "slack", "channels": "slack",
            "email_threads": "email",
        },
        "cross_service_pairs": [
            ("email", "sap_subledger"), ("email", "oracle_gl"), ("email", "blackline"),
            ("oracle_gl", "blackline"), ("oracle_gl", "sap_subledger"),
            ("records_vault", "linear"), ("slack", "linear"),
        ],

        "retention_codes": {"AICPA_SQMS_7Y", "IRS_TAX_7Y", "FIRM_INTERNAL", "INDEFINITE"},
        "slack_channels": {f"C{n:03d}" for n in range(1, 11)} | {"C012"},
        "classifications": {"public", "internal", "restricted"},
        "blackline_exception_types": {
            "unrecorded_invoice", "duplicate_entry_detected", "timing_difference_over_sla",
            "subledger_feed_drop", "missing_accrual_variance", "fx_revaluation_drift",
        },
        "npcs": {
            "Owen Mercer", "Brenda Abbas", "Sofia Halabi", "Farah Dlamini",
            "James Randall", "Lucia Ferreira", "Mateo Kovac",
        },
        "services": ["oracle_gl", "sap_subledger", "blackline", "records_vault",
                     "airtable", "linear", "email", "slack", "contacts", "messaging", "reminder"],

        "account_trap_check": True,
        "entity_name_to_id": {
            "brookfield": "brookfield",
            "acme cloud": "acme_cloud", "acme": "acme_cloud",
            "northstar legal": "northstar_legal", "northstar": "northstar_legal",
        },
        "lifecycle_check_kind": "fiscal_period",
        "lifecycle_states_closed": {"closed", "locked"},
        "lifecycle_states_open": {"open", "draft", "active"},

        "tool_param_traps": {
            "email_send_email": {"content_field": "content", "wrong_field": "body"},
            "slack_conversations_add_message": {"content_field": "payload", "wrong_field": "text"},
            "records_vault_upload_document": {"content_field": "content_b64", "wrong_fields": ["file", "data"], "window": 100, "ignorecase": True},
            "linear_create_issue": {"required": "teamId", "wrong": "team", "window": 100},
        },

        "landmines": [
            "Account-number trap: 105000 / 120000 differ per entity (Cash-Trust on Brookfield, IOLTA on Northstar, Short-term Investments on Acme; 120000 absent on Brookfield, Client Cost Advances on Northstar, Deferred Commissions on Acme). Query oracle_gl.ogl_accounts WHERE account_number=N AND entity_id=E before trusting any prose role label.",
            "Email-chain truthfulness: 'X never responded' claims must be proven by (i) parent_id descendant walk from sender's email, (ii) sender-filter across same subject prefix on email.emails. Never trust prose 'no response' claim without the walk.",
            "Persona-scope: 'my X' framing binds to persona's universe assignments (created_by / owner_email / approver_email = persona email). Verify every rubric value is in the persona's scope.",
            "Lifecycle precondition: posting JE to closed period requires either earlier unlock step OR late_post_authorization_id on the post call.",
        ],
    },

    "keystone": {
        "name": "Keystone Mortgage Partners",
        "framework_version": "v3.1",
        "domain": "Residential mortgage brokerage",
        "base_path": "Mortgage_Base_Universe",
        "docs_path": "Docs_keystone",
        "evals_path": "Evals_keystone",
        "tool_catalog": "Mortgage_Base_Universe/6_Server_Tools_Details.json",
        "persona_briefs": "Mortgage_Base_Universe/3_Persona_Briefs.md",
        "business_function_doc": "Mortgage_Base_Universe/5_Task_Categories_Business_Functions.md",
        "universe_one_pager": "Mortgage_Base_Universe/2_Summary.md",
        "qc_reference_path": "QC_Tasks/V3.1_Tasks",

        "today": "2026-04-28",
        "today_tz": "US/Eastern",
        "persona_email_domain": "keystonemortgage.com",
        "business_functions": [
            "Loan Operations", "Compliance", "Sales", "Finance", "Executive", "IT",
        ],
        "business_function_weights": {
            "Loan Operations": 0.30, "Compliance": 0.20, "Sales": 0.20,
            "Finance": 0.15, "Executive": 0.10, "IT": 0.05,
        },
        "tight_identifiers": [
            "channel names", "doc IDs", "loan IDs", "vendor names", "company names",
            "account numbers", "dollar amounts", "dates", "fiscal periods", "ticket IDs",
        ],
        "oe_service_map": {
            "loans": "mortgage_los", "borrowers": "mortgage_los", "conditions": "mortgage_los",
            "document_checklist": "mortgage_los", "disclosures": "mortgage_los",
            "ap_invoices": "quickbooks", "vendor_bills": "quickbooks", "accounts": "quickbooks",
            "payments": "stripe", "charges": "stripe", "transfers": "stripe", "refunds": "stripe",
            "bank_transactions": "stripe", "fc_accounts": "stripe",
            "borrower_documents": "filesystem", "pdfs": "filesystem",
            "leads": "crm", "deals": "crm", "engagements": "crm",
            "chat": "slack", "channels": "slack",
            "email_threads": "email",
        },
        "cross_service_pairs": [
            ("email", "mortgage_los"), ("email", "quickbooks"), ("email", "crm"),
            ("mortgage_los", "crm"), ("mortgage_los", "filesystem"), ("mortgage_los", "stripe"),
            ("quickbooks", "stripe"), ("slack", "mortgage_los"),
        ],

        "retention_codes": set(),
        "slack_channels": {f"C{n:03d}" for n in range(1, 9)},
        "classifications": set(),
        "blackline_exception_types": set(),
        "npcs": {
            "Marcus Webb",
        },
        "services": ["mortgage_los", "stripe", "filesystem", "crm", "quickbooks",
                     "email", "slack", "contacts"],

        "account_trap_check": False,
        "entity_name_to_id": {
            "keystone": "keystone", "keystone mortgage": "keystone",
        },
        "lifecycle_check_kind": "TRID",
        "loan_statuses_open": {
            "application", "conditional_approval", "processing", "underwriting", "clear_to_close",
        },
        "loan_statuses_closed": {"closed", "denied", "withdrawn"},
        "condition_statuses": {"outstanding", "cleared"},
        "trid_windows": {
            "loan_estimate_days_after_app": 3,
            "closing_disclosure_days_before_close": 3,
        },

        "tool_param_traps": {
            "email_send_email": {"content_field": "content", "wrong_field": "body"},
            "slack_conversations_add_message": {"content_field": "payload", "wrong_field": "text"},
            "mortgage_los_add_condition": {"required": "loan_id"},
            "stripe_create_charge": {"content_field": "amount"},
        },

        "landmines": [
            "TRID timing: Loan Estimate must be sent within 3 business days of application; Closing Disclosure must be delivered 3 business days before closing. Query mortgage_los.disclosures for actual sent_date vs application_date / closing_date and verify windows are respected.",
            "Email-chain truthfulness: 'X never responded' claims must be proven by (i) parent_id descendant walk from sender's email, (ii) sender-filter across same subject prefix on email.emails. Never trust prose 'no response' claim without the walk.",
            "Mortgage LOS vs CRM source-of-truth: loan-level data lives in mortgage_los (loans, borrowers, conditions, document_checklist_items). CRM holds the marketing / referral funnel (leads, deals, engagements). When a claim references loan state, never trust CRM as the source — query mortgage_los.",
            "Departed-employee trap: Marcus Webb is on the staff roster but has departed (scenario_7da8f37a — evidence of pre-resignation data exfiltration). Tasks must not ask the agent to interact with him as if active.",
            "Persona-scope: 'my borrowers' / 'my pipeline' binds to persona's loan officer assignments (mortgage_los.loans.loan_officer_email = persona email). Verify every rubric value is in scope.",
        ],
    },

    "moveops": {
        "name": "MoveOps Inc.",
        "framework_version": "v2.1",
        "domain": "B2B remote-work relocation services",
        "base_path": "MoveOps_Base_Universe",
        "docs_path": "Docs_moveops",
        "evals_path": "Evals_moveops",
        "tool_catalog": "MoveOps_Base_Universe/6_Server_Tools_Details.json",
        "persona_briefs": "MoveOps_Base_Universe/2_Persona_Briefs.md",
        "business_function_doc": "MoveOps_Base_Universe/3_Task_Categories_Business_Functions.md",
        "universe_one_pager": "MoveOps_Base_Universe/5_MoveOps_One_Pager.md",
        "qc_reference_path": "QC_Tasks/V2.1_Tasks",

        "today": "2026-04-26",
        "today_tz": "US/Pacific",
        "persona_email_domain": "moveops.com",
        "business_functions": [
            "Operations", "Customer Engagement / Support", "Engineering", "Finance", "Executive",
        ],
        "business_function_weights": {
            "Operations": 0.25, "Customer Engagement / Support": 0.30, "Engineering": 0.20,
            "Finance": 0.15, "Executive": 0.10,
        },
        "tight_identifiers": [
            "channel names", "ticket IDs", "relocation IDs", "vendor names", "company names",
            "dollar amounts", "dates", "coordinator names", "Airtable record IDs", "CRM deal IDs",
        ],
        "oe_service_map": {
            "relocations": "airtable", "stipends": "airtable", "client_accounts": "airtable",
            "vendor_records": "airtable",
            "ap_invoices": "quickbooks", "vendor_bills": "quickbooks", "customers": "quickbooks",
            "accruals": "quickbooks", "vendor_master": "quickbooks",
            "deals": "crm", "engagements": "crm", "leads": "crm",
            "tickets": "linear", "issues": "linear", "linear_projects": "linear",
            "calendar_events": "calendar",
            "chat": "slack", "channels": "slack",
            "email_threads": "email",
            "contacts": "contacts",
        },
        "cross_service_pairs": [
            ("email", "airtable"), ("email", "crm"), ("email", "quickbooks"),
            ("airtable", "quickbooks"), ("airtable", "linear"), ("airtable", "crm"),
            ("slack", "linear"), ("slack", "airtable"), ("slack", "quickbooks"),
            ("crm", "calendar"), ("crm", "airtable"),
        ],

        "retention_codes": set(),
        "slack_channels": {f"C{n:03d}" for n in range(1, 10)},
        "classifications": set(),
        "blackline_exception_types": set(),
        "npcs": {
            "Marcus Webb",
        },
        "services": ["airtable", "calendar", "contacts", "crm", "email", "linear",
                     "public", "quickbooks", "slack"],

        "account_trap_check": False,
        "entity_name_to_id": {
            "moveops": "moveops", "moveops inc": "moveops",
        },
        "lifecycle_check_kind": "PHMSA_hazmat",
        "lifecycle_states_closed": set(),
        "lifecycle_states_open": set(),

        "tool_param_traps": {
            "email_send_email": {"content_field": "content", "wrong_field": "body"},
            "slack_conversations_add_message": {"content_field": "payload", "wrong_field": "text"},
            "linear_create_issue": {"required": "team", "wrong": "teamId"},
            "linear_create_comment": {"required": "issueId", "content_field": "body"},
            "crm_create_engagement": {"required": "engagement_type", "content_field": "body"},
            "airtable_update_records": {"required": "base_id", "also_required": "table_id"},
            "quickbooks_create_customer": {"required": "DisplayName"},
        },

        "landmines": [
            "PHMSA DOT hazmat compliance: hazmat shipments (cryogenic lab equipment, Class 3B lasers, chemical samples) require a signed DOT certificate from the freight carrier. Verbal driver confirmation does NOT count. When a claim references hazmat documentation, verify the Airtable relocation record AND the Swift / Heartland email thread carry the actual signed certificate reference.",
            "Email-chain truthfulness: 'X never responded' claims must be proven by (i) parent_id descendant walk from sender's email, (ii) sender-filter across same subject prefix on email.emails. Never trust prose 'no response' claim without the walk.",
            "Airtable Relocations source-of-truth: relocation state lives in Airtable (tblRelocations01 — status, vendor, coordinator, special handling). CRM holds the deal / engagement funnel. When a claim references relocation state, never trust CRM as the source — query Airtable.",
            "Vendor cross-reference: Heartland Q1 invoice has multiple cancelled / reassigned moves billed in error. Any vendor-payment-dispute task must cross-reference the invoice line items against tblRelocations01 vendor + status, NOT trust the invoice prose.",
            "Marcus Webb identity (MoveOps): Marcus Webb here is a BrightLoop Analytics senior analyst (CLIENT employee), distinct from the KeyStone departed-employee Marcus Webb. Same name, different person, different universe — do NOT carry KeyStone's departed-employee logic over.",
            "ExpenseBot pilot bugs: the stipend auto-categorizer has known policy-config bugs for Vectral and Mosaic (exclusion checks, amount validation, duplicate hash detection). When verifying stipend approval correctness, query Airtable stipend records against the policy + Dmitri's audit findings (linear ticket portfolio).",
            "Persona-scope: 'my clients' / 'my relocations' binds to persona's CRM assignment or Airtable coordinator field (account_manager_email or coordinator_email = persona email). Verify every rubric value is in scope.",
        ],
    },

    "starpm": {
        "name": "Star Property Management",
        "framework_version": "v4",
        "domain": "Residential property management",
        "base_path": "StarPM_Base_Universe",
        "docs_path": "Docs_starpm",
        "evals_path": "Evals_starpm",
        "tool_catalog": "StarPM_Base_Universe/7_Server_Tools_Details.json",
        "persona_briefs": "StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md",
        "business_function_doc": "StarPM_Base_Universe/3_StarPM_TASK CATEGORIES.md",
        "universe_one_pager": "StarPM_Base_Universe/0_StarPM_One-Pager.md",
        "qc_reference_path": "QC_Tasks/V4_Tasks",

        "today": "2026-07-01",
        "today_tz": "America/Chicago",
        "persona_email_domain": "starpm.com",
        "business_functions": [
            "Property Operations", "Portfolio Coord & Owner Relations",
            "QC & Field Services", "Maintenance & Repairs", "Leasing & Applicant Intake",
        ],
        "business_function_weights": {
            "Property Operations": 0.32, "Portfolio Coord & Owner Relations": 0.20,
            "QC & Field Services": 0.10, "Maintenance & Repairs": 0.18,
            "Leasing & Applicant Intake": 0.20,
        },
        "tight_identifiers": [
            "channel names", "unit numbers", "property names", "vendor names", "owner names",
            "invoice numbers", "dollar amounts", "dates", "Airtable record IDs", "Linear issue IDs",
        ],
        "oe_service_map": {
            "make_ready": "airtable", "turns": "airtable", "maintenance_tickets": "airtable",
            "unit_availability": "airtable",
            "rent_invoices": "quickbooks", "vendor_bills": "quickbooks", "journal_entries": "quickbooks",
            "delinquency": "quickbooks", "owner_distributions": "quickbooks", "accounts": "quickbooks",
            "leasing_deals": "hubspot", "applicants": "hubspot", "leasing_funnel": "hubspot",
            "tickets": "linear", "issues": "linear", "linear_projects": "linear",
            "calendar_events": "gcalendar",
            "email_threads": "gmail", "drafts": "gmail",
            "chat": "slack", "channels": "slack",
            "contacts": "contacts",
        },
        "cross_service_pairs": [
            ("gmail", "airtable"), ("gmail", "quickbooks"), ("gmail", "hubspot"),
            ("airtable", "linear"), ("airtable", "quickbooks"),
            ("hubspot", "gmail"), ("slack", "airtable"), ("slack", "linear"),
            ("gcalendar", "gmail"), ("quickbooks", "airtable"),
        ],

        "retention_codes": set(),
        "slack_channels": {f"C{n:03d}" for n in range(1, 9)},
        "classifications": set(),
        "blackline_exception_types": set(),
        "npcs": set(),
        "personas": {
            "brooke.phillips@starpm.com": "Brooke Phillips",
            "lisa.smith@starpm.com": "Lisa Smith",
            "sandra.allen@starpm.com": "Sandra Allen",
            "john.smith@starpm.com": "John Smith",
            "james.bennett@starpm.com": "James Bennett",
            "jaime.salinas@starpm.com": "Jaime Salinas",
            "randy.jones@starpm.com": "Randy Jones",
            "carlos.mendez@starpm.com": "Carlos Mendez",
            "patricia.nguyen@starpm.com": "Patricia Nguyen",
            "kevin.okafor@starpm.com": "Kevin Okafor",
            "elias.navarro@starpm.com": "Elias Navarro",
            "denise.morales@starpm.com": "Denise Morales",
            "teresa.wood@starpm.com": "Teresa Wood",
        },
        "services": ["airtable", "contacts", "gcalendar", "gmail", "hubspot", "linear",
                     "quickbooks", "slack"],

        "account_trap_check": False,
        "entity_name_to_id": {
            "star property management": "starpm", "starpm": "starpm", "star pm": "starpm",
        },
        "lifecycle_check_kind": "TX_rent_eviction",
        "lifecycle_states_closed": set(),
        "lifecycle_states_open": set(),

        "tool_param_traps": {
            "slack_send_message": {"content_field": "message", "wrong_fields": ["payload", "text"], "window": 100, "ignorecase": True},
            "create_draft": {"content_field": "body", "wrong_field": "content", "window": 100, "ignorecase": True},
            "save_issue": {"required": "team", "wrong": "teamId", "window": 100, "ignorecase": True},
            "save_comment": {"required": "issueId", "content_field": "body"},
            "create_records_for_table": {"required": "baseId", "also_required": "tableId"},
            "manage_crm_objects": {"required": "object_type", "also_required": "action"},
            "create_journal_entry": {"content_field": "properties"},
        },

        "landmines": [
            "No account-number trap, no retention codes, no classifications: single entity (starpm), no Records Vault. Files under Data/Files/ are read-only reference PDFs the agent reads directly.",
            "Near-duplicate decoy files: invoice-2026-419 vs invoice-2026-419-287; invoice-BILL-2026-0392 vs invoice-BILL-2026-0392-920; invoice-2026-481 vs 2026-481-makeready; agreement ...tanya-mitchell vs ...tanya-mitchell-2 (plus the separate reasonable-accommodation-lease-addendum); report-laspalmas-8d-qc-inspection vs -2; final-walk-clearance-las-palmas-8d-2026 vs -2; Las Vistas 9D carries two differently-named QC reports. Select the authoritative artifact, never the decoy.",
            "Cross-property Unit 14 ambiguity: 'Unit 14' is not unique (Rio Bend Unit 14, Sunset Ridge Unit 14, Unit 14 Tanya Mitchell Eviction). Disambiguate by property before acting.",
            "Semantic contradiction: Tanya Mitchell appears simultaneously in a fair-housing ESA accommodation track AND a full rent-to-eviction track. A task must not conflate the protected-accommodation posture with the eviction posture.",
            "Source-of-truth: Airtable (tblMakeReady, tblMaintenanceTickets) is the system of record for make-ready and maintenance work orders; Linear is explicitly secondary. HubSpot is the system of record for the leasing / applicant funnel. Never trust Linear for maintenance ground truth.",
            "Name collisions: Tony Reyes (staff) vs Tommy Reyes (tenant); Patricia Nguyen (persona) vs Patricia Lowe (Court Clerk); Kevin Okafor (persona) vs Jerome Okafor (referral partner); Lisa Smith and John Smith (two Smith personas).",
            "TX rent-to-eviction ladder (hardcoded): 5-day grace period, first late-rent notice, payment plan, 3-day pay-or-quit notice, eviction filing packet (rent ledger plus all prior notices plus payment-plan trail plus owner authorization), JP-court coordination with Court Clerk Patricia Lowe. HVAC failures in San Antonio summer are life-safety events.",
            "Persona-scope: 'my property' / 'my turns' binds to the persona's assigned property and Airtable coordinator field. Verify every rubric value is in the persona's scope.",
        ],
    },
}


def get_universe_constants(universe_name: str) -> dict:
    """Return the constants dict for a universe. Defaults to brookfield if not recognized."""
    return UNIVERSES.get(universe_name.lower().strip(), UNIVERSES["brookfield"])


_KEYSTONE_SIGNALS = re.compile(
    r"\b(?:mortgage_los|TRID|loan\s+estimate|closing\s+disclosure|Keystone\s+Mortgage|keystonemortgage\.com|borrower|loan\s+officer|underwriting\s+condition|wholesale\s+lender|rate\s+lock|stripe_create_charge|stripe_create_refund|mortgage_los_\w+|filesystem_\w+)\b",
    re.IGNORECASE,
)
_BROOKFIELD_SIGNALS = re.compile(
    r"\b(?:oracle_gl|BlackLine|Records?\s+Vault|Brookfield\s+CPAs?|brookfieldcpas\.com|journal\s+entr|trial\s+balance|SAP\s+subledger|fiscal\s+period|northstar_legal|acme_cloud|AICPA_SQMS_7Y|IRS_TAX_7Y|late_post_authorization_id)\b",
    re.IGNORECASE,
)
_MOVEOPS_SIGNALS = re.compile(
    r"\b(?:MoveOps|moveops\.com|Elena\s+Rostova|PHMSA|hazmat|relocation\s+coordinator|stipend\s+platform|UrbanNest|Heartland\s+Movers|Swift\s+Relocations|Atlas\s+Corporate\s+Travel|Vectral\s+Systems|Canopy\s+Health|BrightLoop|Mosaic\s+Robotics|GreenStack\s+Energy|PivotPoint|NorthWind\s+Technologies|StormCloud|airtable_update_records|tblRelocations|tblStipends|ExpenseBot|auto-categorizer)\b",
    re.IGNORECASE,
)
_STARPM_SIGNALS = re.compile(
    r"\b(?:Star\s+Property\s+Management|starpm\.com|hubspot|quickbooks|gcalendar|make-ready|owner-relations|Brooke\s+Phillips|Patricia\s+Nguyen|Teresa\s+Wood)\b",
    re.IGNORECASE,
)


def detect_universe(task_dir: Path) -> str:
    """Auto-detect universe from task contents. Writes _aux/Universe.txt and returns the name.

    Highest-signal universe wins. Ties default to brookfield (back-compat).
    """
    task_dir = Path(task_dir)
    marker = task_dir / "_aux" / "Universe.txt"
    if marker.is_file():
        cached = marker.read_text(encoding="utf-8").strip().lower()
        if cached in UNIVERSES:
            return cached

    scores = {"brookfield": 0, "keystone": 0, "moveops": 0, "starpm": 0}
    for candidate in ("1_Business_Function.txt", "2_Persona.txt", "5_Prompt.txt"):
        f = task_dir / candidate
        if f.is_file():
            text = f.read_text(encoding="utf-8", errors="ignore")
            scores["keystone"] += len(_KEYSTONE_SIGNALS.findall(text))
            scores["brookfield"] += len(_BROOKFIELD_SIGNALS.findall(text))
            scores["moveops"] += len(_MOVEOPS_SIGNALS.findall(text))
            scores["starpm"] += len(_STARPM_SIGNALS.findall(text))

    universe_data = task_dir / "3_UniverseDataForThisTask.json"
    if universe_data.is_file():
        sample = universe_data.read_text(encoding="utf-8", errors="ignore")[:50000]
        scores["keystone"] += len(_KEYSTONE_SIGNALS.findall(sample))
        scores["brookfield"] += len(_BROOKFIELD_SIGNALS.findall(sample))
        scores["moveops"] += len(_MOVEOPS_SIGNALS.findall(sample))
        scores["starpm"] += len(_STARPM_SIGNALS.findall(sample))

    if all(v == 0 for v in scores.values()):
        universe = "brookfield"
    else:
        max_score = max(scores.values())
        winners = [u for u, s in scores.items() if s == max_score]
        if "brookfield" in winners:
            universe = "brookfield"
        else:
            universe = sorted(winners)[0]

    marker.parent.mkdir(parents=True, exist_ok=True)
    marker.write_text(universe + "\n", encoding="utf-8")
    return universe


def list_universes() -> list:
    return sorted(UNIVERSES.keys())


# Per-framework behavioral profile, keyed by a universe's framework_version.
# Nothing reads this yet (additive). It encodes the V4 (starpm) divergence from
# the V3/V3.1/V2.1 baseline: per-model trajectories, a lower average-tool-call
# density floor, and the injection + submission-gate phases. Wire consumers
# through get_framework_profile(universe_name) in a later wave.
FRAMEWORKS = {
    "v3": {
        "density_target": 50,
        "density_floor_avg_tool_calls": 40,
        "verifier_models": ["single"],
        "verifier_files": ["8_Verifier_Fails.txt"],
        "trajectory_layout": "flat",
        "extra_phases": [],
        "docs_path": "Docs",
        "evals_path": "Evals",
        "qc_reference_path": "QC_Tasks/V3_Tasks",
    },
    "v3.1": {
        "density_target": 50,
        "density_floor_avg_tool_calls": 40,
        "verifier_models": ["single"],
        "verifier_files": ["8_Verifier_Fails.txt"],
        "trajectory_layout": "flat",
        "extra_phases": [],
        "docs_path": "Docs_keystone",
        "evals_path": "Evals_keystone",
        "qc_reference_path": "QC_Tasks/V3.1_Tasks",
    },
    "v2.1": {
        "density_target": 50,
        "density_floor_avg_tool_calls": 40,
        "verifier_models": ["single"],
        "verifier_files": ["8_Verifier_Fails.txt"],
        "trajectory_layout": "flat",
        "extra_phases": [],
        "docs_path": "Docs_moveops",
        "evals_path": "Evals_moveops",
        "qc_reference_path": "QC_Tasks/V2.1_Tasks",
    },
    "v4": {
        "density_floor_avg_tool_calls": 15,
        "verifier_models": ["opus", "gemini"],
        "verifier_files": ["8a_Verifier_Fails_Opus.txt", "8b_Verifier_Fails_Gemini.txt"],
        "trajectory_layout": "per_model",
        "extra_phases": ["injection", "submission_gate"],
        "docs_path": "Docs_starpm",
        "evals_path": "Evals_starpm",
        "qc_reference_path": "QC_Tasks/V4_Tasks",
    },
}


def get_framework_profile(universe_name: str) -> dict:
    """Return the framework profile for a universe's framework_version.

    Resolves the universe (brookfield=v3, keystone=v3.1, moveops=v2.1,
    starpm=v4) to its framework_version and looks that up in FRAMEWORKS.
    Nothing reads this yet; it encodes the V4 behavioral divergence for
    future wiring. Defaults to v3 for an unknown / unversioned universe.
    """
    version = get_universe_constants(universe_name).get("framework_version", "v3")
    return FRAMEWORKS.get(version, FRAMEWORKS["v3"])


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 universes.py <task_dir>")
        print(f"Known universes: {list_universes()}")
        sys.exit(1)
    u = detect_universe(Path(sys.argv[1]))
    consts = get_universe_constants(u)
    print(f"Detected universe: {u}")
    print(f"Name: {consts['name']}")
    print(f"Domain: {consts['domain']}")
    print(f"Base path: {consts['base_path']}")
    print(f"Services: {consts['services']}")
    print(f"Slack channels: {sorted(consts['slack_channels'])}")
    print(f"NPCs: {sorted(consts['npcs'])}")
