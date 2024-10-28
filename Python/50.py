#1 to 3931
import numpy as np
from pg import pg

def pg(ceil):
    l=[True]*(ceil+1)
    l[0]=l[1]=False
    for i in range(2,ceil+1):
        if l[i]==True:
            yield(i)
            for j in range(i*i,ceil+1,i):
                l[j]=False
pl=list(pg(4500))
tp=list(pg(1000000))
print('lists established')
def sums(lis):
    for l in range(len(lis),0,-1):
        for i in range(0,len(lis)-l+1):
            if sum(lis[i:i+l]) in tp:
                return(sum(lis[i:i+l]),len(lis[i:i+l]))
            
print(sums(pl))