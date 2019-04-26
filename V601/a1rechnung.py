import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import math

x,y = np.genfromtxt('a1.txt', unpack=True)
m = y/x
print(m)

ua = x * 2/49


print (ua)
u = np.array([0,2.41,6.08,7.30,8.12,8.53,8.73,8.93,9.09,9.21,9.29,9.37,9.45,9.53,9.61,9.73,10])

plt.plot(u, m, 'b', linewidth=0.9)
plt.xlabel('$U_A$ / V')
plt.ylabel('Steigung')
plt.grid()
plt.tight_layout()
plt.savefig('plota1.pdf')
plt.close()
#m
#[ 0.01694915  0.1         0.2         0.4         0.8         1.2
#  1.4         2.          4.          7.5         9.         10.
#  5.          4.5         1.66666667  0.5       ]


t = (6.626*10**(-34)*299792458)/(2*2.014*10**(-10)*2.276*10**(-15))
print(t)
s = (6.626*10**(-34)*299792458)/(2*2.014*10**(-10)*1.968*10**(-15))
print(s)