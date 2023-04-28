import calculus as calc
import matplotlib.pyplot as plt

pravokut = []
integral = []
br = 0
broj=[]
analiticko = []
f = lambda x: (2/3)*x**3 + 3*x
fi = f(1) - f(0)
while br < 1000:
    br += 50
    broj.append(br)
    p1 = calc.Calculus()
    p1.trapezna(lambda x: 2*x**2+3, 0, 1, br)
    integral.append(p1.integral)
    pravokut.append(p1.pravokutna(lambda x: 2*x**2+3, 0, 1, br))
    analiticko.append(fi)
pravokut_gornja = [x[0] for x in pravokut]
pravokut_donja = [x[1] for x in pravokut]
plt.plot(broj, analiticko, label="analiticko rjesenje")
plt.scatter(broj, pravokut_donja, s=1, label ="donja međa")
plt.scatter(broj, pravokut_gornja, s=1, label = "gornja međa")
plt.scatter(broj, integral,color = "red", s=2, label = "trapezna metoda")
plt.xlabel('N koraka')
plt.ylabel('integral')
plt.title('Numericka integracija')
leg = plt.legend(loc='upper center')
plt.show()