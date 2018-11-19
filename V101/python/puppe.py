import numpy as np
from uncertainties import ufloat

massekg = 0.1626

#hkkopf check
rhkkopf = ufloat(15.45 * 10**-3, 0.025 * 10**-3)
vhkkopf = (2/3) * np.pi * rhkkopf**3

#kskopf check
r1kskopf = ufloat(9.075 * 10**-3, 0.025 * 10**-3)
r2kskopf = ufloat(15.45 * 10**-3, 0.025 * 10**-3)
hkskopf = ufloat(35.4 * 10**-3, 0.05 * 10**-3)
vkskopf = (1/3) * np.pi * hkskopf * (r1kskopf**2 + r1kskopf * r2kskopf + r2kskopf**2)

#zhals check
rzhals = ufloat(8 * 10**-3, 0.025 * 10**-3)
hzhals = ufloat(10.7 * 10**-3, 0.05 * 10**-3)
vzhals = np.pi * rzhals**2 * hzhals

#qo1 oberkörper1 check
ho1 = ufloat(49.7 * 10**-3, 0.05 * 10**-3)
bo1 = ufloat(39.45 * 10**-3, 0.05 * 10**-3)
lo1 = ufloat(37 * 10**-3, 0.05 * 10**-3)
vqo1 = lo1 * bo1 * ho1

#zo2 check
rzo2 = ufloat(12.45 * 10**-3, 0.025 * 10**-3)
hzo2 = ufloat(15.15 * 10**-3, 0.05 * 10**-3)
vzo2 = np.pi * rzo2**2 * hzo2

#zo3 check
rzo3 = ufloat(19.1 * 10**-3, 0.025 * 10**-3)
hzo3 = ufloat(35.65 * 10**-3, 0.05 * 10**-3)
vzo3 = np.pi * rzo3**2 * hzo3

#ARME
#karm check
rkarm = ufloat(5.95 * 10**-3, 0.025 * 10**-3)
vkarm = (4/3) * np.pi * rkarm**3

#zarm check
rzarm = ufloat(6 * 10**-3, 0.025 * 10**-3)
hzarm = ufloat(99.15 * 10**-3, 0.05 * 10**-3)
vzarm = np.pi * rzarm**2 * hzarm

#qhand check
hqhand = ufloat(24.7 * 10**-3, 0.05 * 10**-3)
bqhand = ufloat(7.35 * 10**-3, 0.05 * 10**-3)
lqhand = ufloat(12.9 * 10**-3, 0.05 * 10**-3)
vqhand = hqhand * bqhand * lqhand

#BEINE
#kbein check
rkbein = ufloat(6.025* 10**-3, 0.025 * 10**-3)
vkbein = (4/3) * np.pi * rkbein**3

#zb1 check
hzb1 = ufloat(56.8 * 10**-3 , 0.05 * 10**-3)
rzb1 = ufloat(9.35 * 10**-3 ,0.025 * 10**-3)
vzb1 = np.pi * rzb1**2 * hzb1

#zb2 check
hzb2 = ufloat(6.9 * 10**-3 ,0.05 * 10**-3)
rzb2 = ufloat(6.3 * 10**-3 ,0.025 * 10**-3)
vzb2 = np.pi * rzb2**2 * hzb2

#zb3 check
hzb3 = ufloat(61.35 * 10**-3 ,0.05 * 10**-3)
rzb3 = ufloat(8.175 * 10**-3 ,0.025 * 10**-3)
vzb3 = np.pi * rzb3**2 * hzb3

#qfuss 
hqfuss = ufloat(8.6 * 10**-3, 0.05 * 10**-3)
bqfuss = ufloat(15.45 * 10**-3, 0.05 * 10**-3)
lqfuss = ufloat(37.55 * 10**-3, 0.05 * 10**-3)
vqfuss = hqfuss * bqfuss * lqfuss

#volumen
vgesamt = vhkkopf + vkskopf + vzhals + vqo1 + vzo2 + vzo3 + 2*(vkarm + vzarm + vqhand) + 2*(vkbein + vzb1 + vzb2 + vzb3 + vqfuss)

#dichte kg/m³
dichte = massekg/vgesamt

print('V in m³: ')
print('vgesamt = ', vgesamt)
#print('vhkkopf = ', vhkkopf)
#print('vkskopf = ', vkskopf)
#print('vzhals = ', vzhals)
print('VKopf =', vhkkopf+vkskopf+vzhals)
#print('vqo1 = ', vqo1)
#print('vzo2 = ', vzo2)
#print('vzo3 = ', vzo3)
print('VOberkoerper =', vqo1+vzo2+vzo3)
#print('vkarm = ', vkarm)
#print('vzarm = ', vzarm)
#print('vqhand = ', vqhand)
print('VArm =', vkarm+vzarm+vqhand)
#print('vkbein = ', vkbein)
#print('vzb1 = ', vzb1)
#print('vzb2 = ', vzb2)
#print('vzb3 = ', vzb3)
#print('vqfuss = ', vqfuss)
print('VBein =', vkbein+vzb1+vzb2+vzb3+vqfuss)
print('dichte puppe kg/m³ = ', dichte)

#masse test
#mgesamt = dichte * (vhkkopf + vkskopf + vzhals + vqo1 + vzo2 + vzo3 + 2*(vkarm + vzarm + vqhand) + 2*(vkbein + vzb1 + vzb2 + vzb3 + vqfuss))
#print('mgesamt = ', mgesamt)

