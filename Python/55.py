#Can't I just brute force this?
#Start with 51
import math as m
from time import sleep
def lych(n):
    for i in range(0,50):
        if int(str(n))==int(str(n)[::-1]):
            return(False)
        n+=int(str(n)[::-1])
    return(True)

score=0
for i in range(10000):
    if lych(i):
        score+=1
print(score)