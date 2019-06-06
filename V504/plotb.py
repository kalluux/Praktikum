from uncertainties import ufloat
import numpy as np
import matplotlib.pyplot as plt


u5, i5 = np.genfromtxt('a5.txt', unpack=True)
x = np.log(u5)
y = np.log(i5)
print(x)

plt.plot(x,y, 'rx', label= 'x')
plt.ylabel(r'$I$ / mA')
plt.xlabel(r'$U$ / V')
plt.legend()
plt.grid()
plt.show()

#Is in mA 
#0,010
#0,020
#0,045
#0,100
#0,210