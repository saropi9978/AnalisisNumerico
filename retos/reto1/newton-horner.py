"""
    Realizado por:
    - Santiago Romero
    - Sandra Chavez
    - Ricardo Bernal
"""


import pylab as pylab
errorI=[]
nIteraciones=[]
def horner(a, x):
    tam = len(a)
    original = a[0]
    derivada = a[0]
    for j in range(1, tam - 1):
        original = x * original + a[j]
        derivada = x * derivada + original

    original = x * original + a[-1]

    return (original,derivada)


def NewtonHorner(p, x_0, maxIter = 5000, tol = 10e-16):
    n=len(p)-1
    nIter= 0
    x=x_0
    diff=1 + tol
    while nIter<=maxIter and diff>=tol:
        nIteraciones.append(diff)
        H=horner(p,x)
        if abs(H[1])<=tol:
            print("El método de Newton encontró una pendiente casi cero.")
            return None
        xnew = x - H[0] / H[1]
        diff = abs(x - xnew)
        errorI.append(diff)
        nIter+=1
        x= xnew
    if nIter > maxIter:
        print("El numero maximo de iteraciones se ha excedido")
    return x
#print("raiz encontrada en el polinomio x⁴−9x²−5x³+155x−250 es: ",NewtonHorner((1,-5,-9,155,-250),5))
print("raiz encontrada en el polinomio 10x⁵+3x²-2 es: ",NewtonHorner((10,0,0,3,0,-2),5))
#print("raiz encontrada en el polinomio x³−2x²+4x/3−8/27 es: ",NewtonHorner((1,-2,4/3,-(8/27)),5))

# pylab.title("error vs error_i+1(e⁻¹⁶) Newton-Horner (x⁴−9x²−5x³+155x−250)")
# pylab.plot(nIteraciones,errorI)
# pylab.xlabel('(x) error ')
# pylab.ylabel('(y) error_i+1') 
# pylab.show()
