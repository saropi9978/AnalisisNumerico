import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import math
from mpl_toolkits import mplot3d
import bezier as Bezier
from numpy import array as a
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d

def areaParaboloide():
    r=2.1
    h=1
    return 0.5236* (r/h**2) * (((r**2 + 4* h**2)**(3/2))-r**3)

def areaCilindro():
    r=0.76
    h=0.4
    return math.pi * r**2 * h

def areaEsfera():
    r=math.sqrt(2)
    return 4* r**2 * math.pi




def volumenEsfera():
    r=math.sqrt(2)
    return 4/3* r**3 * math.pi

def volumenParaboloide():
    r=2.1
    h=1
    return (math.pi* r**2 *h)/2
def volumenCilindro():
    h=0.4
    return areaCilindro()*h



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

h = -2 #Altura (z)
b = 0.76 #Radio 1
cg = 0
c = 0.55191502449 #constante para mostrar un circulo

#base
def cilindro(curvaNivel=False):
    h = 0
    b = 0.76 #Radio 1
    for i in range(0, 4):
        p = Circle((0, 0), b, color="green", fill=curvaNivel)
        ax.add_patch(p)
        art3d.pathpatch_2d_to_3d(p, z = h)
        h = h + 0.1
def esfera(curvaNivel=False):
    b = 0.0 #Radio 2
    #esfera
    for i in np.arange(-1,1.4,0.1):
        p = Circle((0, 0), b, color="green", fill=curvaNivel)
        ax.add_patch(p)
        art3d.pathpatch_2d_to_3d(p, z = i+1.1)
        b=2-(i*i)

def paraboloide(curvaNivel=False):
    #paraboloide
    radio=0.0
    for i in np.arange(0,1.2,0.1):
        p = Circle((0, 0), radio, color="green", fill=curvaNivel)
        ax.add_patch(p)
        radio=math.sqrt(i)*3-i    
        art3d.pathpatch_2d_to_3d(p, z = i+1.5)
        print(radio)

cilindro(True)
esfera(True)
paraboloide(True)
area=areaCilindro()+areaEsfera()+areaParaboloide()-(abs(areaCilindro()-areaEsfera()))-(abs(areaParaboloide()-areaEsfera()))
volumen= volumenCilindro()+volumenEsfera()+volumenParaboloide()-(abs(volumenCilindro()-volumenEsfera()))-(abs(volumenParaboloide()-volumenEsfera()))
print("el área de la jarra es: ",area)
print("el volumen de la jarra es: ",volumen)



ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-1, 5)
plt.show()
