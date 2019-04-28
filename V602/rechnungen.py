import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.constants import mu_0
import math

h = 6.626070040*10**(-34)
c = 299792458 
d = 2.014*10**(-10)

E = (h*c)/(2*d*math.sin(0.069813170079773))
print(E)

maxenergie = E*6.242*10**(18)
print(maxenergie)

#winkel betamax : 20,15625
#winkel alphamax : 22,34375

Eb = (h*c)/(2*d*math.sin(0.35179292735511))
print(Eb)
Ebeta = Eb*6.242*10**(18)
print(Ebeta)
Ea = (h*c)/(2*d*math.sin(0.38997200474248 ))
print(Ea)
Ealpha = Ea*6.242*10**(18)
print(Ealpha)

#sg1 = 29-math.sqrt(Ebeta/13.6)
#print(sg1)
#sg2 = 29-2*math.sqrt((13.6*(29-sg1)**2 -Ealpha)/13.6)
#print(sg2)
#sg3 = 29-3*math.sqrt((13.6*(29-sg1)**2 -Ebeta)/13.6)
#print(sg3)

Ea1 =(h*c)/(2*d*math.sin(0.38449603421435 ))*6.242*10**(18)
Ea2 =(h*c)/(2*d*math.sin(0.39269908169872))*6.242*10**(18)
Eb1 =(h*c)/(2*d*math.sin(0.34636059005827))*6.242*10**(18)
Eb2 =(h*c)/(2*d*math.sin(0.35456363754265))*6.242*10**(18)
print(Ea1,Ea2,Eb1,Eb2)
DeltaEa = Ea1-Ea2
DeltaEb = Eb1-Eb2
print(DeltaEa,DeltaEb)

#materialien
#winkelbrom = ufloat(13.3, 0.1)
#winkelzirkonium = ufloat(10, 0.1)
#winkelstrontium = ufloat(11.3, 0.1)
#winkelzink = ufloat(18.6, 0.1)
winkelbrom = 13.3
winkelzirkonium = 10
winkelstrontium = 11.3
winkelzink = 18.6
winkelquecksilber1 = 12.5
winkelquecksilber2 = 14.7

ebrom = (h*c)/(2*d*math.sin(winkelbrom * np.pi / 180))*6.242*10**(18)
ezirkonium = (h*c)/(2*d*math.sin(winkelzirkonium * np.pi / 180))*6.242*10**(18)
estrontium = (h*c)/(2*d*math.sin(winkelstrontium * np.pi / 180))*6.242*10**(18)
ezink = (h*c)/(2*d*math.sin(winkelzink * np.pi / 180))*6.242*10**(18)
equecksilber1 = (h*c)/(2*d*math.sin(winkelquecksilber1 * np.pi / 180))*6.242*10**(18)
equecksilber2 = (h*c)/(2*d*math.sin(winkelquecksilber2 * np.pi / 180))*6.242*10**(18)
dqs = equecksilber1 - equecksilber2

print('Energien: ', ebrom, ezirkonium, estrontium, ezink, equecksilber1, equecksilber2)

a= 1/137.036
sgbrom = 35-math.sqrt(ebrom/13.6)
sgzirkonium = 40-math.sqrt(ezirkonium/13.6)
sgstrontium = 38-math.sqrt(estrontium/13.6)
sgzink = 30-math.sqrt(ezink/13.6)
sgquecksilber = 80 - ((4/a) * (dqs/13.61)**0.5 - 5 * (dqs / 13.61))**(1/2) * (1+ (19/32) * a**2 * (dqs / 13.61))**(1/2)

print('Sigma: ', sgbrom, sgzirkonium, sgstrontium, sgzink, sgquecksilber)
print('Wurzeln: ', math.sqrt(ebrom), math.sqrt(ezirkonium), math.sqrt(estrontium) ,math.sqrt(ezink))
print(dqs)