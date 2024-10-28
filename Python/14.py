import os
import numpy as np
import time

def collatz(n):
    sn=n
    yield sn
    while sn!=1:
        if sn%2==0:
            sn=sn/2
        else:
            sn=3*sn+1
        yield(sn)

def collength(n):
    sn=n
    ticker=1
    while sn!=1:
        if sn%2==0:
            sn=sn/2
        else:
            sn=3*sn+1
        ticker+=1
    return(ticker)

start=time.time()
print(max(map(collength,range(1,1000001))))
print(range(1,1000001)[list(map(collength,range(1,1000001))).index(525)])
print(time.time()-start)