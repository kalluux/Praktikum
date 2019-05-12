import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

t, xs, fx, N = np.genfromtxt('beta.txt', unpack = True)
A = N/t
plt.plot(xs, A)
plt.savefig('plot1.pdf')