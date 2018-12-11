import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

mu = ufloat(194.51086486, 13.14812429)
L = ufloat(16.78 * 10**(-3), 0.09 * 10**(-3))
R = ufloat(682, 1)

Reff = 4 * np.pi * L * mu

print('Reff: ', Reff)

#Reff:  41.0+/-2.8

Tex = 2 * L / Reff
print('Tex: ', Tex)

#AUFGABE B
C = ufloat(2.066 * 10**(-9), 0.006 * 10**(-9))

Rap = 2*(L/C)**0.5

print('Rap: ', Rap)

#AUFGABE C
q = L**0.5 / (R * C**0.5)

print('Güte q: ',q)


#AUFGABE D
b = R / (2 * np.pi * L)
print('b: ', b)

f1 = R/(4*np.pi*L) + 1/(2*np.pi) * (R**2/(4*L**2)+ 1/(L*C))**(0.5)
f2 = -R/(4*np.pi*L) + 1/(2*np.pi) * (R**2/(4*L**2)+ 1/(L*C))**(0.5)
fres = 1/(2*np.pi) * (1/(L*C) - R**2/(2*L**2))**0.5
print('f1= ', f1)
print('f2= ', f2)
print('fres= ', fres)