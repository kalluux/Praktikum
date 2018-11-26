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

print('Ikugel: ', ikugel)

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
mu = (e/(2*G))-1
print('Querkontraktionszahl mu: ', mu)