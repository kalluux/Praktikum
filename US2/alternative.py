import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

locha1, ta1 = np.genfromtxt('ascan1.txt', unpack=True)
locha2, ta2 = np.genfromtxt('ascan2.txt', unpack=True)

tiefe1 = ta1 * 8.55 / 60.5 - 0.2
tiefe2 = ta2 * 8.55 / 60.5 - 0.2
durchmessera1 = 8.35 - tiefe1 - tiefe2

#ALTERNATIVE AUSWERTUNG A
print(locha1)
print("Tiefe 1:", tiefe1)
print(locha2)
print("Tiefe 2:", tiefe2)
print("Durchmesser:", durchmessera1)


#[ 3.  4.  5.  6.  7.  8.  9. 10. 11.]
#Tiefe 1: [6.39975207 5.6507438  4.88760331 4.11033058 3.26239669 2.47099174
# 1.65132231 0.85991736 5.80619835]
#[ 3.  4.  5.  6.  7.  8.  9. 10. 11.]
#Tiefe 2: [1.48173554 2.34380165 3.20586777 4.11033058 4.93       5.74966942
# 6.56933884 7.38900826 1.67958678]
#Durchmesser: [0.4685124  0.35545455 0.25652893 0.12933884 0.15760331 0.12933884
# 0.12933884 0.10107438 0.86421488]