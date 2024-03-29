from random import randint

import numpy
import sys
sys.path.insert(0, '../lib/')

from matrix.vecNorms import l2Norm
from matrix.matrixOps import matrixVecMult
from matrix.vecOps import dotProd


def printMatrix(A):
    for line in A:
        print(line)


def diagonallyDominant():
    matrix = [[None for i in range(100)] for j in range(100)]
    for i in range(100):
        for j in range(100):
            if i == j:
                matrix[i][j] = randint(101, 200)
            else:
                matrix[i][j] = randint(-10, 10)
    return matrix


def powerMethod(matrix, x0, lmbd0, tol, maxiter): #lmbd0 refers to initial guess of the eigen value
    error  = tol +1
    for i in range(maxiter):
        y = matrixVecMult(matrix, x0)
        ## normal y
        euclid = l2Norm(y)
        for i in range(len(y)):
            y[i] = y[i]/ euclid
        v = y
        lmbd1 = dotProd(v, matrixVecMult(matrix, v))
        # print("lmd1 = ", lmbd1)
        error = abs(lmbd1 - lmbd0)
        lmbd0 = lmbd1
        x0 = v
        if error < tol:
            return lmbd0
    else:
        print("Max iterations were reached")
        return lmbd0




def main():
    A = diagonallyDominant()
    x0 = [1 for i in range(100)]
    lmbd = 2
    var = powerMethod(A, x0, lmbd, .1, 30)
    print("largest eigen value = ", var)    
main()
