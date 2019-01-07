import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
#Holt Werte aus Textdatei
r, u = np.genfromtxt('data4.txt', unpack=True)

#Definiert Funktion mit der ihr fitten wollt
def f(r, a, b):
   return a * r**(-2) + b


#Erstellt linspace von Bereich, in dem Ausgleichsfunktion erstellt wird
x_plot = np.linspace(6, 80, 5000)
#Fittet
params, covariance_matrix = curve_fit(f, r, u)
errors = np.sqrt(np.diag(covariance_matrix))
#plt.xscale('log')
#Plottet Fit
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
#Gibt berechnete Parameter aus
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
#Formatiert etws schöner
plt.gcf().subplots_adjust(bottom=0.18)
#Plot eurer eigentlichen Messwerte
plt.plot(r , u, 'r.', label='Messwerte', Markersize=4)
#plt.xlim(15,1000)
plt.legend()
plt.grid()
plt.xlabel('$r$ / cm')
plt.ylabel('$U$ / V')
plt.show()
plt.savefig('plot3.pdf')

#(base) daniel@daniel-VB:~/Praktikum/V303$ python plot3.py
#[4.74959779e+02 2.76659273e-01]
#[29.42270703  0.2210627 ]