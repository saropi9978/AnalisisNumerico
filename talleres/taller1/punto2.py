"""
Realizado por:
 - Santiago Romero
 - Sandra Chavez
 - Ricardo Bernal
"""
import scipy
import scipy.optimize as opt
import numpy
import pylab as pylab
#ejercicio 1
cantidad=[]
iteraciones=[]
print("Ejercicio #1\nrealice un algoritmo que le permita sumar ́unicamente los elementos de la submatriz triangular superior o triangular inferior, dada la matriz cuadrada A_n.\nImprima varias pruebas,para diferentes valores deny exprese f(n) en notacion O() con una grafica que muestre su orden deconvergencia.\n")
def triangular_superior(matriz=[]):
    n=len(matriz)
    if n==0 or n==1:
        iteraciones.append(0)
        return 0
    suma=0
    it=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            it+=1
            suma+=matriz[i][j]

    print("la cantidad de iteraciones fueron: ",it)
    iteraciones.append(it)
    return suma
def triangular_inferior(matriz=[]):
    n=len(matriz)
    if n==0 or n==1:
        return 0
    suma=0
    it=0
    for i in range(1,n):
        for j in range(0,i):
            suma+=matriz[i][j]
            it+=1
    print("la cantidad de iteraciones fueron: ",it)
    return suma

matriz= numpy.array([[1 for j in range(5)] for k in range(5)])
print("matriz:\n",matriz)

print("suma de la triangular superior: ",)
print("suma de la triangular inferior: ",triangular_inferior(matriz),"\n")
print("t(n)= O() ",) 



#ejercicio 2
print("Ejercicio #2\nRealice un algoritmo que le permita sumar los n² primeros números naturales al cuadrado. Imprima varias pruebas para diferentes valores de n y exprese f(n) en notación O() con una gráfica que muestre su orden de convergencia.\n")
def sumatoria_cuadrados(n=122):
    if n==0:
        iteraciones.append(0)
        return 0
    contador=1
    suma=1
    resta=3
    it=0
    while contador+resta <=n:
        contador+=resta
        suma+=contador
        resta+=2
        it+=1
    print("la cantidad de iteraciones fueron: ",it)
    iteraciones.append(it)
    return suma
print("la sumatoria de los cuadrados hasta 121 es: ",sumatoria_cuadrados(),"\n")




print("Ejercicio #3\ny(t) = 6 + 2,13t²−0.0013t⁴\nDonde y es la altura en [m] yttiempo en [s]. El cohete esta colocado verticalmente sobre la tierra. Utilizando dos metodos de solución de ecuación no lineal, encuentre la altura m ́axima que alcanza elcohete.\n")

def trayectoria(t=0):
    valor1=(6+(2.13*(t**2)))-(0.0013*(t**4))
    valor2=(6+(2.13*((t+1)**2)))-(0.0013*((t+1)**4))
    cantidad.append(t)
    iteraciones.append(valor1)
    while valor1<valor2:
        t+=1
        valor1=(6+(2.13*(t**2)))-(0.0013*(t**4))
        valor2=(6+(2.13*((t+1)**2)))-(0.0013*((t+1)**4))
        cantidad.append(t)
        iteraciones.append(valor1)
    print("la cantidad de iteraciones fueron: ",t)
    return valor1
print("La altura maxima es: ",trayectoria()," metros\n")

# pylab.title("trayectoria cohete hasta altura maxima")
# pylab.plot(cantidad,iteraciones,color="green", linewidth=2.5, linestyle="-", label="cohete")
# pylab.legend(loc='upper right')
# pylab.plot(cantidad,iteraciones)
# pylab.xlabel('(x) tiempo ')
# pylab.ylabel('(y) altura') 
# pylab.show()





