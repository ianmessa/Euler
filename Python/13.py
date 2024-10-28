import os
import numpy as np
na=np.array([int(i.replace('\n','')) for i in open(r'C:\Users\IanJS\Desktop\Computer Language\Euler\13.txt')])
print(na)
print(str(sum(na))[0:10])