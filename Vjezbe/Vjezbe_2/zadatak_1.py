import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje_xos(F,m): #sila, masa u kg
    t=np.linspace(0,10,50)
    v=np.linspace(0,10,50)
    x=np.linspace(0,10,50)
    a=[F/m]

    for i in range(1,len(t)):
        a.append(F/m)
        v[i]=v[i-1] + a[i]*(t[i]-t[i-1])
        x[i]=x[i-1] + v[i]*(t[i]-t[i-1])

    #x-t graf
    plt.subplot(1,3,1) #1 red, 3 stupca, na 1.mjestu
    plt.plot(t,x)
    plt.title("x-t graf")
    plt.xlabel("$t[s]$")
    plt.ylabel("$x[m]$")

    #v-t graf
    plt.subplot(1,3,2) 
    plt.plot(t,v)
    plt.title("v-t graf")
    plt.xlabel("$t[s]$")
    plt.ylabel("$v[m/s]$")

    #a-t graf
    plt.subplot(1,3,3) 
    plt.plot(t,a)
    plt.title("a-t graf")
    plt.xlabel("$t[s]$")
    plt.ylabel("$a[ms^{-2}$]")

    plt.show()


jednoliko_gibanje_xos(15,50)
