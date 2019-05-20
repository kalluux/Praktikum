import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat
import math
from scipy import stats

N = np.genfromtxt('n.txt', unpack=True)
q = np.mean(N)
#M= N/10
print(q)
print(np.std(N))
print('Mittelwert der Stichprobe', np.mean(N))
print('Varianz der Stichprobe', np.var(N, ddof = 1))
print('Varianz der Stichprobe', np.var(N))
print('gaussverteilung, da stndardabweichung 280^2 = varianz ist')

#N.sort()
#hmean = np.mean(N)
#hstd = np.std(N)
#pdf = stats.norm.pdf(N, hmean, hstd)
#plt.plot(N, pdf)
#plt.savefig('1.pdf')

mean = 5463; std = 280; variance = np.square(std)
x = np.linspace(5462.99,5463.01)
f = np.exp(-np.square(x-mean)/2*variance)/(np.sqrt(2*np.pi*variance))

plt.plot(x,f)




plt.savefig('1.pdf')



