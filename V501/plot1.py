import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.constants import mu_0

#Holt Werte aus Textdatei
I, D = np.genfromtxt('strom.txt', unpack=True)
L = 0.175
N = 20*10**4
R = 0.282
B = mu_0*8/np.sqrt(125)*N*I/R


#Definiert Funktion mit der ihr fitten wollt (hier eine Gerade)
def f(x, A, B):
   return A*x + B

#Erstellt linspace von Bereich, in dem Ausgleichsfunktion erstellt wird
x_plot = np.linspace(0, 0.0005, 400)
#Fittet
params, covariance_matrix = curve_fit(f, B, D/(L**2+D**2))
errors = np.sqrt(np.diag(covariance_matrix))
#Plottet Fit
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
#Gibt berechnete Parameter aus
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
#Formatiert etws schöner
plt.gcf().subplots_adjust(bottom=0.18)
#Plot eurer eigentlichen Messwerte
plt.plot(B , D/(L**2+D**2), 'r.', label='Messwerte', Markersize=4)
plt.xlim(0,0.0005)
plt.legend()
plt.grid()
plt.xlabel(r'$t$ / s')
plt.ylabel(r'ln($U_c/U_0$)')
plt.savefig('plot1.pdf')

