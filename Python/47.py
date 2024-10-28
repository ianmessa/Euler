import math as m
def pf(n):
    factors = set()
    # Check for number of 2s that divide n
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    # n must be odd at this point, so a skip of 2 (i = i + 2) can be used
    for i in range(3, int(m.sqrt(n)) + 1, 2):
        # While i divides n, add i and divide n
        while n % i == 0:
            factors.add(i)
            n //= i
    # This condition is to check if n is a prime number greater than 2
    if n > 2:
        factors.add(n)
    return factors

def cpf(df,ci):
    c=0
    n=2
    while True:
        if len(pf(n))==df:
            c+=1
            if c==ci:
                return([n-x for x in range(ci-1,-1,-1)])
        else:
            c=0
        n+=1
        print(n)
print(cpf(4,4))