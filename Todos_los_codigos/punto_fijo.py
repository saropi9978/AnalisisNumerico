from sympy import  sympify, symbols, Abs, sqrt, cos
import math
import time
from scipy import optimize

x=symbols('x')

start_time = time.time()
print(time.ctime( start_time) )

#a)
def funcionA():
    return sympify(' (cos(2*x)**2) - (x**2) ') #original

#B
def funcionB():
    return sympify('(x*sin(x))-1') #original

#C
def funcionC():
    return sympify('((-3/4)*(x**3)) + ((3/2)*(x**2)) + (2/9)')#original
    





# funcion punto fijo
def puntoFijo(vInicial,tolerancia, n_iteraciones=1000000000):
    global x
    #ecua=funcionA()
    #ecua=funcionB()
    ecua=funcionC()
    x_r=ecua.evalf(subs={x:vInicial})
    error= 100
    while error>=tolerancia and n_iteraciones>=0 :
        n_iteraciones-=1
        print(n_iteraciones)
        x_anterior=x_r
        x_r=ecua.evalf(subs={x:x_anterior})
        error= abs((x_r-x_anterior))
        print("valor x_i+1:", x_r )
        print("valor x_i:", x_anterior )
        print("resta:",x_r  - x_anterior )
        print("error:",error)
    return x_r

print(puntoFijo(0,10e-8,1000000))


    

  
#print(optimize.minpack.fixed_point(funcionCC, 1))



print("tiempo que transcurrido: ", (time.time() - start_time))