import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.constants import mu_0
import math

DU = np.array([0.1576,0.1570,0.1609])
DR = np.array([1530,1530,1570])
print(np.mean(DR),np.std(DR),np.mean(DU),np.std(DU))

NU = np.array([0.0022,0.0042,0.0024])
NR = np.array([114,139,110])
print(np.mean(NR),np.std(NR),np.mean(NU),np.std(NU))

PU = np.array([0.0001,0.0005,0.0005])
PR = np.array([40,55,55])
print(np.mean(PR),np.std(PR),np.mean(PU),np.std(PU))

GU = np.array([0.0755,0.0704,0.0775])
GR = np.array([790,755,780])
print(np.mean(GR),np.std(GR),np.mean(GU),np.std(GU))

################

BD = ufloat(15.85,0.17)
QD = 14.38/(7.8*13.5)
print(QD)#cm
XUD = 4*(0.866*(BD/100))/(QD*710)
print(XUD)
LD = ufloat(1543.33,18.86)
XRD = 2*(LD*0.866)/(9.98*10**5*QD )#
print(XRD)

BN = ufloat(0.29,0.09)
QN = 9.09/(7.24*13.5)
print(QN)
XUN = 4*(0.866*(BN/100))/(QN*710)
print(XUN)
LN = ufloat(121,12.83)
XRN = 2*(LN*0.866)/(9.98*10**5*QN )
print(XRN)

BP = ufloat(0.037,0.019)
QP = 7.87/(6.773*13.5)
print(QP)
XUP = 4*(0.866*(BP/100))/(QP*710)
print(XUP)
LP = ufloat(50,7.07)
XRP = 2*(LP*0.866)/(9.98*10**5*QP )
print(XRP)

BG = ufloat(7.45,0.299)
QG = 14.08/(7.40*13.5)
print(QG)
XUG = 4*(0.866*(BG/100))/(QG*710)
print(XUG)
LG = ufloat(775,14.72)
XRG = 2*(LG*0.866)/(9.98*10**5*QG )
print(XRG)

##################################################
#theoretisch
pi = math.pi
T = 295.15
m0 = 4*pi*10**(-7)
mB = 9.274*10**(-24)
k = 1.381*10**(-23)
XDT = (m0*mB**2*(1.33)**2*2.52*10**(28)*7.5*8.5)/(3*k*T)
print(XDT)
XNT = (m0*mB**2*(0.73)**2*2.59*10**(28)*4.5*5.5)/(3*k*T)
print(XNT)
XPT = (m0*mB**2*(0.8)**2*1.49*10**(28)*4*5)/(3*k*T)
print(XPT)
XGT = (m0*mB**2*(2)**2*2.46*10**(28)*3.5*4.5)/(3*k*T)
print(XGT)

