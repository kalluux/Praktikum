import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.constants import mu_0
import math

#Holt Werte aus Textdatei
x, E = np.genfromtxt('energie.txt', unpack=True)



#Definiert Funktion mit der ihr fitten wollt (hier eine Gerade)
def f(x, A, B):
   return A*x + B

#Erstellt linspace von Bereich, in dem Ausgleichsfunktion erstellt wird
x_plot = np.linspace(-0.02,1.5, 400)
#Fittet
params, covariance_matrix = curve_fit(f, x, E)
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
plt.savefig('plot3.pdf')

