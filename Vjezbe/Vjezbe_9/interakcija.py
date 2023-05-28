import numpy as np

class interakcija():
    def __init__(self, m1, m2, r1,r2, v1, v2, t, dt=60*60*12):
        self.m1 = m1
        self.m2 = m2
        self.v2 = np.asarray(v2, dtype = np.float64)
        self.v1 = np.asarray(v1, dtype = np.float64)
        self.r2 = np.asarray(r2, dtype = np.float64)
        self.r1 = np.asarray(r1, dtype = np.float64)
        self.G = 6.67408*10**(-11) #[Nm^2/kg^2]
        self.t = t
        self.dt = dt
        
        self.a1 = ((-self.G*self.m2*(self.r1-self.r2))/(np.linalg.norm(self.r2-self.r1))**3)
        self.a2 = ((-self.G*self.m1*(self.r2-self.r1))/(np.linalg.norm(self.r1-self.r2))**3)

        self.listax2 = [0]
        self.listay2 = [0]
        self.listax1 = [1.486*10**(11)]
        self.listay1 = [0]


    def pomak(self):
        self.v1 += self.a1*self.dt
        self.r1 += self.v1*self.dt
        self.v2 += self.a2*self.dt
        self.r2 += self.v2*self.dt
        self.a1 = ((-self.G*self.m2*(self.r1-self.r2))/(np.linalg.norm(self.r2-self.r1))**3)
        self.a2 = ((-self.G*self.m1*(self.r2-self.r1))/(np.linalg.norm(self.r1-self.r2))**3)

    def gibanje(self):
        self.trenutak = 0
        while self.trenutak <= self.t:
            self.pomak()
            self.trenutak += self.dt
            self.listax2.append(self.r2[0])
            self.listay2.append(self.r2[1])
            self.listax1.append(self.r1[0])
            self.listay1.append(self.r1[1])
            
        return self.listax1, self.listax2, self.listay1, self.listay2 