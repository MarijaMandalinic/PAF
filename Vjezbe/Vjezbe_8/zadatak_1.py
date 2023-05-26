import em_polje as em
import numpy as np
import matplotlib.pyplot as plt

#elektron

e1 = em.em_polje(20, 1, -1, 0, 0, 0, 0, 0, 1, 0.1, 0.1, 0.1, 0.01)  #t,  m, q, ex, ey, ez, bx, by, bz, vx, vy, vz, dt
e1.gibanje()
plt.title('Putanja nabijene čestice - elektron')
plt.show()

#pozitron

e2 = em.em_polje(20, 1, 1, 0, 0, 0, 0, 0, 1, 0.1, 0.1, 0.1, 0.01)  #t,  m, q, ex, ey, ez, bx, by, bz, vx, vy, vz, dt
e2.gibanje()
plt.title('Putanja nabijene čestice - pozitron')
plt.show()
