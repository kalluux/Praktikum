import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

xs, ys = np.genfromtxt('einzel1.txt', unpack = True)
x = xs/1000
y = (ys-0.00032)*10**(-6)
l = 635 * 10**(-9)

def f(x, a, b):
    s = (l/(np.pi*b*np.sin(x)))**2
    s2 = np.sin((np.pi*b*np.sin(x))/l)
    y = a**2 * b**2 * s * s2**2
    return y


params, covariance_matrix = curve_fit(f, x, y, p0=(6, 0.00015))
errors = np.sqrt(np.diag(covariance_matrix))
a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])

print('A: ', a)
print('b: ', b)


c = np.linspace(x[0], x[64], 1000)
plt.plot(x, y, 'rx', label='Messwerte')
plt.plot(c, f(c, *params), 'b-', label='Regression')
plt.yticks( [0, 0.0000001, 0.0000002, 0.0000003, 0.0000004, 0.0000005, 0.0000006, 0.0000007],
            [r'$0$', r'$0.1$', r'$0.2$', r'$0.3$', r'$0.4$', r'$0.5$', r'$0.6$', r'$0.7$'])
plt.xlabel(r'Winkel / rad')
plt.ylabel(r'Intenstität / µA')
plt.grid()
plt.legend()
#plt.show()
plt.savefig('einzel1.pdf')

#A:  5.14+/-0.11
#b:  0.0001462+/-0.0000035
