import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

xs, ys = np.genfromtxt('doppel.txt', unpack = True)
x = xs/100
y = (ys-0.00032)*10**(-6)
l = 635 * 10**(-9)
sin_phi = x / np.sqrt(x**2 + 1)
phi = np.arctan(x)
print(sin_phi)


#a = gitterkonstante, b = breite
def f(sin_phi, a0, a, b, c, d):
    return a0 * 4 * np.cos(np.pi * a * (np.sin(phi + d)) / l)**2 * (l / (np.pi * b * np.sin(phi + d)))**2 * (np.sin(np.pi * b * np.sin(phi + d) / l))**2 + c


#   return a0 * 4 * np.cos(np.pi * a * (sin_phi + d) / l)**2 * (l / (np.pi * b * (sin_phi + d)))**2 * (np.sin(np.pi * b * (sin_phi + d) / l))**2 + c


params, covariance_matrix = curve_fit(f, x, y, p0=(250, 0.00004, 0.00001, 0, 0))
errors = np.sqrt(np.diag(covariance_matrix))
a0 = ufloat(params[0], errors[0])
a = ufloat(params[1], errors[1])
b = ufloat(params[2], errors[2])


#print('a0: ', a0)
#print('A: ', a)
#print('b: ', b)
print('Parameter: ', params)

c = np.linspace(x[0], x[84], 1000)
plt.plot(x, y, 'rx', linestyle=':', linewidth=2, label='Messwerte')
plt.plot(phi, f(phi, *params), 'b-', label='Regression')
#plt.yticks( [0, 0.0000002, 0.0000004, 0.0000006, 0.0000008, 0.000001, 0.0000012, 0.0000014],
#           [ r'$0$', r'$0.2$', r'$0.4$', r'$0.6$', r'$0.8$', r'$1$', r'$1.2$', r'$1.4$'])
plt.xlabel(r'Winkel / rad')
plt.ylabel(r'Intenstität / µA')
plt.grid()
plt.legend()
plt.savefig('doppel.pdf')


#A:  0.2498718+/-0.0000028
#b:  0.1501936+/-0.0000032
a0 = 1.45186141e-06  
a= 2.30593572e-02
b=  9.66345546e-03
c=  2.94201910e-08
d= -1.19291132e-05