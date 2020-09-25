"""
Realizado por:
 - Santiago Romero
 - Sandra Chavez
 - Ricardo Bernal
"""

import math
import numpy as np 
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

a=[1 for i in range(50)]
x=1.00000000001
resultado=horner(a,x)


# Conversion de numeros decimales (con float) a binario

def float_binario(numero):
    
    nEntero, nDecimal = str(numero).split(".")
    
    entero = decimal_a_binario(int(nEntero))
    decimal = decimal_a_binario(int(nDecimal))

    resultado = str(entero) + "." + str(decimal)

    return resultado

def decimal_a_binario(num): 
      
    bin_number = 0
    contador = 0
    while (num != 0): 
        residuo = num % 2
        c = pow(10, contador)  
        bin_number += residuo * c  
        num //= 2
          
        # Count used to store exponent value  
        contador += 1
      
    return bin_number  
  
# Conversion de binario a decimal (con float)

def binario_float(numero):

    nEntero, nDecimal = str(numero).split(".")
    
    entero = binario_a_decimal(int(nEntero))
    decimal = binario_a_decimal(int(nDecimal))

    resultado = str(entero) + "." + str(decimal)

    return resultado

def binario_a_decimal(bin):
    
    decimal, i,  = 0, 0
    while(bin != 0): 
        dec = bin % 10
        decimal = decimal + dec * pow(2, i) 
        bin = bin//10
        i += 1
    return decimal



# MAIN

print("Ejercicio. \n Evaluar el polinoio en x= 1.00000000001 conP(x) = 1 +x+x²+...+x⁵⁰ y la primera derivada.\nEncuentreel error de c ́alculo al comparalo con los resultados de la expresi ́on equivalenteQ(x) = (x⁵¹−1)/(x−1)\n")
print("resultado de la original: ",resultado[0])
print("resultado de la derivada: ",resultado[1])
print("Resultado de  Q(x): ",((1.00000000001**51)-1)/(1.00000000001-1),"\n")
# a)
print("a) Encuentre los primeros 15 bits en la representacion binaria de π \n")

n1 = np.round(np.pi, 15)
print("Primeros 15 digitos de π: ", n1)
res = float_binario(n1)
print("Primeros 15 digitos de π en binario: ", res,"\n")

# b)
print("b) Convertir los siguientes numeros binarios a base 10: 1010101; 1011.101; 10111.010101...; 111.1111\n")
n1, n2, n3, n4 = 1010101, 1011.101, 10111.010101, 111.1111

print(binario_a_decimal(n1))
print(binario_float(n2))
print(binario_float(n3))
print(binario_float(n4),"\n")

# c)
print("c) Convierta los siguientes numeros de base 10 a binaria:\n-11.25\n-2/3\n-30.6\n-99.9\n")
n1, n2, n3, n4 = 11.25, (2/3), 30.6, 99.9

print(float_binario(n1))
print(float_binario(n2))
print(float_binario(n3))
print(float_binario(n4),"\n")


