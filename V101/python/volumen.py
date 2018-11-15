import numpy as np
from uncertainties import ufloat
#in millimetern, also *10⁻3

#massepuppe
massekg = 0.1626

#volumen kopf
rkopf = ufloat(15.45, 0.05)
vkopf = (4/3) * np.pi * rkopf**3

#volumen oberkörper1
ho1 = ufloat(49.7, 0.05)
bo1 = ufloat(39.45, 0.05)
lo1 = ufloat(37, 0.05)
vo1 = lo1 * bo1 * ho1

#vol oberkörper2
ro2 = ufloat(12.45, 0.05)
ho2 = ufloat(15.15, 0.05)
vo2 = np.pi * ro2**2 * ho2

#vol oberkörper 3
ro3 = ufloat(19.1, 0.05)
ho3 = ufloat(35.65, 0.05)
vo3 = np.pi * ro3**2 * ho3

#vol oberkörper gesamt
vo = vo1 + vo2 + vo3

#vol bein
hbein = ufloat(139.7, 0.05)
rbein = ufloat(8.80, 0.05)
vbein = np.pi * rbein**2 * hbein

#vol arm
harm = ufloat(123.85, 0.05)
rarm = ufloat(6, 0.05)
varm = np.pi * rarm**2 * harm

#vol gesamt
vgesamt = vkopf + vo + vbein*2 + varm*2

#vol gesamt in m³
vgmeter = vgesamt * 10**(-9)

#dichte kg/m³
dichte = massekg/vgmeter

print('dichte puppe kg/m³ = ', dichte)

#umrechnung vol in m³
vmkopf = vkopf * 10**-9
vmo1 = vo1 * 10**-9
vmo2 = vo2 * 10**-9
vmo3 = vo3 * 10**-9
vmbein = vbein * 10**-9
vmarm = varm * 10**-9

print('V in m³: ')
print('vmkopf = ', vmkopf) #kugel
print('vmo1 = ', vmo1) #quader
print('vmo2 = ', vmo2) #zyl
print('vmo3 = ', vmo3) #zyl
print('vmbein = ', vmbein) #zyl
print('vmarm = ', vmarm) #zyl

massen = np.array([vmkopf, vmo1, vmo2, vmo3, vmbein, vmarm]) * dichte
print('Massen (kopf,oberkörper 1 bis 3, bein, arm): ', massen)

def ikugel(r,m):
    i = (2/5) * m * r**2
    return i

def izyl(r, m):
    i = (1/2) * m * r**2
    return i

def iquader(l, b, m):
    i = (1/12) * m * (l**2 + b**2)
    return i

print('Trägheitsmomente I:')

ikopf = ikugel((rkopf*10**-3), (vmkopf*dichte))
print('Ikopf: ', ikopf)

io1 = iquader((lo1*10**-3), (bo1*10**-3), (vmkopf*dichte))
print('Io1: ', io1)

io2 = izyl(ro2*10**-3, vmo2*dichte)
print('Io2: ', io2)

io3 = izyl(ro3*10**-3, vmo3*dichte)
print('Io3: ', io3)

# + steiner
ibein = izyl(rbein*10**-3, vmbein*dichte) + vmbein*dichte * (7.05*10**-3)**2
print('Ibein: ', ibein)

# + steiner
iarm = izyl(rarm*10**-3, vmarm*dichte) + vmarm*dichte * (25.75*10**-3)**2
print('Iarm: ', iarm)

igesamt = ikopf + io1 + io2 + io3 + 2*ibein + 2*iarm
print('Summe: Igesamt: ', igesamt)