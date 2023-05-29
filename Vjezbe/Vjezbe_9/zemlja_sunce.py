import interakcija as inter
import matplotlib.pyplot as plt
import numpy as np

t1 = inter.interakcija(5.9742*10**(24), 1.989*10**(30),np.array((1.486*10**(11), 0)), np.array((0,0)),np.array((0,29783)),np.array((0,0)), 365.242*24*60*60)
t1.gibanje()
#m1, m2, r1,r2, v1, v2, t, dt = 60*60*12
x1, x2, y1, y2 = t1.gibanje()
plt.scatter(x1, y1, s = 0.5, label = 'zemlja')
plt.scatter(x2, y2, c = 'y', s = 10, label = 'sunce')
leg = plt.legend(loc='upper right')
plt.show()