import particle as prt
import numpy as np
import matplotlib.pyplot as plt

p1 = prt.Particle(60, 55, 5, 70, 0.001)    #brzina, kut, x, y 

print("Domet je {:.2f} m.".format(p1.range()))
print("Analiticko rjesenje je: {:.2f} m.".format(p1.analiticki()))
print("Odstupanje: {:.2f} m.".format(abs(p1.range() - p1.analiticki())))

#numericko rjesenje odstupa od analitickog, odstupanje ovisi o velicini vremenskog intrvala, što je manji odstupanje je manje
#npr za dt=0.01 je odstupanje 0.17 (za v=60, alfa=55, x=5, y=70), a za dt=0.001 je odstupanje 0.03m.

p1.plot_trajectory()