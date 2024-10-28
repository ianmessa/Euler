import math as m
import itertools as itt
pTest=lambda n:((1+m.sqrt(1+24*n))/6)%1==0
pList=lambda m,n:[i for i in range(m,n) if pTest(i)]
pDiff=lambda n:[pList(n)[i]-pList(n)[i-1] for i in range(1,len(pList(n)))]

for i,j in [p for p in itt.product(pList(10000,10000000),pList(10000,10000000)) if p[0]>p[1]]:
    if pTest(i+j) and pTest(i-j):
        print(i,j,i-j)