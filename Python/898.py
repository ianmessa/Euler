import itertools as itt
import functools as ft
import numpy as np
from matplotlib import pyplot as plt
def chance(percList):
    truthList=[[round(perc*100,1),round(100-perc*100,1)] for perc in percList]
    print(truthList)
    permIt=list(itt.product(*truthList))
    print(permIt)
    probList=sorted([ft.reduce(lambda x,y:x*y, perm) for perm in permIt])[::-1]
    print(probList)
    
def chance2(percList):
    
#chance(np.arange(0.25,0.76,0.01))
#chance([0.2,0.4,0.6,0.8])
chance2([0.2,0.4,0.6,0.8])