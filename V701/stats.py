from scipy import stats
import numpy as np
import matplotlib.pylab as plt
 
b = np.genfromtxt('n.txt', unpack=True)
 
mean = np.mean(b)
#sem = sem(b)
std = np.std(b)
var = std**2
#print(mean,'+-','Varianz=',var)
 
 
plt.hist(b, bins=10, density = True, label="Messwerte")
xt = plt.xticks()[0]
xmin, xmax = min(xt), max(xt)
lnspc = np.linspace(xmin, xmax, len(b))


pdf_g = stats.norm.pdf(lnspc, mean, std)
plt.plot(lnspc, pdf_g, color="r", label="Gaußverteilung")
plt.xlabel(r'Zählrate N / 1/10s')
plt.ylabel(r'Relative Häufigkeit')
 
poi = np.random.poisson(lam=mean, size= 10000)
plt.hist(poi, bins=10, density = True, histtype = "step", color ="k", label="Poissonverteilung")
plt.grid()
plt.legend()
plt.show()
