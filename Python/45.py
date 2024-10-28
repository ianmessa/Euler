import math as m
tTest=lambda n:(m.sqrt(1+8*n))%2==1
pTest=lambda n:(m.sqrt(1+24*n))%6==5

hVal=lambda n:(1+m.sqrt(1+8*n))/4

def multiGen(flr):
    s=(hVal(flr))+1
    while s>0:
        if pTest(s*(2*s-1)) and tTest(s*(2*s-1)):
            return(s*(2*s-1))
        s+=1
        

print((multiGen(40755)))