smum=0
for i in range(2,999999):
    if sum([int(j)**5 for j in str(i)])==i:
        smum+=i
print(smum)