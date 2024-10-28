vals=[1,2,5,10,20,50,100,200]

l=[0]*201 #Generate a list of possible combinations for every value between zero and our target.
l[0]=1 #We can make zero one way. 
for val in vals: 
    for i in range(val,201): #Every value above (and inclusive of) the one we want will change
        l[i]+=l[i-val] #Take the number of combinations we have using for a certain value, v, using denominations<v. 
                        #Subtract v. We add the number of ways we can make the remainder.
for val in vals:
    print(l[val])


