import math as m
ceil=m.factorial(9)*7

ranger=[i for i in range(10,ceil) if (
    (len(str(i))==3 and str(k) in str(i) for k in range(5,10)) or 
    (len(str(i))==4 and str(k) in str(i) for k in range(6,10)) or 
    (len(str(i)) in [5,6] and str(k) in str(i) for k in range(7,10)) or
    (len(str(i))==7 and str(k) in str(i) for k in range(6,10)))]

for i in ranger:
    if sum([m.factorial(int(k)) for k in str(i)])==i:
        print(i)

#3 digits: need 5+
#4 digits: need 6+
#5 digits: need 7+
#6 digits: need 7+
#7 digits: need 8+