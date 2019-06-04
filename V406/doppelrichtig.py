import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import math

l = 635 * 10**(-9)
phi = np.linspace(-0.008, 0.008, 1000)

i = 4 * (np.cos((np.pi * 0.0005 * np.sin(phi))/l))**2 * (l/(np.pi * 0.0001 * np.sin(phi)))**2 * (np.sin((np.pi * 0.0001 * np.sin(phi)/l)))**2

plt.plot(phi, i, 'r-', label='Theorie')
plt.show()
plt.savefig('theorie.pdf')