import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

x, t, N = np.genfromtxt('messung1.txt', unpack = True)
dN = N**(0.5)
A0 = 1.02
A1 = N/t
A2 = A1 - A0
A = np.log(A2)
dA1 =  dN/t
dA_up = np.log(A + np.sqrt(dA1**2 + 0.04**2)) - np.log(A)
dA_down = np.log(A) - np.log(A - np.sqrt(dA1**2 + 0.04**2))
#print(A1, '+-', dA1)
#print(A, '+-', dA)

#
errY60 = np.sqrt(N)
# y = ys/t
errY = errY60/60
#
x1, y1, u = np.genfromtxt('messung1.txt', unpack = True)

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
plt.errorbar(x, A, yerr=[dA_down, dA_up],  fmt='.', label='Fehlerbalken')
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
#Konstante 1:  -108.7+/-2.1
#Konstante 2:  133+/-8
#errY: [127.70277992  61.00819617  65.7267069   62.20932406  54.99090834
# 48.82622246  42.59107888  39.54743987  37.88139385  30.69201851
# 29.20616373]
#A1: [163.08        74.44        43.2         25.8         15.12
#   9.536        6.04666667   3.91         2.87         1.884
#   1.706     ]
#FehlerA1: [1.2770278  1.22016392 0.65726707 0.41472883 0.27495454 0.19530489
# 0.14197026 0.0988686  0.07576279 0.06138404 0.05841233]
#A: [162.06        73.42        42.18        24.78        14.1
#   8.516        5.02666667   2.89         1.85         0.864
#   0.686     ]
