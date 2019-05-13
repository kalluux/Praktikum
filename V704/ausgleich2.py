import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

x, t, N = np.genfromtxt('messung2.txt', unpack = True)
dN = N**(0.5)
A0 = 1.02
A1 = N/t
A2 = A1 - A0
A = np.log(A2)
dA1 =  dN/t
dA_up = np.log(A + np.sqrt(dA1**2 + 0.04**2)) - np.log(A)
dA_down = np.log(A) - np.log(A - np.sqrt(dA1**2 + 0.04**2))
#print(A1, '+-', dA1)
#print(A2, '+-', dA)

#
errY60 = np.sqrt(N)
# y = ys/t
# errY = errY60/60

x1, y1, u = np.genfromtxt('messung2.txt', unpack = True)

def f(x1, a, b):
    A = a*x1 + np.log(b)
    return A


params, covariance_matrix = curve_fit(f, x1, A)
errors = np.sqrt(np.diag(covariance_matrix))
a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])

print('Konstante 1: ', a)
print('Konstante 2: ', b)
plt.plot(x, A, 'rx', label=r'Messwerte')
plt.errorbar(x, A, yerr=[dA_down, dA_up], fmt='.', label='Fehlerbalken')
plt.plot(x1, f(x1, *params), 'g-', lw=2, label=r'Ausgleich')
# plt.xticks( [30, 32, 34, 34.839, 35.1, 35.2967, 36, 38, 40],
#             [ r'$30$', r'$32$', r'$34$', r'$\nu_{-}$', r'$\nu_{0}$', r'$\nu_{+}$', r'$36$', r'$38$', r'$40$'])
# plt.yticks( [0.2, 0.4, 0.6, 0.8, 0.8485, 1, 1.2],
#             [r'$0.2$', r'$0.4$', r'$0.6$', r'$0.8$', r'$\frac{1}{\sqrt{2}}$', r'$1$', r'$1.2$'])
plt.xlabel(r'$D$ / m')
plt.ylabel(r'ln($A-A_0$)')
plt.tight_layout()
plt.grid()
plt.legend()
plt.show()
print('errY:', errY60)
print('A1:', A1)
print('FehlerA1:', np.sqrt(N)/t)
print('A:', A2)
#
#Konstante 1:  -51.9+/-1.4
#Konstante 2:  137+/-6
#errY: [127.70277992  72.0624729   62.3217458   76.67463727  84.28523002
#  75.43871685  75.76938696  69.34695379  67.5203673   65.39877675
#  59.81638571]
#A1: [163.08       103.86        77.68        58.79        47.36
#  37.94        28.705       24.045       18.236       14.25666667
#  11.92666667]
#FehlerA1: [1.2770278  1.44124946 1.24643492 0.76674637 0.56190153 0.50292478
# 0.37884693 0.34673477 0.27008147 0.21799592 0.19938795]
#A: [162.06       102.84        76.66        57.77        46.34
#  36.92        27.685       23.025       17.216       13.23666667
#  10.90666667]
#
