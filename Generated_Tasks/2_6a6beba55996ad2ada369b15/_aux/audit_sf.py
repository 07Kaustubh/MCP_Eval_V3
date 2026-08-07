import sys, json
sys.path.insert(0, '_aux')
from stream_sf import stream_rows, peak_mib
from collections import defaultdict

SPLIT='_aux/Universe_Split/snowflake.snowflake.tables.json'

def rowget(row, cols, key):
    if isinstance(row, dict): return row.get(key)
    if isinstance(row, list):
        try: return row[cols.index(key)]
        except Exception: return None
    return None

# accumulators
res={}
for source, rd in stream_rows(SPLIT):
    if not isinstance(rd, dict): continue
    name=rd.get('name'); cols=rd.get('columns') or []
    rows=rd.get('rows') or []
    colnames=[c if isinstance(c,str) else (c.get('name') if isinstance(c,dict) else c) for c in cols]

    if name=='DAILY_ACTIVE_USERS':
        n=0; dates=set(); new=0.0; sess=0.0; d1=[]; d7=[]; d30=[]; dau_by_date=defaultdict(float)
        for r in rows:
            if rowget(r,colnames,'game_id')!='combo_fighter': continue
            n+=1
            d=rowget(r,colnames,'date'); dates.add(str(d)[:10])
            def g(k):
                v=rowget(r,colnames,k)
                try: return float(v)
                except: return 0.0
            new+=g('new_users'); sess+=g('total_sessions') or g('sessions')
            dau_by_date[str(d)[:10]]+=g('daily_active_users') or g('dau') or g('active_users')
            for k,acc in (('d1_retention_pct',d1),('d7_retention_pct',d7),('d30_retention_pct',d30)):
                v=rowget(r,colnames,k)
                if v is not None:
                    try: acc.append(float(v))
                    except: pass
        peak=max(dau_by_date.values()) if dau_by_date else None
        res['DAU']=dict(rows=n,dates=len(dates),dmin=min(dates) if dates else None,dmax=max(dates) if dates else None,
            new=round(new,2),sessions=round(sess,2),peak_dau=peak,
            d1=round(sum(d1)/len(d1),2) if d1 else None,d7=round(sum(d7)/len(d7),2) if d7 else None,
            d30=round(sum(d30)/len(d30),2) if d30 else None,
            d1min=round(min(d1),2) if d1 else None,d1max=round(max(d1),2) if d1 else None,
            peak_by=[k for k,v in dau_by_date.items() if v==peak])

    elif name=='REVENUE_DAILY':
        n=0; tot=0.0; iap=0.0; ad=0.0; pay=0.0
        for r in rows:
            if rowget(r,colnames,'game_id')!='combo_fighter': continue
            n+=1
            for k,acc in (('total_revenue_usd','t'),):
                pass
            def g(k):
                v=rowget(r,colnames,k)
                try: return float(v)
                except: return 0.0
            tot+=g('total_revenue_usd'); iap+=g('iap_revenue_usd'); ad+=g('ad_revenue_usd'); pay+=g('paying_users')
        res['REVENUE_DAILY']=dict(rows=n,total=round(tot,2),iap=round(iap,2),ad=round(ad,2),paying=round(pay,2))

    elif name=='IAP_TRANSACTIONS':
        n=sum(1 for r in rows if rowget(r,colnames,'game_id')=='combo_fighter')
        res['IAP']=dict(combo_rows=n,total_rows=len(rows))

    elif name=='REVENUE_DAILY_V2':
        n=len(rows); combo=sum(1 for r in rows if rowget(r,colnames,'game_id')=='combo_fighter')
        games=set(str(rowget(r,colnames,'game_id')) for r in rows)
        res['REVENUE_DAILY_V2']=dict(rows=n,combo=combo,games=sorted(games)[:6])

    elif name=='UA_SPEND_UNIFIED_V2':
        n=len(rows); combo=sum(1 for r in rows if rowget(r,colnames,'game_id')=='combo_fighter')
        games=set(str(rowget(r,colnames,'game_id')) for r in rows)
        res['UA_SPEND_UNIFIED_V2']=dict(rows=n,combo=combo,games=sorted(games)[:6])

    elif name=='AD_SPEND_DAILY':
        # combo lifetime
        combo_n=0; combo_spend=0.0; combo_inst=0.0; combo_impr=0.0; combo_clk=0.0
        chan=defaultdict(float); combo_dates=set()
        # post 02-09 (strict) all games
        post_n=0; post_tot=0.0; post_by_game=defaultdict(float); post_dates=set()
        # 02-28 all games
        d28_n=0; d28_tot=0.0; d28_combo=0.0
        # inclusive >=02-09 all games
        incl_tot=0.0
        maxdate=None
        for r in rows:
            g=rowget(r,colnames,'game_id')
            d=str(rowget(r,colnames,'date'))[:10]
            def num(k):
                v=rowget(r,colnames,k)
                try: return float(v)
                except: return 0.0
            spend=num('spend_usd')
            if maxdate is None or d>maxdate: maxdate=d
            if g=='combo_fighter':
                combo_n+=1; combo_spend+=spend; combo_inst+=num('installs') or num('attributed_installs')
                combo_impr+=num('impressions'); combo_clk+=num('clicks'); combo_dates.add(d)
                ch=rowget(r,colnames,'channel'); chan[ch]+=spend
            if d>'2026-02-09':
                post_n+=1; post_tot+=spend; post_by_game[g]+=spend; post_dates.add(d)
            if d>='2026-02-09':
                incl_tot+=spend
            if d=='2026-02-28':
                d28_n+=1; d28_tot+=spend
                if g=='combo_fighter': d28_combo+=spend
        res['AD_combo']=dict(rows=combo_n,spend=round(combo_spend,2),installs=round(combo_inst,2),
            impr=round(combo_impr,2),clicks=round(combo_clk,2),dmin=min(combo_dates) if combo_dates else None,
            dmax=max(combo_dates) if combo_dates else None, ndates=len(combo_dates),
            channels={str(k):round(v,2) for k,v in sorted(chan.items(), key=lambda x:-x[1])})
        res['AD_post0209_strict']=dict(rows=post_n,total=round(post_tot,2),ndays=len(post_dates),
            by_game={str(k):round(v,2) for k,v in post_by_game.items()})
        res['AD_incl0209']=round(incl_tot,2)
        res['AD_0228']=dict(rows=d28_n,total=round(d28_tot,2),combo=round(d28_combo,2),maxdate=maxdate)

    elif name=='CASH_BALANCE':
        for r in rows:
            d=str(rowget(r,colnames,'month_end_date'))[:10]
            if d=='2026-02-28':
                res['CASH']=dict(cash=rowget(r,colnames,'cash_usd'),net_burn=rowget(r,colnames,'monthly_net_burn'),
                    runway=rowget(r,colnames,'runway_months'),headcount=rowget(r,colnames,'headcount'),
                    notes=rowget(r,colnames,'notes'))

    elif name=='MONTHLY_BURN':
        feb=defaultdict(float); feb_tot=0.0
        for r in rows:
            d=str(rowget(r,colnames,'month') or rowget(r,colnames,'month_date') or rowget(r,colnames,'date'))[:10]
            if d.startswith('2026-02'):
                cat=rowget(r,colnames,'category') or rowget(r,colnames,'expense_category')
                v=rowget(r,colnames,'amount_usd') or rowget(r,colnames,'amount') or 0
                try: v=float(v)
                except: v=0.0
                feb[str(cat)]+=v; feb_tot+=v
        if feb:
            res['MONTHLY_BURN_feb']=dict(total=round(feb_tot,2),cats={k:round(v,2) for k,v in feb.items()})

print(json.dumps(res, indent=1, default=str))
print("PEAK_MiB", round(peak_mib(),1), file=sys.stderr)
