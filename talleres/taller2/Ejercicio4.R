#4. Pruebe el siguiente algoritmo con una matriz $A_{3}$, modifiquelo para quue $a_{ii}=0$ para todo $i$

tril1 <- function(M, k)
{
  if (k != 0) {
    M[!lower.tri(M, diag = TRUE)] <- 0
    M[!upper.tri(M, diag = TRUE)] <- 0
  } 
  else {
    M[col(M) == row(M) + k ] <- 0
  }
  return(M)
}
M = matrix(c(9,7,4,
             10,9,5,
             6,8,7,
             2,1,4), nrow = 4, byrow = TRUE)
r<- tril1(M, 0)
print("Resultado de la funcion:")
print(r)