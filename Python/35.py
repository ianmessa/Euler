import itertools as itt
import numpy as np

def circSet(num):
    for m in range(0,len(str(num))):
        if (''.join(str(num)[i] for i in [(j+m)%(len(str(num))) for j in range(0,len(str(num)))]))[0]!='0':
            yield int(''.join(str(num)[i] for i in [(j+m)%(len(str(num))) for j in range(0,len(str(num)))]))
def cSet(num):
    return(sorted(set(circSet(num)),reverse=True))

def cGen(ceil):
    pl=np.array([True]*ceil)
    pl[0]=pl[1]=False
    for i in range(2,ceil):
        if pl[i]:
            for j in range(i*i,ceil,i):
                pl[j]=False
    for p in range(ceil-1,0,-1):
        if pl[p]:
            #print(cSet(p))
            for c in cSet(p):
                if not pl[c]:
                    pl[cSet(p)]=False
    for p in range(ceil-1,0,-1):
        if pl[p]:
            yield(p)
#cGen(10000)
print(len(list(cGen(1000000))))