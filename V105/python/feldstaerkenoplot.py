import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = np.array([0.041, 0.049, 0.053, 0.056, 0.061, 0.072, 0.080, 0.089, 0.093, 0.10])
y = np.array([0.00174, 0.00202, 0.00214, 0.00217, 0.00241, 0.00271, 0.00297, 0.00319, 0.00334, 0.00358])

def f(x, a, b):

    y = a*x+b
    return y

params, covariance_matrix = curve_fit(f, x, y)
errors = np.sqrt(np.diag(covariance_matrix))
a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])

print('A Konstante: ', a)
print('B Konstante: ', b)
#plt.plot(x, y, 'rx', label='Messwerte')
#plt.plot(x, f(x, *params), 'b-', label='lineare Regression')
#plt.xlabel(r"$r\:/\:\,$m")
#plt.ylabel(r"$B\:/\:10^{-3}\,$T")
#plt.grid()
#plt.legend()
##plt.show()
#plt.savefig('feldstaerke.pdf')
mudipol1 = (0.00138 * 9.81)/a
print('mudipol1: ', mudipol1 )
