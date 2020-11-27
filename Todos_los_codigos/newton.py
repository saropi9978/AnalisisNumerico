import numpy as np
import matplotlib.pyplot as plt
import math

def F(x):
    return (9*math.sin(x))+(8*math.sin(2*x))-(3*math.sin(3*x))-4
 
def dFdx(x):
    return (9*math.cos(x))+(16*math.cos(2*x))-(9*math.cos(3*x))


x = np.linspace(-2,2,100)
plt.figure(num="Newton")
plt.plot(x, F(x))
plt.grid('on')
plt.show()

rootValues = [4.0] # valor inicial
error = 0.001
rootGuess = rootValues[-1]
print ("%11s %11s" % ("x", "F(x)"))
while True:
    print ("%11.8f %11.8f" % (rootGuess, F(rootGuess)))
    droot = -1*F(rootGuess)/dFdx(rootGuess)
    rootGuess = rootGuess + droot
    rootValues.append(rootGuess)
    if abs(rootValues[-2] - rootValues[-1]) < error:
        break
rootValues = np.array(rootValues)
x = np.linspace(0,5,100)
plt.figure(num="Newton")
plt.clf()
plt.plot(x, F(x))
plt.plot(rootValues, F(rootValues), 'ko', ms=6)
plt.grid('on')
plt.show()