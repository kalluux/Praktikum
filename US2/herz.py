import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

schlag, amp = np.genfromtxt('amplituden.txt', unpack=True)

h = 1/2 * 2730 * 10**(-6) * amp * 100
vol = h * np.pi / 6 * (3* 2.5**2 + h**2)
print(vol, np.mean(vol), np.std(vol))
herzvol = ufloat(np.mean(vol), np.std(vol))
vherzende = herzvol * 0.45
print(vherzende)

#(base) daniel@daniel-VB:~/Praktikum/US2$ python herz.py
#[16.47694232 19.78656639 20.93561221 18.65124761 19.19516238 19.92586887
# 17.54855923] 18.931422715796575 1.4051848636239674
#8.5+/-0.6