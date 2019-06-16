import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.constants import mu_0
import math

d = np.array([4.3,4.6,4.8,4.8,4.9,4.8,4.8,4.7,4.8,4.7])
dneu = d/5.017

print('d:',dneu)

z = np.array([3034,3178,3024,3047,3045,3061,3056,3024,3063,3036])
y = (dneu*2*1000000)/z
print('wellenlänge:', y)
print('mittelwert wellenlänge in nm:',np.mean(y), np.std(y))
#mittelwert ohne die ersten beiden werte: 626.869946323239 7.124127395822786
################ BRECHUNGSINDIZE ##################
w = ufloat(615.697,23.393)
w1 = w*10**(-9)
T0 = 273.15
p0 = 1.0132
T = 295.15
b = 0.05
p = 0.6
z1 = np.array([24,23,24,24,25,25,25,24,24,25])

n = 1 + (z1*w1*T*p0)/(2*b*T0*p)
print('brechung:',n)

print('mittelwert brechung:',np.mean(n))



