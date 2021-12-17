from random import randint

import sys
sys.path.insert(0, '../lib/')

from matrix.vecNorms import l2Norm
from matrix.vecOps import dotProd
from matrix.LUsolver import LUsolver




def diagonallyDominant():
    matrix = [[None for i in range(100)] for j in range(100)]
    for i in range(100):
        for j in range(100):
            if i == j:
                matrix[i][j] = randint(101, 200)
            else:
                matrix[i][j] = randint(-10, 10)
    return matrix


def powerMethodIinverse(matrix, x0, lmbd0, tol, maxiter): #lmbd0 refers to initial guess of the eigen value
    error  = tol +1
    for i in range(maxiter):
        y = LUsolver(matrix, x0)  # y = "A ^ -1  * x0"
        ## normal y
        euclid = l2Norm(y)
        for i in range(len(y)):
            y[i] = y[i]/ euclid
        v = y # v = y normalized
        q = LUsolver(matrix, v)         # this is the calcultion of matrix inverse times v.   OR "A -1" * v by solvign Aq = v
        lmbd1 = dotProd(v, q) # dotting v  and q    
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
    var = powerMethodIinverse(A, x0, lmbd, .1, 30)
    print("smallest eigen value = ", var)    
main()
