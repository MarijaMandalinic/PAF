import numpy as np
import matplotlib.pyplot as plt
import math

class Projectile():
    def __init__(self,m, y, v, fi, ro, cd, A, dt = 0.01): #cd - koeficijent trenja, A - povrsina, v - brzina, ro - gustoca, fi - kut otklona
        self.m = m
        self.y = y
        self.x = 0
        self.v = v
        self.fi = math.radians(fi)
        self.ro = ro
        self.cd = cd
        self.A = A
        self.t = 0
        self.dt = dt
        ##
        self.vx = np.cos(self.fi)*self.v
        self.vy = np.sin(self.fi)*self.v
        self.ax = -np.sign(self.vx)*(self.ro*self.cd*self.A/(2*self.m))*(self.vx)**2
        self.ay = - 9.81 -np.sign(self.vy)*(self.ro*self.cd*self.A/(2*self.m))*(self.vy)**2
        ##
        self.listax = [self.x]
        self.listay = [self.y]
        self.listavx = [self.vx]
        self.listavy = [self.vy]
        self.listaax = [self.ax]
        self.listaay = [self.ay]
        self.listat = [self.t]

        ##
        self.x0 = 0
        self.y0 = y
        self.vx0 = np.cos(self.fi)*self.v
        self.vy0 = np.sin(self.fi)*self.v
        self.ax0 = -np.sign(self.vx)*(self.ro*self.cd*self.A/(2*self.m))*(self.vx)**2
        self.ay0 = - 9.81 -np.sign(self.vy)*(self.ro*self.cd*self.A/(2*self.m))*(self.vy)**2
    
    def reset(self):
        self.x = 0
        self.y = self.y0
        self.vx = self.vx0
        self.vy = self.vy0

    def pomak(self):
        #y smjer
        self.vy += self.ay*self.dt
        self.y += self.vy*self.dt
        self.ay = - 9.81 -np.sign(self.vy)*(self.ro*self.cd*self.A/(2*self.m))*(self.vy)**2

        #x smjer
        self.vx += self.ax*self.dt
        self.x += self.vx*self.dt
        self.ax = -np.sign(self.vx)*(self.ro*self.cd*self.A/(2*self.m))*(self.vx)**2
    
    def gibanje(self):
        while self.y >= 0:
            self.pomak()
            self.t += self.dt
            self.listat.append(self.t)
            self.listax.append(self.x)
            self.listay.append(self.y)
            self.listavx.append(self.vx)
            self.listavy.append(self.vy)
            self.listaax.append(self.ax)
            self.listaay.append(self.ay)
    
    def plot_trajectory(self):
        self.gibanje()
        plt.plot(self.listax, self.listay, linewidth = 1, label = "dt = {:.3f}, Euler".format(self.dt))
        plt.xlabel('x[m]')
        plt.ylabel('y[m]')
        plt.title('x-y graf')
    def runge_kutta(self):
        self.xx=[0]
        self.yy=[self.y]
        self.reset()
        self.dt = 0.01
        while self.y >=0:
            self.k1vx = -np.sign(self.vx)*(self.ro*self.cd*self.A/(2*self.m))*(self.vx)**2*self.dt
            self.k1x = self.vx*self.dt
            self.k2vx = -np.sign(self.vx+self.k1vx/2)*(self.ro*self.cd*self.A/(2*self.m))*(self.vx+self.k1vx/2)**2*self.dt
            self.k2x = (self.vx+self.k1vx/2)*self.dt
            self.k3vx = -np.sign(self.vx+self.k2vx/2)*(self.ro*self.cd*self.A/(2*self.m))*(self.vx+self.k2vx/2)**2*self.dt
            self.k3x = (self.vx+self.k2vx/2)*self.dt
            self.k4vx = -np.sign(self.vx+self.k3vx/2)*(self.ro*self.cd*self.A/(2*self.m))*(self.vx+self.k3vx/2)**2*self.dt
            self.k4x = (self.vx+self.k3vx/2)*self.dt
            self.vx += 1/6*(self.k1vx + 2*self.k2vx + 2*self.k3vx + self.k4vx)
            self.x += 1/6*(self.k1x + 2*self.k2x + 2*self.k3x + self.k4x)
            
            self.k1vy =(-9.81 -np.sign(self.vy)*(self.ro*self.cd*self.A/(2*self.m))*(self.vy)**2)*self.dt
            self.k1y = self.vy*self.dt
            self.k2vy = (-9.81 -np.sign(self.vy+self.k1vy/2)*(self.ro*self.cd*self.A/(2*self.m))*(self.vy+self.k1vy/2)**2)*self.dt
            self.k2y = (self.vy+self.k1vy/2)*self.dt
            self.k3vy = (-9.81 -np.sign(self.vy+self.k2vy/2)*(self.ro*self.cd*self.A/(2*self.m))*(self.vy+self.k2vy/2)**2)*self.dt
            self.k3y = (self.vy+self.k2vy/2)*self.dt
            self.k4vy = (-9.81 -np.sign(self.vy+self.k3vy/2)*(self.ro*self.cd*self.A/(2*self.m))*(self.vy+self.k3vy/2)**2)*self.dt
            self.k4y = (self.vy+self.k3vy/2)*self.dt
            self.vy += 1/6*(self.k1vy + 2*self.k2vy + 2*self.k3vy + self.k4vy)
            self.y += 1/6*(self.k1y + 2*self.k2y + 2*self.k3y + self.k4y)

            self.xx.append(self.x)
            self.yy.append(self.y)
        
