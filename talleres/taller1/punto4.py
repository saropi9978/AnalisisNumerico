"""
Realizado por:
 - Santiago Romero
 - Sandra Chavez
 - Ricardo Bernal
"""

import pylab as pylab
import math
import numpy
errorI=[]
iteraciones=[]
def biseccion(f,a,b,N):
    valores=[]
    if f(a)*f(b) >= 0:
        print("f(a)*f(b) >= 0 entonces no es posible de realizar")
        return (None, valores)
    a_n = a
    b_n = b
    for n in range(1,N+1):
        errorI.append((a_n + b_n)/2)
        iteraciones.append(n)
        m_n = (a_n + b_n)/2
        valores.append(m_n)
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("La encontre")
            return (m_n, valores)
        else:
            print("La raiz no se encuentra en el intervalo")
            return (None, valores)
    return ((a_n + b_n)/2, valores)



#punto 1
f1 = lambda x: math.cos(1/x)
print("punto 1")
print("Verifique el tipo de convergencia enx= 1 independiente del origen")
approx_phi = biseccion(f1,1,2,100)
print("raiz: ",approx_phi[0],"\n")

f1 = lambda x: math.cos(1/x)
print("punto 2")
print("Compare los primeros t ́erminos con la sucesión { An }∞ n=0")
approx_phi = biseccion(f1,0.1,0.9,100)
for i in numpy.arange(1,25):
    print("cos(1/",i,")=",math.cos(1/i) )
print("raiz:",approx_phi[0],"\n")



print("punto 3")
print("Sean f(t) = 3sin³t −1 y g(t) = 4sin(t)cos(t) parat≥0 las ecuaciones paramétricas que describe el movimiento en una particula. Utilice un método de solución numérico con error de 10⁻¹⁶ para determinardonde las coordenadas coiciden y muestre gráficamente la solución")
f3 = lambda x: (9*math.sin(x))-(8*math.sin(2*x))-(3*math.sin(3*x))-4
approx_phi = biseccion(f3,0,2,1000)
print("uno de los puntos: ",approx_phi[0])
approx_phi = biseccion(f3,2,4,1000)
print("otro de los puntos: ",approx_phi[0],"\n")
