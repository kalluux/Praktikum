import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = np.array([0.27, 0.68, 1.08, 1.49, 1.90, 2.31, 2.71, 3.12, 3.53, 3.80])
y = np.array([0.0240, 0.0439, 0.0593, 0.0749, 0.0917, 0.1205, 0.1689, 0.1745, 0.2160, 0.2212])

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
plt.xlabel(r"$B\:/\:10^{-3}\,$T")
plt.ylabel(r"$\frac{1}{T}\:/\:\frac{1}{s}$")
plt.grid()
plt.legend()
#plt.show()
plt.savefig('praezession.pdf')
