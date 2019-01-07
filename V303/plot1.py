import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
#Holt Werte aus Textdatei
phi, u = np.genfromtxt('data2.txt', unpack=True)
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
plt.savefig('plot1.pdf')
print(x)

#(base) daniel@daniel-VB:~/Praktikum/V303$ python plot1.py
#[4.33556093 0.93024957 3.15924383 0.22121211]
#[0.23956466 0.08960705 0.14309991 0.19001222]
#[0.         0.26179939 0.52359878 0.78539816 1.04719755 1.30899694
# 1.57079633 1.83259571 2.0943951  2.35619449 2.61799388 2.87979327
# 3.14159265]