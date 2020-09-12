"""
Adaptado y Modificado por:
 - Santiago Romero
 - Sandra Chavez
 - Ricardo Bernal
"""

def derivar(coeficientes):
	polinomio=len(coeficientes)-1
	derivada=[]
	for i in range(0,len(coeficientes)-1):
		derivada.append(coeficientes[i]*polinomio)
		polinomio-=1
	print(derivada)
	return derivada

def horner(coeficientes,x):
	resultado = 0
	for i in range(0,len(coeficientes)):
		resultado = resultado * x + coeficientes[i]
	return resultado
	
x=2

coeficientes=[1,1,1,1]
primera_derivada=derivar(coeficientes)
segunda_derivada=derivar(primera_derivada)

print("Resultado polinomio original:"+ str(horner(coeficientes,x)))
print("Resultado primera derivada:"+ str(horner(primera_derivada,x)))
print("Resultado segunda derivada :"+ str(horner(segunda_derivada,x)))
