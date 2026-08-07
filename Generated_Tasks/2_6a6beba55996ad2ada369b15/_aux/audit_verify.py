import sys, statistics
sys.path.insert(0, "/home/sumit/Desktop/MCP_Eval_V3/Generated_Tasks/2_6a6beba55996ad2ada369b15/_aux")
from stream_sf import stream_rows, peak_mib

PATH = "/home/sumit/Desktop/MCP_Eval_V3/Generated_Tasks/2_6a6beba55996ad2ada369b15/_aux/Universe_Split/snowflake.snowflake.tables.json"

# accumulators
dau = {"dates": [], "new_users": 0, "sessions": 0, "d1": [], "byday": {}, "rows": 0, "cols": None}
rev = {"total": 0.0, "iap": 0.0, "ad": 0.0, "rows": 0, "cols": None}
revv2_combo = 0
ad_combo = 0.0; ad_combo_rows = 0
ad_after_all = 0.0; ad_after_rows = 0
ad_after_bygame = {}
ad_incl_09 = 0.0
ad_combo_after = 0.0
cash = None

def num(x):
    try: return float(x)
    except: return 0.0

for src, rd in stream_rows(PATH):
    if not isinstance(rd, dict): continue
    name = rd.get("name")
    rows = rd.get("rows")
    if not isinstance(rows, list): continue
    if name == "DAILY_ACTIVE_USERS":
        for r in rows:
            if r.get("game_id") != "combo_fighter": continue
            if dau["cols"] is None: dau["cols"] = sorted(r.keys())
            dau["rows"] += 1
            d = r.get("date")
            dau["dates"].append(d)
            dau["new_users"] += num(r.get("new_users"))
            dau["sessions"] += num(r.get("total_sessions"))
            if r.get("d1_retention_pct") is not None:
                dau["d1"].append(num(r.get("d1_retention_pct")))
            # per-day DAU sum across platform
            dcol = r.get("dau") if r.get("dau") is not None else r.get("daily_active_users")
            dau["byday"][d] = dau["byday"].get(d, 0) + num(dcol)
    elif name == "REVENUE_DAILY":
        for r in rows:
            if r.get("game_id") != "combo_fighter": continue
            if rev["cols"] is None: rev["cols"] = sorted(r.keys())
            rev["rows"] += 1
            rev["total"] += num(r.get("total_revenue_usd"))
            rev["iap"] += num(r.get("iap_revenue_usd"))
            rev["ad"] += num(r.get("ad_revenue_usd"))
    elif name == "REVENUE_DAILY_V2":
        for r in rows:
            gid = r.get("game_id") or r.get("title_id")
            if gid == "combo_fighter": revv2_combo += 1
    elif name == "AD_SPEND_DAILY":
        for r in rows:
            g = r.get("game_id"); d = r.get("date"); s = num(r.get("spend_usd"))
            if g == "combo_fighter":
                ad_combo += s; ad_combo_rows += 1
                if d and d > "2026-02-09": ad_combo_after += s
            if d and d > "2026-02-09":
                ad_after_all += s; ad_after_rows += 1
                ad_after_bygame[g] = ad_after_bygame.get(g, 0.0) + s
            if d and d >= "2026-02-09":
                ad_incl_09 += s
    elif name == "CASH_BALANCE":
        for r in rows:
            if r.get("month_end_date") == "2026-02-28":
                cash = dict(r)

print("=== DAILY_ACTIVE_USERS combo_fighter ===")
print("cols:", dau["cols"])
print("rows:", dau["rows"], "distinct_dates:", len(set(dau["dates"])))
print("date min/max:", min(dau["dates"]), max(dau["dates"]))
print("new_users sum:", dau["new_users"])
print("sessions sum:", dau["sessions"])
print("peak per-day DAU (sum across platform):", max(dau["byday"].values()) if dau["byday"] else "NO dau col")
print("d1 mean (simple):", round(statistics.mean(dau["d1"]),4) if dau["d1"] else "n/a", "n=", len(dau["d1"]))
print("=== REVENUE_DAILY combo ===")
print("cols:", rev["cols"], "rows:", rev["rows"], "total:", rev["total"], "iap:", rev["iap"], "ad:", rev["ad"])
print("REVENUE_DAILY_V2 combo rows:", revv2_combo)
print("=== AD_SPEND_DAILY ===")
print("combo lifetime spend:", round(ad_combo,2), "rows:", ad_combo_rows)
print("all after 2026-02-09:", round(ad_after_all,2), "rows:", ad_after_rows)
print("  by game:", {k: round(v,2) for k,v in ad_after_bygame.items()})
print("combo after 2026-02-09:", round(ad_combo_after,2))
print("incl 2026-02-09 (all):", round(ad_incl_09,2))
print("=== CASH_BALANCE 2026-02-28 ===")
print(cash)
print("=== net proceeds derivation: 22500 - 11700 =", 22500-11700)
print("PEAK RSS MiB:", round(peak_mib(),1))
