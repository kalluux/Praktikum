import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

#Holt Werte aus Textdatei
n, U = np.genfromtxt('dreieck.txt', unpack=True)
#T = T*10**(-3)

#Definiert Funktion mit der ihr fitten wollt (hier eine Gerade)
def f(x, A, B):
   return A*x + B

#Erstellt linspace von Bereich, in dem Ausgleichsfunktion erstellt wird
x_plot = np.linspace(-10, 10.1,1000)
#Fittet
params, covariance_matrix = curve_fit(f, np.log(n), np.log(U))
errors = np.sqrt(np.diag(covariance_matrix))
#Plottet Fit
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
#Gibt berechnete Parameter aus
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
#Plot eurer eigentlichen Messwerte
plt.plot(np.log(n) , np.log(U), 'r.', label='Messwerte', Markersize=4)
plt.xlim(-0.1,2.8)
plt.ylim(-5,0.1)
plt.legend()
plt.grid()
plt.xlabel('ln(n)')
plt.ylabel('ln($U/U_1$)')
plt.savefig('plot3.pdf')
