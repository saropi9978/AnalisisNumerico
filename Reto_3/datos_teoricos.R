library(deSolve)
#tamaño poblacional

#estado inicial de los compartimentos
init <- c(S = 990,
          I = 5,
          R = 0,
          V= 0,
          E = 5)
#parámetros del modelo (coeficientes de las variables)
param <- c(
  L = 10,
  miu = 0.001,
  beta = 0.0003,
  alpha =  0.0004,
  gammaa=0.0025,
  epsilon=0.0010,
  siggma = 0.0014,
  delta= 0.001,
  phi=0.00003) # Con r = 2, L = 10
#crear la función con las ODE

N <- sum(init)

sir <- function(times, init, param) {
  with(as.list(c(init, param)), {
    #ecuaciones diferenciales   
    dS <- (miu*N) - (phi*S*I) - (miu*S) -(siggma*S) + (epsilon*V) + (delta*R)
    dE <- (phi*S*I) - ((miu+alpha)*E)
    dI <- (alpha*E) - ((miu+gammaa)*I)
    dR <- (gammaa*I) - ((miu+delta)*R)
    dV <- (siggma*S) - ((miu+epsilon)*V)
           
    #resultados de las tasas de cambio    
    return(list(c(dS, dE, dI, dR, dV)))
  })
}
#intervalo de tiempo y resolución
times <- seq(0, 1000, by = 1)
#resolver el sistema de ecuaciones con función 'ode'


out1 <- ode(y = init, times = times, func = sir, parms = param, method="rk4")
#cambiar out a un data.frame
out1 <- as.data.frame(out1*N) #aqui puede multiplicar 'out' por N
#eliminar la variable 'time' en out
out1$time <- NULL
# #mostrar 10 primeros datos
#head(out1, 100)

out1 <- ode(y = init, times = times, func = sir, parms = param, method="adams")
#cambiar out a un data.frame
out1 <- as.data.frame(out1*N) #aqui puede multiplicar 'out' por N
#eliminar la variable 'time' en out
out1$time <- NULL
#mostrar 10 primeros datos
head(out1, 100)

summary(out1)


# SEGUNDO MODELO

# Basado en "Mathematical model on the transmission of worms in wireless sensor network"

# Valores iniciales
init2 <- c(S = 990,
           I = 5,
           R = 0,
           V= 0,
           E = 5)
# Parametros del Modelo
param2 <- c(
  L = 10,
  miu = 0.001,
  beta = 0.0005,
  alpha =  0.4,
  gammaa=0.0010,
  epsilon=0.0010,
  siggma = 0.0014,
  delta= 0.001,
  rho=0.00003)

# Poblacion Inicial
N <- sum(init2)

# Sistema de ecuaciones
sir2 <- function(times, init, param) {
  with(as.list(c(init, param)), {
    # ODE 
    dS <- (miu*N) - (rho*S*I) - (miu*S) -(siggma*S) + (epsilon*V) + (delta*R)
    dE <- (rho*S*I) - ((miu+alpha)*E)
    dI <- (alpha*E) - ((miu+gammaa)*I)
    dR <- (gammaa*I) - ((miu+delta)*R)
    dV <- (siggma*S) - ((miu+epsilon)*V)
    
    # Resultado ODE
    return(list(c(dS, dE, dI, dR, dV)))
  })
}

# Intervalo
times2 <- seq(0, 1000, by = 1)

# Resolucion del ODE
sol2 <- ode(y = init2, times = times2, func = sir2, parms = param2, method="adams")

# Paso a Data Frame
sol2 <- as.data.frame(sol2*N)

# Eliminacion de Time
sol2$time <- NULL

# Mostrar primeros datos
head(sol2, 100)