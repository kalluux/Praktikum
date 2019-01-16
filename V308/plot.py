import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.constants as const
from scipy.optimize import curve_fit

#plt.savefig('build/plot.pdf')

#HELMHOLTZ

#Spulenabstand d = 11.5 cm

# I = 5A, Abstände in m !!!
abstaende = np.array( [0, 0.005, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040, 0.045, 0.050, 0.055, 0.115, 0.120, 0.125, 0.130, 0.135]) 
B5A = np.array([0.004700 ,0.004561 ,0.004423 ,0.004313 ,0.004236 ,0.004195 ,0.004199 ,0.004241 ,0.004320 ,0.004438 ,0.004581 ,0.004737 ,0.003950 ,0.003615 ,0.003307 ,0.002995 ,0.002710]) 

# I = 3A, Abstände s. 5A !!!
B3A = np.array([0.002846, 0.002760, 0.002689, 0.002613, 0.002566, 0.002545, 0.002548, 0.002576, 0.002626, 0.002696, 0.002780, 0.002877, 0.002388, 0.002196, 0.002007, 0.00181, 0.001639]) 

#Spulenabstand r = 6.25 cm, I = 5A

BR5A = [ 0.007056, 0.007062, 0.007062, 0.007061, 0.007063, 0.007061, 0.007060, 0.004788, 0.004412, 0.004012, 0.003656, 0.003308 ] 
BR5A_h = [0.007056, 0.007062, 0.007062, 0.007061, 0.007063, 0.007061, 0.007060] #_h = Bereich mit homogenem Magnetfeld
abstaendeR_h = [ 0, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006]
abstaendeR = [0, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.060, 0.065, 0.070, 0.075, 0.080 ] 

#LANGE GERADE SPULE

BLS = [0.000065, 0.000079, 0.000096, 0.000125, 0.000172, 0.000257, 0.000417, 0.000700, 0.001209, 0.002010, 0.002611, 0.002941, 0.003108, 0.003182, 0.003221, 0.003243, 0.003253, 0.003252, 0.003243, 0.003222 ]
abstaendeLS = [-0.07, -0.06, -0.05, -0.04, -0.03, -0.02, -0.01, 0    , 0.01 , 0.02 , 0.03 , 0.04 , 0.05 , 0.06 , 0.07 , 0.08 , 0.09 , 0.10 , 0.11 , 0.12]

#KURZE GERADE SPULE 

BKS = [0.000056, 0.000067, 0.000084, 0.000107, 0.000152, 0.000231, 0.000394, 0.000764, 0.001289, 0.002049, 0.002518, 0.002685, 0.002570, 0.002053, 0.001355 ]
abstaendeKS = [-0.07, -0.06 , -0.05 , -0.04 , -0.03 , -0.02 , -0.01 , 0     , 0.01  , 0.02  , 0.03  , 0.04  , 0.05  , 0.06  , 0.07]   

#HYSTERESE

