import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

phi, v = np.genfromtxt('wertec.txt', unpack=True)
U, frequenz = np.genfromtxt('werteb.txt', unpack=True)

a = np.linspace(0,np.pi/2,200)
plt.polar(phi, U, 'rx', label='Messwerte', Markersize=3)
plt.polar(a, np.cos(a), 'k-', label='Theoriekurve', linewidth=1)
#plt.title('Polarplot')
plt.legend()
plt.tight_layout
plt.savefig('plot4.pdf')

