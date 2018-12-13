import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

#Holt Werte aus Textdatei
ln, t = np.genfromtxt('wertea.txt', unpack=True)
#T = T*10**(-3)

#Definiert Funktion mit der ihr fitten wollt (hier eine Gerade)
def f(x, A, B):
   return A*x + B

#Erstellt linspace von Bereich, in dem Ausgleichsfunktion erstellt wird
x_plot = np.linspace(0, 0.0005, 400)
#Fittet
params, covariance_matrix = curve_fit(f, t, ln)
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
plt.plot(t , ln, 'r.', label='Messwerte', Markersize=4)
plt.xlim(0,0.0005)
plt.legend()
plt.grid()
plt.xlabel('$t$ / s')
plt.ylabel('ln($U_c/U_0$)')
plt.savefig('plot1.pdf')
