#for n*n grid:
    #1 way to do 0
    #1 way to do 1
    #2 ways to do 2
    #2 ways to do n-2
    #1 way to do n-1
    #1 way to do n

def moveNum(n):
    layer1=([0 if list(range(0,n+1)).index(i)==0 else 1 for i in range(0,n+1)])
    layerList=[layer1]
    for i in range(n):
        layer=[1]
        for j in range(1,n+1):
            layer.append(layer[j-1]+layerList[i][j])
        layerList.append(layer)
    print(layerList)

(moveNum(20))