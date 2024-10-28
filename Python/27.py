def p(ceil,add0=True,add1=True):
    if add0==True:
        yield(0)
    if add1==True:
        yield(1)
    if ceil>1:
        a = [True] * ceil
        a[0] = a[1] = False
        for (i, isprime) in enumerate(a):
            if isprime:
                yield(i)
                for n in range(i*i, ceil, i):
                    a[n] = False

def primeseq(a,b):
    s=0
    for n in range(0,1000):
        if (n**2+n*a+b) not in p(n**2+n*a+b+1):
            return(s)
            break
        else:
            s+=1

seqMax=0
smProd=0
for i in p(1000):
    for j in p(1000):
        for fp in [(1,1),(-1,-1),(1,-1),(-1,1)]:
            k=fp[0]*i
            l=fp[1]*j
            if primeseq(k,l)>seqMax:
                print(primeseq(k,l),k*l,(k,l))
                seqMax=primeseq(k,l)
                smProd=k*l
print(seqMax)
print(smProd)