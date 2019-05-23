import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

xs, ys = np.genfromtxt('doppel.txt', unpack = True)
x = xs/1000
y = (ys-0.00032)*10**(-6)
l = 635 * 10**(-9)


#a = gitterkonstante, b = breite
def f(x, a, b, c, d):
    r  = np.cos((np.pi*a*np.sin(x+d))/l)
    t = l/(np.pi*b*np.sin(x+d))
    s = np.sin((np.pi*b*np.sin(x+d))/l)
    y = 4 * r**2 * t**2 * s**2
    return y


params, covariance_matrix = curve_fit(f, x, y, p0=(0.275, 0.00005, 0.0001, 0, 0))
errors = np.sqrt(np.diag(covariance_matrix))
a0 = ufloat(params[0], errors[0])
a = ufloat(params[1], errors[1])
b = ufloat(params[2], errors[2])

print('a0: ', a0)
print('A: ', a)
print('b: ', b)

plt.plot(x, y, 'rx', label='Messwerte')
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
