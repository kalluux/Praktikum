import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
#Holt Werte aus Textdatei
t, u = np.genfromtxt('wertea.txt', unpack=True)

#Definiert Funktion mit der ihr fitten wollt
def f(a,b, mu):
   return b * np.exp(-2 * np.pi * mu * a)

#c= [32.19871049 29.79653928 27.59469499 25.79307829 24.59152897 23.39016235
# 21.98907771 21.18786262 20.58672207 20.38521815 19.7842267  19.38307043
# 18.78216482]


#Erstellt linspace von Bereich, in dem Ausgleichsfunktion erstellt wird
x_plot = np.linspace(0.000015, 0.000480, 500)
#Fittet
params, covariance_matrix = curve_fit(f, t, u)
errors = np.sqrt(np.diag(covariance_matrix))
#plt.xscale('log')
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
plt.plot(t , u, 'r.', label='Messwerte', Markersize=4)
#plt.xlim(15,1000)
plt.legend()
plt.grid()
plt.xlabel('$t$ / s')
plt.ylabel('$U_c$ / V')
plt.show()
plt.savefig('plota.pdf')

# b und mu + fehler
#[ 31.32044808 194.51086486]
#[ 0.62582781 13.14812429]
