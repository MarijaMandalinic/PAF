import projectile as prj
import matplotlib.pyplot as plt


p1 = prj.Projectile(4,0, 30, 55, 0.6, 0.1, 0.02, 0.001) 
p1.plot_trajectory()
p1 = prj.Projectile(4,0, 30, 55, 0.6, 0.1, 0.02, 0.01) 
p1.plot_trajectory()
p1 = prj.Projectile(4,0, 30, 55, 0.6, 0.1, 0.02, 0.1) 
p1.plot_trajectory()
p1 = prj.Projectile(4,0, 30, 55, 0.6, 0.1, 0.02, 0.5) 
p1.plot_trajectory()
leg = plt.legend(loc='upper right')
    
plt.show()



