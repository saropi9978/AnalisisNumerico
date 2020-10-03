#Ejercicio 8

#NOTA: Se debe instalar pracma y Matrix para calcular las triangulares inferiores y superiores

require(pracma)
require(Matrix)

n = 4 # Matriz con dimensiones 4x4

D1<-eye(n, m = n)
D2<-ones(n, m = n)
D3<-zeros(n, m = n)

# Matriz A del ejercicio 2

A = matrix(c(-8.1, -7/4, 6.1, -2,
             -1, 4, -3, -1,
             0, -1, -5, 0.6,
             -1, 1/3, 6, 1/2), nrow=4, byrow=TRUE)
print(A)

# Descomposicion de matriz A en A=LU

ludec <- lu(A)
LU_Desc <- expand(ludec)

L <- LU_Desc$L # L = Matriz triangular inferior
print(L)

U <- LU_Desc$U # U = Matriz triangular superior
print(U)

#D <- diag(diag(A))
#print(D)

A1 = L %*% U # Multiplicamos para verificar
print(A1)

# Factorizacion de matriz A en A=QR
# Q = Matriz ortogonal (Q^T * Q = I)
# R -> U = Matriz triangular superior
# Estas matrices se obtienen por medio de Gram-Schimidt

QR <- gramSchmidt(A)
print(QR)

Q <- QR$Q
print(Q)

R <- QR$R
print(R)

A2 = Q %*% R # Multiplicamos para verificar
print(A2)