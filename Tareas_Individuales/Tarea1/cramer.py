"""
Realizado por:
    -Santiago Romero Pineda
"""

import numpy as np
import random
#Prueba
n=int (input("digite el tamaño de la matriz: "))
def generarArreglos(n): 
    matriz= ([[0 for j in range(n)] for i in range(n)])
    res= ([0 for i in range(n)])
    return np.array(matriz), np.array(res)



def generarMatrices():
    for i in range (n):
        for j in range (n):
            matriz[i][j]=round(random.randint(1,10),4)
        res[i]=round(random.randint(1,10),4)


def sol_cramer(A,B,R=[]):
    
    matriz_aux = A.copy() 

    for i in range(0,len(B)):
        for j in range(0,len(B)):
            matriz_aux[j][i]=B[j]
            if i>0:
                matriz_aux[j][i-1]=A[j][i-1]
        R.append(round(np.linalg.det(matriz_aux)/np.linalg.det(A),8))
    return R




#ejercicio1
# matriz=np.array(([[1,1],[0.0001,1]]))
# res= np.array(([2,1]))
#n=2


#ejercicio3
matriz=np.array(([[4,-1,-1],[-1,4,-1],[-1,-1,4]]))
res= np.array(([1,2,3]))
n=3


#ejercicio4
# matriz=np.array(([[2.6,0.3,2.4,6.2],[7.7,0.4,4.7,1.4], [5.1,9.9,9.5,1.5],[6.0,7.0,8.5,4.8]]))
# res= np.array(([50.78,47.36,91.48,98.17]))
#n=4
#matriz,res = generarArreglos(n)
#generarMatrices()


print(matriz)
print("Solucion Directa Exacta")
X = np.linalg.solve(matriz,res)
print(X)


print("Solucion por Cramer")

resultado = sol_cramer(matriz,res)
print(resultado)


"""
referencias:
    -https://youtu.be/DQN4tjbGDfw

"""
