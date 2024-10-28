#2x,3x,4x,5x have same digits

#2x,3x,4x,5x,6x must have same digit count
#MAX VALUE: 1/6 of 10mult ceiling (e.g. for two digit numbers, 16)

#For even in 

import pandas as pd
import math as m
import numpy as np

def candidates(d):
    return([i for i in range(10**(d-1),m.ceil((10**d)/6))])
def fam(mf,mc):
    d=4
    elected=0
    while elected==0:
        for n in candidates(d):
            print(n)
            if all([sorted(str(n*mf))==sorted(str(n*j)) for j in range(mf+1,mc+1)]):
                print(n,'YA')
                elected+=1
                break
        d+=1

fam(2,6)
#for c in mult.columns:
#    print(c)
#    colSet=pd.Series([set(str(i)) for i in mult[c]])
#    if colSet.drop_duplicates().shape[0]==1:
#        print(colSet)