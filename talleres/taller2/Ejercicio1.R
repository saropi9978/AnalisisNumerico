
# Ejercicio 1
# Parte B

# b. Evalue la matriz de transición para el método $\textbf{SOR}$ 
#     y de $Jacobi$      
#   
#   ```{r,echo=T}
# D1<-eye(n, m = n)
# D2<-ones(n, m = n)
# D3<-zeros(n, m = n)
# A = matrix(c(-8.1, -7, 6.123, -2, -1, 4,
#              -3, -1, 0, -1, -5, 0.6,
#              -1, 0.33, 6, 1/2), nrow=4, byrow=TRUE)
# A
# ```

# NOTA: Se debe instalar 'pracma' y 'Matrix' para calcular las tringular superior/inferior


require(pracma)
require(Matrix)

n = 4 # Matriz con dimensiones 4x4

D1<-eye(n, m = n)
D2<-ones(n, m = n)
D3<-zeros(n, m = n)

A = matrix(c(-8.1, -7, 6.123, -2, -1, 4,
                           -3, -1, 0, -1, -5, 0.6,
                           -1, 0.33, 6, 1/2), nrow=4, byrow=TRUE)
print(A)

b = matrix(c(1.45,3,5.12,-4), nrow=n, byrow=TRUE)
print(b)

# METODO sOR

diago <- function(M) { # Obtener Diagonal
  
  M[col(M)!=row(M)] <- 0
  
  return(M)
}


D = diago(A) #Diagonal D para matriz A
#D = diag(diag(A^-1))
L = tril(A,k=-1,diag = FALSE) # Triangular inferior de la matriz A
U = triu(A,k=1,diag = FALSE) # Triangular superior de la matriz A

sum = L+U
sol1 = (-solve(D))
print(sol1)

T = (sol1)%*%(L+U)
#T = round((sol)%*%(sum),4)

print(T)
#print(round(norm(T,"F"),4))

# METODO JACOBI
