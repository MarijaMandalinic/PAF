import numpy as np
import matplotlib.pyplot as plt
import math

def jednoliko_gibanje(F,m,t1): #sila, masa u kg
    t=np.linspace(0,t1,50)
    v=np.linspace(0,t1,50)
    x=np.linspace(0,t1,50)
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
    plt.ylabel("$a[m/s^{-2}$]")

    plt.show()


def kosi_hitac(v0, fi, t1):
    fi=math.radians(fi)
    t=np.linspace(0,t1,50)
    v0x=[v0*np.cos(fi)]
    v0y=np.linspace(0,t1,50)
    a=[-9.81]
    v0y[0]=v0*np.sin(fi)
    x=np.linspace(0,t1,50)
    y=np.linspace(0,t1,50)
    for i in range(1,len(t)):
        a.append(-9.81)
        v0x.append(v0*np.cos(fi))
        v0y[i]=v0y[i-1] + a[i]*(t[i]-t[i-1])
        x[i]=x[i-1] + v0x[i]*(t[i]-t[i-1])
        y[i]=y[i-1] + v0y[i]*(t[i]-t[i-1]) + 1/2*(a[i]*(t[i]-t[i-1])**2)

    plt.subplot(1,3,1) #x-y graf
    plt.plot(x,y)
    plt.title("x-y graf")
    plt.xlabel("$x[m]$")
    plt.ylabel("$y[m]$")

    plt.subplot(1,3,2) #x-t graf
    plt.plot(t,x)
    plt.title("x-t graf")
    plt.xlabel("$t[s]$")
    plt.ylabel("$x[m]$")

    plt.subplot(1,3,3) #y-t graf
    plt.plot(t,y)
    plt.title("y-t graf")
    plt.xlabel("$t[s]$")
    plt.ylabel("$y[m]$")


    
    plt.show()

