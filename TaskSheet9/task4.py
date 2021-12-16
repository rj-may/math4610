
import sys
sys.path.insert(0, '../lib/')

from matrix.vecNorms import l2NormErr
from matrix.matrixOps import matrixVectMult

def jacobiIteration(A, b, x0, tol, maxIter):
    n = len(b)
    error = 10 * tol
    iter = 0
    r = [None for i in range(len(x0))]
    x1 = [None for i in range(len(x0))]
    while(error > tol and iter < maxIter):
        # Residual 
        for i in range(n):
            r[i] = b[i]
            for j in range(n):
                r[i] = r[i] - A[i][j]* x0[j]
        # Update
        for i in range(n):
            x1[i] = x0[i] - r[i]/ A[i][i]
        error = l2NormErr(b, matrixVectMult(A, x1))
        iter += 1
        for i in range(n):
            x0[i] = x1[i]
        if error < tol:
            return x1
    if iter ==  maxIter:
        print("no solution reached", x1)
        return "Maxiterations was reached. "
        



def main():
    #Note this is  random digaonally dominant matrix
    A = [ [3, -7, -2, 2],
        [-3, 5, 1, 0],
        [6, -4, 2, -5],
        [-9, 5, -5, 12]]
    # C = [[3, -2, 1],
    #         [1, -3, 2],
    #         [-1, 2, 4]]

    b = [-5, 5, -15, 35]
    
    print("A = ", A)
    print("b = ", b)
    x0 = [1 for j in range(len(b))]
    tol = 10
    maxiter = 10
    x = jacobiIteration(A, b, x0, tol, maxiter)
    print("The solution of Ax = b")
    print(x)


main()
