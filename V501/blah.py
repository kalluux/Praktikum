import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.constants import mu_0
import math

#Holt Werte aus Textdatei
U, a = np.genfromtxt('kehr.txt', unpack=True)
L = 0.175
N = 20
R = 0.282



#Definiert Funktion mit der ihr fitten wollt (hier eine Gerade)
def f(x, A, B):
   return A*x + B

#Erstellt linspace von Bereich, in dem Ausgleichsfunktion erstellt wird
x_plot = np.linspace(0.002,0.006, 400)
#Fittet
params, covariance_matrix = curve_fit(f, U, a)
errors = np.sqrt(np.diag(covariance_matrix))
#Plottet Fit
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
#Gibt berechnete Parameter aus
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
#Formatiert etws schöner
plt.gcf().subplots_adjust(bottom=0.18)
#Plot eurer eigentlichen Messwerte
plt.plot(U , a, 'r.', label='Messwerte', Markersize=4)
plt.xlim(0.0024,0.0051)
plt.legend()
plt.grid()
plt.xlabel(r'$\frac{1}{U} / \mathrm{\frac{1}{V}}$')
plt.ylabel(r'$\frac{D}{U_d} / (\mathrm{\frac{m}{V}})$')
plt.savefig('plot8.pdf')

a = ufloat(0.324,0.015)
D = (0.0125*300)/a
print(D)
