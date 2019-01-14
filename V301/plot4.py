import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

#Holt Werte aus Textdatei
I, U = np.genfromtxt('sinus.txt', unpack=True)

#Definiert Funktion mit der ihr fitten wollt (hier eine Gerade)
def f(x, A, B):
   return A*x + B

#Erstellt linspace von Bereich, in dem Ausgleichsfunktion erstellt wird
x_plot = np.linspace(0.5, 2.45, 1000)
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
plt.xlim(0.5, 2.45)
plt.ylim(3,1.6)
plt.legend()
plt.grid()
plt.xlabel(r'$I\,/\,\mathrm{mA}$')
plt.ylabel(r'$U\,/\,\mathrm{V}$')
plt.savefig('plot4.pdf')
