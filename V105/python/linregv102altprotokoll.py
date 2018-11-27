import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = np.array([0.00045, 0.000899, 0.00135, 0.0018, 0.00225])
y = np.array([0.0000379, 0.0000612, 0.0000882, 0.0000962, 0.000119])

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
plt.ylabel(r"Ψ")
plt.grid()
plt.legend()
plt.show()
#plt.savefig('linreg.pdf')
