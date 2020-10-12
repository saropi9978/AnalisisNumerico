#5. Cree una función que cuente el número de multiplicaciones
#en el método directo de Gauss-Jordan, para resolver 
#un sistema de $n$ ecuaciones y pruebelo para $n=5$


GaussJordanM = function(A, B){ # Se supone det(A) != 0
  numMult = 0
  n = nrow(A) # = ncol(A) para que sea cuadrada
  
  # matriz ampliada
  Ab = cbind(A,B)
  print(Ab)
  # Eliminación
  for (k in 1:(n-1)){ # desde columna k=1 hasta k=n-1
    if(Ab[k,k]==0){ # intercambio de fila
      fila = which(Ab[k, ]!=0)[1]
      Ab[c(k, fila), ] = Ab[c(fila, k), ]
    }
    
    # Eliminación columna k
    for (i in (k+1):n){# debajo de la diagonal
      # Fi = Fi - a_ik/a_kk * Fk, i=k+1,...,n
      Ab[i, ] = Ab[i, ] - Ab[i, k]/Ab[k,k]*Ab[k, ]
      numMult = numMult + 2*(ncol(Ab))
    }
  }
  
  # Sustitución hacia atrás-------------------------
  x = rep(NA, times=n)
  x[n] = Ab[n, n+1]/Ab[n,n]
  numMult = numMult + n+1
  
  for(i in (n-1):1 )
    {
    x[i]= (Ab[i, n+1] - sum(Ab[i, (i+1):n]*x[(i+1):n]) ) /Ab[i,i]
    numMult = numMult + 2*(n-2)
    }

  cat("Numero de Multiplicaciones del ejercicio:", numMult, "\n")
  return(x)
}

A = matrix(c( 0, 1,1,1,1,
              -5, -4, 3, 4, 8,
              0, 7, -2, 3, 7,
              -1, -7, -8, 3,7,
              3, 7, 5, 5, 9), nrow=5, byrow=TRUE)
B = matrix(c(1,0,0,0,1), nrow=5, byrow=TRUE)

cat("Solucion ejercicio Punto  5: ","\n")
GaussJordanM(A,B)