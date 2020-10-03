#Ejercicio 10 - Parte B

#NOTA: Se debe instalar lib BB

library("BB")
require(BB)

# Funcion 1: 3x^2+2y-5+sin(x-y)*sin(x+y)

trigexp = function(x) {
  n = length(x)
  F = rep(NA, n)
  
  # Ecuaciones del sistema
  F[1] = 3*x[1]^2 + 2*x[2] - 5 + sin(x[1] - x[2]) * sin(x[1] + x[2])
  
  tn1 = 2:(n-1) # Esto actua como un 'for in range(2,n-1)' = Secuencia de 2
                # hasta n-1 para los valores de X
  
  # Se establece el siguiente sistema de ecuciones:
  # se ingresan tn1 ecuaciones que iran desde 2 hasta n-1
  F[tn1] = -x[tn1-1] * exp(x[tn1-1] - x[tn1]) + x[tn1] *
    ( 4 + 3*x[tn1]^2) + 2 * x[tn1 + 1] + sin(x[tn1] -
                                               x[tn1 + 1]) * sin(x[tn1] + x[tn1 + 1]) - 8
  
  # Como la anterior evalua hasta n-1, aca se evalua la ecuacion para n
  F[n] = -x[n-1] * exp(x[n-1] - x[n]) + 4*x[n] - 3  # Esta ecuacion puede ser descrita como:
                                                    # -z * e^(z-w) + 4z - 3
  F # Retornamos
}

n = 10000 # Cantidad de numeros aleatorios para la ecuacion - Aca serian 10000 casos para evaluar la efectividad del metodo
p0 = runif(n) # Genera 'n' numeros aleatorios para los "valores iniciales" para F
sol = BBsolve(par=p0, fn=trigexp)
sol$par # 10mil Soluciones
# [1] 1 1 1 1 1 .......