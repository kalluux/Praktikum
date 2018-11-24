import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

#Holt Werte aus Textdatei
ln, T = np.genfromtxt('Werte.txt', unpack=True)
T = T*10**(-3)

#Definiert Funktion mit der ihr fitten wollt (hier eine Gerade)
def f(x, A, B):
   return A*x + B

#Erstellt linspace von Bereich, in dem Ausgleichsfunktion erstellt wird
x_plot = np.linspace(0.003, 0.0035, 400)
#Fittet
params, covariance_matrix = curve_fit(f, T, ln)
errors = np.sqrt(np.diag(covariance_matrix))
#Plottet Fit
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
#Gibt berechnete Parameter aus
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
#gr = ufloat(-12.81899817, 0.28532842)
#print(gr)
#grr = np.e**(gr)
#print(grr)
#Formatiert etws schöner
plt.gcf().subplots_adjust(bottom=0.18)
#Plot eurer eigentlichen Messwerte
plt.plot(T , ln, 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.xlabel('1/T / 1/K')
plt.ylabel('ln($\eta$/Pas)')
plt.savefig('plot.pdf')
