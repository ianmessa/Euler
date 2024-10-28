#EVERY INTEGER IS CONGRUENT WITH SUM OF DIGITS MOD 9???
#DIVISIBILITY RULES: 
#Div by 2: Ends in 2
#Div by 3, 9: Sum of digits div by 3
#Div by 4: 
#1: Not biggest
#2: 12 and 21
#3: 3+2+1=6, div by 3
#4: 4+3+2+1 
#5: 5+4+3+2+1=15, div by 3
#6: 15+6=21, div by 3
#7: 21+7=28
#8: 28+8=36, div by 3
#9: 36+9=45, div by 3
import numpy as np
import itertools as itt
import math as m
divTest=lambda n: len([p for p in range(1,m.floor(m.sqrt(n))+1) if n%p==0])==1

max=0

for i in itt.permutations([str(j) for j in range(7,0,-1)]):
    if divTest(int(''.join(i))) and int(''.join(i))>max:
        max=int(''.join(i))
print(max)