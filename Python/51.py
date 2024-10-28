import itertools as itt
import numpy as np
from collections import Counter as counter

def mdpg(ceil):
    l=[True]*(ceil+1)
    l[0]=l[1]=False
    for i in range(2,ceil+1):
        if l[i]==True:
            if any([str(i)[0:len(str(i))-1].count(d)>1 
                    for d in str(i)[0:len(str(i))-1]]):
                yield(i)
            for j in range(i*i,ceil+1,i):
                l[j]=False

mdPrimes=[p for p in mdpg(1000000) if len(str(p))>5]
for p in mdPrimes:
    md=list(set([d for d in str(p) if counter(str(p)[0:len(str(p))-1])[d]>1]))
    for d in md:
        pfam=0
        for rep in range(0,10):
            fm=int(str(p).replace(str(d),str(rep)))
            if fm in mdPrimes:
                pfam+=1
            if (rep+1)-pfam>2:
                break
        if pfam==8:
            print(p,d,pfam,'wahoo')
            break

    