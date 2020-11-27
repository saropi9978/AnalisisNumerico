library(PolynomF)
require(deSolve)

rm(list=ls())
euler1 = function(f, t0, y0, h, n) {
  #Datos igualmente espaciados iniciando en x0 = a, paso h. "n" datos
  #f es la derivada es decie dy/dt =f(t,y)
  t = seq(t0, t0 + (n-1)*h, by = h) # n datos
  y = rep(NA, times=n) # n datos
  y[1]=y0
  for(i in 2:n ) y[i]= y[i-1]+h*f(t[i-1], y[i-1])
  print(cbind(t,y)) # print
  plot(t,y, pch=19, col="red", xlab = "ti", ylab = "solución",
       main = "Euler vs RK4")
}
options(digits = 15)
f = function(t,y) (0.7*y)-(t^2)+1
euler1(f, 1, 1, 0.1, 10)
###


#install.packages("deSolve")######################################

fp = function(t,y, parms){
  s = (0.7*y)-(t^2)+1
  return(list(s)) # #ode requiere salida sea una lista
}
tis= seq(1,2,0.1)# Usamos la funcion ode()
sol = ode(c(1,1), tis, fp, parms=NULL, method = "rk4")# metodo Runge Kutta orden 4 # Salida
tabla = cbind(tis, sol[,2] )
colnames(tabla) = c("ti", " Ti ")
tabla
# Representacion
par(new=T)
plot(tis, sol[,2],
     xlab = "ti",
     ylab = "solucion", main = "Euler vs RK4")
a=poly_calc(tis,sol[,2])
curve(a,add=T)
abline(h=0,v=0,col="red")
print(a)

