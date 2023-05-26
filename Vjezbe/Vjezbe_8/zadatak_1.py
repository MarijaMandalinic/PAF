import em_polje as em
import numpy as np
import matplotlib.pyplot as plt

#elektron

e1 = em.em_polje(20, 1, -1, np.array((0,0,0)), np.array((0,0,1)), np.array((0.1,0.1,0.1)), 0.01)  #t,  m, q, e, b, v, dt
e1.gibanje()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(e1.listax, e1.listay, e1.listaz, label= "elektron")

#pozitron

e2 = em.em_polje(20, 1, 1, np.array((0,0,0)), np.array((0,0,1)), np.array((0.1,0.1,0.1)), 0.01) 
e2.gibanje()
ax.plot(e2.listax, e2.listay, e2.listaz, label = "proton")

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Putanja nabijene čestice')
leg = plt.legend(loc='upper right')
plt.show()