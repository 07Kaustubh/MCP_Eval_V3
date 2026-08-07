import sys, statistics, json
sys.path.insert(0, "/home/sumit/Desktop/MCP_Eval_V3/Generated_Tasks/2_6a6beba55996ad2ada369b15/_aux")
from stream_sf import stream_rows, peak_mib

PATH = "/home/sumit/Desktop/MCP_Eval_V3/Generated_Tasks/2_6a6beba55996ad2ada369b15/_aux/Universe_Split/snowflake.snowflake.tables.json"

TARGETS = {"DAILY_ACTIVE_USERS", "REVENUE_DAILY", "REVENUE_DAILY_V2",
           "AD_SPEND_DAILY", "CASH_BALANCE"}

schema_printed = {}
out = {}

for src, rd in stream_rows(PATH):
    if not isinstance(rd, dict):
        continue
    name = rd.get("name")
    if name not in TARGETS:
        continue
    rows = rd.get("rows") or []
    key = (rd.get("database"), rd.get("schema"), name)
    # print schema once per table name
    if name not in schema_printed and rows:
        schema_printed[name] = sorted(rows[0].keys())
        print(f"[SCHEMA] {key} nrows={len(rows)} keys={schema_printed[name]}")

    if name == "DAILY_ACTIVE_USERS":
        combo = [r for r in rows if r.get("game_id") == "combo_fighter"]
        if not combo:
            continue
        # detect DAU field
        dau_field = None
        for cand in ("dau", "daily_active_users", "active_users", "daily_actives"):
            if cand in combo[0]:
                dau_field = cand; break
        by_date = {}
        nu = ss = 0
        d1 = []
        for r in combo:
            d = r.get("date")
            if dau_field is not None:
                by_date[d] = by_date.get(d, 0) + (r.get(dau_field) or 0)
            nu += r.get("new_users") or 0
            ss += r.get("total_sessions") or 0
            if r.get("d1_retention_pct") is not None:
                d1.append(r["d1_retention_pct"])
        dates = sorted(d for d in (r.get("date") for r in combo) if d)
        peak_day = max(by_date.values()) if by_date else None
        peak_single = max((r.get(dau_field) or 0) for r in combo) if dau_field else None
        out["DAU"] = {
            "nrows": len(combo), "min_date": dates[0], "max_date": dates[-1],
            "distinct_dates": len(set(dates)),
            "dau_field": dau_field, "peak_day_sum": peak_day, "peak_single_row": peak_single,
            "sum_new_users": nu, "sum_sessions": ss,
            "mean_d1": round(statistics.fmean(d1), 4) if d1 else None,
            "min_d1": min(d1) if d1 else None, "max_d1": max(d1) if d1 else None,
        }

    elif name == "REVENUE_DAILY":
        combo = [r for r in rows if r.get("game_id") == "combo_fighter"]
        iap = sum(r.get("iap_revenue_usd") or 0 for r in combo)
        ad = sum(r.get("ad_revenue_usd") or 0 for r in combo)
        tot = sum(r.get("total_revenue_usd") or 0 for r in combo)
        pu = sum(r.get("paying_users") or 0 for r in combo)
        out["REVENUE_DAILY"] = {"nrows": len(combo), "iap": iap, "ad": ad,
                                "total": tot, "paying_users": pu}

    elif name == "REVENUE_DAILY_V2":
        # V2 may key by title_id
        combo = [r for r in rows if r.get("game_id") == "combo_fighter"
                 or r.get("title_id") == "combo_fighter"]
        out["REVENUE_DAILY_V2"] = {"total_rows": len(rows), "combo_rows": len(combo)}

    elif name == "AD_SPEND_DAILY":
        combo_life = 0.0
        after = 0.0
        by_game_after = {}
        on_today = {}
        for r in rows:
            g = r.get("game_id"); d = r.get("date"); s = r.get("spend_usd") or 0
            if g == "combo_fighter":
                combo_life += s
            if d and d > "2026-02-09":
                after += s
                by_game_after[g] = by_game_after.get(g, 0) + s
            if d == "2026-02-28":
                on_today[g] = on_today.get(g, 0) + s
        out["AD_SPEND_DAILY"] = {
            "combo_lifetime": round(combo_life, 2),
            "all_after_0209": round(after, 2),
            "by_game_after": {k: round(v, 2) for k, v in sorted(by_game_after.items())},
            "on_2026-02-28": {k: round(v, 2) for k, v in sorted(on_today.items())},
            "today_total": round(sum(on_today.values()), 2),
        }

    elif name == "CASH_BALANCE":
        feb = [r for r in rows if r.get("month_end_date") == "2026-02-28"]
        if feb:
            r = feb[0]
            out["CASH_BALANCE"] = {
                "cash_usd": r.get("cash_usd"),
                "monthly_net_burn": r.get("monthly_net_burn"),
                "runway_months": r.get("runway_months"),
                "headcount": r.get("headcount"),
                "notes": r.get("notes"),
            }

print(json.dumps(out, indent=2, default=str))
print(f"[PEAK RSS MiB] {peak_mib():.2f}")
