import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.constants import mu_0
import math


f, U = np.genfromtxt('spannung.txt', unpack=True)
V = U/100
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(f, V, 'r.', label='Messwerte $U_B=200$V', Markersize=4)
plt.grid()
#plt.xlim((-0.1, 1.8))
plt.xlabel(r'$\nu/$kHz')
plt.ylabel(r'$\frac{U_A}{U_E}$')
plt.axvline(35.1, color='black', linestyle=':')
plt.axhline(0.714, color='blue', linestyle=':')
plt.axhline(0.714, color='blue', linestyle=':')
plt.axvline(34.94, color='blue', linestyle=':')
plt.axvline(35.3, color='blue', linestyle=':')
plt.savefig('plot1.pdf')

Q = 35.1/(35.3-34.94)
print(Q)


