import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0,4.01,0.01)
# x = np.arange(1.50,1)
rate=[]
population=[]

def logicmap(xx, rr):
    return xx * rr * (1-xx)

def iterate(xx, rr):
    a=[]
    n = xx
    for i in range(1,20):
        n = logicmap(n,rr)
        rate.append(rr)
        population.append(n)

for i in r: # r changes
    iterate(0.01,i)

plt.scatter(rate,population, s=0.1)
plt.show()
