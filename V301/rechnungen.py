import numpy as np 
from uncertainties import ufloat
import math
import uncertainties.unumpy as unp

U = np.array([0.9,1.1,1.15,1.17,1.19,1.23,1.25,1.27,1.3,1.32])
ImA = np.array([91.5,70,65,58,47,41,36,32,29,25])

I = ImA/1000 

P = U*I
print(P)

R = U/I
print(R)