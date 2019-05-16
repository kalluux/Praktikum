import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat
import math
from scipy import stats

N = np.genfromtxt('n.txt', unpack=True)
q = np.mean(N)
#M= N/10
print(q)
print(np.std(N))
print('Mittelwert der Stichprobe', np.mean(N))
print('Varianz der Stichprobe', np.var(N, ddof = 1))
print('Varianz der Stichprobe', np.var(N))
print('gaussverteilung, da stndardabweichung 280^2 = varianz ist')

#def f(N):
 #  return 1/(79442*np.sqrt(2*np.pi)) * np.exp(-1/2 * ((N-5463)/79442)**2)
   
#Erstellt linspace von Bereich, in dem Ausgleichsfunktion erstellt wird
#plt.hist(N/10, 15, label='Messwerte', alpha=1, density=1)

#x_plot = np.linspace(4500, 6500)


#plt.plot(x_plot,f(x_plot))


#plt.savefig('h.pdf')