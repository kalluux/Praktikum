import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
#Holt Werte aus Textdatei
f, u0, uc = np.genfromtxt('wertec.txt', unpack=True)
u = uc/u0

#plt.xscale('log')
#Formatiert etws schöner
x_plot = np.linspace(22.5, 29, 500)
y_plot = np.linspace(2.687, 2.687, 500)
plt.gcf().subplots_adjust(bottom=0.18)
#Plot eurer eigentlichen Messwerte
plt.plot(x_plot, y_plot, 'b-', label='b', Markersize=4)
plt.plot(f , u, 'r.', label='Messwerte', Markersize=4)
#plt.xlim(15,1000)
plt.legend()
plt.grid()
plt.xlabel('$f$ / kHz')
plt.ylabel('$U_c/U$')
plt.show()
plt.savefig('plotc.pdf')

print(u)