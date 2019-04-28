import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

#x2, y = np.genfromtxt('messung1.txt', unpack = True)
x = np.array([30, 35, 38, 40])
y = np.array([98.23989117322564, 115.6763676962003, 125.33926764451247, 133.14363168698804])

def f(x, a, b):
    y = a*x + b
    return y


params, covariance_matrix = curve_fit(f, x, y)
errors = np.sqrt(np.diag(covariance_matrix))
a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])

print('Konstante 1: ', a)
print('Konstante 2: ', b)
print('Rydbergenergie: ', a**2)

plt.plot(x, y, 'rx', markersize='6', label='Messwerte')
#plt.axvline(x=14.15, color='r', linewidth='0.75', ymin=0, ymax=1, label='Stelle des Maximums')
plt.plot(x, f(x, *params), 'b-', label='Ausgleich')
plt.xlabel(r'$Z$')
plt.ylabel(r'$\sqrt{E_K}$ / $\sqrt{\mathrm{eV}}$')
plt.grid()
plt.legend()
plt.show()