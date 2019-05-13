import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import unumpy

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

#
errY60 = np.sqrt(N)
# y = ys/t
errY = errY60/60
#

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
print('errY:', errY60)
print('A1:', A1)
print('FehlerA1:', np.sqrt(N)/t)
print('A:', A2)

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
print(unumpy.exp(b), unumpy.exp(b2), unumpy.exp(-b2))

rmax = (b-b2)/(a2-a)
emax = 1.92 * unumpy.sqrt(rmax**2 + 0.22*rmax)
print(rmax)
print(emax)

#[ 3.28557867  1.85386448  1.82041891  1.24615387 -0.0678031  -3.4180045
#         nan -4.80429886         nan         nan -3.11351531]
#A2: [ 2.67244444e+01  6.38444444e+00  6.17444444e+00  3.47694444e+00
#  9.34444444e-01  3.27777778e-02 -4.98412698e-02  8.19444444e-03
# -5.77777778e-02 -1.65555556e-02  4.44444444e-02]
#[27.43        7.09        6.88        4.1825      1.64        0.73833333
#  0.65571429  0.71375     0.64777778  0.689       0.75      ] +- [0.52373658 0.1882817  0.15143756 0.10225581 0.05727128 0.03507928
# 0.03060612 0.02986951 0.02682821 0.02624881 0.02611165]
#A:  [27.43        7.09        6.88        4.1825      1.64        0.73833333
#  0.65571429  0.71375     0.64777778  0.689       0.75      ] +- [0.52373658 0.1882817  0.15143756 0.10225581 0.05727128 0.03507928
# 0.03060612 0.02986951 0.02682821 0.02624881 0.02611165]
#A-A_0:  [ 2.67244444e+01  6.38444444e+00  6.17444444e+00  3.47694444e+00
#  9.34444444e-01  3.27777778e-02 -4.98412698e-02  8.19444444e-03
# -5.77777778e-02 -1.65555556e-02  4.44444444e-02] + [0.14830698 0.09878449 0.08253925 0.08444397        nan        nan
#        nan        nan        nan        nan        nan] - [0.17419732 0.10962336 0.08996989 0.09223797        nan        nan
#        nan        nan        nan        nan        nan]
#R:  [0.02698   0.033725  0.0412794 0.043168  0.05396   0.0682594 0.0814796
# 0.0911924 0.10792   0.1197912 0.1300436]
#Konstante 1:  -132+/-12
#Konstante 2:  6.8+/-0.7
#Konstante 3:  9+/-27
#Konstante 4:  -4.6+/-2.7
#errY: [52.3736575  37.65634077 45.43126677 40.90232267 28.63564213 21.04756518
# 21.42428529 23.89560629 24.14539294 26.2488095  28.72281323]
#A1: [27.43        7.09        6.88        4.1825      1.64        0.73833333
#  0.65571429  0.71375     0.64777778  0.689       0.75      ]
#FehlerA1: [0.52373658 0.1882817  0.15143756 0.10225581 0.05727128 0.03507928
# 0.03060612 0.02986951 0.02682821 0.02624881 0.02611165]
#A: [ 2.67244444e+01  6.38444444e+00  6.17444444e+00  3.47694444e+00
#  9.34444444e-01  3.27777778e-02 -4.98412698e-02  8.19444444e-03
# -5.77777778e-02 -1.65555556e-02  4.44444444e-02]
