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
XUD = 4*(8.66*BD)/(QD*710)# muss noch durch 100
print(XUD)
LD = ufloat(1543.33,18.86)
XRD = 2*(LD*8.66)/(9.98*10**5*QD )#
print(XRD)

BN = ufloat(0.29,0.09)
QN = 9.09/(7.24*13.5)
print(QN)
XUN = 4*(8.66*BN)/(QN*710)
print(XUN)
LN = ufloat(121,12.83)
XRN = 2*(LN*8.66)/(9.98*10**5*QN )
print(XRN)

BP = ufloat(0.037,0.019)
QP = 7.87/(6.773*13.5)
print(QP)
XUP = 4*(8.66*BP)/(QP*710)
print(XUP)
LP = ufloat(50,7.07)
XRP = 2*(LP*8.66)/(9.98*10**5*QP )
print(XRP)

BG = ufloat(7.45,0.299)
QG = 14.08/(7.40*13.5)
print(QG)
XUG = 4*(8.66*BG)/(QG*710)
print(XUG)
LG = ufloat(775,14.72)
XRG = 2*(LG*8.66)/(9.98*10**5*QG )
print(XRG)

##################################################
#theoretisch
m0 = 4

