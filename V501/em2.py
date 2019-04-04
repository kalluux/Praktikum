import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.constants import mu_0
import math

#Holt Werte aus Textdatei
U, D = np.genfromtxt('ud1.txt', unpack=True)
L = 0.175
N = 20
R = 0.282



#Definiert Funktion mit der ihr fitten wollt (hier eine Gerade)
def f(x, A, B):
   return A*x + B

#Erstellt linspace von Bereich, in dem Ausgleichsfunktion erstellt wird
x_plot = np.linspace(-40,15, 400)
#Fittet
params, covariance_matrix = curve_fit(f, U, D)
errors = np.sqrt(np.diag(covariance_matrix))
#Plottet Fit
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
#Gibt berechnete Parameter aus
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
#Formatiert etws schöner
plt.gcf().subplots_adjust(bottom=0.18)
#Plot eurer eigentlichen Messwerte
plt.plot(U , D, 'r.', label='Messwerte', Markersize=4)
plt.xlim(-31, 9)
plt.legend()
plt.grid()
plt.xlabel(r'$U_d/V$')
plt.ylabel(r'$D/$m')
plt.savefig('plot4.pdf')
