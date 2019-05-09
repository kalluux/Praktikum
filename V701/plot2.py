import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.constants import mu_0
import math

#Holt Werte aus Textdatei
#U, a = np.genfromtxt('kehr.txt', unpack=True)
x =[0,0.07,0.1,0.22,0.3,0.37,0.44,0.52,0.59,0.67,0.74,0.81,0.89,0.96,1.04,1.11,1.18,1.26,1.33,1.41,1.48]
N = np.array([100641,99843,97151,89611,81133,80746,87899,73592,62289,60611,48074,42297,50444,22476,12618,9582,15223,5477,3671,1024,723])


y =[0.44,0.52,0.59,0.67,0.74,0.81,0.89,0.96,1.04]
M = np.array([87899,73592,62289,60611,48074,42297,50444,22476,12618 ])

#Definiert Funktion mit der ihr fitten wollt (hier eine Gerade)
def f(y, A, B):
   return A*y + B

#Erstellt linspace von Bereich, in dem Ausgleichsfunktion erstellt wird
x_plot = np.linspace(0.4,1.06, 400)
#Fittet
params, covariance_matrix = curve_fit(f, y, M)
errors = np.sqrt(np.diag(covariance_matrix))
#Plottet Fit
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
#Gibt berechnete Parameter aus
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
#Formatiert etws schöner
plt.gcf().subplots_adjust(bottom=0.18)
#Plot eurer eigentlichen Messwerte
plt.plot(x , N, 'r.', label='Messwerte', Markersize=4)
plt.xlim(-0.0,1.5)
plt.legend()
plt.grid()
plt.xlabel(r'$x/$cm')
plt.ylabel(r'$N$')
plt.savefig('plot2.pdf')

