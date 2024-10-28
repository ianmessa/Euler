import numpy as np
import string as s
import math as m
import collections as c
ad={i:j for (i,j) in zip(list(s.ascii_lowercase),range(1,27))}
wl=np.array([i.strip('"') for i in open(r'Euler\42.txt').read().split(',')])
tf=lambda str:((m.sqrt(8*(sum([ad[l] for l in str.lower()]))+1)-1)/2)%1==0
print(c.Counter(np.vectorize(tf)(wl)))