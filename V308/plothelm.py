import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

mu0 = 4 * np.pi * 10**(-7)

#HELMHOLTZ

#Spulenabstand d = 11.5 cm

# I = 4A, Abstände in m !!!
abstaende = np.array( [0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.15, 0.16, 0.17, 0.18, 0.19]) 
B4A = np.array([0.003515, 0.003258, 0.003074, 0.003004, 0.003073, 0.003255, 0.003525, 0.003256, 0.002761, 0.002786, 0.001865, 0.001506]) 

# I = 2A, Abstände s. 4A !!!
B2A = np.array([0.0017, 0.001565, 0.00147, 0.001435, 0.001466, 0.001557, 0.001694, 0.001541, 0.001281, 0.001031, 0.000808, 0.000633]) 


def helmholtzeinzel(i, r, x, n, v):          # v (und u bei überlagert) geben die Verschiebung der Spulenposition auf der Achse an.  
    return (mu0 * i * n)/(2) * r**2/(r**2 + (x+v)**2)**(3/2)    # Linke Spule bei 0, aber Spulenbreite beachten! (s. bei d =11.5 cm, v = 0.033)


def helmholtzüberlagert(i,r,x,n, v, u):
    return (mu0 * i * n)/(2) * r**2/(r**2 + (x+v)**2)**(3/2) + (mu0 * i * n)/(2) * r**2/(r**2 + (x+u)**2)**(3/2)

def weltformel(a, i, r, n, l):   #a: Punkt entlang der x-Achse, l:Länge der Spule
    return  (mu0 * i * n) / (2 * l) * ( (a) / (np.sqrt(r**2 + (a)**2)) + (l - a) / (np.sqrt(r**2 + (l-a)**2)))


#PLOT
plt.plot(abstaende , B4A, 'rx', label = r'Messwerte bei 4A') #Messwerte eintragen
plt.plot(abstaende , B2A, 'bx', label = r'Messwerte bei 2A')

x_plot = np.linspace(-0.050, 0.2, 10000)
x_plot1 = np.linspace(0, 0.2, 10000) #x-Koordinaten für rechte Spule

plt.plot(x_plot, helmholtzeinzel(4, 0.0625, x_plot, 100, 0.033-0.035), 'r--',alpha = 0.5) #Für 4A
plt.plot(x_plot1, helmholtzeinzel(4, 0.0625, x_plot1, 100, -0.115+0.033-0.035), 'r--',alpha = 0.5)
plt.plot(x_plot, helmholtzüberlagert(4, 0.0625, x_plot, 100, 0.033-0.035, -0.115+0.033-0.035), 'black', label = 'Spulenpaar bei 4A')

plt.plot(x_plot, helmholtzeinzel(2, 0.0625, x_plot, 100, 0.033-0.035), 'b--',alpha = 0.5) #Für 4A
plt.plot(x_plot1, helmholtzeinzel(2, 0.0625, x_plot1, 100, -0.115+0.033-0.035), 'b--',alpha = 0.5)
plt.plot(x_plot, helmholtzüberlagert(2, 0.0625, x_plot, 100, 0.033-0.035, -0.115+0.033-0.035), 'grey', label = 'Spulenpaar bei 2A')


plt.xticks([-0.050, -0.025, 0,  0.025, 0.050, 0.075, 0.100, 0.125, 0.15, 0.175, 0.2],
           ['-5', '-2.5', '0', '2.5', '5', '7.5', '10', '12.5', '15', '17.5', '20'])
plt.yticks([0, 0.001,0.002,0.003,0.004,0.005],
            ['0', '1', '2', '3', '4','5'])
          
plt.xlabel('$x$ / cm')
plt.ylabel('$B$ / mT')
plt.legend(loc = 'lower left')
plt.grid()
plt.show()
plt.savefig('helmholtzD.pdf')

print('2a mitte:', helmholtzüberlagert(2, 0.0625, 0.006+0.0625, 100, 0.033-0.035, -0.115+0.033-0.035))
print('4a mitte:', helmholtzüberlagert(4, 0.0625, 0.006+0.0625, 100, 0.033-0.035, -0.115+0.033-0.035))