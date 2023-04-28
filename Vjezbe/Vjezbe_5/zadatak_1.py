import calculus as calc
import matplotlib.pyplot as plt
import numpy as np
import itertools

colors = itertools.cycle(["r", "b", "g"])

def plot(dx):
    p1 = calc.Calculus(dx)
    p1.three_step(lambda x:np.sin(x), 3)
    p1.raspon(lambda x:5*x**3-2*x**2+2*x-3, 2, -2, "Two-step")  #funkcija, gornja granica, donja granica, zadana three-step metoda (druga opcija "two-step")
    plt.scatter(p1.listax, p1.der,c=next(colors),s=1, label = "$\epsilon$ = {:.2f}".format(dx))

dx=0.01
p1 = calc.Calculus(0.01)
p1.raspon(lambda x:5*x**3-2*x**2+2*x-3, 2, -2, "Two-step")
y=[15*el**2-4*el+2 for el in p1.listax]
plt.plot(p1.listax, y, label = "analiticko rješenje")

while dx<0.5:
    plot(dx)
    dx+=0.1

plt.xlabel('x')
plt.title('Numerical derivation')
leg = plt.legend(loc='upper center')
plt.show()


