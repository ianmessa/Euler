def primeFactors(n):
    fList=[1]
    for i in [2]+list(range(3,n+1,2)):
        while n%i==0:
            n=n/i
            fList.append(i)
    return(fList)

def smallMult(factors):
    numDict={}
    for f in sorted(factors,reverse=True):
        print(primeFactors(f))
        for subfactor in primeFactors(f):
            if subfactor not in numDict.keys():
                numDict[subfactor]=1
            elif primeFactors(f).count(subfactor)>numDict[subfactor]:
                numDict[subfactor]+=1
    print(numDict)
    sum=1
    for num in numDict.keys():
        print(num**numDict[num])
        sum=sum*(num**numDict[num])
    print(sum)

smallMult(list(range(1,21)))