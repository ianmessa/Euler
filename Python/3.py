#The prime factors of 13195 are 5, 7, 13, 29. Largest of 600851475143
def pf(n):
    i=2
    while i*i<n:
        print('i=%s'%i)
        while n%i==0:
            n=n/i
            print('n=%s'%n)
        i=i+1
        print('--------------------')
    print(n)
pf(13195)