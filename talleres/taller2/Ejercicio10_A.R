#Ejercicio 10 - Parte A
#NOTA: Se debe instalar lib BB

require(BB)

sistema = function(x){
  f = rep(NA,length(x))
  f[1] = x[1]^2+x[2]^2-1
  f[2] = x[1]-x[2]
  f
}

p0 = c(1,1)
sol1=BBsolve(par=p0, fn=sistema) # msg: Succesful convergence
cat("Solucion inicial de (1,1): \n",sol1[[1]],"\n")
p0 = c(-1,1)
sol2=BBsolve(par=p0, fn=sistema) # msg: Succesful convergence
cat("Solucion inicial de (-1,1): \n",sol2[[1]],"\n")

# Las soluciones para x^2+y^2=1 son:
# y1 = sqrt(1-x^2); y2 = sqrt(1-x^2) -- Con Centro en (0,0)

f1=function(x){
  sqrt(1-x^2)
}
f2=function(x){
  -sqrt(1-x^2)
}
f3=function(x){
  x
}

# Al resover x^2 + y^2 = 1 respecto a la recta y=x, se obtienen
# los siguientes puntos:
#   x1=(1/sqrt(2)); x2=(-1/sqrt(2))
#   Al radicalizar +- (1/sqrt(2)), se obtiene (sqrt(2)/2)

x=seq(-1,1,0.00001) # Con una tolerancia de 10e-6
plot(x,f3(x),type="l",col="red")
abline(h=0,col="blue") # Eje X
lines(x,f1(x),type="l",col="green") # Circunferencia arriba del eje X
lines(x,f2(x),type="l",col="green") # Circunferencia por debajo del eje X
points(rbind(c(sqrt(2)/2,sqrt(2)/2)),pch=17,cex=1.5,col="red") # Puntos de Interseccion
points(rbind(c(-sqrt(2)/2,-sqrt(2)/2)),pch=17,cex=1.5,col="red") # Puntos de Interseccion