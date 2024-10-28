import math

sum=0
c=5
while sum!=1000:
    for bb in [i for i in range(math.ceil(c**2/2),c**2) if math.sqrt(i)%1==0 if math.sqrt(c**2-i)%1==0]:
        aa=c**2-bb
        a,b=math.sqrt(aa),math.sqrt(bb)
        print(a,b,c,a+b+c)
        if a+b+c==1000:
            print('PROD=%s'%(str(a*b*c)))
            sum=a+b+c
            
    c+=1    