I = np.array( [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

BHY = [0.0020, 0.1087, 0.2738, 0.3997, 0.4787, 0.5366, 0.5827, 0.6194, 0.6496, 0.6774, 0.7030, 0.6866, 
    0.6695, 0.6496, 0.6259, 0.5980, 0.5631, 0.5170, 0.4572, 0.3342, 0.1224, 
    -0.0789, -0.2544, -0.3848, -0.4727, -0.5322, -0.5791, -0.6152, -0.6466, -0.6745, -0.6997, -0.6838, -0.6668, -0.6460, -0.6232, 
    -0.5956, -0.5613, -0.5171, -0.4548, -0.3308, -0.1188, 0.0819, 0.2512, 0.3876, 0.4751, 0.5331, 0.5779, 0.6149, 0.6449, 0.6725, 0.6982]

#PLOTS

#HYSTERESEKURVE

#Äußeres Magnetfeld
N = 595
r = 0.13 

H = (I * N) / (2*np.pi * r)  #Berechnung der äußeren Feldes einer Toroidspule

plt.plot(H, BHY, 'r', linewidth = 0.9, label = r'$Hysteresekurve$')

xdata = np.linspace(-8000,8000,10000)
ydata = np.linspace(-0.75, 0.75, 10000)
plt.plot(xdata, 0+xdata*0, 'black', linewidth = 0.7)
plt.plot(0+0*ydata, ydata, 'black', linewidth = 0.7)

plt.annotate(r'$Koerzitivfeldstärke$', xy=(-461.29, 0), xytext=(-6000, 0.3),
           arrowprops=dict(facecolor='black', shrink=0.05, width = 0.7, headwidth = 5.6))

plt.legend()
plt.xlabel(r'$H \,/\, \mathrm{Am^{-1}}$')
plt.ylabel(r'$B \,/\, \mathrm{T}$')
plt.grid()
plt.savefig('build/hysterese.pdf')
plt.close()

#HELMHOLTZ

def helmholtzeinzel(i, r, x, n, v):          # v (und u bei überlagert) geben die Verschiebung der Spulenposition auf der Achse an.  
    return (const.mu_0 * i * n)/(2) * r**2/(r**2 + (x+v)**2)**(3/2)    # Linke Spule bei 0, aber Spulenbreite beachten! (s. bei d =11.5 cm, v = 0.033)
    

#def helmholtzMittelpunkt(i, r, x, n):
#    return (const.mu_0 * i * r**2 * n) / (r**2 + (x-0.03125)**2)**(3/2)  #merkwürdig

def helmholtzüberlagert(i,r,x,n, v, u):
    return (const.mu_0 * i * n)/(2) * r**2/(r**2 + (x+v)**2)**(3/2) + (const.mu_0 * i * n)/(2) * r**2/(r**2 + (x+u)**2)**(3/2)

def weltformel(a, i, r, n, l):   #a: Punkt entlang der x-Achse, l:Länge der Spule
    return  (const.mu_0 * i * n) / (2 * l) * ( (a) / (np.sqrt(r**2 + (a)**2)) + (l - a) / (np.sqrt(r**2 + (l-a)**2))) 

def weltformelFIT(a, i, r, l, v):   #a: Punkt entlang der x-Achse, l:Länge der Spule
    return  (const.mu_0 * i * 300) / (2 * l) * ( (a+v) / (np.sqrt(r**2 + (a+v)**2)) + (l - (a+v)) / (np.sqrt(r**2 + (l-(a+v))**2))) 

#Abstand d = 11.5cm

plt.plot(abstaende , B5A, 'rx', label = r'$5A$') #Messwerte eintragen
plt.plot(abstaende , B3A, 'bx', label = r'$3A$')

x_plot = np.linspace(-0.050, 0.135, 10000)
x_plot1 = np.linspace(0, 0.135, 10000) #x-Koordinaten für rechte Spule

plt.plot(x_plot, helmholtzeinzel(5, 0.0625, x_plot, 100, 0.033), 'g--',alpha = 0.5) #Für 5A
plt.plot(x_plot1, helmholtzeinzel(5, 0.0625, x_plot1, 100, -0.115+0.033), 'g--',alpha = 0.5)
plt.plot(x_plot, helmholtzüberlagert(5, 0.0625, x_plot, 100, 0.033, -0.115+0.033), 'black', label = r'$Spulenpaar \,bei\, 5A$')

plt.plot(x_plot, helmholtzeinzel(3, 0.0625, x_plot, 100, 0.033), 'b--', alpha = 0.5) #Für 3A
plt.plot(x_plot1, helmholtzeinzel(3, 0.0625, x_plot1, 100, -0.115+0.033), 'b--', alpha = 0.5)
plt.plot(x_plot, helmholtzüberlagert(3, 0.0625, x_plot, 100, 0.033, -0.115+0.033), 'black', label = r'$Spulenpaar \,bei\, 3A$')

#plt.bar(-0.01, 0.007, width = 0.033, color = 'grey')
#plt.bar(0.0725, 0.007, width = 0.033, color = 'grey')

plt.legend(loc = 'lower left')
plt.xlabel(r'$x \,/\, \mathrm{cm}$')
plt.ylabel(r'$B \,/\, \mathrm{mT}$')

plt.xticks([-0.050, -0.025, 0,  0.025, 0.050, 0.075, 0.100, 0.125],
           ['-5', '-2.5', '0', '2.5', '5', '7.5', '10', '12.5'])
plt.yticks([0, 0.001,0.002,0.003,0.004,0.005],
            ['0', '1', '2', '3', '4','5'])


plt.grid()
plt.savefig('build/helmholtzD.pdf')
plt.close()

#Abstand r = 6.25 cm
plt.plot(abstaendeR_h, BR5A_h, 'rx', label = '5A') #Messwerte eintragen
params, cov = np.polyfit(abstaendeR_h, BR5A_h, deg = 0, cov = True)
x_plot = np.linspace(0,0.006, 1000)
plt.plot(x_plot, params[0]+0*x_plot, 'b', label = r'$Ausgleichsgerade$')

errors = np.sqrt(np.diag(cov))

print('Fehler zoomdatei: ', errors[0])

plt.xticks([0,0.001,0.002,0.003,0.004,0.005,0.006],
            ['0','1','2','3','4','5','6'])

plt.yticks([0.007,0.00702, 0.00704, 0.00706, 0.00708, 0.00710],
           [r"$7$", r"$7.02$", r"$7.04$", r"$7.06$", r"$7.08$",r"$7.1$"])
plt.xlabel(r'$x \,/\, \mathrm{mm}$')
plt.ylabel(r'$B \,/\, \mathrm{mT}$')

plt.ylim(0.007,0.0071)

plt.savefig('build/zoom.pdf')
plt.close()

plt.plot(abstaendeR, BR5A, 'rx', label = '5A') #Messwerte eintragen

params, cov = np.polyfit(abstaendeR_h, BR5A_h, deg = 0, cov = True)
x_plot = np.linspace(0,0.006, 1000)
plt.plot(x_plot, params[0]+0*x_plot, 'b', label = r'$Ausgleichsgerade$')

print('Ausgleichsgerade Helmholtz Parameter: ', params[0])

x_plot1 = np.linspace(-0.06, 0.08, 10000)
plt.plot(x_plot1, helmholtzüberlagert(5, 0.0625, x_plot1, 100, 0.033, -0.0625+0.033 ), label = r'$Magnetfeld \, Spulenpaar$')

plt.xticks([-0.06,-0.04,-0.02,0,0.02,0.04,0.06,0.08],
            ['-6','-4','-2','0','2','4','6','8'])

plt.yticks([0.003,0.004,0.005,0.006,0.007],
            ['3','4','5','6','7'])

plt.legend()
plt.xlabel(r'$x \,/\, \mathrm{cm}$')
plt.ylabel(r'$B \,/\, \mathrm{mT}$')
plt.savefig('build/helmholtzR.pdf')
plt.close()

#LANGE SPULE


plt.plot(abstaendeLS, BLS, 'rx', label = r'$Gemessene \, Magnetfeldstärken$') #Messwerte eintragen

#x_plot = np.linspace(-0.07, 0.12, 10000)
#plt.plot(x_plot, weltformel(x_plot-0.017, 1.74, 0.0205, 300, 0.20), 'b--', label = r'$Theoriekurve$') #Theoriekurve
# KOMMENTAR: Graph künstlich rechtsverschoben, deutlich erhöhter Strom! Passt aber so.

x_plot1 = np.linspace(0, 0.12, 1000)
#B_h = (const.mu_0 * 300 * 1.2) / 0.19
#plt.plot(x_plot1, B_h+0*x_plot1, 'b--', label = 'Theorie Spuleninneres') #Theorie im Spuleninneren

#Fit
params, cov = curve_fit(weltformelFIT, abstaendeLS, BLS, p0 = (1.2, 0.0205, 0.19, -0.017 ) )
xplot = np.linspace(-0.07, 0.12, 1000)
plt.plot(xplot, weltformelFIT(xplot, *params), label = r'$Ausgleichskurve$')

ydata = np.linspace(0,0.0035,1000)
plt.plot(0+0*ydata, ydata, 'black', alpha = 0.8)
plt.annotate(r'$Spulenanfang$', xy=(0, 0.002), xytext=(0.001, 0.0034))
         # arrowprops=dict(facecolor='black', shrink=0.05, width = 0.7, headwidth = 0.7))

print('I = ', params[0],
    'R = ', params[1],
    'L = ', params[2],
    'V = ', params[3])

errors = np.sqrt(np.diag(cov))


print('Fehler: ' , 
    'I = ', errors[0],
    'R = ', errors[1],
    'L = ', errors[2],
    'V = ', errors[3] )

plt.xticks([-0.075,-0.050,-0.025, 0, 0.025, 0.050,0.075,0.100,0.125],
            ['-7.5','-5','- 2.5','0','2.5','5','7.5','10','12.5'])
plt.yticks([0,0.0005,0.0010,0.0015,0.0020,0.0025,0.0030,0.0035],
            ['0','0.5','1','1.5','2','2.5','3','3.5'])


plt.legend(loc = 'lower right')
plt.xlabel(r'$x \,/\, \mathrm{cm}$')
plt.ylabel(r'$B \,/\, \mathrm{mT}$')
plt.grid()
plt.savefig('build/spule_lang.pdf')
plt.close()

#KURZE SPULE 
plt.plot(abstaendeKS, BKS, 'rx', label = r'$Gemessene Magnetfeldstärken$')

x_plot = np.linspace(-0.07, 0.07, 1000) #THEORIE
plt.plot(x_plot, weltformel(x_plot - 0.017, 1.3, 0.0205, 100, 0.045), 'b--', label = r'$Theoriekurve$')

#params, cov = curve_fit(weltformel, abstaendeKS, BKS, p0 = (1.3, 0.0205, 100, 0.045)) #FIT
#plt.plot(xplot, weltformel(x_plot, *params), 'g--', label = 'Fit')

plt.xticks([-0.06,-0.04,-0.02,0,0.02,0.04,0.06],
            ['-6','-4','-2','0','2','4','6'])
plt.yticks([0,0.0005,0.001,0.0015,0.002,0.0025],
            ['0','0.5','1','1.5','2','2.5'])

plt.legend(loc = 'lower right')
plt.xlabel(r'$x \,/\, \mathrm{cm}$')
plt.ylabel(r'$B \,/\, \mathrm{mT}$')
plt.savefig('build/spule_kurz.pdf')
plt.close()