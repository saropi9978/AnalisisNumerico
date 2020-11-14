from Bezier import Bezier
import numpy as np
from numpy import array as a
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

h=0

#A-B-C-D (x+,y+,z+)
points_set_1 = a([[0, 1, h], [0.7, 0.7, h], [1, 0, h]])
t_points = np.arange(0, 1, 0.01)
curve_set_1 = Bezier.Curve(t_points, points_set_1)
ax.plot(curve_set_1[:, 0], curve_set_1[:, 1], curve_set_1[:, 2], color="red")
#ax.plot(points_set_1[:, 0], points_set_1[:, 1], points_set_1[:, 2], 'o:')

#D-E-F-G (x+,y-,z+)
points_set_2 = a([[1, 0, h], [0.7, -0.7, h], [0, -1, h]])
t_points = np.arange(0, 1, 0.01)
curve_set_2 = Bezier.Curve(t_points, points_set_2)
ax.plot(curve_set_2[:, 0], curve_set_2[:, 1], curve_set_2[:, 2], color="red")
#ax.plot(points_set_2[:, 0], points_set_2[:, 2], points_set_2[:, 2], 'o:')

#G-H-I-J (x-,y-,z+) --- +B = -F
points_set_3 = a([[0, -1, h], [-0.7, -0.7, h], [-1, 0, h]])
t_points = np.arange(0, 1, 0.01)
curve_set_3 = Bezier.Curve(t_points, points_set_3)
ax.plot(curve_set_3[:, 0], curve_set_3[:, 1], curve_set_3[:, 2], color="red")
#ax.plot(points_set_3[:, 0], points_set_3[:, 2], points_set_3[:, 2], 'o:')

#J-K-L-A (x-,y+,z+)
points_set_4 = a([[-1, 0, h], [-0.7, 0.7, h], [0, 1, h]])
t_points = np.arange(0, 1, 0.01)
curve_set_4 = Bezier.Curve(t_points, points_set_4)
ax.plot(curve_set_4[:, 0], curve_set_4[:, 1], curve_set_4[:, 2], color="red")
#ax.plot(points_set_4[:, 0], points_set_4[:, 2], points_set_4[:, 2], 'o:')

b1=1
r1=0.7

#Inicio Cilindro Base

