#9. Realice varias pruebas que la matriz de transición por 
#el método de Gauss-Seidel esta dada por $T=(-D^{-1}U)(I+LD^{-1})^{-1}$    



N <- 3
A <- Diag(rep(3,N)) + Diag(rep(-2, N-1), k=-1) + Diag(rep(-1, N-1), k=1)
x0 <- rep(0, N)
B = c(4,5,9)

itersolve(A, B, tol=1e-7 , method = "Gauss-Seidel")