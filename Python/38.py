#between 918273654 and 987654321
#four digits between 9182 and 9876
#three digits between 918 and 987
import itertools as itt
import collections as c

m=0
for seg in range(4,1,-1):
    for s1 in [''.join(['9']+list(s1l)) for s1l in itt.permutations([str(i) for i in range(1,9)],seg-1) if int(''.join(['9']+list(s1l)))>int('9182'[0:seg])]:
        s2=str(int(s1)*2)
        print(s1,s2)
        if not any(n in s2 for n in s1) and not any(c.Counter(s2)[x]>1 for x in c.Counter(s2).keys()) and '0' not in s2:
            if len(s1+s2)==9 and int(s1+s2)>m:
                m=int(s1+s2)
            else:
                s3=str(int(s2*3))
                if not any(n in s3 for n in s1+s2) and not any(c.Counter(s3)[x]>1 for x in c.Counter(s2).keys()) and '0' not in s3:
                    if len(s1+s2+s3==9) and int(s1+s2+s3)>m:
                        m=int(s1+s2+s3)
print(m)