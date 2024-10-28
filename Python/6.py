def sqSum(len):
    return(sum([i**2 for i in range(1,len+1)]))

def sumSq(len):
    return(sum(list(range(1,len+1)))**2)

def total(len):
    return(sumSq(len)-sqSum(len))

print(total(100))