import itertools as itt
import math as m

#EVENS: PEAKS AT n/2
#ODDS: Peaks symmetrically at ((n-1)/2),((n+1)/2)
def choose(n,r):
    return(m.factorial(n)/(m.factorial(r)*m.factorial(n-r)))

def chooseFl(nRange,fl):
    v=0
    for n in nRange:
        if n%2==0:
            rCeil,sym=n/2,1
        else:
            rCeil,sym=(n-1)/2,2
        r=0
        while (choose(n,r)<fl and r<=rCeil):
            r+=1
        if choose(n,r)>fl:
            v+=2*(rCeil-r)+sym
    print(v)

chooseFl(range(1,101),1000000)