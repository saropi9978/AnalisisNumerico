import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import math
from mpl_toolkits import mplot3d
import bezier as Bezier
from numpy import array as a
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

h = -2 #Altura (z)
b = 0.76 #Radio 1
cg = 0
c = 0.55191502449 #constante para mostrar un circulo



#base
for i in range(0, 4):
	p = Circle((0, 0), b, color="green", fill=False)
	ax.add_patch(p)
	art3d.pathpatch_2d_to_3d(p, z = h+2)
	h = h + 0.1


h = 0 #Altura (z)
b = 0.0 #Radio 2
#esfera
for i in np.arange(-1,1.4,0.1):
    p = Circle((0, 0), b, color="green", fill=False)
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z = i+1.1)
    b=2-(i*i)
    print(b)

#paraboloide
perimetro=0.0
for i in np.arange(0,1.2,0.1):
    p = Circle((0, 0), perimetro, color="green", fill=False)
    ax.add_patch(p)
    perimetro=math.sqrt(i)*3-i    
    art3d.pathpatch_2d_to_3d(p, z = i+1.5)
    

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-1, 5)
plt.show()
