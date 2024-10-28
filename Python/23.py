import math
import itertools as itt
import numpy as np
def div(n):
    for k in range(1,math.ceil(n**(1/2))):
        if n%k==0:
            if k!=n:
                yield(k)
            if n%(n/k)==0 and n/k!=n and n/k!=k:
                yield(n/k)
    if int(n**(1/2))==n**(1/2):
        yield(n**(1/2))

def abnd(c,r=False):
    if r==True:
        ranger=range(c+1,1,-1)
    else:
        ranger=range(1,c+1)
    for n in ranger:
        if n<sum(div(n)):
            yield(n)

asl=(set([sum(i) for i in itt.product(abnd(28124),abnd(28124))]))

print(sum([i for i in range(28124) if i not in asl]))
