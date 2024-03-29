import harmonic_oscillator as har
import matplotlib.pyplot as plt
import numpy as np

p1 = har.HarmonicOscillator(0.3, 2, 2, 0.1, 0.01)
p1.plot(0.5)
p1 = har.HarmonicOscillator(0.3, 2, 2, 0.1, 0.05)
p1.plot(5)
p1 = har.HarmonicOscillator(0.3, 2, 2, 0.1, 0.08)
p1.plot(5)

vrijeme = np.linspace(0, 2, 200)
fi = np.arctan(0.3*np.sqrt(10/0.1)/2)
a = 0.3/(np.sin(fi))
x = [a*np.sin(np.sqrt(10/0.1)*i + fi) for i in vrijeme]
plt.subplot(1,3,1)
plt.plot(vrijeme, x, linewidth = 1)

v = [np.sqrt(10/0.1)*a*np.cos(np.sqrt(10/0.1)*i + fi) for i in vrijeme]
plt.subplot(1,3,2)
plt.plot(vrijeme, v, linewidth = 1)

a = [-(10/0.1)*a*np.sin(np.sqrt(10/0.1)*i + fi) for i in vrijeme]
plt.subplot(1,3,3)
plt.plot(vrijeme, a, linewidth = 1, label = "analiticko")
leg = plt.legend(loc='upper center')
plt.show()




