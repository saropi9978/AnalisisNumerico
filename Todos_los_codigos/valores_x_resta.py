import matplotlib.pyplot as plt
import numpy as np
print("profe no entiendo muy bien a que se refiere. Sin embargo, le dejo el punto graficado\n solo por si sirve de algo")



x = np.arange(0,100,0.1)
y= (1-(1/np.cos(x)))/np.tan(x)**2

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('profe... unos punticos por graficar')
plt.show()

plt.savefig("output.png")

