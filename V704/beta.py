import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

t, xs, fx, N = np.genfromtxt('beta.txt', unpack = True)
x = xs*2698/10000000
dN = N**(0.5)
A0 = 635/900
A1 = N/t
A2 = A1 - A0
A = np.log(A2)
dA1 =  dN/t
dA_up = np.log(A + np.sqrt(dA1**2 + 0.04**2)) - np.log(A)
dA_down = np.log(A) - np.log(A - np.sqrt(dA1**2 + 0.04**2))
print(A)
print('A2:', A2)
print(A1, '+-', dA1)
print('A: ', A1, '+-', dA1)
print('A-A_0: ', A2, '+', dA_up, '-', dA_down)
print('R: ', x)

xa = np.array([0.02698, 0.033725, 0.0412794, 0.043168, 0.05396,0.0682594, 0.0911924])
xb = np.array([0.0682594, 0.0911924, 0.1300436])

Aa = np.array([3.28557867, 1.85386448, 1.82041891, 1.24615387, -0.0678031,-3.4180045, -4.80429886])
Ab = np.array([-3.4180045, -4.80429886, -3.11351531])

def f1(xa, a, b):
    Aa = a*xa + b
    return Aa


params, covariance_matrix = curve_fit(f1, xa, Aa)
errors = np.sqrt(np.diag(covariance_matrix))
a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])

print('Konstante 1: ', a)
print('Konstante 2: ', b)

def f2(xb, a2, b2):
    Ab = a2*xb + b2
    return Ab


params2, covariance_matrix2 = curve_fit(f2, xb, Ab)
errors2 = np.sqrt(np.diag(covariance_matrix2))
a2 = ufloat(params2[0], errors2[0])
b2 = ufloat(params2[1], errors2[1])

print('Konstante 3: ', a2)
print('Konstante 4: ', b2)

plt.plot(x, A, 'rx', label=r'Messwerte')
plt.errorbar(x, A, yerr=[dA_down, dA_up], fmt='.', label='Fehlerbalken')
plt.plot(xa, f1(xa, *params), 'g-', lw=2, label=r'Ausgleich Teil 1')
plt.plot(xb, f2(xb, *params2), 'k-', lw=2, label=r'Ausgleich Teil 2')
# plt.xticks( [30, 32, 34, 34.839, 35.1, 35.2967, 36, 38, 40],
#             [ r'$30$', r'$32$', r'$34$', r'$\nu_{-}$', r'$\nu_{0}$', r'$\nu_{+}$', r'$36$', r'$38$', r'$40$'])
# plt.yticks( [0.2, 0.4, 0.6, 0.8, 0.8485, 1, 1.2],
#             [r'$0.2$', r'$0.4$', r'$0.6$', r'$0.8$', r'$\frac{1}{\sqrt{2}}$', r'$1$', r'$1.2$'])
plt.xlabel(r'$R$ / $\frac{\mathrm{g}}{\mathrm{cm}^2}$')
plt.ylabel(r'ln($A-A_0$)')
plt.tight_layout()
plt.grid()
plt.legend()
plt.show()