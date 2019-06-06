from uncertainties import ufloat
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
import uncertainties.unumpy as unp
import scipy.constants as con

u1, i1 = np.genfromtxt('a1.txt', unpack=True)
u2, i2 = np.genfromtxt('a2.txt', unpack=True)
u3, i3 = np.genfromtxt('a3.txt', unpack=True)
u4, i4 = np.genfromtxt('a4.txt', unpack=True)
u5, i5 = np.genfromtxt('a5.txt', unpack=True)
################## a ####################
plt.plot(u5,i5, 'x',color='lawngreen',  label=         '2,4A, 4,1V')
plt.hlines(0.19, -10, 270, color='lawngreen', linestyles='dotted', label='Sättigungsstrom für 2,4A')
plt.plot(u4,i4, 'x',color='mediumturquoise',  label=   '2,3A, 4,0V')
plt.hlines(0.095, -10, 270, color='mediumturquoise', linestyles='dotted', label='Sättigungsstrom für 2,3A')
plt.plot(u3,i3, 'x',color='mediumaquamarine',  label=  '2,2A, 3,5V')
plt.hlines(0.042, -10, 270, color='mediumaquamarine', linestyles='dotted', label='Sättigungsstrom für 2,2A')
plt.plot(u2,i2,'x', color='mediumseagreen',  label=    '2,1A, 3,3V')
plt.hlines(0.02, -10, 270, color='mediumseagreen', linestyles='dotted', label='Sättigungsstrom für 2,1A')
plt.plot(u1,i1,'x', color='g',  label=                 '2,0A, 3,0V')
plt.hlines(0.01, -10, 270, color='g', linestyles='dotted', label='Sättigungsstrom für 2,0A')
plt.ylabel(r'$I$ / mA')
plt.xlabel(r'$U$ / V')
plt.legend(loc='upper left', prop={'size': 6})
plt.grid()
plt.show()
plt.close()


#Is in mA 
#0,010 #0.01
#0,020 #0.02
#0,045 #0.042
#0,100 #0.095
#0,200 #0.19

###################### b ####################
lnIb = np.log(i5[1:]) #ln(mA)
lnUb = np.log(u5[1:])

def fb(x, a, b):
    return a * x + np.log(b)

paramsb, covb = curve_fit(fb, lnUb[0:4], lnIb[0:4])
errb = np.sqrt(np.diag(covb))

xx = np.linspace(2.3, 4, 1000)

print('\n\n', 'zu b)\n a = ', paramsb[0], '\pm', errb[0], '\n b= ', paramsb[1], '\pm', errb[1])
plt.plot(lnUb[0:4], lnIb[0:4], 'x', color='mediumaquamarine', label='Raumladungsgebiet')
plt.plot(lnUb[5:], lnIb[5:], 'gx', label='Sättigungsgebiet')
plt.plot(xx, fb(xx, *paramsb), color ='black', label='Fit')
plt.legend(loc='best')
plt.xlabel(r'$\ln(U/U_0)$')
plt.ylabel(r'$\ln(I/I_0)$')
plt.grid()
plt.show()
#zu b)
# a =  1.120140106777639 \pm 0.02580566625009295 
# b=  0.002757510718960697 \pm 0.0002011777662117039
plt.close()

###################### c #####################
Uc, Ic = np.genfromtxt('b.txt', unpack='true')#I/nA, U/V
Icc = Ic * 1e-9 #I in A
UUc = Uc + 1e6 * Icc
lnIc = np.log(Ic)

print('\n\n', 'zu c)\n Korrigierte Spannungen: ', UUc, 'V')

def fc(x, a, b):
    return a * x + np.log(b)

paramscc, covcc = curve_fit(fc, UUc, lnIc)
errcc = np.sqrt(np.diag(covcc))

xxc = np.linspace(UUc[0], 1, 1000)
print('\nA = ', paramscc[0], '\pm', errcc[0])
print('B = ', paramscc[1], '\pm', errcc[1])
plt.plot(UUc, lnIc, 'gx', label='Messwerte')
plt.plot(xxc, fc(xxc, *paramscc), color ='grey', label='Fit')
plt.xlabel(r'$U \:/\: V$')
plt.ylabel(r'$\ln(I/I_0)$')
plt.legend(loc='best')
plt.grid()
plt.show()
plt.close()

Ac = ufloat(paramscc[0], errcc[0])
Tc = -con.e / (con.k * Ac)
print('\nT = ', Tc)
# zu c)
# Korrigierte Spannungen:  [0.054   0.107   0.1615  0.2169  0.273   0.3298  0.38747 0.44555 0.50415
# 0.56305 0.62225 0.6816  0.7412  0.80086 0.86065 0.92046 0.98033 1.00028] V
#
#A =  -5.075489590949637 \pm 0.04725175784359283
#B =  50.31667997312228 \pm 1.4594726683389092
#T =  2286+/-21

######################### d #################
Ud = np.array([3.0, 3.3, 3.5, 4.0, 4.1])
Id = np.array([2.0, 2.1, 2.2, 2.3, 2.4])
f = 0.35
nn = 0.28
sig = 5.7e-12
T = ((Id * Ud - 0.9)/(f * nn * sig))**(1/4)
print('\n\n', 'zu d) \nT = ', T)
Tmean = ufloat(np.mean(T), stats.sem(T))
print('Durchschnitt T: ', np.mean(T), r'\pm', stats.sem(T))

# zu d) 
#T =  [1738.27030514 1812.60884626 1867.89300329 1963.33446436 2000.13425071]
#Durchschnitt T:  1876.4481739529456 \pm 48.004815997264664

####################### e ##################

#Is in mA 

#0,010 #0.01
#0,020 #0.02
#0,045 #0.042
#0,100 #0.095
#0,200 #0.19
I_s = np.array([0.01, 0.02, 0.042, 0.95, 0.19])#in mA
I_s = I_s * 1e-3 #in A
print('\nT:', T)

W = -np.log((I_s * con.h**3)/(4 * np.pi * con.e * con.m_e * f*1e-4 * con.k**2 * T**2)) * con.k * T #in J
W = W / con.e #6.242e18 #in eV
w_mean = np.mean(W)
w_std = np.std(W)
print('\n\n', 'zu e) \nW = ', W, '\nDurchschnitt = ',w_mean, '\pm' ,w_std)

# zu e) 
#W =  [4.51973815 4.61784201 4.63782766 4.75656624 4.72424343] 
#Durchschnitt =  4.651243498176626 \pm 0.08367935310731033
