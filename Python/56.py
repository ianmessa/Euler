#For a,b<100, what is the maximum digital sum?
#Probably an odd power
#
max=0
for d in range(100,0,-1):
    for p in range(99,10,-2):
        s=(sum([int(d) for d in str(d**p)]))
        if s>max:
            max=s
print(max)