import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

xs, ys = np.genfromtxt('doppel.txt', unpack = True)
x = (xs/100)-0.0005
y = (ys-0.00032)*10**(-6)
l = 635 * 10**(-9)
phi = np.arctan(x)

phi2 = np.linspace(-0.02, 0.02, 1000)
#a = gitterkonstante, b = breite
def f(phi, a0, s, b):
    return a0 * (np.cos((np.pi * s * np.sin(phi))/l))**2 * (l/(np.pi * b * np.sin(phi)))**2 * (np.sin((np.pi * b * np.sin(phi)/l)))**2

i = 0.0000003 * (np.cos((np.pi * 0.0005 * np.sin(phi2))/l))**2 * (l/(np.pi * 0.0001 * np.sin(phi2)))**2 * (np.sin((np.pi * 0.0001 * np.sin(phi2)/l)))**2


params, covariance_matrix = curve_fit(f, phi, y, p0=(0.0000003, 0.0005, 0.0001))
errors = np.sqrt(np.diag(covariance_matrix))

print('Parameter: ', params)


plt.plot(phi, y, 'rx', linewidth=2, label='Messwerte')
#plt.plot(phi2, i, 'b-', label='Theorie')
plt.plot(phi, f(phi, *params), 'g-', label='Regression')
#plt.yticks( [0, 0.0000002, 0.0000004, 0.0000006, 0.0000008, 0.000001, 0.0000012, 0.0000014],
#           [ r'$0$', r'$0.2$', r'$0.4$', r'$0.6$', r'$0.8$', r'$1$', r'$1.2$', r'$1.4$'])
plt.xlabel(r'Winkel / rad')
plt.ylabel(r'Intenstität / µA')
plt.grid()
plt.legend()
plt.savefig('doppelfix.pdf')


#A:  0.2498718+/-0.0000028
#b:  0.1501936+/-0.0000032
a0 = 1.45186141e-06  
a= 2.30593572e-02
b=  9.66345546e-03
c=  2.94201910e-08
d= -1.19291132e-05