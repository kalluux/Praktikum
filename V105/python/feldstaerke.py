import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = np.array([0.041, 0.049, 0.053, 0.056, 0.061, 0.072, 0.080, 0.089, 0.093, 0.10])
y = np.array([1.74, 2.02, 2.14, 2.17, 2.41, 2.71, 2.97, 3.19, 3.34, 3.58])

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
plt.xlabel(r"$r\:/\:\,$m")
plt.ylabel(r"$B\:/\:10^{-3}\,$T")
plt.grid()
plt.legend()
#plt.show()
plt.savefig('feldstaerke.pdf')
