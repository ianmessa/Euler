import numpy as np
flerm=np.arange(1,26).reshape(5,5)
norm=np.arange(1,26)

def sqSpi(inArr):
    A=inArr
    out=[]
    while A.size!=0:
        out.append(A[0][::-1])
        A=A[1:][::-1].T
    return(np.concatenate(out))

def sqSpiSum(inArr,dim):
    A=np.array((inArr)[::-1])
    corners=[]
    index=0
    interval=dim-1
    counter=0

    corners.append(A[index])
    while 1 not in corners:
        index+=interval
        corners.append(A[index])
        counter+=1
        if counter==4:
            counter=0
            interval-=2
    print(corners)
    print(sum(corners))
        

sqSpiSum(np.arange(1,1002002),1001)