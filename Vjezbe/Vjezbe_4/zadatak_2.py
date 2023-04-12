import particle as prt
import numpy as np
import matplotlib.pyplot as plt


dt=0
interval = []
err = []
while dt < 0.10:
    dt += 0.0001
    p1 = prt.Particle(10, 60, 0, 0, dt)
    err.append((abs(p1.analiticki()-p1.range())/p1.analiticki())*100)
    interval.append(dt)


plt.plot(interval, err)
plt.xlabel('dt [s]')
plt.ylabel('Absolute relative error [%]')
plt.title('Absolute relative error for range of projectile')
plt.show()