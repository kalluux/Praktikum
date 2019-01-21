import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

mu0 = 4 * np.pi * 10**(-7)
#LANGE GERADE SPULE 

b = [0.000131, 0.000193, 0.000316, 0.000569, 0.001033, 0.001648, 0.002007, 0.002185, 0.002280, 0.002330, 0.002353, 0.002369, 0.002374, 0.002372, 0.002364, 0.002346, 0.002307]
x = [-0.04 , -0.03 , -0.02 , -0.01 , 0     , 0.01  , 0.02  , 0.03  , 0.04  , 0.05  , 0.06  , 0.07, 0.08, 0.09, 0.1, 0.11, 0.12]


def weltformel(a, i, r, n, l):   #a: Punkt entlang der x-Achse, l:Länge der Spule
    return  (mu0 * i * n) / (2 * l) * ( (a) / (np.sqrt(r**2 + (a)**2)) + (l - a) / (np.sqrt(r**2 + (l-a)**2)))


#KURZE SPULE 
plt.plot(x, b, 'rx', label = 'Messwerte', Markersize=4)

x_plot = np.linspace(-0.05, 0.12, 1000) #THEORIE
plt.plot(x_plot, weltformel(x_plot - 0.005, 1, 0.0205, 300, 0.15), 'b--', label = 'Theoriekurve')

plt.xticks([-0.06,-0.04,-0.02,0,0.02,0.04,0.06,0.08,0.1,0.12],
            ['-6','-4','-2','0','2','4','6','8','10','12'])
plt.yticks([0,0.0005,0.001,0.0015,0.002,0.0025],
            ['0','0.5','1','1.5','2','2.5'])

plt.legend()
plt.xlabel('$x$ / cm')
plt.ylabel('$B$ / mT')
plt.grid()
plt.show()
plt.savefig('lang.pdf')

print('theorie bei 8cm', weltformel(0.08 - 0.005, 1, 0.0205, 300, 0.15))