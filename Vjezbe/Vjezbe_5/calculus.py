import numpy as np
import matplotlib.pyplot as plt

class Calculus():

    def __init__(self, dx=0.1):
        self.dx = dx
        self.listax = []
        self.listaxi = []
        self.der = []
        self.gornja_meda = 0
        self.donja_meda = 0
        self.donja_integral = 0
        self.gornja_integral = 0
        
    def two_step(self, f, x):
        df = (f(x+self.dx)-f(x))/(self.dx)
        return df
    
    def three_step(self, f, x):
        df = (f(x+self.dx)-f(x-self.dx))/(2*self.dx)
        return df

    def raspon(self, f, gornja, donja, metoda="three-step"): 
        x = donja

        while x >= donja and x < gornja:

            if metoda == "three-step":
                self.d = self.three_step(f, x)
            else:
                self.d = self.two_step(f, x)

            self.der.append(self.d)
            self.listax.append(x)
            x += 0.05

        print(self.der)
        print(self.listax)

    def pravokutna(self, f, p1, p2, br):
        x = np.linspace(p1, p2, br)
        for i in range(len(x)-1):
            self.gornja_meda += f(x[i+1])*(x[i+1]-x[i])
            self.donja_meda += f(x[i])*(x[i+1]-x[i])
        return [self.gornja_meda, self.donja_meda]

    def trapezna(self, f, p1, p2, br):
        self.donja_integral = p1
        self.gornja_integral = p2
        x = np.linspace(p1, p2, br)
        x1 = x[1:-1]
        d = x[2]-x[1]
        self.integral = 0
        for i in range(len(x1)):
            self.integral += f(x1[i])
        self.integral = d*(self.integral + (f(p1)+f(p2))/2)
        return self.integral

