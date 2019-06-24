import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as con
from scipy.optimize import curve_fit
from scipy import stats
from uncertainties import ufloat

def f(x, a, b):
    return a * x + b

##################### TEIL 1 #######################

# GELB

print('\n\nGELB')
Uge, Ige = np.genfromtxt('gelb.txt', unpack=True)
Ige = np.sqrt(Ige)

paramsge, covge = curve_fit(f, Uge, Ige)
errge = np.sqrt(np.diag(covge))

print('a = ', paramsge[0], r'\pm', errge[0])
print('b = ', paramsge[1], r'\pm', errge[1])

UGge = - (ufloat(paramsge[1], errge[1]) / ufloat(paramsge[0], errge[0]))
print('Grenzspannung Ug = ', UGge)

xge = np.linspace(-0.025, unp.nominal_values(UGge)+0.1, 1000)

plt.plot(Uge, Ige, 'kx', label='Messwerte')
plt.plot(xge, f(xge, *paramsge), color='#f4b642', label='Fit')
plt.xlabel(r'$U \:/\: $V')
plt.ylabel(r'$\sqrt{I} \:\mathrm{/\: \sqrt{nA}}$')
plt.grid(True)
plt.legend(loc='best')
#plt.show()
plt.savefig('gelb.pdf')
plt.close()

# GRUEN

print('\n\nGRUEN')
Ugr, Igr = np.genfromtxt('gruen.txt', unpack=True)
Igr = np.sqrt(Igr)

paramsge, covge = curve_fit(f, Ugr, Igr)
errge = np.sqrt(np.diag(covge))

print('a = ', paramsge[0], r'\pm', errge[0])
print('b = ', paramsge[1], r'\pm', errge[1])

UGgr = - (ufloat(paramsge[1], errge[1]) / ufloat(paramsge[0], errge[0]))
print('Grenzspannung Ug = ', UGgr)

xgr = np.linspace(-0.025, unp.nominal_values(UGgr)+0.1, 1000)

plt.plot(Ugr, Igr, 'kx', label='Messwerte')
plt.plot(xgr, f(xgr, *paramsge), color='#6bb200', label='Fit')
plt.xlabel(r'$U \:/\: $V')
plt.ylabel(r'$\sqrt{I} \:\mathrm{/\: \sqrt{nA}}$')
plt.grid(True)
plt.legend(loc='best')
#plt.show()
plt.savefig('gruen.pdf')
plt.close()


# BLAUGRUEN


print('\n\nBLAUGRUEN')
Ubg, Ibg = np.genfromtxt('blaugruen.txt', unpack=True)
Ibg = np.sqrt(Ibg)

paramsge, covge = curve_fit(f, Ubg, Ibg)
errge = np.sqrt(np.diag(covge))

print('a = ', paramsge[0], r'\pm', errge[0])
print('b = ', paramsge[1], r'\pm', errge[1])

UGbg = - (ufloat(paramsge[1], errge[1]) / ufloat(paramsge[0], errge[0]))
print('Grenzspannung Ug = ', UGbg)

xbg = np.linspace(-0.025, unp.nominal_values(UGbg)+0.1, 1000)

plt.plot(Ubg, Ibg, 'kx', label='Messwerte')
plt.plot(xbg, f(xbg, *paramsge), color='#15d8a4', label='Fit')
plt.xlabel(r'$U \:/\: $V')
plt.ylabel(r'$\sqrt{I} \:\mathrm{/\: \sqrt{nA}}$')
plt.grid(True)
plt.legend(loc='best')
#plt.show()
plt.savefig('blaugruen.pdf')
plt.close()


# VIOLETT1

print('\n\nVIOLETT1')
Uv1, Iv1 = np.genfromtxt('violett.txt', unpack=True)
Iv1 = np.sqrt(Iv1)

paramsv1, covv1 = curve_fit(f, Uv1, Iv1)
errv1 = np.sqrt(np.diag(covv1))

print('a = ', paramsv1[0], r'\pm', errv1[0])
print('b = ', paramsv1[1], r'\pm', errv1[1])

UGv1 = - (ufloat(paramsv1[1], errv1[1]) / ufloat(paramsv1[0], errv1[0]))
print('Grenzspannung Ug = ', UGv1)

xv1 = np.linspace(-0.025, unp.nominal_values(UGv1)+0.1, 1000)

plt.plot(Uv1, Iv1, 'kx', label='Messwerte')
plt.plot(xv1, f(xv1, *paramsv1), color='#7289da', label='Fit')
plt.xlabel(r'$U \:/\: $V')
plt.ylabel(r'$\sqrt{I} \:\mathrm{/\: \sqrt{nA}}$')
plt.grid(True)
plt.legend(loc='best')
#plt.show()
plt.savefig('violett1.pdf')
plt.close()


