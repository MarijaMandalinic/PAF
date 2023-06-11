import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class em_polje():

    def __init__(self, m, q, v, dt,fbx, fby, fbz, fe, t = 30): #masa, naboj, brzina, dt, fb, fe, t = 30
        self.fbx = fbx
        self.fby = fby
        self.fbz = fbz
        self.fe = fe
        self.trenutak = 0
        self.t = t
        self.dt = dt
        self.v = v
        self.x = 0
        self.y = 0
        self.z = 0
        self.m = m
        self.q = q
        self.a = (self.q/self.m)*np.array((0,0,fe(self.trenutak))) + (self.q/self.m)*np.cross(self.v, np.array((fbx(self.trenutak),fbx(self.trenutak),fbz(self.trenutak))))
        self.listax = [self.x]
        self.listay = [self.y]
        self.listaz = [self.z]

    
    def pomak(self):
        self.v += self.a*self.dt
        self.x += self.v[0]*self.dt
        self.y += self.v[1]*self.dt
        self.z += self.v[2]*self.dt
        self.a = (self.q/self.m)*np.array((0,0,self.fe(self.trenutak))) + (self.q/self.m)*np.cross(self.v, np.array((self.fbx(self.trenutak),self.fbx(self.trenutak),self.fbz(self.trenutak))))
    
    def gibanje(self):
        self.trenutak = 0
        while self.trenutak <= self.t:
            self.pomak()
            self.trenutak += self.dt
            self.listax.append(self.x)
            self.listay.append(self.y)
            self.listaz.append(self.z)