for i in np.arange(0,1,0.3):
    
    #A-B-C-D (x+,y+,z+)
    points_set_1 = a([[0, b1, h], [r1, r1, h], [b1, 0, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_1 = Bezier.Curve(t_points, points_set_1)
    ax.plot(curve_set_1[:, 0], curve_set_1[:, 1], curve_set_1[:, 2], color="red")
    #ax.plot(points_set_1[:, 0], points_set_1[:, 1], points_set_1[:, 2], 'o:')

    #D-E-F-G (x+,y-,z+)
    points_set_2 = a([[b1, 0, h], [r1, -r1, h], [0, -b1, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_2 = Bezier.Curve(t_points, points_set_2)
    ax.plot(curve_set_2[:, 0], curve_set_2[:, 1], curve_set_2[:, 2], color="red")
    #ax.plot(points_set_2[:, 0], points_set_2[:, 2], points_set_2[:, 2], 'o:')

    #G-H-I-J (x-,y-,z+) --- +B = -F
    points_set_3 = a([[0, -b1, h], [-r1, -r1, h], [-b1, 0, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_3 = Bezier.Curve(t_points, points_set_3)
    ax.plot(curve_set_3[:, 0], curve_set_3[:, 1], curve_set_3[:, 2], color="red")
    #ax.plot(points_set_3[:, 0], points_set_3[:, 2], points_set_3[:, 2], 'o:')

    #J-K-L-A (x-,y+,z+)
    points_set_4 = a([[-b1, 0, h], [-r1, r1, h], [0, b1, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_4 = Bezier.Curve(t_points, points_set_4)
    ax.plot(curve_set_4[:, 0], curve_set_4[:, 1], curve_set_4[:, 2], color="red")
    #ax.plot(points_set_4[:, 0], points_set_4[:, 2], points_set_4[:, 2], 'o:')
    h=h+0.02

#Fin Cilindro Base

print("b: ",b1, "r: ",r1, "h: ", h)

#Inicio Esfera Inferior
for i in np.arange(0,1,0.1):
    
    b2 = b1+i
    r2 = r1+i

    #A-B-C-D (x+,y+,z+)
    points_set_1 = a([[0, b1+i, h], [r1+i, r1+i, h], [b1+i, 0, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_1 = Bezier.Curve(t_points, points_set_1)
    ax.plot(curve_set_1[:, 0], curve_set_1[:, 1], curve_set_1[:, 2], color="red")
    #ax.plot(points_set_1[:, 0], points_set_1[:, 1], points_set_1[:, 2], 'o:')

    #D-E-F-G (x+,y-,z+)
    points_set_2 = a([[b1+i, 0, h], [r1+i, -r1-i, h], [0, -b1-i, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_2 = Bezier.Curve(t_points, points_set_2)
    ax.plot(curve_set_2[:, 0], curve_set_2[:, 1], curve_set_2[:, 2], color="red")
    #ax.plot(points_set_2[:, 0], points_set_2[:, 2], points_set_2[:, 2], 'o:')

    #G-H-I-J (x-,y-,z+) --- +B = -F
    points_set_3 = a([[0, -b1-i, h], [-r1-i, -r1-i, h], [-b1-i, 0, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_3 = Bezier.Curve(t_points, points_set_3)
    ax.plot(curve_set_3[:, 0], curve_set_3[:, 1], curve_set_3[:, 2], color="red")
    #ax.plot(points_set_3[:, 0], points_set_3[:, 2], points_set_3[:, 2], 'o:')

    #J-K-L-A (x-,y+,z+)
    points_set_4 = a([[-b1-i, 0, h], [-r1-i, r1+i, h], [0, b1+i, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_4 = Bezier.Curve(t_points, points_set_4)
    ax.plot(curve_set_4[:, 0], curve_set_4[:, 1], curve_set_4[:, 2], color="red")
    #ax.plot(points_set_4[:, 0], points_set_4[:, 2], points_set_4[:, 2], 'o:')
    h=h+0.05

print("b: ",b2, "r: ",r2, "h: ", h)
#Fin Esfera Inferior

b1 = b2
r1 = r2


#Inicio Esfera Mitad
for i in np.arange(0,1.3,0.1):
    
    #A-B-C-D (x+,y+,z+)
    points_set_1 = a([[0, b1, h], [r1, r1, h], [b1, 0, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_1 = Bezier.Curve(t_points, points_set_1)
    ax.plot(curve_set_1[:, 0], curve_set_1[:, 1], curve_set_1[:, 2], color="red")
    #ax.plot(points_set_1[:, 0], points_set_1[:, 1], points_set_1[:, 2], 'o:')

    #D-E-F-G (x+,y-,z+)
    points_set_2 = a([[b1, 0, h], [r1, -r1, h], [0, -b1, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_2 = Bezier.Curve(t_points, points_set_2)
    ax.plot(curve_set_2[:, 0], curve_set_2[:, 1], curve_set_2[:, 2], color="red")
    #ax.plot(points_set_2[:, 0], points_set_2[:, 2], points_set_2[:, 2], 'o:')

    #G-H-I-J (x-,y-,z+) --- +B = -F
    points_set_3 = a([[0, -b1, h], [-r1, -r1, h], [-b1, 0, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_3 = Bezier.Curve(t_points, points_set_3)
    ax.plot(curve_set_3[:, 0], curve_set_3[:, 1], curve_set_3[:, 2], color="red")
    #ax.plot(points_set_3[:, 0], points_set_3[:, 2], points_set_3[:, 2], 'o:')

    #J-K-L-A (x-,y+,z+)
    points_set_4 = a([[-b1, 0, h], [-r1, r1, h], [0, b1, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_4 = Bezier.Curve(t_points, points_set_4)
    ax.plot(curve_set_4[:, 0], curve_set_4[:, 1], curve_set_4[:, 2], color="red")
    #ax.plot(points_set_4[:, 0], points_set_4[:, 2], points_set_4[:, 2], 'o:')
    h=h+0.05

print("b: ",b2, "r: ",r2, "h: ", h)

#Fin Esfera Mitad

b1 = b2
r1 = r2

#Inicio Esfera Superior
for i in np.arange(0,1,0.1):
    
    b2 = b1-i
    r2 = r1-i

    #A-B-C-D (x+,y+,z+)
    points_set_1 = a([[0, b1-i, h], [r1-i, r1-i, h], [b1-i, 0, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_1 = Bezier.Curve(t_points, points_set_1)
    ax.plot(curve_set_1[:, 0], curve_set_1[:, 1], curve_set_1[:, 2], color="red")
    #ax.plot(points_set_1[:, 0], points_set_1[:, 1], points_set_1[:, 2], 'o:')

    #D-E-F-G (x+,y-,z+)
    points_set_2 = a([[b1-i, 0, h], [r1-i, -r1+i, h], [0, -b1+i, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_2 = Bezier.Curve(t_points, points_set_2)
    ax.plot(curve_set_2[:, 0], curve_set_2[:, 1], curve_set_2[:, 2], color="red")
    #ax.plot(points_set_2[:, 0], points_set_2[:, 2], points_set_2[:, 2], 'o:')

    #G-H-I-J (x-,y-,z+) --- +B = -F
    points_set_3 = a([[0, -b1+i, h], [-r1+i, -r1+i, h], [-b1+i, 0, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_3 = Bezier.Curve(t_points, points_set_3)
    ax.plot(curve_set_3[:, 0], curve_set_3[:, 1], curve_set_3[:, 2], color="red")
    #ax.plot(points_set_3[:, 0], points_set_3[:, 2], points_set_3[:, 2], 'o:')

    #J-K-L-A (x-,y+,z+)
    points_set_4 = a([[-b1+i, 0, h], [-r1+i, r1-i, h], [0, b1-i, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_4 = Bezier.Curve(t_points, points_set_4)
    ax.plot(curve_set_4[:, 0], curve_set_4[:, 1], curve_set_4[:, 2], color="red")
    #ax.plot(points_set_4[:, 0], points_set_4[:, 2], points_set_4[:, 2], 'o:')
    h=h+0.05

print("b: ",b2, "r: ",r2, "h: ", h)

#Fin Esfera Superior

b1 = b2
r1 = r2



#Inicio "Paraboloide"
k = 0.01

for i in np.arange(0,1.5,0.1):
    
    b2 = b1-k
    r2 = r1-k

    #A-B-C-D (x+,y+,z+)
    points_set_1 = a([[0, b1-k, h], [r1-k, r1-k, h], [b1-k, 0, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_1 = Bezier.Curve(t_points, points_set_1)
    ax.plot(curve_set_1[:, 0], curve_set_1[:, 1], curve_set_1[:, 2], color="red")
    #ax.plot(points_set_1[:, 0], points_set_1[:, 1], points_set_1[:, 2], 'o:')

    #D-E-F-G (x+,y-,z+)
    points_set_2 = a([[b1-k, 0, h], [r1-k, -r1+k, h], [0, -b1+k, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_2 = Bezier.Curve(t_points, points_set_2)
    ax.plot(curve_set_2[:, 0], curve_set_2[:, 1], curve_set_2[:, 2], color="red")
    #ax.plot(points_set_2[:, 0], points_set_2[:, 2], points_set_2[:, 2], 'o:')

    #G-H-I-J (x-,y-,z+) --- +B = -F
    points_set_3 = a([[0, -b1+k, h], [-r1+k, -r1+k, h], [-b1+k, 0, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_3 = Bezier.Curve(t_points, points_set_3)
    ax.plot(curve_set_3[:, 0], curve_set_3[:, 1], curve_set_3[:, 2], color="red")
    #ax.plot(points_set_3[:, 0], points_set_3[:, 2], points_set_3[:, 2], 'o:')

    #J-K-L-A (x-,y+,z+)
    points_set_4 = a([[-b1+k, 0, h], [-r1+k, r1-i, h], [0, b1-k, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_4 = Bezier.Curve(t_points, points_set_4)
    ax.plot(curve_set_4[:, 0], curve_set_4[:, 1], curve_set_4[:, 2], color="red")
    #ax.plot(points_set_4[:, 0], points_set_4[:, 2], points_set_4[:, 2], 'o:')
    h=h+0.05
    k=k+0.01

print("b: ",b2, "r: ",r2, "h: ", h)

b1 = b2
r1 = r2

for i in np.arange(0,1,0.1):
    
    #A-B-C-D (x+,y+,z+)
    points_set_1 = a([[0, b1, h], [r1, r1, h], [b1, 0, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_1 = Bezier.Curve(t_points, points_set_1)
    ax.plot(curve_set_1[:, 0], curve_set_1[:, 1], curve_set_1[:, 2], color="red")
    #ax.plot(points_set_1[:, 0], points_set_1[:, 1], points_set_1[:, 2], 'o:')

    #D-E-F-G (x+,y-,z+)
    points_set_2 = a([[b1, 0, h], [r1, -r1, h], [0, -b1, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_2 = Bezier.Curve(t_points, points_set_2)
    ax.plot(curve_set_2[:, 0], curve_set_2[:, 1], curve_set_2[:, 2], color="red")
    #ax.plot(points_set_2[:, 0], points_set_2[:, 2], points_set_2[:, 2], 'o:')

    #G-H-I-J (x-,y-,z+) --- +B = -F
    points_set_3 = a([[0, -b1, h], [-r1, -r1, h], [-b1, 0, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_3 = Bezier.Curve(t_points, points_set_3)
    ax.plot(curve_set_3[:, 0], curve_set_3[:, 1], curve_set_3[:, 2], color="red")
    #ax.plot(points_set_3[:, 0], points_set_3[:, 2], points_set_3[:, 2], 'o:')

    #J-K-L-A (x-,y+,z+)
    points_set_4 = a([[-b1, 0, h], [-r1, r1, h], [0, b1, h]])
    t_points = np.arange(0, 1, 0.01)
    curve_set_4 = Bezier.Curve(t_points, points_set_4)
    ax.plot(curve_set_4[:, 0], curve_set_4[:, 1], curve_set_4[:, 2], color="red")
    #ax.plot(points_set_4[:, 0], points_set_4[:, 2], points_set_4[:, 2], 'o:')
    h=h+0.05

print("b: ",b2, "r: ",r2, "h: ", h)

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-2, 2)

plt.show()