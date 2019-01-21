import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

mu0 = 4 * np.pi * 10**(-7)
#KURZE GERADE SPULE 

b = [0.000039, 0.000079, 0.000147, 0.000287, 0.000567, 0.00113, 0.001551, 0.001801, 0.001838, 0.001684, 0.001351, 0.0000728, 0.0000377, 0.0000173, 0.00001, 0.00006, 0.000035, 0.000018]
x = [-0.05 , -0.04 , -0.03 , -0.02 , -0.01 , 0     , 0.01  , 0.02  , 0.03  , 0.04  , 0.05  , 0.06  , 0.07, 0.08, 0.09, 0.1, 0.11, 0.12]


def weltformel(a, i, r, n, l):   #a: Punkt entlang der x-Achse, l:Länge der Spule
    return  (mu0 * i * n) / (2 * l) * ( (a) / (np.sqrt(r**2 + (a)**2)) + (l - a) / (np.sqrt(r**2 + (l-a)**2)))


#KURZE SPULE 
plt.plot(x, b, 'rx', label = 'Messwerte', Markersize=4)

x_plot = np.linspace(-0.05, 0.12, 1000) #THEORIE
plt.plot(x_plot, weltformel(x_plot - 0.005, 1, 0.0205, 100, 0.045), 'b--', label = 'Theoriekurve')

plt.xticks([-0.06,-0.04,-0.02,0,0.02,0.04,0.06,0.08,0.1,0.12],
            ['-6','-4','-2','0','2','4','6','8','10','12'])
plt.yticks([0,0.0005,0.001,0.0015,0.002,0.0025],
            ['0','0.5','1','1.5','2','2.5'])

plt.legend()
plt.xlabel('$x$ / cm')
plt.ylabel('$B$ / mT')
plt.grid()
plt.show()
plt.savefig('kurz.pdf')

print('theorie bei 3cm', weltformel(0.03 - 0.005, 1, 0.0205, 100, 0.045))