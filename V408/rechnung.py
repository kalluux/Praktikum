import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.constants import mu_0
import math

g, b = np.genfromtxt('daten.txt', unpack=True)

V1 = b/g
f = (1/b + 1/g)**(-1)
#print('V:', V1)
print('brennweiten:',f)
print('mittelwert brennweite:',np.mean(f), np.std(f))

l = np.array([96.5, 99])
print(np.mean(l), np.std(l))


###############################BESSEL WEISS

g1, b1, g2, b2 = np.genfromtxt('bessel.txt', unpack=True)
e = np.array([500,520,540,560,580,600,620,640,660,680])

d1 = g1-b1
d2 = g2-b2
print('d1:',d1)
print('d2:',d2)

f1 = (e**2 -d1**2)/(4*e)
print('Brennweite d1:', f1)
print('mittelwert f1:', np.mean(f1), np.std(f1))
f2 = (e**2 -d2**2)/(4*e)
print('Brennweite d2:', f2)
print('mittelwert f2:', np.mean(f2), np.std(f2))


###### BESSEL ROT
eBR = np.array([500,550,600,650,700])
b1R = np.array([138,130,128,124,122])
g1R = np.array([362,420,472,526,578])
b2R = np.array([368,423,478,532,584])
g2R = np.array([132,127,122,118,116])

d1R = g1R-b1R
d2R = g2R-b2R
print('d1R:',d1R)
print('d2R:',d2R)
f1R = (eBR**2 -d1R**2)/(4*eBR)
f2R = (eBR**2 -d2R**2)/(4*eBR)
print('Brennweite d1:',f1R)
print(np.mean(f1R),np.std(f1R))
print('Brennweite d2:',f2R)
print(np.mean(f2R),np.std(f2R))


####### BESSEL BLAU
eBL = np.array([500,550,600,650,700])
b1L = np.array([134,130,124,121,117])
g1L = np.array([366,420,476,529,583])
b2L = np.array([369,425,480,533,585])
g2L = np.array([131,125,120,117,115])

d1L = g1L-b1L
d2L = g2L-b2L
print('d1L:',d1L)
print('d2L:',d2L)
f1L = (eBL**2 -d1L**2)/(4*eBL)
f2L = (eBL**2 -d2L**2)/(4*eBL)
print('Brennweite d1:',f1L)
print(np.mean(f1L),np.std(f1L))
print('Brennweite d1:',f2L)
print(np.mean(f2L),np.std(f2L))