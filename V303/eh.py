import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

#Holt Werte aus Textdatei
r, u = np.genfromtxt('data4.txt', unpack=True)
#T = T*10**(-3)

#Definiert Funktion mit der ihr fitten wollt (hier eine Gerade)
def f(r, A, B):
   return A*r + B

#Erstellt linspace von Bereich, in dem Ausgleichsfunktion erstellt wird
x_plot = np.linspace(3, 6, 500)
#Fittet
params, covariance_matrix = curve_fit(f, np.log(r), np.log(u))
errors = np.sqrt(np.diag(covariance_matrix))
#Plottet Fit
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
#Gibt berechnete Parameter aus
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
#Plot eurer eigentlichen Messwerte
plt.plot(np.log(r) , np.log(u), 'r.', label='Messwerte', Markersize=4)
plt.xlim(3,4.5)
plt.ylim(-5,0)
plt.legend()
plt.grid()
plt.xlabel('ln($r$) ')
plt.ylabel('ln($U$) ')
plt.savefig('plot3.pdf')
