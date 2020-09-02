"""
Realizado por:
 - Santiago Romero
 - Sandra Chavez
 - Ricardo Bernal
"""
import math
import pylab as pylab
"""
Usar un numero N bajo de iteraciones e ir incrementando
este numero en caso de no encontrar la raiz
"""
errorI=[]

nIteraciones=[]
def punto_fijo(f, x_0, TOL, fd, ite=10000000000 ):
    error = 0.004
    iteraciones=0
    #if abs(fd(x_0))>1:
    #    print ("no converge")
    #    return  
    while error >= TOL and iteraciones <= ite :  
        errorI.append(error)
        
        x_i = f(x_0)
        error = abs(x_i - x_0)
        print("E_i:",errorI[len(errorI)-1], " e_i+1: ", error)
        nIteraciones.append(iteraciones)
        x_0 = x_i
        iteraciones += 1
        
        #print(f'p{iteraciones} = {x_0: 0.20f}')
    print(f'Raiz: {x_0} \n Iteraciones: {iteraciones}')


if __name__ == '__main__':
    
    f1D= lambda x: -(math.sin(4*x)/math.sqrt(math.cos(2*x)**2)) #Ejercicio 1 derivada
    f1 = lambda x: (math.cos(2*x)**2) - x**2   #Ejercicio 1
    f2D = lambda x: (-(math.cos(x)/math.sin(x))*(1/math.sin(x)) ) #Ejercicio 2 derivada
    f2= lambda x: (1/(math.sin(x)))#Ejercicio 2
    f3D = lambda x: -((9*(x**2))/4) + 3*x  #Ejercicio 3 derivada
    f3 = lambda x: ((-3/4)*(x**3)) + ((3/2)*(x**2)) + (2/9) #Ejercicio 3
    
    #(punto_fijo(f1, 0, 1e-8, f1D,100000000))
    #(punto_fijo(f2, 1, 1e-8, f2D))
    (punto_fijo(f3, 1, 1e-8, f3D))
    #print(nIteraciones)
    #print(errorI)
    #pylab.title("iteraciones vs error C.")
    #pylab.plot(nIteraciones,errorI)
    #pylab.xlabel('(x) iteraciones ')
    #pylab.ylabel('(y) error') 
    #pylab.show()
