from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
#arriba
x = np.array([0.9, 1.3, 1.9, 2.1, 2.6, 3, 3.9, 4.4, 4.7, 5, 6, 7, 8, 9.2, 10.5, 11.3, 11.6, 12, 12.6, 13,13.3])
y = np.array([1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25])
f1 = interp1d(x, y, kind='cubic')
xnew = np.linspace(x[0], x[20], 21)
plt.plot(x, y, 'o', xnew, f1(xnew),'-')
plt.legend(['data', 'linear', 'cubic'], loc='best')

x = np.array([13.3, 10.7, 10])
y = np.array([0.25, 0, 0.25])
f1 = interp1d(x, y, kind='quadratic')
xnew = np.linspace(x[0], x[2], 3)
plt.plot(x, y, 'o', xnew, f1(xnew),'-')
plt.legend(['data', 'linear', 'cubic','nearest','quadratic'], loc='best')

x = np.array([10,8.5])
y = np.array([0.25,-0.5])
f1 = interp1d(x, y)
xnew = np.linspace(x[0], x[1], 2)
plt.plot(x, y, 'o', xnew, f1(xnew),'-')
plt.legend(['data', 'linear', 'cubic','nearest','quadratic'], loc='best')

x = np.array([8.5, 8,  7, 6,4.75])
y = np.array([-0.5, -2, -4, -4.8, -5.1])
f1 = interp1d(x, y, kind='cubic')
xnew = np.linspace(x[0], x[4], 4)
plt.plot(x, y, 'o', xnew, f1(xnew),'-')
plt.legend(['data', 'linear', 'cubic','nearest','quadratic'], loc='best')

x = np.array([4.75, 5.1, 5.48, 5.6])
y = np.array([-5.1, -4, -2, 0.1])
f1 = interp1d(x, y, kind='cubic')
xnew = np.linspace(x[0], x[3], 4)
plt.plot(x, y, 'o', xnew, f1(xnew),'-')
plt.legend(['data', 'linear', 'cubic','nearest','quadratic'], loc='best')

x = np.array([5.6, 4.2, 3.5, 2.55, 2.1, 1.3,0.9])
y = np.array([0.1, 1.01, 1.01, 1.05, 1.2, 1,1.3])
f1 = interp1d(x, y, kind='cubic')
xnew = np.linspace(x[0], x[5], 6)
plt.plot(x, y, 'o', xnew, f1(xnew),'-')
plt.legend(['data', 'linear', 'cubic','nearest','quadratic'], loc='best')

f1 = interp1d(x, y, kind='cubic')
xnew = np.linspace(x[5], x[6], 2)
plt.plot(x, y, 'o', xnew, f1(xnew),'-')
plt.legend(['data', 'linear', 'cubic','nearest','quadratic'], loc='best')



plt.show()