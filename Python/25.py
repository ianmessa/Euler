def fib(n):
    x=0
    y=1
    yield(0)
    yield(1)
    for i in range(0,n):
        z=x+y
        yield(z)
        x=y
        y=z

c=-1
for i in fib(50000):
    c+=1
    if len(str(i))>=1000:
        print(c,i)
        break