import projectile as prj
import matplotlib.pyplot as plt


p1 = prj.Projectile(4,0, 30, 55, 0.6, 0.1, 0.02, 0.01) #m, y, v, fi, ro, cd, A, dt
p1.runge_kutta()
plt.plot(p1.xx, p1.yy, label = "dt = 0.01, Runge-Kutta")
p1 = prj.Projectile(4,0, 30, 55, 0.6, 0.1, 0.02, 0.01) 
p1.plot_trajectory()

leg = plt.legend(loc='upper right')
plt.show()

