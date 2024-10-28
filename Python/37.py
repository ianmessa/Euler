import numpy as np

def tSet(num):
    yield(num)
    t=1
    while t<len(str(num)):
        yield(int(str(num)[0+t:len(str(num))]))
        yield(int(str(num)[0:len(str(num))-t]))
        t+=1

def tGen(ceil):
    pl=np.array([True]*ceil)
    pl[0]=pl[1]=False
    for i in range(2,ceil):
        if pl[i]:
            for j in range(i*i,ceil,i):
                pl[j]=False
    for p in range(11,ceil):
        if pl[list(tSet(p))].all():
            yield(p)
    
print(sum(list(tGen(1000000))))