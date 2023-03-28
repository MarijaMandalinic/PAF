#graf linearne regersije
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336] #Nm
fi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] #rad
xy=[]
x2=[]
for i in range(len(M)):
    xy.append(M[i]*fi[i])
    x2.append(fi[i]*fi[i])
Df=mean(xy)/mean(x2)
y=[]
for i in range(len(fi)):
    y.append(Df*fi[i])
print(Df)
plt.scatter(fi,M)
plt.plot(fi,y, color="red")
plt.xlabel("$\u03C6[rad]$")
plt.ylabel("$M[Nm]$")
plt.show()