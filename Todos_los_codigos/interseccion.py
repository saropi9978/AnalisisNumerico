

import numpy as np
import matplotlib.pyplot as plt
 
x = np.linspace(-100, 100, 10000000)
plt.plot(
    x, np.cos(x), 
    x, - (np.e**x)
)
plt.show()