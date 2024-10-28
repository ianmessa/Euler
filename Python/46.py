import numpy as np
import math as m
import pandas as pd
def pg(ceil):
    l=[True]*(ceil+1)
    l[0]=l[1]=False
    for i in range(2,ceil+1):
        if l[i]==True:
            yield(i)
            for j in range(i*i,ceil+1,i):
                l[j]=False

ceil=10000
compsPd=pd.Series(range(0,ceil+1))
comps=list(compsPd.drop(pg(ceil)).loc[compsPd%2==1])

for i in comps:
   if not any([m.sqrt((i-j)/2)%1==0 for j in pg(i)]):
       print(i)
            