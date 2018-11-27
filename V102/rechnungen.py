import numpy as np 
from uncertainties import ufloat
import math
import uncertainties.unumpy as unp

#Periodendauer
T = np.array([18.247, 18.242, 18.244, 18.245, 18.250, 18.249, 18.243, 18.235, 18.248, 18.250])
print('T: ', np.mean(T),np.std(T))

Tmittel = ufloat(18.245, 0.004)

mkugel = ufloat(0.5883, 0.00023532)
rkugel = ufloat(0.05103/2, 0.000020412/2)
ikugel = 2/5 * mkugel * rkugel**2
igesamt = ikugel + 2.25*10**(-6)

print('Ikugel: ', ikugel)
print('Igesamt: ', igesamt)

#Durchmesser Draht in m
d = np.array([0.000172, 0.000173, 0.00017])
print('d Draht: ', np.mean(d),'+-',np.std(d))

dmittel = ufloat(0.00017166666, 0.000001247)
rdraht = dmittel/2

print('dmittel = ', dmittel)
#Länge Draht in m
L = 0.663

print('Ausgabe: ' , mkugel,',',rkugel,',',L,',',Tmittel,',',dmittel)
G = (16 * np.pi * mkugel * rkugel**2 * L)/(5 * Tmittel**2 * rdraht**4)
print('Schubmodul G: ', G)

e = 210 * 10**9
mu = ((e/(2*G))-1)*(-1)
print('Querkontraktionszahl mu: ', mu)
Q = e / (3 - 6 * mu)
print('Kompressionsmodel Q: ', Q)

Galtprotokoll = (16 * np.pi * 0.5122 * 0.02538**2 * 0.624) / (5 * 18.515**2 * (0.000197/2)**4)
print('Schubmodul Galtprotokoll: ', Galtprotokoll)

#MAGNETISCHES MOMENT
#bfeld
rspule = 0.072
mu0 = 4 * np.pi*10**(-7)

bfeld = mu0 * (8*1)/(np.sqrt(125) * 0.072) * 80 #I = 1 in diesem fall
print('bfeld =', bfeld)

a4 = np.array([5.670, 5.687, 5.659, 5.682, 5.441])
a5 = np.array([5.087, 5.039, 5.046, 5.090, 5.107])
a6 = np.array([4.576, 4.596, 4.611, 4.603, 4.597])
a8 = np.array([3.842, 3.856, 3.846, 3.847, 3.831])
a10 = np.array([3.301, 3.284, 3.276, 3.270, 3.289])

print('a4mittel: ', np.mean(a4),np.std(a4))
print('a5mittel: ', np.mean(a5),np.std(a5))
print('a6mittel: ', np.mean(a6),np.std(a6))
print('a8mittel: ', np.mean(a8),np.std(a8))
print('a10mittel: ', np.mean(a10),np.std(a10))

a4mittel = ufloat(5.6278, 0.0939)
a5mittel = ufloat(5.0738, 0.0265)
a6mittel = ufloat(4.5966, 0.0116)
a8mittel = ufloat(3.8444, 0.0081)
a10mittel = ufloat(3.2840, 0.0107)

#PLOT psi funktion
psi = 4 * np.pi**2 * igesamt / a10mittel**2
print('psi: ', psi)