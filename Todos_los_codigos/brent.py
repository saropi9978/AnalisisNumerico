
"""
Adaptado y Modificado por:
 - Santiago Romero
 - Sandra Chavez
 - Ricardo Bernal
"""
import pylab as pylab
errorI = []
nIteraciones = []


def MetodoBrent(f, x0, x1, maxIter, Tol):

    fx0 = f(x0)
    fx1 = f(x1)

    if (fx0 * fx1) >= 0:
        return "La raiz no se encuentra en el rango", 0 

    if abs(fx0) < abs(fx1):
        x0, x1 = x1, x0
        fx0, fx1 = fx1, fx0

    x2, fx2 = x0, fx0

    validacion = True
    nIter = 0

    while nIter < maxIter and abs(x1-x0) > Tol:
        nIteraciones.append(nIter)
        errorI.append(abs(x1-x0))
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)

        if fx0 != fx2 and fx1 != fx2:
             # En esta parte del algortimo se usa el método de  interpolaciín inversa cuadrática
            L0 = (x0 * fx1 * fx2) / ((fx0 - fx1) * (fx0 - fx2))
            L1 = (x1 * fx0 * fx2) / ((fx1 - fx0) * (fx1 - fx2))
            L2 = (x2 * fx1 * fx0) / ((fx2 - fx0) * (fx2 - fx1))
            funSec = L0 + L1 + L2

        else:
            # En esta parte del algortimo se usa el método de la secante
            funSec = x1 - ((fx1 * (x1 - x0)) / (fx1 - fx0))

        if ((funSec < ((3 * x0 + x1) / 4) or funSec > x1) or
            (validacion == True and (abs(funSec - x1)) >= (abs(x1 - x2) / 2)) or
            (validacion == False and (abs(funSec - x1)) >= (abs(x2 - d) / 2)) or
            (validacion == True and (abs(x1 - x2)) < Tol) or
            (validacion == False and (abs(x2 - d)) < Tol)):
            # En esta parte del algortimo se usa el método de bisección
            funSec = (x0 + x1) / 2
            validacion = True

        else:
            validacion = False

        ffunSec = f(funSec)
        d, x2 = x2, x1

        if (fx0 * ffunSec) < 0:
            x1 = funSec
        else:
            x0 = funSec

        if abs(fx0) < abs(fx1):
            x0, x1 = x1, x0

        nIter += 1

    return x1, nIter

if __name__ == '__main__':
    funcion1 = lambda x: ((x**3)-(2*( x**2))+((4*x)/3)-(8/27))
    raiz, iteraciones= MetodoBrent(funcion1, 0, 1,50, Tol=10e-5)
    print ("La raiz del polinomio x³−2x²+4x/3−8/27 es :",raiz)
    print ("El número de iteraciones alcanzadas es :", iteraciones)
    
   
    pylab.title("iteraciones vs tolerancia(e⁻⁷) Brent (x³−2x²+4x/3−8/27) en intervalo (0 ,1 )")
    pylab.plot(nIteraciones,errorI,color="green", linewidth=2.5, linestyle="-", label="Brent")
    pylab.legend(loc='upper right')
    #pylab.plot(nIteraciones,errorI)
    pylab.xlabel('(x) iteraciones ')
    pylab.ylabel('(y) tolerancia') 
    pylab.show()











"""
adaptado del algoritmo 
Realizado por: Nick Ryan

"""