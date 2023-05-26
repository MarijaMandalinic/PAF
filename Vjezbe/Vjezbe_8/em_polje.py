import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class em_polje():

    def __init__(self,t,  m, q, ex, ey, ez, bx, by, bz, vx, vy, vz, dt): #vrijeme, masa, naboj, komponente e, b, v
        self.t = t
        self.dt = dt
        self.v = np.array((vx, vy, vz))
        self.e = np.array((ex, ey, ez))
        self.b = np.array((bx, by, bz))
        self.x = 0
        self.y = 0
        self.z = 0
        self.m = m
        self.q = q
        self.a = (self.q/self.m)*self.e + (self.q/self.m)*np.cross(self.v, self.b)
        self.listax = [self.x]
        self.listay = [self.y]
        self.listaz = [self.z]
    
    def pomak(self):
        self.v += self.a*self.dt
        self.x += self.v[0]*self.dt
        self.y += self.v[1]*self.dt
        self.z += self.v[2]*self.dt
        self.a = (self.q/self.m)*self.e + (self.q/self.m)*np.cross(self.v, self.b)
    
    def gibanje(self):
        self.trenutak = 0
        while self.trenutak <= self.t:
            self.pomak()
            self.trenutak += self.dt
            self.listax.append(self.x)
            self.listay.append(self.y)
            self.listaz.append(self.z)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(self.listax, self.listay, self.listaz)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        


