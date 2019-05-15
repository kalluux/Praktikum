import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.constants import mu_0
import math

#Holt Werte aus Textdatei
x, E = np.genfromtxt('energie2.txt', unpack=True)

y = [0.1,0.22,0.3,0.37,0.44,0.52,0.59,0.67,0.74]
B = [3.64,3.46,3.4,3.34,3.4,3.16,2.97,3.03,2.91]

#Definiert Funktion mit der ihr fitten wollt (hier eine Gerade)
def f(y, A, B):
   return A*y + B

#Erstellt linspace von Bereich, in dem Ausgleichsfunktion erstellt wird
x_plot = np.linspace(0.09,0.75, 400)
#Fittet
params, covariance_matrix = curve_fit(f, y, B)
errors = np.sqrt(np.diag(covariance_matrix))
#Plottet Fit
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
#Gibt berechnete Parameter aus
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
#Formatiert etws schöner
plt.gcf().subplots_adjust(bottom=0.18)
#Plot eurer eigentlichen Messwerte
plt.plot(x , E, 'r.', label='Messwerte', Markersize=4)
plt.xlim(-0.02,1.5)
plt.legend()
plt.grid()
plt.xlabel(r'$x/$cm')
plt.ylabel(r'$E/$MeV')
plt.savefig('plot4.pdf')


