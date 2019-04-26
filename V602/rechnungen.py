import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.constants import mu_0
import math

h = 6.626*10**(-34)
c = 299792458 
d = 2.014*10**(-10)

E = (h*c)/(2*d*math.sin(0.069813170079773))
print(E)

