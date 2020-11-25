library(deSolve)
  library(ggplot2)
  #tamaño poblacional
  
  #estado inicial de los compartimentos
  init2 <- c(S = 990,
             I = 5,
             R = 0,
             V= 0,
             E = 5)
  #parámetros del modelo (coeficientes de las variables)
  param2 <- c(
    L = 10,
    miu = 0.001,
    beta = 0.0005,
    alpha =  0.1,
    gammaa=0.0010,
    epsilon=0.0010,
    siggma = 0.0014,
    delta= 0.001,
    rho=0.00003)
  #crear la función con las ODE
  
  N <- sum(init)
  
  sir2 <- function(times, init, param) {
    with(as.list(c(init, param)), {
      #ecuaciones diferenciales   
      dS <- (miu*N) - (rho*S*I) - (miu*S) -(siggma*S) + (epsilon*V) + (delta*R)
      dE <- (rho*S*I) - ((miu+alpha)*E)
      dI <- (alpha*E) - ((miu+gammaa)*I)
      dR <- (gammaa*I) - ((miu+delta)*R)
      dV <- (siggma*S) - ((miu+epsilon)*V)
      
      #resultados de las tasas de cambio    
      return(list(c(dS, dE, dI, dR, dV)))
    })
  }
  #intervalo de tiempo y resolución
  times2 <- seq(0, 1000, by = 1)
  #resolver el sistema de ecuaciones con función 'ode'
  sol2 <- ode(y = init2, times = times2, func = sir2, parms = param2, method="euler")
  #cambiar out a un data.frame
  sol2 <- as.data.frame(out2*N) #aqui puede multiplicar 'out' por N
  #eliminar la variable 'time' en out
  sol2$time <- NULL
  #mostrar 10 primeros datos
  head(out2, 1000)
  
  # 
  # # ggplot(iris,aes(x = times, y = out2))+ geom_point() + geom_smooth()
  # matplot(x = times, y = out1, type = "l",
  #         xlab = "Tiempo", ylab = "Poblacion (S, E, I, R, V)", main = "Datos Exp",
  #         lwd = 1, lty = 1, bty = "l", col = 2:4)
  # añadir leyenda de líneas
  #legend(100, 0.1, c("Susceptibles", "razon de cambio nodos expuestos", "Infectados","Recuperados Sin vacuna","recuperados vacunados"),pch = 1, col = 2:4, bty = "n", cex = 1)
  # 
  # plot(times, S, type="l", col="blue", ylim=c(0,N), xlab="Tiempo (en horas)", ylab="Numero de Personas",main = "Metodo 1: Runge Kutta 4")
  # lines(times, I, type="l", col="red")
  # lines(times, R, type="l", col="green")
  
  
  #out1%>%gather(variable,value,-time)%>%ggplot(aes(x=time,y=value,color=variable))+geom_line(size=2)+theme_classic()+labs(x='time (yr)',y='number of individuals')
  