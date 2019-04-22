import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.constants import mu_0
import math

T = np.array([299.25,418.15, 472.15, 377.15])
w =  0.0029/5.5*10**7*math.exp(-6876/299.1)
x =  0.0029/5.5*10**7*math.exp(-6876/418.15)
y =  0.0029/5.5*10**7*math.exp(-6876/472.15)
z =  0.0029/5.5*10**7*math.exp(-6876/377.15)

print(w,x,y,z)

a = 0.01
b = a/w
c = a/x
d = a/y
e = a/z
print(b,c,d,e)