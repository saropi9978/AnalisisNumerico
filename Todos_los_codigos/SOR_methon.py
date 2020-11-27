import numpy as np

def sor_solver(A, b, omega, initial_guess, convergence_criteria):
  """
  This is an implementation of the pseduo-code provided in the Wikipedia article.
  Inputs:
    A: nxn numpy matrix
    b: n dimensional numpy vector
    omega: relaxation factor
    initial_guess: An initial solution guess for the solver to start with
  Returns:
    phi: solution vector of dimension n
  """
  phi = initial_guess[:]
  residual = np.linalg.norm(np.matmul(A, phi) - b) #Initial residual
  while residual > convergence_criteria:
    for i in range(A.shape[0]):
      sigma = 0
      for j in range(A.shape[1]):
        if j != i:
          sigma += A[i][j] * phi[j]
      phi[i] = (1 - omega) * phi[i] + (omega / A[i][i]) * (b[i] - sigma)
    residual = np.linalg.norm(np.matmul(A, phi) - b)
    print('Residual: {0:10.6g}'.format(residual))
  return phi


#An example case that mirrors the one in the Wikipedia article
residual_convergence = 1e-8
omega = 0.5 #Relaxation factor

A = np.array([[15., -4., -3., 8.],
          [-4., 10., -4., 2.],
          [-3., -4., 10., 2.],
          [8., 2., 2., 12.]
          ])
# vector b
b = np.array([2., -12., -4., 6.])

initial_guess = np.zeros(4)

phi = sor_solver(A, b, omega, initial_guess, residual_convergence)
print(phi)