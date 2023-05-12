import harmonic_oscillator as har
import matplotlib.pyplot as plt
import numpy as np
dt = 0.001
lista = [dt]
lista1 = [2*np.pi/np.sqrt(100)]
while dt <= 0.09:
    dt += 0.001
    lista.append(dt)
    lista1.append(2*np.pi/np.sqrt(100))
    p1 = har.HarmonicOscillator(0.3, 2, 2, 0.1, dt)
    plt.scatter(dt, abs(p1.period_titranja()), s=1)
plt.plot(lista, lista1, linewidth = 1)
plt.xlabel('korak $\Delta$t')
plt.ylabel('period')
plt.title('preciznost metode u ovisnosti o veličini koraka $\Delta$t')
plt.show()