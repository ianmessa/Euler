import numpy as np

def p(ceil):
    a = [True] * ceil
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield(i)
            for n in range(i*i, ceil, i):
                a[n] = False

def repeatCheck(n,d):
    vals=[]
    for i in range(0,1000):
        if np.mod(n*(10**i),d) in vals:
            return(len(vals[vals.index(np.mod(n*(10**i),d)):]))
            break
        else:
            vals.append(np.mod(n*(10**i),d))
max=0
for i in p(1000):
    if repeatCheck(1,i)>max:
        max=i
        print(i,repeatCheck(1,i))
print('--------')
print(max,repeatCheck(1,max))