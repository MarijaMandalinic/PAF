#a
import numpy as np
from statistics import mean
from statistics import pstdev
def aritmeticka_sredina(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    lista=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
    x=0
    brojnik=0
    for i in range(10):
        x+=lista[i]
    sredina=x/10

    print(sredina)

    for i in range(10):
        brojnik+=(lista[i]-sredina)**2
    devijacija=np.sqrt(brojnik/(10*9))
    print(devijacija)

aritmeticka_sredina(1,2,3,4,5,6,7,8,9,10)

#b
print(mean([1,2,3,4,5,6,7,8,9,10]))
print(pstdev([1,2,3,4,5,6,7,8,9,10])/np.sqrt(9)) #kroz sqrt(n-1)





