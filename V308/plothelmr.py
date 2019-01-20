import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

mu0 = 4 * np.pi * 10**(-7)

#HELMHOLTZ

#Spulenabstand d = 6.25 cm

# I = 2A, Abstände in m !!!
abstaende = np.array( [0.028, 0.029, 0.03, 0.031, 0.032, 0.033, 0.034, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14]) 
B4A = np.array([0.002724, 0.002728, 0.002729, 0.002729, 0.002729, 0.002729, 0.002728, 0.00138, 0.00146, 0.00117, 0.000901, 0.000701, 0.000544]) 


def helmholtzeinzel(i, r, x, n, v):          # v (und u bei überlagert) geben die Verschiebung der Spulenposition auf der Achse an.  
    return (mu0 * i * n)/(2) * r**2/(r**2 + (x+v)**2)**(3/2)    # Linke Spule bei 0, aber Spulenbreite beachten! (s. bei d =11.5 cm, v = 0.033)


def helmholtzüberlagert(i,r,x,n, v, u):
    return (mu0 * i * n)/(2) * r**2/(r**2 + (x+v)**2)**(3/2) + (mu0 * i * n)/(2) * r**2/(r**2 + (x+u)**2)**(3/2)

def weltformel(a, i, r, n, l):   #a: Punkt entlang der x-Achse, l:Länge der Spule
    return  (mu0 * i * n) / (2 * l) * ( (a) / (np.sqrt(r**2 + (a)**2)) + (l - a) / (np.sqrt(r**2 + (l-a)**2)))


#PLOT
plt.plot(abstaende , B4A, 'rx', label = 'Messwerte') #Messwerte eintragen

x_plot = np.linspace(-0.050, 0.2, 10000)
x_plot1 = np.linspace(-0.05, 0.2, 10000) #x-Koordinaten für rechte Spule

plt.plot(x_plot, helmholtzeinzel(2, 0.0625, x_plot, 100, 0.033-0.035), 'r--',alpha = 0.5) #Für 4A
plt.plot(x_plot1, helmholtzeinzel(2, 0.0625, x_plot1, 100, -0.115+0.033-0.035+0.05), 'r--',alpha = 0.5)
plt.plot(x_plot1, helmholtzüberlagert(2, 0.0625, x_plot1, 100, 0.033-0.035, -0.0625+0.033-0.035 ), 'black', label = 'Theoriekurve')

plt.xticks([-0.050, -0.025, 0,  0.025, 0.050, 0.075, 0.100, 0.125, 0.15, 0.175, 0.2],
           ['-5', '-2.5', '0', '2.5', '5', '7.5', '10', '12.5', '15', '17.5', '20'])
plt.yticks([0, 0.001,0.002,0.003,0.004,0.005],
            ['0', '1', '2', '3', '4','5'])
          
plt.xlabel('$x$ / cm')
plt.ylabel('$B$ / mT')
plt.legend(loc = 'lower left')
plt.grid()
plt.show()
plt.savefig('helmholtzR.pdf')