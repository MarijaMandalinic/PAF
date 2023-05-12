import numpy as np
import matplotlib.pyplot as plt
import numpy as np

class HarmonicOscillator():
    
    def __init__(self, x, v, t, m, dt = 0.005):
        self.x0 = x
        self.v0 = v
        self.tk0 = t
        self.x = x
        self.v = v
        self.tk = t
        self.dt = dt
        self.t = [0]
        self.listax = [self.x]
        self.listav = [self.v]
        self.k = 10
        self.m = m
        self.trenutak = 0
        self.a = -(self.k/self.m)*self.x
        self.listaa = [self.a]
    def pomak(self):
        self.v = self.v + self.a*self.dt
        self.x = self.x + self.v*self.dt
        self.a = -(self.k/self.m)*self.x
    def gibanje(self):
        while self.trenutak <= self.tk:
                    self.pomak()
                    self.trenutak += self.dt
                    self.listax.append(self.x)
                    self.listaa.append(self.a)
                    self.listav.append(self.v)
                    self.t.append(self.trenutak)
    
    def plot(self, s):
        self.gibanje()
        self.s = s
        plt.subplot(1,3,1) 
        plt.scatter(self.t, self.listax, s=self.s)
        plt.xlabel('t[s]')
        plt.ylabel('x[m]')
        plt.title('x-t graf')

        plt.subplot(1,3,2) 
        plt.scatter(self.t, self.listav, s = self.s)
        plt.xlabel('t[s]')
        plt.ylabel('v[m/s]')
        plt.title('v-t graf')
        plt.subplot(1,3,3) 
        plt.scatter(self.t, self.listaa, s = self.s, label = "dt = {:.2f}".format(self.dt))
        plt.xlabel('t[s]')
        plt.ylabel('a[$m/2^2$]')
        plt.title('a-t graf')
    
    def period_titranja(self):
        if self.x > 0:
            while self.x >=0:
                 self.pomak()
            self.trenutak = 0
            while self.x < 0:
                 self.pomak()
                 self.trenutak += self.dt
        elif self.x < 0:
            while self.x <0:
                 self.pomak()
                 self.trenutak = 0
            while self.x > 0:
                 self.pomak()
                 self.trenutak += self.dt
        return self.trenutak*2
        
            