#Metodo de biseccion para encontrar CEROS 
#Agosto2020 Eherrera
import pylab as pylab
import math
def f(x):
    return (9*math.sin(x))-(8*math.sin(2*x))-(3*math.sin(3*x))-4#funcion encontrar raices
errorI=[]
iteraciones=[]
def bisection_method(a, b, tol):#el intervalo de busqueda[a,b]
#tol=tolerancia como criterio de parada
    if f(a)*f(b) > 0:#sin son de igual signo no hay raiz en [a,b]
        #Fin del proceso, no hay raiz en [a,b].
        print("No se encontro raiz.")
    
    else:
        it=0
        
        while (a + b)/2.0 > tol:
            errorI.append((a + b)/2.0)
            iteraciones.append(it)
            puntomedio = (a + b)/2.0
            
            if f(puntomedio) == 0:
                print(it)
                return(puntomedio) #TElpunto medio es el intercepto en x /raiz
            elif f(a)*f(puntomedio) < 0: #Caso creciente pero, por debajo de 0
                b = puntomedio
            else:
                a = puntomedio
            it+=1
        return puntomedio
 
Prueba = bisection_method(0, 1, 0.000001)
print(Prueba)

pylab.title("Iteraciones vs Error Caso tres.")
#pylab.plot(nIteraciones,errorI)
pylab.xlabel('(x) iteraciones ')
pylab.ylabel('(y) error')
#pylab.plot(nIteraciones,errorI, color="blue", linewidth=2.5, linestyle="-", label="Punto fijo")
pylab.plot(iteraciones, errorI, color="red",  linewidth=2.5, linestyle="-", label="Biseccion") 
pylab.legend(loc='upper right')
pylab.show()
 
print("Prueba:", round(Prueba, 6))