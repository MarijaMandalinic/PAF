import matplotlib.pyplot as plt
import numpy as np
def funkcija(x1,y1,x2,y2, ime, a): #fja za pravac kroz 2 tocke, ime pod kojim ce se spremiti, a=1 prikaz na ekranu, 2 za pdf
    k=(y2-y1)/(x2-x1)
    l=-x1*k+y1
    x=np.linspace(0,9,10)
    y=k*x+l
    print(x,y)
    print("y={}x+{}".format(k,l))
    plt.plot(y)
    plt.scatter([x1], [y1], color="red", zorder=5) #tocka1 na grafu
    plt.scatter([x2], [y2], color="red", zorder=5) #tocka2
    if a==1:
        plt.show()
    else:
        plt.savefig(ime+".pdf", format='pdf')
funkcija(2,6,4,5, "slika", 0)