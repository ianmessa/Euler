def primeList(n):
    k=1
    num=3
    while num<n:
        k+=2
        score=0
        for d in list(range(3,k,2)):
            if k%d==0:
                score+=1
        if score==0:
            num+=1
            print(num,k)
    print('------------')
    print('-------------')         
        


print(primeList(10002))
