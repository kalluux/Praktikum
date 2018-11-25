import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = np.array([194.2, 210.5, 230.4, 254.5, 283.3, 320.5, 369, 432.9, 526.3, 672.1])
y = np.array([0.716, 0.75, 0.785, 0.910, 1.010, 1.143, 1.311, 1.568, 1.893, 2.437])

def f(x, a, b):

    y = a*x+b
    return y

params, covariance_matrix = curve_fit(f, x, y)
errors = np.sqrt(np.diag(covariance_matrix))
a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])

print('A Konstante: ', a)
print('B Konstante: ', b)
plt.plot(x, y, 'rx', label='Messwerte')
plt.plot(x, f(x, *params), 'b-', label='lineare Regression')
plt.xlabel(r"$\frac{1}{B}\:/\:\frac{1}{T}$")
plt.ylabel(r"$T^2\:/\:s^2$")
plt.grid()
plt.legend()
#plt.show()
plt.savefig('schwingung.pdf')
