#abcdefghij where:
#   d%2=0
#   (c+d+e)%3=0
#   f=0|5
#   (('ef')-2g)%7=0
#   (f-g+h)%11=0
#   (g*4-('hi'))%13=0
#   (('hi')-5*j)%17)=0
import itertools as itt

rList=list(range(0,10))
summer=0
for d in [n for n in rList if n%2==0]:
    rl1=list(range(0,10))
    pd=[0,0,0,0,0,0,0,0,0,0]
    pd[3]=d
    rl1.remove(d)
    for (c,e) in [nm for nm in itt.product(rl1,rl1) if nm[0]!=nm[1]]:
        rl2=[i for i in rl1]
        if (c+d+e)%3==0:
            pd[2],pd[4]=c,e
            rl2.remove(c)
            rl2.remove(e)
            for f in rl2:
                rl3=[i for i in rl2]
                if f==0 or f==5:
                    pd[5]=f
                    rl3.remove(f)
                    for g in rl3:
                        rl4=[i for i in rl3]
                        if (int(str(e)+str(f))-2*g)%7==0:
                            pd[6]=g
                            rl4.remove(g)
                            for h in rl4:
                                rl5=[i for i in rl4]
                                if (f-g+h)%11==0:
                                    pd[7]=h
                                    rl5.remove(h)
                                    for i in rl5:
                                        rl6=[i for i in rl5]
                                        if (g*4-int(str(h)+str(i)))%13==0:
                                            pd[8]=i
                                            rl6.remove(i)
                                            for j in rl6:
                                                rl7=[i for i in rl6]
                                                if (int(str(h)+str(i))-5*j)%17==0:
                                                    pd[9]=j
                                                    rl7.remove(j)
                                                    for a in rl7:
                                                        rl8=[i for i in rl7]
                                                        rl8.remove(a)
                                                        pd[0],pd[1]=a,rl8[0]
                                                        pdInt=int(''.join([str(i) for i in pd]))
                                                        summer+=pdInt
print(summer)
            #rl.remove(c)
            #rl.remove(e)
            #print(rl)
