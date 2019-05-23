import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

xs, ys = np.genfromtxt('einzel2.txt', unpack = True)
x = xs/1000
y = (ys-0.00032)*10**(-6)
l = 635 * 10**(-9)

def f(x, a, b):
    s = (l/(np.pi*b*np.sin(x)))**2
    s2 = np.sin((np.pi*b*np.sin(x))/l)
    y = a**2 * b**2 * s * s2**2
    return y


params, covariance_matrix = curve_fit(f, x, y, p0=(4.7, 0.0004))
errors = np.sqrt(np.diag(covariance_matrix))
a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])

print('A: ', a)
print('b: ', b)



plt.plot(x, y, 'rx', label='Messwerte')
plt.plot(x, f(x, *params), 'b-', label='Regression')
plt.yticks( [0, 0.000001, 0.000002, 0.000003, 0.000004, 0.000005],
            [r'$0$', r'$1$', r'$2$', r'$3$', r'$4$', r'$5$'])
plt.xlabel(r'Winkel / rad')
plt.ylabel(r'Intenstität / µA')
plt.grid()
plt.legend()
plt.show()

#A:  6.40+/-0.09
#b:  0.000338+/-0.000005