# VIOLETT2

print('\n\nVIOLETT2')
Uv2, Iv2 = np.genfromtxt('violett2.txt', unpack=True)
Iv2 = np.sqrt(Iv2)

paramsv2, covv2 = curve_fit(f, Uv2, Iv2)
errv2 = np.sqrt(np.diag(covv2))

print('a = ', paramsv2[0], r'\pm', errv2[0])
print('b = ', paramsv2[1], r'\pm', errv2[1])

UGv2 = - (ufloat(paramsv2[1], errv2[1]) / ufloat(paramsv2[0], errv2[0]))
print('Grenzspannung Ug = ', UGv2)

xv2 = np.linspace(-0.025, unp.nominal_values(UGv2)+0.1, 2000)

plt.plot(Uv2, Iv2, 'kx', label='Messwerte')
plt.plot(xv2, f(xv2, *paramsv2), color='#863ded', label='Fit')
plt.xlabel(r'$U \:/\: $V')
plt.ylabel(r'$\sqrt{I} \:\mathrm{/\: \sqrt{nA}}$')
plt.grid(True)
plt.legend(loc='best')
#plt.show()
plt.savefig('violett2.pdf')
plt.close()

#################### Plot Grenzspannungen ##########

print('\n\n\nPLOT GRENZSPANNUNG')

U1 = unp.uarray([unp.nominal_values(UGge), unp.nominal_values(UGgr), unp.nominal_values(UGbg),
unp.nominal_values(UGv1), unp.nominal_values(UGv2)], [unp.std_devs(UGge), unp.std_devs(UGgr),
unp.std_devs(UGbg), unp.std_devs(UGv1), unp.std_devs(UGv2)])

gelb = np.array([579.1, 577.0])
violett1 = np.array([435.8, 434.7])
violett2 = np.array([407.8, 404.7])

l = np.array([np.mean(gelb), 546, 491.6, np.mean(violett1), np.mean(violett2)])

nu = con.c / (l * 10**(-9))

print('\nFit')
paramsGallb, covGallb = curve_fit(f, nu / 10**(14), unp.nominal_values(U1))
errGallb = np.sqrt(np.diag(covGallb))
print('a = ', paramsGallb[0] * 10, r'\pm', errGallb[0] * 10)
print('b = ', paramsGallb[1], r'\pm', errGallb[1])

xG = np.linspace(380992264928556.4 / 10**(14)-0.2, 8.5, 1000)


plt.plot(xG, f(xG, *paramsGallb), '--', color='#000000', label='Fit')
plt.errorbar(nu / 10**(14), unp.nominal_values(U1), yerr=unp.std_devs(U1), fmt='g.', capsize=2, label='Fehlerbehaftete Messwerte')
plt.grid(True)
plt.legend(loc='best')
plt.xlabel(r'$\nu \:/\: 10^{14}\,$Hz')
plt.ylabel(r'$U_\mathrm{G} \:/\: $V')
#plt.show()
plt.savefig('grenz.pdf')
plt.close()

####################### TEIL 2 ###################

#GELB 2 
U2, I2 = np.genfromtxt('gelb2.txt', unpack=True)

plt.plot(U2, I2, 'x', label='Messwerte')
plt.xlabel(r'$U \:/\: $V')
plt.ylabel(r'$I \:/\: $nA')
plt.grid(True)
plt.savefig('gelb2.pdf')
plt.close()


#AUSGABE:
#GELB
#a =  -1.1224418381841559 \pm 0.01664073986057484
#b =  0.6290951699311398 \pm 0.004922652914366159
#Grenzspannung Ug =  0.560+/-0.009
#
#
#GRUEN
#a =  -0.9367476581439225 \pm 0.017046771724341356
#b =  0.5459414676157502 \pm 0.005043550742957911
#Grenzspannung Ug =  0.583+/-0.012
#
#
#BLAUGRUEN
#a =  -0.2578222876852573 \pm 0.008849594880019875
#b =  0.20704260733525184 \pm 0.0026182893409581343
#Grenzspannung Ug =  0.803+/-0.029
#
#
#VIOLETT1
#a =  -0.8364540518239221 \pm 0.016767794388495273
#b =  0.9506425342220014 \pm 0.008952180768376184
#Grenzspannung Ug =  1.137+/-0.025
#
#
#VIOLETT2
#a =  -0.5951991178883578 \pm 0.002522900844542432
#b =  0.7754581762869285 \pm 0.0017911465254093891
#Grenzspannung Ug =  1.303+/-0.006
#
#
#
#PLOT GRENZSPANNUNG
#
#Fit
#a =  3.5766205114373606 \pm 0.2284043489640486
#b =  -1.3434145545459109 \pm 0.14305252091013726
#