import seminar as em
import numpy as np
import matplotlib.pyplot as plt

#elektron

e1 = em.em_polje(1, -1, np.array((0.1,0.1,0.1)), 0.01,lambda x: 0, lambda x: 0, lambda x: (1/10)*x, lambda x: 0*x) 
#masa, naboj, brzina, dt, fb, fe, t = 30
e1.gibanje()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(e1.listax, e1.listay, e1.listaz, linewidth = 0.8,  label = 'elektron u promjenjivom magnetskom polju')

#elektron uvremenski konstantom magnetnom polju

e2 = em.em_polje(1, -1, np.array((0.1,0.1,0.1)), 0.01,lambda x: 0, lambda x: 0,  lambda x: 1, lambda x:0) 
e2.gibanje()
ax.plot(e2.listax, e2.listay, e2.listaz, linewidth = 0.8, label = 'elektron u vremenski konstantom polju')

# pozitron

e3 = em.em_polje(1, 1, np.array((0.1,0.1,0.1)), 0.01,lambda x: 0, lambda x: 0,  lambda x: (1/10)*x, lambda x: 0*x) 
#masa, naboj, brzina, dt, fb, fe, t = 30
e3.gibanje()
ax.plot(e3.listax, e3.listay, e3.listaz, linewidth = 0.8, label = 'pozitron u promjenjivom magnetskom polju')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
leg = plt.legend(loc='upper center')
plt.title('Putanja nabijene čestice')
plt.show()