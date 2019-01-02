import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
#Holt Werte aus Textdatei
f, a, phi = np.genfromtxt('phase.txt', unpack=True)


plt.xscale('log')
#Formatiert etws schöner
#x_plot = np.linspace(22.5, 29, 500)
#y_plot = np.linspace(2.687, 2.687, 500)
plt.gcf().subplots_adjust(bottom=0.18)
#Plot eurer eigentlichen Messwerte
#plt.plot(x_plot, y_plot, 'b-', label='b', Markersize=4)
plt.plot(f , phi, 'r.', label='Messwerte', Markersize=4)
#plt.xlim(15,1000)
plt.legend()
plt.grid()
plt.xlabel('$f$ / kHz')
plt.ylabel('$\phi$ / rad')
plt.show()
plt.savefig('plotd.pdf')
