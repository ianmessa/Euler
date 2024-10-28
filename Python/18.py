import os
os.chdir(os.path.join(os.getcwd(),'Euler'))

file=open('18.txt')

bottomUp=[[int(j) for j in i.lstrip('      ').replace('\n','').split(' ')] for i in list(reversed(list(file.readlines())))]

sumRow=bottomUp[0]
for i in range(1,15):
    print([max(sumRow[j:j+2])+bottomUp[i][j] for j in range(0,len(bottomUp[i]))])
    sumRow=[max(sumRow[j:j+2])+bottomUp[i][j] for j in range(0,len(bottomUp[i]))]

