import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

xs1, ys1 = np.genfromtxt('einzel1.txt', unpack = True)
x1 = xs1/1000
y1 = (ys1-0.00032)*10**(-6)
l = 635 * 10**(-9)

phi2 = np.linspace(-0.02, 0.02, 1000)
params = [3.40192987e-07, 4.50069313e-04, 7.26999476e-05, 2.42158314e-04]
i = params[0] * (np.cos((np.pi * params[1] * np.sin(phi2-params[3]))/l))**2 * (l/(np.pi * params[2] * np.sin(phi2-params[3])))**2 * (np.sin((np.pi * params[2] * np.sin(phi2-params[3])/l)))**2

plt.plot(0.5*phi2-0.00012, 1.6*i, 'r-', label='Skalierter Doppelspalt')

def f1(x, a, b):
    s = (l/(np.pi*b*np.sin(x)))**2
    s2 = np.sin((np.pi*b*np.sin(x))/l)
    y = a**2 * b**2 * s * s2**2
    return y

params1, covariance_matrix1 = curve_fit(f1, x1, y1, p0=(6, 0.00015))
c = np.linspace(x1[0], x1[64], 1000)
plt.plot(c, f1(c, *params1), 'b-', label='Einzelspalt 1')

plt.xlabel(r'Winkel / rad')
plt.ylabel(r'Intenstität / µA')
plt.grid()
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('vergleich.pdf')