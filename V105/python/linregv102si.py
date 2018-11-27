import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = np.array([0.0003996, 0.0004995, 0.0005995, 0.0007993, 0.0009991])
y = np.array([0.000194, 0.0002384, 0.0002904, 0.0004152, 0.0005690])

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
#plt.show()
#plt.savefig('linreg.pdf')
