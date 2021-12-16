#Matrix operations


import sys
sys.path.insert(0, '../lib/')

from matrix.vecOps import dotProd

def matrixAdd(A, B):
    C = [[None for k in range(len(A[0]))] for j in range(len(A))]
    if len(A) != len(B):
        return "Error"
    for i in range(len(A)):
        for j in range(len(A[i])):
            C[i][j] = A[i][j] + B[i][j]
    return C

def matrixSub(A, B):
    C = [[None for k in range(len(A[0]))] for j in range(len(A))]
    if len(A) != len(B):
        return "Error"
    for i in range(len(A)):
        for j in range(len(A[i])):
            C[i][j] = A[i][j] - B[i][j]
    return C

def transpose(mtrx):
    # mtrxT = mtrx[:][:]
    mtrxT = [[None for j in range(len(mtrx))] for j in range(len(mtrx[0]))]
    # print(mtrxT)
    # size = len(mtrx)
    for i in range(len(mtrxT)):
        for j in range(len(mtrxT[0])):
            mtrxT[i][j] = mtrx[j][i]
    return mtrxT

def scalarMatrix(A, scalar):
    C = [[None for k in range(len(A[0]))] for j in range(len(A))]
    # print(C)
    for i in range(len(A)):
       for j in range(len(A[i])):
           C[i][j] = A[i][j] * scalar
    return C

def matrixVectMult(A, x):
    b = [None for i in range(len(A))]
    if len(A[0]) != len(x):
        return "Sizes don't match"
    else:
        for i in range(len(A)):
            b[i] = dotProd(A[i], x)
        return b

def matrixMult(A, B):
    C = [[None for k in range(len(A))] for j in range(len(B[0]))]
    if len(A[0]) != len(B):
        return "Incompatible matrix multiplication"
    else:
        col = [None for j in range(len(B))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(col)): # this gets a column from B
                    col[k] = B[k][j] 
                C[i][j] = dotProd(A[i], col)
        return C


