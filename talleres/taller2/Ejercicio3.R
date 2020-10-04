#Ejercicio 3
#
#
#3. Sea el sistema $AX=b$ dados en ejercicio,y  con tol= e^-8        
#a. Implemente una función en R para que evalue las raíces del polinomio característico asociado a la matriz $A$    
#  b. Use el teorema de convergencia para determinar cuál método iterativo es más favorable.  
#c. Evalue la matriz de transición para cada caso (método) y en el caso del método de relajación determine el valor óptimo de $\omega$      
#  d. Teniendo en cuenta lo anterior resolver el sistema   
#e Comparar con la solución por defecto       
#f. Evaluar el número de condición de la matriz A    
#g. Evaluar el efecto en la solución si la entradad $a_{11}=4.01$ aplicar cambio y solucionar. Después, debe comparar con el valor condicón   

#```{r, echo=T}
#A = matrix(c(4, -1, -1, -1, -1, 4,
#             -1, -1, -1, -1, 4, -1,
#             -1, -1, -1, 4), nrow=4, byrow=TRUE)
#A
#b = c(1.11111, 5, 1.5,-2.33)
#b
#```
rm(list=ls())
library(pracma)
library(Matrix)

#Punto A
A = matrix(c(4, -1, -1, -1, -1, 4,
             -1, -1, -1, -1, 4, -1,
             -1, -1, -1, 4), nrow=4, byrow=TRUE)
print(A)
b = c(1.11111, 5, 1.5,-2.33)
print(b)

qr.solve(A,b)

#punto B





# Parte B


# Matriz A
#Punto A
A = matrix(c(4, -1, -1, -1, -1, 4,
             -1, -1, -1, -1, 4, -1,
             -1, -1, -1, 4), nrow=4, byrow=TRUE)
print(A)
b = c(1.11111, 5, 1.5,-2.33)
print(b)

# Ahora vamos a evaluar la solucion con cada uno de los metodos iterativos y determinaremos cual es mas favorable
# Teniendo en cuenta que ambos son algoritmos lineales entonces tienen una complejidad de O(n)

toleracia=1e-9
# Por Gauss-Seidel

solGS=itersolve(A,b,x0=NULL,nmax = 1000,toleracia,method = "Gauss-Seidel")
print(solGS)

# Por Jacobi

solJacobi=itersolve(A, b, 1:4,nmax = 1000, toleracia, method = c("Jacobi"))
print(solJacobi)

# Por Richardson
solRichar=itersolve(A, b, x0 = NULL, nmax = 1000, toleracia, method = c("Richardson"))
print(solRichar) 

print("Como se puede observar por la cantidad de iteraciones el metodo de gauss-sediel es mas rapido\nlo que quiere decir que converge mas rapido que los algoritmos jacobi y richardson ")


#Punto c

A = matrix(c(4, -1, -1, -1, -1, 4,
             -1, -1, -1, -1, 4, -1,
             -1, -1, -1, 4), nrow=4, byrow=TRUE)
print(A)
b = c(1.11111, 5, 1.5,-2.33)
print(b)

# w grado de relajación 0<w<2
fSOR<-function(a,n,w){
  D=a*eye(n, m = n)
  L<-a
  L[lower.tri(L, diag = FALSE)]<-0
  auxT=(D-(w*L))
  auxT1=inv(auxT)
  U<-a
  U[upper.tri(U, diag = FALSE)]<-0
  auxT2=((1-w)*D+(w*U))
  Tfinal=auxT1*auxT2
}
#fSOR(A,4,1)
#Jacobi
#se realiza la separacion de jacobi entre D, L, U y el resultado es la sumatoria de todas estas divisiones.
jacobi<-function(a,n){
  D=a*eye(n, m = n)
  L<-a
  L[lower.tri(L, diag = FALSE)]<-0
  U<-a
  U[upper.tri(U, diag = FALSE)]<-0
  AA=D+L+U
  print(AA)
}
jacobi(A,4)

#Punto d
solucion<- solve(A,b)
print(solucion)
