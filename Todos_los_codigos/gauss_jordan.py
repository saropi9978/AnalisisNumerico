import numpy
import random
import time
"""
Modificado y mejorado por:
    -Santiago Romero pineda
"""

n=int (input("digite el tamaño de la matriz: "))
start_time = time.time()
print("tiempo inicial",time.ctime( start_time) )

def generarArreglos(n): 
    matriz= ([[0 for j in range(n)] for i in range(n)])
    res= ([0 for i in range(n)])
    return matriz,res

matriz,res = generarArreglos(n)

def generarMatrices():
    for i in range (n):
        for j in range (n):
            matriz[i][j]=round(random.randint(1,10),4)
        res[i]=round(random.randint(1,10),4)

def gauss(n):
    for z in range(n - 1):
        for x in range(1, n - z):
            if (matriz[z][z] != 0):
                p = matriz[x + z][z] / matriz[z][z]
                for y in range(n):
                    matriz[x + z][y] = matriz[x + z][y] - (matriz[z][y] * p)
                res[x + z] = res[x + z] - (res[z] * p)

def gjordan(n):
        for z in range(n - 1, 0, -1):
            for x in range(z):
                if (matriz[z][z] != 0):
                    p = matriz[x][z] / matriz[z][z]
                    matriz[x][z] = matriz[x][z] - (matriz[z][z] * p)
                    res[x] = res[x] - (res[z] * p)

def sol(n):
    print("\n")
    for i in range(n):
        if (matriz[i][i] != 0):
            ms = True
        else:
            ms = False
            break
    if (ms == True):
        for i in range(n):
            print("El valor de x" + str(i) + ' es = ' + str(res[i] / matriz[i][i]))
    else:
        print('La matriz no tiene solucion')
def det(n):
    deter = 1
    for x in range(n):
        deter *= matriz[x][x] 
    print('\nEl determinante de la matriz es = ', deter)


#generarMatrices()


#ejercicio1
# matriz=([[1,1],[0.0001,1]])
# res= ([2,1])
# n=2


#ejercicio3
# matriz=([[4,-1,-1],[-1,4,-1],[-1,-1,4]])
# res= ([1,2,3])
# n=3


#ejercicio4
matriz=([[2.6,0.3,2.4,6.2],[7.7,0.4,4.6,1.4], [5.1,9.9,9.5,1.5],[6.0,7.0,8.5,4.8]])
res= ([50.78,47.36,91.48,98.17])
n=4

print("resolver A*x = B")
print(numpy.array(matriz), "X = ", res)

gauss(n)
gjordan(n)
sol(n)
det(n)


print("tiempo transcurrido: ", (time.time() - start_time))











"""
Referencias y fuentes: 
    - https://es.stackoverflow.com
    
"""