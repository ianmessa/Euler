import math

sum=0
for prod in ([i for i in range(0,10000) if len(set(str(i)))==len(str(i)) if '0' not in str(i)]):
    for fact in range(1,math.floor(prod**1/2)):
        if prod%fact==0 and prod%(prod/fact)==0 and '0' not in (str(int(fact))+str(int(prod/fact))):
            if(len(str(int(prod))+str(int(fact))+str(int(prod/fact))))==len(set(str(int(prod))+str(int(fact))+str(int(prod/fact))))==9:
                print(fact,prod/fact,prod)
                sum+=prod
                break

print(sum)