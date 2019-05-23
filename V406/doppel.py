import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

xs, ys = np.genfromtxt('doppel.txt', unpack = True)
x = xs/1000
y = (ys-0.00032)*10**(-6)
l = 635 * 10**(-9)
sin_phi = x / np.sqrt(x**2 + 1)
print(sin_phi)


#a = gitterkonstante, b = breite
def f(sin_phi, a0, a, b, c, d):
    return a0 * 4 * np.cos(np.pi * a * (sin_phi + d) / l)**2 * (l / (np.pi * b * (sin_phi + d)))**2 * (np.sin(np.pi * b * (sin_phi + d) / l))**2 + c


params, covariance_matrix = curve_fit(f, x, y, p0=(250, 0.0001, 0.00005, 0, 0))
errors = np.sqrt(np.diag(covariance_matrix))
a0 = ufloat(params[0], errors[0])
a = ufloat(params[1], errors[1])
b = ufloat(params[2], errors[2])

print('a0: ', a0)
print('A: ', a)
print('b: ', b)

plt.plot(x[51:84], y[51:84], 'rx', label='Messwerte')
plt.plot(x, f(x, *params), 'b-', label='Regression')
#plt.yticks( [0, 0.0000002, 0.0000004, 0.0000006, 0.0000008, 0.000001, 0.0000012, 0.0000014],
#           [ r'$0$', r'$0.2$', r'$0.4$', r'$0.6$', r'$0.8$', r'$1$', r'$1.2$', r'$1.4$'])
plt.xlabel(r'Winkel / rad')
plt.ylabel(r'Intenstität / µA')
plt.grid()
plt.legend()
plt.show()

#A:  0.2498718+/-0.0000028
#b:  0.1501936+/-0.0000032
