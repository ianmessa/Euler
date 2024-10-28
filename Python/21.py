import math
import pandas as pd
def nDivisor(n):
    for k in range(1,math.ceil(n**(1/2))):
        if n%k==0:
            if k!=n:
                yield(k)
            if n%(n/k)==0 and n/k!=n:
                yield(n/k)

def amicable(ceil):
    some=0
    rnge=pd.Series(range(1,ceil))
    for i in rnge:
        j=sum(list(nDivisor(i)))
        if i==sum(list(nDivisor(j))) and i!=j:
            print(i,j)
            some+=i+j
    print(some/2)

amicable(10000)