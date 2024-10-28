#NOTE MINE
def pSum(ceil):
    sum=0
    a = [True] * ceil                          # Initialize the primality list
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            sum+=i
            for n in range(i*i, ceil, i):
                a[n] = False
    print(sum)

pSum(2000000)