import numpy as np 
from uncertainties import ufloat
import math
import uncertainties.unumpy as unp

#Periodendauer
T = np.array([18.247, 18.242, 18.244, 18.245, 18.250, 18.249, 18.243, 18.235, 18.248, 18.250])
print(np.mean(T),np.std(T))

Tmittel = ufloat(18.245, 0.004)

