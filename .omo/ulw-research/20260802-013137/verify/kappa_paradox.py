"""Phase 3 verification: does the kappa paradox explain a 90%-agreement / kappa-0.23 grid?
Stdlib only. No numpy. Mirrors what the pipeline could ship in Validators/."""
from fractions import Fraction as F

def stats(a, b, c, d):
    """2x2: a=both Pass, b=r1 Pass r2 Fail, c=r1 Fail r2 Pass, d=both Fail."""
    n = a + b + c + d
    po = F(a + d, n)
    p1 = F(a + b, n); q1 = F(a + c, n)          # rater1 / rater2 marginal for "Pass"
    pe = p1 * q1 + (1 - p1) * (1 - q1)          # Cohen expected agreement
    kappa = (po - pe) / (1 - pe) if pe != 1 else None
    pabak = 2 * po - 1
    pi = F(a - d, n)                             # Byrt prevalence index
    bi = F(b - c, n)                             # Byrt bias index
    pi_hat = (p1 + q1) / 2                       # Gwet: avg marginal for the '+' category
    pe_ac1 = 2 * pi_hat * (1 - pi_hat)
    ac1 = (po - pe_ac1) / (1 - pe_ac1) if pe_ac1 != 1 else None
    return dict(n=n, po=po, pe=pe, kappa=kappa, pabak=pabak, pi=pi, bi=bi, ac1=ac1)

def show(label, t):
    s = stats(*t)
    f = lambda x: "n/a" if x is None else f"{float(x):+.3f}"
    print(f"{label:<44} n={s['n']:<4} Po={float(s['po']):.3f}  Pe={float(s['pe']):.3f}  "
          f"kappa={f(s['kappa'])}  AC1={f(s['ac1'])}  PABAK={f(s['pabak'])}  "
          f"PI={f(s['pi'])}  BI={f(s['bi'])}")

print("=" * 150)
print("CLAIM UNDER TEST: '90% raw agreement on a mostly-Fail grid is Cohen's kappa ~0.23'")
print("=" * 150)
# 360 decision cells (60 criteria x 6 runs). Mostly-Fail, 90% agreement, symmetric disagreement.
show("mostly-Fail grid, 90% agree (a=18,b=18,c=18,d=306)", (18, 18, 18, 306))
show("balanced grid,    90% agree (a=162,b=18,c=18,d=162)", (162, 18, 18, 162))
print()
print("=" * 150)
print("PARADOX-1 SWEEP: agreement HELD FIXED at 90%; only the Pass/Fail balance changes.")
print("=" * 150)
N, DIS = 360, 36
for pass_rate in (0.50, 0.40, 0.30, 0.20, 0.10, 0.05, 0.02):
    agree = N - DIS
    a = round(agree * pass_rate); d = agree - a
    b = DIS // 2; c = DIS - b
    s = stats(a, b, c, d)
    prev_major = max(a + d and (a + b + a + c) / (2 * N), 0)
    print(f"  Pass prevalence ~{pass_rate:>5.0%} | Po={float(s['po']):.3f} "
          f"kappa={float(s['kappa']):+.3f}  AC1={float(s['ac1']):+.3f}  "
          f"PABAK={float(s['pabak']):+.3f}  PI={float(s['pi']):+.3f}")
print()
print("=" * 150)
print("REPORTED PIPELINE INSTABILITY: '8.5% and 8.6% of decision cells moved'")
print("=" * 150)
for pct, lbl in ((0.085, "regrade A: 8.5% cells moved"), (0.086, "regrade B: 8.6% cells moved")):
    dis = round(N * pct); agree = N - dis
    a = round(agree * 0.20); d = agree - a          # ~20% Pass => Fail-dominant, as reported
    b = dis // 2; c = dis - b
    s = stats(a, b, c, d)
    print(f"  {lbl:<30} Po={float(s['po']):.3f} kappa={float(s['kappa']):+.3f} "
          f"AC1={float(s['ac1']):+.3f} PABAK={float(s['pabak']):+.3f} PI={float(s['pi']):+.3f}")
print()
print("Landis-Koch band for kappa: <=0.20 poor | 0.21-0.40 fair | 0.41-0.60 moderate |")
print("                            0.61-0.80 substantial | >0.80 almost perfect")
print("Krippendorff alpha band:    >=0.800 firm | 0.667-0.799 tentative | <0.667 discard")
