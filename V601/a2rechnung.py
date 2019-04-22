import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import math

x,y = np.genfromtxt('a2.txt', unpack=True)
m = y/x
print(m)

ua = x * 2/49


print (ua)
u = np.array([0,2.57,3.94,4.35,4.55,4.75,5.16,5.57,6.39,9.25,10])
#
plt.plot(u, m, 'b', linewidth=0.9)
plt.xlabel('$U_A$ / V')
plt.ylabel('Steigung')
plt.grid()
plt.tight_layout()
plt.savefig('plota2.pdf')
plt.close()

#m
#[ 0.01694915  0.1         0.2         0.4         0.8         1.2
#  1.4         2.          4.          7.5         9.         10.
#  5.          4.5         1.66666667  0.5       ]

