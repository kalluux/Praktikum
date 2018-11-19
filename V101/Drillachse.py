import numpy as np 
from uncertainties import ufloat
import math
import uncertainties.unumpy as unp

#Winkelrichtgröße

F = np.array([0.46,0.26,0.62,0.39,0.80,0.48,0.94,0.57,1.10,0.66])
W = np.array([30,30,40,40,50,50,60,60,70,70])
#r = np.array([0.02965,0.04945,0.02965,0.04945,0.02965,0.04945,0.02965,0.04945,0.02965,0.04945])
r1 = ufloat(0.02965,0.00005)
r2 = ufloat(0.04945,0.00005)
r = np.array([r1,r2,r1,r2,r1,r2,r1,r2,r1,r2])

D = F*r/W
#print(D)

Dmittel = np.mean(D)
#print(Dmittel)

#trägheitsmoment drillachse

m = ufloat(592.91362861,11.52390938)
b = ufloat(4.39487838,0.35911135)

m1 = 0.2218
d1 = ufloat(0.03475, 0.00005)
h1 = ufloat(0.0297, 0.00005)
m2 = 0.2225

Izy1 = m1*((((d1/2)**2)/4)+((h1**2)/12))
Izy2 = m2*((((d1/2)**2)/4)+((h1**2)/12))

#print(Izy1)
#print(Izy2)
Izy = Izy1+Izy2
#print(Izy)


Idrill = ((b*Dmittel)/(4*(np.pi**2)))-Izy
#print(Idrill)


# Trägheitsmoment Kugel

mk = 0.8123
dk = ufloat(0.13755, 0.00005)
Ik = 2/5 * mk * ((dk/2)**2)
#print(Ik)

s1 = ufloat(1.47, 0.0625)
s2 = ufloat(1.45, 0.0625)
s3 = ufloat(1.48, 0.0625)
s4 = ufloat(1.44, 0.0625)
s5 = ufloat(1.46, 0.0625)
s = np.array([s1,s2,s3,s4,s5])
ss = np.mean(s)
#print(ss)

Ikugel = (((ss**2)*Dmittel)/(4*((np.pi)**2)))
#print(Ikugel)

#zylinder


t1 = ufloat(0.7222,0.1)
t2 = ufloat(0.7464,0.1)
t3 = ufloat(0.7394,0.1)
t4 = ufloat(0.7418,0.1)
t5 = ufloat(0.7360,0.1)
t = np.array([t1,t2,t3,t4,t5])
tt = np.mean(t)
#print(tt)

mz = 0.3684
dz = ufloat(0.0973,0.00005)
hz = ufloat(0.101,0.00005)
Iz = (mz*((dz/2)**2))/2
#print(Iz)

Izylinder = (((tt**2)*Dmittel)/(4*((np.pi)**2)))
#print(Izylinder)



#puppe

sch1 = ufloat(0.3378,0.1)
sch2 = ufloat(0.3480,0.1)
sch3 = ufloat(0.3576,0.1)
sch4 = ufloat(0.3836,0.1)
sch5 = ufloat(0.3478,0.1)
schw = np.array([sch1,sch2,sch3,sch4,sch5])
schww = np.mean(schw)
print(schww)
Ip1 = (((schww**2)*Dmittel)/(4*((np.pi)**2)))
print(Ip1)


p1 = ufloat(0.8497,0.05)
p2 = ufloat(0.8485,0.05)
p3 = ufloat(0.8395,0.05)
p4 = ufloat(0.8510,0.05)
p5 = ufloat(0.8572,0.05)
pe = np.array([p1,p2,p3,p4,p5])
pep = np.mean(pe)
print(pep)
Ip2 = (((pep**2)*Dmittel)/(4*((np.pi)**2)))
print(Ip2)









#Zylinder

Iz = 1/2 * 0.3684*(0.04865**2)
#print(Iz)










