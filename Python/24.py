import numpy as np
import math

vals=[0,1,2,3,4,5,6,7,8,9]
inp=1000000
c=0
num=[]

k=inp-1
for i in range(len(vals)):
    perms=math.factorial(len(vals))
    ind=math.floor(len(vals)*(k/perms))
    num.append(vals[ind])
    k-=perms*(ind/len(vals))
    vals=[i for i in vals if i not in num]

print(num)