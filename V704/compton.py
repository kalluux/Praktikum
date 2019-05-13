import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
re= 2.82*10**(-15)
e= 1.295
na = 6.022*10**23
#sig = 2 * np.pi * re**2 * ((1+e)/e**2 * ((2(1+e))/(1+e**2) - np.log(1+2*e)/e) + np.log(1+2*e)/2*e - (1+3*e)/((1+2*e)**2))
sig2 = 2* np.pi * re**2 * ( (1+e)/(e**2) * ( (2*(1+e))/(1+2*e) - np.log(1+2*e)/e ) + np.log(1+2*e)/(2*e) - (1+3*e)/((1+2*e)**2))
sig = 5.746621960743576*10**(-30)


m1 = 207.2
rho1 = 11342
z1= 82
mu1 = z1 * na * rho1 * sig2 / m1
print(mu1)

m2 = 55.845
rho2 = 7874
z2 = 26
mu2 = z2 * na * rho2 * sig2 / m2
print(mu2)

#mu1 = 0.06934931469908188
#mu2 = 0.0566386499242974
