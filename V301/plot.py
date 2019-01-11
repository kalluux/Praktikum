import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

#Holt Werte aus Textdatei
I, U = np.genfromtxt('werte1.txt', unpack=True)
I = I*10**(-3)

#Definiert Funktion mit der ihr fitten wollt (hier eine Gerade)
def f(x, A, B):
   return A*x + B

#Erstellt linspace von Bereich, in dem Ausgleichsfunktion erstellt wird
x_plot = np.linspace(0.02, 0.1, 1000)
#Fittet
params, covariance_matrix = curve_fit(f, I, U)
errors = np.sqrt(np.diag(covariance_matrix))
#Plottet Fit
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
#Gibt berechnete Parameter aus
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
#Plot eurer eigentlichen Messwerte
plt.plot(I , U, 'r.', label='Messwerte', Markersize=4)
plt.xlim(0.024, 0.1)
plt.ylim(0.87,1.35)
plt.legend()
plt.grid()
plt.xlabel(r'$I/\mathrm{A}$')
plt.ylabel(r'$U_K/\mathrm{V}$')
plt.savefig('plot1.pdf')
