import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

xs1, ys1 = np.genfromtxt('einzel1.txt', unpack = True)
x1 = xs1/1000
y1 = (ys1-0.00032)*10**(-6)
l = 635 * 10**(-9)

xs2, ys2 = np.genfromtxt('doppel.txt', unpack = True)
x2 = xs2/100
y2 = (ys2-0.00032)*10**(-6)
sin_phi = x2 / np.sqrt(x2**2 + 1)
phi = np.arctan(x2)
print(sin_phi)

def f2(sin_phi, a0, a, b, c, d):
    return a0 * 4 * np.cos(np.pi * a * (np.sin(phi + d)) / l)**2 * (l / (np.pi * b * np.sin(phi + d)))**2 * (np.sin(np.pi * b * np.sin(phi + d) / l))**2 + c

params2, covariance_matrix2 = curve_fit(f2, x2, y2, p0=(250, 0.00004, 0.00001, 0, 0))
plt.plot(x2-0.0007, 2 * f2(x2, *params2), 'r-', label='Skalierter Doppelspalt')

def f1(x, a, b):
    s = (l/(np.pi*b*np.sin(x)))**2
    s2 = np.sin((np.pi*b*np.sin(x))/l)
    y = a**2 * b**2 * s * s2**2
    return y

params1, covariance_matrix1 = curve_fit(f1, x1, y1, p0=(6, 0.00015))
c = np.linspace(x1[0], x1[64], 1000)
plt.plot(c, f1(c, *params1), 'b-', label='Einzelspalt')

plt.xlabel(r'Winkel / rad')
plt.ylabel(r'Intenstität / µA')
plt.grid()
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('vergleich.pdf')