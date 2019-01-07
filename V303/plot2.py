import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
#Holt Werte aus Textdatei
phi, u = np.genfromtxt('data3.txt', unpack=True)
x=phi*np.pi/180

#Definiert Funktion mit der ihr fitten wollt
def f(x, a, b, c, d):
   return a*np.cos(b*x + c) + d


#Erstellt linspace von Bereich, in dem Ausgleichsfunktion erstellt wird
x_plot = np.linspace(0, 2*np.pi, 500)
#Fittet
params, covariance_matrix = curve_fit(f, x, u)
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
plt.plot(x , u, 'r.', label='Messwerte', Markersize=4)
#plt.xlim(15,1000)
plt.legend()
plt.grid()
plt.xlabel('$\phi$ / rad')
plt.ylabel('$U$ / V')
plt.show()
plt.savefig('plot2.pdf')
print(x)

#(base) daniel@daniel-VB:~/Praktikum/V303$ python plot2.py
#[ 4.35747587  0.92058524  3.18862142 -0.13737109]
#[0.24449187 0.08953557 0.14430498 0.18842802]
#[0.         0.26179939 0.52359878 0.78539816 1.04719755 1.30899694
# 1.57079633 1.83259571 2.0943951  2.35619449 2.61799388 2.87979327
# 3.14159265]