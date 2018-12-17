import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

#Holt Werte aus Textdatei
phi, v = np.genfromtxt('wertec.txt', unpack=True)




#Definiert Funktion mit der ihr fitten wollt (hier eine Gerade)
def f(c,d):
   return np.arctan(d*c*2*np.pi)
#Erstellt linspace von Bereich, in dem Ausgleichsfunktion erstellt wird
x_plot = np.linspace(9, 10800, 1000)
#Fittet
params, covariance_matrix = curve_fit(f, v, phi)
errors = np.sqrt(np.diag(covariance_matrix))
plt.xscale('log')
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
plt.plot(v , phi, 'r.', label='Messwerte', Markersize=4)
plt.xlim(9,10800)
plt.legend()
plt.grid()
plt.xlabel(r'$f$ / Hz')
plt.ylabel('$\phi$ / rad')
plt.savefig('plot3.pdf')
