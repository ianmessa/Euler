def pg(ceil):
    l=[True]*(ceil+1)
    l[0]=l[1]=False
    for i in range(2,ceil+1):
        if l[i]==True:
            yield(i)
            for j in range(i*i,ceil+1,i):
                l[j]=False