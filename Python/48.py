def sp(ceil):
    return sum([i**i for i in range(1,ceil+1)])

print(str(sp(1000))[len(str(sp(1000)))-10:])