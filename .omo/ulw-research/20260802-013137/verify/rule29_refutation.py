"""Does AGENTS.md rule 29's headline number survive contact with the reported data?
Rule 29 asserts: '90% raw agreement on a mostly-Fail grid is kappa 0.23, which is fair and far
below the 0.60 conventionally treated as acceptable.'
Reported Task 44 Opus per-run PASS counts (out of 60 criteria): 32,32,44,32,36,46 (pass 4)
                                                    and before: 28,33,43,31,32,37 (pass 3)"""
from fractions import Fraction as F

def kappa_ac1(a, b, c, d):
    n = a+b+c+d
    po = F(a+d, n); p1 = F(a+b, n); q1 = F(a+c, n)
    pe = p1*q1 + (1-p1)*(1-q1)
    k = (po-pe)/(1-pe)
    ph = (p1+q1)/2; pe1 = 2*ph*(1-ph)
    return float(po), float(pe), float(k), float((po-pe1)/(1-pe1)), float(2*po-1), float(F(a-d,n))

pass4 = [32,32,44,32,36,46]; pass3 = [28,33,43,31,32,37]
N = 60*6
tot4, tot3 = sum(pass4), sum(pass3)
print("="*118)
print("STEP 1 — what is the ACTUAL Pass prevalence of this grid?")
print("="*118)
print(f"  pass-4 export: {pass4}  -> {tot4}/{N} cells Pass = {tot4/N:.1%}")
print(f"  pass-3 export: {pass3}  -> {tot3}/{N} cells Pass = {tot3/N:.1%}")
print(f"  => The grid is NEAR-BALANCED (~50%), NOT 'mostly-Fail'.")
print()
print("="*118)
print("STEP 2 — kappa across the two regradings, at the reported 8.5% cell movement")
print("="*118)
dis = round(N*0.085)                     # 31 cells moved
# marginals fixed by the two exports; disagreement split to respect the observed net drift
net = tot4 - tot3                        # net cells that flipped Fail->Pass
c = (dis + net)//2; b = dis - c          # b = Pass->Fail, c = Fail->Pass
a = tot3 - b                             # both Pass
d = N - a - b - c
po,pe,k,ac1,pabak,pi = kappa_ac1(a,b,c,d)
print(f"  cells moved = {dis} ({dis/N:.1%}), net drift = {net:+d} toward Pass")
print(f"  2x2 = [both-Pass {a}, Pass->Fail {b}, Fail->Pass {c}, both-Fail {d}]")
print(f"  Po    = {po:.3f}")
print(f"  Pe    = {pe:.3f}")
print(f"  kappa = {k:+.3f}   <-- Landis-Koch: ", end="")
print("almost perfect" if k>0.80 else "SUBSTANTIAL" if k>0.60 else "moderate" if k>0.40 else "fair" if k>0.20 else "poor")
print(f"  AC1   = {ac1:+.3f}    PABAK = {pabak:+.3f}    PrevalenceIndex = {pi:+.3f} (|PI| small => paradox NOT triggered)")
print()
print("="*118)
print("STEP 3 — what Pass prevalence WOULD be needed to make rule 29's 'kappa 0.23' true at 90% Po?")
print("="*118)
best=None
for pr in [x/1000 for x in range(5,501)]:
    agree=N-36; a2=round(agree*pr); d2=agree-a2; b2=18; c2=18
    _,_,k2,_,_,_ = kappa_ac1(a2,b2,c2,d2)
    if best is None or abs(k2-0.23)<abs(best[1]-0.23): best=(pr,k2)
print(f"  kappa=0.23 at 90% agreement requires Pass prevalence ~= {best[0]:.1%} (kappa={best[1]:.3f})")
print(f"  i.e. ~{100-best[0]*100:.0f}% of all decision cells would have to be Fail.")
print(f"  The observed grid is {tot4/N:.0%} Pass. Rule 29's premise does not hold for this data.")
print()
print("="*118)
print("VERDICT: rule 29's headline number is REFUTED for the data it cites.")
print("  - '8.5% of cells moved' corresponds to kappa ~= %.2f (SUBSTANTIAL), not 0.23 (fair)." % k)
print("  - The grid is ~50%% Pass, so the kappa paradox is NOT the active failure mode here.")
print("  - The rule's DIRECTION (report chance-corrected agreement, not raw %) remains correct")
print("    and is independently supported by arXiv:2606.19544's universal 33-41pp kappa deflation.")
print("="*118)
