import numpy as np 
from uncertainties import ufloat
import math

#Winkelrichtgröße

F = np.array([0.46,0.26,0.62,0.39,0.80,0.48,0.94,0.57,1.10,0.66])
W = np.array([30,30,40,40,50,50,60,60,70,70])
#r = np.array([0.02965,0.04945,0.02965,0.04945,0.02965,0.04945,0.02965,0.04945,0.02965,0.04945])
r1 = ufloat(0.02965,0.00005)
r2 = ufloat(0.04945,0.00005)
r = np.array([r1,r2,r1,r2,r1,r2,r1,r2,r1,r2])

D = F*r/W
print(D)

Dmittel = np.mean(D)
print(Dmittel)

# Trägheitmoment Kugel

Ik = 2/5 * 0.8123*(0.068775**2)
print(Ik)


#Zylinder

Iz = 1/2 * 0.3684*(0.04865**2)
print(Iz)