#massen
mhkkopf = vhkkopf * dichte
mkskopf = vkskopf * dichte
mzhals = vzhals * dichte
mqo1 = vqo1 * dichte
mzo2 = vzo2 * dichte
mzo3 = vzo3 * dichte
mkarm = vkarm * dichte
mzarm = vzarm * dichte
mqhand = vqhand * dichte
mkbein = vkbein * dichte
mzb1 = vzb1 * dichte
mzb2 = vzb2 * dichte
mzb3 = vzb3 * dichte
mqfuss = vqfuss * dichte

print('MKopf =', mhkkopf+mkskopf+mzhals)
print('MOberkoerper =', mqo1+mzo2+mzo3)
print('MArm =', mkarm+mzarm+mqhand)
print('MBein =', mkbein+mzb1+mzb2+mzb3+mqfuss)

def ikugel(r,m):
    i = (2/5) * m * r**2
    return i

def izyl(r, m):
    i = (1/2) * m * r**2
    return i

def iquader(l, b, m):
    i = (1/12) * m * (l**2 + b**2)
    return i

# PUPPE ALLGEMEIN

ihkkopf = 1/2 * ikugel(rhkkopf, mhkkopf) #halbekugel
ikskopf = (3/10) * mhkkopf * (r2kskopf**5-r1kskopf**5)/(r2kskopf**3-r1kskopf**3) #manuell
izhals = izyl(rzhals, mzhals)
iqo1 = iquader(lo1, bo1, mqo1)
izo2 = izyl(rzo2, mzo2)
izo3 = izyl(rzo3, mzo3)
ikarm = ikugel(rkarm, mkarm)
izarm = izyl(rzarm, mzarm)
iqhand = iquader(lqhand, bqhand, mqhand)
ikbein = ikugel(rkbein, mkbein)
izb1 = izyl(rzb1, mzb1)
izb2 = izyl(rzb2, mzb2)
izb3 = izyl(rzb3, mzb3)
iqfuss = iquader(lqfuss, bqfuss, mqfuss)

# PUPPE1
akarm1 = ufloat(25.675 * 10**-3, 0.05 * 10**-3)
azarm1 = ufloat(25.75 * 10**-3, 0.05 * 10**-3)
aqhand1 = ufloat(25.75 * 10**-3, 0.05 * 10**-3)
akbein1 = ufloat(13.075 * 10**-3, 0.05 * 10**-3)
azb11 = ufloat(13.075 * 10**-3, 0.05 * 10**-3)
azb21 = ufloat(13.075 * 10**-3, 0.05 * 10**-3)
azb31 = ufloat(13.075 * 10**-3, 0.05 * 10**-3)
aqfuss1 = ufloat(13.075 * 10**-3, 0.05 * 10**-3)


ikarm1 = ikarm + akarm1**2 * mkarm
izarm1 = izarm + azarm1**2 * mzarm
iqhand1 = iqhand + aqhand1**2 * mqhand
ikbein1 = ikbein + akbein1**2 * mkbein
izb11 = izb1 + azb11**2 * mzb1
izb21 = izb2 + azb21**2 * mzb2
izb31 = izb3 + azb31**2 * mzb3
iqfuss1 = iqfuss + aqfuss1**2 * mqfuss

igesamt1 = ihkkopf + ikskopf + izhals + iqo1 + izo2 + izo3 + 2*(ikarm1 + izarm1 + iqhand1) + 2*(ikbein1 + izb11 + izb21 + izb31 + iqfuss1)

print('i1 gesamt: ', igesamt1)

# PUPPE2
akarm2 = ufloat(25.675 * 10**-3, 0.05 * 10**-3)
azarm2 = ufloat(81.2 * 10**-3, 0.05 * 10**-3)
aqhand2 = ufloat(143.125 * 10**-3, 0.05 * 10**-3)
akbein2 = ufloat(13.075 * 10**-3, 0.05 * 10**-3)
azb12 = ufloat(36.82 * 10**-3, 0.05 * 10**-3)
azb22 = ufloat(67.55 * 10**-3, 0.05 * 10**-3)
azb32 = ufloat(101.25 * 10**-3, 0.05 * 10**-3)
aqfuss2 = ufloat(136 * 10**-3, 0.05 * 10**-3)

ikarm2 = ikarm1
izarm2 = mzarm * ((rzarm**2)/(4) + (hzarm**2)/(12)) + azarm2**2 * mzarm
iqhand2 = iquader(hqhand, bqhand, mqhand) + aqhand2**2 * mqhand
ikbein2 = ikbein1
izb12 = mzb1 * ((rzb1**2)/(4) + (hzb1**2)/(12)) + azb12**2 * mzb1
izb22 = mzb2 * ((rzb2**2)/(4) + (hzb2**2)/(12)) + azb22**2 * mzb2
izb32 = mzb3 * ((rzb3**2)/(4) + (hzb3**2)/(12)) + azb32**2 * mzb3
iqfuss2 = iquader(hqfuss, bqfuss, mqfuss) + aqfuss2**2 * mqfuss

igesamt2 = ihkkopf + ikskopf + izhals + iqo1 + izo2 + izo3 + 2*(ikarm2 + izarm2 + iqhand2) + 2*(ikbein2 + izb12 + izb22 + izb32 + iqfuss2)

print('i2 gesamt: ', igesamt2)