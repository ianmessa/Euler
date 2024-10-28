import itertools as itt

def pg(ceil):
    l=[True]*(ceil+1)
    l[0]=l[1]=False
    for i in range(2,ceil+1):
        if l[i]==True:
            yield(i)
            for j in range(i*i,ceil+1,i):
                l[j]=False

s=[i for i in pg(10000) if len(str(i))==4]
dList=[]
for p in s:
    pperms=sorted(set([int(''.join(perm)) for perm in itt.permutations(str(p)) if int(''.join(perm)) in s]))
    if len(pperms)>2 and set(str(p)) not in dList:
        for j in range(0,len(pperms)):
            for i in range(j+1,len(pperms)):
                if 2*pperms[i]-pperms[j] in pperms:
                    print(pperms[j],pperms[i],2*pperms[i]-pperms[j])
        dList.append(set(str(p)))