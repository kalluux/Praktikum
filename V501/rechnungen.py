import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.constants import mu_0
import math

w =  0.0029/5.5*10**7*math.exp(-6876/T)
T = np.array([299.1,418.15, 472.15, 377.15 ])
print(T)