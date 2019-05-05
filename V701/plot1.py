import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.constants import mu_0
import math

#Holt Werte aus Textdatei
#U, a = np.genfromtxt('kehr.txt', unpack=True)
x =[0, 0.09,0.18,0.27,0.36,0.44,0.53,0.62,0.71,0.8,0.89,0.98,1.07,1.15,1.24,1.33,1.42,1.51,1.6,1.69,1.78]
N = np.array([76536,71337,68768,65863,62204,58339,58861,66611,62401,57024,51804,43950,36752,27549,19646,10923,6037,2710,815,393,84])

y =[0.62,0.71,0.8,0.89,0.98,1.07,1.15,1.24,1.33]
M = np.array([66611,62401,57024,51804,43950,36752,27549,19646,10923 ])

#Definiert Funktion mit der ihr fitten wollt (hier eine Gerade)
def f(y, A, B):
   return A*y + B

#Erstellt linspace von Bereich, in dem Ausgleichsfunktion erstellt wird
x_plot = np.linspace(0.6,1.34, 400)
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
plt.xlim(-0.02,1.8)
plt.legend()
plt.grid()
plt.xlabel(r'$x/$cm')
plt.ylabel(r'$N$')
plt.savefig('plot1.pdf')

