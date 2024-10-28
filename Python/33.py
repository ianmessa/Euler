from itertools import product
import numpy as np

numList=[]
denList=[]

for pair in product(range(10,100),range(10,100)):
    pair=[str(i) for i in pair]
    if pair[0][1]==pair[1][0] and '0' not in pair[0] and '0' not in pair[1]:
        if int(pair[0][0])/int(pair[1][1])==int(pair[0])/int(pair[1])<1:
            numList.append(int(pair[0]))
            denList.append(int(pair[1]))
print(np.prod((numList)))
print(np.prod(denList))