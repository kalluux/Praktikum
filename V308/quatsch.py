import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

N = 595
r = 0.13

I = np.array( [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

BHY = [-0.002562, 0.1342, 0.2923, 0.4011, 0.4765, 0.5298, 0.5732, 0.6084, 0.6384, 0.6648, 0.6888, 0.6736, 0.6557, 0.6365, 0.6137, 0.5858, 0.551, 0.5047, 0.4443, 0.3151, 0.1222, -0.0724, -0.2428, -0.3738, -0.4632, -0.5232, -0.5695, -0.6055, -0.6365, -0.6642, -0.6894, -0.6739, -0.656, -0.6369, -0.6138, -0.5856, -0.5511, -0.5066, -0.4436, -0.3146, -0.122, 0.07566, 0.2465, 0.3827, 0.4661, 0.5257, 0.5716, 0.6063, 0.6365, 0.664, 0.6875]

H = (I * N) / (2*np.pi * r)  #Berechnung der äußeren Feldes einer Toroidspule

plt.plot(H, BHY, 'r', linewidth = 0.9, label = 'Hysteresekurve')

xdata = np.linspace(-8000,8000,10000)
ydata = np.linspace(-0.75, 0.75, 10000)
plt.plot(xdata, 0+xdata*0, 'black', linewidth = 0.7)
plt.plot(0+0*ydata, ydata, 'black', linewidth = 0.7)

#plt.annotate(r'Koerzitivfeldstärke', xy=(-461.29, 0), xytext=(-6000, 0.3),
#           arrowprops=dict(facecolor='black', shrink=0.05, width = 0.7, headwidth = 5.6))
#
plt.legend()
plt.xlabel('$H$ / A/m')
plt.ylabel('$B$ / T')
plt.xlim(-457.5,-457.4)
plt.ylim(-0.000001,0.000001)
plt.grid()
plt.savefig('quatsch.pdf')
plt.close()
