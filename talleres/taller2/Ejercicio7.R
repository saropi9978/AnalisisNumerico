# Ejercicio 9
# Parte A - Encuentre los valores de Alpha y Beta de la matriz A para asegurar la convergencia de Jacobi
# Convergencia de Jacobi -> A debe ser 'estrictamente diagonal dominante'

require(BB)
require(Matrix)
require(pracma)

beta  <- 0
alpha <- 3

A = matrix(c( 2,0,-1,
              beta,2,-1,
              -1,1,alpha),nrow=3,byrow=TRUE)
print(A)

b = matrix (c(1,2,1),nrow=3, byrow=TRUE)
Ab = cbind(A,b)
print(Ab) # Aca se puede verificar de forma visual la condicion de convergencia.

sol1 = solve(A,b) # Reemplazar solve por Jacobi!!!!
print(sol1)

# Parte B - Genere una tabla que tenga 10 iteraciones

toleracia=1e-9

solJacobi=itersolve(A, b, x0 = c(1,2,3), nmax = 10, toleracia, method = c("Jacobi"))
print(solJacobi)