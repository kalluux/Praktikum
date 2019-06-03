import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.constants import mu_0
import math


g, b = np.genfromtxt('daten.txt', unpack=True)

c = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

def f(x, a, b):
   return a * x + b

x_plot = np.linspace(0, 17)
plt.gcf().subplots_adjust(bottom=0.18)
for i in range(0, 9, 1):
    plt.plot([0, g[i]], [b[i], 0], 'bx-', linewidth = 0.4)
plt.legend()
plt.grid()
plt.ylabel(r'$b / $mm')
plt.xlabel(r'$g / $mm')
plt.axvline(x=96.5, linewidth=0.3,color = 'r')
plt.axhline(y=99, linewidth=0.3,color = 'r')
plt.axvline(x=0, color='k', linewidth=0.5)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.savefig('plot1.pdf')