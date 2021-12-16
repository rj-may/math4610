import sys
sys.path.insert(0, '../lib/')

from matrix.vecNorms import l2Norm
from matrix.matrixOps import matrixVecMult
from matrix.vecOps import dotProd


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




