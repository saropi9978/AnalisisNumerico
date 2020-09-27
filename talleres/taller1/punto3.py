"""
Realizado por:
 - Santiago Romero
 - Sandra Chavez
 - Ricardo Bernal
"""
import numpy as np
import math as m
import matplotlib.pyplot as plt
import pylab as pylab

#punto 1.a
def fx(x):
    return m.log((x+2), np.exp(1))-np.sin(x)

E = 10e-16
ptos = []
ptos2= []
ptos.append(-1.9)
ptos.append(-1.1)

n = 2
dif = 100
error = []

while dif > E:
    xn =  (ptos[n-1]) - ((fx(ptos[n-1])*(ptos[n-1]-ptos[n-2]))/(fx(ptos[n-1])-fx(ptos[n-2])))
    ptos.append(xn)
    ptos2.append(xn)
    dif = np.abs(ptos[n] - ptos[n-1])
    error.append(dif)
    n = n + 1
    
n = 0

print("ejercicio a")
print(" Utilice la siguiente formula recursiva conE= 10⁻¹⁶ para determinar aproximadamente el punto deintersección.\n")

while n < len(error):
    print(ptos[n]," ",error[n])
    n = n + 1
print("\n")

# pylab.title("puntos vs error")
# pylab.plot(ptos2,error,color="green", linewidth=2.5, linestyle="-", label="p vs e formula a")
# pylab.legend(loc='upper right')
# pylab.plot(ptos2,error)
# pylab.xlabel('(x) puntos ')
# pylab.ylabel('(y) error') 
# pylab.show()


#punto 1.b

errorI = []
nIteraciones = []
'''Punto 3.1.b '''
def PuntoB(fxgx ,E,x0,xn):
    iteraciones=0
    error=1
    resultado=0
    while error>=10**-8:
        if fxgx(xn)-fxgx(x0)==0:
            break
        x2 = xn-(fxgx(xn))*((xn-(xn-x0))/fxgx(xn)-fxgx(x0))
        iteraciones+=1
        nIteraciones.append(iteraciones)
        error= x2-xn
        errorI.append(error)
        x0=xn
        x1=x2
        resultado=x2
    return resultado


x0=0
xn=0.2
fX = lambda x: m.log(x+2)
gX = lambda x: m.sin(x)
fxgx=lambda x: m.log(x+2)-m.sin(x)
result =PuntoB(fxgx,1e-8,x0,xn)
print("punto b")
print("Aplicar el método iterativo siguiente con E = 10⁻⁸ para encontrar el punto de intersección\n")

print("Resultado metodo iterativo :",  result,"\n")








#punto 3

e = m.e
pi = m.pi

nIteraciones=[]
valoresX=[]

def newton_raphson(f, df, x, TOL):
    error = 1
    ite = 0
    while error > TOL:
        nIteraciones.append(ite)
        new_x = x - f(x)/df(x)
        error = abs(new_x - x)
        x = new_x
        valoresX.append(x)
        ite += 1
        print("Iteracion: ", ite, "X = ",x)
    return x,ite

def modificado_newton(f, df, ddf, x, TOL):
    error = 1
    ite = 0
    while error > TOL:
        f_x = f(x)
        d_x = df(x)
        new_x = x - (f_x*d_x)/(d_x*d_x - f_x*ddf(x))
        error = abs(new_x - x)
        x = new_x
        ite += 1
        print("Iteracion: ", ite, "X = ",x)
    return x,ite


f = lambda x: ((m.exp(x)) - x - 1)
df = lambda x: ((m.exp(x)) - 1)
ddf = lambda x: (m.exp(x))

#punto 3 
print("punto 3")
print("sea f(x)= e^x -x-1")
print("punto 1.\nDemuestre que Tiene un cero de multiplicidad 2 enx= 0")
print("punto 2.\nUtilizando el método de Newton con p0= 1 verifique que converge a cero pero no de forma cuadrática")
print("punto 3.\nUtilizando el método de Newton generalizado, mejora la tasa de rendimiento? explique su respuesta\n")



raiz,n = newton_raphson(f, df, 1, 1e-16)
print("Newton Raphson: ",raiz, "Iteraciones: ",n)

raiz,n = modificado_newton(f, df, ddf, 1, 1e-16)
print("Newton Modificado: ",raiz, "Iteraciones: ",n)
