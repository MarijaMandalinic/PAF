import numpy as np
import matplotlib.pyplot as plt
import math 

class Particle: #pocetna brzina, kut otklona, pocetni polozaj
    def __init__(self, V0, alfa, x, y, dt=0.01):
        self.x0 = x
        self.y0 = y
        self.dt = dt
        self.alfa = math.radians(alfa)
        self.x = x
        self.y = y
        self.V0 = V0
        self.V0x = self.V0*np.cos(self.alfa)
        self.V0y = self.V0*np.sin(self.alfa)
        self.xx=[]
        self.yy=[]

    def reset(self):
        self.V0 = 0
        self.alfa = 0
        self.x = 0

    def __move(self):
        self.y = self.y + self.V0y*self.dt
        self.x = self.x + self.V0x*self.dt
        self.V0y = self.V0y + (-9.81)*self.dt

    def range(self):
        while self.y >= 0:
            self.__move()
            self.xx.append(self.x)
            self.yy.append(self.y)
        return self.x
    
    def plot_trajectory(self):
        self.range()
        plt.plot(self.xx, self.yy)
        plt.title("putanja")
        plt.xlabel("$x[m]$")
        plt.ylabel("$y[m]$")
        plt.grid(linestyle='--')
        plt.show()

    def analiticki(self):
        self.domet = self.V0*np.cos(self.alfa)*((self.V0*np.sin(self.alfa)+np.sqrt((self.V0*np.sin(self.alfa))**2+2*9.81*self.y0))/9.81) + self.x0
        return self.domet
        
    




