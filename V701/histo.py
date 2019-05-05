import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat
import math
from scipy import stats

N = np.genfromtxt('n.txt', unpack=True)
q = np.mean(N)
print(q)
print(np.std(N))
print('Mittelwert der Stichprobe', np.mean(N))
print('Varianz der Stichprobe', np.var(N, ddof = 1))
print('Varianz der Stichprobe', np.var(N))
print('gaussverteilung, da stndardabweichung 280^2 = varianz ist')


