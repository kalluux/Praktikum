import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.constants import mu_0
import math

g, b, B = np.genfromtxt('abbe.txt', unpack=True)
G = 28

def f(x, a, b):
   return a * x + b

x_plot = np.linspace(0, 3)
params, covariance_matrix = curve_fit(f, 1+1/(B/G) , g)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(1+1/(B/G), g, 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.xlim((0, 2.2))
plt.ylabel(r'$g / $mm')
plt.xlabel(r'$1+1/V$')
plt.savefig('plot2.pdf')


