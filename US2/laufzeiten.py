import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

locha1, ta1 = np.genfromtxt('ascan1.txt', unpack=True)
locha2, ta2 = np.genfromtxt('ascan2.txt', unpack=True)
lochb1, tb1 = np.genfromtxt('bscan1.txt', unpack=True)
lochb2, tb2 = np.genfromtxt('bscan2.txt', unpack=True)

#umrechnung in meter
tb1 = tb1 * 10**(-3)
tb2 = tb2 * 10**(-3)

c = 2370 * 10**(-6)

tiefe1 = 1/2 * c * ta1 - 0.002
tiefe2 = 1/2 * c * ta2 - 0.002
durchmessera1 = 0.0826 - tiefe1 - tiefe2
durchmesserb = 0.0835 - tb1 - tb2 + 0.002 + 0.002

#AUSWERTUNG A
print(locha1)
print("Tiefe 1:", tiefe1)
print(locha2)
print("Tiefe 2:", tiefe2)
print("Durchmesser:", durchmessera1)
#AUSWERTUNG B
print(lochb1)
print(lochb2)
print("Durchmesser:", durchmesserb)

#ALTERNATIVE AUSWERTUNG A

#IN METERN
#[ 3.  4.  5.  6.  7.  8.  9. 10. 11.]
#Tiefe 1: [0.0533395 0.047059  0.04066   0.0341425 0.0270325 0.0203965 0.0135235
# 0.0068875 0.0483625]
#[ 3.  4.  5.  6.  7.  8.  9. 10. 11.]
#Tiefe 2: [0.0121015 0.01933   0.0265585 0.0341425 0.0410155 0.0478885 0.0547615
# 0.0616345 0.0137605]
#Durchmesser: [0.018059  0.017111  0.0162815 0.015215  0.015452  0.015215  0.015215
# 0.014978  0.021377 ]

#B
#[3. 4. 5. 6. 7. 8. 9.]
#[3. 4. 5. 6. 7. 8. 9.]
#Durchmesser: [0.0102 0.0092 0.0083 0.0069 0.007  0.0072 0.007 ]